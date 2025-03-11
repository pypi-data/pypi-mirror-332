"""
Python module generated from Java source file org.bukkit.material.Mushroom

Java source file obtained from artifact spigot-api version 1.21.3-R0.1-20241203.162251-46

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.base import Preconditions
from java.util import EnumSet
from org.bukkit import Material
from org.bukkit.block import BlockFace
from org.bukkit.material import *
from org.bukkit.material.types import MushroomBlockTexture
from typing import Any, Callable, Iterable, Tuple


class Mushroom(MaterialData):
    """
    Represents a huge mushroom block with certain combinations of faces set to
    cap, pores or stem.

    See
    - Material.LEGACY_HUGE_MUSHROOM_2

    Deprecated
    - all usage of MaterialData is deprecated and subject to removal.
    Use org.bukkit.block.data.BlockData.
    """

    def __init__(self, shroom: "Material"):
        """
        Constructs a brown/red mushroom block with all sides set to pores.

        Arguments
        - shroom: A brown or red mushroom material type.

        See
        - Material.LEGACY_HUGE_MUSHROOM_2
        """
        ...


    def __init__(self, shroom: "Material", capFace: "BlockFace"):
        """
        Constructs a brown/red mushroom cap block with the specified face or
        faces set to cap texture.
        
        Setting any of the four sides will also set the top to cap.
        
        To set two side faces at once use e.g. north-west.
        
        Specify self to set all six faces at once.

        Arguments
        - shroom: A brown or red mushroom material type.
        - capFace: The face or faces to set to mushroom cap texture.

        See
        - BlockFace
        """
        ...


    def __init__(self, shroom: "Material", texture: "MushroomBlockTexture"):
        """
        Constructs a brown/red mushroom block with the specified textures.

        Arguments
        - shroom: A brown or red mushroom material type.
        - texture: The textured mushroom faces.

        See
        - Material.LEGACY_HUGE_MUSHROOM_2
        """
        ...


    def __init__(self, shroom: "Material", data: int):
        """
        Arguments
        - shroom: the type
        - data: the raw data value

        Deprecated
        - Magic value
        """
        ...


    def isStem(self) -> bool:
        """
        Returns
        - Whether this is a mushroom stem.
        """
        ...


    def setStem(self) -> None:
        """
        Sets this to be a mushroom stem.

        See
        - MushroomBlockTexture.ALL_STEM

        Deprecated
        - Use
        .setBlockTexture(org.bukkit.material.types.MushroomBlockTexture)
        with MushroomBlockTexture.STEM_SIDES or
        MushroomBlockTexture.ALL_STEM
        """
        ...


    def getBlockTexture(self) -> "MushroomBlockTexture":
        """
        Gets the mushroom texture of this block.

        Returns
        - The mushroom texture of this block
        """
        ...


    def setBlockTexture(self, texture: "MushroomBlockTexture") -> None:
        """
        Sets the mushroom texture of this block.

        Arguments
        - texture: The mushroom texture to set
        """
        ...


    def isFacePainted(self, face: "BlockFace") -> bool:
        """
        Checks whether a face of the block is painted with cap texture.

        Arguments
        - face: The face to check.

        Returns
        - True if it is painted.
        """
        ...


    def setFacePainted(self, face: "BlockFace", painted: bool) -> None:
        """
        Set a face of the block to be painted or not. Note that due to the
        nature of how the data is stored, setting a face painted or not is not
        guaranteed to leave the other faces unchanged.

        Arguments
        - face: The face to paint or unpaint.
        - painted: True if you want to paint it, False if you want the
            pores to show.

        Deprecated
        - Use MushroomBlockType cap options
        """
        ...


    def getPaintedFaces(self) -> set["BlockFace"]:
        """
        Returns
        - A set of all faces that are currently painted (an empty set if
            it is a stem)
        """
        ...


    def toString(self) -> str:
        ...


    def clone(self) -> "Mushroom":
        ...
