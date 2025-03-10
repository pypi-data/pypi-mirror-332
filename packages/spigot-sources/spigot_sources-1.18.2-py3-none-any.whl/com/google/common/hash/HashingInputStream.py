"""
Python module generated from Java source file com.google.common.hash.HashingInputStream

Java source file obtained from artifact guava version 31.0.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.hash import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from java.io import FilterInputStream
from java.io import IOException
from java.io import InputStream
from typing import Any, Callable, Iterable, Tuple


class HashingInputStream(FilterInputStream):
    """
    An InputStream that maintains a hash of the data read from it.

    Author(s)
    - Qian Huang

    Since
    - 16.0
    """

    def __init__(self, hashFunction: "HashFunction", in: "InputStream"):
        """
        Creates an input stream that hashes using the given HashFunction and delegates all data
        read from it to the underlying InputStream.
        
        The InputStream should not be read from before or after the hand-off.
        """
        ...


    def read(self) -> int:
        """
        Reads the next byte of data from the underlying input stream and updates the hasher with the
        byte read.
        """
        ...


    def read(self, bytes: list[int], off: int, len: int) -> int:
        """
        Reads the specified bytes of data from the underlying input stream and updates the hasher with
        the bytes read.
        """
        ...


    def markSupported(self) -> bool:
        """
        mark() is not supported for HashingInputStream

        Returns
        - `False` always
        """
        ...


    def mark(self, readlimit: int) -> None:
        """
        mark() is not supported for HashingInputStream
        """
        ...


    def reset(self) -> None:
        """
        reset() is not supported for HashingInputStream.

        Raises
        - IOException: this operation is not supported
        """
        ...


    def hash(self) -> "HashCode":
        """
        Returns the HashCode based on the data read from this stream. The result is unspecified
        if this method is called more than once on the same instance.
        """
        ...
