"""
Python module generated from Java source file com.google.common.io.CountingOutputStream

Java source file obtained from artifact guava version 32.1.2-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtIncompatible
from com.google.common.annotations import J2ktIncompatible
from com.google.common.io import *
from java.io import FilterOutputStream
from java.io import IOException
from java.io import OutputStream
from typing import Any, Callable, Iterable, Tuple


class CountingOutputStream(FilterOutputStream):
    """
    An OutputStream that counts the number of bytes written.

    Author(s)
    - Chris Nokleberg

    Since
    - 1.0
    """

    def __init__(self, out: "OutputStream"):
        """
        Wraps another output stream, counting the number of bytes written.

        Arguments
        - out: the output stream to be wrapped
        """
        ...


    def getCount(self) -> int:
        """
        Returns the number of bytes written.
        """
        ...


    def write(self, b: list[int], off: int, len: int) -> None:
        ...


    def write(self, b: int) -> None:
        ...


    def close(self) -> None:
        ...
