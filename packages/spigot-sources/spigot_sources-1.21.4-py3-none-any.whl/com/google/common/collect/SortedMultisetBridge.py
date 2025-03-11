"""
Python module generated from Java source file com.google.common.collect.SortedMultisetBridge

Java source file obtained from artifact guava version 33.3.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtIncompatible
from com.google.common.collect import *
from java.util import SortedSet
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class SortedMultisetBridge(Multiset):
    """
    Superinterface of SortedMultiset to introduce a bridge method for `elementSet()`,
    to ensure binary compatibility with older Guava versions that specified `elementSet()` to
    return `SortedSet`.

    Author(s)
    - Louis Wasserman
    """

    def elementSet(self) -> "SortedSet"["E"]:
        ...
