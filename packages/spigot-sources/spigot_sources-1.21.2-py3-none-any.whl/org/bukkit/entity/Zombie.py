"""
Python module generated from Java source file org.bukkit.entity.Zombie

Java source file obtained from artifact spigot-api version 1.21.2-R0.1-20241023.084343-5

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import *
from typing import Any, Callable, Iterable, Tuple


class Zombie(Monster, Ageable):
    """
    Represents a Zombie.
    """

    def isBaby(self) -> bool:
        """
        Gets whether the zombie is a baby

        Returns
        - Whether the zombie is a baby

        Deprecated
        - see Ageable.isAdult()
        """
        ...


    def setBaby(self, flag: bool) -> None:
        """
        Sets whether the zombie is a baby

        Arguments
        - flag: Whether the zombie is a baby

        Deprecated
        - see Ageable.setBaby() and Ageable.setAdult()
        """
        ...


    def isVillager(self) -> bool:
        """
        Gets whether the zombie is a villager

        Returns
        - Whether the zombie is a villager

        Deprecated
        - check if instanceof ZombieVillager.
        """
        ...


    def setVillager(self, flag: bool) -> None:
        """
        Arguments
        - flag: flag

        Deprecated
        - must spawn ZombieVillager.
        """
        ...


    def setVillagerProfession(self, profession: "Villager.Profession") -> None:
        """
        Arguments
        - profession: profession

        See
        - ZombieVillager.getVillagerProfession()
        """
        ...


    def getVillagerProfession(self) -> "Villager.Profession":
        """
        Returns
        - profession

        See
        - ZombieVillager.getVillagerProfession()
        """
        ...


    def isConverting(self) -> bool:
        """
        Get if this entity is in the process of converting to a Drowned as a
        result of being underwater.

        Returns
        - conversion status
        """
        ...


    def getConversionTime(self) -> int:
        """
        Gets the amount of ticks until this entity will be converted to a Drowned
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
        Sets the amount of ticks until this entity will be converted to a Drowned
        as a result of being underwater.
        
        When this reaches 0, the entity will be converted. A value of less than 0
        will stop the current conversion process without converting the current
        entity.

        Arguments
        - time: new conversion time
        """
        ...


    def canBreakDoors(self) -> bool:
        """
        Gets whether this zombie can break doors

        Returns
        - Whether this zombie can break doors
        """
        ...


    def setCanBreakDoors(self, flag: bool) -> None:
        """
        Sets whether this zombie can break doors
        
        This will be ignored if the entity is a Drowned. Will also stop the action if
        the entity is currently breaking a door.

        Arguments
        - flag: Whether this zombie can break doors
        """
        ...
