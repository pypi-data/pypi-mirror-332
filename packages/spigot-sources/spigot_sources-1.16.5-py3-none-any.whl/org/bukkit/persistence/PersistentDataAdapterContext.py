"""
Python module generated from Java source file org.bukkit.persistence.PersistentDataAdapterContext

Java source file obtained from artifact spigot-api version 1.16.5-R0.1-20210611.041013-99

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.persistence import *
from typing import Any, Callable, Iterable, Tuple


class PersistentDataAdapterContext:
    """
    This interface represents the context in which the PersistentDataType can
    serialize and deserialize the passed values.
    """

    def newPersistentDataContainer(self) -> "PersistentDataContainer":
        """
        Creates a new and empty meta container instance.

        Returns
        - the fresh container instance
        """
        ...
