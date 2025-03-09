"""
Python module generated from Java source file com.google.common.base.Present

Java source file obtained from artifact guava version 32.1.2-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.base import *
from java.util import Collections
from javax.annotation import CheckForNull
from typing import Any, Callable, Iterable, Tuple


class Present(Optional):
    """
    Implementation of an Optional containing a reference.
    """

    def isPresent(self) -> bool:
        ...


    def get(self) -> "T":
        ...


    def or(self, defaultValue: "T") -> "T":
        ...


    def or(self, secondChoice: "Optional"["T"]) -> "Optional"["T"]:
        ...


    def or(self, supplier: "Supplier"["T"]) -> "T":
        ...


    def orNull(self) -> "T":
        ...


    def asSet(self) -> set["T"]:
        ...


    def transform(self, function: "Function"["T", "V"]) -> "Optional"["V"]:
        ...


    def equals(self, object: "Object") -> bool:
        ...


    def hashCode(self) -> int:
        ...


    def toString(self) -> str:
        ...
