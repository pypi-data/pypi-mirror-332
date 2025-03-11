"""
Python module generated from Java source file com.google.common.hash.ChecksumHashFunction

Java source file obtained from artifact guava version 33.3.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.hash import *
from com.google.errorprone.annotations import Immutable
from com.google.j2objc.annotations import J2ObjCIncompatible
from java.io import Serializable
from java.lang.invoke import MethodHandle
from java.lang.invoke import MethodHandles
from java.lang.invoke import MethodType
from java.util.zip import Checksum
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class ChecksumHashFunction(AbstractHashFunction, Serializable):
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
