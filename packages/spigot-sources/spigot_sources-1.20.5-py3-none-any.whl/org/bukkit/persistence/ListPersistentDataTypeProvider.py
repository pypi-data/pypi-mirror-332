"""
Python module generated from Java source file org.bukkit.persistence.ListPersistentDataTypeProvider

Java source file obtained from artifact spigot-api version 1.20.5-R0.1-20240429.101539-37

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.collect import Collections2
from com.google.common.collect import Lists
from org.bukkit.persistence import *
from typing import Any, Callable, Iterable, Tuple


class ListPersistentDataTypeProvider:
    """
    A provider for list persistent data types that represent the known primitive
    types exposed by PersistentDataType.
    """

    def bytes(self) -> "ListPersistentDataType"["Byte", "Byte"]:
        """
        Provides a shared ListPersistentDataType that is capable of
        storing lists of bytes.

        Returns
        - the persistent data type.
        """
        ...


    def shorts(self) -> "ListPersistentDataType"["Short", "Short"]:
        """
        Provides a shared ListPersistentDataType that is capable of
        storing lists of shorts.

        Returns
        - the persistent data type.
        """
        ...


    def integers(self) -> "ListPersistentDataType"["Integer", "Integer"]:
        """
        Provides a shared ListPersistentDataType that is capable of
        storing lists of integers.

        Returns
        - the persistent data type.
        """
        ...


    def longs(self) -> "ListPersistentDataType"["Long", "Long"]:
        """
        Provides a shared ListPersistentDataType that is capable of
        storing lists of longs.

        Returns
        - the persistent data type.
        """
        ...


    def floats(self) -> "ListPersistentDataType"["Float", "Float"]:
        """
        Provides a shared ListPersistentDataType that is capable of
        storing lists of floats.

        Returns
        - the persistent data type.
        """
        ...


    def doubles(self) -> "ListPersistentDataType"["Double", "Double"]:
        """
        Provides a shared ListPersistentDataType that is capable of
        storing lists of doubles.

        Returns
        - the persistent data type.
        """
        ...


    def booleans(self) -> "ListPersistentDataType"["Byte", "Boolean"]:
        """
        Provides a shared ListPersistentDataType that is capable of
        storing lists of booleans.

        Returns
        - the persistent data type.
        """
        ...


    def strings(self) -> "ListPersistentDataType"[str, str]:
        """
        Provides a shared ListPersistentDataType that is capable of
        storing lists of strings.

        Returns
        - the persistent data type.
        """
        ...


    def byteArrays(self) -> "ListPersistentDataType"[list[int], list[int]]:
        """
        Provides a shared ListPersistentDataType that is capable of
        storing lists of byte arrays.

        Returns
        - the persistent data type.
        """
        ...


    def integerArrays(self) -> "ListPersistentDataType"[list[int], list[int]]:
        """
        Provides a shared ListPersistentDataType that is capable of
        storing lists of int arrays.

        Returns
        - the persistent data type.
        """
        ...


    def longArrays(self) -> "ListPersistentDataType"[list[int], list[int]]:
        """
        Provides a shared ListPersistentDataType that is capable of
        storing lists of long arrays.

        Returns
        - the persistent data type.
        """
        ...


    def dataContainers(self) -> "ListPersistentDataType"["PersistentDataContainer", "PersistentDataContainer"]:
        """
        Provides a shared ListPersistentDataType that is capable of
        persistent data containers..

        Returns
        - the persistent data type.
        """
        ...


    def listTypeFrom(self, elementType: "PersistentDataType"["P", "C"]) -> "ListPersistentDataType"["P", "C"]:
        """
        Constructs a new list persistent data type given any persistent data type
        for its elements.
        
        Type `<P>`: the generic type of the primitives stored in the list.
        
        Type `<C>`: the generic type of the complex values yielded back by the
        persistent data types.

        Arguments
        - elementType: the persistent data type that is capable of
        writing/reading the elements of the list.

        Returns
        - the created list persistent data type.
        """
        ...
