import os
import gazu
import sys
import argparse
import time
import traceback
import pathlib
from datetime import datetime, timedelta

from kabaret import flow
from libreflow.session import BaseCLISession


def prefix_log():
    return f"[KITSU REQUEST FETCH - {datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')}]"


class KitsuRequestSession(BaseCLISession):

    def init_variables(self, project_name, make_request):
        # Kitsu
        self.kitsu_config = self.cmds.Flow.call(f"/{project_name}", 'kitsu_config', [], {})
        self.kitsu_api = self.cmds.Flow.call(f"/{project_name}", 'kitsu_api', [], {})
        
        # Exchange - Minio
        exchange_site = self.cmds.Flow.call(f"/{project_name}", 'get_exchange_site', [], {})
        self.bucket_name = exchange_site.bucket_name.get()
        self.minio_client = exchange_site.sync_manager._ensure_client()
        
        # For revisions
        entity_manager = self.cmds.Flow.call(f"/{project_name}", 'get_entity_manager', [], {})
        self.rev_col = entity_manager.get_revision_collection()
        
        self.root_path = self.cmds.Flow.call(f"/{project_name}", 'get_root', [], {})
        self.working_site = self.cmds.Flow.call(f"/{project_name}", 'get_current_site', [], {})
        self.user_name = self.cmds.Flow.call(f"/{project_name}", 'get_user_name', [], {})
        
        self.make_request = make_request

    def kitsu_login(self):
        login = os.environ.get('KITSU_LOGIN', None)
        password = os.environ.get('KITSU_PASSWORD', None)

        if login or password is None:
            self.log_error((f'{prefix_log()} Make sure KITSU_LOGIN and KITSU_PASSWORD env variables are set up.'))
            return False

        gazu.client.set_host(f"{self.kitsu_config.server_url.get()}/api")
        try:
            gazu.log_in(login, password)
        except (
            gazu.exception.AuthFailedException,
            gazu.exception.ServerErrorException,
        ):
            return False
        else:
            return True

    def get_kitsu_shots(self):
        shots_list = []

        kitsu_project = gazu.project.get_project_by_name(self.kitsu_config.project_name.get())
        task_type = gazu.task.get_task_type_by_name('Shots_Rendering')
        task_status = gazu.task.get_task_status_by_short_name('ADA')

        tasks = gazu.task.all_tasks_for_task_status(kitsu_project, task_type, task_status)
        shot_entities = [gazu.entity.get_entity(task_entity["entity_id"]) for task_entity in tasks]
        for entity in shot_entities:
            shot_name = entity['name']
            sequence_entity = gazu.shot.get_sequence_from_shot(entity)
            if sequence_entity:
                sequence_name = sequence_entity['name']
                shots_list.append([sequence_name, shot_name])

        return shots_list

    def get_file_size(self, path):
        if os.path.isfile(path):
            return os.path.getsize(path)
        else:
            path = pathlib.Path(path)
            return sum(f.stat().st_size for f in path.glob('**/*') if f.is_file())

    def get_server_path(self, path):
        '''
        Returns the path of the associated object on the server.
        '''

        if os.path.splitext(path)[1] == '':
            path += '/' + os.path.basename(path) + '.zip'
        
        return path

    def get_revision(self, oid):
        query = (
            self.rev_col.get_entity_store()
            .get_collection(self.rev_col.collection_name())
            .find({"name": {"$regex": oid}, "site": self.working_site.name(), "working_copy": False})
            .sort({"date": -1}).limit(1)
        )
        query = list(query)
        return query[0] if len(query) > 0 else None

    def check_minio_object(self, path):
        # Check if object exists
        response = None
        try:
            response = self.minio_client.stat_object(self.bucket_name, path)
        except:
            return None
        finally:
            return response

    def check_exchange_status(self, oids):
        revision_oids = []

        for oid in oids:
            revision = self.get_revision(oid)
            server_path = self.get_server_path(revision['path'])
            minio_object = self.check_minio_object(server_path)
            
            if minio_object:
                # Specific for passes folder
                if 'passes' in oid and minio_object.size < 2000000: # Under 2mb
                    # Upload
                    revision_oids.append(revision['name'])
            else:
                # Upload
                revision_oids.append(revision['name'])
        
        return revision_oids

    def upload_revision(self, oid):
        rev = self.get_actor('Flow').get_object(oid)

        file_path = os.path.normpath(os.path.join(
            self.root_path,
            rev.path.get()
        ))
        size_value = self.get_file_size(file_path)
        rev.file_size.set(size_value)

        # Add an upload job for the current site
        # Handled by auto-sync
        job = self.working_site.get_queue().submit_job(
            job_type='Upload',
            init_status='WAITING',
            emitter_oid=rev.oid(),
            user=self.user_name,
            studio=self.working_site.name(),
        )

        if self.make_request:
            request_action = rev.request_as
            request_action.sites.target_site.set("dca")
            request_action.sites.source_site.set("lfs")
            request_action.run(None)

    def process_shots(self, shots_list):
        self.log_info(f'{prefix_log()} Checking {len(shots_list)} shots')
        for s in shots_list:
            seq = s[0]
            shot = s[1]
            base_oid = f"/anpo/films/anpo/sequences/{seq}/shots/{shot}/tasks/comp/files"

            # After Effects file and passes folder
            file_oids = [
                f"{base_oid}/compositing_aep",
                f"{base_oid}/passes"
            ]

            revision_oids = self.check_exchange_status(file_oids)
            
            if len(revision_oids) > 0:
                # Create upload jobs
                for rev_oid in revision_oids:
                    self.upload_revision(rev_oid)
            else:
                # Update kitsu status to DONE
                self.log_info(f'{prefix_log()} Update kitsu status - {seq} {shot}')
                self.kitsu_api.set_shot_task_status(seq, shot, 'Shots_Rendering', 'Done', 'Files are ready to download')


