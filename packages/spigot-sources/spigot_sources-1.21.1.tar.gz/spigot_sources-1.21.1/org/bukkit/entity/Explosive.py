"""
Python module generated from Java source file org.bukkit.entity.Explosive

Java source file obtained from artifact spigot-api version 1.21.1-R0.1-20241022.152140-54

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import *
from typing import Any, Callable, Iterable, Tuple


class Explosive(Entity):
    """
    A representation of an explosive entity
    """

    def setYield(self, yield: float) -> None:
        """
        Set the radius affected by this explosive's explosion

        Arguments
        - yield: The explosive yield
        """
        ...


    def getYield(self) -> float:
        """
        Return the radius or yield of this explosive's explosion

        Returns
        - the radius of blocks affected
        """
        ...


    def setIsIncendiary(self, isIncendiary: bool) -> None:
        """
        Set whether or not this explosive's explosion causes fire

        Arguments
        - isIncendiary: Whether it should cause fire
        """
        ...


    def isIncendiary(self) -> bool:
        """
        Return whether or not this explosive creates a fire when exploding

        Returns
        - True if the explosive creates fire, False otherwise
        """
        ...
