"""
Python module generated from Java source file org.bukkit.entity.Hoglin

Java source file obtained from artifact spigot-api version 1.20.5-R0.1-20240429.101539-37

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import *
from typing import Any, Callable, Iterable, Tuple


class Hoglin(Animals, Enemy):
    """
    Represents a Hoglin.
    """

    def isImmuneToZombification(self) -> bool:
        """
        Gets whether the hoglin is immune to zombification.

        Returns
        - Whether the hoglin is immune to zombification
        """
        ...


    def setImmuneToZombification(self, flag: bool) -> None:
        """
        Sets whether the hoglin is immune to zombification.

        Arguments
        - flag: Whether the hoglin is immune to zombification
        """
        ...


    def isAbleToBeHunted(self) -> bool:
        """
        Get whether the hoglin is able to be hunted by piglins.

        Returns
        - Whether the hoglin is able to be hunted by piglins
        """
        ...


    def setIsAbleToBeHunted(self, flag: bool) -> None:
        """
        Sets whether the hoglin is able to be hunted by piglins.

        Arguments
        - flag: Whether the hoglin is able to be hunted by piglins.
        """
        ...


    def getConversionTime(self) -> int:
        """
        Gets the amount of ticks until this entity will be converted to a Zoglin.
        
        When this reaches 300, the entity will be converted.

        Returns
        - conversion time

        Raises
        - IllegalStateException: if .isConverting() is False.
        """
        ...


    def setConversionTime(self, time: int) -> None:
        """
        Sets the amount of ticks until this entity will be converted to a Zoglin.
        
        When this reaches 0, the entity will be converted. A value of less than 0
        will stop the current conversion process without converting the current
        entity.

        Arguments
        - time: new conversion time
        """
        ...


    def isConverting(self) -> bool:
        """
        Get if this entity is in the process of converting to a Zoglin.

        Returns
        - conversion status
        """
        ...
