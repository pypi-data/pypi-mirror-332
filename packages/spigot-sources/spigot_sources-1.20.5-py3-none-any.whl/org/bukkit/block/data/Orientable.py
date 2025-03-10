"""
Python module generated from Java source file org.bukkit.block.data.Orientable

Java source file obtained from artifact spigot-api version 1.20.5-R0.1-20240429.101539-37

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Axis
from org.bukkit.block.data import *
from typing import Any, Callable, Iterable, Tuple


class Orientable(BlockData):
    """
    'axis' represents the axis along whilst this block is oriented.
    
    Some blocks such as the portal block may not be able to be placed in all
    orientations, use .getAxes() to retrieve all possible such
    orientations.
    """

    def getAxis(self) -> "Axis":
        """
        Gets the value of the 'axis' property.

        Returns
        - the 'axis' value
        """
        ...


    def setAxis(self, axis: "Axis") -> None:
        """
        Sets the value of the 'axis' property.

        Arguments
        - axis: the new 'axis' value
        """
        ...


    def getAxes(self) -> set["Axis"]:
        """
        Gets the axes which are applicable to this block.

        Returns
        - the allowed 'axis' values
        """
        ...
