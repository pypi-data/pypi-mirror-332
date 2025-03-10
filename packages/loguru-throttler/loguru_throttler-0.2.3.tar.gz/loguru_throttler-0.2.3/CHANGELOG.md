# Changelog

All notable changes to the loguru-throttler project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.2.3] - 2024-03-09

### Added
- Throttling statistics tracking and reporting functionality
- New `report_stats` parameter to enable/disable statistics reporting
- New `report_interval` parameter to control how often statistics are reported
- New `get_statistics()` method to retrieve current throttling statistics
- Automatic summary logs showing suppressed message counts

## [0.2.2] - 2024-03-08

### Fixed
- Updated GitHub Actions workflow badge in README.md to correctly point to the Python Package workflow

## [0.2.1] - 2024-03-08

### Added
- Burst mode support to allow a specified number of messages before throttling begins
- Option to include extra fields in throttling decisions
- New example demonstrating burst mode and extra fields inclusion
- Additional unit tests for new features

### Changed
- Improved message hashing to optionally include extra fields
- Updated documentation with new features and examples
- Cross-platform build tools for Windows/Linux/macOS compatibility

## [0.1.0] - 2024-03-08

### Added
- Initial release
- Basic message throttling functionality
- Thread-safe operation with minimal overhead
- LRU cache for bounded memory usage
- Helper function for easy integration with loguru
- Comprehensive test suite
- Cross-platform compatibility
