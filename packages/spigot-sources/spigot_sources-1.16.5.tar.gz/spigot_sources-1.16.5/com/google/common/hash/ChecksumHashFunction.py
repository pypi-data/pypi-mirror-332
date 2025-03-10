"""
Python module generated from Java source file com.google.common.hash.ChecksumHashFunction

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.base import Supplier
from com.google.common.hash import *
from java.io import Serializable
from java.util.zip import Checksum
from typing import Any, Callable, Iterable, Tuple


class ChecksumHashFunction(AbstractStreamingHashFunction, Serializable):
    """
    HashFunction adapter for Checksum instances.

    Author(s)
    - Colin Decker
    """

    def bits(self) -> int:
        ...


    def newHasher(self) -> "Hasher":
        ...


    def toString(self) -> str:
        ...
