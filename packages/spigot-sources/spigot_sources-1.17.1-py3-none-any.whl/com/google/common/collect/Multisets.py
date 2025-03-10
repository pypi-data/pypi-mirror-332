"""
Python module generated from Java source file com.google.common.collect.Multisets

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.annotations import GwtCompatible
from com.google.common.base import Objects
from com.google.common.base import Predicate
from com.google.common.base import Predicates
from com.google.common.collect import *
from com.google.common.collect.Multiset import Entry
from com.google.common.math import IntMath
from com.google.common.primitives import Ints
from com.google.errorprone.annotations import CanIgnoreReturnValue
from java.io import Serializable
from java.util import Collections
from java.util import Iterator
from java.util import NoSuchElementException
from java.util import Spliterator
from javax.annotation import Nullable
from typing import Any, Callable, Iterable, Tuple


class Multisets:
    """
    Provides static utility methods for creating and working with Multiset instances.
    
    See the Guava User Guide article on <a href=
    "https://github.com/google/guava/wiki/CollectionUtilitiesExplained#multisets">
    `Multisets`</a>.

    Author(s)
    - Louis Wasserman

    Since
    - 2.0
    """

    @staticmethod
    def unmodifiableMultiset(multiset: "Multiset"["E"]) -> "Multiset"["E"]:
        """
        Returns an unmodifiable view of the specified multiset. Query operations on
        the returned multiset "read through" to the specified multiset, and
        attempts to modify the returned multiset result in an
        UnsupportedOperationException.
        
        The returned multiset will be serializable if the specified multiset is
        serializable.

        Arguments
        - multiset: the multiset for which an unmodifiable view is to be
            generated

        Returns
        - an unmodifiable view of the multiset
        """
        ...


    @staticmethod
    def unmodifiableMultiset(multiset: "ImmutableMultiset"["E"]) -> "Multiset"["E"]:
        """
        Simply returns its argument.

        Since
        - 10.0

        Deprecated
        - no need to use this
        """
        ...


    @staticmethod
    def unmodifiableSortedMultiset(sortedMultiset: "SortedMultiset"["E"]) -> "SortedMultiset"["E"]:
        """
        Returns an unmodifiable view of the specified sorted multiset. Query
        operations on the returned multiset "read through" to the specified
        multiset, and attempts to modify the returned multiset result in an UnsupportedOperationException.
        
        The returned multiset will be serializable if the specified multiset is
        serializable.

        Arguments
        - sortedMultiset: the sorted multiset for which an unmodifiable view is
            to be generated

        Returns
        - an unmodifiable view of the multiset

        Since
        - 11.0
        """
        ...


    @staticmethod
    def immutableEntry(e: "E", n: int) -> "Multiset.Entry"["E"]:
        """
        Returns an immutable multiset entry with the specified element and count.
        The entry will be serializable if `e` is.

        Arguments
        - e: the element to be associated with the returned entry
        - n: the count to be associated with the returned entry

        Raises
        - IllegalArgumentException: if `n` is negative
        """
        ...


    @staticmethod
    def filter(unfiltered: "Multiset"["E"], predicate: "Predicate"["E"]) -> "Multiset"["E"]:
        """
        Returns a view of the elements of `unfiltered` that satisfy a predicate. The returned
        multiset is a live view of `unfiltered`; changes to one affect the other.
        
        The resulting multiset's iterators, and those of its `entrySet()` and
        `elementSet()`, do not support `remove()`.  However, all other multiset methods
        supported by `unfiltered` are supported by the returned multiset. When given an element
        that doesn't satisfy the predicate, the multiset's `add()` and `addAll()` methods
        throw an IllegalArgumentException. When methods such as `removeAll()` and
        `clear()` are called on the filtered multiset, only elements that satisfy the filter
        will be removed from the underlying multiset.
        
        The returned multiset isn't threadsafe or serializable, even if `unfiltered` is.
        
        Many of the filtered multiset's methods, such as `size()`, iterate across every
        element in the underlying multiset and determine which elements satisfy the filter. When a
        live view is *not* needed, it may be faster to copy the returned multiset and use the
        copy.
        
        **Warning:** `predicate` must be *consistent with equals*, as documented at
        Predicate.apply. Do not provide a predicate such as
        `Predicates.instanceOf(ArrayList.class)`, which is inconsistent with equals. (See
        Iterables.filter(Iterable, Class) for related functionality.)

        Since
        - 14.0
        """
        ...


    @staticmethod
    def union(multiset1: "Multiset"["E"], multiset2: "Multiset"["E"]) -> "Multiset"["E"]:
        """
        Returns an unmodifiable view of the union of two multisets.
        In the returned multiset, the count of each element is the *maximum*
        of its counts in the two backing multisets. The iteration order of the
        returned multiset matches that of the element set of `multiset1`
        followed by the members of the element set of `multiset2` that are
        not contained in `multiset1`, with repeated occurrences of the same
        element appearing consecutively.
        
        Results are undefined if `multiset1` and `multiset2` are
        based on different equivalence relations (as `HashMultiset` and
        `TreeMultiset` are).

        Since
        - 14.0
        """
        ...


    @staticmethod
    def intersection(multiset1: "Multiset"["E"], multiset2: "Multiset"[Any]) -> "Multiset"["E"]:
        """
        Returns an unmodifiable view of the intersection of two multisets.
        In the returned multiset, the count of each element is the *minimum*
        of its counts in the two backing multisets, with elements that would have
        a count of 0 not included. The iteration order of the returned multiset
        matches that of the element set of `multiset1`, with repeated
        occurrences of the same element appearing consecutively.
        
        Results are undefined if `multiset1` and `multiset2` are
        based on different equivalence relations (as `HashMultiset` and
        `TreeMultiset` are).

        Since
        - 2.0
        """
        ...


    @staticmethod
    def sum(multiset1: "Multiset"["E"], multiset2: "Multiset"["E"]) -> "Multiset"["E"]:
        """
        Returns an unmodifiable view of the sum of two multisets.
        In the returned multiset, the count of each element is the *sum* of
        its counts in the two backing multisets. The iteration order of the
        returned multiset matches that of the element set of `multiset1`
        followed by the members of the element set of `multiset2` that
        are not contained in `multiset1`, with repeated occurrences of the
        same element appearing consecutively.
        
        Results are undefined if `multiset1` and `multiset2` are
        based on different equivalence relations (as `HashMultiset` and
        `TreeMultiset` are).

        Since
        - 14.0
        """
        ...


    @staticmethod
    def difference(multiset1: "Multiset"["E"], multiset2: "Multiset"[Any]) -> "Multiset"["E"]:
        """
        Returns an unmodifiable view of the difference of two multisets.
        In the returned multiset, the count of each element is the result of the
        *zero-truncated subtraction* of its count in the second multiset from
        its count in the first multiset, with elements that would have a count of
        0 not included. The iteration order of the returned multiset matches that
        of the element set of `multiset1`, with repeated occurrences of the
        same element appearing consecutively.
        
        Results are undefined if `multiset1` and `multiset2` are
        based on different equivalence relations (as `HashMultiset` and
        `TreeMultiset` are).

        Since
        - 14.0
        """
        ...


    @staticmethod
    def containsOccurrences(superMultiset: "Multiset"[Any], subMultiset: "Multiset"[Any]) -> bool:
        """
        Returns `True` if `subMultiset.count(o) <=
        superMultiset.count(o)` for all `o`.

        Since
        - 10.0
        """
        ...


    @staticmethod
    def retainOccurrences(multisetToModify: "Multiset"[Any], multisetToRetain: "Multiset"[Any]) -> bool:
        """
        Modifies `multisetToModify` so that its count for an element
        `e` is at most `multisetToRetain.count(e)`.
        
        To be precise, `multisetToModify.count(e)` is set to
        `Math.min(multisetToModify.count(e),
        multisetToRetain.count(e))`. This is similar to
        .intersection(Multiset, Multiset) intersection
        `(multisetToModify, multisetToRetain)`, but mutates
        `multisetToModify` instead of returning a view.
        
        In contrast, `multisetToModify.retainAll(multisetToRetain)` keeps
        all occurrences of elements that appear at all in `multisetToRetain`, and deletes all occurrences of all other elements.

        Returns
        - `True` if `multisetToModify` was changed as a result
                of this operation

        Since
        - 10.0
        """
        ...


    @staticmethod
    def removeOccurrences(multisetToModify: "Multiset"[Any], occurrencesToRemove: Iterable[Any]) -> bool:
        """
        For each occurrence of an element `e` in `occurrencesToRemove`,
        removes one occurrence of `e` in `multisetToModify`.
        
        Equivalently, this method modifies `multisetToModify` so that
        `multisetToModify.count(e)` is set to
        `Math.max(0, multisetToModify.count(e) -
        Iterables.frequency(occurrencesToRemove, e))`.
        
        This is *not* the same as `multisetToModify.`
        Multiset.removeAll removeAll`(occurrencesToRemove)`, which
        removes all occurrences of elements that appear in
        `occurrencesToRemove`. However, this operation *is* equivalent
        to, albeit sometimes more efficient than, the following: ```   `for (E e : occurrencesToRemove) {
            multisetToModify.remove(e);`}```

        Returns
        - `True` if `multisetToModify` was changed as a result of
                this operation

        Since
        - 18.0 (present in 10.0 with a requirement that the second parameter
            be a `Multiset`)
        """
        ...


    @staticmethod
    def removeOccurrences(multisetToModify: "Multiset"[Any], occurrencesToRemove: "Multiset"[Any]) -> bool:
        """
        For each occurrence of an element `e` in `occurrencesToRemove`,
        removes one occurrence of `e` in `multisetToModify`.
        
        Equivalently, this method modifies `multisetToModify` so that
        `multisetToModify.count(e)` is set to
        `Math.max(0, multisetToModify.count(e) -
        occurrencesToRemove.count(e))`.
        
        This is *not* the same as `multisetToModify.`
        Multiset.removeAll removeAll`(occurrencesToRemove)`, which
        removes all occurrences of elements that appear in
        `occurrencesToRemove`. However, this operation *is* equivalent
        to, albeit sometimes more efficient than, the following: ```   `for (E e : occurrencesToRemove) {
            multisetToModify.remove(e);`}```

        Returns
        - `True` if `multisetToModify` was changed as a result of
                this operation

        Since
        - 10.0 (missing in 18.0 when only the overload taking an `Iterable` was present)
        """
        ...


    @staticmethod
    def copyHighestCountFirst(multiset: "Multiset"["E"]) -> "ImmutableMultiset"["E"]:
        """
        Returns a copy of `multiset` as an ImmutableMultiset whose iteration order is
        highest count first, with ties broken by the iteration order of the original multiset.

        Since
        - 11.0
        """
        ...
