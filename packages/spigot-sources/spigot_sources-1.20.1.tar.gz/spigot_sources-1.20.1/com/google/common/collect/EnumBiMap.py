"""
Python module generated from Java source file com.google.common.collect.EnumBiMap

Java source file obtained from artifact guava version 31.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.annotations import GwtIncompatible
from com.google.common.collect import *
from java.io import IOException
from java.io import ObjectInputStream
from java.io import ObjectOutputStream
from java.util import EnumMap
from typing import Any, Callable, Iterable, Tuple


class EnumBiMap(AbstractBiMap):
    """
    A `BiMap` backed by two `EnumMap` instances. Null keys and values are not permitted.
    An `EnumBiMap` and its inverse are both serializable.
    
    See the Guava User Guide article on <a href=
    "https://github.com/google/guava/wiki/NewCollectionTypesExplained#bimap">`BiMap`</a>.

    Author(s)
    - Mike Bostock

    Since
    - 2.0
    """

    @staticmethod
    def create(keyType: type["K"], valueType: type["V"]) -> "EnumBiMap"["K", "V"]:
        """
        Returns a new, empty `EnumBiMap` using the specified key and value types.

        Arguments
        - keyType: the key type
        - valueType: the value type
        """
        ...


    @staticmethod
    def create(map: dict["K", "V"]) -> "EnumBiMap"["K", "V"]:
        """
        Returns a new bimap with the same mappings as the specified map. If the specified map is an
        `EnumBiMap`, the new bimap has the same types as the provided map. Otherwise, the
        specified map must contain at least one mapping, in order to determine the key and value types.

        Arguments
        - map: the map whose mappings are to be placed in this map

        Raises
        - IllegalArgumentException: if map is not an `EnumBiMap` instance and contains no
            mappings
        """
        ...


    def keyType(self) -> type["K"]:
        """
        Returns the associated key type.
        """
        ...


    def valueType(self) -> type["V"]:
        """
        Returns the associated value type.
        """
        ...
