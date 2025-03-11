"""
Python module generated from Java source file org.bukkit.entity.Villager

Java source file obtained from artifact spigot-api version 1.21.2-R0.1-20241023.084343-5

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.base import Preconditions
from com.google.common.collect import Lists
from java.util import Locale
from org.bukkit import Keyed
from org.bukkit import Location
from org.bukkit import NamespacedKey
from org.bukkit import Registry
from org.bukkit.entity import *
from org.bukkit.util import OldEnum
from typing import Any, Callable, Iterable, Tuple


class Villager(AbstractVillager):
    """
    Represents a villager NPC
    """

    def getProfession(self) -> "Profession":
        """
        Gets the current profession of this villager.

        Returns
        - Current profession.
        """
        ...


    def setProfession(self, profession: "Profession") -> None:
        """
        Sets the new profession of this villager.

        Arguments
        - profession: New profession.
        """
        ...


    def getVillagerType(self) -> "Type":
        """
        Gets the current type of this villager.

        Returns
        - Current type.
        """
        ...


    def setVillagerType(self, type: "Type") -> None:
        """
        Sets the new type of this villager.

        Arguments
        - type: New type.
        """
        ...


    def getVillagerLevel(self) -> int:
        """
        Gets the level of this villager.
        
        A villager with a level of 1 and no experience is liable to lose its
        profession.

        Returns
        - this villager's level
        """
        ...


    def setVillagerLevel(self, level: int) -> None:
        """
        Sets the level of this villager.
        
        A villager with a level of 1 and no experience is liable to lose its
        profession.

        Arguments
        - level: the new level

        Raises
        - IllegalArgumentException: if level not between [1, 5]
        """
        ...


    def getVillagerExperience(self) -> int:
        """
        Gets the trading experience of this villager.

        Returns
        - trading experience
        """
        ...


    def setVillagerExperience(self, experience: int) -> None:
        """
        Sets the trading experience of this villager.

        Arguments
        - experience: new experience

        Raises
        - IllegalArgumentException: if experience &lt; 0
        """
        ...


    def sleep(self, location: "Location") -> bool:
        """
        Attempts to make this villager sleep at the given location.
        
        The location must be in the current world and have a bed placed at the
        location. The villager will put its head on the specified block while
        sleeping.

        Arguments
        - location: the location of the bed

        Returns
        - whether the sleep was successful
        """
        ...


    def wakeup(self) -> None:
        """
        Causes this villager to wake up if he's currently sleeping.

        Raises
        - IllegalStateException: if not sleeping
        """
        ...


    def shakeHead(self) -> None:
        """
        Causes this villager to shake his head.
        """
        ...


    def zombify(self) -> "ZombieVillager":
        """
        Convert this Villager into a ZombieVillager as if it was killed by a
        Zombie.
        
        **Note:** this will fire a EntityTransformEvent

        Returns
        - the converted entity ZombieVillager or null if the
        conversion its cancelled
        """
        ...
