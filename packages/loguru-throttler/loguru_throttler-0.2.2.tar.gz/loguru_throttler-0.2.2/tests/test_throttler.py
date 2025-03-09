"""
Unit tests for the loguru-throttler package.
"""

import io
import os
import sys
import tempfile
import threading
import time
import unittest
from contextlib import redirect_stdout
from unittest.mock import MagicMock

from loguru import logger

from loguru_throttler import ThrottleSink, add_throttled_sink


class TestThrottleSink(unittest.TestCase):
    """Test cases for the ThrottleSink class."""

    def setUp(self):
        """Set up test environment."""
        # Remove default logger
        logger.remove()

        # Create a temporary file for testing
        self.test_file = tempfile.NamedTemporaryFile(delete=False)
        self.test_file.close()

    def tearDown(self):
        """Clean up after tests."""
        # Remove all sinks
        logger.remove()

        # Remove temporary file
        if os.path.exists(self.test_file.name):
            os.unlink(self.test_file.name)

    def test_message_throttling(self):
        """Test that duplicate messages are throttled."""
        # Create a throttled sink with a 0.1-second window
        throttler = ThrottleSink(throttle_time=0.1)

        # Create a mock record
        record = {"message": "Test message", "level": MagicMock(name="INFO")}

        # First call should return True (message allowed)
        self.assertTrue(throttler(record))

        # Second call should return False (message throttled)
        self.assertFalse(throttler(record))

        # Wait for throttle window to expire
        time.sleep(0.2)

        # Third call should return True again (throttle window expired)
        self.assertTrue(throttler(record))

    def test_different_messages_not_throttled(self):
        """Test that different messages are not throttled."""
        # Create a throttled sink
        throttler = ThrottleSink(throttle_time=0.1)

        # Create two different records
        record1 = {"message": "Test message 1", "level": MagicMock(name="INFO")}

        record2 = {"message": "Test message 2", "level": MagicMock(name="INFO")}

        # Both should be allowed
        self.assertTrue(throttler(record1))
        self.assertTrue(throttler(record2))

    def test_different_levels_not_throttled(self):
        """Test that same message with different levels is not throttled."""
        # Create a throttled sink
        throttler = ThrottleSink(throttle_time=0.1)

        # Create two records with same message but different levels
        record1 = {"message": "Test message", "level": MagicMock(name="INFO")}

        record2 = {"message": "Test message", "level": MagicMock(name="ERROR")}

        # Both should be allowed
        self.assertTrue(throttler(record1))
        self.assertTrue(throttler(record2))

    def test_integration_with_loguru(self):
        """Test integration with loguru logger."""
        # Capture stdout
        captured_output = io.StringIO()

        with redirect_stdout(captured_output):
            # Add a throttled sink to stdout
            logger.add(sys.stdout, filter=ThrottleSink(throttle_time=0.1))

            # Log the same message twice
            logger.info("Test message")
            logger.info("Test message")

            # Wait for throttle window to expire
            time.sleep(0.2)

            # Log the message again
            logger.info("Test message")

        # Check that the message appears twice in the output (not three times)
        output = captured_output.getvalue()
        self.assertEqual(output.count("Test message"), 2)

    def test_file_sink_throttling(self):
        """Test throttling with a file sink."""
        # Add a throttled file sink
        add_throttled_sink(logger, self.test_file.name, throttle_time=0.1)

        # Log the same message twice
        logger.info("Test file message")
        logger.info("Test file message")

        # Wait for throttle window to expire
        time.sleep(0.2)

        # Log the message again
        logger.info("Test file message")

        # Check the file content
        with open(self.test_file.name, "r") as f:
            content = f.read()
            self.assertEqual(content.count("Test file message"), 2)

    def test_thread_safety(self):
        """Test thread safety of the throttling mechanism."""
        # Create a throttled sink with a 1-second window
        throttler = ThrottleSink(throttle_time=1)

        # Create a record
        record = {"message": "Thread test message", "level": MagicMock(name="INFO")}

        # Counter for allowed messages
        allowed_count = 0

        # Lock for thread safety
        lock = threading.Lock()

        def test_thread():
            nonlocal allowed_count
            result = throttler(record)
            with lock:
                if result:
                    allowed_count += 1

        # Create and start 10 threads
        threads = []
        for _ in range(10):
            thread = threading.Thread(target=test_thread)
            threads.append(thread)
            thread.start()

        # Wait for all threads to complete
        for thread in threads:
            thread.join()

        # Only one message should be allowed
        self.assertEqual(allowed_count, 1)

    def test_burst_mode(self):
        """Test burst mode functionality."""
        # Create a throttled sink with burst mode (allow 3 messages)
        throttler = ThrottleSink(throttle_time=0.2, burst_limit=3)

        # Create a record
        record = {"message": "Burst test message", "level": MagicMock(name="INFO")}

        # First three calls should return True (within burst limit)
        self.assertTrue(throttler(record))
        self.assertTrue(throttler(record))
        self.assertTrue(throttler(record))

        # Fourth call should return False (exceeded burst limit)
        self.assertFalse(throttler(record))

        # Wait for throttle window to expire
        time.sleep(0.3)

        # After window expires, burst counter should reset
        self.assertTrue(throttler(record))
        self.assertTrue(throttler(record))
        self.assertTrue(throttler(record))
        self.assertFalse(throttler(record))

    def test_burst_window_different_from_throttle_time(self):
        """Test burst mode with a different burst window than throttle time."""
        # Create a throttled sink with burst mode (allow 2 messages in 0.1s window, but throttle for 0.3s)
        throttler = ThrottleSink(throttle_time=0.3, burst_limit=2, burst_window=0.1)

        # Create a record
        record = {
            "message": "Burst window test message",
            "level": MagicMock(name="INFO"),
        }

        # First two calls should return True (within burst limit)
        self.assertTrue(throttler(record))
        self.assertTrue(throttler(record))

        # Third call should return False (exceeded burst limit)
        self.assertFalse(throttler(record))

        # Wait for burst window to expire but not throttle time
        time.sleep(0.15)

        # Burst counter should reset, but we're still within throttle time
        self.assertTrue(throttler(record))
        self.assertTrue(throttler(record))
        self.assertFalse(throttler(record))

        # Wait for throttle time to expire
        time.sleep(0.2)

        # Everything should reset
        self.assertTrue(throttler(record))


if __name__ == "__main__":
    unittest.main()
