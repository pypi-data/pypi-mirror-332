# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html)[^1].

<!---
Types of changes

- Added for new features.
- Changed for changes in existing functionality.
- Deprecated for soon-to-be removed features.
- Removed for now removed features.
- Fixed for any bug fixes.
- Security in case of vulnerabilities.

-->

## [Unreleased]

## [1.1.0] - 2025-03-07

### Added

* A CLI session to request compositing files from Kitsu 
    * When a shot's rendering task is in ADA status, the session will create upload jobs for the latest revision of the After Effects file and passes folder.
    * As soon as these files are available on the exchange server, the status of the rendering task will be updated to "Done".

## [1.0.1] - 2024-05-15

### Fixed

* versioneer dependency for pip install was added

## [1.0.0] - 2024-05-15

### Added

* initial release : this overrides the actions which create assets from Kitsu
