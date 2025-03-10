"""
Python module generated from Java source file org.bukkit.block.Skull

Java source file obtained from artifact spigot-api version 1.16.5-R0.1-20210611.041013-99

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Material
from org.bukkit import OfflinePlayer
from org.bukkit import SkullType
from org.bukkit.block import *
from org.bukkit.block.data import BlockData
from typing import Any, Callable, Iterable, Tuple


class Skull(TileState):
    """
    Represents a captured state of a skull block.
    """

    def hasOwner(self) -> bool:
        """
        Checks to see if the skull has an owner

        Returns
        - True if the skull has an owner
        """
        ...


    def getOwner(self) -> str:
        """
        Gets the owner of the skull, if one exists

        Returns
        - the owner of the skull or null if the skull does not have an owner

        Deprecated
        - See .getOwningPlayer().
        """
        ...


    def setOwner(self, name: str) -> bool:
        """
        Sets the owner of the skull
        
        Involves a potentially blocking web request to acquire the profile data for
        the provided name.

        Arguments
        - name: the new owner of the skull

        Returns
        - True if the owner was successfully set

        Deprecated
        - see .setOwningPlayer(org.bukkit.OfflinePlayer).
        """
        ...


    def getOwningPlayer(self) -> "OfflinePlayer":
        """
        Get the player which owns the skull. This player may appear as the
        texture depending on skull type.

        Returns
        - owning player
        """
        ...


    def setOwningPlayer(self, player: "OfflinePlayer") -> None:
        """
        Set the player which owns the skull. This player may appear as the
        texture depending on skull type.

        Arguments
        - player: the owning player
        """
        ...


    def getRotation(self) -> "BlockFace":
        """
        Gets the rotation of the skull in the world (or facing direction if this
        is a wall mounted skull).

        Returns
        - the rotation of the skull

        Deprecated
        - use BlockData
        """
        ...


    def setRotation(self, rotation: "BlockFace") -> None:
        """
        Sets the rotation of the skull in the world (or facing direction if this
        is a wall mounted skull).

        Arguments
        - rotation: the rotation of the skull

        Deprecated
        - use BlockData
        """
        ...


    def getSkullType(self) -> "SkullType":
        """
        Gets the type of skull

        Returns
        - the type of skull

        Deprecated
        - check Material instead
        """
        ...


    def setSkullType(self, skullType: "SkullType") -> None:
        """
        Sets the type of skull

        Arguments
        - skullType: the type of skull

        Deprecated
        - check Material instead
        """
        ...
