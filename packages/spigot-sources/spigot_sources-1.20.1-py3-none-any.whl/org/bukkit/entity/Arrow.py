"""
Python module generated from Java source file org.bukkit.entity.Arrow

Java source file obtained from artifact spigot-api version 1.20.1-R0.1-20230921.163938-66

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Color
from org.bukkit.entity import *
from org.bukkit.potion import PotionData
from org.bukkit.potion import PotionEffect
from org.bukkit.potion import PotionEffectType
from typing import Any, Callable, Iterable, Tuple


class Arrow(AbstractArrow):

    def setBasePotionData(self, data: "PotionData") -> None:
        """
        Sets the underlying potion data

        Arguments
        - data: PotionData to set the base potion state to
        """
        ...


    def getBasePotionData(self) -> "PotionData":
        """
        Returns the potion data about the base potion

        Returns
        - a PotionData object
        """
        ...


    def getColor(self) -> "Color":
        """
        Gets the color of this arrow.

        Returns
        - arrow Color or null if not color is set
        """
        ...


    def setColor(self, color: "Color") -> None:
        """
        Sets the color of this arrow. Will be applied as a tint to its particles.

        Arguments
        - color: arrow color, null to clear the color
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
        this arrow.
        
        Plugins should check that hasCustomEffects() returns True before calling
        this method.

        Returns
        - the immutable list of custom potion effects
        """
        ...


    def addCustomEffect(self, effect: "PotionEffect", overwrite: bool) -> bool:
        """
        Adds a custom potion effect to this arrow.

        Arguments
        - effect: the potion effect to add
        - overwrite: True if any existing effect of the same type should be
        overwritten

        Returns
        - True if the effect was added as a result of this call
        """
        ...


    def removeCustomEffect(self, type: "PotionEffectType") -> bool:
        """
        Removes a custom potion effect from this arrow.

        Arguments
        - type: the potion effect type to remove

        Returns
        - True if the an effect was removed as a result of this call

        Raises
        - IllegalArgumentException: if this operation would leave the Arrow
        in a state with no Custom Effects and PotionType.UNCRAFTABLE
        """
        ...


    def hasCustomEffect(self, type: "PotionEffectType") -> bool:
        """
        Checks for a specific custom potion effect type on this arrow.

        Arguments
        - type: the potion effect type to check for

        Returns
        - True if the potion has this effect
        """
        ...


    def clearCustomEffects(self) -> None:
        """
        Removes all custom potion effects from this arrow.

        Raises
        - IllegalArgumentException: if this operation would leave the Arrow
        in a state with no Custom Effects and PotionType.UNCRAFTABLE
        """
        ...
