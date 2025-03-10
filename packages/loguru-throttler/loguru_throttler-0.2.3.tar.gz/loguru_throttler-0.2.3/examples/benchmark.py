#!/usr/bin/env python3
"""
Loguru Throttler Performance Benchmark

This script measures the performance overhead of using loguru-throttler
compared to standard loguru logging.
"""

import statistics
import sys
import time

from loguru import logger

from loguru_throttler import ThrottleSink

# Clear any existing handlers
logger.remove()

# Disable actual writing to files for benchmark
null_sink = open("/dev/null", "w") if sys.platform != "win32" else open("NUL", "w")


def benchmark_standard_logging(iterations=10000):
    """Benchmark standard loguru logging without throttling"""
    # Setup standard logger
    logger.remove()
    handler_id = logger.add(null_sink, level="INFO")

    start_time = time.time()

    # Log messages
    for i in range(iterations):
        logger.info(f"Standard log message {i}")

    elapsed = time.time() - start_time

    # Clean up
    logger.remove(handler_id)

    return elapsed


def benchmark_throttled_logging(iterations=10000, unique_messages=False):
    """Benchmark loguru logging with throttling"""
    # Setup throttled logger
    logger.remove()
    throttler = ThrottleSink(throttle_time=1)
    handler_id = logger.add(null_sink, filter=throttler, level="INFO")

    start_time = time.time()

    # Log messages (either all the same or all unique)
    if unique_messages:
        for i in range(iterations):
            logger.info(f"Unique throttled message {i}")
    else:
        for i in range(iterations):
            logger.info("Same throttled message")

    elapsed = time.time() - start_time

    # Clean up
    logger.remove(handler_id)

    return elapsed


def benchmark_throttled_with_extra(iterations=10000):
    """Benchmark loguru logging with throttling and extra fields"""
    # Setup throttled logger with extra fields
    logger.remove()
    throttler = ThrottleSink(throttle_time=1, include_extra=True)
    handler_id = logger.add(null_sink, filter=throttler, level="INFO")

    start_time = time.time()

    # Log messages with extra fields
    for i in range(iterations):
        logger.bind(request_id=i % 100).info("Throttled message with extra fields")

    elapsed = time.time() - start_time

    # Clean up
    logger.remove(handler_id)

    return elapsed


def run_benchmarks(iterations=10000, runs=5):
    """Run all benchmarks multiple times and report results"""
    print(f"Running benchmarks with {iterations} log messages, {runs} runs each...")

    results = {
        "Standard Logging": [],
        "Throttled (Same Message)": [],
        "Throttled (Unique Messages)": [],
        "Throttled with Extra Fields": [],
    }

    for i in range(runs):
        print(f"Run {i + 1}/{runs}...")

        results["Standard Logging"].append(benchmark_standard_logging(iterations))
        results["Throttled (Same Message)"].append(
            benchmark_throttled_logging(iterations, False)
        )
        results["Throttled (Unique Messages)"].append(
            benchmark_throttled_logging(iterations, True)
        )
        results["Throttled with Extra Fields"].append(
            benchmark_throttled_with_extra(iterations)
        )

    # Print results
    print("\nBenchmark Results:")
    print(f"{'Test':<30} | {'Time (s)':<10} | {'Msgs/sec':<10} | {'Overhead':<10}")
    print("-" * 65)

    baseline = statistics.mean(results["Standard Logging"])

    for test, times in results.items():
        avg_time = statistics.mean(times)
        msgs_per_sec = iterations / avg_time
        overhead = ((avg_time / baseline) - 1) * 100  # percentage overhead

        print(
            f"{test:<30} | {avg_time:<10.4f} | {msgs_per_sec:<10.0f} | {overhead:>9.2f}%"
        )

    print("\nNote: Overhead is relative to standard logging without throttling")


if __name__ == "__main__":
    # Use a smaller number for slower machines
    run_benchmarks(iterations=50000, runs=3)
