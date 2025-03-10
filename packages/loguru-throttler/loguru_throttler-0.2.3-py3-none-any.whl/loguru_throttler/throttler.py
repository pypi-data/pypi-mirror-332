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
        report_stats: Whether to report throttling statistics (default: False)
        report_interval: Time in seconds between statistics reports (default: 60)
    """

    def __init__(
        self,
        throttle_time: int = 60,
        max_cache_size: int = 1024,
        burst_limit: int = 1,
        burst_window: Optional[int] = None,
        include_extra: bool = False,
        report_stats: bool = False,
        report_interval: int = 60,
    ):
        self.throttle_time = throttle_time
        self.burst_limit = burst_limit
        self.burst_window = burst_window if burst_window is not None else throttle_time
        self.include_extra = include_extra
        self.report_stats = report_stats
        self.report_interval = report_interval
        self.message_cache: Dict[
            str, float
        ] = {}  # Use a regular dict for message timestamps
        self.burst_counts: Dict[
            str, Tuple[float, int]
        ] = {}  # Use a regular dict for burst counts
        self.cache_keys: List[str] = []  # List to track key order for LRU
        self.max_cache_size = max_cache_size
        self.lock = threading.RLock()

        # Statistics tracking
        self.throttled_counts: Dict[str, int] = {}  # Track throttled messages by hash
        self.total_throttled = 0  # Total number of throttled messages
        self.last_report_time = time.time()  # Last time statistics were reported
        self.message_content_cache: Dict[
            str, str
        ] = {}  # Cache message content for reporting

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

        # Store message content for reporting if stats are enabled
        if self.report_stats and message_hash not in self.message_content_cache:
            self.message_content_cache[message_hash] = record["message"]

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

                    # Update throttling statistics
                    if self.report_stats:
                        self.throttled_counts[message_hash] = (
                            self.throttled_counts.get(message_hash, 0) + 1
                        )
                        self.total_throttled += 1

                        # Check if it's time to report statistics
                        if current_time - self.last_report_time >= self.report_interval:
                            self._report_statistics(record)
                            self.last_report_time = current_time

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
            if oldest_key in self.throttled_counts:
                del self.throttled_counts[oldest_key]
            if oldest_key in self.message_content_cache:
                del self.message_content_cache[oldest_key]

    def _report_statistics(self, record: Dict[str, Any]) -> None:
        """
        Report throttling statistics.

        This method creates a summary log message with throttling statistics.

        Args:
            record: The current loguru record (used to get logger instance)
        """
        if not self.throttled_counts:
            return

        # Get the logger instance from the record
        # In loguru, we can use the same sink that received the original message
        logger = record.get("extra", {}).get("logger", None)

        # If we can't get the logger from extra, try to get it from the record directly
        if not logger:
            # Use the sink directly if available
            sink = record.get("sink", None)
            if sink:
                # Create a summary of throttled messages
                summary_lines = []

                # Add total count
                summary_lines.append(
                    f"Suppressed {self.total_throttled} messages in the last {self.report_interval} seconds"
                )

                # Add top throttled messages (up to 5)
                top_messages = sorted(
                    self.throttled_counts.items(), key=lambda x: x[1], reverse=True
                )[:5]

                for msg_hash, count in top_messages:
                    message = self.message_content_cache.get(
                        msg_hash, "Unknown message"
                    )
                    if len(message) > 50:
                        message = message[:47] + "..."
                    summary_lines.append(f"  - '{message}': {count} times")

                # Write directly to the sink
                try:
                    sink(record["message"] + "\n" + "\n".join(summary_lines))
                except Exception:
                    # If direct sink access fails, fall back to print
                    print("\n".join(summary_lines))

                # Reset counters after reporting
                self.throttled_counts.clear()
                self.total_throttled = 0
                return

            # If we can't get the sink either, fall back to print
            summary_lines = [
                f"Suppressed {self.total_throttled} messages in the last {self.report_interval} seconds"
            ]
            top_messages = sorted(
                self.throttled_counts.items(), key=lambda x: x[1], reverse=True
            )[:5]

            for msg_hash, count in top_messages:
                message = self.message_content_cache.get(msg_hash, "Unknown message")
                if len(message) > 50:
                    message = message[:47] + "..."
                summary_lines.append(f"  - '{message}': {count} times")

            print("\n".join(summary_lines))

            # Reset counters after reporting
            self.throttled_counts.clear()
            self.total_throttled = 0
            return

        # Create a summary of throttled messages
        summary_lines = []

        # Add total count
        summary_lines.append(
            f"Suppressed {self.total_throttled} messages in the last {self.report_interval} seconds"
        )

        # Add top throttled messages (up to 5)
        top_messages = sorted(
            self.throttled_counts.items(), key=lambda x: x[1], reverse=True
        )[:5]

        for msg_hash, count in top_messages:
            message = self.message_content_cache.get(msg_hash, "Unknown message")
            if len(message) > 50:
                message = message[:47] + "..."
            summary_lines.append(f"  - '{message}': {count} times")

        # Log the summary using the same level as the original message
        level = record["level"].name
        logger.log(level, "\n".join(summary_lines))

        # Reset counters after reporting
        self.throttled_counts.clear()
        self.total_throttled = 0

    def get_statistics(self) -> Dict[str, Any]:
        """
        Get current throttling statistics.

        Returns:
            A dictionary containing throttling statistics
        """
        with self.lock:
            stats = {
                "total_throttled": self.total_throttled,
                "throttled_messages": {
                    self.message_content_cache.get(msg_hash, "Unknown"): count
                    for msg_hash, count in self.throttled_counts.items()
                },
                "cache_size": len(self.message_cache),
                "throttle_time": self.throttle_time,
                "report_interval": self.report_interval,
            }
            return stats


def add_throttled_sink(
    logger,
    sink: Union[str, Callable, Any],
    throttle_time: int = 60,
    max_cache_size: int = 1024,
    burst_limit: int = 1,
    burst_window: Optional[int] = None,
    include_extra: bool = False,
    report_stats: bool = False,
    report_interval: int = 60,
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
        report_stats: Whether to report throttling statistics
        report_interval: Time in seconds between statistics reports
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
        report_stats=report_stats,
        report_interval=report_interval,
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
