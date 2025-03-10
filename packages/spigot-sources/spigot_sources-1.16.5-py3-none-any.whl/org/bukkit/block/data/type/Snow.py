"""
Python module generated from Java source file org.bukkit.block.data.type.Snow

Java source file obtained from artifact spigot-api version 1.16.5-R0.1-20210611.041013-99

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block.data import BlockData
from org.bukkit.block.data.type import *
from typing import Any, Callable, Iterable, Tuple


class Snow(BlockData):
    """
    'layers' represents the amount of layers of snow which are present in this
    block.
    
    May not be lower than .getMinimumLayers() or higher than
    .getMaximumLayers().
    """

    def getLayers(self) -> int:
        """
        Gets the value of the 'layers' property.

        Returns
        - the 'layers' value
        """
        ...


    def setLayers(self, layers: int) -> None:
        """
        Sets the value of the 'layers' property.

        Arguments
        - layers: the new 'layers' value
        """
        ...


    def getMinimumLayers(self) -> int:
        """
        Gets the minimum allowed value of the 'layers' property.

        Returns
        - the minimum 'layers' value
        """
        ...


    def getMaximumLayers(self) -> int:
        """
        Gets the maximum allowed value of the 'layers' property.

        Returns
        - the maximum 'layers' value
        """
        ...
