"""
Python module generated from Java source file com.google.common.hash.AbstractNonStreamingHashFunction

Java source file obtained from artifact guava version 31.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.base import Preconditions
from com.google.common.hash import *
from com.google.errorprone.annotations import Immutable
from java.io import ByteArrayOutputStream
from java.nio.charset import Charset
from java.util import Arrays
from typing import Any, Callable, Iterable, Tuple


class AbstractNonStreamingHashFunction(AbstractHashFunction):
    """
    Skeleton implementation of HashFunction, appropriate for non-streaming algorithms. All
    the hash computation done using .newHasher() are delegated to the .hashBytes(byte[], int, int) method.

    Author(s)
    - Dimitris Andreou
    """

    def newHasher(self) -> "Hasher":
        ...


    def newHasher(self, expectedInputSize: int) -> "Hasher":
        ...


    def hashInt(self, input: int) -> "HashCode":
        ...


    def hashLong(self, input: int) -> "HashCode":
        ...


    def hashUnencodedChars(self, input: "CharSequence") -> "HashCode":
        ...


    def hashString(self, input: "CharSequence", charset: "Charset") -> "HashCode":
        ...


    def hashBytes(self, input: list[int], off: int, len: int) -> "HashCode":
        ...


    def hashBytes(self, input: "ByteBuffer") -> "HashCode":
        ...
