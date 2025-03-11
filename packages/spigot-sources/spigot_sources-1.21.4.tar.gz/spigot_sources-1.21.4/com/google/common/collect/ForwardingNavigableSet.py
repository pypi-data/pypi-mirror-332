"""
Python module generated from Java source file com.google.common.collect.ForwardingNavigableSet

Java source file obtained from artifact guava version 33.3.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtIncompatible
from com.google.common.collect import *
from java.util import Iterator
from java.util import NavigableSet
from java.util import SortedSet
from javax.annotation import CheckForNull
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class ForwardingNavigableSet(ForwardingSortedSet, NavigableSet):
    """
    A navigable set which forwards all its method calls to another navigable set. Subclasses should
    override one or more methods to modify the behavior of the backing set as desired per the <a
    href="http://en.wikipedia.org/wiki/Decorator_pattern">decorator pattern</a>.
    
    **Warning:** The methods of `ForwardingNavigableSet` forward *indiscriminately*
    to the methods of the delegate. For example, overriding .add alone *will not* change
    the behavior of .addAll, which can lead to unexpected behavior. In this case, you should
    override `addAll` as well, either providing your own implementation, or delegating to the
    provided `standardAddAll` method.
    
    **`default` method warning:** This class does *not* forward calls to `default` methods. Instead, it inherits their default implementations. When those implementations
    invoke methods, they invoke methods on the `ForwardingNavigableSet`.
    
    Each of the `standard` methods uses the set's comparator (or the natural ordering of the
    elements, if there is no comparator) to test element equality. As a result, if the comparator is
    not consistent with equals, some of the standard implementations may violate the `Set`
    contract.
    
    The `standard` methods and the collection views they return are not guaranteed to be
    thread-safe, even when all of the methods that they depend on are thread-safe.

    Author(s)
    - Louis Wasserman

    Since
    - 12.0
    """

    def lower(self, e: "E") -> "E":
        ...


    def floor(self, e: "E") -> "E":
        ...


    def ceiling(self, e: "E") -> "E":
        ...


    def higher(self, e: "E") -> "E":
        ...


    def pollFirst(self) -> "E":
        ...


    def pollLast(self) -> "E":
        ...


    def descendingSet(self) -> "NavigableSet"["E"]:
        ...


    def descendingIterator(self) -> Iterator["E"]:
        ...


    def subSet(self, fromElement: "E", fromInclusive: bool, toElement: "E", toInclusive: bool) -> "NavigableSet"["E"]:
        ...


    def headSet(self, toElement: "E", inclusive: bool) -> "NavigableSet"["E"]:
        ...


    def tailSet(self, fromElement: "E", inclusive: bool) -> "NavigableSet"["E"]:
        ...
