"""
Python module generated from Java source file com.google.common.collect.FluentIterable

Java source file obtained from artifact guava version 31.0.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.annotations import GwtCompatible
from com.google.common.annotations import GwtIncompatible
from com.google.common.base import Function
from com.google.common.base import Joiner
from com.google.common.base import Optional
from com.google.common.base import Predicate
from com.google.common.collect import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from com.google.errorprone.annotations import InlineMe
from java.util import Arrays
from java.util import Collections
from java.util import Comparator
from java.util import Iterator
from java.util import SortedSet
from java.util.stream import Stream
from javax.annotation import CheckForNull
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class FluentIterable(Iterable):
    """
    A discouraged (but not deprecated) precursor to Java's superior Stream library.
    
    The following types of methods are provided:
    
    
      - chaining methods which return a new `FluentIterable` based in some way on the
          contents of the current one (for example .transform)
      - element extraction methods which facilitate the retrieval of certain elements (for example
          .last)
      - query methods which answer questions about the `FluentIterable`'s contents (for
          example .anyMatch)
      - conversion methods which copy the `FluentIterable`'s contents into a new collection
          or array (for example .toList)
    
    
    Several lesser-used features are currently available only as static methods on the Iterables class.
    
    <a id="streams"></a>
    
    <h3>Comparison to streams</h3>
    
    Stream is similar to this class, but generally more powerful, and certainly more
    standard. Key differences include:
    
    
      - A stream is *single-use*; it becomes invalid as soon as any "terminal operation" such
          as `findFirst()` or `iterator()` is invoked. (Even though `Stream`
          contains all the right method *signatures* to implement Iterable, it does not
          actually do so, to avoid implying repeat-iterability.) `FluentIterable`, on the other
          hand, is multiple-use, and does implement Iterable.
      - Streams offer many features not found here, including `min/max`, `distinct`,
          `reduce`, `sorted`, the very powerful `collect`, and built-in support for
          parallelizing stream operations.
      - `FluentIterable` contains several features not available on `Stream`, which are
          noted in the method descriptions below.
      - Streams include primitive-specialized variants such as `IntStream`, the use of which
          is strongly recommended.
      - Streams are standard Java, not requiring a third-party dependency.
    
    
    <h3>Example</h3>
    
    Here is an example that accepts a list from a database call, filters it based on a predicate,
    transforms it by invoking `toString()` on each element, and returns the first 10 elements
    as a `List`:
    
    ````ImmutableList<String> results =
        FluentIterable.from(database.getClientList())
            .filter(Client::isActiveInLastMonth)
            .transform(Object::toString)
            .limit(10)
            .toList();````
    
    The approximate stream equivalent is:
    
    ````List<String> results =
        database.getClientList()
            .stream()
            .filter(Client::isActiveInLastMonth)
            .map(Object::toString)
            .limit(10)
            .collect(Collectors.toList());````

    Author(s)
    - Marcin Mikosik

    Since
    - 12.0
    """

    @staticmethod
    def from(iterable: Iterable["E"]) -> "FluentIterable"["E"]:
        """
        Returns a fluent iterable that wraps `iterable`, or `iterable` itself if it is
        already a `FluentIterable`.
        
        **`Stream` equivalent:** Collection.stream if `iterable` is a Collection; Streams.stream(Iterable) otherwise.
        """
        ...


    @staticmethod
    def from(elements: list["E"]) -> "FluentIterable"["E"]:
        """
        Returns a fluent iterable containing `elements` in the specified order.
        
        The returned iterable is an unmodifiable view of the input array.
        
        **`Stream` equivalent:** java.util.stream.Stream.of(Object[])
        Stream.of(T...).

        Since
        - 20.0 (since 18.0 as an overload of `of`)
        """
        ...


    @staticmethod
    def from(iterable: "FluentIterable"["E"]) -> "FluentIterable"["E"]:
        """
        Construct a fluent iterable from another fluent iterable. This is obviously never necessary,
        but is intended to help call out cases where one migration from `Iterable` to `FluentIterable` has obviated the need to explicitly convert to a `FluentIterable`.

        Deprecated
        - instances of `FluentIterable` don't need to be converted to `FluentIterable`
        """
        ...


    @staticmethod
    def concat(a: Iterable["T"], b: Iterable["T"]) -> "FluentIterable"["T"]:
        """
        Returns a fluent iterable that combines two iterables. The returned iterable has an iterator
        that traverses the elements in `a`, followed by the elements in `b`. The source
        iterators are not polled until necessary.
        
        The returned iterable's iterator supports `remove()` when the corresponding input
        iterator supports it.
        
        **`Stream` equivalent:** Stream.concat.

        Since
        - 20.0
        """
        ...


    @staticmethod
    def concat(a: Iterable["T"], b: Iterable["T"], c: Iterable["T"]) -> "FluentIterable"["T"]:
        """
        Returns a fluent iterable that combines three iterables. The returned iterable has an iterator
        that traverses the elements in `a`, followed by the elements in `b`, followed by
        the elements in `c`. The source iterators are not polled until necessary.
        
        The returned iterable's iterator supports `remove()` when the corresponding input
        iterator supports it.
        
        **`Stream` equivalent:** use nested calls to Stream.concat, or see the
        advice in .concat(Iterable...).

        Since
        - 20.0
        """
        ...


    @staticmethod
    def concat(a: Iterable["T"], b: Iterable["T"], c: Iterable["T"], d: Iterable["T"]) -> "FluentIterable"["T"]:
        """
        Returns a fluent iterable that combines four iterables. The returned iterable has an iterator
        that traverses the elements in `a`, followed by the elements in `b`, followed by
        the elements in `c`, followed by the elements in `d`. The source iterators are not
        polled until necessary.
        
        The returned iterable's iterator supports `remove()` when the corresponding input
        iterator supports it.
        
        **`Stream` equivalent:** use nested calls to Stream.concat, or see the
        advice in .concat(Iterable...).

        Since
        - 20.0
        """
        ...


    @staticmethod
    def concat(*inputs: Tuple[Iterable["T"], ...]) -> "FluentIterable"["T"]:
        """
        Returns a fluent iterable that combines several iterables. The returned iterable has an
        iterator that traverses the elements of each iterable in `inputs`. The input iterators
        are not polled until necessary.
        
        The returned iterable's iterator supports `remove()` when the corresponding input
        iterator supports it.
        
        **`Stream` equivalent:** to concatenate an arbitrary number of streams, use `Stream.of(stream1, stream2, ...).flatMap(s -> s)`. If the sources are iterables, use `Stream.of(iter1, iter2, ...).flatMap(Streams::stream)`.

        Raises
        - NullPointerException: if any of the provided iterables is `null`

        Since
        - 20.0
        """
        ...


    @staticmethod
    def concat(inputs: Iterable[Iterable["T"]]) -> "FluentIterable"["T"]:
        """
        Returns a fluent iterable that combines several iterables. The returned iterable has an
        iterator that traverses the elements of each iterable in `inputs`. The input iterators
        are not polled until necessary.
        
        The returned iterable's iterator supports `remove()` when the corresponding input
        iterator supports it. The methods of the returned iterable may throw `NullPointerException` if any of the input iterators is `null`.
        
        **`Stream` equivalent:** `streamOfStreams.flatMap(s -> s)` or `streamOfIterables.flatMap(Streams::stream)`. (See Streams.stream.)

        Since
        - 20.0
        """
        ...


    @staticmethod
    def of() -> "FluentIterable"["E"]:
        """
        Returns a fluent iterable containing no elements.
        
        **`Stream` equivalent:** Stream.empty.

        Since
        - 20.0
        """
        ...


    @staticmethod
    def of(element: "E", *elements: Tuple["E", ...]) -> "FluentIterable"["E"]:
        """
        Returns a fluent iterable containing the specified elements in order.
        
        **`Stream` equivalent:** java.util.stream.Stream.of(Object[])
        Stream.of(T...).

        Since
        - 20.0
        """
        ...


    def toString(self) -> str:
        """
        Returns a string representation of this fluent iterable, with the format `[e1, e2, ...,
        en]`.
        
        **`Stream` equivalent:** `stream.collect(Collectors.joining(", ", "[", "]"))`
        or (less efficiently) `stream.collect(Collectors.toList()).toString()`.
        """
        ...


    def size(self) -> int:
        """
        Returns the number of elements in this fluent iterable.
        
        **`Stream` equivalent:** Stream.count.
        """
        ...


    def contains(self, target: "Object") -> bool:
        """
        Returns `True` if this fluent iterable contains any object for which `equals(target)` is True.
        
        **`Stream` equivalent:** `stream.anyMatch(Predicate.isEqual(target))`.
        """
        ...


    def cycle(self) -> "FluentIterable"["E"]:
        """
        Returns a fluent iterable whose `Iterator` cycles indefinitely over the elements of this
        fluent iterable.
        
        That iterator supports `remove()` if `iterable.iterator()` does. After `remove()` is called, subsequent cycles omit the removed element, which is no longer in this
        fluent iterable. The iterator's `hasNext()` method returns `True` until this fluent
        iterable is empty.
        
        **Warning:** Typical uses of the resulting iterator may produce an infinite loop. You
        should use an explicit `break` or be certain that you will eventually remove all the
        elements.
        
        **`Stream` equivalent:** if the source iterable has only a single element `e`, use `Stream.generate(() -> e)`. Otherwise, collect your stream into a collection and
        use `Stream.generate(() -> collection).flatMap(Collection::stream)`.
        """
        ...


    def append(self, other: Iterable["E"]) -> "FluentIterable"["E"]:
        """
        Returns a fluent iterable whose iterators traverse first the elements of this fluent iterable,
        followed by those of `other`. The iterators are not polled until necessary.
        
        The returned iterable's `Iterator` supports `remove()` when the corresponding
        `Iterator` supports it.
        
        **`Stream` equivalent:** Stream.concat.

        Since
        - 18.0
        """
        ...


    def append(self, *elements: Tuple["E", ...]) -> "FluentIterable"["E"]:
        """
        Returns a fluent iterable whose iterators traverse first the elements of this fluent iterable,
        followed by `elements`.
        
        **`Stream` equivalent:** `Stream.concat(thisStream, Stream.of(elements))`.

        Since
        - 18.0
        """
        ...


    def filter(self, predicate: "Predicate"["E"]) -> "FluentIterable"["E"]:
        """
        Returns the elements from this fluent iterable that satisfy a predicate. The resulting fluent
        iterable's iterator does not support `remove()`.
        
        **`Stream` equivalent:** Stream.filter (same).
        """
        ...


    def filter(self, type: type["T"]) -> "FluentIterable"["T"]:
        """
        Returns the elements from this fluent iterable that are instances of class `type`.
        
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


    def anyMatch(self, predicate: "Predicate"["E"]) -> bool:
        """
        Returns `True` if any element in this fluent iterable satisfies the predicate.
        
        **`Stream` equivalent:** Stream.anyMatch (same).
        """
        ...


    def allMatch(self, predicate: "Predicate"["E"]) -> bool:
        """
        Returns `True` if every element in this fluent iterable satisfies the predicate. If this
        fluent iterable is empty, `True` is returned.
        
        **`Stream` equivalent:** Stream.allMatch (same).
        """
        ...


    def firstMatch(self, predicate: "Predicate"["E"]) -> "Optional"["E"]:
        """
        Returns an Optional containing the first element in this fluent iterable that satisfies
        the given predicate, if such an element exists.
        
        **Warning:** avoid using a `predicate` that matches `null`. If `null`
        is matched in this fluent iterable, a NullPointerException will be thrown.
        
        **`Stream` equivalent:** `stream.filter(predicate).findFirst()`.
        """
        ...


    def transform(self, function: "Function"["E", "T"]) -> "FluentIterable"["T"]:
        """
        Returns a fluent iterable that applies `function` to each element of this fluent
        iterable.
        
        The returned fluent iterable's iterator supports `remove()` if this iterable's
        iterator does. After a successful `remove()` call, this fluent iterable no longer
        contains the corresponding element.
        
        **`Stream` equivalent:** Stream.map.
        """
        ...


    def transformAndConcat(self, function: "Function"["E", Iterable["T"]]) -> "FluentIterable"["T"]:
        """
        Applies `function` to each element of this fluent iterable and returns a fluent iterable
        with the concatenated combination of results. `function` returns an Iterable of results.
        
        The returned fluent iterable's iterator supports `remove()` if this function-returned
        iterables' iterator does. After a successful `remove()` call, the returned fluent
        iterable no longer contains the corresponding element.
        
        **`Stream` equivalent:** Stream.flatMap (using a function that produces
        streams, not iterables).

        Since
        - 13.0 (required `Function<E, Iterable<T>>` until 14.0)
        """
        ...


    def first(self) -> "Optional"["E"]:
        """
        Returns an Optional containing the first element in this fluent iterable. If the
        iterable is empty, `Optional.absent()` is returned.
        
        **`Stream` equivalent:** if the goal is to obtain any element, Stream.findAny; if it must specifically be the *first* element, `Stream.findFirst`.

        Raises
        - NullPointerException: if the first element is null; if this is a possibility, use `iterator().next()` or Iterables.getFirst instead.
        """
        ...


    def last(self) -> "Optional"["E"]:
        """
        Returns an Optional containing the last element in this fluent iterable. If the
        iterable is empty, `Optional.absent()` is returned. If the underlying `iterable` is
        a List with java.util.RandomAccess support, then this operation is guaranteed
        to be `O(1)`.
        
        **`Stream` equivalent:** `stream.reduce((a, b) -> b)`.

        Raises
        - NullPointerException: if the last element is null; if this is a possibility, use Iterables.getLast instead.
        """
        ...


    def skip(self, numberToSkip: int) -> "FluentIterable"["E"]:
        """
        Returns a view of this fluent iterable that skips its first `numberToSkip` elements. If
        this fluent iterable contains fewer than `numberToSkip` elements, the returned fluent
        iterable skips all of its elements.
        
        Modifications to this fluent iterable before a call to `iterator()` are reflected in
        the returned fluent iterable. That is, the its iterator skips the first `numberToSkip`
        elements that exist when the iterator is created, not when `skip()` is called.
        
        The returned fluent iterable's iterator supports `remove()` if the `Iterator` of
        this fluent iterable supports it. Note that it is *not* possible to delete the last
        skipped element by immediately calling `remove()` on the returned fluent iterable's
        iterator, as the `Iterator` contract states that a call to `* remove()` before a
        call to `next()` will throw an IllegalStateException.
        
        **`Stream` equivalent:** Stream.skip (same).
        """
        ...


    def limit(self, maxSize: int) -> "FluentIterable"["E"]:
        """
        Creates a fluent iterable with the first `size` elements of this fluent iterable. If this
        fluent iterable does not contain that many elements, the returned fluent iterable will have the
        same behavior as this fluent iterable. The returned fluent iterable's iterator supports `remove()` if this fluent iterable's iterator does.
        
        **`Stream` equivalent:** Stream.limit (same).

        Arguments
        - maxSize: the maximum number of elements in the returned fluent iterable

        Raises
        - IllegalArgumentException: if `size` is negative
        """
        ...


    def isEmpty(self) -> bool:
        """
        Determines whether this fluent iterable is empty.
        
        **`Stream` equivalent:** `!stream.findAny().isPresent()`.
        """
        ...


    def toList(self) -> "ImmutableList"["E"]:
        """
        Returns an `ImmutableList` containing all of the elements from this fluent iterable in
        proper sequence.
        
        **`Stream` equivalent:** pass ImmutableList.toImmutableList to `stream.collect()`.

        Raises
        - NullPointerException: if any element is `null`

        Since
        - 14.0 (since 12.0 as `toImmutableList()`).
        """
        ...


    def toSortedList(self, comparator: "Comparator"["E"]) -> "ImmutableList"["E"]:
        """
        Returns an `ImmutableList` containing all of the elements from this `FluentIterable` in the order specified by `comparator`. To produce an `ImmutableList` sorted by its natural ordering, use `toSortedList(Ordering.natural())`.
        
        **`Stream` equivalent:** pass ImmutableList.toImmutableList to `stream.sorted(comparator).collect()`.

        Arguments
        - comparator: the function by which to sort list elements

        Raises
        - NullPointerException: if any element of this iterable is `null`

        Since
        - 14.0 (since 13.0 as `toSortedImmutableList()`).
        """
        ...


    def toSet(self) -> "ImmutableSet"["E"]:
        """
        Returns an `ImmutableSet` containing all of the elements from this fluent iterable with
        duplicates removed.
        
        **`Stream` equivalent:** pass ImmutableSet.toImmutableSet to `stream.collect()`.

        Raises
        - NullPointerException: if any element is `null`

        Since
        - 14.0 (since 12.0 as `toImmutableSet()`).
        """
        ...


    def toSortedSet(self, comparator: "Comparator"["E"]) -> "ImmutableSortedSet"["E"]:
        """
        Returns an `ImmutableSortedSet` containing all of the elements from this `FluentIterable` in the order specified by `comparator`, with duplicates (determined by
        `comparator.compare(x, y) == 0`) removed. To produce an `ImmutableSortedSet` sorted
        by its natural ordering, use `toSortedSet(Ordering.natural())`.
        
        **`Stream` equivalent:** pass ImmutableSortedSet.toImmutableSortedSet to
        `stream.collect()`.

        Arguments
        - comparator: the function by which to sort set elements

        Raises
        - NullPointerException: if any element of this iterable is `null`

        Since
        - 14.0 (since 12.0 as `toImmutableSortedSet()`).
        """
        ...


    def toMultiset(self) -> "ImmutableMultiset"["E"]:
        """
        Returns an `ImmutableMultiset` containing all of the elements from this fluent iterable.
        
        **`Stream` equivalent:** pass ImmutableMultiset.toImmutableMultiset to
        `stream.collect()`.

        Raises
        - NullPointerException: if any element is null

        Since
        - 19.0
        """
        ...


    def toMap(self, valueFunction: "Function"["E", "V"]) -> "ImmutableMap"["E", "V"]:
        """
        Returns an immutable map whose keys are the distinct elements of this `FluentIterable`
        and whose value for each key was computed by `valueFunction`. The map's iteration order
        is the order of the first appearance of each key in this iterable.
        
        When there are multiple instances of a key in this iterable, it is unspecified whether
        `valueFunction` will be applied to more than one instance of that key and, if it is,
        which result will be mapped to that key in the returned map.
        
        **`Stream` equivalent:** `stream.collect(ImmutableMap.toImmutableMap(k -> k,
        valueFunction))`.

        Raises
        - NullPointerException: if any element of this iterable is `null`, or if `valueFunction` produces `null` for any key

        Since
        - 14.0
        """
        ...


    def index(self, keyFunction: "Function"["E", "K"]) -> "ImmutableListMultimap"["K", "E"]:
        """
        Creates an index `ImmutableListMultimap` that contains the results of applying a
        specified function to each item in this `FluentIterable` of values. Each element of this
        iterable will be stored as a value in the resulting multimap, yielding a multimap with the same
        size as this iterable. The key used to store that value in the multimap will be the result of
        calling the function on that value. The resulting multimap is created as an immutable snapshot.
        In the returned multimap, keys appear in the order they are first encountered, and the values
        corresponding to each key appear in the same order as they are encountered.
        
        **`Stream` equivalent:** `stream.collect(Collectors.groupingBy(keyFunction))`
        behaves similarly, but returns a mutable `Map<K, List<E>>` instead, and may not preserve
        the order of entries).

        Arguments
        - keyFunction: the function used to produce the key for each value

        Raises
        - NullPointerException: if any element of this iterable is `null`, or if `keyFunction` produces `null` for any key

        Since
        - 14.0
        """
        ...


    def uniqueIndex(self, keyFunction: "Function"["E", "K"]) -> "ImmutableMap"["K", "E"]:
        """
        Returns a map with the contents of this `FluentIterable` as its `values`, indexed
        by keys derived from those values. In other words, each input value produces an entry in the
        map whose key is the result of applying `keyFunction` to that value. These entries appear
        in the same order as they appeared in this fluent iterable. Example usage:
        
        ````Color red = new Color("red", 255, 0, 0);
        ...
        FluentIterable<Color> allColors = FluentIterable.from(ImmutableSet.of(red, green, blue));
        
        Map<String, Color> colorForName = allColors.uniqueIndex(toStringFunction());
        assertThat(colorForName).containsEntry("red", red);````
        
        If your index may associate multiple values with each key, use .index(Function)
        index.
        
        **`Stream` equivalent:** `stream.collect(ImmutableMap.toImmutableMap(keyFunction, v -> v))`.

        Arguments
        - keyFunction: the function used to produce the key for each value

        Returns
        - a map mapping the result of evaluating the function `keyFunction` on each value
            in this fluent iterable to that value

        Raises
        - IllegalArgumentException: if `keyFunction` produces the same key for more than one
            value in this fluent iterable
        - NullPointerException: if any element of this iterable is `null`, or if `keyFunction` produces `null` for any key

        Since
        - 14.0
        """
        ...


    def toArray(self, type: type["E"]) -> list["E"]:
        """
        Returns an array containing all of the elements from this fluent iterable in iteration order.
        
        **`Stream` equivalent:** if an object array is acceptable, use `stream.toArray()`; if `type` is a class literal such as `MyType.class`, use `stream.toArray(MyType[]::new)`. Otherwise use `stream.toArray( len -> (E[])
        Array.newInstance(type, len))`.

        Arguments
        - type: the type of the elements

        Returns
        - a newly-allocated array into which all the elements of this fluent iterable have been
            copied
        """
        ...


    def copyInto(self, collection: "C") -> "C":
        """
        Copies all the elements from this fluent iterable to `collection`. This is equivalent to
        calling `Iterables.addAll(collection, this)`.
        
        **`Stream` equivalent:** `stream.forEachOrdered(collection::add)` or `stream.forEach(collection::add)`.

        Arguments
        - collection: the collection to copy elements to

        Returns
        - `collection`, for convenience

        Since
        - 14.0
        """
        ...


    def join(self, joiner: "Joiner") -> str:
        """
        Returns a String containing all of the elements of this fluent iterable joined with
        `joiner`.
        
        **`Stream` equivalent:** `joiner.join(stream.iterator())`, or, if you are not
        using any optional `Joiner` features, `stream.collect(Collectors.joining(delimiter)`.

        Since
        - 18.0
        """
        ...


    def get(self, position: int) -> "E":
        """
        Returns the element at the specified position in this fluent iterable.
        
        **`Stream` equivalent:** `stream.skip(position).findFirst().get()` (but note
        that this throws different exception types, and throws an exception if `null` would be
        returned).

        Arguments
        - position: position of the element to return

        Returns
        - the element at the specified position in this fluent iterable

        Raises
        - IndexOutOfBoundsException: if `position` is negative or greater than or equal to
            the size of this fluent iterable
        """
        ...


    def stream(self) -> "Stream"["E"]:
        """
        Returns a stream of this fluent iterable's contents (similar to calling Collection.stream on a collection).
        
        **Note:** the earlier in the chain you can switch to `Stream` usage (ideally not
        going through `FluentIterable` at all), the more performant and idiomatic your code will
        be. This method is a transitional aid, to be used only when really necessary.

        Since
        - 21.0
        """
        ...
