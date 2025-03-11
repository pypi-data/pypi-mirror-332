"""
Python module generated from Java source file org.bukkit.block.data.type.Farmland

Java source file obtained from artifact spigot-api version 1.21.3-R0.1-20241203.162251-46

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block.data import BlockData
from org.bukkit.block.data.type import *
from typing import Any, Callable, Iterable, Tuple


class Farmland(BlockData):
    """
    The 'moisture' level of farmland indicates how close it is to a water source
    (if any).
    
    A higher moisture level leads, to faster growth of crops on this block, but
    cannot be higher than .getMaximumMoisture().
    """

    def getMoisture(self) -> int:
        """
        Gets the value of the 'moisture' property.

        Returns
        - the 'moisture' value
        """
        ...


    def setMoisture(self, moisture: int) -> None:
        """
        Sets the value of the 'moisture' property.

        Arguments
        - moisture: the new 'moisture' value
        """
        ...


    def getMaximumMoisture(self) -> int:
        """
        Gets the maximum allowed value of the 'moisture' property.

        Returns
        - the maximum 'moisture' value
        """
        ...
