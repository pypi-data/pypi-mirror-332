#!/usr/bin/env python3
"""
Loguru Throttler Demo Script

This script demonstrates various features of the loguru-throttler package:
1. Basic throttling
2. Advanced configuration with burst mode
3. Throttling with extra fields
4. Multiple sinks with different throttling configurations
"""

import sys
import time

from loguru import logger

from loguru_throttler import ThrottleSink, add_throttled_sink

# Clear any existing handlers
logger.remove()


def separator(title):
    """Print a separator with a title for better readability"""
    print("\n" + "=" * 80)
    print(f" {title} ".center(80, "="))
    print("=" * 80 + "\n")


# Example 1: Basic Throttling
separator("BASIC THROTTLING")
print("Adding a basic throttled sink with 5-second window")

# Add a basic throttled sink
logger.add(sys.stdout, filter=ThrottleSink(throttle_time=5), level="INFO")

print(
    "Sending 10 identical messages - only the first should appear, then wait 6 seconds..."
)
for i in range(10):
    logger.info("This is a throttled message (basic)")
    time.sleep(0.2)

print("\nWaiting 6 seconds for throttle window to expire...")
time.sleep(6)

print("\nSending the same message again - should appear once more")
logger.info("This is a throttled message (basic)")

# Remove the basic sink before moving to the next example
logger.remove()


# Example 2: Burst Mode
separator("BURST MODE")
print("Adding a throttled sink with burst mode (3 messages allowed in 5-second window)")

# Configure a sink with burst mode
burst_throttler = ThrottleSink(throttle_time=5, burst_limit=3, burst_window=5)
logger.add(sys.stdout, filter=burst_throttler, level="INFO")

print("Sending 10 identical messages - first 3 should appear within 5-second window")
for i in range(10):
    logger.info("This is a throttled message (burst mode)")
    time.sleep(0.2)

print("\nWaiting 6 seconds for throttle window to expire...")
time.sleep(6)

print("\nSending 2 more messages - should see them both (under burst limit)")
logger.info("This is a throttled message (burst mode)")
time.sleep(0.5)
logger.info("This is a throttled message (burst mode)")

# Remove the burst sink before moving to the next example
logger.remove()


# Example 3: Throttling with Extra Fields
separator("THROTTLING WITH EXTRA FIELDS")
print("Adding a throttled sink that includes extra fields in throttling decisions")

# Configure a sink that includes extra fields
extra_throttler = ThrottleSink(throttle_time=5, include_extra=True)
logger.add(sys.stdout, filter=extra_throttler, level="INFO")

print("Sending messages with different extra fields - should see both")
logger.bind(request_id="12345").info("Processing request")
logger.bind(request_id="67890").info("Processing request")

print(
    "\nSending duplicate messages with same extra fields - should see only first of each"
)
for i in range(3):
    logger.bind(request_id="12345").info("Processing request")
    time.sleep(0.2)

for i in range(3):
    logger.bind(request_id="67890").info("Processing request")
    time.sleep(0.2)

# Remove the extra fields sink before moving to the next example
logger.remove()


# Example 4: Multiple Sinks with Different Configurations
separator("MULTIPLE SINKS WITH DIFFERENT CONFIGURATIONS")
print("Adding multiple sinks with different throttling configurations")

# Add a sink with short throttle time
logger.add(
    sys.stdout,
    filter=ThrottleSink(throttle_time=3),
    level="INFO",
    format="<blue>{time}</blue> | <level>{level}</level> | <cyan>SINK 1 (3s)</cyan> | <level>{message}</level>",
)

# Add another sink with longer throttle time
logger.add(
    sys.stdout,
    filter=ThrottleSink(throttle_time=10),
    level="INFO",
    format="<blue>{time}</blue> | <level>{level}</level> | <green>SINK 2 (10s)</green> | <level>{message}</level>",
)

print(
    "Sending messages every 4 seconds - should appear once in SINK 1 every 3s, once in SINK 2 every 10s"
)
for i in range(4):
    logger.info(f"Multi-sink message #{i + 1}")
    time.sleep(4)

# Example 5: Using the helper function
separator("USING THE HELPER FUNCTION")
print("Using add_throttled_sink helper function to create a file sink")

# Remove previous sinks
logger.remove()

# Create a file with throttled logging
add_throttled_sink(
    logger, "throttled_output.log", throttle_time=5, level="DEBUG", rotation="1 MB"
)

# Also add console output for demonstration
logger.add(sys.stdout, level="INFO")

print("Sending debug messages to file with throttling")
for i in range(5):
    logger.debug(f"This debug message #{i + 1} is throttled in the file")
    logger.info(
        f"Console message #{i + 1} (check throttled_output.log for debug messages)"
    )
    time.sleep(1)

print("\nDemo completed! Check throttled_output.log for file output.")
