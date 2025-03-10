"""
Python module generated from Java source file java.util.NavigableMap

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util import *
from typing import Any, Callable, Iterable, Tuple


class NavigableMap(SortedMap):
    """
    A SortedMap extended with navigation methods returning the
    closest matches for given search targets. Methods
    .lowerEntry, .floorEntry, .ceilingEntry,
    and .higherEntry return `Map.Entry` objects
    associated with keys respectively less than, less than or equal,
    greater than or equal, and greater than a given key, returning
    `null` if there is no such key.  Similarly, methods
    .lowerKey, .floorKey, .ceilingKey, and
    .higherKey return only the associated keys. All of these
    methods are designed for locating, not traversing entries.
    
    A `NavigableMap` may be accessed and traversed in either
    ascending or descending key order.  The .descendingMap
    method returns a view of the map with the senses of all relational
    and directional methods inverted. The performance of ascending
    operations and views is likely to be faster than that of descending
    ones.  Methods
    .subMap(Object, boolean, Object, boolean) subMap(K, boolean, K, boolean),
    .headMap(Object, boolean) headMap(K, boolean), and
    .tailMap(Object, boolean) tailMap(K, boolean)
    differ from the like-named `SortedMap` methods in accepting
    additional arguments describing whether lower and upper bounds are
    inclusive versus exclusive.  Submaps of any `NavigableMap`
    must implement the `NavigableMap` interface.
    
    This interface additionally defines methods .firstEntry,
    .pollFirstEntry, .lastEntry, and
    .pollLastEntry that return and/or remove the least and
    greatest mappings, if any exist, else returning `null`.
    
    Implementations of entry-returning methods are expected to
    return `Map.Entry` pairs representing snapshots of mappings
    at the time they were produced, and thus generally do *not*
    support the optional `Entry.setValue` method. Note however
    that it is possible to change mappings in the associated map using
    method `put`.
    
    Methods
    .subMap(Object, Object) subMap(K, K),
    .headMap(Object) headMap(K), and
    .tailMap(Object) tailMap(K)
    are specified to return `SortedMap` to allow existing
    implementations of `SortedMap` to be compatibly retrofitted to
    implement `NavigableMap`, but extensions and implementations
    of this interface are encouraged to override these methods to return
    `NavigableMap`.  Similarly,
    .keySet() can be overridden to return NavigableSet.
    
    This interface is a member of the
    <a href="/java.base/java/util/package-summary.html#CollectionsFramework">
    Java Collections Framework</a>.
    
    Type `<K>`: the type of keys maintained by this map
    
    Type `<V>`: the type of mapped values

    Author(s)
    - Josh Bloch

    Since
    - 1.6
    """

    def lowerEntry(self, key: "K") -> "Map.Entry"["K", "V"]:
        """
        Returns a key-value mapping associated with the greatest key
        strictly less than the given key, or `null` if there is
        no such key.

        Arguments
        - key: the key

        Returns
        - an entry with the greatest key less than `key`,
                or `null` if there is no such key

        Raises
        - ClassCastException: if the specified key cannot be compared
                with the keys currently in the map
        - NullPointerException: if the specified key is null
                and this map does not permit null keys
        """
        ...


    def lowerKey(self, key: "K") -> "K":
        """
        Returns the greatest key strictly less than the given key, or
        `null` if there is no such key.

        Arguments
        - key: the key

        Returns
        - the greatest key less than `key`,
                or `null` if there is no such key

        Raises
        - ClassCastException: if the specified key cannot be compared
                with the keys currently in the map
        - NullPointerException: if the specified key is null
                and this map does not permit null keys
        """
        ...


    def floorEntry(self, key: "K") -> "Map.Entry"["K", "V"]:
        """
        Returns a key-value mapping associated with the greatest key
        less than or equal to the given key, or `null` if there
        is no such key.

        Arguments
        - key: the key

        Returns
        - an entry with the greatest key less than or equal to
                `key`, or `null` if there is no such key

        Raises
        - ClassCastException: if the specified key cannot be compared
                with the keys currently in the map
        - NullPointerException: if the specified key is null
                and this map does not permit null keys
        """
        ...


    def floorKey(self, key: "K") -> "K":
        """
        Returns the greatest key less than or equal to the given key,
        or `null` if there is no such key.

        Arguments
        - key: the key

        Returns
        - the greatest key less than or equal to `key`,
                or `null` if there is no such key

        Raises
        - ClassCastException: if the specified key cannot be compared
                with the keys currently in the map
        - NullPointerException: if the specified key is null
                and this map does not permit null keys
        """
        ...


    def ceilingEntry(self, key: "K") -> "Map.Entry"["K", "V"]:
        """
        Returns a key-value mapping associated with the least key
        greater than or equal to the given key, or `null` if
        there is no such key.

        Arguments
        - key: the key

        Returns
        - an entry with the least key greater than or equal to
                `key`, or `null` if there is no such key

        Raises
        - ClassCastException: if the specified key cannot be compared
                with the keys currently in the map
        - NullPointerException: if the specified key is null
                and this map does not permit null keys
        """
        ...


    def ceilingKey(self, key: "K") -> "K":
        """
        Returns the least key greater than or equal to the given key,
        or `null` if there is no such key.

        Arguments
        - key: the key

        Returns
        - the least key greater than or equal to `key`,
                or `null` if there is no such key

        Raises
        - ClassCastException: if the specified key cannot be compared
                with the keys currently in the map
        - NullPointerException: if the specified key is null
                and this map does not permit null keys
        """
        ...


    def higherEntry(self, key: "K") -> "Map.Entry"["K", "V"]:
        """
        Returns a key-value mapping associated with the least key
        strictly greater than the given key, or `null` if there
        is no such key.

        Arguments
        - key: the key

        Returns
        - an entry with the least key greater than `key`,
                or `null` if there is no such key

        Raises
        - ClassCastException: if the specified key cannot be compared
                with the keys currently in the map
        - NullPointerException: if the specified key is null
                and this map does not permit null keys
        """
        ...


    def higherKey(self, key: "K") -> "K":
        """
        Returns the least key strictly greater than the given key, or
        `null` if there is no such key.

        Arguments
        - key: the key

        Returns
        - the least key greater than `key`,
                or `null` if there is no such key

        Raises
        - ClassCastException: if the specified key cannot be compared
                with the keys currently in the map
        - NullPointerException: if the specified key is null
                and this map does not permit null keys
        """
        ...


    def firstEntry(self) -> "Map.Entry"["K", "V"]:
        """
        Returns a key-value mapping associated with the least
        key in this map, or `null` if the map is empty.

        Returns
        - an entry with the least key,
                or `null` if this map is empty
        """
        ...


    def lastEntry(self) -> "Map.Entry"["K", "V"]:
        """
        Returns a key-value mapping associated with the greatest
        key in this map, or `null` if the map is empty.

        Returns
        - an entry with the greatest key,
                or `null` if this map is empty
        """
        ...


    def pollFirstEntry(self) -> "Map.Entry"["K", "V"]:
        """
        Removes and returns a key-value mapping associated with
        the least key in this map, or `null` if the map is empty.

        Returns
        - the removed first entry of this map,
                or `null` if this map is empty
        """
        ...


    def pollLastEntry(self) -> "Map.Entry"["K", "V"]:
        """
        Removes and returns a key-value mapping associated with
        the greatest key in this map, or `null` if the map is empty.

        Returns
        - the removed last entry of this map,
                or `null` if this map is empty
        """
        ...


    def descendingMap(self) -> "NavigableMap"["K", "V"]:
        """
        Returns a reverse order view of the mappings contained in this map.
        The descending map is backed by this map, so changes to the map are
        reflected in the descending map, and vice-versa.  If either map is
        modified while an iteration over a collection view of either map
        is in progress (except through the iterator's own `remove`
        operation), the results of the iteration are undefined.
        
        The returned map has an ordering equivalent to
        Collections.reverseOrder(Comparator) Collections.reverseOrder`(comparator())`.
        The expression `m.descendingMap().descendingMap()` returns a
        view of `m` essentially equivalent to `m`.

        Returns
        - a reverse order view of this map
        """
        ...


    def navigableKeySet(self) -> "NavigableSet"["K"]:
        """
        Returns a NavigableSet view of the keys contained in this map.
        The set's iterator returns the keys in ascending order.
        The set is backed by the map, so changes to the map are reflected in
        the set, and vice-versa.  If the map is modified while an iteration
        over the set is in progress (except through the iterator's own `remove` operation), the results of the iteration are undefined.  The
        set supports element removal, which removes the corresponding mapping
        from the map, via the `Iterator.remove`, `Set.remove`,
        `removeAll`, `retainAll`, and `clear` operations.
        It does not support the `add` or `addAll` operations.

        Returns
        - a navigable set view of the keys in this map
        """
        ...


    def descendingKeySet(self) -> "NavigableSet"["K"]:
        """
        Returns a reverse order NavigableSet view of the keys contained in this map.
        The set's iterator returns the keys in descending order.
        The set is backed by the map, so changes to the map are reflected in
        the set, and vice-versa.  If the map is modified while an iteration
        over the set is in progress (except through the iterator's own `remove` operation), the results of the iteration are undefined.  The
        set supports element removal, which removes the corresponding mapping
        from the map, via the `Iterator.remove`, `Set.remove`,
        `removeAll`, `retainAll`, and `clear` operations.
        It does not support the `add` or `addAll` operations.

        Returns
        - a reverse order navigable set view of the keys in this map
        """
        ...


    def subMap(self, fromKey: "K", fromInclusive: bool, toKey: "K", toInclusive: bool) -> "NavigableMap"["K", "V"]:
        """
        Returns a view of the portion of this map whose keys range from
        `fromKey` to `toKey`.  If `fromKey` and
        `toKey` are equal, the returned map is empty unless
        `fromInclusive` and `toInclusive` are both True.  The
        returned map is backed by this map, so changes in the returned map are
        reflected in this map, and vice-versa.  The returned map supports all
        optional map operations that this map supports.
        
        The returned map will throw an `IllegalArgumentException`
        on an attempt to insert a key outside of its range, or to construct a
        submap either of whose endpoints lie outside its range.

        Arguments
        - fromKey: low endpoint of the keys in the returned map
        - fromInclusive: `True` if the low endpoint
               is to be included in the returned view
        - toKey: high endpoint of the keys in the returned map
        - toInclusive: `True` if the high endpoint
               is to be included in the returned view

        Returns
        - a view of the portion of this map whose keys range from
                `fromKey` to `toKey`

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


    def headMap(self, toKey: "K", inclusive: bool) -> "NavigableMap"["K", "V"]:
        """
        Returns a view of the portion of this map whose keys are less than (or
        equal to, if `inclusive` is True) `toKey`.  The returned
        map is backed by this map, so changes in the returned map are reflected
        in this map, and vice-versa.  The returned map supports all optional
        map operations that this map supports.
        
        The returned map will throw an `IllegalArgumentException`
        on an attempt to insert a key outside its range.

        Arguments
        - toKey: high endpoint of the keys in the returned map
        - inclusive: `True` if the high endpoint
               is to be included in the returned view

        Returns
        - a view of the portion of this map whose keys are less than
                (or equal to, if `inclusive` is True) `toKey`

        Raises
        - ClassCastException: if `toKey` is not compatible
                with this map's comparator (or, if the map has no comparator,
                if `toKey` does not implement Comparable).
                Implementations may, but are not required to, throw this
                exception if `toKey` cannot be compared to keys
                currently in the map.
        - NullPointerException: if `toKey` is null
                and this map does not permit null keys
        - IllegalArgumentException: if this map itself has a
                restricted range, and `toKey` lies outside the
                bounds of the range
        """
        ...


    def tailMap(self, fromKey: "K", inclusive: bool) -> "NavigableMap"["K", "V"]:
        """
        Returns a view of the portion of this map whose keys are greater than (or
        equal to, if `inclusive` is True) `fromKey`.  The returned
        map is backed by this map, so changes in the returned map are reflected
        in this map, and vice-versa.  The returned map supports all optional
        map operations that this map supports.
        
        The returned map will throw an `IllegalArgumentException`
        on an attempt to insert a key outside its range.

        Arguments
        - fromKey: low endpoint of the keys in the returned map
        - inclusive: `True` if the low endpoint
               is to be included in the returned view

        Returns
        - a view of the portion of this map whose keys are greater than
                (or equal to, if `inclusive` is True) `fromKey`

        Raises
        - ClassCastException: if `fromKey` is not compatible
                with this map's comparator (or, if the map has no comparator,
                if `fromKey` does not implement Comparable).
                Implementations may, but are not required to, throw this
                exception if `fromKey` cannot be compared to keys
                currently in the map.
        - NullPointerException: if `fromKey` is null
                and this map does not permit null keys
        - IllegalArgumentException: if this map itself has a
                restricted range, and `fromKey` lies outside the
                bounds of the range
        """
        ...


    def subMap(self, fromKey: "K", toKey: "K") -> "SortedMap"["K", "V"]:
        """
        
        
        Equivalent to `subMap(fromKey, True, toKey, False)`.

        Raises
        - ClassCastException: 
        - NullPointerException: 
        - IllegalArgumentException: 
        """
        ...


    def headMap(self, toKey: "K") -> "SortedMap"["K", "V"]:
        """
        
        
        Equivalent to `headMap(toKey, False)`.

        Raises
        - ClassCastException: 
        - NullPointerException: 
        - IllegalArgumentException: 
        """
        ...


    def tailMap(self, fromKey: "K") -> "SortedMap"["K", "V"]:
        """
        
        
        Equivalent to `tailMap(fromKey, True)`.

        Raises
        - ClassCastException: 
        - NullPointerException: 
        - IllegalArgumentException: 
        """
        ...
