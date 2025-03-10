"""
Python module generated from Java source file com.google.common.collect.AbstractMapBasedMultiset

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.annotations import GwtIncompatible
from com.google.common.collect import *
from com.google.common.primitives import Ints
from com.google.errorprone.annotations import CanIgnoreReturnValue
from java.io import InvalidObjectException
from java.io import ObjectStreamException
from java.io import Serializable
from java.util import ConcurrentModificationException
from java.util import Iterator
from java.util.function import ObjIntConsumer
from javax.annotation import Nullable
from typing import Any, Callable, Iterable, Tuple


class AbstractMapBasedMultiset(AbstractMultiset, Serializable):
    """
    Basic implementation of `Multiset<E>` backed by an instance of `Map<E, Count>`.
    
    For serialization to work, the subclass must specify explicit `readObject` and `writeObject` methods.

    Author(s)
    - Kevin Bourrillion
    """

    def entrySet(self) -> set["Multiset.Entry"["E"]]:
        """
        
        
        Invoking Multiset.Entry.getCount on an entry in the returned
        set always returns the current count of that element in the multiset, as
        opposed to the count at the time the entry was retrieved.
        """
        ...


    def forEachEntry(self, action: "ObjIntConsumer"["E"]) -> None:
        ...


    def clear(self) -> None:
        ...


    def size(self) -> int:
        ...


    def iterator(self) -> Iterator["E"]:
        ...


    def count(self, element: "Object") -> int:
        ...


    def add(self, element: "E", occurrences: int) -> int:
        """
        Raises
        - IllegalArgumentException: if the call would result in more than
            Integer.MAX_VALUE occurrences of `element` in this
            multiset.
        """
        ...


    def remove(self, element: "Object", occurrences: int) -> int:
        ...


    def setCount(self, element: "E", count: int) -> int:
        ...
