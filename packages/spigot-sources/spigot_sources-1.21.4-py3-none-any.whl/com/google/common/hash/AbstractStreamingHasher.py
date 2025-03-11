"""
Python module generated from Java source file com.google.common.hash.AbstractStreamingHasher

Java source file obtained from artifact guava version 33.3.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.hash import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from typing import Any, Callable, Iterable, Tuple


class AbstractStreamingHasher(AbstractHasher):

    def putBytes(self, bytes: list[int], off: int, len: int) -> "Hasher":
        ...


    def putBytes(self, readBuffer: "ByteBuffer") -> "Hasher":
        ...


    def putByte(self, b: int) -> "Hasher":
        ...


    def putShort(self, s: int) -> "Hasher":
        ...


    def putChar(self, c: str) -> "Hasher":
        ...


    def putInt(self, i: int) -> "Hasher":
        ...


    def putLong(self, l: int) -> "Hasher":
        ...


    def hash(self) -> "HashCode":
        ...
