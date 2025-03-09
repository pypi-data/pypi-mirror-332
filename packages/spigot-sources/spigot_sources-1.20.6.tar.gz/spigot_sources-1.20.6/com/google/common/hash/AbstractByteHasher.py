"""
Python module generated from Java source file com.google.common.hash.AbstractByteHasher

Java source file obtained from artifact guava version 32.1.2-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.hash import *
from com.google.common.primitives import Chars
from com.google.common.primitives import Ints
from com.google.common.primitives import Longs
from com.google.common.primitives import Shorts
from com.google.errorprone.annotations import CanIgnoreReturnValue
from typing import Any, Callable, Iterable, Tuple


class AbstractByteHasher(AbstractHasher):
    """
    Abstract Hasher that handles converting primitives to bytes using a scratch `ByteBuffer` and streams all bytes to a sink to compute the hash.

    Author(s)
    - Colin Decker
    """

    def putByte(self, b: int) -> "Hasher":
        ...


    def putBytes(self, bytes: list[int]) -> "Hasher":
        ...


    def putBytes(self, bytes: list[int], off: int, len: int) -> "Hasher":
        ...


    def putBytes(self, bytes: "ByteBuffer") -> "Hasher":
        ...


    def putShort(self, s: int) -> "Hasher":
        ...


    def putInt(self, i: int) -> "Hasher":
        ...


    def putLong(self, l: int) -> "Hasher":
        ...


    def putChar(self, c: str) -> "Hasher":
        ...
