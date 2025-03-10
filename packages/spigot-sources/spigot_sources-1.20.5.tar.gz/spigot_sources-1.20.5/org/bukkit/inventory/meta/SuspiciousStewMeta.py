"""
Python module generated from Java source file org.bukkit.inventory.meta.SuspiciousStewMeta

Java source file obtained from artifact spigot-api version 1.20.5-R0.1-20240429.101539-37

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.inventory.meta import *
from org.bukkit.potion import PotionEffect
from org.bukkit.potion import PotionEffectType
from typing import Any, Callable, Iterable, Tuple


class SuspiciousStewMeta(ItemMeta):
    """
    Represents a suspicious stew that can have custom effects.
    """

    def hasCustomEffects(self) -> bool:
        """
        Checks for the presence of custom potion effects.

        Returns
        - True if custom potion effects are applied
        """
        ...


    def getCustomEffects(self) -> list["PotionEffect"]:
        """
        Gets an immutable list containing all custom potion effects applied to
        this suspicious stew.
        
        Plugins should check that hasCustomEffects() returns True before calling
        this method.

        Returns
        - the immutable list of custom potion effects
        """
        ...


    def addCustomEffect(self, effect: "PotionEffect", overwrite: bool) -> bool:
        """
        Adds a custom potion effect to this suspicious stew.

        Arguments
        - effect: the potion effect to add
        - overwrite: True if any existing effect of the same type should be
        overwritten

        Returns
        - True if the suspicious stew meta changed as a result of this call
        """
        ...


    def removeCustomEffect(self, type: "PotionEffectType") -> bool:
        """
        Removes a custom potion effect from this suspicious stew.

        Arguments
        - type: the potion effect type to remove

        Returns
        - True if the suspicious stew meta changed as a result of this call
        """
        ...


    def hasCustomEffect(self, type: "PotionEffectType") -> bool:
        """
        Checks for a specific custom potion effect type on this suspicious stew.

        Arguments
        - type: the potion effect type to check for

        Returns
        - True if the suspicious stew has this effect
        """
        ...


    def clearCustomEffects(self) -> bool:
        """
        Removes all custom potion effects from this suspicious stew.

        Returns
        - True if the suspicious stew meta changed as a result of this call
        """
        ...


    def clone(self) -> "SuspiciousStewMeta":
        ...
