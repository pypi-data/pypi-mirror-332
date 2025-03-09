"""
Python module generated from Java source file java.util.SortedMap

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util import *
from typing import Any, Callable, Iterable, Tuple


class SortedMap(Map):

    def comparator(self) -> "Comparator"["K"]:
        """
        Returns the comparator used to order the keys in this map, or
        `null` if this map uses the Comparable
        natural ordering of its keys.

        Returns
        - the comparator used to order the keys in this map,
                or `null` if this map uses the natural ordering
                of its keys
        """
        ...


    def subMap(self, fromKey: "K", toKey: "K") -> "SortedMap"["K", "V"]:
        """
        Returns a view of the portion of this map whose keys range from
        `fromKey`, inclusive, to `toKey`, exclusive.  (If
        `fromKey` and `toKey` are equal, the returned map
        is empty.)  The returned map is backed by this map, so changes
        in the returned map are reflected in this map, and vice-versa.
        The returned map supports all optional map operations that this
        map supports.
        
        The returned map will throw an `IllegalArgumentException`
        on an attempt to insert a key outside its range.

        Arguments
        - fromKey: low endpoint (inclusive) of the keys in the returned map
        - toKey: high endpoint (exclusive) of the keys in the returned map

        Returns
        - a view of the portion of this map whose keys range from
                `fromKey`, inclusive, to `toKey`, exclusive

        Raises
        - ClassCastException: if `fromKey` and `toKey`
                cannot be compared to one another using this map's comparator
                (or, if the map has no comparator, using natural ordering).
                Implementations may, but are not required to, throw this
                exception if `fromKey` or `toKey`
                cannot be compared to keys currently in the map.
        - NullPointerException: if `fromKey` or `toKey`
                is null and this map does not permit null keys
        - IllegalArgumentException: if `fromKey` is greater than
                `toKey`; or if this map itself has a restricted
                range, and `fromKey` or `toKey` lies
                outside the bounds of the range
        """
        ...


    def headMap(self, toKey: "K") -> "SortedMap"["K", "V"]:
        """
        Returns a view of the portion of this map whose keys are
        strictly less than `toKey`.  The returned map is backed
        by this map, so changes in the returned map are reflected in
        this map, and vice-versa.  The returned map supports all
        optional map operations that this map supports.
        
        The returned map will throw an `IllegalArgumentException`
        on an attempt to insert a key outside its range.

        Arguments
        - toKey: high endpoint (exclusive) of the keys in the returned map

        Returns
        - a view of the portion of this map whose keys are strictly
                less than `toKey`

        Raises
        - ClassCastException: if `toKey` is not compatible
                with this map's comparator (or, if the map has no comparator,
                if `toKey` does not implement Comparable).
                Implementations may, but are not required to, throw this
                exception if `toKey` cannot be compared to keys
                currently in the map.
        - NullPointerException: if `toKey` is null and
                this map does not permit null keys
        - IllegalArgumentException: if this map itself has a
                restricted range, and `toKey` lies outside the
                bounds of the range
        """
        ...


    def tailMap(self, fromKey: "K") -> "SortedMap"["K", "V"]:
        """
        Returns a view of the portion of this map whose keys are
        greater than or equal to `fromKey`.  The returned map is
        backed by this map, so changes in the returned map are
        reflected in this map, and vice-versa.  The returned map
        supports all optional map operations that this map supports.
        
        The returned map will throw an `IllegalArgumentException`
        on an attempt to insert a key outside its range.

        Arguments
        - fromKey: low endpoint (inclusive) of the keys in the returned map

        Returns
        - a view of the portion of this map whose keys are greater
                than or equal to `fromKey`

        Raises
        - ClassCastException: if `fromKey` is not compatible
                with this map's comparator (or, if the map has no comparator,
                if `fromKey` does not implement Comparable).
                Implementations may, but are not required to, throw this
                exception if `fromKey` cannot be compared to keys
                currently in the map.
        - NullPointerException: if `fromKey` is null and
                this map does not permit null keys
        - IllegalArgumentException: if this map itself has a
                restricted range, and `fromKey` lies outside the
                bounds of the range
        """
        ...


    def firstKey(self) -> "K":
        """
        Returns the first (lowest) key currently in this map.

        Returns
        - the first (lowest) key currently in this map

        Raises
        - NoSuchElementException: if this map is empty
        """
        ...


    def lastKey(self) -> "K":
        """
        Returns the last (highest) key currently in this map.

        Returns
        - the last (highest) key currently in this map

        Raises
        - NoSuchElementException: if this map is empty
        """
        ...


    def keySet(self) -> set["K"]:
        """
        Returns a Set view of the keys contained in this map.
        The set's iterator returns the keys in ascending order.
        The set is backed by the map, so changes to the map are
        reflected in the set, and vice-versa.  If the map is modified
        while an iteration over the set is in progress (except through
        the iterator's own `remove` operation), the results of
        the iteration are undefined.  The set supports element removal,
        which removes the corresponding mapping from the map, via the
        `Iterator.remove`, `Set.remove`,
        `removeAll`, `retainAll`, and `clear`
        operations.  It does not support the `add` or `addAll`
        operations.

        Returns
        - a set view of the keys contained in this map, sorted in
                ascending order
        """
        ...


    def values(self) -> Iterable["V"]:
        """
        Returns a Collection view of the values contained in this map.
        The collection's iterator returns the values in ascending order
        of the corresponding keys.
        The collection is backed by the map, so changes to the map are
        reflected in the collection, and vice-versa.  If the map is
        modified while an iteration over the collection is in progress
        (except through the iterator's own `remove` operation),
        the results of the iteration are undefined.  The collection
        supports element removal, which removes the corresponding
        mapping from the map, via the `Iterator.remove`,
        `Collection.remove`, `removeAll`,
        `retainAll` and `clear` operations.  It does not
        support the `add` or `addAll` operations.

        Returns
        - a collection view of the values contained in this map,
                sorted in ascending key order
        """
        ...


    def entrySet(self) -> set["Map.Entry"["K", "V"]]:
        """
        Returns a Set view of the mappings contained in this map.
        The set's iterator returns the entries in ascending key order.
        The set is backed by the map, so changes to the map are
        reflected in the set, and vice-versa.  If the map is modified
        while an iteration over the set is in progress (except through
        the iterator's own `remove` operation, or through the
        `setValue` operation on a map entry returned by the
        iterator) the results of the iteration are undefined.  The set
        supports element removal, which removes the corresponding
        mapping from the map, via the `Iterator.remove`,
        `Set.remove`, `removeAll`, `retainAll` and
        `clear` operations.  It does not support the
        `add` or `addAll` operations.

        Returns
        - a set view of the mappings contained in this map,
                sorted in ascending key order
        """
        ...
