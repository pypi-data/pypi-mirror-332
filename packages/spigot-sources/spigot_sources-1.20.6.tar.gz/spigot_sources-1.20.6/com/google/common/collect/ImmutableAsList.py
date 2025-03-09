"""
Python module generated from Java source file com.google.common.collect.ImmutableAsList

Java source file obtained from artifact guava version 32.1.2-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.annotations import GwtIncompatible
from com.google.common.annotations import J2ktIncompatible
from com.google.common.collect import *
from java.io import InvalidObjectException
from java.io import ObjectInputStream
from java.io import Serializable
from javax.annotation import CheckForNull
from typing import Any, Callable, Iterable, Tuple


class ImmutableAsList(ImmutableList):
    """
    List returned by ImmutableCollection.asList that delegates `contains` checks to the
    backing collection.

    Author(s)
    - Louis Wasserman
    """

    def contains(self, target: "Object") -> bool:
        ...


    def size(self) -> int:
        ...


    def isEmpty(self) -> bool:
        ...
