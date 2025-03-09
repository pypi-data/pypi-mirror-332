# Loguru Throttler

[![PyPI version](https://img.shields.io/pypi/v/loguru-throttler.svg)](https://pypi.org/project/loguru-throttler/)
[![Python Versions](https://img.shields.io/pypi/pyversions/loguru-throttler.svg)](https://pypi.org/project/loguru-throttler/)
[![License](https://img.shields.io/github/license/acadiancapitalpartners/loguru-throttler.svg)](https://github.com/acadiancapitalpartners/loguru-throttler/blob/main/LICENSE)
[![Build Status](https://github.com/acadiancapitalpartners/loguru-throttler/actions/workflows/python-package.yml/badge.svg)](https://github.com/acadiancapitalpartners/loguru-throttler/actions)


A Python package that provides message throttling capabilities for the [loguru](https://github.com/Delgan/loguru) logging library.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Requirements](#requirements)
- [Usage](#usage)
  - [Basic Usage](#basic-usage)
  - [Advanced Configuration](#advanced-configuration)
  - [Burst Mode](#burst-mode)
- [Examples](#examples)
- [How It Works](#how-it-works)
- [Performance](#performance)
- [Future Enhancements](#future-enhancements)
- [Development](#development)
  - [Setup](#setup)
  - [Running Tests](#running-tests)
  - [Building the Package](#building-the-package)
  - [Windows Development](#windows-development)
- [License](#license)

## Features

- Throttle duplicate log messages on a per-sink, per-level, and per-message basis
- Configurable time window for suppression
- Burst mode to allow a specified number of messages before throttling
- Option to include extra fields in throttling decisions
- Thread-safe operation
- Minimal performance overhead
- Easy integration with existing loguru sinks

## Installation

```bash
pip install loguru-throttler
```

## Requirements

- Python 3.9 or higher
- loguru

## Usage

### Basic Usage

```python
from loguru import logger
from loguru_throttler import ThrottleSink

# Add a throttled sink with a 30-second window
logger.add("file.log", filter=ThrottleSink(throttle_time=30), level="INFO")

# Or use the helper function
from loguru_throttler import add_throttled_sink
add_throttled_sink(logger, "output.log", throttle_time=60, level="DEBUG")

# Now identical log messages will be throttled
for _ in range(100):
    logger.info("This message will only appear once per 30 seconds")
```

### Advanced Configuration

```python
from loguru_throttler import ThrottleSink

# Custom throttling configuration
throttler = ThrottleSink(
    throttle_time=120,       # 2 minutes
    max_cache_size=1000,     # Limit memory usage
    burst_limit=3,           # Allow 3 messages before throttling
    burst_window=60,         # Reset burst counter after 60 seconds
    include_extra=True       # Include extra fields in throttling decisions
)

# Add to logger
logger.add("app.log", filter=throttler, level="INFO")

# Messages with different extra fields are treated as different messages
logger.bind(request_id="12345").info("Processing request")
logger.bind(request_id="67890").info("Processing request")  # Not throttled (different request_id)
```

### Burst Mode

Burst mode allows a specified number of messages to pass through before throttling kicks in:

```python
from loguru_throttler import ThrottleSink

# Allow 5 messages within a 30-second window before throttling
burst_throttler = ThrottleSink(
    throttle_time=30,
    burst_limit=5,
    burst_window=30
)

logger.add(sys.stdout, filter=burst_throttler, level="INFO")

# The first 5 identical messages will be logged, then throttling begins
for i in range(10):
    logger.info("This message will appear 5 times before being throttled")
```

## Examples

Check out the [examples directory](examples/) for comprehensive demonstrations:

1. **Core Features Demo** ([throttler_demo.py](examples/throttler_demo.py)): Demonstrates all core features with clear examples
2. **API Client Simulation** ([advanced_example.py](examples/advanced_example.py)): A realistic use case with API rate limiting
3. **Custom Throttling Strategy** ([custom_throttling.py](examples/custom_throttling.py)): Advanced customization with level-based rules
4. **Performance Benchmark** ([benchmark.py](examples/benchmark.py)): Measure the performance impact of throttling

Run any example with:

```bash
python examples/throttler_demo.py
```

## How It Works

The throttler works by:
1. Intercepting log messages
2. Computing a hash based on message content, log level, and optionally extra fields
3. Checking if an identical message was logged within the throttle window
4. Applying burst mode rules if configured
5. Suppressing duplicate messages or forwarding unique ones to the sink

## Performance

The throttling mechanism adds minimal overhead (<10%) to logging operations while effectively reducing log volume for repetitive messages. See the [benchmark example](examples/benchmark.py) for detailed performance metrics.

## Future Enhancements

The following features are planned for upcoming releases:

### v0.3.0 (Planned)
- **Custom Throttling Keys**: Allow users to provide custom functions for generating throttling keys
- **Throttling Statistics**: Track and report how many messages were throttled
- **Throttling Notifications**: Option to log a summary message when throttling occurs (e.g., "Suppressed 42 similar messages in the last 60 seconds")

### v0.4.0 (Planned)
- **Pattern-Based Throttling**: Allow throttling based on regex patterns rather than exact message matches
- **Adaptive Throttling**: Automatically adjust throttle windows based on message frequency
- **Sink-Specific Configuration**: Support different throttling rules for different sinks

### Future Considerations
- **Message Aggregation**: Combine similar messages into aggregated summaries
- **Distributed Throttling**: Support for throttling across multiple processes or servers
- **Configuration via Environment Variables**: Allow configuration through environment variables

## Development

### Setup

Clone the repository and install development dependencies:

```bash
# Install in development mode
pip install -e .
pip install -r requirements-dev.txt
```

### Running Tests

```bash
# Using pytest directly
pytest tests/ --cov=loguru_throttler

# Or using the build tools
python build_tools.py test
```

### Building the Package

You can use either the Makefile (Unix/Linux/macOS) or the cross-platform build script:

#### Using Makefile (Unix/Linux/macOS)

```bash
# Build the package
make build

# Run tests
make test

# Format code
make format

# Run linting
make lint
```

#### Using build_tools.py (Cross-platform)

```bash
# Build the package
python build_tools.py build

# Run tests
python build_tools.py test

# Format code
python build_tools.py format

# Run linting
python build_tools.py lint
```

### Windows Development

When developing on Windows, be aware that files and directories starting with a dot (like `.github` or `.gitignore`) require special handling. A helper script is provided:

```bash
# Create or update GitHub templates and workflows
python create_github_templates.py
```

For more details, see the [Contributing Guide](CONTRIBUTING.md).

## License

MIT
