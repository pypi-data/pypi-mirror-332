"""
Python module generated from Java source file com.google.common.base.PairwiseEquivalence

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.base import *
from java.io import Serializable
from java.util import Iterator
from javax.annotation import Nullable
from typing import Any, Callable, Iterable, Tuple


class PairwiseEquivalence(Equivalence, Serializable):

    def equals(self, object: "Object") -> bool:
        ...


    def hashCode(self) -> int:
        ...


    def toString(self) -> str:
        ...
