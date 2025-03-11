"""
Python module generated from Java source file com.google.common.collect.Iterables

Java source file obtained from artifact guava version 33.3.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.annotations import GwtIncompatible
from com.google.common.base import Function
from com.google.common.base import Optional
from com.google.common.base import Predicate
from com.google.common.base import Predicates
from com.google.common.collect import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from java.util import Comparator
from java.util import Iterator
from java.util import NoSuchElementException
from java.util import Queue
from java.util import RandomAccess
from java.util import Spliterator
from java.util.function import Consumer
from java.util.stream import Stream
from javax.annotation import CheckForNull
from org.checkerframework.checker.nullness.qual import NonNull
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class Iterables:
    """
    An assortment of mainly legacy static utility methods that operate on or return objects of type
    `Iterable`. Except as noted, each method has a corresponding Iterator-based method
    in the Iterators class.
    
    **Java 8+ users:** several common uses for this class are now more comprehensively
    addressed by the new java.util.stream.Stream library. Read the method documentation below
    for comparisons. This class is not being deprecated, but we gently encourage you to migrate to
    streams.
    
    *Performance notes:* Unless otherwise noted, all of the iterables produced in this class
    are *lazy*, which means that their iterators only advance the backing iteration when
    absolutely necessary.
    
    See the Guava User Guide article on <a href=
    "https://github.com/google/guava/wiki/CollectionUtilitiesExplained#iterables">`Iterables`</a>.

    Author(s)
    - Jared Levy

    Since
    - 2.0
    """

    @staticmethod
    def unmodifiableIterable(iterable: Iterable["T"]) -> Iterable["T"]:
        """
        Returns an unmodifiable view of `iterable`.
        """
        ...


    @staticmethod
    def unmodifiableIterable(iterable: "ImmutableCollection"["E"]) -> Iterable["E"]:
        """
        Simply returns its argument.

        Since
        - 10.0

        Deprecated
        - no need to use this
        """
        ...


    @staticmethod
    def size(iterable: Iterable[Any]) -> int:
        """
        Returns the number of elements in `iterable`.
        """
        ...


    @staticmethod
    def contains(iterable: Iterable["Object"], element: "Object") -> bool:
        ...


    @staticmethod
    def removeAll(removeFrom: Iterable[Any], elementsToRemove: Iterable[Any]) -> bool:
        """
        Removes, from an iterable, every element that belongs to the provided collection.
        
        This method calls Collection.removeAll if `iterable` is a collection, and
        Iterators.removeAll otherwise.

        Arguments
        - removeFrom: the iterable to (potentially) remove elements from
        - elementsToRemove: the elements to remove

        Returns
        - `True` if any element was removed from `iterable`
        """
        ...


    @staticmethod
    def retainAll(removeFrom: Iterable[Any], elementsToRetain: Iterable[Any]) -> bool:
        """
        Removes, from an iterable, every element that does not belong to the provided collection.
        
        This method calls Collection.retainAll if `iterable` is a collection, and
        Iterators.retainAll otherwise.

        Arguments
        - removeFrom: the iterable to (potentially) remove elements from
        - elementsToRetain: the elements to retain

        Returns
        - `True` if any element was removed from `iterable`
        """
        ...


    @staticmethod
    def removeIf(removeFrom: Iterable["T"], predicate: "Predicate"["T"]) -> bool:
        """
        Removes, from an iterable, every element that satisfies the provided predicate.
        
        Removals may or may not happen immediately as each element is tested against the predicate.
        The behavior of this method is not specified if `predicate` is dependent on `removeFrom`.
        
        **Java 8+ users:** if `removeFrom` is a Collection, use `removeFrom.removeIf(predicate)` instead.

        Arguments
        - removeFrom: the iterable to (potentially) remove elements from
        - predicate: a predicate that determines whether an element should be removed

        Returns
        - `True` if any elements were removed from the iterable

        Raises
        - UnsupportedOperationException: if the iterable does not support `remove()`.

        Since
        - 2.0
        """
        ...


    @staticmethod
    def elementsEqual(iterable1: Iterable[Any], iterable2: Iterable[Any]) -> bool:
        """
        Determines whether two iterables contain equal elements in the same order. More specifically,
        this method returns `True` if `iterable1` and `iterable2` contain the same
        number of elements and every element of `iterable1` is equal to the corresponding element
        of `iterable2`.
        """
        ...


    @staticmethod
    def toString(iterable: Iterable[Any]) -> str:
        """
        Returns a string representation of `iterable`, with the format `[e1, e2, ..., en]`
        (that is, identical to java.util.Arrays Arrays`.toString(Iterables.toArray(iterable))`). Note that for *most* implementations of Collection, `collection.toString()` also gives the same result, but that behavior is not
        generally guaranteed.
        """
        ...


    @staticmethod
    def getOnlyElement(iterable: Iterable["T"]) -> "T":
        """
        Returns the single element contained in `iterable`.
        
        **Java 8+ users:** the `Stream` equivalent to this method is `stream.collect(MoreCollectors.onlyElement())`.

        Raises
        - NoSuchElementException: if the iterable is empty
        - IllegalArgumentException: if the iterable contains multiple elements
        """
        ...


    @staticmethod
    def getOnlyElement(iterable: Iterable["T"], defaultValue: "T") -> "T":
        """
        Returns the single element contained in `iterable`, or `defaultValue` if the
        iterable is empty.
        
        **Java 8+ users:** the `Stream` equivalent to this method is `stream.collect(MoreCollectors.toOptional()).orElse(defaultValue)`.

        Raises
        - IllegalArgumentException: if the iterator contains multiple elements
        """
        ...


    @staticmethod
    def toArray(iterable: Iterable["T"], type: type["T"]) -> list["T"]:
        """
        Copies an iterable's elements into an array.

        Arguments
        - iterable: the iterable to copy
        - type: the type of the elements

        Returns
        - a newly-allocated array into which all the elements of the iterable have been copied
        """
        ...


    @staticmethod
    def addAll(addTo: Iterable["T"], elementsToAdd: Iterable["T"]) -> bool:
        """
        Adds all elements in `iterable` to `collection`.

        Returns
        - `True` if `collection` was modified as a result of this operation.
        """
        ...


    @staticmethod
    def frequency(iterable: Iterable[Any], element: "Object") -> int:
        """
        Returns the number of elements in the specified iterable that equal the specified object. This
        implementation avoids a full iteration when the iterable is a Multiset or Set.
        
        **Java 8+ users:** In most cases, the `Stream` equivalent of this method is `stream.filter(element::equals).count()`. If `element` might be null, use `stream.filter(Predicate.isEqual(element)).count()` instead.

        See
        - java.util.Collections.frequency(Collection, Object) Collections.frequency(Collection,
            Object)
        """
        ...


    @staticmethod
    def cycle(iterable: Iterable["T"]) -> Iterable["T"]:
        """
        Returns an iterable whose iterators cycle indefinitely over the elements of `iterable`.
        
        That iterator supports `remove()` if `iterable.iterator()` does. After `remove()` is called, subsequent cycles omit the removed element, which is no longer in `iterable`. The iterator's `hasNext()` method returns `True` until `iterable`
        is empty.
        
        **Warning:** Typical uses of the resulting iterator may produce an infinite loop. You
        should use an explicit `break` or be certain that you will eventually remove all the
        elements.
        
        To cycle over the iterable `n` times, use the following: `Iterables.concat(Collections.nCopies(n, iterable))`
        
        **Java 8+ users:** The `Stream` equivalent of this method is `Stream.generate(() -> iterable).flatMap(Streams::stream)`.
        """
        ...


    @staticmethod
    def cycle(*elements: Tuple["T", ...]) -> Iterable["T"]:
        """
        Returns an iterable whose iterators cycle indefinitely over the provided elements.
        
        After `remove` is invoked on a generated iterator, the removed element will no longer
        appear in either that iterator or any other iterator created from the same source iterable.
        That is, this method behaves exactly as `Iterables.cycle(Lists.newArrayList(elements))`.
        The iterator's `hasNext` method returns `True` until all of the original elements
        have been removed.
        
        **Warning:** Typical uses of the resulting iterator may produce an infinite loop. You
        should use an explicit `break` or be certain that you will eventually remove all the
        elements.
        
        To cycle over the elements `n` times, use the following: `Iterables.concat(Collections.nCopies(n, Arrays.asList(elements)))`
        
        **Java 8+ users:** If passing a single element `e`, the `Stream` equivalent
        of this method is `Stream.generate(() -> e)`. Otherwise, put the elements in a collection
        and use `Stream.generate(() -> collection).flatMap(Collection::stream)`.
        """
        ...


    @staticmethod
    def concat(a: Iterable["T"], b: Iterable["T"]) -> Iterable["T"]:
        """
        Combines two iterables into a single iterable. The returned iterable has an iterator that
        traverses the elements in `a`, followed by the elements in `b`. The source
        iterators are not polled until necessary.
        
        The returned iterable's iterator supports `remove()` when the corresponding input
        iterator supports it.
        
        **Java 8+ users:** The `Stream` equivalent of this method is `Stream.concat(a, b)`.
        """
        ...


    @staticmethod
    def concat(a: Iterable["T"], b: Iterable["T"], c: Iterable["T"]) -> Iterable["T"]:
        """
        Combines three iterables into a single iterable. The returned iterable has an iterator that
        traverses the elements in `a`, followed by the elements in `b`, followed by the
        elements in `c`. The source iterators are not polled until necessary.
        
        The returned iterable's iterator supports `remove()` when the corresponding input
        iterator supports it.
        
        **Java 8+ users:** The `Stream` equivalent of this method is `Streams.concat(a, b, c)`.
        """
        ...


    @staticmethod
    def concat(a: Iterable["T"], b: Iterable["T"], c: Iterable["T"], d: Iterable["T"]) -> Iterable["T"]:
        """
        Combines four iterables into a single iterable. The returned iterable has an iterator that
        traverses the elements in `a`, followed by the elements in `b`, followed by the
        elements in `c`, followed by the elements in `d`. The source iterators are not
        polled until necessary.
        
        The returned iterable's iterator supports `remove()` when the corresponding input
        iterator supports it.
        
        **Java 8+ users:** The `Stream` equivalent of this method is `Streams.concat(a, b, c, d)`.
        """
        ...


    @staticmethod
    def concat(*inputs: Tuple[Iterable["T"], ...]) -> Iterable["T"]:
        """
        Combines multiple iterables into a single iterable. The returned iterable has an iterator that
        traverses the elements of each iterable in `inputs`. The input iterators are not polled
        until necessary.
        
        The returned iterable's iterator supports `remove()` when the corresponding input
        iterator supports it.
        
        **Java 8+ users:** The `Stream` equivalent of this method is `Streams.concat(...)`.

        Raises
        - NullPointerException: if any of the provided iterables is null
        """
        ...


    @staticmethod
    def concat(inputs: Iterable[Iterable["T"]]) -> Iterable["T"]:
        """
        Combines multiple iterables into a single iterable. The returned iterable has an iterator that
        traverses the elements of each iterable in `inputs`. The input iterators are not polled
        until necessary.
        
        The returned iterable's iterator supports `remove()` when the corresponding input
        iterator supports it. The methods of the returned iterable may throw `NullPointerException` if any of the input iterators is null.
        
        **Java 8+ users:** The `Stream` equivalent of this method is `streamOfStreams.flatMap(s -> s)`.
        """
        ...


    @staticmethod
    def partition(iterable: Iterable["T"], size: int) -> Iterable[list["T"]]:
        """
        Divides an iterable into unmodifiable sublists of the given size (the final iterable may be
        smaller). For example, partitioning an iterable containing `[a, b, c, d, e]` with a
        partition size of 3 yields `[[a, b, c], [d, e]]` -- an outer iterable containing two
        inner lists of three and two elements, all in the original order.
        
        Iterators returned by the returned iterable do not support the Iterator.remove()
        method. The returned lists implement RandomAccess, whether or not the input list does.
        
        **Note:** The current implementation eagerly allocates storage for `size` elements.
        As a consequence, passing values like `Integer.MAX_VALUE` can lead to OutOfMemoryError.
        
        **Note:** if `iterable` is a List, use Lists.partition(List, int)
        instead.

        Arguments
        - iterable: the iterable to return a partitioned view of
        - size: the desired size of each partition (the last may be smaller)

        Returns
        - an iterable of unmodifiable lists containing the elements of `iterable` divided
            into partitions

        Raises
        - IllegalArgumentException: if `size` is nonpositive
        """
        ...


    @staticmethod
    def paddedPartition(iterable: Iterable["T"], size: int) -> Iterable[list["T"]]:
        """
        Divides an iterable into unmodifiable sublists of the given size, padding the final iterable
        with null values if necessary. For example, partitioning an iterable containing `[a, b,
        c, d, e]` with a partition size of 3 yields `[[a, b, c], [d, e, null]]` -- an outer
        iterable containing two inner lists of three elements each, all in the original order.
        
        Iterators returned by the returned iterable do not support the Iterator.remove()
        method.

        Arguments
        - iterable: the iterable to return a partitioned view of
        - size: the desired size of each partition

        Returns
        - an iterable of unmodifiable lists containing the elements of `iterable` divided
            into partitions (the final iterable may have trailing null elements)

        Raises
        - IllegalArgumentException: if `size` is nonpositive
        """
        ...


    @staticmethod
    def filter(unfiltered: Iterable["T"], retainIfTrue: "Predicate"["T"]) -> Iterable["T"]:
        """
        Returns a view of `unfiltered` containing all elements that satisfy the input predicate
        `retainIfTrue`. The returned iterable's iterator does not support `remove()`.
        
        **`Stream` equivalent:** Stream.filter.
        """
        ...


    @staticmethod
    def filter(unfiltered: Iterable[Any], desiredType: type["T"]) -> Iterable["T"]:
        """
        Returns a view of `unfiltered` containing all elements that are of the type `desiredType`. The returned iterable's iterator does not support `remove()`.
        
        **`Stream` equivalent:** `stream.filter(type::isInstance).map(type::cast)`.
        This does perform a little more work than necessary, so another option is to insert an
        unchecked cast at some later point:
        
        ```
        `@SuppressWarnings("unchecked") // safe because of ::isInstance check
        ImmutableList<NewType> result =
            (ImmutableList) stream.filter(NewType.class::isInstance).collect(toImmutableList());`
        ```
        """
        ...


    @staticmethod
    def any(iterable: Iterable["T"], predicate: "Predicate"["T"]) -> bool:
        """
        Returns `True` if any element in `iterable` satisfies the predicate.
        
        **`Stream` equivalent:** Stream.anyMatch.
        """
        ...


    @staticmethod
    def all(iterable: Iterable["T"], predicate: "Predicate"["T"]) -> bool:
        """
        Returns `True` if every element in `iterable` satisfies the predicate. If `iterable` is empty, `True` is returned.
        
        **`Stream` equivalent:** Stream.allMatch.
        """
        ...


    @staticmethod
    def find(iterable: Iterable["T"], predicate: "Predicate"["T"]) -> "T":
        """
        Returns the first element in `iterable` that satisfies the given predicate; use this
        method only when such an element is known to exist. If it is possible that *no* element
        will match, use .tryFind or .find(Iterable, Predicate, Object) instead.
        
        **`Stream` equivalent:** `stream.filter(predicate).findFirst().get()`

        Raises
        - NoSuchElementException: if no element in `iterable` matches the given predicate
        """
        ...


    @staticmethod
    def find(iterable: Iterable["T"], predicate: "Predicate"["T"], defaultValue: "T") -> "T":
        ...


    @staticmethod
    def tryFind(iterable: Iterable["T"], predicate: "Predicate"["T"]) -> "Optional"["T"]:
        """
        Returns an Optional containing the first element in `iterable` that satisfies the
        given predicate, if such an element exists.
        
        **Warning:** avoid using a `predicate` that matches `null`. If `null`
        is matched in `iterable`, a NullPointerException will be thrown.
        
        **`Stream` equivalent:** `stream.filter(predicate).findFirst()`

        Since
        - 11.0
        """
        ...


    @staticmethod
    def indexOf(iterable: Iterable["T"], predicate: "Predicate"["T"]) -> int:
        """
        Returns the index in `iterable` of the first element that satisfies the provided `predicate`, or `-1` if the Iterable has no such elements.
        
        More formally, returns the lowest index `i` such that `predicate.apply(Iterables.get(iterable, i))` returns `True`, or `-1` if there is no
        such index.

        Since
        - 2.0
        """
        ...


    @staticmethod
    def transform(fromIterable: Iterable["F"], function: "Function"["F", "T"]) -> Iterable["T"]:
        """
        Returns a view containing the result of applying `function` to each element of `fromIterable`.
        
        The returned iterable's iterator supports `remove()` if `fromIterable`'s
        iterator does. After a successful `remove()` call, `fromIterable` no longer
        contains the corresponding element.
        
        If the input `Iterable` is known to be a `List` or other `Collection`,
        consider Lists.transform and Collections2.transform.
        
        **`Stream` equivalent:** Stream.map
        """
        ...


    @staticmethod
    def get(iterable: Iterable["T"], position: int) -> "T":
        """
        Returns the element at the specified position in an iterable.
        
        **`Stream` equivalent:** `stream.skip(position).findFirst().get()` (throws
        `NoSuchElementException` if out of bounds)

        Arguments
        - position: position of the element to return

        Returns
        - the element at the specified position in `iterable`

        Raises
        - IndexOutOfBoundsException: if `position` is negative or greater than or equal to
            the size of `iterable`
        """
        ...


    @staticmethod
    def get(iterable: Iterable["T"], position: int, defaultValue: "T") -> "T":
        """
        Returns the element at the specified position in an iterable or a default value otherwise.
        
        **`Stream` equivalent:** `stream.skip(position).findFirst().orElse(defaultValue)` (returns the default value if the index
        is out of bounds)

        Arguments
        - position: position of the element to return
        - defaultValue: the default value to return if `position` is greater than or equal to
            the size of the iterable

        Returns
        - the element at the specified position in `iterable` or `defaultValue` if
            `iterable` contains fewer than `position + 1` elements.

        Raises
        - IndexOutOfBoundsException: if `position` is negative

        Since
        - 4.0
        """
        ...


    @staticmethod
    def getFirst(iterable: Iterable["T"], defaultValue: "T") -> "T":
        """
        Returns the first element in `iterable` or `defaultValue` if the iterable is empty.
        The Iterators analog to this method is Iterators.getNext.
        
        If no default value is desired (and the caller instead wants a NoSuchElementException to be thrown), it is recommended that `iterable.iterator().next()` is used instead.
        
        To get the only element in a single-element `Iterable`, consider using .getOnlyElement(Iterable) or .getOnlyElement(Iterable, Object) instead.
        
        **`Stream` equivalent:** `stream.findFirst().orElse(defaultValue)`

        Arguments
        - defaultValue: the default value to return if the iterable is empty

        Returns
        - the first element of `iterable` or the default value

        Since
        - 7.0
        """
        ...


    @staticmethod
    def getLast(iterable: Iterable["T"]) -> "T":
        """
        Returns the last element of `iterable`. If `iterable` is a List with RandomAccess support, then this operation is guaranteed to be `O(1)`.
        
        **`Stream` equivalent:** Streams.findLast Streams.findLast(stream).get()

        Returns
        - the last element of `iterable`

        Raises
        - NoSuchElementException: if the iterable is empty
        """
        ...


    @staticmethod
    def getLast(iterable: Iterable["T"], defaultValue: "T") -> "T":
        """
        Returns the last element of `iterable` or `defaultValue` if the iterable is empty.
        If `iterable` is a List with RandomAccess support, then this operation is
        guaranteed to be `O(1)`.
        
        **`Stream` equivalent:** `Streams.findLast(stream).orElse(defaultValue)`

        Arguments
        - defaultValue: the value to return if `iterable` is empty

        Returns
        - the last element of `iterable` or the default value

        Since
        - 3.0
        """
        ...


    @staticmethod
    def skip(iterable: Iterable["T"], numberToSkip: int) -> Iterable["T"]:
        """
        Returns a view of `iterable` that skips its first `numberToSkip` elements. If
        `iterable` contains fewer than `numberToSkip` elements, the returned iterable skips
        all of its elements.
        
        Modifications to the underlying Iterable before a call to `iterator()` are
        reflected in the returned iterator. That is, the iterator skips the first `numberToSkip`
        elements that exist when the `Iterator` is created, not when `skip()` is called.
        
        The returned iterable's iterator supports `remove()` if the iterator of the underlying
        iterable supports it. Note that it is *not* possible to delete the last skipped element by
        immediately calling `remove()` on that iterator, as the `Iterator` contract states
        that a call to `remove()` before a call to `next()` will throw an IllegalStateException.
        
        **`Stream` equivalent:** Stream.skip

        Since
        - 3.0
        """
        ...


    @staticmethod
    def limit(iterable: Iterable["T"], limitSize: int) -> Iterable["T"]:
        """
        Returns a view of `iterable` containing its first `limitSize` elements. If `iterable` contains fewer than `limitSize` elements, the returned view contains all of its
        elements. The returned iterable's iterator supports `remove()` if `iterable`'s
        iterator does.
        
        **`Stream` equivalent:** Stream.limit

        Arguments
        - iterable: the iterable to limit
        - limitSize: the maximum number of elements in the returned iterable

        Raises
        - IllegalArgumentException: if `limitSize` is negative

        Since
        - 3.0
        """
        ...


    @staticmethod
    def consumingIterable(iterable: Iterable["T"]) -> Iterable["T"]:
        """
        Returns a view of the supplied iterable that wraps each generated Iterator through
        Iterators.consumingIterator(Iterator).
        
        Note: If `iterable` is a Queue, the returned iterable will instead use Queue.isEmpty and Queue.remove(), since Queue's iteration order is undefined.
        Calling Iterator.hasNext() on a generated iterator from the returned iterable may cause
        an item to be immediately dequeued for return on a subsequent call to Iterator.next().
        
        Whether the input `iterable` is a Queue or not, the returned `Iterable`
        is not thread-safe.

        Arguments
        - iterable: the iterable to wrap

        Returns
        - a view of the supplied iterable that wraps each generated iterator through Iterators.consumingIterator(Iterator); for queues, an iterable that generates iterators
            that return and consume the queue's elements in queue order

        See
        - Iterators.consumingIterator(Iterator)

        Since
        - 2.0
        """
        ...


    @staticmethod
    def isEmpty(iterable: Iterable[Any]) -> bool:
        """
        Determines if the given iterable contains no elements.
        
        There is no precise Iterator equivalent to this method, since one can only ask an
        iterator whether it has any elements *remaining* (which one does using Iterator.hasNext).
        
        **`Stream` equivalent:** `!stream.findAny().isPresent()`

        Returns
        - `True` if the iterable contains no elements
        """
        ...


    @staticmethod
    def mergeSorted(iterables: Iterable[Iterable["T"]], comparator: "Comparator"["T"]) -> Iterable["T"]:
        """
        Returns an iterable over the merged contents of all given `iterables`. Equivalent entries
        will not be de-duplicated.
        
        Callers must ensure that the source `iterables` are in non-descending order as this
        method does not sort its input.
        
        For any equivalent elements across all `iterables`, it is undefined which element is
        returned first.

        Since
        - 11.0
        """
        ...
