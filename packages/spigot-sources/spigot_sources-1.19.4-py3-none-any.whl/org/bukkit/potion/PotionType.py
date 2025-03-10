"""
Python module generated from Java source file org.bukkit.potion.PotionType

Java source file obtained from artifact spigot-api version 1.19.4-R0.1-20230607.155743-88

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit.potion import *
from typing import Any, Callable, Iterable, Tuple


class PotionType(Enum):
    """
    This enum reflects and matches each potion state that can be obtained from
    the Creative mode inventory
    """

    UNCRAFTABLE = (None, False, False)
    WATER = (None, False, False)
    MUNDANE = (None, False, False)
    THICK = (None, False, False)
    AWKWARD = (None, False, False)
    NIGHT_VISION = (PotionEffectType.NIGHT_VISION, False, True)
    INVISIBILITY = (PotionEffectType.INVISIBILITY, False, True)
    JUMP = (PotionEffectType.JUMP, True, True)
    FIRE_RESISTANCE = (PotionEffectType.FIRE_RESISTANCE, False, True)
    SPEED = (PotionEffectType.SPEED, True, True)
    SLOWNESS = (PotionEffectType.SLOW, True, True)
    WATER_BREATHING = (PotionEffectType.WATER_BREATHING, False, True)
    INSTANT_HEAL = (PotionEffectType.HEAL, True, False)
    INSTANT_DAMAGE = (PotionEffectType.HARM, True, False)
    POISON = (PotionEffectType.POISON, True, True)
    REGEN = (PotionEffectType.REGENERATION, True, True)
    STRENGTH = (PotionEffectType.INCREASE_DAMAGE, True, True)
    WEAKNESS = (PotionEffectType.WEAKNESS, False, True)
    LUCK = (PotionEffectType.LUCK, False, False)
    TURTLE_MASTER = (PotionEffectType.SLOW, True, True)
    SLOW_FALLING = (PotionEffectType.SLOW_FALLING, False, True)


    def getEffectType(self) -> "PotionEffectType":
        ...


    def isInstant(self) -> bool:
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
