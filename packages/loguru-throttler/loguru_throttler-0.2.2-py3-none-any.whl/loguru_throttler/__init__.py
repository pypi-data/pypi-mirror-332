"""
Loguru Throttler - A package for throttling duplicate log messages in loguru.
"""

from .throttler import ThrottleSink, add_throttled_sink

__version__ = "0.2.2"
__all__ = ["ThrottleSink", "add_throttled_sink"]
