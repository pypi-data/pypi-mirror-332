"""
Python module generated from Java source file org.bukkit.material.Hopper

Java source file obtained from artifact spigot-api version 1.20.2-R0.1-20231205.164257-71

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Material
from org.bukkit.block import BlockFace
from org.bukkit.material import *
from typing import Any, Callable, Iterable, Tuple


class Hopper(MaterialData, Directional, Redstone):
    """
    Represents a hopper in an active or deactivated state and facing in a
    specific direction.

    See
    - Material.HOPPER

    Deprecated
    - all usage of MaterialData is deprecated and subject to removal.
    Use org.bukkit.block.data.BlockData.
    """

    def __init__(self):
        """
        Constructs a hopper facing the default direction (down) and initially
        active.
        """
        ...


    def __init__(self, facingDirection: "BlockFace"):
        """
        Constructs a hopper facing the specified direction and initially active.

        Arguments
        - facingDirection: the direction the hopper is facing

        See
        - BlockFace
        """
        ...


    def __init__(self, facingDirection: "BlockFace", isActive: bool):
        """
        Constructs a hopper facing the specified direction and either active or
        not.

        Arguments
        - facingDirection: the direction the hopper is facing
        - isActive: True if the hopper is initially active, False if
        deactivated

        See
        - BlockFace
        """
        ...


    def __init__(self, type: "Material"):
        ...


    def __init__(self, type: "Material", data: int):
        """
        Arguments
        - type: the type
        - data: the raw data value

        Deprecated
        - Magic value
        """
        ...


    def setActive(self, isActive: bool) -> None:
        """
        Sets whether the hopper is active or not.

        Arguments
        - isActive: True if the hopper is active, False if deactivated as if
        powered by redstone
        """
        ...


    def isActive(self) -> bool:
        """
        Checks whether the hopper is active or not.

        Returns
        - True if the hopper is active, False if deactivated
        """
        ...


    def setFacingDirection(self, face: "BlockFace") -> None:
        """
        Sets the direction this hopper is facing

        Arguments
        - face: The direction to set this hopper to

        See
        - BlockFace
        """
        ...


    def getFacing(self) -> "BlockFace":
        """
        Gets the direction this hopper is facing

        Returns
        - The direction this hopper is facing

        See
        - BlockFace
        """
        ...


    def toString(self) -> str:
        ...


    def clone(self) -> "Hopper":
        ...


    def isPowered(self) -> bool:
        """
        Checks if the hopper is powered.

        Returns
        - True if the hopper is powered
        """
        ...
