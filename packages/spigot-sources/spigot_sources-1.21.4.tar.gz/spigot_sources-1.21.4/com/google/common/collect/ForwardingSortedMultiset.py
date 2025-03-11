"""
Python module generated from Java source file com.google.common.collect.ForwardingSortedMultiset

Java source file obtained from artifact guava version 33.3.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.collect import *
from java.util import Comparator
from java.util import Iterator
from java.util import NavigableSet
from javax.annotation import CheckForNull
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class ForwardingSortedMultiset(ForwardingMultiset, SortedMultiset):
    """
    A sorted multiset which forwards all its method calls to another sorted multiset. Subclasses
    should override one or more methods to modify the behavior of the backing multiset as desired per
    the <a href="http://en.wikipedia.org/wiki/Decorator_pattern">decorator pattern</a>.
    
    **Warning:** The methods of `ForwardingSortedMultiset` forward
    **indiscriminately** to the methods of the delegate. For example, overriding .add(Object, int) alone **will not** change the behavior of .add(Object), which can
    lead to unexpected behavior. In this case, you should override `add(Object)` as well,
    either providing your own implementation, or delegating to the provided `standardAdd`
    method.
    
    **`default` method warning:** This class does *not* forward calls to `default` methods. Instead, it inherits their default implementations. When those implementations
    invoke methods, they invoke methods on the `ForwardingSortedMultiset`.
    
    The `standard` methods and any collection views they return are not guaranteed to be
    thread-safe, even when all of the methods that they depend on are thread-safe.

    Author(s)
    - Louis Wasserman

    Since
    - 15.0
    """

    def elementSet(self) -> "NavigableSet"["E"]:
        ...


    def comparator(self) -> "Comparator"["E"]:
        ...


    def descendingMultiset(self) -> "SortedMultiset"["E"]:
        ...


    def firstEntry(self) -> "Entry"["E"]:
        ...


    def lastEntry(self) -> "Entry"["E"]:
        ...


    def pollFirstEntry(self) -> "Entry"["E"]:
        ...


    def pollLastEntry(self) -> "Entry"["E"]:
        ...


    def headMultiset(self, upperBound: "E", boundType: "BoundType") -> "SortedMultiset"["E"]:
        ...


    def subMultiset(self, lowerBound: "E", lowerBoundType: "BoundType", upperBound: "E", upperBoundType: "BoundType") -> "SortedMultiset"["E"]:
        ...


    def tailMultiset(self, lowerBound: "E", boundType: "BoundType") -> "SortedMultiset"["E"]:
        ...
