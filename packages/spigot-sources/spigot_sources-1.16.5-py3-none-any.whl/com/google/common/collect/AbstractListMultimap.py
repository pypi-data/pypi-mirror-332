"""
Python module generated from Java source file com.google.common.collect.AbstractListMultimap

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


class AbstractListMultimap(AbstractMapBasedMultimap, ListMultimap):
    """
    Basic implementation of the ListMultimap interface. It's a wrapper
    around AbstractMapBasedMultimap that converts the returned collections into
    `Lists`. The .createCollection method must return a `List`.

    Author(s)
    - Jared Levy

    Since
    - 2.0
    """

    def get(self, key: "K") -> list["V"]:
        """
        
        
        Because the values for a given key may have duplicates and follow the
        insertion ordering, this method returns a List, instead of the
        Collection specified in the Multimap interface.
        """
        ...


    def removeAll(self, key: "Object") -> list["V"]:
        """
        
        
        Because the values for a given key may have duplicates and follow the
        insertion ordering, this method returns a List, instead of the
        Collection specified in the Multimap interface.
        """
        ...


    def replaceValues(self, key: "K", values: Iterable["V"]) -> list["V"]:
        """
        
        
        Because the values for a given key may have duplicates and follow the
        insertion ordering, this method returns a List, instead of the
        Collection specified in the Multimap interface.
        """
        ...


    def put(self, key: "K", value: "V") -> bool:
        """
        Stores a key-value pair in the multimap.

        Arguments
        - key: key to store in the multimap
        - value: value to store in the multimap

        Returns
        - `True` always
        """
        ...


    def asMap(self) -> dict["K", Iterable["V"]]:
        """
        
        
        Though the method signature doesn't say so explicitly, the returned map
        has List values.
        """
        ...


    def equals(self, object: "Object") -> bool:
        """
        Compares the specified object to this multimap for equality.
        
        Two `ListMultimap` instances are equal if, for each key, they
        contain the same values in the same order. If the value orderings disagree,
        the multimaps will not be considered equal.
        """
        ...
