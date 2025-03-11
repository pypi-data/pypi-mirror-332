"""
Python module generated from Java source file org.bukkit.block.Lockable

Java source file obtained from artifact spigot-api version 1.21.2-R0.1-20241023.084343-5

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block import *
from org.bukkit.inventory import ItemStack
from typing import Any, Callable, Iterable, Tuple


class Lockable:
    """
    Represents a block (usually a container) that may be locked. When a lock is
    active an item with a name corresponding to the key will be required to open
    this block.
    """

    def isLocked(self) -> bool:
        """
        Checks if the container has a valid (non empty) key.

        Returns
        - True if the key is valid.
        """
        ...


    def getLock(self) -> str:
        """
        Gets the key needed to access the container.

        Returns
        - the key needed.

        Deprecated
        - locks are not necessarily pure strings
        """
        ...


    def setLock(self, key: str) -> None:
        """
        Sets the key required to access this container. Set to null (or empty
        string) to remove key.

        Arguments
        - key: the key required to access the container.

        Deprecated
        - locks are not necessarily pure strings
        """
        ...


    def setLockItem(self, key: "ItemStack") -> None:
        """
        Sets the key required to access this container. All explicit
        modifications to the set key will be required to match on the opening
        key. Set to null to remove key.

        Arguments
        - key: the key required to access the container.
        """
        ...
