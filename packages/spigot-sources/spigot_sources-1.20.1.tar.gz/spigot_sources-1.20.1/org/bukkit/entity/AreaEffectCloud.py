"""
Python module generated from Java source file org.bukkit.entity.AreaEffectCloud

Java source file obtained from artifact spigot-api version 1.20.1-R0.1-20230921.163938-66

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Color
from org.bukkit import Particle
from org.bukkit.entity import *
from org.bukkit.potion import PotionData
from org.bukkit.potion import PotionEffect
from org.bukkit.potion import PotionEffectType
from org.bukkit.projectiles import ProjectileSource
from typing import Any, Callable, Iterable, Tuple


class AreaEffectCloud(Entity):
    """
    Represents an area effect cloud which will imbue a potion effect onto
    entities which enter it.
    """

    def getDuration(self) -> int:
        """
        Gets the duration which this cloud will exist for (in ticks).

        Returns
        - cloud duration
        """
        ...


    def setDuration(self, duration: int) -> None:
        """
        Sets the duration which this cloud will exist for (in ticks).

        Arguments
        - duration: cloud duration
        """
        ...


    def getWaitTime(self) -> int:
        """
        Gets the time which an entity has to be exposed to the cloud before the
        effect is applied.

        Returns
        - wait time
        """
        ...


    def setWaitTime(self, waitTime: int) -> None:
        """
        Sets the time which an entity has to be exposed to the cloud before the
        effect is applied.

        Arguments
        - waitTime: wait time
        """
        ...


    def getReapplicationDelay(self) -> int:
        """
        Gets the time that an entity will be immune from subsequent exposure.

        Returns
        - reapplication delay
        """
        ...


    def setReapplicationDelay(self, delay: int) -> None:
        """
        Sets the time that an entity will be immune from subsequent exposure.

        Arguments
        - delay: reapplication delay
        """
        ...


    def getDurationOnUse(self) -> int:
        """
        Gets the amount that the duration of this cloud will decrease by when it
        applies an effect to an entity.

        Returns
        - duration on use delta
        """
        ...


    def setDurationOnUse(self, duration: int) -> None:
        """
        Sets the amount that the duration of this cloud will decrease by when it
        applies an effect to an entity.

        Arguments
        - duration: duration on use delta
        """
        ...


    def getRadius(self) -> float:
        """
        Gets the initial radius of the cloud.

        Returns
        - radius
        """
        ...


    def setRadius(self, radius: float) -> None:
        """
        Sets the initial radius of the cloud.

        Arguments
        - radius: radius
        """
        ...


    def getRadiusOnUse(self) -> float:
        """
        Gets the amount that the radius of this cloud will decrease by when it
        applies an effect to an entity.

        Returns
        - radius on use delta
        """
        ...


    def setRadiusOnUse(self, radius: float) -> None:
        """
        Sets the amount that the radius of this cloud will decrease by when it
        applies an effect to an entity.

        Arguments
        - radius: radius on use delta
        """
        ...


    def getRadiusPerTick(self) -> float:
        """
        Gets the amount that the radius of this cloud will decrease by each tick.

        Returns
        - radius per tick delta
        """
        ...


    def setRadiusPerTick(self, radius: float) -> None:
        """
        Gets the amount that the radius of this cloud will decrease by each tick.

        Arguments
        - radius: per tick delta
        """
        ...


    def getParticle(self) -> "Particle":
        """
        Gets the particle which this cloud will be composed of

        Returns
        - particle the set particle type
        """
        ...


    def setParticle(self, particle: "Particle") -> None:
        """
        Sets the particle which this cloud will be composed of

        Arguments
        - particle: the new particle type
        """
        ...


    def setParticle(self, particle: "Particle", data: "T") -> None:
        """
        Sets the particle which this cloud will be composed of
        
        Type `<T>`: type of particle data (see Particle.getDataType()

        Arguments
        - particle: the new particle type
        - data: the data to use for the particle or null,
                    the type of this depends on Particle.getDataType()
        """
        ...


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
        this cloud.
        
        Plugins should check that hasCustomEffects() returns True before calling
        this method.

        Returns
        - the immutable list of custom potion effects
        """
        ...


    def addCustomEffect(self, effect: "PotionEffect", overwrite: bool) -> bool:
        """
        Adds a custom potion effect to this cloud.

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
        Removes a custom potion effect from this cloud.

        Arguments
        - type: the potion effect type to remove

        Returns
        - True if the an effect was removed as a result of this call
        """
        ...


    def hasCustomEffect(self, type: "PotionEffectType") -> bool:
        """
        Checks for a specific custom potion effect type on this cloud.

        Arguments
        - type: the potion effect type to check for

        Returns
        - True if the potion has this effect
        """
        ...


    def clearCustomEffects(self) -> None:
        """
        Removes all custom potion effects from this cloud.
        """
        ...


    def getColor(self) -> "Color":
        """
        Gets the color of this cloud. Will be applied as a tint to its particles.

        Returns
        - cloud color
        """
        ...


    def setColor(self, color: "Color") -> None:
        """
        Sets the color of this cloud. Will be applied as a tint to its particles.

        Arguments
        - color: cloud color
        """
        ...


    def getSource(self) -> "ProjectileSource":
        """
        Retrieve the original source of this cloud.

        Returns
        - the ProjectileSource that threw the LingeringPotion
        """
        ...


    def setSource(self, source: "ProjectileSource") -> None:
        """
        Set the original source of this cloud.

        Arguments
        - source: the ProjectileSource that threw the LingeringPotion
        """
        ...
