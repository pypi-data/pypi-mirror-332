"""
Python module generated from Java source file com.google.common.hash.SipHashFunction

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.hash import *
from java.io import Serializable
from javax.annotation import Nullable
from typing import Any, Callable, Iterable, Tuple


class SipHashFunction(AbstractStreamingHashFunction, Serializable):
    """
    HashFunction implementation of SipHash-c-d.

    Author(s)
    - Daniel J. Bernstein
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
