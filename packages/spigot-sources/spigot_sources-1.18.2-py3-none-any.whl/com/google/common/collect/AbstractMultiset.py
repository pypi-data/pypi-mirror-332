"""
Python module generated from Java source file com.google.common.collect.AbstractMultiset

Java source file obtained from artifact guava version 31.0.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.collect import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from com.google.errorprone.annotations.concurrent import LazyInit
from com.google.j2objc.annotations import WeakOuter
from java.util import AbstractCollection
from java.util import Iterator
from javax.annotation import CheckForNull
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class AbstractMultiset(AbstractCollection, Multiset):
    """
    This class provides a skeletal implementation of the Multiset interface. A new multiset
    implementation can be created easily by extending this class and implementing the Multiset.entrySet() method, plus optionally overriding .add(Object, int) and .remove(Object, int) to enable modifications to the multiset.
    
    The .count and .size implementations all iterate across the set returned by
    Multiset.entrySet(), as do many methods acting on the set returned by .elementSet(). Override those methods for better performance.

    Author(s)
    - Louis Wasserman
    """

    def isEmpty(self) -> bool:
        ...


    def contains(self, element: "Object") -> bool:
        ...


    def add(self, element: "E") -> bool:
        ...


    def add(self, element: "E", occurrences: int) -> int:
        ...


    def remove(self, element: "Object") -> bool:
        ...


    def remove(self, element: "Object", occurrences: int) -> int:
        ...


    def setCount(self, element: "E", count: int) -> int:
        ...


    def setCount(self, element: "E", oldCount: int, newCount: int) -> bool:
        ...


    def addAll(self, elementsToAdd: Iterable["E"]) -> bool:
        """
        
        
        This implementation is highly efficient when `elementsToAdd` is itself a Multiset.
        """
        ...


    def removeAll(self, elementsToRemove: Iterable[Any]) -> bool:
        ...


    def retainAll(self, elementsToRetain: Iterable[Any]) -> bool:
        ...


    def clear(self) -> None:
        ...


    def elementSet(self) -> set["E"]:
        ...


    def entrySet(self) -> set["Entry"["E"]]:
        ...


    def equals(self, object: "Object") -> bool:
        """
        
        
        This implementation returns `True` if `object` is a multiset of the same size
        and if, for each element, the two multisets have the same count.
        """
        ...


    def hashCode(self) -> int:
        """
        
        
        This implementation returns the hash code of Multiset.entrySet().
        """
        ...


    def toString(self) -> str:
        """
        
        
        This implementation returns the result of invoking `toString` on Multiset.entrySet().
        """
        ...
