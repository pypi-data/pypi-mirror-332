"""
Python module generated from Java source file com.google.common.io.CountingInputStream

Java source file obtained from artifact guava version 33.3.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtIncompatible
from com.google.common.annotations import J2ktIncompatible
from com.google.common.io import *
from java.io import FilterInputStream
from java.io import IOException
from java.io import InputStream
from typing import Any, Callable, Iterable, Tuple


class CountingInputStream(FilterInputStream):
    """
    An InputStream that counts the number of bytes read.

    Author(s)
    - Chris Nokleberg

    Since
    - 1.0
    """

    def __init__(self, in: "InputStream"):
        """
        Wraps another input stream, counting the number of bytes read.

        Arguments
        - in: the input stream to be wrapped
        """
        ...


    def getCount(self) -> int:
        """
        Returns the number of bytes read.
        """
        ...


    def read(self) -> int:
        ...


    def read(self, b: list[int], off: int, len: int) -> int:
        ...


    def skip(self, n: int) -> int:
        ...


    def mark(self, readlimit: int) -> None:
        ...


    def reset(self) -> None:
        ...
