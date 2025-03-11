"""
Python module generated from Java source file com.google.common.collect.SortedMultiset

Java source file obtained from artifact guava version 32.1.2-jre

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


class SortedMultiset(SortedMultisetBridge, SortedIterable):
    """
    A Multiset which maintains the ordering of its elements, according to either their
    natural order or an explicit Comparator. This order is reflected when iterating over the
    sorted multiset, either directly, or through its `elementSet` or `entrySet` views. In
    all cases, this implementation uses Comparable.compareTo or Comparator.compare
    instead of Object.equals to determine equivalence of instances.
    
    **Warning:** The comparison must be *consistent with equals* as explained by the
    Comparable class specification. Otherwise, the resulting multiset will violate the Collection contract, which is specified in terms of Object.equals.
    
    See the Guava User Guide article on <a href=
    "https://github.com/google/guava/wiki/NewCollectionTypesExplained#multiset">`Multiset`</a>.

    Author(s)
    - Louis Wasserman

    Since
    - 11.0
    """

    def comparator(self) -> "Comparator"["E"]:
        """
        Returns the comparator that orders this multiset, or Ordering.natural() if the natural
        ordering of the elements is used.
        """
        ...


    def firstEntry(self) -> "Entry"["E"]:
        """
        Returns the entry of the first element in this multiset, or `null` if this multiset is
        empty.
        """
        ...


    def lastEntry(self) -> "Entry"["E"]:
        """
        Returns the entry of the last element in this multiset, or `null` if this multiset is
        empty.
        """
        ...


    def pollFirstEntry(self) -> "Entry"["E"]:
        """
        Returns and removes the entry associated with the lowest element in this multiset, or returns
        `null` if this multiset is empty.
        """
        ...


    def pollLastEntry(self) -> "Entry"["E"]:
        """
        Returns and removes the entry associated with the greatest element in this multiset, or returns
        `null` if this multiset is empty.
        """
        ...


    def elementSet(self) -> "NavigableSet"["E"]:
        """
        Returns a NavigableSet view of the distinct elements in this multiset.

        Since
        - 14.0 (present with return type `SortedSet` since 11.0)
        """
        ...


    def entrySet(self) -> set["Entry"["E"]]:
        """
        
        
        The `entrySet`'s iterator returns entries in ascending element order according to this
        multiset's comparator.
        """
        ...


    def iterator(self) -> Iterator["E"]:
        """
        
        
        The iterator returns the elements in ascending order according to this multiset's
        comparator.
        """
        ...


    def descendingMultiset(self) -> "SortedMultiset"["E"]:
        """
        Returns a descending view of this multiset. Modifications made to either map will be reflected
        in the other.
        """
        ...


    def headMultiset(self, upperBound: "E", boundType: "BoundType") -> "SortedMultiset"["E"]:
        """
        Returns a view of this multiset restricted to the elements less than `upperBound`,
        optionally including `upperBound` itself. The returned multiset is a view of this
        multiset, so changes to one will be reflected in the other. The returned multiset supports all
        operations that this multiset supports.
        
        The returned multiset will throw an IllegalArgumentException on attempts to add
        elements outside its range.
        """
        ...


    def subMultiset(self, lowerBound: "E", lowerBoundType: "BoundType", upperBound: "E", upperBoundType: "BoundType") -> "SortedMultiset"["E"]:
        """
        Returns a view of this multiset restricted to the range between `lowerBound` and `upperBound`. The returned multiset is a view of this multiset, so changes to one will be
        reflected in the other. The returned multiset supports all operations that this multiset
        supports.
        
        The returned multiset will throw an IllegalArgumentException on attempts to add
        elements outside its range.
        
        This method is equivalent to `tailMultiset(lowerBound,
        lowerBoundType).headMultiset(upperBound, upperBoundType)`.
        """
        ...


    def tailMultiset(self, lowerBound: "E", boundType: "BoundType") -> "SortedMultiset"["E"]:
        """
        Returns a view of this multiset restricted to the elements greater than `lowerBound`,
        optionally including `lowerBound` itself. The returned multiset is a view of this
        multiset, so changes to one will be reflected in the other. The returned multiset supports all
        operations that this multiset supports.
        
        The returned multiset will throw an IllegalArgumentException on attempts to add
        elements outside its range.
        """
        ...
