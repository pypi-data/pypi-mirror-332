"""
Python module generated from Java source file com.google.common.collect.SortedSetMultimap

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.collect import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from java.util import Comparator
from java.util import SortedSet
from javax.annotation import Nullable
from typing import Any, Callable, Iterable, Tuple


class SortedSetMultimap(SetMultimap):
    """
    A `SetMultimap` whose set of values for a given key are kept sorted;
    that is, they comprise a SortedSet. It cannot hold duplicate
    key-value pairs; adding a key-value pair that's already in the multimap has
    no effect. This interface does not specify the ordering of the multimap's
    keys. See the Multimap documentation for information common to all
    multimaps.
    
    The .get, .removeAll, and .replaceValues methods
    each return a SortedSet of values, while Multimap.entries()
    returns a Set of map entries. Though the method signature doesn't say
    so explicitly, the map returned by .asMap has `SortedSet`
    values.
    
    See the Guava User Guide article on <a href=
    "https://github.com/google/guava/wiki/NewCollectionTypesExplained#multimap">
    `Multimap`</a>.

    Author(s)
    - Jared Levy

    Since
    - 2.0
    """

    def get(self, key: "K") -> "SortedSet"["V"]:
        """
        Returns a collection view of all values associated with a key. If no
        mappings in the multimap have the provided key, an empty collection is
        returned.
        
        Changes to the returned collection will update the underlying multimap,
        and vice versa.
        
        Because a `SortedSetMultimap` has unique sorted values for a given
        key, this method returns a SortedSet, instead of the
        java.util.Collection specified in the Multimap interface.
        """
        ...


    def removeAll(self, key: "Object") -> "SortedSet"["V"]:
        """
        Removes all values associated with a given key.
        
        Because a `SortedSetMultimap` has unique sorted values for a given
        key, this method returns a SortedSet, instead of the
        java.util.Collection specified in the Multimap interface.
        """
        ...


    def replaceValues(self, key: "K", values: Iterable["V"]) -> "SortedSet"["V"]:
        """
        Stores a collection of values with the same key, replacing any existing
        values for that key.
        
        Because a `SortedSetMultimap` has unique sorted values for a given
        key, this method returns a SortedSet, instead of the
        java.util.Collection specified in the Multimap interface.
        
        Any duplicates in `values` will be stored in the multimap once.
        """
        ...


    def asMap(self) -> dict["K", Iterable["V"]]:
        """
        Returns a map view that associates each key with the corresponding values
        in the multimap. Changes to the returned map, such as element removal, will
        update the underlying multimap. The map does not support `setValue()`
        on its entries, `put`, or `putAll`.
        
        When passed a key that is present in the map, `asMap().get(Object)` has the same behavior as .get, returning a
        live collection. When passed a key that is not present, however, `asMap().get(Object)` returns `null` instead of an empty collection.
        
        **Note:** The returned map's values are guaranteed to be of type
        SortedSet. To obtain this map with the more specific generic type
        `Map<K, SortedSet<V>>`, call
        Multimaps.asMap(SortedSetMultimap) instead.
        """
        ...


    def valueComparator(self) -> "Comparator"["V"]:
        """
        Returns the comparator that orders the multimap values, with `null`
        indicating that natural ordering is used.
        """
        ...
