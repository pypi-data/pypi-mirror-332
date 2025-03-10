"""
Python module generated from Java source file org.bukkit.potion.PotionBrewer

Java source file obtained from artifact spigot-api version 1.18.2-R0.1-20220607.160742-53

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.potion import *
from typing import Any, Callable, Iterable, Tuple


class PotionBrewer:
    """
    Represents a brewer that can create PotionEffects.
    """

    def createEffect(self, potion: "PotionEffectType", duration: int, amplifier: int) -> "PotionEffect":
        """
        Creates a PotionEffect from the given PotionEffectType,
        applying duration modifiers and checks.

        Arguments
        - potion: The type of potion
        - duration: The duration in ticks
        - amplifier: The amplifier of the effect

        Returns
        - The resulting potion effect
        """
        ...


    def getEffectsFromDamage(self, damage: int) -> Iterable["PotionEffect"]:
        """
        Returns a collection of PotionEffect that would be applied from
        a potion with the given data value.

        Arguments
        - damage: The data value of the potion

        Returns
        - The list of effects

        Deprecated
        - Non-Functional
        """
        ...


    def getEffects(self, type: "PotionType", upgraded: bool, extended: bool) -> Iterable["PotionEffect"]:
        """
        Returns a collection of PotionEffect that would be applied from
        a potion with the given type.

        Arguments
        - type: The type of the potion
        - upgraded: Whether the potion is upgraded
        - extended: Whether the potion is extended

        Returns
        - The list of effects
        """
        ...
