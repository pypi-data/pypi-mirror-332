"""
Python module generated from Java source file org.bukkit.potion.PotionEffectType

Java source file obtained from artifact spigot-api version 1.17.1-R0.1-20211121.234319-104

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util import Arrays
from org.apache.commons.lang import Validate
from org.bukkit import Color
from org.bukkit.potion import *
from typing import Any, Callable, Iterable, Tuple


class PotionEffectType:
    """
    Represents a type of potion and its effect on an entity.
    """

    SPEED = PotionEffectTypeWrapper(1)
    """
    Increases movement speed.
    """
    SLOW = PotionEffectTypeWrapper(2)
    """
    Decreases movement speed.
    """
    FAST_DIGGING = PotionEffectTypeWrapper(3)
    """
    Increases dig speed.
    """
    SLOW_DIGGING = PotionEffectTypeWrapper(4)
    """
    Decreases dig speed.
    """
    INCREASE_DAMAGE = PotionEffectTypeWrapper(5)
    """
    Increases damage dealt.
    """
    HEAL = PotionEffectTypeWrapper(6)
    """
    Heals an entity.
    """
    HARM = PotionEffectTypeWrapper(7)
    """
    Hurts an entity.
    """
    JUMP = PotionEffectTypeWrapper(8)
    """
    Increases jump height.
    """
    CONFUSION = PotionEffectTypeWrapper(9)
    """
    Warps vision on the client.
    """
    REGENERATION = PotionEffectTypeWrapper(10)
    """
    Regenerates health.
    """
    DAMAGE_RESISTANCE = PotionEffectTypeWrapper(11)
    """
    Decreases damage dealt to an entity.
    """
    FIRE_RESISTANCE = PotionEffectTypeWrapper(12)
    """
    Stops fire damage.
    """
    WATER_BREATHING = PotionEffectTypeWrapper(13)
    """
    Allows breathing underwater.
    """
    INVISIBILITY = PotionEffectTypeWrapper(14)
    """
    Grants invisibility.
    """
    BLINDNESS = PotionEffectTypeWrapper(15)
    """
    Blinds an entity.
    """
    NIGHT_VISION = PotionEffectTypeWrapper(16)
    """
    Allows an entity to see in the dark.
    """
    HUNGER = PotionEffectTypeWrapper(17)
    """
    Increases hunger.
    """
    WEAKNESS = PotionEffectTypeWrapper(18)
    """
    Decreases damage dealt by an entity.
    """
    POISON = PotionEffectTypeWrapper(19)
    """
    Deals damage to an entity over time.
    """
    WITHER = PotionEffectTypeWrapper(20)
    """
    Deals damage to an entity over time and gives the health to the
    shooter.
    """
    HEALTH_BOOST = PotionEffectTypeWrapper(21)
    """
    Increases the maximum health of an entity.
    """
    ABSORPTION = PotionEffectTypeWrapper(22)
    """
    Increases the maximum health of an entity with health that cannot be
    regenerated, but is refilled every 30 seconds.
    """
    SATURATION = PotionEffectTypeWrapper(23)
    """
    Increases the food level of an entity each tick.
    """
    GLOWING = PotionEffectTypeWrapper(24)
    """
    Outlines the entity so that it can be seen from afar.
    """
    LEVITATION = PotionEffectTypeWrapper(25)
    """
    Causes the entity to float into the air.
    """
    LUCK = PotionEffectTypeWrapper(26)
    """
    Loot table luck.
    """
    UNLUCK = PotionEffectTypeWrapper(27)
    """
    Loot table unluck.
    """
    SLOW_FALLING = PotionEffectTypeWrapper(28)
    """
    Slows entity fall rate.
    """
    CONDUIT_POWER = PotionEffectTypeWrapper(29)
    """
    Effects granted by a nearby conduit. Includes enhanced underwater abilities.
    """
    DOLPHINS_GRACE = PotionEffectTypeWrapper(30)
    """
    Squee'ek uh'k kk'kkkk squeek eee'eek.
    """
    BAD_OMEN = PotionEffectTypeWrapper(31)
    """
    oof.
    """
    HERO_OF_THE_VILLAGE = PotionEffectTypeWrapper(32)
    """
    \o/.
    """


    def createEffect(self, duration: int, amplifier: int) -> "PotionEffect":
        """
        Creates a PotionEffect from this PotionEffectType, applying duration
        modifiers and checks.

        Arguments
        - duration: time in ticks
        - amplifier: the effect's amplifier

        Returns
        - a resulting potion effect

        See
        - PotionBrewer.createEffect(PotionEffectType, int, int)
        """
        ...


    def getDurationModifier(self) -> float:
        """
        Returns the duration modifier applied to effects of this type.

        Returns
        - duration modifier

        Deprecated
        - unused, always 1.0
        """
        ...


    def getId(self) -> int:
        """
        Returns the unique ID of this type.

        Returns
        - Unique ID

        Deprecated
        - Magic value
        """
        ...


    def getName(self) -> str:
        """
        Returns the name of this effect type.

        Returns
        - The name of this effect type
        """
        ...


    def isInstant(self) -> bool:
        """
        Returns whether the effect of this type happens once, immediately.

        Returns
        - whether this type is normally instant
        """
        ...


    def getColor(self) -> "Color":
        """
        Returns the color of this effect type.

        Returns
        - the color
        """
        ...


    def equals(self, obj: "Object") -> bool:
        ...


    def hashCode(self) -> int:
        ...


    def toString(self) -> str:
        ...


    @staticmethod
    def getById(id: int) -> "PotionEffectType":
        """
        Gets the effect type specified by the unique id.

        Arguments
        - id: Unique ID to fetch

        Returns
        - Resulting type, or null if not found.

        Deprecated
        - Magic value
        """
        ...


    @staticmethod
    def getByName(name: str) -> "PotionEffectType":
        """
        Gets the effect type specified by the given name.

        Arguments
        - name: Name of PotionEffectType to fetch

        Returns
        - Resulting PotionEffectType, or null if not found.
        """
        ...


    @staticmethod
    def registerPotionEffectType(type: "PotionEffectType") -> None:
        """
        Registers an effect type with the given object.
        
        Generally not to be used from within a plugin.

        Arguments
        - type: PotionType to register
        """
        ...


    @staticmethod
    def stopAcceptingRegistrations() -> None:
        """
        Stops accepting any effect type registrations.
        """
        ...


    @staticmethod
    def values() -> list["PotionEffectType"]:
        """
        Returns an array of all the registered PotionEffectTypes.
        This array is not necessarily in any particular order.

        Returns
        - Array of types.
        """
        ...
