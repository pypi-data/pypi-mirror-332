"""
Python module generated from Java source file org.bukkit.potion.PotionEffect

Java source file obtained from artifact spigot-api version 1.17.1-R0.1-20211121.234319-104

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.collect import ImmutableMap
from java.util import NoSuchElementException
from org.apache.commons.lang import Validate
from org.bukkit import Color
from org.bukkit.configuration.serialization import ConfigurationSerializable
from org.bukkit.configuration.serialization import SerializableAs
from org.bukkit.entity import LivingEntity
from org.bukkit.potion import *
from typing import Any, Callable, Iterable, Tuple


class PotionEffect(ConfigurationSerializable):
    """
    Represents a potion effect, that can be added to a LivingEntity. A
    potion effect has a duration that it will last for, an amplifier that will
    enhance its effects, and a PotionEffectType, that represents its
    effect on an entity.
    """

    def __init__(self, type: "PotionEffectType", duration: int, amplifier: int, ambient: bool, particles: bool, icon: bool):
        """
        Creates a potion effect.

        Arguments
        - type: effect type
        - duration: measured in ticks, see PotionEffect.getDuration()
        - amplifier: the amplifier, see PotionEffect.getAmplifier()
        - ambient: the ambient status, see PotionEffect.isAmbient()
        - particles: the particle status, see PotionEffect.hasParticles()
        - icon: the icon status, see PotionEffect.hasIcon()
        """
        ...


    def __init__(self, type: "PotionEffectType", duration: int, amplifier: int, ambient: bool, particles: bool):
        """
        Creates a potion effect with no defined color.

        Arguments
        - type: effect type
        - duration: measured in ticks, see PotionEffect.getDuration()
        - amplifier: the amplifier, see PotionEffect.getAmplifier()
        - ambient: the ambient status, see PotionEffect.isAmbient()
        - particles: the particle status, see PotionEffect.hasParticles()
        """
        ...


    def __init__(self, type: "PotionEffectType", duration: int, amplifier: int, ambient: bool):
        """
        Creates a potion effect. Assumes that particles are visible

        Arguments
        - type: effect type
        - duration: measured in ticks, see PotionEffect.getDuration()
        - amplifier: the amplifier, see PotionEffect.getAmplifier()
        - ambient: the ambient status, see PotionEffect.isAmbient()
        """
        ...


    def __init__(self, type: "PotionEffectType", duration: int, amplifier: int):
        """
        Creates a potion effect. Assumes ambient is True.

        Arguments
        - type: Effect type
        - duration: measured in ticks
        - amplifier: the amplifier for the effect

        See
        - PotionEffect.PotionEffect(PotionEffectType, int, int, boolean)
        """
        ...


    def __init__(self, map: dict[str, "Object"]):
        """
        Constructor for deserialization.

        Arguments
        - map: the map to deserialize from
        """
        ...


    def serialize(self) -> dict[str, "Object"]:
        ...


    def apply(self, entity: "LivingEntity") -> bool:
        """
        Attempts to add the effect represented by this object to the given
        LivingEntity.

        Arguments
        - entity: The entity to add this effect to

        Returns
        - Whether the effect could be added

        See
        - LivingEntity.addPotionEffect(PotionEffect)
        """
        ...


    def equals(self, obj: "Object") -> bool:
        ...


    def getAmplifier(self) -> int:
        """
        Returns the amplifier of this effect. A higher amplifier means the
        potion effect happens more often over its duration and in some cases
        has more effect on its target.

        Returns
        - The effect amplifier
        """
        ...


    def getDuration(self) -> int:
        """
        Returns the duration (in ticks) that this effect will run for when
        applied to a LivingEntity.

        Returns
        - The duration of the effect
        """
        ...


    def getType(self) -> "PotionEffectType":
        """
        Returns the PotionEffectType of this effect.

        Returns
        - The potion type of this effect
        """
        ...


    def isAmbient(self) -> bool:
        """
        Makes potion effect produce more, translucent, particles.

        Returns
        - if this effect is ambient
        """
        ...


    def hasParticles(self) -> bool:
        """
        Returns
        - whether this effect has particles or not
        """
        ...


    def getColor(self) -> "Color":
        """
        Returns
        - color of this potion's particles. May be null if the potion has no particles or defined color.

        Deprecated
        - color is not part of potion effects
        """
        ...


    def hasIcon(self) -> bool:
        """
        Returns
        - whether this effect has an icon or not
        """
        ...


    def hashCode(self) -> int:
        ...


    def toString(self) -> str:
        ...
