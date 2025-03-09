"""
Python module generated from Java source file com.google.common.collect.AbstractSetMultimap

Java source file obtained from artifact guava version 32.1.2-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.collect import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from java.util import Collections
from javax.annotation import CheckForNull
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class AbstractSetMultimap(AbstractMapBasedMultimap, SetMultimap):
    """
    Basic implementation of the SetMultimap interface. It's a wrapper around AbstractMapBasedMultimap that converts the returned collections into `Sets`. The .createCollection method must return a `Set`.

    Author(s)
    - Jared Levy
    """

    def get(self, key: "K") -> set["V"]:
        """
        
        
        Because a `SetMultimap` has unique values for a given key, this method returns a
        Set, instead of the Collection specified in the Multimap interface.
        """
        ...


    def entries(self) -> set["Entry"["K", "V"]]:
        """
        
        
        Because a `SetMultimap` has unique values for a given key, this method returns a
        Set, instead of the Collection specified in the Multimap interface.
        """
        ...


    def removeAll(self, key: "Object") -> set["V"]:
        """
        
        
        Because a `SetMultimap` has unique values for a given key, this method returns a
        Set, instead of the Collection specified in the Multimap interface.
        """
        ...


    def replaceValues(self, key: "K", values: Iterable["V"]) -> set["V"]:
        """
        
        
        Because a `SetMultimap` has unique values for a given key, this method returns a
        Set, instead of the Collection specified in the Multimap interface.
        
        Any duplicates in `values` will be stored in the multimap once.
        """
        ...


    def asMap(self) -> dict["K", Iterable["V"]]:
        """
        
        
        Though the method signature doesn't say so explicitly, the returned map has Set
        values.
        """
        ...


    def put(self, key: "K", value: "V") -> bool:
        """
        Stores a key-value pair in the multimap.

        Arguments
        - key: key to store in the multimap
        - value: value to store in the multimap

        Returns
        - `True` if the method increased the size of the multimap, or `False` if the
            multimap already contained the key-value pair
        """
        ...


    def equals(self, object: "Object") -> bool:
        """
        Compares the specified object to this multimap for equality.
        
        Two `SetMultimap` instances are equal if, for each key, they contain the same values.
        Equality does not depend on the ordering of keys or values.
        """
        ...
