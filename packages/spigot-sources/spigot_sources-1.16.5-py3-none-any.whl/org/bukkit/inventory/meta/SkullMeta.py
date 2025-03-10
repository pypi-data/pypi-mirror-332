"""
Python module generated from Java source file org.bukkit.inventory.meta.SkullMeta

Java source file obtained from artifact spigot-api version 1.16.5-R0.1-20210611.041013-99

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import OfflinePlayer
from org.bukkit.inventory.meta import *
from typing import Any, Callable, Iterable, Tuple


class SkullMeta(ItemMeta):
    """
    Represents a skull that can have an owner.
    """

    def getOwner(self) -> str:
        """
        Gets the owner of the skull.

        Returns
        - the owner if the skull

        Deprecated
        - see .getOwningPlayer().
        """
        ...


    def hasOwner(self) -> bool:
        """
        Checks to see if the skull has an owner.

        Returns
        - True if the skull has an owner
        """
        ...


    def setOwner(self, owner: str) -> bool:
        """
        Sets the owner of the skull.

        Arguments
        - owner: the new owner of the skull

        Returns
        - True if the owner was successfully set

        Deprecated
        - see .setOwningPlayer(org.bukkit.OfflinePlayer).
        """
        ...


    def getOwningPlayer(self) -> "OfflinePlayer":
        """
        Gets the owner of the skull.

        Returns
        - the owner if the skull
        """
        ...


    def setOwningPlayer(self, owner: "OfflinePlayer") -> bool:
        """
        Sets the owner of the skull.
        
        Plugins should check that hasOwner() returns True before calling this
        plugin.

        Arguments
        - owner: the new owner of the skull

        Returns
        - True if the owner was successfully set
        """
        ...


    def clone(self) -> "SkullMeta":
        ...
