"""
Python module generated from Java source file com.google.common.hash.AbstractHashFunction

Java source file obtained from artifact guava version 31.0.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.hash import *
from com.google.errorprone.annotations import Immutable
from java.nio.charset import Charset
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class AbstractHashFunction(HashFunction):
    """
    Skeleton implementation of HashFunction in terms of .newHasher().
    
    TODO(lowasser): make public
    """

    def hashObject(self, instance: "T", funnel: "Funnel"["T"]) -> "HashCode":
        ...


    def hashUnencodedChars(self, input: "CharSequence") -> "HashCode":
        ...


    def hashString(self, input: "CharSequence", charset: "Charset") -> "HashCode":
        ...


    def hashInt(self, input: int) -> "HashCode":
        ...


    def hashLong(self, input: int) -> "HashCode":
        ...


    def hashBytes(self, input: list[int]) -> "HashCode":
        ...


    def hashBytes(self, input: list[int], off: int, len: int) -> "HashCode":
        ...


    def hashBytes(self, input: "ByteBuffer") -> "HashCode":
        ...


    def newHasher(self, expectedInputSize: int) -> "Hasher":
        ...
