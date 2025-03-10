"""
Python module generated from Java source file com.google.common.collect.ForwardingNavigableMap

Java source file obtained from artifact guava version 31.0.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.annotations import GwtIncompatible
from com.google.common.collect import *
from java.util import Iterator
from java.util import NavigableMap
from java.util import NavigableSet
from java.util import NoSuchElementException
from java.util import SortedMap
from java.util.function import BiFunction
from javax.annotation import CheckForNull
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class ForwardingNavigableMap(ForwardingSortedMap, NavigableMap):
    """
    A navigable map which forwards all its method calls to another navigable map. Subclasses should
    override one or more methods to modify the behavior of the backing map as desired per the <a
    href="http://en.wikipedia.org/wiki/Decorator_pattern">decorator pattern</a>.
    
    **Warning:** The methods of `ForwardingNavigableMap` forward *indiscriminately*
    to the methods of the delegate. For example, overriding .put alone *will not* change
    the behavior of .putAll, which can lead to unexpected behavior. In this case, you should
    override `putAll` as well, either providing your own implementation, or delegating to the
    provided `standardPutAll` method.
    
    **`default` method warning:** This class does *not* forward calls to `default` methods. Instead, it inherits their default implementations. When those implementations
    invoke methods, they invoke methods on the `ForwardingNavigableMap`.
    
    Each of the `standard` methods uses the map's comparator (or the natural ordering of the
    elements, if there is no comparator) to test element equality. As a result, if the comparator is
    not consistent with equals, some of the standard implementations may violate the `Map`
    contract.
    
    The `standard` methods and the collection views they return are not guaranteed to be
    thread-safe, even when all of the methods that they depend on are thread-safe.

    Author(s)
    - Louis Wasserman

    Since
    - 12.0
    """

    def lowerEntry(self, key: "K") -> "Entry"["K", "V"]:
        ...


    def lowerKey(self, key: "K") -> "K":
        ...


    def floorEntry(self, key: "K") -> "Entry"["K", "V"]:
        ...


    def floorKey(self, key: "K") -> "K":
        ...


    def ceilingEntry(self, key: "K") -> "Entry"["K", "V"]:
        ...


    def ceilingKey(self, key: "K") -> "K":
        ...


    def higherEntry(self, key: "K") -> "Entry"["K", "V"]:
        ...


    def higherKey(self, key: "K") -> "K":
        ...


    def firstEntry(self) -> "Entry"["K", "V"]:
        ...


    def lastEntry(self) -> "Entry"["K", "V"]:
        ...


    def pollFirstEntry(self) -> "Entry"["K", "V"]:
        ...


    def pollLastEntry(self) -> "Entry"["K", "V"]:
        ...


    def descendingMap(self) -> "NavigableMap"["K", "V"]:
        ...


    def navigableKeySet(self) -> "NavigableSet"["K"]:
        ...


    def descendingKeySet(self) -> "NavigableSet"["K"]:
        ...


    def subMap(self, fromKey: "K", fromInclusive: bool, toKey: "K", toInclusive: bool) -> "NavigableMap"["K", "V"]:
        ...


    def headMap(self, toKey: "K", inclusive: bool) -> "NavigableMap"["K", "V"]:
        ...


    def tailMap(self, fromKey: "K", inclusive: bool) -> "NavigableMap"["K", "V"]:
        ...
