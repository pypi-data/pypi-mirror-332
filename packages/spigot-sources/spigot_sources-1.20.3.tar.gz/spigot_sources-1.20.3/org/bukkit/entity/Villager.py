"""
Python module generated from Java source file org.bukkit.entity.Villager

Java source file obtained from artifact spigot-api version 1.20.3-R0.1-20231207.085553-9

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from java.util import Locale
from org.bukkit import Keyed
from org.bukkit import Location
from org.bukkit import NamespacedKey
from org.bukkit.entity import *
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


    class Type(Enum):
        """
        Represents Villager type, usually corresponding to what biome they spawn
        in.
        """

        DESERT = 0
        JUNGLE = 1
        PLAINS = 2
        SAVANNA = 3
        SNOW = 4
        SWAMP = 5
        TAIGA = 6


        def getKey(self) -> "NamespacedKey":
            ...


    class Profession(Enum):
        """
        Represents the various different Villager professions there may be.
        Villagers have different trading options depending on their profession,
        """

        NONE = 0
        ARMORER = 1
        """
        Armorer profession. Wears a black apron. Armorers primarily trade for
        iron armor, chainmail armor, and sometimes diamond armor.
        """
        BUTCHER = 2
        """
        Butcher profession. Wears a white apron. Butchers primarily trade for
        raw and cooked food.
        """
        CARTOGRAPHER = 3
        """
        Cartographer profession. Wears a white robe. Cartographers primarily
        trade for explorer maps and some paper.
        """
        CLERIC = 4
        """
        Cleric profession. Wears a purple robe. Clerics primarily trade for
        rotten flesh, gold ingot, redstone, lapis, ender pearl, glowstone,
        and bottle o' enchanting.
        """
        FARMER = 5
        """
        Farmer profession. Wears a brown robe. Farmers primarily trade for
        food-related items.
        """
        FISHERMAN = 6
        """
        Fisherman profession. Wears a brown robe. Fisherman primarily trade
        for fish, as well as possibly selling string and/or coal.
        """
        FLETCHER = 7
        """
        Fletcher profession. Wears a brown robe. Fletchers primarily trade
        for string, bows, and arrows.
        """
        LEATHERWORKER = 8
        """
        Leatherworker profession. Wears a white apron. Leatherworkers
        primarily trade for leather, and leather armor, as well as saddles.
        """
        LIBRARIAN = 9
        """
        Librarian profession. Wears a white robe. Librarians primarily trade
        for paper, books, and enchanted books.
        """
        MASON = 10
        """
        Mason profession.
        """
        NITWIT = 11
        """
        Nitwit profession. Wears a green apron, cannot trade. Nitwit
        villagers do not do anything. They do not have any trades by default.
        """
        SHEPHERD = 12
        """
        Sheperd profession. Wears a brown robe. Shepherds primarily trade for
        wool items, and shears.
        """
        TOOLSMITH = 13
        """
        Toolsmith profession. Wears a black apron. Tool smiths primarily
        trade for iron and diamond tools.
        """
        WEAPONSMITH = 14
        """
        Weaponsmith profession. Wears a black apron. Weapon smiths primarily
        trade for iron and diamond weapons, sometimes enchanted.
        """


        def getKey(self) -> "NamespacedKey":
            ...
