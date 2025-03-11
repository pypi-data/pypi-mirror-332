"""
Python module generated from Java source file org.bukkit.inventory.meta.components.consumable.ConsumableComponent

Java source file obtained from artifact spigot-api version 1.21.4-R0.1-20250303.102353-42

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit import Sound
from org.bukkit.configuration.serialization import ConfigurationSerializable
from org.bukkit.inventory.meta.components.consumable import *
from org.bukkit.inventory.meta.components.consumable.effects import ConsumableEffect
from typing import Any, Callable, Iterable, Tuple


class ConsumableComponent(ConfigurationSerializable):
    """
    Represents a component which item can be consumed on use.
    """

    def getConsumeSeconds(self) -> float:
        """
        Gets the time in seconds it will take for this item to be consumed.

        Returns
        - consume time
        """
        ...


    def setConsumeSeconds(self, consumeSeconds: float) -> None:
        """
        Sets the time in seconds it will take for this item to be consumed.

        Arguments
        - consumeSeconds: new consume time
        """
        ...


    def getAnimation(self) -> "Animation":
        """
        Gets the animation used during consumption of the item.

        Returns
        - animation
        """
        ...


    def setAnimation(self, animation: "Animation") -> None:
        """
        Sets the animation used during consumption of the item.

        Arguments
        - animation: the new animation
        """
        ...


    def getSound(self) -> "Sound":
        """
        Gets the sound to play during and on completion of the item's
        consumption.

        Returns
        - the sound
        """
        ...


    def setSound(self, sound: "Sound") -> None:
        """
        Sets the sound to play during and on completion of the item's
        consumption.

        Arguments
        - sound: sound or null for current default
        """
        ...


    def hasConsumeParticles(self) -> bool:
        """
        Gets whether consumption particles are emitted while consuming this item.

        Returns
        - True for particles emitted while consuming, False otherwise
        """
        ...


    def setConsumeParticles(self, consumeParticles: bool) -> None:
        """
        Sets whether consumption particles are emitted while consuming this item.

        Arguments
        - consumeParticles: if particles need to be emitted while consuming
        the item
        """
        ...


    def getEffects(self) -> list["ConsumableEffect"]:
        """
        Gets the effects which may be applied by this item when consumed.

        Returns
        - consumable effects
        """
        ...


    def setEffects(self, effects: list["ConsumableEffect"]) -> None:
        """
        Sets the effects which may be applied by this item when consumed.

        Arguments
        - effects: new effects
        """
        ...


    def addEffect(self, effect: "ConsumableEffect") -> "ConsumableEffect":
        """
        Adds an effect which may be applied by this item when consumed.

        Arguments
        - effect: the effect

        Returns
        - the added effect
        """
        ...


    class Animation(Enum):
        """
        Represents the animations for an item being consumed.
        """

        DRINK = 0
        EAT = 1
        NONE = 2
        BLOCK = 3
        BOW = 4
        BRUSH = 5
        CROSSBOW = 6
        SPEAR = 7
        SPYGLASS = 8
        TOOT_HORN = 9
