"""
Python module generated from Java source file org.bukkit.persistence.ListPersistentDataType

Java source file obtained from artifact spigot-api version 1.20.5-R0.1-20240429.101539-37

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.persistence import *
from typing import Any, Callable, Iterable, Tuple


class ListPersistentDataType(PersistentDataType):
    """
    The list persistent data represents a data type that is capable of storing a
    list of other data types in a PersistentDataContainer.
    
    Type `<P>`: the primitive type of the list element.
    
    Type `<C>`: the complex type of the list elements.
    """

    def elementType(self) -> "PersistentDataType"["P", "C"]:
        """
        Provides the persistent data type of the elements found in the list.

        Returns
        - the persistent data type.
        """
        ...
