"""
Python module generated from Java source file com.google.common.collect.ForwardingSortedMap

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.annotations import GwtCompatible
from com.google.common.collect import *
from java.util import Comparator
from java.util import NoSuchElementException
from java.util import SortedMap
from javax.annotation import Nullable
from typing import Any, Callable, Iterable, Tuple


class ForwardingSortedMap(ForwardingMap, SortedMap):
    """
    A sorted map which forwards all its method calls to another sorted map.
    Subclasses should override one or more methods to modify the behavior of
    the backing sorted map as desired per the <a
    href="http://en.wikipedia.org/wiki/Decorator_pattern">decorator pattern</a>.
    
    **Warning:** The methods of `ForwardingSortedMap` forward
    *indiscriminately* to the methods of the delegate. For example,
    overriding .put alone *will not* change the behavior of .putAll, which can lead to unexpected behavior. In this case, you should
    override `putAll` as well, either providing your own implementation, or
    delegating to the provided `standardPutAll` method.
    
    **`default` method warning:** This class does *not* forward calls to `default` methods. Instead, it inherits their default implementations. When those implementations
    invoke methods, they invoke methods on the `ForwardingSortedMap`.
    
    Each of the `standard` methods, where appropriate, use the
    comparator of the map to test equality for both keys and values, unlike
    `ForwardingMap`.
    
    The `standard` methods and the collection views they return are not
    guaranteed to be thread-safe, even when all of the methods that they depend
    on are thread-safe.

    Author(s)
    - Louis Wasserman

    Since
    - 2.0
    """

    def comparator(self) -> "Comparator"["K"]:
        ...


    def firstKey(self) -> "K":
        ...


    def headMap(self, toKey: "K") -> "SortedMap"["K", "V"]:
        ...


    def lastKey(self) -> "K":
        ...


    def subMap(self, fromKey: "K", toKey: "K") -> "SortedMap"["K", "V"]:
        ...


    def tailMap(self, fromKey: "K") -> "SortedMap"["K", "V"]:
        ...
