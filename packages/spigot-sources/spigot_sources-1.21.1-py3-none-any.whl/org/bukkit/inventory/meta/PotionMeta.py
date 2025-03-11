"""
Python module generated from Java source file org.bukkit.inventory.meta.PotionMeta

Java source file obtained from artifact spigot-api version 1.21.1-R0.1-20241022.152140-54

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Color
from org.bukkit.inventory.meta import *
from org.bukkit.potion import PotionData
from org.bukkit.potion import PotionEffect
from org.bukkit.potion import PotionEffectType
from org.bukkit.potion import PotionType
from typing import Any, Callable, Iterable, Tuple


class PotionMeta(ItemMeta):
    """
    Represents a potion or item that can have custom effects.
    """

    def setBasePotionData(self, data: "PotionData") -> None:
        """
        Sets the underlying potion data

        Arguments
        - data: PotionData to set the base potion state to

        Deprecated
        - Upgraded / extended potions are now their own PotionType use .setBasePotionType instead.
        """
        ...


    def getBasePotionData(self) -> "PotionData":
        """
        Returns the potion data about the base potion

        Returns
        - a PotionData object

        Deprecated
        - Upgraded / extended potions are now their own PotionType use .getBasePotionType() instead.
        """
        ...


    def setBasePotionType(self, type: "PotionType") -> None:
        """
        Sets the underlying potion type

        Arguments
        - type: PotionType to set the base potion state to
        """
        ...


    def getBasePotionType(self) -> "PotionType":
        """
        Returns the potion type about the base potion

        Returns
        - a PotionType object
        """
        ...


    def hasBasePotionType(self) -> bool:
        """
        Checks for the presence of a base potion type

        Returns
        - True if a base potion type is present
        """
        ...


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
        this potion.
        
        Plugins should check that hasCustomEffects() returns True before calling
        this method.

        Returns
        - the immutable list of custom potion effects
        """
        ...


    def addCustomEffect(self, effect: "PotionEffect", overwrite: bool) -> bool:
        """
        Adds a custom potion effect to this potion.

        Arguments
        - effect: the potion effect to add
        - overwrite: True if any existing effect of the same type should be
        overwritten

        Returns
        - True if the potion meta changed as a result of this call
        """
        ...


    def removeCustomEffect(self, type: "PotionEffectType") -> bool:
        """
        Removes a custom potion effect from this potion.

        Arguments
        - type: the potion effect type to remove

        Returns
        - True if the potion meta changed as a result of this call
        """
        ...


    def hasCustomEffect(self, type: "PotionEffectType") -> bool:
        """
        Checks for a specific custom potion effect type on this potion.

        Arguments
        - type: the potion effect type to check for

        Returns
        - True if the potion has this effect
        """
        ...


    def setMainEffect(self, type: "PotionEffectType") -> bool:
        """
        Moves a potion effect to the top of the potion effect list.
        
        This causes the client to display the potion effect in the potion's name.

        Arguments
        - type: the potion effect type to move

        Returns
        - True if the potion meta changed as a result of this call

        Deprecated
        - use .setBasePotionType(org.bukkit.potion.PotionType)
        """
        ...


    def clearCustomEffects(self) -> bool:
        """
        Removes all custom potion effects from this potion.

        Returns
        - True if the potion meta changed as a result of this call
        """
        ...


    def hasColor(self) -> bool:
        """
        Checks for existence of a potion color.

        Returns
        - True if this has a custom potion color
        """
        ...


    def getColor(self) -> "Color":
        """
        Gets the potion color that is set. A custom potion color will alter the
        display of the potion in an inventory slot.
        
        Plugins should check that hasColor() returns `True` before
        calling this method.

        Returns
        - the potion color that is set
        """
        ...


    def setColor(self, color: "Color") -> None:
        """
        Sets the potion color. A custom potion color will alter the display of
        the potion in an inventory slot.

        Arguments
        - color: the color to set
        """
        ...


    def clone(self) -> "PotionMeta":
        ...
