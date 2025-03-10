"""
Python module generated from Java source file org.bukkit.block.data.type.StructureBlock

Java source file obtained from artifact spigot-api version 1.20-R0.1-20230612.113428-32

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit.block.data import BlockData
from org.bukkit.block.data.type import *
from typing import Any, Callable, Iterable, Tuple


class StructureBlock(BlockData):
    """
    'mode' represents the different modes in which this structure block may
    operate.
    """

    def getMode(self) -> "Mode":
        """
        Gets the value of the 'mode' property.

        Returns
        - the 'mode' value
        """
        ...


    def setMode(self, mode: "Mode") -> None:
        """
        Sets the value of the 'mode' property.

        Arguments
        - mode: the new 'mode' value
        """
        ...


    class Mode(Enum):
        """
        Operating mode of a structure block.
        """

        SAVE = 0
        """
        Allows selection and saving of a structure.
        """
        LOAD = 1
        """
        Allows loading of a structure.
        """
        CORNER = 2
        """
        Used for detection of two opposite corners of a structure.
        """
        DATA = 3
        """
        Dummy block used to run a custom function during world generation
        before being removed.
        """
