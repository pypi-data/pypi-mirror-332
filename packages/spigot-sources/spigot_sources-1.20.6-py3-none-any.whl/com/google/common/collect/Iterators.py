"""
Python module generated from Java source file com.google.common.collect.Iterators

Java source file obtained from artifact guava version 32.1.2-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.annotations import GwtIncompatible
from com.google.common.base import Function
from com.google.common.base import Objects
from com.google.common.base import Optional
from com.google.common.base import Preconditions
from com.google.common.base import Predicate
from com.google.common.collect import *
from com.google.common.primitives import Ints
from com.google.errorprone.annotations import CanIgnoreReturnValue
from java.util import ArrayDeque
from java.util import Arrays
from java.util import Collections
from java.util import Comparator
from java.util import Deque
from java.util import Enumeration
from java.util import Iterator
from java.util import ListIterator
from java.util import NoSuchElementException
from java.util import PriorityQueue
from java.util import Queue
from javax.annotation import CheckForNull
from org.checkerframework.checker.nullness.qual import NonNull
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class Iterators:
    """
    This class contains static utility methods that operate on or return objects of type Iterator. Except as noted, each method has a corresponding Iterable-based method in the
    Iterables class.
    
    *Performance notes:* Unless otherwise noted, all of the iterators produced in this class
    are *lazy*, which means that they only advance the backing iteration when absolutely
    necessary.
    
    See the Guava User Guide section on <a href=
    "https://github.com/google/guava/wiki/CollectionUtilitiesExplained#iterables">`Iterators`</a>.

    Author(s)
    - Jared Levy

    Since
    - 2.0
    """

    @staticmethod
    def unmodifiableIterator(iterator: Iterator["T"]) -> "UnmodifiableIterator"["T"]:
        """
        Returns an unmodifiable view of `iterator`.
        """
        ...


    @staticmethod
    def unmodifiableIterator(iterator: "UnmodifiableIterator"["T"]) -> "UnmodifiableIterator"["T"]:
        """
        Simply returns its argument.

        Since
        - 10.0

        Deprecated
        - no need to use this
        """
        ...


    @staticmethod
    def size(iterator: Iterator[Any]) -> int:
        """
        Returns the number of elements remaining in `iterator`. The iterator will be left
        exhausted: its `hasNext()` method will return `False`.
        """
        ...


    @staticmethod
    def contains(iterator: Iterator[Any], element: "Object") -> bool:
        """
        Returns `True` if `iterator` contains `element`.
        """
        ...


    @staticmethod
    def removeAll(removeFrom: Iterator[Any], elementsToRemove: Iterable[Any]) -> bool:
        """
        Traverses an iterator and removes every element that belongs to the provided collection. The
        iterator will be left exhausted: its `hasNext()` method will return `False`.

        Arguments
        - removeFrom: the iterator to (potentially) remove elements from
        - elementsToRemove: the elements to remove

        Returns
        - `True` if any element was removed from `iterator`
        """
        ...


    @staticmethod
    def removeIf(removeFrom: Iterator["T"], predicate: "Predicate"["T"]) -> bool:
        """
        Removes every element that satisfies the provided predicate from the iterator. The iterator
        will be left exhausted: its `hasNext()` method will return `False`.

        Arguments
        - removeFrom: the iterator to (potentially) remove elements from
        - predicate: a predicate that determines whether an element should be removed

        Returns
        - `True` if any elements were removed from the iterator

        Since
        - 2.0
        """
        ...


    @staticmethod
    def retainAll(removeFrom: Iterator[Any], elementsToRetain: Iterable[Any]) -> bool:
        """
        Traverses an iterator and removes every element that does not belong to the provided
        collection. The iterator will be left exhausted: its `hasNext()` method will return
        `False`.

        Arguments
        - removeFrom: the iterator to (potentially) remove elements from
        - elementsToRetain: the elements to retain

        Returns
        - `True` if any element was removed from `iterator`
        """
        ...


    @staticmethod
    def elementsEqual(iterator1: Iterator[Any], iterator2: Iterator[Any]) -> bool:
        """
        Determines whether two iterators contain equal elements in the same order. More specifically,
        this method returns `True` if `iterator1` and `iterator2` contain the same
        number of elements and every element of `iterator1` is equal to the corresponding element
        of `iterator2`.
        
        Note that this will modify the supplied iterators, since they will have been advanced some
        number of elements forward.
        """
        ...


    @staticmethod
    def toString(iterator: Iterator[Any]) -> str:
        """
        Returns a string representation of `iterator`, with the format `[e1, e2, ..., en]`.
        The iterator will be left exhausted: its `hasNext()` method will return `False`.
        """
        ...


    @staticmethod
    def getOnlyElement(iterator: Iterator["T"]) -> "T":
        """
        Returns the single element contained in `iterator`.

        Raises
        - NoSuchElementException: if the iterator is empty
        - IllegalArgumentException: if the iterator contains multiple elements. The state of the
            iterator is unspecified.
        """
        ...


    @staticmethod
    def getOnlyElement(iterator: Iterator["T"], defaultValue: "T") -> "T":
        """
        Returns the single element contained in `iterator`, or `defaultValue` if the
        iterator is empty.

        Raises
        - IllegalArgumentException: if the iterator contains multiple elements. The state of the
            iterator is unspecified.
        """
        ...


    @staticmethod
    def toArray(iterator: Iterator["T"], type: type["T"]) -> list["T"]:
        """
        Copies an iterator's elements into an array. The iterator will be left exhausted: its `hasNext()` method will return `False`.

        Arguments
        - iterator: the iterator to copy
        - type: the type of the elements

        Returns
        - a newly-allocated array into which all the elements of the iterator have been copied
        """
        ...


    @staticmethod
    def addAll(addTo: Iterable["T"], iterator: Iterator["T"]) -> bool:
        """
        Adds all elements in `iterator` to `collection`. The iterator will be left
        exhausted: its `hasNext()` method will return `False`.

        Returns
        - `True` if `collection` was modified as a result of this operation
        """
        ...


    @staticmethod
    def frequency(iterator: Iterator[Any], element: "Object") -> int:
        """
        Returns the number of elements in the specified iterator that equal the specified object. The
        iterator will be left exhausted: its `hasNext()` method will return `False`.

        See
        - Collections.frequency
        """
        ...


    @staticmethod
    def cycle(iterable: Iterable["T"]) -> Iterator["T"]:
        """
        Returns an iterator that cycles indefinitely over the elements of `iterable`.
        
        The returned iterator supports `remove()` if the provided iterator does. After `remove()` is called, subsequent cycles omit the removed element, which is no longer in `iterable`. The iterator's `hasNext()` method returns `True` until `iterable`
        is empty.
        
        **Warning:** Typical uses of the resulting iterator may produce an infinite loop. You
        should use an explicit `break` or be certain that you will eventually remove all the
        elements.
        """
        ...


    @staticmethod
    def cycle(*elements: Tuple["T", ...]) -> Iterator["T"]:
        """
        Returns an iterator that cycles indefinitely over the provided elements.
        
        The returned iterator supports `remove()`. After `remove()` is called,
        subsequent cycles omit the removed element, but `elements` does not change. The
        iterator's `hasNext()` method returns `True` until all of the original elements
        have been removed.
        
        **Warning:** Typical uses of the resulting iterator may produce an infinite loop. You
        should use an explicit `break` or be certain that you will eventually remove all the
        elements.
        """
        ...


    @staticmethod
    def concat(a: Iterator["T"], b: Iterator["T"]) -> Iterator["T"]:
        """
        Combines two iterators into a single iterator. The returned iterator iterates across the
        elements in `a`, followed by the elements in `b`. The source iterators are not
        polled until necessary.
        
        The returned iterator supports `remove()` when the corresponding input iterator
        supports it.
        """
        ...


    @staticmethod
    def concat(a: Iterator["T"], b: Iterator["T"], c: Iterator["T"]) -> Iterator["T"]:
        """
        Combines three iterators into a single iterator. The returned iterator iterates across the
        elements in `a`, followed by the elements in `b`, followed by the elements in
        `c`. The source iterators are not polled until necessary.
        
        The returned iterator supports `remove()` when the corresponding input iterator
        supports it.
        """
        ...


    @staticmethod
    def concat(a: Iterator["T"], b: Iterator["T"], c: Iterator["T"], d: Iterator["T"]) -> Iterator["T"]:
        """
        Combines four iterators into a single iterator. The returned iterator iterates across the
        elements in `a`, followed by the elements in `b`, followed by the elements in
        `c`, followed by the elements in `d`. The source iterators are not polled until
        necessary.
        
        The returned iterator supports `remove()` when the corresponding input iterator
        supports it.
        """
        ...


    @staticmethod
    def concat(*inputs: Tuple[Iterator["T"], ...]) -> Iterator["T"]:
        """
        Combines multiple iterators into a single iterator. The returned iterator iterates across the
        elements of each iterator in `inputs`. The input iterators are not polled until
        necessary.
        
        The returned iterator supports `remove()` when the corresponding input iterator
        supports it.

        Raises
        - NullPointerException: if any of the provided iterators is null
        """
        ...


    @staticmethod
    def concat(inputs: Iterator[Iterator["T"]]) -> Iterator["T"]:
        """
        Combines multiple iterators into a single iterator. The returned iterator iterates across the
        elements of each iterator in `inputs`. The input iterators are not polled until
        necessary.
        
        The returned iterator supports `remove()` when the corresponding input iterator
        supports it. The methods of the returned iterator may throw `NullPointerException` if any
        of the input iterators is null.
        """
        ...


    @staticmethod
    def partition(iterator: Iterator["T"], size: int) -> "UnmodifiableIterator"[list["T"]]:
        """
        Divides an iterator into unmodifiable sublists of the given size (the final list may be
        smaller). For example, partitioning an iterator containing `[a, b, c, d, e]` with a
        partition size of 3 yields `[[a, b, c], [d, e]]` -- an outer iterator containing two
        inner lists of three and two elements, all in the original order.
        
        The returned lists implement java.util.RandomAccess.
        
        **Note:** The current implementation eagerly allocates storage for `size` elements.
        As a consequence, passing values like `Integer.MAX_VALUE` can lead to OutOfMemoryError.

        Arguments
        - iterator: the iterator to return a partitioned view of
        - size: the desired size of each partition (the last may be smaller)

        Returns
        - an iterator of immutable lists containing the elements of `iterator` divided into
            partitions

        Raises
        - IllegalArgumentException: if `size` is nonpositive
        """
        ...


    @staticmethod
    def paddedPartition(iterator: Iterator["T"], size: int) -> "UnmodifiableIterator"[list["T"]]:
        """
        Divides an iterator into unmodifiable sublists of the given size, padding the final iterator
        with null values if necessary. For example, partitioning an iterator containing `[a, b,
        c, d, e]` with a partition size of 3 yields `[[a, b, c], [d, e, null]]` -- an outer
        iterator containing two inner lists of three elements each, all in the original order.
        
        The returned lists implement java.util.RandomAccess.

        Arguments
        - iterator: the iterator to return a partitioned view of
        - size: the desired size of each partition

        Returns
        - an iterator of immutable lists containing the elements of `iterator` divided into
            partitions (the final iterable may have trailing null elements)

        Raises
        - IllegalArgumentException: if `size` is nonpositive
        """
        ...


    @staticmethod
    def filter(unfiltered: Iterator["T"], retainIfTrue: "Predicate"["T"]) -> "UnmodifiableIterator"["T"]:
        """
        Returns a view of `unfiltered` containing all elements that satisfy the input predicate
        `retainIfTrue`.
        """
        ...


    @staticmethod
    def filter(unfiltered: Iterator[Any], desiredType: type["T"]) -> "UnmodifiableIterator"["T"]:
        """
        Returns a view of `unfiltered` containing all elements that are of the type `desiredType`.
        """
        ...


    @staticmethod
    def any(iterator: Iterator["T"], predicate: "Predicate"["T"]) -> bool:
        """
        Returns `True` if one or more elements returned by `iterator` satisfy the given
        predicate.
        """
        ...


    @staticmethod
    def all(iterator: Iterator["T"], predicate: "Predicate"["T"]) -> bool:
        """
        Returns `True` if every element returned by `iterator` satisfies the given
        predicate. If `iterator` is empty, `True` is returned.
        """
        ...


    @staticmethod
    def find(iterator: Iterator["T"], predicate: "Predicate"["T"]) -> "T":
        """
        Returns the first element in `iterator` that satisfies the given predicate; use this
        method only when such an element is known to exist. If no such element is found, the iterator
        will be left exhausted: its `hasNext()` method will return `False`. If it is
        possible that *no* element will match, use .tryFind or .find(Iterator,
        Predicate, Object) instead.

        Raises
        - NoSuchElementException: if no element in `iterator` matches the given predicate
        """
        ...


    @staticmethod
    def find(iterator: Iterator["T"], predicate: "Predicate"["T"], defaultValue: "T") -> "T":
        ...


    @staticmethod
    def tryFind(iterator: Iterator["T"], predicate: "Predicate"["T"]) -> "Optional"["T"]:
        """
        Returns an Optional containing the first element in `iterator` that satisfies the
        given predicate, if such an element exists. If no such element is found, an empty Optional will be returned from this method and the iterator will be left exhausted: its `hasNext()` method will return `False`.
        
        **Warning:** avoid using a `predicate` that matches `null`. If `null`
        is matched in `iterator`, a NullPointerException will be thrown.

        Since
        - 11.0
        """
        ...


    @staticmethod
    def indexOf(iterator: Iterator["T"], predicate: "Predicate"["T"]) -> int:
        """
        Returns the index in `iterator` of the first element that satisfies the provided `predicate`, or `-1` if the Iterator has no such elements.
        
        More formally, returns the lowest index `i` such that `predicate.apply(Iterators.get(iterator, i))` returns `True`, or `-1` if there is no
        such index.
        
        If -1 is returned, the iterator will be left exhausted: its `hasNext()` method will
        return `False`. Otherwise, the iterator will be set to the element which satisfies the
        `predicate`.

        Since
        - 2.0
        """
        ...


    @staticmethod
    def transform(fromIterator: Iterator["F"], function: "Function"["F", "T"]) -> Iterator["T"]:
        """
        Returns a view containing the result of applying `function` to each element of `fromIterator`.
        
        The returned iterator supports `remove()` if `fromIterator` does. After a
        successful `remove()` call, `fromIterator` no longer contains the corresponding
        element.
        """
        ...


    @staticmethod
    def get(iterator: Iterator["T"], position: int) -> "T":
        """
        Advances `iterator` `position + 1` times, returning the element at the `position`th position.

        Arguments
        - position: position of the element to return

        Returns
        - the element at the specified position in `iterator`

        Raises
        - IndexOutOfBoundsException: if `position` is negative or greater than or equal to
            the number of elements remaining in `iterator`
        """
        ...


    @staticmethod
    def get(iterator: Iterator["T"], position: int, defaultValue: "T") -> "T":
        """
        Advances `iterator` `position + 1` times, returning the element at the `position`th position or `defaultValue` otherwise.

        Arguments
        - position: position of the element to return
        - defaultValue: the default value to return if the iterator is empty or if `position`
            is greater than the number of elements remaining in `iterator`

        Returns
        - the element at the specified position in `iterator` or `defaultValue` if
            `iterator` produces fewer than `position + 1` elements.

        Raises
        - IndexOutOfBoundsException: if `position` is negative

        Since
        - 4.0
        """
        ...


    @staticmethod
    def getNext(iterator: Iterator["T"], defaultValue: "T") -> "T":
        """
        Returns the next element in `iterator` or `defaultValue` if the iterator is empty.
        The Iterables analog to this method is Iterables.getFirst.

        Arguments
        - defaultValue: the default value to return if the iterator is empty

        Returns
        - the next element of `iterator` or the default value

        Since
        - 7.0
        """
        ...


    @staticmethod
    def getLast(iterator: Iterator["T"]) -> "T":
        """
        Advances `iterator` to the end, returning the last element.

        Returns
        - the last element of `iterator`

        Raises
        - NoSuchElementException: if the iterator is empty
        """
        ...


    @staticmethod
    def getLast(iterator: Iterator["T"], defaultValue: "T") -> "T":
        """
        Advances `iterator` to the end, returning the last element or `defaultValue` if the
        iterator is empty.

        Arguments
        - defaultValue: the default value to return if the iterator is empty

        Returns
        - the last element of `iterator`

        Since
        - 3.0
        """
        ...


    @staticmethod
    def advance(iterator: Iterator[Any], numberToAdvance: int) -> int:
        """
        Calls `next()` on `iterator`, either `numberToAdvance` times or until `hasNext()` returns `False`, whichever comes first.

        Returns
        - the number of elements the iterator was advanced

        Since
        - 13.0 (since 3.0 as `Iterators.skip`)
        """
        ...


    @staticmethod
    def limit(iterator: Iterator["T"], limitSize: int) -> Iterator["T"]:
        """
        Returns a view containing the first `limitSize` elements of `iterator`. If `iterator` contains fewer than `limitSize` elements, the returned view contains all of its
        elements. The returned iterator supports `remove()` if `iterator` does.

        Arguments
        - iterator: the iterator to limit
        - limitSize: the maximum number of elements in the returned iterator

        Raises
        - IllegalArgumentException: if `limitSize` is negative

        Since
        - 3.0
        """
        ...


    @staticmethod
    def consumingIterator(iterator: Iterator["T"]) -> Iterator["T"]:
        """
        Returns a view of the supplied `iterator` that removes each element from the supplied
        `iterator` as it is returned.
        
        The provided iterator must support Iterator.remove() or else the returned iterator
        will fail on the first call to `next`. The returned Iterator is also not
        thread-safe.

        Arguments
        - iterator: the iterator to remove and return elements from

        Returns
        - an iterator that removes and returns elements from the supplied iterator

        Since
        - 2.0
        """
        ...


    @staticmethod
    def forArray(*array: Tuple["T", ...]) -> "UnmodifiableIterator"["T"]:
        """
        Returns an iterator containing the elements of `array` in order. The returned iterator is
        a view of the array; subsequent changes to the array will be reflected in the iterator.
        
        **Note:** It is often preferable to represent your data using a collection type, for
        example using Arrays.asList(Object[]), making this method unnecessary.
        
        The `Iterable` equivalent of this method is either Arrays.asList(Object[]),
        ImmutableList.copyOf(Object[])}, or ImmutableList.of.
        """
        ...


    @staticmethod
    def singletonIterator(value: "T") -> "UnmodifiableIterator"["T"]:
        """
        Returns an iterator containing only `value`.
        
        The Iterable equivalent of this method is Collections.singleton.
        """
        ...


    @staticmethod
    def forEnumeration(enumeration: "Enumeration"["T"]) -> "UnmodifiableIterator"["T"]:
        """
        Adapts an `Enumeration` to the `Iterator` interface.
        
        This method has no equivalent in Iterables because viewing an `Enumeration` as
        an `Iterable` is impossible. However, the contents can be *copied* into a collection
        using Collections.list.
        
        **Java 9 users:** use `enumeration.asIterator()` instead, unless it is important to
        return an `UnmodifiableIterator` instead of a plain `Iterator`.
        """
        ...


    @staticmethod
    def asEnumeration(iterator: Iterator["T"]) -> "Enumeration"["T"]:
        """
        Adapts an `Iterator` to the `Enumeration` interface.
        
        The `Iterable` equivalent of this method is either Collections.enumeration (if
        you have a Collection), or `Iterators.asEnumeration(collection.iterator())`.
        """
        ...


    @staticmethod
    def peekingIterator(iterator: Iterator["T"]) -> "PeekingIterator"["T"]:
        """
        Returns a `PeekingIterator` backed by the given iterator.
        
        Calls to the `peek` method with no intervening calls to `next` do not affect the
        iteration, and hence return the same object each time. A subsequent call to `next` is
        guaranteed to return the same object again. For example:
        
        ````PeekingIterator<String> peekingIterator =
            Iterators.peekingIterator(Iterators.forArray("a", "b"));
        String a1 = peekingIterator.peek(); // returns "a"
        String a2 = peekingIterator.peek(); // also returns "a"
        String a3 = peekingIterator.next(); // also returns "a"````
        
        Any structural changes to the underlying iteration (aside from those performed by the
        iterator's own PeekingIterator.remove() method) will leave the iterator in an undefined
        state.
        
        The returned iterator does not support removal after peeking, as explained by PeekingIterator.remove().
        
        Note: If the given iterator is already a `PeekingIterator`, it *might* be
        returned to the caller, although this is neither guaranteed to occur nor required to be
        consistent. For example, this method *might* choose to pass through recognized
        implementations of `PeekingIterator` when the behavior of the implementation is known to
        meet the contract guaranteed by this method.
        
        There is no Iterable equivalent to this method, so use this method to wrap each
        individual iterator as it is generated.

        Arguments
        - iterator: the backing iterator. The PeekingIterator assumes ownership of this
            iterator, so users should cease making direct calls to it after calling this method.

        Returns
        - a peeking iterator backed by that iterator. Apart from the additional PeekingIterator.peek() method, this iterator behaves exactly the same as `iterator`.
        """
        ...


    @staticmethod
    def peekingIterator(iterator: "PeekingIterator"["T"]) -> "PeekingIterator"["T"]:
        """
        Simply returns its argument.

        Since
        - 10.0

        Deprecated
        - no need to use this
        """
        ...


    @staticmethod
    def mergeSorted(iterators: Iterable[Iterator["T"]], comparator: "Comparator"["T"]) -> "UnmodifiableIterator"["T"]:
        """
        Returns an iterator over the merged contents of all given `iterators`, traversing every
        element of the input iterators. Equivalent entries will not be de-duplicated.
        
        Callers must ensure that the source `iterators` are in non-descending order as this
        method does not sort its input.
        
        For any equivalent elements across all `iterators`, it is undefined which element is
        returned first.

        Since
        - 11.0
        """
        ...
