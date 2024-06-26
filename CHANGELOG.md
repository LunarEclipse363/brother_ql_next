# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.11.1] - 2024-06-26
### Added
- Changed package name to `brother_ql_next` for PyPi release
- Support for Python 3.9+ (previously 3.10+)

## [0.11.0] - 2024-06-26

### Added
- A `status` subcommand to query the printer status
- Optional json output for the `info labels` and `info models` subcommands

### Fixed
- The backend and other global options are now properly set to their default values
- The driver now ensures the minimum and maximum label lengths for every printer are respected
- Commands now use the new API and no longer show a deprecation warning for the devicedependent module

### Removed
- `devicedependent` module

## [0.10.0] - 2023-11-12

### Added
- The Changelog
- Features from `matmair/brother_ql-inventree` version `1.0`
- A GitHub release action
- Support for the QL-600 printer [matmair/brother_ql-inventree #17](https://github.com/matmair/brother_ql-inventree/pull/17)
- Support for the QL-1100, QL-1100NWB and QL-1115NWB printers [matmair/brother_ql-inventree #18](https://github.com/matmair/brother_ql-inventree/pull/18)
- Support for 103mm labels (DK-11247, DK22246) [matmair/brother_ql-inventree #18](https://github.com/matmair/brother_ql-inventree/pull/18)
- Support for 54x29mm (DK-3235) labels [matmair/brother_ql-inventree #19](https://github.com/matmair/brother_ql-inventree/pull/19)
- Support for 60x87mm (DK-1234) labels [matmair/brother_ql-inventree #22](https://github.com/matmair/brother_ql-inventree/pull/22)

### Changed
- Compared to the `matmair/brother_ql-inventree` fork, this one keeps going from 0.10 instead of creating a 1.0 release

### Fixed
- Removed duplicated 103mm label - the "104" label - [matmair/brother_ql-inventree #20](https://github.com/matmair/brother_ql-inventree/pull/20)
- Use 400 byte invalidate command for QL-8xx models - [matmair/brother_ql-inventree #26](https://github.com/matmair/brother_ql-inventree/pull/26)
