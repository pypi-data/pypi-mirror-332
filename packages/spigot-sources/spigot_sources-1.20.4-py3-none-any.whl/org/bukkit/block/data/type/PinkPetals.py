"""
Python module generated from Java source file org.bukkit.block.data.type.PinkPetals

Java source file obtained from artifact spigot-api version 1.20.4-R0.1-20240423.152506-123

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block.data import Directional
from org.bukkit.block.data.type import *
from typing import Any, Callable, Iterable, Tuple


class PinkPetals(Directional):
    """
    'flower_amount' represents the number of petals.
    """

    def getFlowerAmount(self) -> int:
        """
        Gets the value of the 'flower_amount' property.

        Returns
        - the 'flower_amount' value
        """
        ...


    def setFlowerAmount(self, flower_amount: int) -> None:
        """
        Sets the value of the 'flower_amount' property.

        Arguments
        - flower_amount: the new 'flower_amount' value
        """
        ...


    def getMaximumFlowerAmount(self) -> int:
        """
        Gets the maximum allowed value of the 'flower_amount' property.

        Returns
        - the maximum 'flower_amount' value
        """
        ...
