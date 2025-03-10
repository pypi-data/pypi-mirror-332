"""
Python module generated from Java source file org.bukkit.block.data.type.Beehive

Java source file obtained from artifact spigot-api version 1.20.3-R0.1-20231207.085553-9

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block.data import Directional
from org.bukkit.block.data.type import *
from typing import Any, Callable, Iterable, Tuple


class Beehive(Directional):
    """
    'honey_level' represents the amount of honey stored in the hive.
    """

    def getHoneyLevel(self) -> int:
        """
        Gets the value of the 'honey_level' property.

        Returns
        - the 'honey_level' value
        """
        ...


    def setHoneyLevel(self, honeyLevel: int) -> None:
        """
        Sets the value of the 'honey_level' property.

        Arguments
        - honeyLevel: the new 'honey_level' value
        """
        ...


    def getMaximumHoneyLevel(self) -> int:
        """
        Gets the maximum allowed value of the 'honey_level' property.

        Returns
        - the maximum 'honey_level' value
        """
        ...
