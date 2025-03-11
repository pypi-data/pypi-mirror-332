"""
Python module generated from Java source file org.bukkit.inventory.meta.components.consumable.effects.ConsumableApplyEffects

Java source file obtained from artifact spigot-api version 1.21.4-R0.1-20250303.102353-42

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.inventory.meta.components.consumable.effects import *
from org.bukkit.potion import PotionEffect
from typing import Any, Callable, Iterable, Tuple


class ConsumableApplyEffects(ConsumableEffect):
    """
    Represent the effects applied when an item is consumed.
    """

    def getEffects(self) -> list["PotionEffect"]:
        """
        Gets the effects which may be applied by this item when consumed.

        Returns
        - consumable effects
        """
        ...


    def setEffects(self, effects: list["PotionEffect"]) -> None:
        """
        Sets the effects which may be applied by this item when consumed.

        Arguments
        - effects: new effects
        """
        ...


    def addEffect(self, effect: "PotionEffect") -> "PotionEffect":
        """
        Adds an effect which may be applied by this item when consumed.

        Arguments
        - effect: the effect

        Returns
        - the added effect
        """
        ...


    def getProbability(self) -> float:
        """
        Gets the probability of this effect being applied.

        Returns
        - probability
        """
        ...


    def setProbability(self, probability: float) -> None:
        """
        Sets the probability of this effect being applied.

        Arguments
        - probability: between 0 and 1 inclusive.
        """
        ...
