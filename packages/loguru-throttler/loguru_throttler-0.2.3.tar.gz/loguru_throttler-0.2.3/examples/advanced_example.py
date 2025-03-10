#!/usr/bin/env python3
"""
Advanced Loguru Throttler Example: API Client Simulation

This script demonstrates a practical use case for loguru-throttler by simulating
an API client that experiences rate limiting and occasional failures.
"""

import random
import sys
import time
from datetime import datetime

from loguru import logger

from loguru_throttler import ThrottleSink

# Clear any existing handlers
logger.remove()

# Configure logging with different throttling strategies for different log levels
# Regular console output
logger.add(
    sys.stdout,
    level="INFO",
    format="<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
)

# Throttled error logging (allow 2 errors of the same type every 30 seconds)
error_throttler = ThrottleSink(
    throttle_time=30, burst_limit=2, burst_window=30, include_extra=True
)

# Add a file sink with error throttling
logger.add(
    "api_errors.log",
    filter=error_throttler,
    level="ERROR",
    format="{time:YYYY-MM-DD HH:mm:ss.SSS} | {level: <8} | {name}:{function}:{line} - {message} | {extra}",
)

# Add a debug log with aggressive throttling (only show unique messages every 5 minutes)
debug_throttler = ThrottleSink(
    throttle_time=300,  # 5 minutes
    include_extra=False,
    max_cache_size=500,  # Limit memory usage
)

logger.add(
    "api_debug.log",
    filter=debug_throttler,
    level="DEBUG",
    format="{time:YYYY-MM-DD HH:mm:ss.SSS} | {level: <8} | {message}",
)


class APIClient:
    """Simulated API client that experiences rate limiting and occasional failures"""

    def __init__(self, name, rate_limit=10):
        self.name = name
        self.rate_limit = rate_limit
        self.request_count = 0
        self.last_reset = datetime.now()
        self.logger = logger.bind(api_client=name)

    def _check_rate_limit(self):
        """Check if we've hit the rate limit"""
        # Reset counter if a minute has passed
        now = datetime.now()
        if (now - self.last_reset).total_seconds() > 60:
            self.request_count = 0
            self.last_reset = now

        # Check if we're over the limit
        if self.request_count >= self.rate_limit:
            return False

        self.request_count += 1
        return True

    def make_request(self, endpoint, payload=None):
        """Simulate making an API request"""
        request_id = random.randint(10000, 99999)
        log = self.logger.bind(request_id=request_id, endpoint=endpoint)

        log.debug(f"Making request to {endpoint} with payload: {payload}")

        # Simulate rate limiting
        if not self._check_rate_limit():
            log.error("Rate limit exceeded", rate_limit=self.rate_limit)
            return {"error": "Rate limit exceeded", "status": 429}

        # Simulate random failures (10% chance)
        if random.random() < 0.1:
            error_type = random.choice(["timeout", "server_error", "bad_gateway"])
            status = {"timeout": 408, "server_error": 500, "bad_gateway": 502}[
                error_type
            ]

            log.error(
                f"Request failed with {error_type}",
                error_type=error_type,
                status=status,
            )

            return {"error": error_type, "status": status}

        # Successful request
        log.info(f"Request to {endpoint} successful")
        return {"status": 200, "data": f"Response from {endpoint}"}


def simulate_api_traffic():
    """Simulate traffic to multiple API endpoints"""
    # Create two API clients with different rate limits
    client1 = APIClient("PaymentAPI", rate_limit=5)
    client2 = APIClient("InventoryAPI", rate_limit=15)

    # Endpoints to call
    endpoints = ["/users", "/products", "/orders", "/payments", "/shipments"]

    logger.info("Starting API traffic simulation")
    logger.info("This will generate throttled logs in api_errors.log and api_debug.log")

    # Simulate 100 requests
    for i in range(100):
        # Pick a random client and endpoint
        client = random.choice([client1, client2])
        endpoint = random.choice(endpoints)

        # Make the request
        client.make_request(endpoint, {"timestamp": time.time()})

        # Small delay between requests
        time.sleep(0.1)

        # Print progress every 20 requests
        if (i + 1) % 20 == 0:
            logger.info(f"Completed {i + 1}/100 simulated requests")

    logger.info("API traffic simulation completed")
    logger.info("Check api_errors.log and api_debug.log to see the throttled output")


if __name__ == "__main__":
    simulate_api_traffic()
