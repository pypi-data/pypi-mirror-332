"""
Python module generated from Java source file com.google.common.collect.LexicographicalOrdering

Java source file obtained from artifact guava version 31.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.collect import *
from java.io import Serializable
from java.util import Comparator
from java.util import Iterator
from javax.annotation import CheckForNull
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class LexicographicalOrdering(Ordering, Serializable):
    """
    An ordering which sorts iterables by comparing corresponding elements pairwise.
    """

    def compare(self, leftIterable: Iterable["T"], rightIterable: Iterable["T"]) -> int:
        ...


    def equals(self, object: "Object") -> bool:
        ...


    def hashCode(self) -> int:
        ...


    def toString(self) -> str:
        ...
