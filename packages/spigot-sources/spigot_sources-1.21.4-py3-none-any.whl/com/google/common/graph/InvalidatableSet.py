"""
Python module generated from Java source file com.google.common.graph.InvalidatableSet

Java source file obtained from artifact guava version 33.3.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.base import Supplier
from com.google.common.collect import ForwardingSet
from com.google.common.graph import *
from typing import Any, Callable, Iterable, Tuple


class InvalidatableSet(ForwardingSet):
    """
    A subclass of `ForwardingSet` that throws `IllegalStateException` on invocation of any method
    (except `hashCode` and `equals`) if the provided `Supplier` returns False.
    """

    @staticmethod
    def of(delegate: set["E"], validator: "Supplier"["Boolean"], errorMessage: "Supplier"[str]) -> "InvalidatableSet"["E"]:
        ...


    def hashCode(self) -> int:
        ...
