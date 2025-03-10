"""
Python module generated from Java source file org.bukkit.block.data.Directional

Java source file obtained from artifact spigot-api version 1.18.2-R0.1-20220607.160742-53

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block import BlockFace
from org.bukkit.block.data import *
from typing import Any, Callable, Iterable, Tuple


class Directional(BlockData):
    """
    'facing' represents the face towards which the block is pointing.
    
    Some blocks may not be able to face in all directions, use
    .getFaces() to get all possible directions for this block.
    """

    def getFacing(self) -> "BlockFace":
        """
        Gets the value of the 'facing' property.

        Returns
        - the 'facing' value
        """
        ...


    def setFacing(self, facing: "BlockFace") -> None:
        """
        Sets the value of the 'facing' property.

        Arguments
        - facing: the new 'facing' value
        """
        ...


    def getFaces(self) -> set["BlockFace"]:
        """
        Gets the faces which are applicable to this block.

        Returns
        - the allowed 'facing' values
        """
        ...
