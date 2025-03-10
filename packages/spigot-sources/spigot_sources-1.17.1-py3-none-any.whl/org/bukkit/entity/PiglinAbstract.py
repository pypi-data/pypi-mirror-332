"""
Python module generated from Java source file org.bukkit.entity.PiglinAbstract

Java source file obtained from artifact spigot-api version 1.17.1-R0.1-20211121.234319-104

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import *
from typing import Any, Callable, Iterable, Tuple


class PiglinAbstract(Monster, Ageable):
    """
    Piglin / Piglin Brute.
    """

    def isImmuneToZombification(self) -> bool:
        """
        Gets whether the piglin is immune to zombification.

        Returns
        - Whether the piglin is immune to zombification
        """
        ...


    def setImmuneToZombification(self, flag: bool) -> None:
        """
        Sets whether the piglin is immune to zombification.

        Arguments
        - flag: Whether the piglin is immune to zombification
        """
        ...


    def getConversionTime(self) -> int:
        """
        Gets the amount of ticks until this entity will be converted to a
        Zombified Piglin.
        
        When this reaches 300, the entity will be converted.

        Returns
        - conversion time

        Raises
        - IllegalStateException: if .isConverting() is False.
        """
        ...


    def setConversionTime(self, time: int) -> None:
        """
        Sets the amount of ticks until this entity will be converted to a
        Zombified Piglin.
        
        When this reaches 0, the entity will be converted. A value of less than 0
        will stop the current conversion process without converting the current
        entity.

        Arguments
        - time: new conversion time
        """
        ...


    def isConverting(self) -> bool:
        """
        Get if this entity is in the process of converting to a Zombified Piglin.

        Returns
        - conversion status
        """
        ...


    def isBaby(self) -> bool:
        """
        Gets whether the piglin is a baby

        Returns
        - Whether the piglin is a baby

        Deprecated
        - see Ageable.isAdult()
        """
        ...


    def setBaby(self, flag: bool) -> None:
        """
        Sets whether the piglin is a baby

        Arguments
        - flag: Whether the piglin is a baby

        Deprecated
        - see Ageable.setBaby() and Ageable.setAdult()
        """
        ...
