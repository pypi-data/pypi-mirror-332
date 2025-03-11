"""
Python module generated from Java source file org.bukkit.entity.MushroomCow

Java source file obtained from artifact spigot-api version 1.20.6-R0.1-20240613.150924-57

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit.entity import *
from org.bukkit.potion import PotionEffect
from org.bukkit.potion import PotionEffectType
from typing import Any, Callable, Iterable, Tuple


class MushroomCow(Cow):
    """
    Represents a mushroom Cow
    """

    def hasEffectsForNextStew(self) -> bool:
        """
        Checks for the presence of custom potion effects to be applied to the
        next suspicious stew received from milking this MushroomCow.

        Returns
        - True if custom potion effects are applied to the stew
        """
        ...


    def getEffectsForNextStew(self) -> list["PotionEffect"]:
        """
        Gets an immutable list containing all custom potion effects applied to
        the next suspicious stew received from milking this MushroomCow.
        
        Plugins should check that hasCustomEffects() returns True before calling
        this method.

        Returns
        - an immutable list of custom potion effects
        """
        ...


    def addEffectToNextStew(self, effect: "PotionEffect", overwrite: bool) -> bool:
        """
        Adds a custom potion effect to be applied to the next suspicious stew
        received from milking this MushroomCow.

        Arguments
        - effect: the potion effect to add
        - overwrite: True if any existing effect of the same type should be
        overwritten

        Returns
        - True if the effects to be applied to the suspicious stew changed
        as a result of this call
        """
        ...


    def removeEffectFromNextStew(self, type: "PotionEffectType") -> bool:
        """
        Removes a custom potion effect from being applied to the next suspicious
        stew received from milking this MushroomCow.

        Arguments
        - type: the potion effect type to remove

        Returns
        - True if the effects to be applied to the suspicious stew changed
        as a result of this call
        """
        ...


    def hasEffectForNextStew(self, type: "PotionEffectType") -> bool:
        """
        Checks for a specific custom potion effect type to be applied to the next
        suspicious stew received from milking this MushroomCow.

        Arguments
        - type: the potion effect type to check for

        Returns
        - True if the suspicious stew to be generated has this effect
        """
        ...


    def clearEffectsForNextStew(self) -> None:
        """
        Removes all custom potion effects to be applied to the next suspicious
        stew received from milking this MushroomCow.
        """
        ...


    def getVariant(self) -> "Variant":
        """
        Get the variant of this cow.

        Returns
        - cow variant
        """
        ...


    def setVariant(self, variant: "Variant") -> None:
        """
        Set the variant of this cow.

        Arguments
        - variant: cow variant
        """
        ...


    class Variant(Enum):
        """
        Represents the variant of a cow - ie its color.
        """

        RED = 0
        """
        Red mushroom cow.
        """
        BROWN = 1
        """
        Brown mushroom cow.
        """
