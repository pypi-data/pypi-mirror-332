"""
Python module generated from Java source file org.bukkit.material.Door

Java source file obtained from artifact spigot-api version 1.20.1-R0.1-20230921.163938-66

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Material
from org.bukkit import TreeSpecies
from org.bukkit.block import BlockFace
from org.bukkit.material import *
from typing import Any, Callable, Iterable, Tuple


class Door(MaterialData, Directional, Openable):
    """
    Represents a door.
    
    This class was previously deprecated, but has been retrofitted to
    work with modern doors. Some methods are undefined dependant on `isTopHalf()`
    due to Minecraft's internal representation of doors.

    See
    - Material.LEGACY_DARK_OAK_DOOR

    Deprecated
    - all usage of MaterialData is deprecated and subject to removal.
    Use org.bukkit.block.data.BlockData.
    """

    def __init__(self):
        """
        Deprecated
        - Artifact of old API, equivalent to new `Door(Material.LEGACY_WOODEN_DOOR);`
        """
        ...


    def __init__(self, type: "Material"):
        ...


    def __init__(self, type: "Material", face: "BlockFace"):
        """
        Constructs the bottom half of a door of the given material type, facing the specified direction and set to closed

        Arguments
        - type: The type of material this door is made of. This must match the type of the block above.
        - face: The direction the door is facing.

        See
        - BlockFace.SOUTH
        """
        ...


    def __init__(self, type: "Material", face: "BlockFace", isOpen: bool):
        """
        Constructs the bottom half of a door of the given material type, facing the specified direction and set to open
        or closed

        Arguments
        - type: The type of material this door is made of. This must match the type of the block above.
        - face: The direction the door is facing.
        - isOpen: Whether the door is currently opened.

        See
        - BlockFace.SOUTH
        """
        ...


    def __init__(self, type: "Material", isHingeRight: bool):
        """
        Constructs the top half of door of the given material type and with the hinge on the left or right

        Arguments
        - type: The type of material this door is made of. This must match the type of the block below.
        - isHingeRight: True if the hinge is on the right hand side, False if the hinge is on the left hand side.

        See
        - Material.LEGACY_DARK_OAK_DOOR
        """
        ...


    def __init__(self, species: "TreeSpecies", face: "BlockFace"):
        """
        Constructs the bottom half of a wooden door of the given species, facing the specified direction and set to
        closed

        Arguments
        - species: The species this wooden door is made of. This must match the species of the block above.
        - face: The direction the door is facing.

        See
        - BlockFace.SOUTH
        """
        ...


    def __init__(self, species: "TreeSpecies", face: "BlockFace", isOpen: bool):
        """
        Constructs the bottom half of a wooden door of the given species, facing the specified direction and set to open
        or closed

        Arguments
        - species: The species this wooden door is made of. This must match the species of the block above.
        - face: The direction the door is facing.
        - isOpen: Whether the door is currently opened.

        See
        - BlockFace.SOUTH
        """
        ...


    def __init__(self, species: "TreeSpecies", isHingeRight: bool):
        """
        Constructs the top half of a wooden door of the given species and with the hinge on the left or right

        Arguments
        - species: The species this wooden door is made of. This must match the species of the block below.
        - isHingeRight: True if the hinge is on the right hand side, False if the hinge is on the left hand side.

        See
        - TreeSpecies
        """
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


    @staticmethod
    def getWoodDoorOfSpecies(species: "TreeSpecies") -> "Material":
        """
        Returns the item type of a wooden door for the given tree species.

        Arguments
        - species: The species of wood door required.

        Returns
        - The item type for the given species.

        See
        - Material.LEGACY_DARK_OAK_DOOR
        """
        ...


    def isOpen(self) -> bool:
        """
        Result is undefined if `isTopHalf()` is True.
        """
        ...


    def setOpen(self, isOpen: bool) -> None:
        """
        Set whether the door is open. Undefined if `isTopHalf()` is True.
        """
        ...


    def isTopHalf(self) -> bool:
        """
        Returns
        - whether this is the top half of the door
        """
        ...


    def setTopHalf(self, isTopHalf: bool) -> None:
        """
        Configure this part of the door to be either the top or the bottom half

        Arguments
        - isTopHalf: True to make it the top half.
        """
        ...


    def getHingeCorner(self) -> "BlockFace":
        """
        Returns
        - BlockFace.SELF

        Deprecated
        - This method should not be used; use hinge and facing accessors instead.
        """
        ...


    def toString(self) -> str:
        ...


    def setFacingDirection(self, face: "BlockFace") -> None:
        """
        Set the direction that this door should is facing.
        
        Undefined if `isTopHalf()` is True.

        Arguments
        - face: the direction
        """
        ...


    def getFacing(self) -> "BlockFace":
        """
        Get the direction that this door is facing.
        
        Undefined if `isTopHalf()` is True.

        Returns
        - the direction
        """
        ...


    def getHinge(self) -> bool:
        """
        Returns the side of the door the hinge is on.
        
        Undefined if `isTopHalf()` is False.

        Returns
        - False for left hinge, True for right hinge
        """
        ...


    def setHinge(self, isHingeRight: bool) -> None:
        """
        Set whether the hinge is on the left or right side. Left is False, right is True.
        
        Undefined if `isTopHalf()` is False.

        Arguments
        - isHingeRight: True if the hinge is on the right hand side, False if the hinge is on the left hand side.
        """
        ...


    def clone(self) -> "Door":
        ...
