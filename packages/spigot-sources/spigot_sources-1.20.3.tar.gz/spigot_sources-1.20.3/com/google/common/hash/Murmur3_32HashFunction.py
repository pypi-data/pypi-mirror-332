"""
Python module generated from Java source file com.google.common.hash.Murmur3_32HashFunction

Java source file obtained from artifact guava version 32.1.2-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.base import Charsets
from com.google.common.hash import *
from com.google.common.primitives import Chars
from com.google.common.primitives import Ints
from com.google.common.primitives import Longs
from com.google.errorprone.annotations import CanIgnoreReturnValue
from com.google.errorprone.annotations import Immutable
from java.io import Serializable
from java.nio.charset import Charset
from javax.annotation import CheckForNull
from typing import Any, Callable, Iterable, Tuple


class Murmur3_32HashFunction(AbstractHashFunction, Serializable):
    """
    See MurmurHash3_x86_32 in <a
    href="https://github.com/aappleby/smhasher/blob/master/src/MurmurHash3.cpp">the C++
    implementation</a>.

    Author(s)
    - Kurt Alfred Kluever
    """

    def bits(self) -> int:
        ...


    def newHasher(self) -> "Hasher":
        ...


    def toString(self) -> str:
        ...


    def equals(self, object: "Object") -> bool:
        ...


    def hashCode(self) -> int:
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
