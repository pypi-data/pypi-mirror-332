"""
Python module generated from Java source file com.google.common.collect.SetMultimap

Java source file obtained from artifact guava version 31.0.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.collect import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from javax.annotation import CheckForNull
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class SetMultimap(Multimap):
    """
    A `Multimap` that cannot hold duplicate key-value pairs. Adding a key-value pair that's
    already in the multimap has no effect. See the Multimap documentation for information
    common to all multimaps.
    
    The .get, .removeAll, and .replaceValues methods each return a Set of values, while .entries returns a `Set` of map entries. Though the method
    signature doesn't say so explicitly, the map returned by .asMap has `Set` values.
    
    If the values corresponding to a single key should be ordered according to a java.util.Comparator (or the natural order), see the SortedSetMultimap subinterface.
    
    Since the value collections are sets, the behavior of a `SetMultimap` is not specified
    if key *or value* objects already present in the multimap change in a manner that affects
    `equals` comparisons. Use caution if mutable objects are used as keys or values in a `SetMultimap`.
    
    **Warning:** Do not modify either a key *or a value* of a `SetMultimap` in a way
    that affects its Object.equals behavior. Undefined behavior and bugs will result.
    
    See the Guava User Guide article on <a href=
    "https://github.com/google/guava/wiki/NewCollectionTypesExplained#multimap"> `Multimap`</a>.

    Author(s)
    - Jared Levy

    Since
    - 2.0
    """

    def get(self, key: "K") -> set["V"]:
        """
        
        
        Because a `SetMultimap` has unique values for a given key, this method returns a
        Set, instead of the java.util.Collection specified in the Multimap
        interface.
        """
        ...


    def removeAll(self, key: "Object") -> set["V"]:
        """
        
        
        Because a `SetMultimap` has unique values for a given key, this method returns a
        Set, instead of the java.util.Collection specified in the Multimap
        interface.
        """
        ...


    def replaceValues(self, key: "K", values: Iterable["V"]) -> set["V"]:
        """
        
        
        Because a `SetMultimap` has unique values for a given key, this method returns a
        Set, instead of the java.util.Collection specified in the Multimap
        interface.
        
        Any duplicates in `values` will be stored in the multimap once.
        """
        ...


    def entries(self) -> set["Entry"["K", "V"]]:
        """
        
        
        Because a `SetMultimap` has unique values for a given key, this method returns a
        Set, instead of the java.util.Collection specified in the Multimap
        interface.
        """
        ...


    def asMap(self) -> dict["K", Iterable["V"]]:
        """
        
        
        **Note:** The returned map's values are guaranteed to be of type Set. To obtain
        this map with the more specific generic type `Map<K, Set<V>>`, call Multimaps.asMap(SetMultimap) instead.
        """
        ...


    def equals(self, obj: "Object") -> bool:
        """
        Compares the specified object to this multimap for equality.
        
        Two `SetMultimap` instances are equal if, for each key, they contain the same values.
        Equality does not depend on the ordering of keys or values.
        
        An empty `SetMultimap` is equal to any other empty `Multimap`, including an
        empty `ListMultimap`.
        """
        ...
