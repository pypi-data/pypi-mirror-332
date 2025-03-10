"""
Python module generated from Java source file com.google.common.collect.Sets

Java source file obtained from artifact guava version 31.0.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.annotations import GwtCompatible
from com.google.common.annotations import GwtIncompatible
from com.google.common.base import Predicate
from com.google.common.base import Predicates
from com.google.common.collect import *
from com.google.common.collect.Collections2 import FilteredCollection
from com.google.common.math import IntMath
from com.google.errorprone.annotations import CanIgnoreReturnValue
from com.google.errorprone.annotations import DoNotCall
from java.io import Serializable
from java.util import AbstractSet
from java.util import Arrays
from java.util import BitSet
from java.util import Collections
from java.util import Comparator
from java.util import EnumSet
from java.util import Iterator
from java.util import LinkedHashSet
from java.util import NavigableSet
from java.util import NoSuchElementException
from java.util import SortedSet
from java.util.concurrent import ConcurrentHashMap
from java.util.concurrent import CopyOnWriteArraySet
from java.util.function import Consumer
from java.util.stream import Collector
from java.util.stream import Stream
from javax.annotation import CheckForNull
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class Sets:
    """
    Static utility methods pertaining to Set instances. Also see this class's counterparts
    Lists, Maps and Queues.
    
    See the Guava User Guide article on <a href=
    "https://github.com/google/guava/wiki/CollectionUtilitiesExplained#sets"> `Sets`</a>.

    Author(s)
    - Chris Povirk

    Since
    - 2.0
    """

    @staticmethod
    def immutableEnumSet(anElement: "E", *otherElements: Tuple["E", ...]) -> "ImmutableSet"["E"]:
        ...


    @staticmethod
    def immutableEnumSet(elements: Iterable["E"]) -> "ImmutableSet"["E"]:
        ...


    @staticmethod
    def toImmutableEnumSet() -> "Collector"["E", Any, "ImmutableSet"["E"]]:
        """
        Returns a `Collector` that accumulates the input elements into a new `ImmutableSet`
        with an implementation specialized for enums. Unlike ImmutableSet.toImmutableSet, the
        resulting set will iterate over elements in their enum definition order, not encounter order.

        Since
        - 21.0
        """
        ...


    @staticmethod
    def newEnumSet(iterable: Iterable["E"], elementType: type["E"]) -> "EnumSet"["E"]:
        """
        Returns a new, *mutable* `EnumSet` instance containing the given elements in their
        natural order. This method behaves identically to EnumSet.copyOf(Collection), but also
        accepts non-`Collection` iterables and empty iterables.
        """
        ...


    @staticmethod
    def newHashSet() -> set["E"]:
        """
        Creates a *mutable*, initially empty `HashSet` instance.
        
        **Note:** if mutability is not required, use ImmutableSet.of() instead. If `E` is an Enum type, use EnumSet.noneOf instead. Otherwise, strongly consider
        using a `LinkedHashSet` instead, at the cost of increased memory footprint, to get
        deterministic iteration behavior.
        
        **Note for Java 7 and later:** this method is now unnecessary and should be treated as
        deprecated. Instead, use the `HashSet` constructor directly, taking advantage of the new
        <a href="http://goo.gl/iz2Wi">"diamond" syntax</a>.
        """
        ...


    @staticmethod
    def newHashSet(*elements: Tuple["E", ...]) -> set["E"]:
        """
        Creates a *mutable* `HashSet` instance initially containing the given elements.
        
        **Note:** if elements are non-null and won't be added or removed after this point, use
        ImmutableSet.of() or ImmutableSet.copyOf(Object[]) instead. If `E` is an
        Enum type, use EnumSet.of(Enum, Enum[]) instead. Otherwise, strongly consider
        using a `LinkedHashSet` instead, at the cost of increased memory footprint, to get
        deterministic iteration behavior.
        
        This method is just a small convenience, either for `newHashSet(`Arrays.asList
        asList`(...))`, or for creating an empty set then calling Collections.addAll.
        This method is not actually very useful and will likely be deprecated in the future.
        """
        ...


    @staticmethod
    def newHashSet(elements: Iterable["E"]) -> set["E"]:
        """
        Creates a *mutable* `HashSet` instance containing the given elements. A very thin
        convenience for creating an empty set then calling Collection.addAll or Iterables.addAll.
        
        **Note:** if mutability is not required and the elements are non-null, use ImmutableSet.copyOf(Iterable) instead. (Or, change `elements` to be a FluentIterable and call `elements.toSet()`.)
        
        **Note:** if `E` is an Enum type, use .newEnumSet(Iterable, Class)
        instead.
        
        **Note for Java 7 and later:** if `elements` is a Collection, you don't
        need this method. Instead, use the `HashSet` constructor directly, taking advantage of
        the new <a href="http://goo.gl/iz2Wi">"diamond" syntax</a>.
        
        Overall, this method is not very useful and will likely be deprecated in the future.
        """
        ...


    @staticmethod
    def newHashSet(elements: Iterator["E"]) -> set["E"]:
        """
        Creates a *mutable* `HashSet` instance containing the given elements. A very thin
        convenience for creating an empty set and then calling Iterators.addAll.
        
        **Note:** if mutability is not required and the elements are non-null, use ImmutableSet.copyOf(Iterator) instead.
        
        **Note:** if `E` is an Enum type, you should create an EnumSet
        instead.
        
        Overall, this method is not very useful and will likely be deprecated in the future.
        """
        ...


    @staticmethod
    def newHashSetWithExpectedSize(expectedSize: int) -> set["E"]:
        """
        Returns a new hash set using the smallest initial table size that can hold `expectedSize`
        elements without resizing. Note that this is not what HashSet.HashSet(int) does, but it
        is what most users want and expect it to do.
        
        This behavior can't be broadly guaranteed, but has been tested with OpenJDK 1.7 and 1.8.

        Arguments
        - expectedSize: the number of elements you expect to add to the returned set

        Returns
        - a new, empty hash set with enough capacity to hold `expectedSize` elements
            without resizing

        Raises
        - IllegalArgumentException: if `expectedSize` is negative
        """
        ...


    @staticmethod
    def newConcurrentHashSet() -> set["E"]:
        """
        Creates a thread-safe set backed by a hash map. The set is backed by a ConcurrentHashMap instance, and thus carries the same concurrency guarantees.
        
        Unlike `HashSet`, this class does NOT allow `null` to be used as an element. The
        set is serializable.

        Returns
        - a new, empty thread-safe `Set`

        Since
        - 15.0
        """
        ...


    @staticmethod
    def newConcurrentHashSet(elements: Iterable["E"]) -> set["E"]:
        """
        Creates a thread-safe set backed by a hash map and containing the given elements. The set is
        backed by a ConcurrentHashMap instance, and thus carries the same concurrency
        guarantees.
        
        Unlike `HashSet`, this class does NOT allow `null` to be used as an element. The
        set is serializable.

        Arguments
        - elements: the elements that the set should contain

        Returns
        - a new thread-safe set containing those elements (minus duplicates)

        Raises
        - NullPointerException: if `elements` or any of its contents is null

        Since
        - 15.0
        """
        ...


    @staticmethod
    def newLinkedHashSet() -> "LinkedHashSet"["E"]:
        """
        Creates a *mutable*, empty `LinkedHashSet` instance.
        
        **Note:** if mutability is not required, use ImmutableSet.of() instead.
        
        **Note for Java 7 and later:** this method is now unnecessary and should be treated as
        deprecated. Instead, use the `LinkedHashSet` constructor directly, taking advantage of
        the new <a href="http://goo.gl/iz2Wi">"diamond" syntax</a>.

        Returns
        - a new, empty `LinkedHashSet`
        """
        ...


    @staticmethod
    def newLinkedHashSet(elements: Iterable["E"]) -> "LinkedHashSet"["E"]:
        """
        Creates a *mutable* `LinkedHashSet` instance containing the given elements in order.
        
        **Note:** if mutability is not required and the elements are non-null, use ImmutableSet.copyOf(Iterable) instead.
        
        **Note for Java 7 and later:** if `elements` is a Collection, you don't
        need this method. Instead, use the `LinkedHashSet` constructor directly, taking advantage
        of the new <a href="http://goo.gl/iz2Wi">"diamond" syntax</a>.
        
        Overall, this method is not very useful and will likely be deprecated in the future.

        Arguments
        - elements: the elements that the set should contain, in order

        Returns
        - a new `LinkedHashSet` containing those elements (minus duplicates)
        """
        ...


    @staticmethod
    def newLinkedHashSetWithExpectedSize(expectedSize: int) -> "LinkedHashSet"["E"]:
        """
        Creates a `LinkedHashSet` instance, with a high enough "initial capacity" that it
        *should* hold `expectedSize` elements without growth. This behavior cannot be
        broadly guaranteed, but it is observed to be True for OpenJDK 1.7. It also can't be guaranteed
        that the method isn't inadvertently *oversizing* the returned set.

        Arguments
        - expectedSize: the number of elements you expect to add to the returned set

        Returns
        - a new, empty `LinkedHashSet` with enough capacity to hold `expectedSize`
            elements without resizing

        Raises
        - IllegalArgumentException: if `expectedSize` is negative

        Since
        - 11.0
        """
        ...


    @staticmethod
    def newTreeSet() -> set["E"]:
        """
        Creates a *mutable*, empty `TreeSet` instance sorted by the natural sort ordering of
        its elements.
        
        **Note:** if mutability is not required, use ImmutableSortedSet.of() instead.
        
        **Note for Java 7 and later:** this method is now unnecessary and should be treated as
        deprecated. Instead, use the `TreeSet` constructor directly, taking advantage of the new
        <a href="http://goo.gl/iz2Wi">"diamond" syntax</a>.

        Returns
        - a new, empty `TreeSet`
        """
        ...


    @staticmethod
    def newTreeSet(elements: Iterable["E"]) -> set["E"]:
        """
        Creates a *mutable* `TreeSet` instance containing the given elements sorted by their
        natural ordering.
        
        **Note:** if mutability is not required, use ImmutableSortedSet.copyOf(Iterable)
        instead.
        
        **Note:** If `elements` is a `SortedSet` with an explicit comparator, this
        method has different behavior than TreeSet.TreeSet(SortedSet), which returns a `TreeSet` with that comparator.
        
        **Note for Java 7 and later:** this method is now unnecessary and should be treated as
        deprecated. Instead, use the `TreeSet` constructor directly, taking advantage of the new
        <a href="http://goo.gl/iz2Wi">"diamond" syntax</a>.
        
        This method is just a small convenience for creating an empty set and then calling Iterables.addAll. This method is not very useful and will likely be deprecated in the future.

        Arguments
        - elements: the elements that the set should contain

        Returns
        - a new `TreeSet` containing those elements (minus duplicates)
        """
        ...


    @staticmethod
    def newTreeSet(comparator: "Comparator"["E"]) -> set["E"]:
        """
        Creates a *mutable*, empty `TreeSet` instance with the given comparator.
        
        **Note:** if mutability is not required, use `ImmutableSortedSet.orderedBy(comparator).build()` instead.
        
        **Note for Java 7 and later:** this method is now unnecessary and should be treated as
        deprecated. Instead, use the `TreeSet` constructor directly, taking advantage of the new
        <a href="http://goo.gl/iz2Wi">"diamond" syntax</a>. One caveat to this is that the `TreeSet` constructor uses a null `Comparator` to mean "natural ordering," whereas this
        factory rejects null. Clean your code accordingly.

        Arguments
        - comparator: the comparator to use to sort the set

        Returns
        - a new, empty `TreeSet`

        Raises
        - NullPointerException: if `comparator` is null
        """
        ...


    @staticmethod
    def newIdentityHashSet() -> set["E"]:
        """
        Creates an empty `Set` that uses identity to determine equality. It compares object
        references, instead of calling `equals`, to determine whether a provided object matches
        an element in the set. For example, `contains` returns `False` when passed an
        object that equals a set member, but isn't the same instance. This behavior is similar to the
        way `IdentityHashMap` handles key lookups.

        Since
        - 8.0
        """
        ...


    @staticmethod
    def newCopyOnWriteArraySet() -> "CopyOnWriteArraySet"["E"]:
        """
        Creates an empty `CopyOnWriteArraySet` instance.
        
        **Note:** if you need an immutable empty Set, use Collections.emptySet
        instead.

        Returns
        - a new, empty `CopyOnWriteArraySet`

        Since
        - 12.0
        """
        ...


    @staticmethod
    def newCopyOnWriteArraySet(elements: Iterable["E"]) -> "CopyOnWriteArraySet"["E"]:
        """
        Creates a `CopyOnWriteArraySet` instance containing the given elements.

        Arguments
        - elements: the elements that the set should contain, in order

        Returns
        - a new `CopyOnWriteArraySet` containing those elements

        Since
        - 12.0
        """
        ...


    @staticmethod
    def complementOf(collection: Iterable["E"]) -> "EnumSet"["E"]:
        """
        Creates an `EnumSet` consisting of all enum values that are not in the specified
        collection. If the collection is an EnumSet, this method has the same behavior as
        EnumSet.complementOf. Otherwise, the specified collection must contain at least one
        element, in order to determine the element type. If the collection could be empty, use .complementOf(Collection, Class) instead of this method.

        Arguments
        - collection: the collection whose complement should be stored in the enum set

        Returns
        - a new, modifiable `EnumSet` containing all values of the enum that aren't present
            in the given collection

        Raises
        - IllegalArgumentException: if `collection` is not an `EnumSet` instance and
            contains no elements
        """
        ...


    @staticmethod
    def complementOf(collection: Iterable["E"], type: type["E"]) -> "EnumSet"["E"]:
        """
        Creates an `EnumSet` consisting of all enum values that are not in the specified
        collection. This is equivalent to EnumSet.complementOf, but can act on any input
        collection, as long as the elements are of enum type.

        Arguments
        - collection: the collection whose complement should be stored in the `EnumSet`
        - type: the type of the elements in the set

        Returns
        - a new, modifiable `EnumSet` initially containing all the values of the enum not
            present in the given collection
        """
        ...


    @staticmethod
    def newSetFromMap(map: dict["E", "Boolean"]) -> set["E"]:
        """
        Returns a set backed by the specified map. The resulting set displays the same ordering,
        concurrency, and performance characteristics as the backing map. In essence, this factory
        method provides a Set implementation corresponding to any Map implementation.
        There is no need to use this method on a Map implementation that already has a
        corresponding Set implementation (such as java.util.HashMap or java.util.TreeMap).
        
        Each method invocation on the set returned by this method results in exactly one method
        invocation on the backing map or its `keySet` view, with one exception. The `addAll` method is implemented as a sequence of `put` invocations on the backing map.
        
        The specified map must be empty at the time this method is invoked, and should not be
        accessed directly after this method returns. These conditions are ensured if the map is created
        empty, passed directly to this method, and no reference to the map is retained, as illustrated
        in the following code fragment:
        
        ````Set<Object> identityHashSet = Sets.newSetFromMap(
            new IdentityHashMap<Object, Boolean>());````
        
        The returned set is serializable if the backing map is.

        Arguments
        - map: the backing map

        Returns
        - the set backed by the map

        Raises
        - IllegalArgumentException: if `map` is not empty

        Deprecated
        - Use Collections.newSetFromMap instead.
        """
        ...


    @staticmethod
    def union(set1: set["E"], set2: set["E"]) -> "SetView"["E"]:
        """
        Returns an unmodifiable **view** of the union of two sets. The returned set contains all
        elements that are contained in either backing set. Iterating over the returned set iterates
        first over all the elements of `set1`, then over each element of `set2`, in order,
        that is not contained in `set1`.
        
        Results are undefined if `set1` and `set2` are sets based on different
        equivalence relations, for example if `set1` is a HashSet and `set2` is a
        TreeSet or the Map.keySet of an `IdentityHashMap`.
        """
        ...


    @staticmethod
    def intersection(set1: set["E"], set2: set[Any]) -> "SetView"["E"]:
        """
        Returns an unmodifiable **view** of the intersection of two sets. The returned set contains
        all elements that are contained by both backing sets. The iteration order of the returned set
        matches that of `set1`.
        
        Results are undefined if `set1` and `set2` are sets based on different
        equivalence relations, for example if `set1` is a HashSet and `set2` is a
        TreeSet or the Map.keySet of an `IdentityHashMap`.
        
        **Note:** The returned view performs slightly better when `set1` is the smaller of
        the two sets. If you have reason to believe one of your sets will generally be smaller than the
        other, pass it first. Unfortunately, since this method sets the generic type of the returned
        set based on the type of the first set passed, this could in rare cases force you to make a
        cast, for example:
        
        ````Set<Object> aFewBadObjects = ...
        Set<String> manyBadStrings = ...
        
        // impossible for a non-String to be in the intersection
        SuppressWarnings("unchecked")
        Set<String> badStrings = (Set) Sets.intersection(
            aFewBadObjects, manyBadStrings);````
        
        This is unfortunate, but should come up only very rarely.
        """
        ...


    @staticmethod
    def difference(set1: set["E"], set2: set[Any]) -> "SetView"["E"]:
        """
        Returns an unmodifiable **view** of the difference of two sets. The returned set contains
        all elements that are contained by `set1` and not contained by `set2`. `set2`
        may also contain elements not present in `set1`; these are simply ignored. The iteration
        order of the returned set matches that of `set1`.
        
        Results are undefined if `set1` and `set2` are sets based on different
        equivalence relations, for example if `set1` is a HashSet and `set2` is a
        TreeSet or the Map.keySet of an `IdentityHashMap`.
        """
        ...


    @staticmethod
    def symmetricDifference(set1: set["E"], set2: set["E"]) -> "SetView"["E"]:
        """
        Returns an unmodifiable **view** of the symmetric difference of two sets. The returned set
        contains all elements that are contained in either `set1` or `set2` but not in
        both. The iteration order of the returned set is undefined.
        
        Results are undefined if `set1` and `set2` are sets based on different
        equivalence relations, for example if `set1` is a HashSet and `set2` is a
        TreeSet or the Map.keySet of an `IdentityHashMap`.

        Since
        - 3.0
        """
        ...


    @staticmethod
    def filter(unfiltered: set["E"], predicate: "Predicate"["E"]) -> set["E"]:
        ...


    @staticmethod
    def filter(unfiltered: "SortedSet"["E"], predicate: "Predicate"["E"]) -> "SortedSet"["E"]:
        """
        Returns the elements of a `SortedSet`, `unfiltered`, that satisfy a predicate. The
        returned set is a live view of `unfiltered`; changes to one affect the other.
        
        The resulting set's iterator does not support `remove()`, but all other set methods
        are supported. When given an element that doesn't satisfy the predicate, the set's `add()` and `addAll()` methods throw an IllegalArgumentException. When methods
        such as `removeAll()` and `clear()` are called on the filtered set, only elements
        that satisfy the filter will be removed from the underlying set.
        
        The returned set isn't threadsafe or serializable, even if `unfiltered` is.
        
        Many of the filtered set's methods, such as `size()`, iterate across every element in
        the underlying set and determine which elements satisfy the filter. When a live view is
        *not* needed, it may be faster to copy `Iterables.filter(unfiltered, predicate)` and
        use the copy.
        
        **Warning:** `predicate` must be *consistent with equals*, as documented at
        Predicate.apply. Do not provide a predicate such as `Predicates.instanceOf(ArrayList.class)`, which is inconsistent with equals. (See Iterables.filter(Iterable, Class) for related functionality.)

        Since
        - 11.0
        """
        ...


    @staticmethod
    def filter(unfiltered: "NavigableSet"["E"], predicate: "Predicate"["E"]) -> "NavigableSet"["E"]:
        """
        Returns the elements of a `NavigableSet`, `unfiltered`, that satisfy a predicate.
        The returned set is a live view of `unfiltered`; changes to one affect the other.
        
        The resulting set's iterator does not support `remove()`, but all other set methods
        are supported. When given an element that doesn't satisfy the predicate, the set's `add()` and `addAll()` methods throw an IllegalArgumentException. When methods
        such as `removeAll()` and `clear()` are called on the filtered set, only elements
        that satisfy the filter will be removed from the underlying set.
        
        The returned set isn't threadsafe or serializable, even if `unfiltered` is.
        
        Many of the filtered set's methods, such as `size()`, iterate across every element in
        the underlying set and determine which elements satisfy the filter. When a live view is
        *not* needed, it may be faster to copy `Iterables.filter(unfiltered, predicate)` and
        use the copy.
        
        **Warning:** `predicate` must be *consistent with equals*, as documented at
        Predicate.apply. Do not provide a predicate such as `Predicates.instanceOf(ArrayList.class)`, which is inconsistent with equals. (See Iterables.filter(Iterable, Class) for related functionality.)

        Since
        - 14.0
        """
        ...


    @staticmethod
    def cartesianProduct(sets: list[set["B"]]) -> set[list["B"]]:
        """
        Returns every possible list that can be formed by choosing one element from each of the given
        sets in order; the "n-ary <a href="http://en.wikipedia.org/wiki/Cartesian_product">Cartesian
        product</a>" of the sets. For example:
        
        ````Sets.cartesianProduct(ImmutableList.of(
            ImmutableSet.of(1, 2),
            ImmutableSet.of("A", "B", "C")))````
        
        returns a set containing six lists:
        
        
          - `ImmutableList.of(1, "A")`
          - `ImmutableList.of(1, "B")`
          - `ImmutableList.of(1, "C")`
          - `ImmutableList.of(2, "A")`
          - `ImmutableList.of(2, "B")`
          - `ImmutableList.of(2, "C")`
        
        
        The result is guaranteed to be in the "traditional", lexicographical order for Cartesian
        products that you would get from nesting for loops:
        
        ````for (B b0 : sets.get(0)) {
          for (B b1 : sets.get(1)) {
            ...
            ImmutableList<B> tuple = ImmutableList.of(b0, b1, ...);
            // operate on tuple`
        }
        }```
        
        Note that if any input set is empty, the Cartesian product will also be empty. If no sets at
        all are provided (an empty list), the resulting Cartesian product has one element, an empty
        list (counter-intuitive, but mathematically consistent).
        
        *Performance notes:* while the cartesian product of sets of size `m, n, p` is a
        set of size `m x n x p`, its actual memory consumption is much smaller. When the
        cartesian set is constructed, the input sets are merely copied. Only as the resulting set is
        iterated are the individual lists created, and these are not retained after iteration.
        
        Type `<B>`: any common base class shared by all axes (often just Object)

        Arguments
        - sets: the sets to choose elements from, in the order that the elements chosen from those
            sets should appear in the resulting lists

        Returns
        - the Cartesian product, as an immutable set containing immutable lists

        Raises
        - NullPointerException: if `sets`, any one of the `sets`, or any element of a
            provided set is null
        - IllegalArgumentException: if the cartesian product size exceeds the `int` range

        Since
        - 2.0
        """
        ...


    @staticmethod
    def cartesianProduct(*sets: Tuple[set["B"], ...]) -> set[list["B"]]:
        """
        Returns every possible list that can be formed by choosing one element from each of the given
        sets in order; the "n-ary <a href="http://en.wikipedia.org/wiki/Cartesian_product">Cartesian
        product</a>" of the sets. For example:
        
        ````Sets.cartesianProduct(
            ImmutableSet.of(1, 2),
            ImmutableSet.of("A", "B", "C"))````
        
        returns a set containing six lists:
        
        
          - `ImmutableList.of(1, "A")`
          - `ImmutableList.of(1, "B")`
          - `ImmutableList.of(1, "C")`
          - `ImmutableList.of(2, "A")`
          - `ImmutableList.of(2, "B")`
          - `ImmutableList.of(2, "C")`
        
        
        The result is guaranteed to be in the "traditional", lexicographical order for Cartesian
        products that you would get from nesting for loops:
        
        ````for (B b0 : sets.get(0)) {
          for (B b1 : sets.get(1)) {
            ...
            ImmutableList<B> tuple = ImmutableList.of(b0, b1, ...);
            // operate on tuple`
        }
        }```
        
        Note that if any input set is empty, the Cartesian product will also be empty. If no sets at
        all are provided (an empty list), the resulting Cartesian product has one element, an empty
        list (counter-intuitive, but mathematically consistent).
        
        *Performance notes:* while the cartesian product of sets of size `m, n, p` is a
        set of size `m x n x p`, its actual memory consumption is much smaller. When the
        cartesian set is constructed, the input sets are merely copied. Only as the resulting set is
        iterated are the individual lists created, and these are not retained after iteration.
        
        Type `<B>`: any common base class shared by all axes (often just Object)

        Arguments
        - sets: the sets to choose elements from, in the order that the elements chosen from those
            sets should appear in the resulting lists

        Returns
        - the Cartesian product, as an immutable set containing immutable lists

        Raises
        - NullPointerException: if `sets`, any one of the `sets`, or any element of a
            provided set is null
        - IllegalArgumentException: if the cartesian product size exceeds the `int` range

        Since
        - 2.0
        """
        ...


    @staticmethod
    def powerSet(set: set["E"]) -> set[set["E"]]:
        """
        Returns the set of all possible subsets of `set`. For example, `powerSet(ImmutableSet.of(1, 2))` returns the set `{{`, {1}, {2}, {1, 2}}}.
        
        Elements appear in these subsets in the same iteration order as they appeared in the input
        set. The order in which these subsets appear in the outer set is undefined. Note that the power
        set of the empty set is not the empty set, but a one-element set containing the empty set.
        
        The returned set and its constituent sets use `equals` to decide whether two elements
        are identical, even if the input set uses a different concept of equivalence.
        
        *Performance notes:* while the power set of a set with size `n` is of size `2^n`, its memory usage is only `O(n)`. When the power set is constructed, the input set
        is merely copied. Only as the power set is iterated are the individual subsets created, and
        these subsets themselves occupy only a small constant amount of memory.

        Arguments
        - set: the set of elements to construct a power set from

        Returns
        - the power set, as an immutable set of immutable sets

        Raises
        - IllegalArgumentException: if `set` has more than 30 unique elements (causing the
            power set size to exceed the `int` range)
        - NullPointerException: if `set` is or contains `null`

        See
        - <a href="http://en.wikipedia.org/wiki/Power_set">Power set article at Wikipedia</a>

        Since
        - 4.0
        """
        ...


    @staticmethod
    def combinations(set: set["E"], size: int) -> set[set["E"]]:
        """
        Returns the set of all subsets of `set` of size `size`. For example, `combinations(ImmutableSet.of(1, 2, 3), 2)` returns the set `{{1, 2`, {1, 3}, {2, 3}}}.
        
        Elements appear in these subsets in the same iteration order as they appeared in the input
        set. The order in which these subsets appear in the outer set is undefined.
        
        The returned set and its constituent sets use `equals` to decide whether two elements
        are identical, even if the input set uses a different concept of equivalence.
        
        *Performance notes:* the memory usage of the returned set is only `O(n)`. When
        the result set is constructed, the input set is merely copied. Only as the result set is
        iterated are the individual subsets created. Each of these subsets occupies an additional O(n)
        memory but only for as long as the user retains a reference to it. That is, the set returned by
        `combinations` does not retain the individual subsets.

        Arguments
        - set: the set of elements to take combinations of
        - size: the number of elements per combination

        Returns
        - the set of all combinations of `size` elements from `set`

        Raises
        - IllegalArgumentException: if `size` is not between 0 and `set.size()`
            inclusive
        - NullPointerException: if `set` is or contains `null`

        Since
        - 23.0
        """
        ...


    @staticmethod
    def unmodifiableNavigableSet(set: "NavigableSet"["E"]) -> "NavigableSet"["E"]:
        """
        Returns an unmodifiable view of the specified navigable set. This method allows modules to
        provide users with "read-only" access to internal navigable sets. Query operations on the
        returned set "read through" to the specified set, and attempts to modify the returned set,
        whether direct or via its collection views, result in an `UnsupportedOperationException`.
        
        The returned navigable set will be serializable if the specified navigable set is
        serializable.

        Arguments
        - set: the navigable set for which an unmodifiable view is to be returned

        Returns
        - an unmodifiable view of the specified navigable set

        Since
        - 12.0
        """
        ...


    @staticmethod
    def synchronizedNavigableSet(navigableSet: "NavigableSet"["E"]) -> "NavigableSet"["E"]:
        """
        Returns a synchronized (thread-safe) navigable set backed by the specified navigable set. In
        order to guarantee serial access, it is critical that **all** access to the backing
        navigable set is accomplished through the returned navigable set (or its views).
        
        It is imperative that the user manually synchronize on the returned sorted set when
        iterating over it or any of its `descendingSet`, `subSet`, `headSet`, or
        `tailSet` views.
        
        ````NavigableSet<E> set = synchronizedNavigableSet(new TreeSet<E>());
         ...
        synchronized (set) {
          // Must be in the synchronized block
          Iterator<E> it = set.iterator();
          while (it.hasNext()) {
            foo(it.next());`
        }
        }```
        
        or:
        
        ````NavigableSet<E> set = synchronizedNavigableSet(new TreeSet<E>());
        NavigableSet<E> set2 = set.descendingSet().headSet(foo);
         ...
        synchronized (set) { // Note: set, not set2!!!
          // Must be in the synchronized block
          Iterator<E> it = set2.descendingIterator();
          while (it.hasNext())
            foo(it.next());`
        }
        }```
        
        Failure to follow this advice may result in non-deterministic behavior.
        
        The returned navigable set will be serializable if the specified navigable set is
        serializable.

        Arguments
        - navigableSet: the navigable set to be "wrapped" in a synchronized navigable set.

        Returns
        - a synchronized view of the specified navigable set.

        Since
        - 13.0
        """
        ...


    @staticmethod
    def subSet(set: "NavigableSet"["K"], range: "Range"["K"]) -> "NavigableSet"["K"]:
        """
        Returns a view of the portion of `set` whose elements are contained by `range`.
        
        This method delegates to the appropriate methods of NavigableSet (namely NavigableSet.subSet(Object, boolean, Object, boolean) subSet(), NavigableSet.tailSet(Object, boolean) tailSet(), and NavigableSet.headSet(Object,
        boolean) headSet()) to actually construct the view. Consult these methods for a full
        description of the returned view's behavior.
        
        **Warning:** `Range`s always represent a range of values using the values' natural
        ordering. `NavigableSet` on the other hand can specify a custom ordering via a Comparator, which can violate the natural ordering. Using this method (or in general using
        `Range`) with unnaturally-ordered sets can lead to unexpected and undefined behavior.

        Since
        - 20.0
        """
        ...


    class SetView(AbstractSet):
        """
        An unmodifiable view of a set which may be backed by other sets; this view will change as the
        backing sets do. Contains methods to copy the data into a new set which will then remain
        stable. There is usually no reason to retain a reference of type `SetView`; typically,
        you either use it as a plain Set, or immediately invoke .immutableCopy or
        .copyInto and forget the `SetView` itself.

        Since
        - 2.0
        """

        def immutableCopy(self) -> "ImmutableSet"["E"]:
            """
            Returns an immutable copy of the current contents of this set view. Does not support null
            elements.
            
            **Warning:** this may have unexpected results if a backing set of this view uses a
            nonstandard notion of equivalence, for example if it is a TreeSet using a comparator
            that is inconsistent with Object.equals(Object).
            """
            ...


        def copyInto(self, set: "S") -> "S":
            ...


        def add(self, e: "E") -> bool:
            """
            Guaranteed to throw an exception and leave the collection unmodified.

            Raises
            - UnsupportedOperationException: always

            Deprecated
            - Unsupported operation.
            """
            ...


        def remove(self, object: "Object") -> bool:
            """
            Guaranteed to throw an exception and leave the collection unmodified.

            Raises
            - UnsupportedOperationException: always

            Deprecated
            - Unsupported operation.
            """
            ...


        def addAll(self, newElements: Iterable["E"]) -> bool:
            """
            Guaranteed to throw an exception and leave the collection unmodified.

            Raises
            - UnsupportedOperationException: always

            Deprecated
            - Unsupported operation.
            """
            ...


        def removeAll(self, oldElements: Iterable[Any]) -> bool:
            """
            Guaranteed to throw an exception and leave the collection unmodified.

            Raises
            - UnsupportedOperationException: always

            Deprecated
            - Unsupported operation.
            """
            ...


        def removeIf(self, filter: "java.util.function.Predicate"["E"]) -> bool:
            """
            Guaranteed to throw an exception and leave the collection unmodified.

            Raises
            - UnsupportedOperationException: always

            Deprecated
            - Unsupported operation.
            """
            ...


        def retainAll(self, elementsToKeep: Iterable[Any]) -> bool:
            """
            Guaranteed to throw an exception and leave the collection unmodified.

            Raises
            - UnsupportedOperationException: always

            Deprecated
            - Unsupported operation.
            """
            ...


        def clear(self) -> None:
            """
            Guaranteed to throw an exception and leave the collection unmodified.

            Raises
            - UnsupportedOperationException: always

            Deprecated
            - Unsupported operation.
            """
            ...


        def iterator(self) -> "UnmodifiableIterator"["E"]:
            """
            Scope the return type to UnmodifiableIterator to ensure this is an unmodifiable view.

            Since
            - 20.0 (present with return type Iterator since 2.0)
            """
            ...
