"""
Python module generated from Java source file org.bukkit.entity.ZombieVillager

Java source file obtained from artifact spigot-api version 1.20.6-R0.1-20240613.150924-57

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import OfflinePlayer
from org.bukkit.entity import *
from typing import Any, Callable, Iterable, Tuple


class ZombieVillager(Zombie):
    """
    Represents a Zombie which was once a Villager.
    """

    def setVillagerProfession(self, profession: "Villager.Profession") -> None:
        """
        Sets the villager profession of this zombie.
        """
        ...


    def getVillagerProfession(self) -> "Villager.Profession":
        """
        Returns the villager profession of this zombie.

        Returns
        - the profession or null
        """
        ...


    def getVillagerType(self) -> "Villager.Type":
        """
        Gets the current type of this villager.

        Returns
        - Current type.
        """
        ...


    def setVillagerType(self, type: "Villager.Type") -> None:
        """
        Sets the new type of this villager.

        Arguments
        - type: New type.
        """
        ...


    def isConverting(self) -> bool:
        """
        Get if this entity is in the process of converting to a Villager as a
        result of being cured.

        Returns
        - conversion status
        """
        ...


    def getConversionTime(self) -> int:
        """
        Gets the amount of ticks until this entity will be converted to a
        Villager as a result of being cured.
        
        When this reaches 0, the entity will be converted.

        Returns
        - conversion time

        Raises
        - IllegalStateException: if .isConverting() is False.
        """
        ...


    def setConversionTime(self, time: int) -> None:
        """
        Sets the amount of ticks until this entity will be converted to a
        Villager as a result of being cured.
        
        When this reaches 0, the entity will be converted. A value of less than 0
        will stop the current conversion process without converting the current
        entity.

        Arguments
        - time: new conversion time
        """
        ...


    def getConversionPlayer(self) -> "OfflinePlayer":
        """
        Gets the player who initiated the conversion.

        Returns
        - the player, or `null` if the player is unknown or the
        entity isn't converting currently
        """
        ...


    def setConversionPlayer(self, conversionPlayer: "OfflinePlayer") -> None:
        """
        Sets the player who initiated the conversion.
        
        This has no effect if this entity isn't converting currently.

        Arguments
        - conversionPlayer: the player
        """
        ...
