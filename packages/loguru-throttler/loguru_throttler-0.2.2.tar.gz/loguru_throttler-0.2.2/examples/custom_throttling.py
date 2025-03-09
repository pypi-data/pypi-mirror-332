#!/usr/bin/env python3
"""
Custom Throttling Strategy Example

This script demonstrates how to implement a custom throttling strategy
that applies different throttling rules based on log level and message content.
"""

import random
import sys
import time

from loguru import logger

from loguru_throttler import ThrottleSink


class SmartThrottleSink:
    """
    A custom throttling sink that applies different throttling rules
    based on log level and message content.

    Features:
    - Critical logs are never throttled
    - Error logs use burst mode (allow 3 before throttling)
    - Warning logs are throttled based on prefix patterns
    - Info logs are aggressively throttled
    - Debug logs are extremely throttled
    """

    def __init__(self):
        # Create different throttlers for different levels
        self.critical_throttler = None  # Never throttle critical logs

        self.error_throttler = ThrottleSink(
            throttle_time=30, burst_limit=3, burst_window=60, include_extra=True
        )

        self.warning_throttler = ThrottleSink(throttle_time=60, include_extra=False)

        self.info_throttler = ThrottleSink(
            throttle_time=300, max_cache_size=100  # 5 minutes
        )

        self.debug_throttler = ThrottleSink(
            throttle_time=600, max_cache_size=50  # 10 minutes
        )

        # Special patterns get different throttling rules
        self.pattern_throttlers = {
            "API": ThrottleSink(throttle_time=120),  # API related logs
            "DB": ThrottleSink(throttle_time=180),  # Database related logs
            "PERF": ThrottleSink(throttle_time=300),  # Performance related logs
        }

    def __call__(self, record):
        """
        Apply throttling based on log level and message content

        Returns:
            bool: True if the message should be logged, False if it should be throttled
        """
        # Extract level and message
        level = record["level"].name
        message = record["message"]

        # Critical logs are never throttled
        if level == "CRITICAL":
            return True

        # Check for special patterns first
        for pattern, throttler in self.pattern_throttlers.items():
            if pattern in message:
                return throttler(record)

        # Apply level-specific throttling
        if level == "ERROR":
            return self.error_throttler(record)
        elif level == "WARNING":
            return self.warning_throttler(record)
        elif level == "INFO":
            return self.info_throttler(record)
        elif level == "DEBUG":
            return self.debug_throttler(record)

        # Default: allow the message
        return True


def simulate_application_logs():
    """Generate a variety of log messages to demonstrate the smart throttling"""
    # Set up the smart throttler
    logger.remove()
    smart_throttler = SmartThrottleSink()

    # Add console output with smart throttling
    logger.add(
        sys.stdout,
        filter=smart_throttler,
        format="<blue>{time:HH:mm:ss}</blue> | <level>{level: <8}</level> | <level>{message}</level>",
    )

    # Add file output with the same throttling
    logger.add(
        "smart_throttled.log",
        filter=smart_throttler,
        format="{time:YYYY-MM-DD HH:mm:ss.SSS} | {level: <8} | {message}",
    )

    logger.info("Starting smart throttling demonstration")

    # Message templates for different categories
    messages = {
        "API": [
            "API request to {} returned status {}",
            "API endpoint {} called with parameters {}",
            "API rate limit reached for {}",
        ],
        "DB": [
            "DB query executed in {} ms",
            "DB connection pool at {} capacity",
            "DB transaction {} committed",
        ],
        "PERF": [
            "PERF metric: rendering took {} ms",
            "PERF warning: memory usage at {}%",
            "PERF critical: CPU usage spike to {}%",
        ],
        "GENERAL": [
            "User {} logged in",
            "File {} processed",
            "Task {} completed in {} seconds",
            "Configuration reloaded",
            "Cache hit ratio: {}%",
        ],
    }

    # Log levels to use
    levels = ["debug", "info", "warning", "error", "critical"]

    # Generate 200 log messages
    for i in range(200):
        # Determine category
        if i % 10 == 0:
            # Every 10th message is a performance message
            category = "PERF"
        elif i % 5 == 0:
            # Every 5th message is a database message
            category = "DB"
        elif i % 3 == 0:
            # Every 3rd message is an API message
            category = "API"
        else:
            # Others are general messages
            category = "GENERAL"

        # Select a random message template from the category
        template = random.choice(messages[category])

        # Generate random parameters for the template
        params = []
        for _ in range(template.count("{}")):
            if "%" in template:
                # Percentage value
                params.append(random.randint(1, 100))
            elif "status" in template:
                # HTTP status code
                params.append(random.choice([200, 201, 400, 404, 500]))
            elif "ms" in template:
                # Milliseconds
                params.append(random.randint(1, 1000))
            else:
                # Generic ID or name
                params.append(f"item-{random.randint(1000, 9999)}")

        # Format the message
        message = template.format(*params)

        # Determine log level based on content and patterns
        if "critical" in message.lower():
            level = "critical"
        elif "error" in message.lower() or "failed" in message.lower():
            level = "error"
        elif "warning" in message.lower() or "at " in message.lower():
            level = "warning"
        elif category in ["API", "DB"]:
            # API and DB messages are usually info level
            level = "info"
        else:
            # Use a weighted random level
            weights = [
                0.4,
                0.3,
                0.2,
                0.08,
                0.02,
            ]  # debug, info, warning, error, critical
            level = random.choices(levels, weights=weights)[0]

        # Log the message with the appropriate level
        getattr(logger, level)(message)

        # Add a small delay between messages
        time.sleep(0.05)

        # Print progress every 50 messages
        if (i + 1) % 50 == 0:
            print(f"\n--- Generated {i + 1}/200 messages ---\n")

    logger.info("Smart throttling demonstration completed")
    logger.info("Check smart_throttled.log to see the complete log output")


if __name__ == "__main__":
    simulate_application_logs()
