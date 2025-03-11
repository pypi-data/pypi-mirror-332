"""
Python module generated from Java source file org.bukkit.inventory.meta.tags.ItemTagAdapterContext

Java source file obtained from artifact spigot-api version 1.21.1-R0.1-20241022.152140-54

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.inventory.meta.tags import *
from org.bukkit.persistence import PersistentDataAdapterContext
from org.bukkit.persistence import PersistentDataHolder
from typing import Any, Callable, Iterable, Tuple


class ItemTagAdapterContext:
    """
    This interface represents the context in which the ItemTagType can
    serialize and deserialize the passed values.

    Deprecated
    - this API part has been replaced by PersistentDataHolder.
    Please use PersistentDataAdapterContext instead of this.
    """

    def newTagContainer(self) -> "CustomItemTagContainer":
        """
        Creates a new and empty tag container instance.

        Returns
        - the fresh container instance
        """
        ...
