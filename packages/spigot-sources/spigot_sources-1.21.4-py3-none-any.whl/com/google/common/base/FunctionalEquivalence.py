"""
Python module generated from Java source file com.google.common.base.FunctionalEquivalence

Java source file obtained from artifact guava version 33.3.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.base import *
from java.io import Serializable
from javax.annotation import CheckForNull
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class FunctionalEquivalence(Equivalence, Serializable):
    """
    Equivalence applied on functional result.

    Author(s)
    - Bob Lee

    Since
    - 10.0
    """

    def equals(self, obj: "Object") -> bool:
        ...


    def hashCode(self) -> int:
        ...


    def toString(self) -> str:
        ...
