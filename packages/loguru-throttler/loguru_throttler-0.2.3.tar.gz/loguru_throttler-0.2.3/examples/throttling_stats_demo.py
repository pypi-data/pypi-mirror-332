#!/usr/bin/env python3
"""
Throttling Statistics Demo

This example demonstrates the throttling statistics and reporting features
of the loguru-throttler package.
"""

import sys
import time

from loguru import logger

from loguru_throttler import ThrottleSink


def main():
    """Run the throttling statistics demonstration."""
    # Remove default logger
    logger.remove()

    print("=== Throttling Statistics Demo ===\n")

    # Example 1: Basic statistics reporting
    print("\n=== Example 1: Automatic Statistics Reporting ===")

    # Configure a throttler with statistics reporting enabled
    # Use a short report interval for the demo
    throttler = ThrottleSink(
        throttle_time=2,  # 2 seconds throttle window
        report_stats=True,  # Enable statistics reporting
        report_interval=5,  # Report every 5 seconds
    )

    # Add a console sink with the throttler
    logger.add(
        sys.stdout,
        format="<green>{time:HH:mm:ss}</green> | <level>{level: <8}</level> | <level>{message}</level>",
        filter=throttler,
        level="INFO",
    )

    print("Generating duplicate messages (automatic reporting)...")
    print("Watch for the statistics summary every 5 seconds:")

    # Generate duplicate messages for 15 seconds
    start_time = time.time()
    while time.time() - start_time < 15:
        # Log the same message repeatedly
        logger.info("This is a duplicate message that will be throttled")

        # Log another message less frequently
        if int(time.time()) % 3 == 0:
            logger.warning("This is another message that will be throttled")

        time.sleep(0.1)

    # Remove the sink before moving to the next example
    logger.remove()
    print("\nExample 1 completed.")

    # Example 2: Manual statistics retrieval
    print("\n=== Example 2: Manual Statistics Retrieval ===")

    # Configure a new throttler without automatic reporting
    manual_throttler = ThrottleSink(
        throttle_time=1,  # 1 second throttle window
        report_stats=False,  # Disable automatic reporting
    )

    # Add a console sink with the throttler
    sink_id = logger.add(
        sys.stdout,
        format="<blue>{time:HH:mm:ss}</blue> | <level>{level: <8}</level> | <level>{message}</level>",
        filter=manual_throttler,
        level="INFO",
    )

    print("Generating duplicate messages (manual statistics)...")

    # Generate duplicate messages for 5 seconds
    start_time = time.time()
    while time.time() - start_time < 5:
        # Log different messages with different frequencies
        logger.info("First type of duplicate message")

        if int(time.time() * 10) % 5 == 0:
            logger.warning("Second type of duplicate message")

        if int(time.time() * 10) % 20 == 0:
            logger.error("Third type of duplicate message")

        time.sleep(0.1)

    # Retrieve and display statistics manually
    stats = manual_throttler.get_statistics()

    print("\nManually retrieved throttling statistics:")
    print(f"Total throttled messages: {stats['total_throttled']}")
    print("Throttled message counts:")

    for message, count in stats["throttled_messages"].items():
        print(f"  - '{message}': {count} times")

    print(f"Current cache size: {stats['cache_size']}")
    print(f"Throttle time: {stats['throttle_time']} seconds")

    # Remove the sink
    logger.remove(sink_id)
    print("\nExample 2 completed.")

    # Example 3: Different throttle and report intervals
    print("\n=== Example 3: Custom Reporting Intervals ===")

    # Configure a throttler with custom intervals
    custom_throttler = ThrottleSink(
        throttle_time=3,  # 3 seconds throttle window
        report_stats=True,  # Enable statistics reporting
        report_interval=8,  # Report every 8 seconds
    )

    # Add a console sink with the throttler
    logger.add(
        sys.stdout,
        format="<yellow>{time:HH:mm:ss}</yellow> | <level>{level: <8}</level> | <level>{message}</level>",
        filter=custom_throttler,
        level="INFO",
    )

    print("Generating messages with different patterns...")
    print("Watch for the statistics summary after 8 seconds:")

    # Generate messages with a pattern for 10 seconds
    start_time = time.time()
    while time.time() - start_time < 10:
        # Create a pattern of message bursts
        current_second = int(time.time()) % 10

        if current_second < 3:
            # Burst of type A messages
            logger.info("Type A message - high frequency")
        elif current_second < 6:
            # Burst of type B messages
            logger.warning("Type B message - medium frequency")
        else:
            # Burst of type C messages
            logger.error("Type C message - low frequency")

        time.sleep(0.1)

    # Wait for the final report
    print("\nWaiting for final statistics report...")
    time.sleep(3)

    # Clean up
    logger.remove()
    print("\nExample 3 completed.")

    print("\n=== Throttling Statistics Demo Completed ===")


if __name__ == "__main__":
    main()
