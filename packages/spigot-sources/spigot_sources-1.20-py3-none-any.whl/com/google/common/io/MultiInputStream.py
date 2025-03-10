"""
Python module generated from Java source file com.google.common.io.MultiInputStream

Java source file obtained from artifact guava version 31.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtIncompatible
from com.google.common.io import *
from java.io import IOException
from java.io import InputStream
from java.util import Iterator
from javax.annotation import CheckForNull
from typing import Any, Callable, Iterable, Tuple


class MultiInputStream(InputStream):
    """
    An InputStream that concatenates multiple substreams. At most one stream will be open at
    a time.

    Author(s)
    - Chris Nokleberg

    Since
    - 1.0
    """

    def __init__(self, it: Iterator["ByteSource"]):
        """
        Creates a new instance.

        Arguments
        - it: an iterator of I/O suppliers that will provide each substream
        """
        ...


    def close(self) -> None:
        ...


    def available(self) -> int:
        ...


    def markSupported(self) -> bool:
        ...


    def read(self) -> int:
        ...


    def read(self, b: list[int], off: int, len: int) -> int:
        ...


    def skip(self, n: int) -> int:
        ...
