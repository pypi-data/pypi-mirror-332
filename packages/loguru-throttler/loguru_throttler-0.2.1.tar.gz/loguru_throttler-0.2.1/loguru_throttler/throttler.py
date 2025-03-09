"""
Core implementation of the loguru message throttling functionality.
"""

import hashlib
import json
import threading
import time
from collections import OrderedDict
from typing import Any, Callable, Dict, List, Optional, Tuple, Union


class LRUCache(OrderedDict):
    """A size-bounded LRU cache implementation."""

    def __init__(self, maxsize: int = 1024):
        super().__init__()
        self.maxsize = maxsize

    def __getitem__(self, key):
        value = super().__getitem__(key)
        self.move_to_end(key)
        return value

    def __setitem__(self, key, value):
        if key in self:
            self.move_to_end(key)
        super().__setitem__(key, value)
        if len(self) > self.maxsize:
            oldest = next(iter(self))
            del self[oldest]


class ThrottleSink:
    """
    A filter for loguru that throttles duplicate log messages.

    This class implements a message throttling mechanism that suppresses
    identical log messages that occur within a specified time window.

    Args:
        throttle_time: Time in seconds to suppress duplicate messages (default: 60)
        max_cache_size: Maximum number of message hashes to keep in memory (default: 1024)
        burst_limit: Number of messages to allow before throttling begins (default: 1)
        burst_window: Time window in seconds for the burst limit (default: same as throttle_time)
        include_extra: Whether to include extra fields in message hash calculation (default: False)
    """

    def __init__(
        self,
        throttle_time: int = 60,
        max_cache_size: int = 1024,
        burst_limit: int = 1,
        burst_window: Optional[int] = None,
        include_extra: bool = False,
    ):
        self.throttle_time = throttle_time
        self.burst_limit = burst_limit
        self.burst_window = burst_window if burst_window is not None else throttle_time
        self.include_extra = include_extra
        self.message_cache: Dict[
            str, float
        ] = {}  # Use a regular dict for message timestamps
        self.burst_counts: Dict[
            str, Tuple[float, int]
        ] = {}  # Use a regular dict for burst counts
        self.cache_keys: List[str] = []  # List to track key order for LRU
        self.max_cache_size = max_cache_size
        self.lock = threading.RLock()

    def _hash_message(self, record: Dict[str, Any]) -> str:
        """
        Generate a unique hash for a log message based on its content and level.

        Args:
            record: The loguru record dictionary

        Returns:
            A string hash representing the message
        """
        # Extract the relevant parts of the record to hash
        message = record["message"]
        level = record["level"].name

        # Include extra fields if configured
        extra_str = ""
        if self.include_extra and "extra" in record:
            # Sort keys for consistent hashing regardless of order
            extra_dict = record["extra"]
            # Convert to JSON with sorted keys for consistent ordering
            extra_str = json.dumps(extra_dict, sort_keys=True)

        # Create a hash of the message content and level
        content = f"{message}:{level}:{extra_str}"
        return hashlib.sha256(content.encode()).hexdigest()

    def __call__(self, record: Dict[str, Any]) -> bool:
        """
        Filter method called by loguru for each log message.

        Args:
            record: The loguru record dictionary

        Returns:
            True if the message should be logged, False if it should be suppressed
        """
        message_hash = self._hash_message(record)
        current_time = time.time()

        with self.lock:
            # Check if the message is in the cache
            if message_hash in self.message_cache:
                last_logged = self.message_cache[message_hash]

                # If the message was logged recently
                if current_time - last_logged < self.throttle_time:
                    # Check if we're within burst limit
                    if self.burst_limit > 1:
                        # Get burst data: (first_burst_time, count)
                        if message_hash in self.burst_counts:
                            first_burst_time, count = self.burst_counts[message_hash]

                            # Reset burst counter if we're outside the burst window
                            if current_time - first_burst_time > self.burst_window:
                                self.burst_counts[message_hash] = (current_time, 1)
                                self.message_cache[message_hash] = current_time
                                self._update_lru(message_hash)
                                return True

                            # Allow message if we're under burst limit
                            if count < self.burst_limit:
                                self.burst_counts[message_hash] = (
                                    first_burst_time,
                                    count + 1,
                                )
                                return True

                    # Suppress the message
                    return False

            # Update the cache with the current timestamp
            self.message_cache[message_hash] = current_time
            self._update_lru(message_hash)

            # Reset burst counter
            if self.burst_limit > 1:
                self.burst_counts[message_hash] = (current_time, 1)

            return True

    def _update_lru(self, key):
        """Update the LRU tracking for a key."""
        # Remove the key if it's already in the list
        if key in self.cache_keys:
            self.cache_keys.remove(key)

        # Add the key to the end of the list (most recently used)
        self.cache_keys.append(key)

        # If we've exceeded the max cache size, remove the oldest key
        if len(self.cache_keys) > self.max_cache_size:
            oldest_key = self.cache_keys.pop(
                0
            )  # Remove from the beginning (least recently used)
            if oldest_key in self.message_cache:
                del self.message_cache[oldest_key]
            if oldest_key in self.burst_counts:
                del self.burst_counts[oldest_key]


def add_throttled_sink(
    logger,
    sink: Union[str, Callable, Any],
    throttle_time: int = 60,
    max_cache_size: int = 1024,
    burst_limit: int = 1,
    burst_window: Optional[int] = None,
    include_extra: bool = False,
    **kwargs,
) -> int:
    """
    Helper function to add a throttled sink to a loguru logger.

    Args:
        logger: The loguru logger instance
        sink: The sink to add (file, function, etc.)
        throttle_time: Time in seconds to suppress duplicate messages
        max_cache_size: Maximum number of message hashes to keep in memory
        burst_limit: Number of messages to allow before throttling begins
        burst_window: Time window in seconds for the burst limit
        include_extra: Whether to include extra fields in message hash calculation
        **kwargs: Additional arguments to pass to logger.add()

    Returns:
        The sink ID returned by logger.add()
    """
    throttler = ThrottleSink(
        throttle_time=throttle_time,
        max_cache_size=max_cache_size,
        burst_limit=burst_limit,
        burst_window=burst_window,
        include_extra=include_extra,
    )

    # Add the filter to kwargs if it doesn't exist, otherwise combine with existing filter
    if "filter" in kwargs:
        original_filter = kwargs["filter"]

        def combined_filter(record):
            return original_filter(record) and throttler(record)

        kwargs["filter"] = combined_filter
    else:
        kwargs["filter"] = throttler

    return logger.add(sink, **kwargs)
