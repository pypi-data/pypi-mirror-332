"""
Python module generated from Java source file com.google.common.collect.AbstractSortedSetMultimap

Java source file obtained from artifact guava version 32.1.2-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.collect import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from java.util import Collections
from java.util import NavigableSet
from java.util import SortedSet
from javax.annotation import CheckForNull
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class AbstractSortedSetMultimap(AbstractSetMultimap, SortedSetMultimap):
    """
    Basic implementation of the SortedSetMultimap interface. It's a wrapper around AbstractMapBasedMultimap that converts the returned collections into sorted sets. The .createCollection method must return a `SortedSet`.

    Author(s)
    - Jared Levy
    """

    def get(self, key: "K") -> "SortedSet"["V"]:
        """
        Returns a collection view of all values associated with a key. If no mappings in the multimap
        have the provided key, an empty collection is returned.
        
        Changes to the returned collection will update the underlying multimap, and vice versa.
        
        Because a `SortedSetMultimap` has unique sorted values for a given key, this method
        returns a SortedSet, instead of the Collection specified in the Multimap interface.
        """
        ...


    def removeAll(self, key: "Object") -> "SortedSet"["V"]:
        """
        Removes all values associated with a given key. The returned collection is immutable.
        
        Because a `SortedSetMultimap` has unique sorted values for a given key, this method
        returns a SortedSet, instead of the Collection specified in the Multimap interface.
        """
        ...


    def replaceValues(self, key: "K", values: Iterable["V"]) -> "SortedSet"["V"]:
        """
        Stores a collection of values with the same key, replacing any existing values for that key.
        The returned collection is immutable.
        
        Because a `SortedSetMultimap` has unique sorted values for a given key, this method
        returns a SortedSet, instead of the Collection specified in the Multimap interface.
        
        Any duplicates in `values` will be stored in the multimap once.
        """
        ...


    def asMap(self) -> dict["K", Iterable["V"]]:
        """
        Returns a map view that associates each key with the corresponding values in the multimap.
        Changes to the returned map, such as element removal, will update the underlying multimap. The
        map does not support `setValue` on its entries, `put`, or `putAll`.
        
        When passed a key that is present in the map, `asMap().get(Object)` has the same
        behavior as .get, returning a live collection. When passed a key that is not present,
        however, `asMap().get(Object)` returns `null` instead of an empty collection.
        
        Though the method signature doesn't say so explicitly, the returned map has SortedSet values.
        """
        ...


    def values(self) -> Iterable["V"]:
        """
        
        
        Consequently, the values do not follow their natural ordering or the ordering of the value
        comparator.
        """
        ...
