"""
Python module generated from Java source file org.bukkit.material.Cake

Java source file obtained from artifact spigot-api version 1.20.1-R0.1-20230921.163938-66

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Material
from org.bukkit.material import *
from typing import Any, Callable, Iterable, Tuple


class Cake(MaterialData):
    """
    Deprecated
    - all usage of MaterialData is deprecated and subject to removal.
    Use org.bukkit.block.data.BlockData.
    """

    def __init__(self):
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


    def getSlicesEaten(self) -> int:
        """
        Gets the number of slices eaten from this cake

        Returns
        - The number of slices eaten
        """
        ...


    def getSlicesRemaining(self) -> int:
        """
        Gets the number of slices remaining on this cake

        Returns
        - The number of slices remaining
        """
        ...


    def setSlicesEaten(self, n: int) -> None:
        """
        Sets the number of slices eaten from this cake

        Arguments
        - n: The number of slices eaten
        """
        ...


    def setSlicesRemaining(self, n: int) -> None:
        """
        Sets the number of slices remaining on this cake

        Arguments
        - n: The number of slices remaining
        """
        ...


    def toString(self) -> str:
        ...


    def clone(self) -> "Cake":
        ...
