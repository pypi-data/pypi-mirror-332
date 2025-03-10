"""
Python module generated from Java source file org.bukkit.entity.Bee

Java source file obtained from artifact spigot-api version 1.18.2-R0.1-20220607.160742-53

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Location
from org.bukkit.entity import *
from typing import Any, Callable, Iterable, Tuple


class Bee(Animals):
    """
    Represents a Bee.
    """

    def getHive(self) -> "Location":
        """
        Get the bee's hive location.

        Returns
        - hive location or null
        """
        ...


    def setHive(self, location: "Location") -> None:
        """
        Set the bee's hive location.

        Arguments
        - location: or null
        """
        ...


    def getFlower(self) -> "Location":
        """
        Get the bee's flower location.

        Returns
        - flower location or null
        """
        ...


    def setFlower(self, location: "Location") -> None:
        """
        Set the bee's flower location.

        Arguments
        - location: or null
        """
        ...


    def hasNectar(self) -> bool:
        """
        Get if the bee has nectar.

        Returns
        - nectar
        """
        ...


    def setHasNectar(self, nectar: bool) -> None:
        """
        Set if the bee has nectar.

        Arguments
        - nectar: whether the entity has nectar
        """
        ...


    def hasStung(self) -> bool:
        """
        Get if the bee has stung.

        Returns
        - has stung
        """
        ...


    def setHasStung(self, stung: bool) -> None:
        """
        Set if the bee has stung.

        Arguments
        - stung: has stung
        """
        ...


    def getAnger(self) -> int:
        """
        Get the bee's anger level.

        Returns
        - anger level
        """
        ...


    def setAnger(self, anger: int) -> None:
        """
        Set the bee's new anger level.

        Arguments
        - anger: new anger
        """
        ...


    def getCannotEnterHiveTicks(self) -> int:
        """
        Get the amount of ticks the bee cannot enter the hive for.

        Returns
        - Ticks the bee cannot enter a hive for
        """
        ...


    def setCannotEnterHiveTicks(self, ticks: int) -> None:
        """
        Set the amount of ticks the bee cannot enter a hive for.

        Arguments
        - ticks: Ticks the bee cannot enter a hive for
        """
        ...
