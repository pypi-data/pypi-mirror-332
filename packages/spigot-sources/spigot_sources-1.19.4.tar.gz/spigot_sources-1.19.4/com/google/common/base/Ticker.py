"""
Python module generated from Java source file com.google.common.base.Ticker

Java source file obtained from artifact guava version 31.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.base import *
from typing import Any, Callable, Iterable, Tuple


class Ticker:
    """
    A time source; returns a time value representing the number of nanoseconds elapsed since some
    fixed but arbitrary point in time. Note that most users should use Stopwatch instead of
    interacting with this class directly.
    
    **Warning:** this interface can only be used to measure elapsed time, not wall time.

    Author(s)
    - Kevin Bourrillion

    Since
    - 10.0 (<a href="https://github.com/google/guava/wiki/Compatibility">mostly
        source-compatible</a> since 9.0)
    """

    def read(self) -> int:
        """
        Returns the number of nanoseconds elapsed since this ticker's fixed point of reference.
        """
        ...


    @staticmethod
    def systemTicker() -> "Ticker":
        """
        A ticker that reads the current time using System.nanoTime.

        Since
        - 10.0
        """
        ...
