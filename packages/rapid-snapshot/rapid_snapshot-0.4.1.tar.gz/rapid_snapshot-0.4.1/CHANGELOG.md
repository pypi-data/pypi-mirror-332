# Changelog

All notable changes to this project will be documented in this file.

## v0.3.3 - 2025-01-24
### Fixed
- Fixed implementation failures with CLI logging

## v0.3.2 - 2025-01-10
### Added
- Added more traces for developer logs
- Added version and time taken to output file so speed validation can be supported via logs

### Fixed
- Fixed issues with architecture not being filtered out resulting in more requests than required

## v0.3.1 - 2024-12-19
### Added
- Implemented full edge node cases for HIL and VIL environments

### Fixed
- Fixed issues with edge nodes hanging onto TCP connection
- Fixed TCP Socket remaining open through manual RST packets

## v0.3.0 - 2024-12-02
### Added
- `--update <VERSION>` to the command line arguments to allow users to self-update code. The available versions are listed in the GitLab Repo Package Registry.
- Management for Edge Nodes and support for Doip Gateway activation prior to Edge Node snapshot.

### Changed
- Refactored the doip testing sequence and process.

### Fixed
- Made execution more consistent following the Doip Gateway activation process.
- Fixed Entity management.

## v0.2.2 - 2024-11-27
### Added
- New CLI argument for adding delay between requests. (#11)

### Changed
- Removed raw from snapshot output for cleanliness.

### Fixed
- Timeout early return.

## v0.2.1 - 2024-11-27

### Changed
- Moved parser to separate process outside of read.
- Added short aliases for commands, use `--help` for more info.

### Fixed
- Setting empty path killed execution.
- No longer hanging, after DoIP not available.

## v0.2.0 - 2024-11-26
### Added
- Custom path command line argument for custom ECU and DID reading. (#7)

`C:\rapid_snapshot_tool.exe --custom-path "static/example-input.json"`

### Changed
- Improved command line argument passing to allow for combining arguments.

`C:\rapid_snapshot_tool.exe --log-level max --custom-path "static/example-input.json"`

### Deprecated
- Deprecated support for older command line.

`C:\rapid_snapshot_tool.exe log-level max`

## v0.1.3 - 2024-11-25
Adds the implementation of architecture mapping to the ECUs and includes the addition of all EVA2 and EVA25 ECUs. ECUs now have DIDs within the ECU struct:

```rust
pub struct SnapshotEcu {
    pub name: &'static str,
    pub acronym: &'static str,
    pub address: [u8; 2],
    pub architecture: &'static [JlrArchitecture],
    pub dids: Vec<Did>,
}
```

This means changing the execution method to go by each did in an ECU. This opens the project up for an accepted feature request to add custom DIDs per ECU.

### Added
- Vehicle Architecture Distinctions (#3)

### Changed
- Begun adding in execution changes for custom ECU + DID input

## v0.1.2 - 2024-11-XX

## v0.1.1 - 2024-11-20
Added command line argument passing with log-level as the first example, this will gateway feature flags for future feature requests.
With log-level you must specify one of the following:

- Off
- Trace
- Debug
- Info
- Warn
- Error
- Max

This will then run the internal logs at this log level logging anything with that severity and above.
Help with the command line can be found by using rapid_snapshot.exe --help to get all available commands.

### Added
- Command Line Argument support (#1)

### Changed
- Change CI pipeline to only build on default branch


## [TEMPLATE] - DATE (YYYY-MM-DD)
### Added
- Implemented user authentication with JWT.
- Added a user profile page with the ability to update personal information.
- Introduced email notifications for account updates.

### Changed
- Updated the user dashboard UI for a more intuitive layout.
- Refactored user settings page for better performance.

### Fixed
- Resolved a bug where password reset link expired prematurely.
- Fixed broken image links on the homepage.

### Deprecated
- Deprecated support for Internet Explorer 11.
