"""
Python module generated from Java source file com.google.common.collect.EnumHashBiMap

Java source file obtained from artifact guava version 31.0.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.annotations import GwtIncompatible
from com.google.common.collect import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from java.io import IOException
from java.io import ObjectInputStream
from java.io import ObjectOutputStream
from java.util import EnumMap
from javax.annotation import CheckForNull
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class EnumHashBiMap(AbstractBiMap):
    """
    A `BiMap` backed by an `EnumMap` instance for keys-to-values, and a `HashMap`
    instance for values-to-keys. Null keys are not permitted, but null values are. An `EnumHashBiMap` and its inverse are both serializable.
    
    See the Guava User Guide article on <a href=
    "https://github.com/google/guava/wiki/NewCollectionTypesExplained#bimap"> `BiMap`</a>.

    Author(s)
    - Mike Bostock

    Since
    - 2.0
    """

    @staticmethod
    def create(keyType: type["K"]) -> "EnumHashBiMap"["K", "V"]:
        """
        Returns a new, empty `EnumHashBiMap` using the specified key type.

        Arguments
        - keyType: the key type
        """
        ...


    @staticmethod
    def create(map: dict["K", "V"]) -> "EnumHashBiMap"["K", "V"]:
        """
        Constructs a new bimap with the same mappings as the specified map. If the specified map is an
        `EnumHashBiMap` or an EnumBiMap, the new bimap has the same key type as the input
        bimap. Otherwise, the specified map must contain at least one mapping, in order to determine
        the key type.

        Arguments
        - map: the map whose mappings are to be placed in this map

        Raises
        - IllegalArgumentException: if map is not an `EnumBiMap` or an `EnumHashBiMap`
            instance and contains no mappings
        """
        ...


    def put(self, key: "K", value: "V") -> "V":
        ...


    def forcePut(self, key: "K", value: "V") -> "V":
        ...


    def keyType(self) -> type["K"]:
        """
        Returns the associated key type.
        """
        ...