def parse_remaining_args(args):
    parser = argparse.ArgumentParser(
        description='Libreflow Kitsu Request Fetch Arguments'
    )
    parser.add_argument(
        '-s', '--site', default='lfs', dest='site'
    )
    parser.add_argument(
        '-p', '--project', dest='project',
    )
    parser.add_argument(
        '-f', '--fetch-period', dest='period', default=0,
    )
    parser.add_argument(
        '-m', '--make-request', dest='make_request', default=False, action='store_true'
    )
    values, _ = parser.parse_known_args(args)

    if values.site:
        os.environ["KABARET_SITE_NAME"] = values.site

    return (
        values.project,
        float(values.period),
        values.make_request
    )

def main(argv):
    (
        session_name,
        host,
        port,
        cluster_name,
        db,
        password,
        debug,
        read_replica_host,
        read_replica_port,
        remaining_args,
    ) = KitsuRequestSession.parse_command_line_args(argv)
    (
        project_name,
        period,
        make_request
    ) = parse_remaining_args(remaining_args)

    session = KitsuRequestSession(session_name=session_name, debug=debug)
    session.cmds.Cluster.connect(host, port, cluster_name, db, password, read_replica_host, read_replica_port)

    session.init_variables(project_name, make_request)

    TASK_COMPLETED = False
    while (TASK_COMPLETED is False):
        try:
            session.log_info(f'{prefix_log()} Fetching {project_name} started')

            # Login to Kitsu
            logged = session.kitsu_login()

            if logged:
                session.log_info(f'{prefix_log()} Kitsu connected')

                # Fetch ADA Rendering kitsu shots
                shots_list = session.get_kitsu_shots()
                
                # Process shots list
                session.process_shots(shots_list)

            session.log_info(f'{prefix_log()} Fetching {project_name} completed')

            # Execute only once if no period argument
            if period == 0:
                TASK_COMPLETED = True
                return
            
            # Schedule next indexing
            schedule_date = datetime.now() + timedelta(seconds=period)
            session.log_info(
                f"{prefix_log()} Next request fetching scheduled at {schedule_date.strftime('%Y-%m-%d %H:%M:%S')}"
            )
            time.sleep(period)
        except (Exception, KeyboardInterrupt) as e:
            if isinstance(e, KeyboardInterrupt):
                session.log_info(f'{prefix_log()} Fetching {project_name} manually stopped')
                break
            else:
                session.log_error(f"{prefix_log()} The following error occurred:")
                session.log_error(traceback.format_exc())
                session.log_error(f"{prefix_log()} Restart fetching...")
    
    session.close()


if __name__ == "__main__":
    main(sys.argv[1:])
