# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Support for P-Touch series files in the `analyze` subcommand
- Initial Support for the PT-P750W printer
- Initial Support for the PT-P950NW printer [matmair/brother_ql-inventree #6](https://github.com/matmair/brother_ql-inventree/pull/6), [matmair/brother_ql-inventree #21](https://github.com/matmair/brother_ql-inventree/pull/21)
- A `status` subcommand to query the printer status
- Optional json output for the `info labels` and `info models` subcommands

### Removed
- Deprecation Warning

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
