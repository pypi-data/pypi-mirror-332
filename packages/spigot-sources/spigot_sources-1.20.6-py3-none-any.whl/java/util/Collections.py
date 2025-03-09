"""
Python module generated from Java source file java.util.Collections

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.io import IOException
from java.io import ObjectInputStream
from java.io import ObjectOutputStream
from java.io import Serializable
from java.lang.reflect import Array
from java.util import *
from java.util.function import BiConsumer
from java.util.function import BiFunction
from java.util.function import Consumer
from java.util.function import Function
from java.util.function import IntFunction
from java.util.function import Predicate
from java.util.function import UnaryOperator
from java.util.stream import IntStream
from java.util.stream import Stream
from java.util.stream import StreamSupport
from jdk.internal.access import SharedSecrets
from typing import Any, Callable, Iterable, Tuple


class Collections:

    EMPTY_SET = EmptySet<>()
    """
    The empty set (immutable).  This set is serializable.

    See
    - .emptySet()
    """
    EMPTY_LIST = EmptyList<>()
    """
    The empty list (immutable).  This list is serializable.

    See
    - .emptyList()
    """
    EMPTY_MAP = EmptyMap<>()
    """
    The empty map (immutable).  This map is serializable.

    See
    - .emptyMap()

    Since
    - 1.3
    """


    @staticmethod
    def sort(list: list["T"]) -> None:
        """
        Sorts the specified list into ascending order, according to the
        Comparable natural ordering of its elements.
        All elements in the list must implement the Comparable
        interface.  Furthermore, all elements in the list must be
        *mutually comparable* (that is, `e1.compareTo(e2)`
        must not throw a `ClassCastException` for any elements
        `e1` and `e2` in the list).
        
        This sort is guaranteed to be *stable*:  equal elements will
        not be reordered as a result of the sort.
        
        The specified list must be modifiable, but need not be resizable.
        
        Type `<T>`: the class of the objects in the list

        Arguments
        - list: the list to be sorted.

        Raises
        - ClassCastException: if the list contains elements that are not
                *mutually comparable* (for example, strings and integers).
        - UnsupportedOperationException: if the specified list's
                list-iterator does not support the `set` operation.
        - IllegalArgumentException: (optional) if the implementation
                detects that the natural ordering of the list elements is
                found to violate the Comparable contract

        See
        - List.sort(Comparator)

        Unknown Tags
        - This implementation defers to the List.sort(Comparator)
        method using the specified list and a `null` comparator.
        """
        ...


    @staticmethod
    def sort(list: list["T"], c: "Comparator"["T"]) -> None:
        """
        Sorts the specified list according to the order induced by the
        specified comparator.  All elements in the list must be *mutually
        comparable* using the specified comparator (that is,
        `c.compare(e1, e2)` must not throw a `ClassCastException`
        for any elements `e1` and `e2` in the list).
        
        This sort is guaranteed to be *stable*:  equal elements will
        not be reordered as a result of the sort.
        
        The specified list must be modifiable, but need not be resizable.
        
        Type `<T>`: the class of the objects in the list

        Arguments
        - list: the list to be sorted.
        - c: the comparator to determine the order of the list.  A
               `null` value indicates that the elements' *natural
               ordering* should be used.

        Raises
        - ClassCastException: if the list contains elements that are not
                *mutually comparable* using the specified comparator.
        - UnsupportedOperationException: if the specified list's
                list-iterator does not support the `set` operation.
        - IllegalArgumentException: (optional) if the comparator is
                found to violate the Comparator contract

        See
        - List.sort(Comparator)

        Unknown Tags
        - This implementation defers to the List.sort(Comparator)
        method using the specified list and comparator.
        """
        ...


    @staticmethod
    def binarySearch(list: list["Comparable"["T"]], key: "T") -> int:
        """
        Searches the specified list for the specified object using the binary
        search algorithm.  The list must be sorted into ascending order
        according to the Comparable natural ordering of its
        elements (as by the .sort(List) method) prior to making this
        call.  If it is not sorted, the results are undefined.  If the list
        contains multiple elements equal to the specified object, there is no
        guarantee which one will be found.
        
        This method runs in log(n) time for a "random access" list (which
        provides near-constant-time positional access).  If the specified list
        does not implement the RandomAccess interface and is large,
        this method will do an iterator-based binary search that performs
        O(n) link traversals and O(log n) element comparisons.
        
        Type `<T>`: the class of the objects in the list

        Arguments
        - list: the list to be searched.
        - key: the key to be searched for.

        Returns
        - the index of the search key, if it is contained in the list;
                otherwise, `(-(*insertion point*) - 1)`.  The
                *insertion point* is defined as the point at which the
                key would be inserted into the list: the index of the first
                element greater than the key, or `list.size()` if all
                elements in the list are less than the specified key.  Note
                that this guarantees that the return value will be &gt;= 0 if
                and only if the key is found.

        Raises
        - ClassCastException: if the list contains elements that are not
                *mutually comparable* (for example, strings and
                integers), or the search key is not mutually comparable
                with the elements of the list.
        """
        ...


    @staticmethod
    def binarySearch(list: list["T"], key: "T", c: "Comparator"["T"]) -> int:
        """
        Searches the specified list for the specified object using the binary
        search algorithm.  The list must be sorted into ascending order
        according to the specified comparator (as by the
        .sort(List, Comparator) sort(List, Comparator)
        method), prior to making this call.  If it is
        not sorted, the results are undefined.  If the list contains multiple
        elements equal to the specified object, there is no guarantee which one
        will be found.
        
        This method runs in log(n) time for a "random access" list (which
        provides near-constant-time positional access).  If the specified list
        does not implement the RandomAccess interface and is large,
        this method will do an iterator-based binary search that performs
        O(n) link traversals and O(log n) element comparisons.
        
        Type `<T>`: the class of the objects in the list

        Arguments
        - list: the list to be searched.
        - key: the key to be searched for.
        - c: the comparator by which the list is ordered.
                A `null` value indicates that the elements'
                Comparable natural ordering should be used.

        Returns
        - the index of the search key, if it is contained in the list;
                otherwise, `(-(*insertion point*) - 1)`.  The
                *insertion point* is defined as the point at which the
                key would be inserted into the list: the index of the first
                element greater than the key, or `list.size()` if all
                elements in the list are less than the specified key.  Note
                that this guarantees that the return value will be &gt;= 0 if
                and only if the key is found.

        Raises
        - ClassCastException: if the list contains elements that are not
                *mutually comparable* using the specified comparator,
                or the search key is not mutually comparable with the
                elements of the list using this comparator.
        """
        ...


    @staticmethod
    def reverse(list: list[Any]) -> None:
        """
        Reverses the order of the elements in the specified list.
        
        This method runs in linear time.

        Arguments
        - list: the list whose elements are to be reversed.

        Raises
        - UnsupportedOperationException: if the specified list or
                its list-iterator does not support the `set` operation.
        """
        ...


    @staticmethod
    def shuffle(list: list[Any]) -> None:
        """
        Randomly permutes the specified list using a default source of
        randomness.  All permutations occur with approximately equal
        likelihood.
        
        The hedge "approximately" is used in the foregoing description because
        default source of randomness is only approximately an unbiased source
        of independently chosen bits. If it were a perfect source of randomly
        chosen bits, then the algorithm would choose permutations with perfect
        uniformity.
        
        This implementation traverses the list backwards, from the last
        element up to the second, repeatedly swapping a randomly selected element
        into the "current position".  Elements are randomly selected from the
        portion of the list that runs from the first element to the current
        position, inclusive.
        
        This method runs in linear time.  If the specified list does not
        implement the RandomAccess interface and is large, this
        implementation dumps the specified list into an array before shuffling
        it, and dumps the shuffled array back into the list.  This avoids the
        quadratic behavior that would result from shuffling a "sequential
        access" list in place.

        Arguments
        - list: the list to be shuffled.

        Raises
        - UnsupportedOperationException: if the specified list or
                its list-iterator does not support the `set` operation.
        """
        ...


    @staticmethod
    def shuffle(list: list[Any], rnd: "Random") -> None:
        """
        Randomly permute the specified list using the specified source of
        randomness.  All permutations occur with equal likelihood
        assuming that the source of randomness is fair.
        
        This implementation traverses the list backwards, from the last element
        up to the second, repeatedly swapping a randomly selected element into
        the "current position".  Elements are randomly selected from the
        portion of the list that runs from the first element to the current
        position, inclusive.
        
        This method runs in linear time.  If the specified list does not
        implement the RandomAccess interface and is large, this
        implementation dumps the specified list into an array before shuffling
        it, and dumps the shuffled array back into the list.  This avoids the
        quadratic behavior that would result from shuffling a "sequential
        access" list in place.

        Arguments
        - list: the list to be shuffled.
        - rnd: the source of randomness to use to shuffle the list.

        Raises
        - UnsupportedOperationException: if the specified list or its
                list-iterator does not support the `set` operation.
        """
        ...


    @staticmethod
    def swap(list: list[Any], i: int, j: int) -> None:
        """
        Swaps the elements at the specified positions in the specified list.
        (If the specified positions are equal, invoking this method leaves
        the list unchanged.)

        Arguments
        - list: The list in which to swap elements.
        - i: the index of one element to be swapped.
        - j: the index of the other element to be swapped.

        Raises
        - IndexOutOfBoundsException: if either `i` or `j`
                is out of range (i &lt; 0 || i &gt;= list.size()
                || j &lt; 0 || j &gt;= list.size()).

        Since
        - 1.4
        """
        ...


    @staticmethod
    def fill(list: list["T"], obj: "T") -> None:
        """
        Replaces all of the elements of the specified list with the specified
        element. 
        
        This method runs in linear time.
        
        Type `<T>`: the class of the objects in the list

        Arguments
        - list: the list to be filled with the specified element.
        - obj: The element with which to fill the specified list.

        Raises
        - UnsupportedOperationException: if the specified list or its
                list-iterator does not support the `set` operation.
        """
        ...


    @staticmethod
    def copy(dest: list["T"], src: list["T"]) -> None:
        """
        Copies all of the elements from one list into another.  After the
        operation, the index of each copied element in the destination list
        will be identical to its index in the source list.  The destination
        list's size must be greater than or equal to the source list's size.
        If it is greater, the remaining elements in the destination list are
        unaffected. 
        
        This method runs in linear time.
        
        Type `<T>`: the class of the objects in the lists

        Arguments
        - dest: The destination list.
        - src: The source list.

        Raises
        - IndexOutOfBoundsException: if the destination list is too small
                to contain the entire source List.
        - UnsupportedOperationException: if the destination list's
                list-iterator does not support the `set` operation.
        """
        ...


    @staticmethod
    def min(coll: Iterable["T"]) -> "T":
        """
        Returns the minimum element of the given collection, according to the
        *natural ordering* of its elements.  All elements in the
        collection must implement the `Comparable` interface.
        Furthermore, all elements in the collection must be *mutually
        comparable* (that is, `e1.compareTo(e2)` must not throw a
        `ClassCastException` for any elements `e1` and
        `e2` in the collection).
        
        This method iterates over the entire collection, hence it requires
        time proportional to the size of the collection.
        
        Type `<T>`: the class of the objects in the collection

        Arguments
        - coll: the collection whose minimum element is to be determined.

        Returns
        - the minimum element of the given collection, according
                to the *natural ordering* of its elements.

        Raises
        - ClassCastException: if the collection contains elements that are
                not *mutually comparable* (for example, strings and
                integers).
        - NoSuchElementException: if the collection is empty.

        See
        - Comparable
        """
        ...


    @staticmethod
    def min(coll: Iterable["T"], comp: "Comparator"["T"]) -> "T":
        """
        Returns the minimum element of the given collection, according to the
        order induced by the specified comparator.  All elements in the
        collection must be *mutually comparable* by the specified
        comparator (that is, `comp.compare(e1, e2)` must not throw a
        `ClassCastException` for any elements `e1` and
        `e2` in the collection).
        
        This method iterates over the entire collection, hence it requires
        time proportional to the size of the collection.
        
        Type `<T>`: the class of the objects in the collection

        Arguments
        - coll: the collection whose minimum element is to be determined.
        - comp: the comparator with which to determine the minimum element.
                A `null` value indicates that the elements' *natural
                ordering* should be used.

        Returns
        - the minimum element of the given collection, according
                to the specified comparator.

        Raises
        - ClassCastException: if the collection contains elements that are
                not *mutually comparable* using the specified comparator.
        - NoSuchElementException: if the collection is empty.

        See
        - Comparable
        """
        ...


    @staticmethod
    def max(coll: Iterable["T"]) -> "T":
        """
        Returns the maximum element of the given collection, according to the
        *natural ordering* of its elements.  All elements in the
        collection must implement the `Comparable` interface.
        Furthermore, all elements in the collection must be *mutually
        comparable* (that is, `e1.compareTo(e2)` must not throw a
        `ClassCastException` for any elements `e1` and
        `e2` in the collection).
        
        This method iterates over the entire collection, hence it requires
        time proportional to the size of the collection.
        
        Type `<T>`: the class of the objects in the collection

        Arguments
        - coll: the collection whose maximum element is to be determined.

        Returns
        - the maximum element of the given collection, according
                to the *natural ordering* of its elements.

        Raises
        - ClassCastException: if the collection contains elements that are
                not *mutually comparable* (for example, strings and
                integers).
        - NoSuchElementException: if the collection is empty.

        See
        - Comparable
        """
        ...


    @staticmethod
    def max(coll: Iterable["T"], comp: "Comparator"["T"]) -> "T":
        """
        Returns the maximum element of the given collection, according to the
        order induced by the specified comparator.  All elements in the
        collection must be *mutually comparable* by the specified
        comparator (that is, `comp.compare(e1, e2)` must not throw a
        `ClassCastException` for any elements `e1` and
        `e2` in the collection).
        
        This method iterates over the entire collection, hence it requires
        time proportional to the size of the collection.
        
        Type `<T>`: the class of the objects in the collection

        Arguments
        - coll: the collection whose maximum element is to be determined.
        - comp: the comparator with which to determine the maximum element.
                A `null` value indicates that the elements' *natural
               ordering* should be used.

        Returns
        - the maximum element of the given collection, according
                to the specified comparator.

        Raises
        - ClassCastException: if the collection contains elements that are
                not *mutually comparable* using the specified comparator.
        - NoSuchElementException: if the collection is empty.

        See
        - Comparable
        """
        ...


    @staticmethod
    def rotate(list: list[Any], distance: int) -> None:
        """
        Rotates the elements in the specified list by the specified distance.
        After calling this method, the element at index `i` will be
        the element previously at index `(i - distance)` mod
        `list.size()`, for all values of `i` between `0`
        and `list.size()-1`, inclusive.  (This method has no effect on
        the size of the list.)
        
        For example, suppose `list` comprises`[t, a, n, k, s]`.
        After invoking `Collections.rotate(list, 1)` (or
        `Collections.rotate(list, -4)`), `list` will comprise
        `[s, t, a, n, k]`.
        
        Note that this method can usefully be applied to sublists to
        move one or more elements within a list while preserving the
        order of the remaining elements.  For example, the following idiom
        moves the element at index `j` forward to position
        `k` (which must be greater than or equal to `j`):
        ```
            Collections.rotate(list.subList(j, k+1), -1);
        ```
        To make this concrete, suppose `list` comprises
        `[a, b, c, d, e]`.  To move the element at index `1`
        (`b`) forward two positions, perform the following invocation:
        ```
            Collections.rotate(l.subList(1, 4), -1);
        ```
        The resulting list is `[a, c, d, b, e]`.
        
        To move more than one element forward, increase the absolute value
        of the rotation distance.  To move elements backward, use a positive
        shift distance.
        
        If the specified list is small or implements the RandomAccess interface, this implementation exchanges the first
        element into the location it should go, and then repeatedly exchanges
        the displaced element into the location it should go until a displaced
        element is swapped into the first element.  If necessary, the process
        is repeated on the second and successive elements, until the rotation
        is complete.  If the specified list is large and doesn't implement the
        `RandomAccess` interface, this implementation breaks the
        list into two sublist views around index `-distance mod size`.
        Then the .reverse(List) method is invoked on each sublist view,
        and finally it is invoked on the entire list.  For a more complete
        description of both algorithms, see Section 2.3 of Jon Bentley's
        *Programming Pearls* (Addison-Wesley, 1986).

        Arguments
        - list: the list to be rotated.
        - distance: the distance to rotate the list.  There are no
               constraints on this value; it may be zero, negative, or
               greater than `list.size()`.

        Raises
        - UnsupportedOperationException: if the specified list or
                its list-iterator does not support the `set` operation.

        Since
        - 1.4
        """
        ...


    @staticmethod
    def replaceAll(list: list["T"], oldVal: "T", newVal: "T") -> bool:
        """
        Replaces all occurrences of one specified value in a list with another.
        More formally, replaces with `newVal` each element `e`
        in `list` such that
        `(oldVal==null ? e==null : oldVal.equals(e))`.
        (This method has no effect on the size of the list.)
        
        Type `<T>`: the class of the objects in the list

        Arguments
        - list: the list in which replacement is to occur.
        - oldVal: the old value to be replaced.
        - newVal: the new value with which `oldVal` is to be
               replaced.

        Returns
        - `True` if `list` contained one or more elements
                `e` such that
                `(oldVal==null ?  e==null : oldVal.equals(e))`.

        Raises
        - UnsupportedOperationException: if the specified list or
                its list-iterator does not support the `set` operation.

        Since
        - 1.4
        """
        ...


    @staticmethod
    def indexOfSubList(source: list[Any], target: list[Any]) -> int:
        """
        Returns the starting position of the first occurrence of the specified
        target list within the specified source list, or -1 if there is no
        such occurrence.  More formally, returns the lowest index `i`
        such that `source.subList(i, i+target.size()).equals(target)`,
        or -1 if there is no such index.  (Returns -1 if
        `target.size() > source.size()`)
        
        This implementation uses the "brute force" technique of scanning
        over the source list, looking for a match with the target at each
        location in turn.

        Arguments
        - source: the list in which to search for the first occurrence
               of `target`.
        - target: the list to search for as a subList of `source`.

        Returns
        - the starting position of the first occurrence of the specified
                target list within the specified source list, or -1 if there
                is no such occurrence.

        Since
        - 1.4
        """
        ...


    @staticmethod
    def lastIndexOfSubList(source: list[Any], target: list[Any]) -> int:
        """
        Returns the starting position of the last occurrence of the specified
        target list within the specified source list, or -1 if there is no such
        occurrence.  More formally, returns the highest index `i`
        such that `source.subList(i, i+target.size()).equals(target)`,
        or -1 if there is no such index.  (Returns -1 if
        `target.size() > source.size()`)
        
        This implementation uses the "brute force" technique of iterating
        over the source list, looking for a match with the target at each
        location in turn.

        Arguments
        - source: the list in which to search for the last occurrence
               of `target`.
        - target: the list to search for as a subList of `source`.

        Returns
        - the starting position of the last occurrence of the specified
                target list within the specified source list, or -1 if there
                is no such occurrence.

        Since
        - 1.4
        """
        ...


    @staticmethod
    def unmodifiableCollection(c: Iterable["T"]) -> Iterable["T"]:
        """
        Returns an <a href="Collection.html#unmodview">unmodifiable view</a> of the
        specified collection. Query operations on the returned collection "read through"
        to the specified collection, and attempts to modify the returned
        collection, whether direct or via its iterator, result in an
        `UnsupportedOperationException`.
        
        The returned collection does *not* pass the hashCode and equals
        operations through to the backing collection, but relies on
        `Object`'s `equals` and `hashCode` methods.  This
        is necessary to preserve the contracts of these operations in the case
        that the backing collection is a set or a list.
        
        The returned collection will be serializable if the specified collection
        is serializable.
        
        Type `<T>`: the class of the objects in the collection

        Arguments
        - c: the collection for which an unmodifiable view is to be
                returned.

        Returns
        - an unmodifiable view of the specified collection.

        Unknown Tags
        - This method may return its argument if the argument is already unmodifiable.
        """
        ...


    @staticmethod
    def unmodifiableSet(s: set["T"]) -> set["T"]:
        """
        Returns an <a href="Collection.html#unmodview">unmodifiable view</a> of the
        specified set. Query operations on the returned set "read through" to the specified
        set, and attempts to modify the returned set, whether direct or via its
        iterator, result in an `UnsupportedOperationException`.
        
        The returned set will be serializable if the specified set
        is serializable.
        
        Type `<T>`: the class of the objects in the set

        Arguments
        - s: the set for which an unmodifiable view is to be returned.

        Returns
        - an unmodifiable view of the specified set.

        Unknown Tags
        - This method may return its argument if the argument is already unmodifiable.
        """
        ...


    @staticmethod
    def unmodifiableSortedSet(s: "SortedSet"["T"]) -> "SortedSet"["T"]:
        """
        Returns an <a href="Collection.html#unmodview">unmodifiable view</a> of the
        specified sorted set. Query operations on the returned sorted set "read
        through" to the specified sorted set.  Attempts to modify the returned
        sorted set, whether direct, via its iterator, or via its
        `subSet`, `headSet`, or `tailSet` views, result in
        an `UnsupportedOperationException`.
        
        The returned sorted set will be serializable if the specified sorted set
        is serializable.
        
        Type `<T>`: the class of the objects in the set

        Arguments
        - s: the sorted set for which an unmodifiable view is to be
               returned.

        Returns
        - an unmodifiable view of the specified sorted set.

        Unknown Tags
        - This method may return its argument if the argument is already unmodifiable.
        """
        ...


    @staticmethod
    def unmodifiableNavigableSet(s: "NavigableSet"["T"]) -> "NavigableSet"["T"]:
        """
        Returns an <a href="Collection.html#unmodview">unmodifiable view</a> of the
        specified navigable set. Query operations on the returned navigable set "read
        through" to the specified navigable set.  Attempts to modify the returned
        navigable set, whether direct, via its iterator, or via its
        `subSet`, `headSet`, or `tailSet` views, result in
        an `UnsupportedOperationException`.
        
        The returned navigable set will be serializable if the specified
        navigable set is serializable.
        
        Type `<T>`: the class of the objects in the set

        Arguments
        - s: the navigable set for which an unmodifiable view is to be
               returned

        Returns
        - an unmodifiable view of the specified navigable set

        Since
        - 1.8

        Unknown Tags
        - This method may return its argument if the argument is already unmodifiable.
        """
        ...


    @staticmethod
    def unmodifiableList(list: list["T"]) -> list["T"]:
        """
        Returns an <a href="Collection.html#unmodview">unmodifiable view</a> of the
        specified list. Query operations on the returned list "read through" to the
        specified list, and attempts to modify the returned list, whether
        direct or via its iterator, result in an
        `UnsupportedOperationException`.
        
        The returned list will be serializable if the specified list
        is serializable. Similarly, the returned list will implement
        RandomAccess if the specified list does.
        
        Type `<T>`: the class of the objects in the list

        Arguments
        - list: the list for which an unmodifiable view is to be returned.

        Returns
        - an unmodifiable view of the specified list.

        Unknown Tags
        - This method may return its argument if the argument is already unmodifiable.
        """
        ...


    @staticmethod
    def unmodifiableMap(m: dict["K", "V"]) -> dict["K", "V"]:
        """
        Returns an <a href="Collection.html#unmodview">unmodifiable view</a> of the
        specified map. Query operations on the returned map "read through"
        to the specified map, and attempts to modify the returned
        map, whether direct or via its collection views, result in an
        `UnsupportedOperationException`.
        
        The returned map will be serializable if the specified map
        is serializable.
        
        Type `<K>`: the class of the map keys
        
        Type `<V>`: the class of the map values

        Arguments
        - m: the map for which an unmodifiable view is to be returned.

        Returns
        - an unmodifiable view of the specified map.

        Unknown Tags
        - This method may return its argument if the argument is already unmodifiable.
        """
        ...


    @staticmethod
    def unmodifiableSortedMap(m: "SortedMap"["K", "V"]) -> "SortedMap"["K", "V"]:
        """
        Returns an <a href="Collection.html#unmodview">unmodifiable view</a> of the
        specified sorted map. Query operations on the returned sorted map "read through"
        to the specified sorted map.  Attempts to modify the returned
        sorted map, whether direct, via its collection views, or via its
        `subMap`, `headMap`, or `tailMap` views, result in
        an `UnsupportedOperationException`.
        
        The returned sorted map will be serializable if the specified sorted map
        is serializable.
        
        Type `<K>`: the class of the map keys
        
        Type `<V>`: the class of the map values

        Arguments
        - m: the sorted map for which an unmodifiable view is to be
               returned.

        Returns
        - an unmodifiable view of the specified sorted map.

        Unknown Tags
        - This method may return its argument if the argument is already unmodifiable.
        """
        ...


    @staticmethod
    def unmodifiableNavigableMap(m: "NavigableMap"["K", "V"]) -> "NavigableMap"["K", "V"]:
        """
        Returns an <a href="Collection.html#unmodview">unmodifiable view</a> of the
        specified navigable map. Query operations on the returned navigable map "read
        through" to the specified navigable map.  Attempts to modify the returned
        navigable map, whether direct, via its collection views, or via its
        `subMap`, `headMap`, or `tailMap` views, result in
        an `UnsupportedOperationException`.
        
        The returned navigable map will be serializable if the specified
        navigable map is serializable.
        
        Type `<K>`: the class of the map keys
        
        Type `<V>`: the class of the map values

        Arguments
        - m: the navigable map for which an unmodifiable view is to be
               returned

        Returns
        - an unmodifiable view of the specified navigable map

        Since
        - 1.8

        Unknown Tags
        - This method may return its argument if the argument is already unmodifiable.
        """
        ...


    @staticmethod
    def synchronizedCollection(c: Iterable["T"]) -> Iterable["T"]:
        """
        Returns a synchronized (thread-safe) collection backed by the specified
        collection.  In order to guarantee serial access, it is critical that
        <strong>all</strong> access to the backing collection is accomplished
        through the returned collection.
        
        It is imperative that the user manually synchronize on the returned
        collection when traversing it via Iterator, Spliterator
        or Stream:
        ```
         Collection c = Collections.synchronizedCollection(myCollection);
            ...
         synchronized (c) {
             Iterator i = c.iterator(); // Must be in the synchronized block
             while (i.hasNext())
                foo(i.next());
         }
        ```
        Failure to follow this advice may result in non-deterministic behavior.
        
        The returned collection does *not* pass the `hashCode`
        and `equals` operations through to the backing collection, but
        relies on `Object`'s equals and hashCode methods.  This is
        necessary to preserve the contracts of these operations in the case
        that the backing collection is a set or a list.
        
        The returned collection will be serializable if the specified collection
        is serializable.
        
        Type `<T>`: the class of the objects in the collection

        Arguments
        - c: the collection to be "wrapped" in a synchronized collection.

        Returns
        - a synchronized view of the specified collection.
        """
        ...


    @staticmethod
    def synchronizedSet(s: set["T"]) -> set["T"]:
        """
        Returns a synchronized (thread-safe) set backed by the specified
        set.  In order to guarantee serial access, it is critical that
        <strong>all</strong> access to the backing set is accomplished
        through the returned set.
        
        It is imperative that the user manually synchronize on the returned
        collection when traversing it via Iterator, Spliterator
        or Stream:
        ```
         Set s = Collections.synchronizedSet(new HashSet());
             ...
         synchronized (s) {
             Iterator i = s.iterator(); // Must be in the synchronized block
             while (i.hasNext())
                 foo(i.next());
         }
        ```
        Failure to follow this advice may result in non-deterministic behavior.
        
        The returned set will be serializable if the specified set is
        serializable.
        
        Type `<T>`: the class of the objects in the set

        Arguments
        - s: the set to be "wrapped" in a synchronized set.

        Returns
        - a synchronized view of the specified set.
        """
        ...


    @staticmethod
    def synchronizedSortedSet(s: "SortedSet"["T"]) -> "SortedSet"["T"]:
        """
        Returns a synchronized (thread-safe) sorted set backed by the specified
        sorted set.  In order to guarantee serial access, it is critical that
        <strong>all</strong> access to the backing sorted set is accomplished
        through the returned sorted set (or its views).
        
        It is imperative that the user manually synchronize on the returned
        sorted set when traversing it or any of its `subSet`,
        `headSet`, or `tailSet` views via Iterator,
        Spliterator or Stream:
        ```
         SortedSet s = Collections.synchronizedSortedSet(new TreeSet());
             ...
         synchronized (s) {
             Iterator i = s.iterator(); // Must be in the synchronized block
             while (i.hasNext())
                 foo(i.next());
         }
        ```
        or:
        ```
         SortedSet s = Collections.synchronizedSortedSet(new TreeSet());
         SortedSet s2 = s.headSet(foo);
             ...
         synchronized (s) {  // Note: s, not s2!!!
             Iterator i = s2.iterator(); // Must be in the synchronized block
             while (i.hasNext())
                 foo(i.next());
         }
        ```
        Failure to follow this advice may result in non-deterministic behavior.
        
        The returned sorted set will be serializable if the specified
        sorted set is serializable.
        
        Type `<T>`: the class of the objects in the set

        Arguments
        - s: the sorted set to be "wrapped" in a synchronized sorted set.

        Returns
        - a synchronized view of the specified sorted set.
        """
        ...


    @staticmethod
    def synchronizedNavigableSet(s: "NavigableSet"["T"]) -> "NavigableSet"["T"]:
        """
        Returns a synchronized (thread-safe) navigable set backed by the
        specified navigable set.  In order to guarantee serial access, it is
        critical that <strong>all</strong> access to the backing navigable set is
        accomplished through the returned navigable set (or its views).
        
        It is imperative that the user manually synchronize on the returned
        navigable set when traversing it, or any of its `subSet`,
        `headSet`, or `tailSet` views, via Iterator,
        Spliterator or Stream:
        ```
         NavigableSet s = Collections.synchronizedNavigableSet(new TreeSet());
             ...
         synchronized (s) {
             Iterator i = s.iterator(); // Must be in the synchronized block
             while (i.hasNext())
                 foo(i.next());
         }
        ```
        or:
        ```
         NavigableSet s = Collections.synchronizedNavigableSet(new TreeSet());
         NavigableSet s2 = s.headSet(foo, True);
             ...
         synchronized (s) {  // Note: s, not s2!!!
             Iterator i = s2.iterator(); // Must be in the synchronized block
             while (i.hasNext())
                 foo(i.next());
         }
        ```
        Failure to follow this advice may result in non-deterministic behavior.
        
        The returned navigable set will be serializable if the specified
        navigable set is serializable.
        
        Type `<T>`: the class of the objects in the set

        Arguments
        - s: the navigable set to be "wrapped" in a synchronized navigable
        set

        Returns
        - a synchronized view of the specified navigable set

        Since
        - 1.8
        """
        ...


    @staticmethod
    def synchronizedList(list: list["T"]) -> list["T"]:
        """
        Returns a synchronized (thread-safe) list backed by the specified
        list.  In order to guarantee serial access, it is critical that
        <strong>all</strong> access to the backing list is accomplished
        through the returned list.
        
        It is imperative that the user manually synchronize on the returned
        list when traversing it via Iterator, Spliterator
        or Stream:
        ```
         List list = Collections.synchronizedList(new ArrayList());
             ...
         synchronized (list) {
             Iterator i = list.iterator(); // Must be in synchronized block
             while (i.hasNext())
                 foo(i.next());
         }
        ```
        Failure to follow this advice may result in non-deterministic behavior.
        
        The returned list will be serializable if the specified list is
        serializable.
        
        Type `<T>`: the class of the objects in the list

        Arguments
        - list: the list to be "wrapped" in a synchronized list.

        Returns
        - a synchronized view of the specified list.
        """
        ...


    @staticmethod
    def synchronizedMap(m: dict["K", "V"]) -> dict["K", "V"]:
        """
        Returns a synchronized (thread-safe) map backed by the specified
        map.  In order to guarantee serial access, it is critical that
        <strong>all</strong> access to the backing map is accomplished
        through the returned map.
        
        It is imperative that the user manually synchronize on the returned
        map when traversing any of its collection views via Iterator,
        Spliterator or Stream:
        ```
         Map m = Collections.synchronizedMap(new HashMap());
             ...
         Set s = m.keySet();  // Needn't be in synchronized block
             ...
         synchronized (m) {  // Synchronizing on m, not s!
             Iterator i = s.iterator(); // Must be in synchronized block
             while (i.hasNext())
                 foo(i.next());
         }
        ```
        Failure to follow this advice may result in non-deterministic behavior.
        
        The returned map will be serializable if the specified map is
        serializable.
        
        Type `<K>`: the class of the map keys
        
        Type `<V>`: the class of the map values

        Arguments
        - m: the map to be "wrapped" in a synchronized map.

        Returns
        - a synchronized view of the specified map.
        """
        ...


    @staticmethod
    def synchronizedSortedMap(m: "SortedMap"["K", "V"]) -> "SortedMap"["K", "V"]:
        """
        Returns a synchronized (thread-safe) sorted map backed by the specified
        sorted map.  In order to guarantee serial access, it is critical that
        <strong>all</strong> access to the backing sorted map is accomplished
        through the returned sorted map (or its views).
        
        It is imperative that the user manually synchronize on the returned
        sorted map when traversing any of its collection views, or the
        collections views of any of its `subMap`, `headMap` or
        `tailMap` views, via Iterator, Spliterator or
        Stream:
        ```
         SortedMap m = Collections.synchronizedSortedMap(new TreeMap());
             ...
         Set s = m.keySet();  // Needn't be in synchronized block
             ...
         synchronized (m) {  // Synchronizing on m, not s!
             Iterator i = s.iterator(); // Must be in synchronized block
             while (i.hasNext())
                 foo(i.next());
         }
        ```
        or:
        ```
         SortedMap m = Collections.synchronizedSortedMap(new TreeMap());
         SortedMap m2 = m.subMap(foo, bar);
             ...
         Set s2 = m2.keySet();  // Needn't be in synchronized block
             ...
         synchronized (m) {  // Synchronizing on m, not m2 or s2!
             Iterator i = s2.iterator(); // Must be in synchronized block
             while (i.hasNext())
                 foo(i.next());
         }
        ```
        Failure to follow this advice may result in non-deterministic behavior.
        
        The returned sorted map will be serializable if the specified
        sorted map is serializable.
        
        Type `<K>`: the class of the map keys
        
        Type `<V>`: the class of the map values

        Arguments
        - m: the sorted map to be "wrapped" in a synchronized sorted map.

        Returns
        - a synchronized view of the specified sorted map.
        """
        ...


    @staticmethod
    def synchronizedNavigableMap(m: "NavigableMap"["K", "V"]) -> "NavigableMap"["K", "V"]:
        """
        Returns a synchronized (thread-safe) navigable map backed by the
        specified navigable map.  In order to guarantee serial access, it is
        critical that <strong>all</strong> access to the backing navigable map is
        accomplished through the returned navigable map (or its views).
        
        It is imperative that the user manually synchronize on the returned
        navigable map when traversing any of its collection views, or the
        collections views of any of its `subMap`, `headMap` or
        `tailMap` views, via Iterator, Spliterator or
        Stream:
        ```
         NavigableMap m = Collections.synchronizedNavigableMap(new TreeMap());
             ...
         Set s = m.keySet();  // Needn't be in synchronized block
             ...
         synchronized (m) {  // Synchronizing on m, not s!
             Iterator i = s.iterator(); // Must be in synchronized block
             while (i.hasNext())
                 foo(i.next());
         }
        ```
        or:
        ```
         NavigableMap m = Collections.synchronizedNavigableMap(new TreeMap());
         NavigableMap m2 = m.subMap(foo, True, bar, False);
             ...
         Set s2 = m2.keySet();  // Needn't be in synchronized block
             ...
         synchronized (m) {  // Synchronizing on m, not m2 or s2!
             Iterator i = s.iterator(); // Must be in synchronized block
             while (i.hasNext())
                 foo(i.next());
         }
        ```
        Failure to follow this advice may result in non-deterministic behavior.
        
        The returned navigable map will be serializable if the specified
        navigable map is serializable.
        
        Type `<K>`: the class of the map keys
        
        Type `<V>`: the class of the map values

        Arguments
        - m: the navigable map to be "wrapped" in a synchronized navigable
                     map

        Returns
        - a synchronized view of the specified navigable map.

        Since
        - 1.8
        """
        ...


    @staticmethod
    def checkedCollection(c: Iterable["E"], type: type["E"]) -> Iterable["E"]:
        """
        Returns a dynamically typesafe view of the specified collection.
        Any attempt to insert an element of the wrong type will result in an
        immediate ClassCastException.  Assuming a collection
        contains no incorrectly typed elements prior to the time a
        dynamically typesafe view is generated, and that all subsequent
        access to the collection takes place through the view, it is
        *guaranteed* that the collection cannot contain an incorrectly
        typed element.
        
        The generics mechanism in the language provides compile-time
        (static) type checking, but it is possible to defeat this mechanism
        with unchecked casts.  Usually this is not a problem, as the compiler
        issues warnings on all such unchecked operations.  There are, however,
        times when static type checking alone is not sufficient.  For example,
        suppose a collection is passed to a third-party library and it is
        imperative that the library code not corrupt the collection by
        inserting an element of the wrong type.
        
        Another use of dynamically typesafe views is debugging.  Suppose a
        program fails with a `ClassCastException`, indicating that an
        incorrectly typed element was put into a parameterized collection.
        Unfortunately, the exception can occur at any time after the erroneous
        element is inserted, so it typically provides little or no information
        as to the real source of the problem.  If the problem is reproducible,
        one can quickly determine its source by temporarily modifying the
        program to wrap the collection with a dynamically typesafe view.
        For example, this declaration:
         ``` `Collection<String> c = new HashSet<>();````
        may be replaced temporarily by this one:
         ``` `Collection<String> c = Collections.checkedCollection(
                new HashSet<>(), String.class);````
        Running the program again will cause it to fail at the point where
        an incorrectly typed element is inserted into the collection, clearly
        identifying the source of the problem.  Once the problem is fixed, the
        modified declaration may be reverted back to the original.
        
        The returned collection does *not* pass the hashCode and equals
        operations through to the backing collection, but relies on
        `Object`'s `equals` and `hashCode` methods.  This
        is necessary to preserve the contracts of these operations in the case
        that the backing collection is a set or a list.
        
        The returned collection will be serializable if the specified
        collection is serializable.
        
        Since `null` is considered to be a value of any reference
        type, the returned collection permits insertion of null elements
        whenever the backing collection does.
        
        Type `<E>`: the class of the objects in the collection

        Arguments
        - c: the collection for which a dynamically typesafe view is to be
                 returned
        - type: the type of element that `c` is permitted to hold

        Returns
        - a dynamically typesafe view of the specified collection

        Since
        - 1.5
        """
        ...


    @staticmethod
    def checkedQueue(queue: "Queue"["E"], type: type["E"]) -> "Queue"["E"]:
        """
        Returns a dynamically typesafe view of the specified queue.
        Any attempt to insert an element of the wrong type will result in
        an immediate ClassCastException.  Assuming a queue contains
        no incorrectly typed elements prior to the time a dynamically typesafe
        view is generated, and that all subsequent access to the queue
        takes place through the view, it is *guaranteed* that the
        queue cannot contain an incorrectly typed element.
        
        A discussion of the use of dynamically typesafe views may be
        found in the documentation for the .checkedCollection
        checkedCollection method.
        
        The returned queue will be serializable if the specified queue
        is serializable.
        
        Since `null` is considered to be a value of any reference
        type, the returned queue permits insertion of `null` elements
        whenever the backing queue does.
        
        Type `<E>`: the class of the objects in the queue

        Arguments
        - queue: the queue for which a dynamically typesafe view is to be
                    returned
        - type: the type of element that `queue` is permitted to hold

        Returns
        - a dynamically typesafe view of the specified queue

        Since
        - 1.8
        """
        ...


    @staticmethod
    def checkedSet(s: set["E"], type: type["E"]) -> set["E"]:
        """
        Returns a dynamically typesafe view of the specified set.
        Any attempt to insert an element of the wrong type will result in
        an immediate ClassCastException.  Assuming a set contains
        no incorrectly typed elements prior to the time a dynamically typesafe
        view is generated, and that all subsequent access to the set
        takes place through the view, it is *guaranteed* that the
        set cannot contain an incorrectly typed element.
        
        A discussion of the use of dynamically typesafe views may be
        found in the documentation for the .checkedCollection
        checkedCollection method.
        
        The returned set will be serializable if the specified set is
        serializable.
        
        Since `null` is considered to be a value of any reference
        type, the returned set permits insertion of null elements whenever
        the backing set does.
        
        Type `<E>`: the class of the objects in the set

        Arguments
        - s: the set for which a dynamically typesafe view is to be
                 returned
        - type: the type of element that `s` is permitted to hold

        Returns
        - a dynamically typesafe view of the specified set

        Since
        - 1.5
        """
        ...


    @staticmethod
    def checkedSortedSet(s: "SortedSet"["E"], type: type["E"]) -> "SortedSet"["E"]:
        """
        Returns a dynamically typesafe view of the specified sorted set.
        Any attempt to insert an element of the wrong type will result in an
        immediate ClassCastException.  Assuming a sorted set
        contains no incorrectly typed elements prior to the time a
        dynamically typesafe view is generated, and that all subsequent
        access to the sorted set takes place through the view, it is
        *guaranteed* that the sorted set cannot contain an incorrectly
        typed element.
        
        A discussion of the use of dynamically typesafe views may be
        found in the documentation for the .checkedCollection
        checkedCollection method.
        
        The returned sorted set will be serializable if the specified sorted
        set is serializable.
        
        Since `null` is considered to be a value of any reference
        type, the returned sorted set permits insertion of null elements
        whenever the backing sorted set does.
        
        Type `<E>`: the class of the objects in the set

        Arguments
        - s: the sorted set for which a dynamically typesafe view is to be
                 returned
        - type: the type of element that `s` is permitted to hold

        Returns
        - a dynamically typesafe view of the specified sorted set

        Since
        - 1.5
        """
        ...


    @staticmethod
    def checkedNavigableSet(s: "NavigableSet"["E"], type: type["E"]) -> "NavigableSet"["E"]:
        """
        Returns a dynamically typesafe view of the specified navigable set.
        Any attempt to insert an element of the wrong type will result in an
        immediate ClassCastException.  Assuming a navigable set
        contains no incorrectly typed elements prior to the time a
        dynamically typesafe view is generated, and that all subsequent
        access to the navigable set takes place through the view, it is
        *guaranteed* that the navigable set cannot contain an incorrectly
        typed element.
        
        A discussion of the use of dynamically typesafe views may be
        found in the documentation for the .checkedCollection
        checkedCollection method.
        
        The returned navigable set will be serializable if the specified
        navigable set is serializable.
        
        Since `null` is considered to be a value of any reference
        type, the returned navigable set permits insertion of null elements
        whenever the backing sorted set does.
        
        Type `<E>`: the class of the objects in the set

        Arguments
        - s: the navigable set for which a dynamically typesafe view is to be
                 returned
        - type: the type of element that `s` is permitted to hold

        Returns
        - a dynamically typesafe view of the specified navigable set

        Since
        - 1.8
        """
        ...


    @staticmethod
    def checkedList(list: list["E"], type: type["E"]) -> list["E"]:
        """
        Returns a dynamically typesafe view of the specified list.
        Any attempt to insert an element of the wrong type will result in
        an immediate ClassCastException.  Assuming a list contains
        no incorrectly typed elements prior to the time a dynamically typesafe
        view is generated, and that all subsequent access to the list
        takes place through the view, it is *guaranteed* that the
        list cannot contain an incorrectly typed element.
        
        A discussion of the use of dynamically typesafe views may be
        found in the documentation for the .checkedCollection
        checkedCollection method.
        
        The returned list will be serializable if the specified list
        is serializable.
        
        Since `null` is considered to be a value of any reference
        type, the returned list permits insertion of null elements whenever
        the backing list does.
        
        Type `<E>`: the class of the objects in the list

        Arguments
        - list: the list for which a dynamically typesafe view is to be
                    returned
        - type: the type of element that `list` is permitted to hold

        Returns
        - a dynamically typesafe view of the specified list

        Since
        - 1.5
        """
        ...


    @staticmethod
    def checkedMap(m: dict["K", "V"], keyType: type["K"], valueType: type["V"]) -> dict["K", "V"]:
        """
        Returns a dynamically typesafe view of the specified map.
        Any attempt to insert a mapping whose key or value have the wrong
        type will result in an immediate ClassCastException.
        Similarly, any attempt to modify the value currently associated with
        a key will result in an immediate ClassCastException,
        whether the modification is attempted directly through the map
        itself, or through a Map.Entry instance obtained from the
        map's Map.entrySet() entry set view.
        
        Assuming a map contains no incorrectly typed keys or values
        prior to the time a dynamically typesafe view is generated, and
        that all subsequent access to the map takes place through the view
        (or one of its collection views), it is *guaranteed* that the
        map cannot contain an incorrectly typed key or value.
        
        A discussion of the use of dynamically typesafe views may be
        found in the documentation for the .checkedCollection
        checkedCollection method.
        
        The returned map will be serializable if the specified map is
        serializable.
        
        Since `null` is considered to be a value of any reference
        type, the returned map permits insertion of null keys or values
        whenever the backing map does.
        
        Type `<K>`: the class of the map keys
        
        Type `<V>`: the class of the map values

        Arguments
        - m: the map for which a dynamically typesafe view is to be
                 returned
        - keyType: the type of key that `m` is permitted to hold
        - valueType: the type of value that `m` is permitted to hold

        Returns
        - a dynamically typesafe view of the specified map

        Since
        - 1.5
        """
        ...


    @staticmethod
    def checkedSortedMap(m: "SortedMap"["K", "V"], keyType: type["K"], valueType: type["V"]) -> "SortedMap"["K", "V"]:
        """
        Returns a dynamically typesafe view of the specified sorted map.
        Any attempt to insert a mapping whose key or value have the wrong
        type will result in an immediate ClassCastException.
        Similarly, any attempt to modify the value currently associated with
        a key will result in an immediate ClassCastException,
        whether the modification is attempted directly through the map
        itself, or through a Map.Entry instance obtained from the
        map's Map.entrySet() entry set view.
        
        Assuming a map contains no incorrectly typed keys or values
        prior to the time a dynamically typesafe view is generated, and
        that all subsequent access to the map takes place through the view
        (or one of its collection views), it is *guaranteed* that the
        map cannot contain an incorrectly typed key or value.
        
        A discussion of the use of dynamically typesafe views may be
        found in the documentation for the .checkedCollection
        checkedCollection method.
        
        The returned map will be serializable if the specified map is
        serializable.
        
        Since `null` is considered to be a value of any reference
        type, the returned map permits insertion of null keys or values
        whenever the backing map does.
        
        Type `<K>`: the class of the map keys
        
        Type `<V>`: the class of the map values

        Arguments
        - m: the map for which a dynamically typesafe view is to be
                 returned
        - keyType: the type of key that `m` is permitted to hold
        - valueType: the type of value that `m` is permitted to hold

        Returns
        - a dynamically typesafe view of the specified map

        Since
        - 1.5
        """
        ...


    @staticmethod
    def checkedNavigableMap(m: "NavigableMap"["K", "V"], keyType: type["K"], valueType: type["V"]) -> "NavigableMap"["K", "V"]:
        """
        Returns a dynamically typesafe view of the specified navigable map.
        Any attempt to insert a mapping whose key or value have the wrong
        type will result in an immediate ClassCastException.
        Similarly, any attempt to modify the value currently associated with
        a key will result in an immediate ClassCastException,
        whether the modification is attempted directly through the map
        itself, or through a Map.Entry instance obtained from the
        map's Map.entrySet() entry set view.
        
        Assuming a map contains no incorrectly typed keys or values
        prior to the time a dynamically typesafe view is generated, and
        that all subsequent access to the map takes place through the view
        (or one of its collection views), it is *guaranteed* that the
        map cannot contain an incorrectly typed key or value.
        
        A discussion of the use of dynamically typesafe views may be
        found in the documentation for the .checkedCollection
        checkedCollection method.
        
        The returned map will be serializable if the specified map is
        serializable.
        
        Since `null` is considered to be a value of any reference
        type, the returned map permits insertion of null keys or values
        whenever the backing map does.
        
        Type `<K>`: type of map keys
        
        Type `<V>`: type of map values

        Arguments
        - m: the map for which a dynamically typesafe view is to be
                 returned
        - keyType: the type of key that `m` is permitted to hold
        - valueType: the type of value that `m` is permitted to hold

        Returns
        - a dynamically typesafe view of the specified map

        Since
        - 1.8
        """
        ...


    @staticmethod
    def emptyIterator() -> Iterator["T"]:
        """
        Returns an iterator that has no elements.  More precisely,
        
        
        - Iterator.hasNext hasNext always returns `False`.
        - Iterator.next next always throws NoSuchElementException.
        - Iterator.remove remove always throws IllegalStateException.
        
        
        Implementations of this method are permitted, but not
        required, to return the same object from multiple invocations.
        
        Type `<T>`: type of elements, if there were any, in the iterator

        Returns
        - an empty iterator

        Since
        - 1.7
        """
        ...


    @staticmethod
    def emptyListIterator() -> "ListIterator"["T"]:
        """
        Returns a list iterator that has no elements.  More precisely,
        
        
        - Iterator.hasNext hasNext and ListIterator.hasPrevious hasPrevious always return `False`.
        - Iterator.next next and ListIterator.previous
        previous always throw NoSuchElementException.
        - Iterator.remove remove and ListIterator.set
        set always throw IllegalStateException.
        - ListIterator.add add always throws UnsupportedOperationException.
        - ListIterator.nextIndex nextIndex always returns
        `0`.
        - ListIterator.previousIndex previousIndex always
        returns `-1`.
        
        
        Implementations of this method are permitted, but not
        required, to return the same object from multiple invocations.
        
        Type `<T>`: type of elements, if there were any, in the iterator

        Returns
        - an empty list iterator

        Since
        - 1.7
        """
        ...


    @staticmethod
    def emptyEnumeration() -> "Enumeration"["T"]:
        """
        Returns an enumeration that has no elements.  More precisely,
        
        
        - Enumeration.hasMoreElements hasMoreElements always
        returns `False`.
        -  Enumeration.nextElement nextElement always throws
        NoSuchElementException.
        
        
        Implementations of this method are permitted, but not
        required, to return the same object from multiple invocations.
        
        Type `<T>`: the class of the objects in the enumeration

        Returns
        - an empty enumeration

        Since
        - 1.7
        """
        ...


    @staticmethod
    def emptySet() -> set["T"]:
        """
        Returns an empty set (immutable).  This set is serializable.
        Unlike the like-named field, this method is parameterized.
        
        This example illustrates the type-safe way to obtain an empty set:
        ```
            Set&lt;String&gt; s = Collections.emptySet();
        ```
        
        Type `<T>`: the class of the objects in the set

        Returns
        - the empty set

        See
        - .EMPTY_SET

        Since
        - 1.5

        Unknown Tags
        - Implementations of this method need not create a separate
        `Set` object for each call.  Using this method is likely to have
        comparable cost to using the like-named field.  (Unlike this method, the
        field does not provide type safety.)
        """
        ...


    @staticmethod
    def emptySortedSet() -> "SortedSet"["E"]:
        """
        Returns an empty sorted set (immutable).  This set is serializable.
        
        This example illustrates the type-safe way to obtain an empty
        sorted set:
        ``` `SortedSet<String> s = Collections.emptySortedSet();````
        
        Type `<E>`: type of elements, if there were any, in the set

        Returns
        - the empty sorted set

        Since
        - 1.8

        Unknown Tags
        - Implementations of this method need not create a separate
        `SortedSet` object for each call.
        """
        ...


    @staticmethod
    def emptyNavigableSet() -> "NavigableSet"["E"]:
        """
        Returns an empty navigable set (immutable).  This set is serializable.
        
        This example illustrates the type-safe way to obtain an empty
        navigable set:
        ``` `NavigableSet<String> s = Collections.emptyNavigableSet();````
        
        Type `<E>`: type of elements, if there were any, in the set

        Returns
        - the empty navigable set

        Since
        - 1.8

        Unknown Tags
        - Implementations of this method need not
        create a separate `NavigableSet` object for each call.
        """
        ...


    @staticmethod
    def emptyList() -> list["T"]:
        """
        Returns an empty list (immutable).  This list is serializable.
        
        This example illustrates the type-safe way to obtain an empty list:
        ```
            List&lt;String&gt; s = Collections.emptyList();
        ```
        
        Type `<T>`: type of elements, if there were any, in the list

        Returns
        - an empty immutable list

        See
        - .EMPTY_LIST

        Since
        - 1.5

        Unknown Tags
        - Implementations of this method need not create a separate `List`
        object for each call.   Using this method is likely to have comparable
        cost to using the like-named field.  (Unlike this method, the field does
        not provide type safety.)
        """
        ...


    @staticmethod
    def emptyMap() -> dict["K", "V"]:
        """
        Returns an empty map (immutable).  This map is serializable.
        
        This example illustrates the type-safe way to obtain an empty map:
        ```
            Map&lt;String, Date&gt; s = Collections.emptyMap();
        ```
        
        Type `<K>`: the class of the map keys
        
        Type `<V>`: the class of the map values

        Returns
        - an empty map

        See
        - .EMPTY_MAP

        Since
        - 1.5

        Unknown Tags
        - Implementations of this method need not create a separate
        `Map` object for each call.  Using this method is likely to have
        comparable cost to using the like-named field.  (Unlike this method, the
        field does not provide type safety.)
        """
        ...


    @staticmethod
    def emptySortedMap() -> "SortedMap"["K", "V"]:
        """
        Returns an empty sorted map (immutable).  This map is serializable.
        
        This example illustrates the type-safe way to obtain an empty map:
        ``` `SortedMap<String, Date> s = Collections.emptySortedMap();````
        
        Type `<K>`: the class of the map keys
        
        Type `<V>`: the class of the map values

        Returns
        - an empty sorted map

        Since
        - 1.8

        Unknown Tags
        - Implementations of this method need not create a separate
        `SortedMap` object for each call.
        """
        ...


    @staticmethod
    def emptyNavigableMap() -> "NavigableMap"["K", "V"]:
        """
        Returns an empty navigable map (immutable).  This map is serializable.
        
        This example illustrates the type-safe way to obtain an empty map:
        ``` `NavigableMap<String, Date> s = Collections.emptyNavigableMap();````
        
        Type `<K>`: the class of the map keys
        
        Type `<V>`: the class of the map values

        Returns
        - an empty navigable map

        Since
        - 1.8

        Unknown Tags
        - Implementations of this method need not create a separate
        `NavigableMap` object for each call.
        """
        ...


    @staticmethod
    def singleton(o: "T") -> set["T"]:
        """
        Returns an immutable set containing only the specified object.
        The returned set is serializable.
        
        Type `<T>`: the class of the objects in the set

        Arguments
        - o: the sole object to be stored in the returned set.

        Returns
        - an immutable set containing only the specified object.
        """
        ...


    @staticmethod
    def singletonList(o: "T") -> list["T"]:
        """
        Returns an immutable list containing only the specified object.
        The returned list is serializable.
        
        Type `<T>`: the class of the objects in the list

        Arguments
        - o: the sole object to be stored in the returned list.

        Returns
        - an immutable list containing only the specified object.

        Since
        - 1.3
        """
        ...


    @staticmethod
    def singletonMap(key: "K", value: "V") -> dict["K", "V"]:
        """
        Returns an immutable map, mapping only the specified key to the
        specified value.  The returned map is serializable.
        
        Type `<K>`: the class of the map keys
        
        Type `<V>`: the class of the map values

        Arguments
        - key: the sole key to be stored in the returned map.
        - value: the value to which the returned map maps `key`.

        Returns
        - an immutable map containing only the specified key-value
                mapping.

        Since
        - 1.3
        """
        ...


    @staticmethod
    def nCopies(n: int, o: "T") -> list["T"]:
        """
        Returns an immutable list consisting of `n` copies of the
        specified object.  The newly allocated data object is tiny (it contains
        a single reference to the data object).  This method is useful in
        combination with the `List.addAll` method to grow lists.
        The returned list is serializable.
        
        Type `<T>`: the class of the object to copy and of the objects
                in the returned list.

        Arguments
        - n: the number of elements in the returned list.
        - o: the element to appear repeatedly in the returned list.

        Returns
        - an immutable list consisting of `n` copies of the
                specified object.

        Raises
        - IllegalArgumentException: if `n < 0`

        See
        - List.addAll(int, Collection)
        """
        ...


    @staticmethod
    def reverseOrder() -> "Comparator"["T"]:
        """
        Returns a comparator that imposes the reverse of the *natural
        ordering* on a collection of objects that implement the
        `Comparable` interface.  (The natural ordering is the ordering
        imposed by the objects' own `compareTo` method.)  This enables a
        simple idiom for sorting (or maintaining) collections (or arrays) of
        objects that implement the `Comparable` interface in
        reverse-natural-order.  For example, suppose `a` is an array of
        strings. Then: ```
                 Arrays.sort(a, Collections.reverseOrder());
        ``` sorts the array in reverse-lexicographic (alphabetical) order.
        
        The returned comparator is serializable.
        
        Type `<T>`: the class of the objects compared by the comparator

        Returns
        - A comparator that imposes the reverse of the *natural
                ordering* on a collection of objects that implement
                the `Comparable` interface.

        See
        - Comparable
        """
        ...


    @staticmethod
    def reverseOrder(cmp: "Comparator"["T"]) -> "Comparator"["T"]:
        """
        Returns a comparator that imposes the reverse ordering of the specified
        comparator.  If the specified comparator is `null`, this method is
        equivalent to .reverseOrder() (in other words, it returns a
        comparator that imposes the reverse of the *natural ordering* on
        a collection of objects that implement the Comparable interface).
        
        The returned comparator is serializable (assuming the specified
        comparator is also serializable or `null`).
        
        Type `<T>`: the class of the objects compared by the comparator

        Arguments
        - cmp: a comparator who's ordering is to be reversed by the returned
        comparator or `null`

        Returns
        - A comparator that imposes the reverse ordering of the
                specified comparator.

        Since
        - 1.5
        """
        ...


    @staticmethod
    def enumeration(c: Iterable["T"]) -> "Enumeration"["T"]:
        """
        Returns an enumeration over the specified collection.  This provides
        interoperability with legacy APIs that require an enumeration
        as input.
        
        The iterator returned from a call to Enumeration.asIterator()
        does not support removal of elements from the specified collection.  This
        is necessary to avoid unintentionally increasing the capabilities of the
        returned enumeration.
        
        Type `<T>`: the class of the objects in the collection

        Arguments
        - c: the collection for which an enumeration is to be returned.

        Returns
        - an enumeration over the specified collection.

        See
        - Enumeration
        """
        ...


    @staticmethod
    def list(e: "Enumeration"["T"]) -> list["T"]:
        """
        Returns an array list containing the elements returned by the
        specified enumeration in the order they are returned by the
        enumeration.  This method provides interoperability between
        legacy APIs that return enumerations and new APIs that require
        collections.
        
        Type `<T>`: the class of the objects returned by the enumeration

        Arguments
        - e: enumeration providing elements for the returned
                 array list

        Returns
        - an array list containing the elements returned
                by the specified enumeration.

        See
        - ArrayList

        Since
        - 1.4
        """
        ...


    @staticmethod
    def frequency(c: Iterable[Any], o: "Object") -> int:
        """
        Returns the number of elements in the specified collection equal to the
        specified object.  More formally, returns the number of elements
        `e` in the collection such that
        `Objects.equals(o, e)`.

        Arguments
        - c: the collection in which to determine the frequency
            of `o`
        - o: the object whose frequency is to be determined

        Returns
        - the number of elements in `c` equal to `o`

        Raises
        - NullPointerException: if `c` is null

        Since
        - 1.5
        """
        ...


    @staticmethod
    def disjoint(c1: Iterable[Any], c2: Iterable[Any]) -> bool:
        """
        Returns `True` if the two specified collections have no
        elements in common.
        
        Care must be exercised if this method is used on collections that
        do not comply with the general contract for `Collection`.
        Implementations may elect to iterate over either collection and test
        for containment in the other collection (or to perform any equivalent
        computation).  If either collection uses a nonstandard equality test
        (as does a SortedSet whose ordering is not *compatible with
        equals*, or the key set of an IdentityHashMap), both
        collections must use the same nonstandard equality test, or the
        result of this method is undefined.
        
        Care must also be exercised when using collections that have
        restrictions on the elements that they may contain. Collection
        implementations are allowed to throw exceptions for any operation
        involving elements they deem ineligible. For absolute safety the
        specified collections should contain only elements which are
        eligible elements for both collections.
        
        Note that it is permissible to pass the same collection in both
        parameters, in which case the method will return `True` if and
        only if the collection is empty.

        Arguments
        - c1: a collection
        - c2: a collection

        Returns
        - `True` if the two specified collections have no
        elements in common.

        Raises
        - NullPointerException: if either collection is `null`.
        - NullPointerException: if one collection contains a `null`
        element and `null` is not an eligible element for the other collection.
        (<a href="Collection.html#optional-restrictions">optional</a>)
        - ClassCastException: if one collection contains an element that is
        of a type which is ineligible for the other collection.
        (<a href="Collection.html#optional-restrictions">optional</a>)

        Since
        - 1.5
        """
        ...


    @staticmethod
    def addAll(c: Iterable["T"], *elements: Tuple["T", ...]) -> bool:
        """
        Adds all of the specified elements to the specified collection.
        Elements to be added may be specified individually or as an array.
        The behaviour of this convenience method is similar to that of
        `cc.addAll(Collections.unmodifiableList(Arrays.asList(elements)))`.
        
        When elements are specified individually, this method provides a
        convenient way to add a few elements to an existing collection:
        ```
            Collections.addAll(flavors, "Peaches 'n Plutonium", "Rocky Racoon");
        ```
        
        Type `<T>`: the class of the elements to add and of the collection

        Arguments
        - c: the collection into which `elements` are to be inserted
        - elements: the elements to insert into `c`

        Returns
        - `True` if the collection changed as a result of the call

        Raises
        - UnsupportedOperationException: if `c` does not support
                the `add` operation
        - NullPointerException: if `elements` contains one or more
                null values and `c` does not permit null elements, or
                if `c` or `elements` are `null`
        - IllegalArgumentException: if some property of a value in
                `elements` prevents it from being added to `c`

        See
        - Collection.addAll(Collection)

        Since
        - 1.5
        """
        ...


    @staticmethod
    def newSetFromMap(map: dict["E", "Boolean"]) -> set["E"]:
        """
        Returns a set backed by the specified map.  The resulting set displays
        the same ordering, concurrency, and performance characteristics as the
        backing map.  In essence, this factory method provides a Set
        implementation corresponding to any Map implementation.  There
        is no need to use this method on a Map implementation that
        already has a corresponding Set implementation (such as HashMap or TreeMap).
        
        Each method invocation on the set returned by this method results in
        exactly one method invocation on the backing map or its `keySet`
        view, with one exception.  The `addAll` method is implemented
        as a sequence of `put` invocations on the backing map.
        
        The specified map must be empty at the time this method is invoked,
        and should not be accessed directly after this method returns.  These
        conditions are ensured if the map is created empty, passed directly
        to this method, and no reference to the map is retained, as illustrated
        in the following code fragment:
        ```
           Set&lt;Object&gt; weakHashSet = Collections.newSetFromMap(
               new WeakHashMap&lt;Object, Boolean&gt;());
        ```
        
        Type `<E>`: the class of the map keys and of the objects in the
               returned set

        Arguments
        - map: the backing map

        Returns
        - the set backed by the map

        Raises
        - IllegalArgumentException: if `map` is not empty

        Since
        - 1.6
        """
        ...


    @staticmethod
    def asLifoQueue(deque: "Deque"["T"]) -> "Queue"["T"]:
        """
        Returns a view of a Deque as a Last-in-first-out (Lifo)
        Queue. Method `add` is mapped to `push`,
        `remove` is mapped to `pop` and so on. This
        view can be useful when you would like to use a method
        requiring a `Queue` but you need Lifo ordering.
        
        Each method invocation on the queue returned by this method
        results in exactly one method invocation on the backing deque, with
        one exception.  The Queue.addAll addAll method is
        implemented as a sequence of Deque.addFirst addFirst
        invocations on the backing deque.
        
        Type `<T>`: the class of the objects in the deque

        Arguments
        - deque: the deque

        Returns
        - the queue

        Since
        - 1.6
        """
        ...
