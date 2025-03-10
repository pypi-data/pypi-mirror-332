"""
Performance benchmark for loguru-throttler.

This script measures the overhead introduced by the throttling mechanism
compared to standard loguru logging.
"""

import os
import sys
import tempfile
import time

from loguru import logger

from loguru_throttler import add_throttled_sink


def run_benchmark(iterations=10000):
    """Run a performance benchmark."""
    # Create temporary files for output
    standard_file = tempfile.NamedTemporaryFile(delete=False)
    throttled_file = tempfile.NamedTemporaryFile(delete=False)
    standard_file.close()
    throttled_file.close()

    try:
        # Remove default logger
        logger.remove()

        # Setup standard logger
        standard_logger = logger.bind(benchmark="standard")
        standard_sink_id = standard_logger.add(standard_file.name, level="INFO")

        # Setup throttled logger
        throttled_logger = logger.bind(benchmark="throttled")
        throttled_sink_id = add_throttled_sink(
            throttled_logger, throttled_file.name, throttle_time=60, level="INFO"
        )

        # Benchmark standard logging
        print("Benchmarking standard logging...")
        start_time = time.time()
        for i in range(iterations):
            # Mix of unique and duplicate messages
            if i % 10 == 0:
                standard_logger.info(f"Unique message {i}")
            else:
                standard_logger.info("Duplicate message")
        standard_duration = time.time() - start_time

        # Benchmark throttled logging
        print("Benchmarking throttled logging...")
        start_time = time.time()
        for i in range(iterations):
            # Mix of unique and duplicate messages
            if i % 10 == 0:
                throttled_logger.info(f"Unique message {i}")
            else:
                throttled_logger.info("Duplicate message")
        throttled_duration = time.time() - start_time

        # Calculate overhead
        overhead_percent = ((throttled_duration / standard_duration) - 1) * 100

        # Print results
        print("\nBenchmark Results:")
        print(f"Iterations: {iterations}")
        print(f"Standard logging time: {standard_duration:.4f} seconds")
        print(f"Throttled logging time: {throttled_duration:.4f} seconds")
        print(f"Throttling overhead: {overhead_percent:.2f}%")

        # Check file sizes to see throttling effect
        standard_size = os.path.getsize(standard_file.name)
        throttled_size = os.path.getsize(throttled_file.name)
        size_reduction = ((standard_size - throttled_size) / standard_size) * 100

        print("\nLog Size Comparison:")
        print(f"Standard log size: {standard_size} bytes")
        print(f"Throttled log size: {throttled_size} bytes")
        print(f"Size reduction: {size_reduction:.2f}%")

        # Clean up
        logger.remove(standard_sink_id)
        logger.remove(throttled_sink_id)

    finally:
        # Remove temporary files
        for file_path in [standard_file.name, throttled_file.name]:
            if os.path.exists(file_path):
                os.unlink(file_path)


if __name__ == "__main__":
    # Run with default 10,000 iterations or custom from command line
    iterations = int(sys.argv[1]) if len(sys.argv) > 1 else 10000
    run_benchmark(iterations)
