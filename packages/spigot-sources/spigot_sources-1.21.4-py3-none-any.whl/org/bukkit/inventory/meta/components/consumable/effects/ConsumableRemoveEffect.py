"""
Python module generated from Java source file org.bukkit.inventory.meta.components.consumable.effects.ConsumableRemoveEffect

Java source file obtained from artifact spigot-api version 1.21.4-R0.1-20250303.102353-42

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.inventory.meta.components.consumable.effects import *
from org.bukkit.potion import PotionEffectType
from typing import Any, Callable, Iterable, Tuple


class ConsumableRemoveEffect(ConsumableEffect):
    """
    Represent the effects to be removed when an item is consumed.
    """

    def getEffectTypes(self) -> list["PotionEffectType"]:
        """
        Gets the effects which may be removed by this item when consumed.

        Returns
        - the effects
        """
        ...


    def setEffectTypes(self, effects: list["PotionEffectType"]) -> None:
        """
        Sets the effects which may be removed by this item when consumed.

        Arguments
        - effects: new effects
        """
        ...


    def addEffectType(self, effect: "PotionEffectType") -> "PotionEffectType":
        """
        Adds an effect which may be applied by this item when consumed.

        Arguments
        - effect: the effect

        Returns
        - the added effect
        """
        ...
