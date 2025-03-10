"""
Python module generated from Java source file java.util.concurrent.ConcurrentNavigableMap

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util import NavigableMap
from java.util import NavigableSet
from java.util.concurrent import *
from typing import Any, Callable, Iterable, Tuple


class ConcurrentNavigableMap(ConcurrentMap, NavigableMap):
    """
    A ConcurrentMap supporting NavigableMap operations,
    and recursively so for its navigable sub-maps.
    
    This interface is a member of the
    <a href="/java.base/java/util/package-summary.html#CollectionsFramework">
    Java Collections Framework</a>.
    
    Type `<K>`: the type of keys maintained by this map
    
    Type `<V>`: the type of mapped values

    Author(s)
    - Doug Lea

    Since
    - 1.6
    """

    def subMap(self, fromKey: "K", fromInclusive: bool, toKey: "K", toInclusive: bool) -> "ConcurrentNavigableMap"["K", "V"]:
        """
        Raises
        - ClassCastException: 
        - NullPointerException: 
        - IllegalArgumentException: 
        """
        ...


    def headMap(self, toKey: "K", inclusive: bool) -> "ConcurrentNavigableMap"["K", "V"]:
        """
        Raises
        - ClassCastException: 
        - NullPointerException: 
        - IllegalArgumentException: 
        """
        ...


    def tailMap(self, fromKey: "K", inclusive: bool) -> "ConcurrentNavigableMap"["K", "V"]:
        """
        Raises
        - ClassCastException: 
        - NullPointerException: 
        - IllegalArgumentException: 
        """
        ...


    def subMap(self, fromKey: "K", toKey: "K") -> "ConcurrentNavigableMap"["K", "V"]:
        """
        Raises
        - ClassCastException: 
        - NullPointerException: 
        - IllegalArgumentException: 
        """
        ...


    def headMap(self, toKey: "K") -> "ConcurrentNavigableMap"["K", "V"]:
        """
        Raises
        - ClassCastException: 
        - NullPointerException: 
        - IllegalArgumentException: 
        """
        ...


    def tailMap(self, fromKey: "K") -> "ConcurrentNavigableMap"["K", "V"]:
        """
        Raises
        - ClassCastException: 
        - NullPointerException: 
        - IllegalArgumentException: 
        """
        ...


    def descendingMap(self) -> "ConcurrentNavigableMap"["K", "V"]:
        """
        Returns a reverse order view of the mappings contained in this map.
        The descending map is backed by this map, so changes to the map are
        reflected in the descending map, and vice-versa.
        
        The returned map has an ordering equivalent to
        java.util.Collections.reverseOrder(Comparator) Collections.reverseOrder`(comparator())`.
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
        The set is backed by the map, so changes to the map are
        reflected in the set, and vice-versa.  The set supports element
        removal, which removes the corresponding mapping from the map,
        via the `Iterator.remove`, `Set.remove`,
        `removeAll`, `retainAll`, and `clear`
        operations.  It does not support the `add` or `addAll`
        operations.
        
        The view's iterators and spliterators are
        <a href="package-summary.html#Weakly">*weakly consistent*</a>.

        Returns
        - a navigable set view of the keys in this map
        """
        ...


    def keySet(self) -> "NavigableSet"["K"]:
        """
        Returns a NavigableSet view of the keys contained in this map.
        The set's iterator returns the keys in ascending order.
        The set is backed by the map, so changes to the map are
        reflected in the set, and vice-versa.  The set supports element
        removal, which removes the corresponding mapping from the map,
        via the `Iterator.remove`, `Set.remove`,
        `removeAll`, `retainAll`, and `clear`
        operations.  It does not support the `add` or `addAll`
        operations.
        
        The view's iterators and spliterators are
        <a href="package-summary.html#Weakly">*weakly consistent*</a>.
        
        This method is equivalent to method `navigableKeySet`.

        Returns
        - a navigable set view of the keys in this map
        """
        ...


    def descendingKeySet(self) -> "NavigableSet"["K"]:
        """
        Returns a reverse order NavigableSet view of the keys contained in this map.
        The set's iterator returns the keys in descending order.
        The set is backed by the map, so changes to the map are
        reflected in the set, and vice-versa.  The set supports element
        removal, which removes the corresponding mapping from the map,
        via the `Iterator.remove`, `Set.remove`,
        `removeAll`, `retainAll`, and `clear`
        operations.  It does not support the `add` or `addAll`
        operations.
        
        The view's iterators and spliterators are
        <a href="package-summary.html#Weakly">*weakly consistent*</a>.

        Returns
        - a reverse order navigable set view of the keys in this map
        """
        ...
