"""
Python module generated from Java source file org.bukkit.block.data.MultipleFacing

Java source file obtained from artifact spigot-api version 1.20.4-R0.1-20240423.152506-123

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block import BlockFace
from org.bukkit.block.data import *
from typing import Any, Callable, Iterable, Tuple


class MultipleFacing(BlockData):
    """
    This class encompasses the 'north', 'east', 'south', 'west', 'up', 'down'
    boolean flags which are used to set which faces of the block textures are
    displayed on.
    
    Some blocks may not be able to have faces on all directions, use
    .getAllowedFaces() to get all possible faces for this block. It is
    not valid to call any methods on non-allowed faces.
    """

    def hasFace(self, face: "BlockFace") -> bool:
        """
        Checks if this block has the specified face enabled.

        Arguments
        - face: to check

        Returns
        - if face is enabled
        """
        ...


    def setFace(self, face: "BlockFace", has: bool) -> None:
        """
        Set whether this block has the specified face enabled.

        Arguments
        - face: to set
        - has: the face
        """
        ...


    def getFaces(self) -> set["BlockFace"]:
        """
        Get all of the faces which are enabled on this block.

        Returns
        - all faces enabled
        """
        ...


    def getAllowedFaces(self) -> set["BlockFace"]:
        """
        Gets all of this faces which may be set on this block.

        Returns
        - all allowed faces
        """
        ...
