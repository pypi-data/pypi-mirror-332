"""
Python module generated from Java source file com.google.common.hash.Murmur3_128HashFunction

Java source file obtained from artifact guava version 33.3.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.hash import *
from com.google.errorprone.annotations import Immutable
from java.io import Serializable
from javax.annotation import CheckForNull
from typing import Any, Callable, Iterable, Tuple


class Murmur3_128HashFunction(AbstractHashFunction, Serializable):
    """
    See MurmurHash3_x64_128 in <a href="http://smhasher.googlecode.com/svn/trunk/MurmurHash3.cpp">the
    C++ implementation</a>.

    Author(s)
    - Dimitris Andreou
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
