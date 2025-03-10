"""
Python module generated from Java source file com.google.common.collect.Multiset

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.annotations import GwtCompatible
from com.google.common.collect import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from com.google.errorprone.annotations import CompatibleWith
from java.util import Collections
from java.util import Iterator
from java.util import Spliterator
from java.util.function import Consumer
from java.util.function import ObjIntConsumer
from javax.annotation import Nullable
from typing import Any, Callable, Iterable, Tuple


class Multiset(Collection):
    """
    A collection that supports order-independent equality, like Set, but
    may have duplicate elements. A multiset is also sometimes called a
    *bag*.
    
    Elements of a multiset that are equal to one another are referred to as
    *occurrences* of the same single element. The total number of
    occurrences of an element in a multiset is called the *count* of that
    element (the terms "frequency" and "multiplicity" are equivalent, but not
    used in this API). Since the count of an element is represented as an `int`, a multiset may never contain more than Integer.MAX_VALUE
    occurrences of any one element.
    
    `Multiset` refines the specifications of several methods from
    `Collection`. It also defines an additional query operation, .count, which returns the count of an element. There are five new
    bulk-modification operations, for example .add(Object, int), to add
    or remove multiple occurrences of an element at once, or to set the count of
    an element to a specific value. These modification operations are optional,
    but implementations which support the standard collection operations .add(Object) or .remove(Object) are encouraged to implement the
    related methods as well. Finally, two collection views are provided: .elementSet contains the distinct elements of the multiset "with duplicates
    collapsed", and .entrySet is similar but contains Entry
    Multiset.Entry instances, each providing both a distinct element and the
    count of that element.
    
    In addition to these required methods, implementations of `Multiset` are expected to provide two `static` creation methods:
    `create()`, returning an empty multiset, and `create(Iterable<? extends E>)`, returning a multiset containing the
    given initial elements. This is simply a refinement of `Collection`'s
    constructor recommendations, reflecting the new developments of Java 5.
    
    As with other collection types, the modification operations are optional,
    and should throw UnsupportedOperationException when they are not
    implemented. Most implementations should support either all add operations
    or none of them, all removal operations or none of them, and if and only if
    all of these are supported, the `setCount` methods as well.
    
    A multiset uses Object.equals to determine whether two instances
    should be considered "the same," *unless specified otherwise* by the
    implementation.
    
    Common implementations include ImmutableMultiset, HashMultiset, and ConcurrentHashMultiset.
    
    If your values may be zero, negative, or outside the range of an int, you
    may wish to use com.google.common.util.concurrent.AtomicLongMap
    instead. Note, however, that unlike `Multiset`, `AtomicLongMap`
    does not automatically remove zeros.
    
    See the Guava User Guide article on <a href=
    "https://github.com/google/guava/wiki/NewCollectionTypesExplained#multiset">
    `Multiset`</a>.

    Author(s)
    - Kevin Bourrillion

    Since
    - 2.0
    """

    def size(self) -> int:
        """
        Returns the total number of all occurrences of all elements in this multiset.
        
        **Note:** this method does not return the number of *distinct elements* in the
        multiset, which is given by `entrySet().size()`.
        """
        ...


    def count(self, element: "Object") -> int:
        """
        Returns the number of occurrences of an element in this multiset (the *count* of the
        element). Note that for an Object.equals-based multiset, this gives the same result as
        Collections.frequency (which would presumably perform more poorly).
        
        **Note:** the utility method Iterables.frequency generalizes this operation; it
        correctly delegates to this method when dealing with a multiset, but it can also accept any
        other iterable type.

        Arguments
        - element: the element to count occurrences of

        Returns
        - the number of occurrences of the element in this multiset; possibly zero but never
            negative
        """
        ...


    def add(self, element: "E", occurrences: int) -> int:
        """
        Adds a number of occurrences of an element to this multiset. Note that if
        `occurrences == 1`, this method has the identical effect to .add(Object). This method is functionally equivalent (except in the case
        of overflow) to the call `addAll(Collections.nCopies(element,
        occurrences))`, which would presumably perform much more poorly.

        Arguments
        - element: the element to add occurrences of; may be null only if
            explicitly allowed by the implementation
        - occurrences: the number of occurrences of the element to add. May be
            zero, in which case no change will be made.

        Returns
        - the count of the element before the operation; possibly zero

        Raises
        - IllegalArgumentException: if `occurrences` is negative, or if
            this operation would result in more than Integer.MAX_VALUE
            occurrences of the element
        - NullPointerException: if `element` is null and this
            implementation does not permit null elements. Note that if `occurrences` is zero, the implementation may opt to return normally.
        """
        ...


    def remove(self, element: "Object", occurrences: int) -> int:
        """
        Removes a number of occurrences of the specified element from this multiset. If the multiset
        contains fewer than this number of occurrences to begin with, all occurrences will be removed.
        Note that if `occurrences == 1`, this is functionally equivalent to the call `remove(element)`.

        Arguments
        - element: the element to conditionally remove occurrences of
        - occurrences: the number of occurrences of the element to remove. May be zero, in which
            case no change will be made.

        Returns
        - the count of the element before the operation; possibly zero

        Raises
        - IllegalArgumentException: if `occurrences` is negative
        """
        ...


    def setCount(self, element: "E", count: int) -> int:
        """
        Adds or removes the necessary occurrences of an element such that the
        element attains the desired count.

        Arguments
        - element: the element to add or remove occurrences of; may be null
            only if explicitly allowed by the implementation
        - count: the desired count of the element in this multiset

        Returns
        - the count of the element before the operation; possibly zero

        Raises
        - IllegalArgumentException: if `count` is negative
        - NullPointerException: if `element` is null and this
            implementation does not permit null elements. Note that if `count` is zero, the implementor may optionally return zero instead.
        """
        ...


    def setCount(self, element: "E", oldCount: int, newCount: int) -> bool:
        """
        Conditionally sets the count of an element to a new value, as described in
        .setCount(Object, int), provided that the element has the expected
        current count. If the current count is not `oldCount`, no change is
        made.

        Arguments
        - element: the element to conditionally set the count of; may be null
            only if explicitly allowed by the implementation
        - oldCount: the expected present count of the element in this multiset
        - newCount: the desired count of the element in this multiset

        Returns
        - `True` if the condition for modification was met. This
            implies that the multiset was indeed modified, unless
            `oldCount == newCount`.

        Raises
        - IllegalArgumentException: if `oldCount` or `newCount` is
            negative
        - NullPointerException: if `element` is null and the
            implementation does not permit null elements. Note that if `oldCount` and `newCount` are both zero, the implementor may
            optionally return `True` instead.
        """
        ...


    def elementSet(self) -> set["E"]:
        """
        Returns the set of distinct elements contained in this multiset. The
        element set is backed by the same data as the multiset, so any change to
        either is immediately reflected in the other. The order of the elements in
        the element set is unspecified.
        
        If the element set supports any removal operations, these necessarily
        cause **all** occurrences of the removed element(s) to be removed from
        the multiset. Implementations are not expected to support the add
        operations, although this is possible.
        
        A common use for the element set is to find the number of distinct
        elements in the multiset: `elementSet().size()`.

        Returns
        - a view of the set of distinct elements in this multiset
        """
        ...


    def entrySet(self) -> set["Entry"["E"]]:
        """
        Returns a view of the contents of this multiset, grouped into `Multiset.Entry` instances, each providing an element of the multiset and
        the count of that element. This set contains exactly one entry for each
        distinct element in the multiset (thus it always has the same size as the
        .elementSet). The order of the elements in the element set is
        unspecified.
        
        The entry set is backed by the same data as the multiset, so any change
        to either is immediately reflected in the other. However, multiset changes
        may or may not be reflected in any `Entry` instances already
        retrieved from the entry set (this is implementation-dependent).
        Furthermore, implementations are not required to support modifications to
        the entry set at all, and the `Entry` instances themselves don't
        even have methods for modification. See the specific implementation class
        for more details on how its entry set handles modifications.

        Returns
        - a set of entries representing the data of this multiset
        """
        ...


    def forEachEntry(self, action: "ObjIntConsumer"["E"]) -> None:
        """
        Runs the specified action for each distinct element in this multiset, and the number of
        occurrences of that element. For some `Multiset` implementations, this may be more
        efficient than iterating over the .entrySet() either explicitly or with `entrySet().forEach(action)`.

        Since
        - 21.0
        """
        ...


    def equals(self, object: "Object") -> bool:
        """
        Compares the specified object with this multiset for equality. Returns `True` if the
        given object is also a multiset and contains equal elements with equal counts, regardless of
        order.
        """
        ...


    def hashCode(self) -> int:
        """
        Returns the hash code for this multiset. This is defined as the sum of
        ```   `((element == null) ? 0 : element.hashCode()) ^ count(element)````
        
        over all distinct elements in the multiset. It follows that a multiset and
        its entry set always have the same hash code.
        """
        ...


    def toString(self) -> str:
        """
        
        
        It is recommended, though not mandatory, that this method return the
        result of invoking .toString on the .entrySet, yielding a
        result such as `[a x 3, c, d x 2, e]`.
        """
        ...


    def iterator(self) -> Iterator["E"]:
        """
        
        
        Elements that occur multiple times in the multiset will appear
        multiple times in this iterator, though not necessarily sequentially.
        """
        ...


    def contains(self, element: "Object") -> bool:
        """
        Determines whether this multiset contains the specified element.
        
        This method refines Collection.contains to further specify that
        it **may not** throw an exception in response to `element` being
        null or of the wrong type.

        Arguments
        - element: the element to check for

        Returns
        - `True` if this multiset contains at least one occurrence of
            the element
        """
        ...


    def containsAll(self, elements: Iterable[Any]) -> bool:
        """
        Returns `True` if this multiset contains at least one occurrence of
        each element in the specified collection.
        
        This method refines Collection.containsAll to further specify
        that it **may not** throw an exception in response to any of `elements` being null or of the wrong type.
        
        **Note:** this method does not take into account the occurrence
        count of an element in the two collections; it may still return `True` even if `elements` contains several occurrences of an element
        and this multiset contains only one. This is no different than any other
        collection type like List, but it may be unexpected to the user of
        a multiset.

        Arguments
        - elements: the collection of elements to be checked for containment in
            this multiset

        Returns
        - `True` if this multiset contains at least one occurrence of
            each element contained in `elements`

        Raises
        - NullPointerException: if `elements` is null
        """
        ...


    def add(self, element: "E") -> bool:
        """
        Adds a single occurrence of the specified element to this multiset.
        
        This method refines Collection.add, which only *ensures*
        the presence of the element, to further specify that a successful call must
        always increment the count of the element, and the overall size of the
        collection, by one.
        
        To both add the element and obtain the previous count of that element,
        use .add(E, int) add`(element, 1)` instead.

        Arguments
        - element: the element to add one occurrence of; may be null only if
            explicitly allowed by the implementation

        Returns
        - `True` always, since this call is required to modify the
            multiset, unlike other Collection types

        Raises
        - NullPointerException: if `element` is null and this
            implementation does not permit null elements
        - IllegalArgumentException: if Integer.MAX_VALUE occurrences
            of `element` are already contained in this multiset
        """
        ...


    def remove(self, element: "Object") -> bool:
        """
        Removes a *single* occurrence of the specified element from this
        multiset, if present.
        
        This method refines Collection.remove to further specify that it
        **may not** throw an exception in response to `element` being null
        or of the wrong type.
        
        To both remove the element and obtain the previous count of that element,
        use .remove(E, int) remove`(element, 1)` instead.

        Arguments
        - element: the element to remove one occurrence of

        Returns
        - `True` if an occurrence was found and removed
        """
        ...


    def removeAll(self, c: Iterable[Any]) -> bool:
        """
        
        
        **Note:** This method ignores how often any element might appear in
        `c`, and only cares whether or not an element appears at all.
        If you wish to remove one occurrence in this multiset for every occurrence
        in `c`, see Multisets.removeOccurrences(Multiset, Multiset).
        
        This method refines Collection.removeAll to further specify that
        it **may not** throw an exception in response to any of `elements`
        being null or of the wrong type.
        """
        ...


    def retainAll(self, c: Iterable[Any]) -> bool:
        """
        
        
        **Note:** This method ignores how often any element might appear in
        `c`, and only cares whether or not an element appears at all.
        If you wish to remove one occurrence in this multiset for every occurrence
        in `c`, see Multisets.retainOccurrences(Multiset, Multiset).
        
        This method refines Collection.retainAll to further specify that
        it **may not** throw an exception in response to any of `elements`
        being null or of the wrong type.

        See
        - Multisets.retainOccurrences(Multiset, Multiset)
        """
        ...


    def forEach(self, action: "Consumer"["E"]) -> None:
        """
        
        
        Elements that occur multiple times in the multiset will be passed to the `Consumer`
        correspondingly many times, though not necessarily sequentially.
        """
        ...


    def spliterator(self) -> "Spliterator"["E"]:
        ...
