"""
Python module generated from Java source file com.google.common.collect.ListMultimap

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.collect import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from javax.annotation import Nullable
from typing import Any, Callable, Iterable, Tuple


class ListMultimap(Multimap):
    """
    A `Multimap` that can hold duplicate key-value pairs and that maintains
    the insertion ordering of values for a given key. See the Multimap
    documentation for information common to all multimaps.
    
    The .get, .removeAll, and .replaceValues methods
    each return a List of values. Though the method signature doesn't say
    so explicitly, the map returned by .asMap has `List` values.
    
    See the Guava User Guide article on <a href=
    "https://github.com/google/guava/wiki/NewCollectionTypesExplained#multimap">
    `Multimap`</a>.

    Author(s)
    - Jared Levy

    Since
    - 2.0
    """

    def get(self, key: "K") -> list["V"]:
        """
        
        
        Because the values for a given key may have duplicates and follow the
        insertion ordering, this method returns a List, instead of the
        java.util.Collection specified in the Multimap interface.
        """
        ...


    def removeAll(self, key: "Object") -> list["V"]:
        """
        
        
        Because the values for a given key may have duplicates and follow the
        insertion ordering, this method returns a List, instead of the
        java.util.Collection specified in the Multimap interface.
        """
        ...


    def replaceValues(self, key: "K", values: Iterable["V"]) -> list["V"]:
        """
        
        
        Because the values for a given key may have duplicates and follow the
        insertion ordering, this method returns a List, instead of the
        java.util.Collection specified in the Multimap interface.
        """
        ...


    def asMap(self) -> dict["K", Iterable["V"]]:
        """
        
        
        **Note:** The returned map's values are guaranteed to be of type
        List. To obtain this map with the more specific generic type
        `Map<K, List<V>>`, call Multimaps.asMap(ListMultimap)
        instead.
        """
        ...


    def equals(self, obj: "Object") -> bool:
        """
        Compares the specified object to this multimap for equality.
        
        Two `ListMultimap` instances are equal if, for each key, they
        contain the same values in the same order. If the value orderings disagree,
        the multimaps will not be considered equal.
        
        An empty `ListMultimap` is equal to any other empty `Multimap`, including an empty `SetMultimap`.
        """
        ...
