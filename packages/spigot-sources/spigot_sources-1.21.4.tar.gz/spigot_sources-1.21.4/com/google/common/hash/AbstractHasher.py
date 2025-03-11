"""
Python module generated from Java source file com.google.common.hash.AbstractHasher

Java source file obtained from artifact guava version 33.3.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.base import Preconditions
from com.google.common.hash import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from java.nio.charset import Charset
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class AbstractHasher(Hasher):
    """
    An abstract implementation of Hasher, which only requires subtypes to implement .putByte. Subtypes may provide more efficient implementations, however.

    Author(s)
    - Dimitris Andreou
    """

    def putBoolean(self, b: bool) -> "Hasher":
        ...


    def putDouble(self, d: float) -> "Hasher":
        ...


    def putFloat(self, f: float) -> "Hasher":
        ...


    def putUnencodedChars(self, charSequence: "CharSequence") -> "Hasher":
        ...


    def putString(self, charSequence: "CharSequence", charset: "Charset") -> "Hasher":
        ...


    def putBytes(self, bytes: list[int]) -> "Hasher":
        ...


    def putBytes(self, bytes: list[int], off: int, len: int) -> "Hasher":
        ...


    def putBytes(self, b: "ByteBuffer") -> "Hasher":
        ...


    def putShort(self, s: int) -> "Hasher":
        ...


    def putInt(self, i: int) -> "Hasher":
        ...


    def putLong(self, l: int) -> "Hasher":
        ...


    def putChar(self, c: str) -> "Hasher":
        ...


    def putObject(self, instance: "T", funnel: "Funnel"["T"]) -> "Hasher":
        ...
