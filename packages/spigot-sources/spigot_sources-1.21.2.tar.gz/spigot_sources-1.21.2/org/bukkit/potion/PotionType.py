"""
Python module generated from Java source file org.bukkit.potion.PotionType

Java source file obtained from artifact spigot-api version 1.21.2-R0.1-20241023.084343-5

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.base import Suppliers
from enum import Enum
from java.util.function import Supplier
from org.bukkit import Bukkit
from org.bukkit import Keyed
from org.bukkit import NamespacedKey
from org.bukkit.potion import *
from typing import Any, Callable, Iterable, Tuple


class PotionType(Enum):
    """
    This enum reflects and matches each potion state that can be obtained from
    the Creative mode inventory
    """

    WATER = ("water")
    MUNDANE = ("mundane")
    THICK = ("thick")
    AWKWARD = ("awkward")
    NIGHT_VISION = ("night_vision")
    LONG_NIGHT_VISION = ("long_night_vision")
    INVISIBILITY = ("invisibility")
    LONG_INVISIBILITY = ("long_invisibility")
    LEAPING = ("leaping")
    LONG_LEAPING = ("long_leaping")
    STRONG_LEAPING = ("strong_leaping")
    FIRE_RESISTANCE = ("fire_resistance")
    LONG_FIRE_RESISTANCE = ("long_fire_resistance")
    SWIFTNESS = ("swiftness")
    LONG_SWIFTNESS = ("long_swiftness")
    STRONG_SWIFTNESS = ("strong_swiftness")
    SLOWNESS = ("slowness")
    LONG_SLOWNESS = ("long_slowness")
    STRONG_SLOWNESS = ("strong_slowness")
    WATER_BREATHING = ("water_breathing")
    LONG_WATER_BREATHING = ("long_water_breathing")
    HEALING = ("healing")
    STRONG_HEALING = ("strong_healing")
    HARMING = ("harming")
    STRONG_HARMING = ("strong_harming")
    POISON = ("poison")
    LONG_POISON = ("long_poison")
    STRONG_POISON = ("strong_poison")
    REGENERATION = ("regeneration")
    LONG_REGENERATION = ("long_regeneration")
    STRONG_REGENERATION = ("strong_regeneration")
    STRENGTH = ("strength")
    LONG_STRENGTH = ("long_strength")
    STRONG_STRENGTH = ("strong_strength")
    WEAKNESS = ("weakness")
    LONG_WEAKNESS = ("long_weakness")
    LUCK = ("luck")
    TURTLE_MASTER = ("turtle_master")
    LONG_TURTLE_MASTER = ("long_turtle_master")
    STRONG_TURTLE_MASTER = ("strong_turtle_master")
    SLOW_FALLING = ("slow_falling")
    LONG_SLOW_FALLING = ("long_slow_falling")
    WIND_CHARGED = ("wind_charged")
    WEAVING = ("weaving")
    OOZING = ("oozing")
    INFESTED = ("infested")


    def getEffectType(self) -> "PotionEffectType":
        """
        Returns
        - the potion effect type of this potion type

        Deprecated
        - Potions can have multiple effects use .getPotionEffects()
        """
        ...


    def getPotionEffects(self) -> list["PotionEffect"]:
        """
        Returns
        - a list of all effects this potion type has
        """
        ...


    def isInstant(self) -> bool:
        """
        Returns
        - if this potion type is instant

        Deprecated
        - PotionType can have multiple effects, some of which can be instant and others not.
        Use PotionEffectType.isInstant() in combination with .getPotionEffects() and PotionEffect.getType()
        """
        ...


    def isUpgradeable(self) -> bool:
        """
        Checks if the potion type has an upgraded state.
        This refers to whether or not the potion type can be Tier 2,
        such as Potion of Fire Resistance II.

        Returns
        - True if the potion type can be upgraded;
        """
        ...


    def isExtendable(self) -> bool:
        """
        Checks if the potion type has an extended state.
        This refers to the extended duration potions

        Returns
        - True if the potion type can be extended
        """
        ...


    def getMaxLevel(self) -> int:
        ...


    @staticmethod
    def getByEffect(effectType: "PotionEffectType") -> "PotionType":
        """
        Arguments
        - effectType: the effect to get by

        Returns
        - the matching potion type

        Deprecated
        - Misleading
        """
        ...


    def getKey(self) -> "NamespacedKey":
        ...


    class InternalPotionData:
        """
        Deprecated
        - Do not use, interface will get removed, and the plugin won't run
        """

        def getEffectType(self) -> "PotionEffectType":
            ...


        def getPotionEffects(self) -> list["PotionEffect"]:
            ...


        def isInstant(self) -> bool:
            ...


        def isUpgradeable(self) -> bool:
            ...


        def isExtendable(self) -> bool:
            ...


        def getMaxLevel(self) -> int:
            ...
