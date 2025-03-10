"""
Python module generated from Java source file org.bukkit.block.data.Ageable

Java source file obtained from artifact spigot-api version 1.18.2-R0.1-20220607.160742-53

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block.data import *
from typing import Any, Callable, Iterable, Tuple


class Ageable(BlockData):
    """
    'age' represents the different growth stages that a crop-like block can go
    through.
    
    A value of 0 indicates that the crop was freshly planted, whilst a value
    equal to .getMaximumAge() indicates that the crop is ripe and ready
    to be harvested.
    """

    def getAge(self) -> int:
        """
        Gets the value of the 'age' property.

        Returns
        - the 'age' value
        """
        ...


    def setAge(self, age: int) -> None:
        """
        Sets the value of the 'age' property.

        Arguments
        - age: the new 'age' value
        """
        ...


    def getMaximumAge(self) -> int:
        """
        Gets the maximum allowed value of the 'age' property.

        Returns
        - the maximum 'age' value
        """
        ...
