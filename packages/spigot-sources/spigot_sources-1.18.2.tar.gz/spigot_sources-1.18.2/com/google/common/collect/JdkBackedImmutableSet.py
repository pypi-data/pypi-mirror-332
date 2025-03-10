"""
Python module generated from Java source file com.google.common.collect.JdkBackedImmutableSet

Java source file obtained from artifact guava version 31.0.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.collect import *
from javax.annotation import CheckForNull
from typing import Any, Callable, Iterable, Tuple


class JdkBackedImmutableSet(IndexedImmutableSet):
    """
    ImmutableSet implementation backed by a JDK HashSet, used to defend against apparent hash
    flooding. This implementation is never used on the GWT client side, but it must be present there
    for serialization to work.

    Author(s)
    - Louis Wasserman
    """

    def contains(self, object: "Object") -> bool:
        ...


    def size(self) -> int:
        ...
