"""
Python module generated from Java source file com.google.common.hash.HashingOutputStream

Java source file obtained from artifact guava version 31.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.hash import *
from java.io import FilterOutputStream
from java.io import IOException
from java.io import OutputStream
from typing import Any, Callable, Iterable, Tuple


class HashingOutputStream(FilterOutputStream):
    """
    An OutputStream that maintains a hash of the data written to it.

    Author(s)
    - Nick Piepmeier

    Since
    - 16.0
    """

    def __init__(self, hashFunction: "HashFunction", out: "OutputStream"):
        ...


    def write(self, b: int) -> None:
        ...


    def write(self, bytes: list[int], off: int, len: int) -> None:
        ...


    def hash(self) -> "HashCode":
        """
        Returns the HashCode based on the data written to this stream. The result is
        unspecified if this method is called more than once on the same instance.
        """
        ...


    def close(self) -> None:
        ...
