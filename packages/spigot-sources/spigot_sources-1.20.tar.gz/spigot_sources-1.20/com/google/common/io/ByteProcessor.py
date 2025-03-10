"""
Python module generated from Java source file com.google.common.io.ByteProcessor

Java source file obtained from artifact guava version 31.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.annotations import GwtIncompatible
from com.google.common.io import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from com.google.errorprone.annotations import DoNotMock
from java.io import IOException
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class ByteProcessor:
    """
    A callback interface to process bytes from a stream.
    
    .processBytes will be called for each chunk of data that is read, and should return
    `False` when you want to stop processing.

    Author(s)
    - Chris Nokleberg

    Since
    - 1.0
    """

    def processBytes(self, buf: list[int], off: int, len: int) -> bool:
        """
        This method will be called for each chunk of bytes in an input stream. The implementation
        should process the bytes from `buf[off]` through `buf[off + len - 1]` (inclusive).

        Arguments
        - buf: the byte array containing the data to process
        - off: the initial offset into the array
        - len: the length of data to be processed

        Returns
        - True to continue processing, False to stop
        """
        ...


    def getResult(self) -> "T":
        """
        Return the result of processing all the bytes.
        """
        ...
