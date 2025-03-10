"""
Python module generated from Java source file org.bukkit.entity.Husk

Java source file obtained from artifact spigot-api version 1.20.2-R0.1-20231205.164257-71

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import *
from typing import Any, Callable, Iterable, Tuple


class Husk(Zombie):
    """
    Represents a Husk - variant of Zombie.
    """

    def isConverting(self) -> bool:
        """
        Get if this entity is in the process of converting to a Zombie as a
        result of being underwater.

        Returns
        - conversion status
        """
        ...


    def getConversionTime(self) -> int:
        """
        Gets the amount of ticks until this entity will be converted to a Zombie
        as a result of being underwater.
        
        When this reaches 0, the entity will be converted.

        Returns
        - conversion time

        Raises
        - IllegalStateException: if .isConverting() is False.
        """
        ...


    def setConversionTime(self, time: int) -> None:
        """
        Sets the amount of ticks until this entity will be converted to a Zombie
        as a result of being underwater.
        
        When this reaches 0, the entity will be converted. A value of less than 0
        will stop the current conversion process without converting the current
        entity.

        Arguments
        - time: new conversion time
        """
        ...
