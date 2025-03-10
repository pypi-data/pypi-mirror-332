"""
Python module generated from Java source file org.bukkit.potion.PotionEffectType

Java source file obtained from artifact spigot-api version 1.20.1-R0.1-20230921.163938-66

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.base import Preconditions
from java.util import Arrays
from org.bukkit import Color
from org.bukkit import Keyed
from org.bukkit import NamespacedKey
from org.bukkit.potion import *
from typing import Any, Callable, Iterable, Tuple


class PotionEffectType(Keyed):
    """
    Represents a type of potion and its effect on an entity.
    """

    SPEED = PotionEffectTypeWrapper(1, "speed")
    """
    Increases movement speed.
    """
    SLOW = PotionEffectTypeWrapper(2, "slowness")
    """
    Decreases movement speed.
    """
    FAST_DIGGING = PotionEffectTypeWrapper(3, "haste")
    """
    Increases dig speed.
    """
    SLOW_DIGGING = PotionEffectTypeWrapper(4, "mining_fatigue")
    """
    Decreases dig speed.
    """
    INCREASE_DAMAGE = PotionEffectTypeWrapper(5, "strength")
    """
    Increases damage dealt.
    """
    HEAL = PotionEffectTypeWrapper(6, "instant_health")
    """
    Heals an entity.
    """
    HARM = PotionEffectTypeWrapper(7, "instant_damage")
    """
    Hurts an entity.
    """
    JUMP = PotionEffectTypeWrapper(8, "jump_boost")
    """
    Increases jump height.
    """
    CONFUSION = PotionEffectTypeWrapper(9, "nausea")
    """
    Warps vision on the client.
    """
    REGENERATION = PotionEffectTypeWrapper(10, "regeneration")
    """
    Regenerates health.
    """
    DAMAGE_RESISTANCE = PotionEffectTypeWrapper(11, "resistance")
    """
    Decreases damage dealt to an entity.
    """
    FIRE_RESISTANCE = PotionEffectTypeWrapper(12, "fire_resistance")
    """
    Stops fire damage.
    """
    WATER_BREATHING = PotionEffectTypeWrapper(13, "water_breathing")
    """
    Allows breathing underwater.
    """
    INVISIBILITY = PotionEffectTypeWrapper(14, "invisibility")
    """
    Grants invisibility.
    """
    BLINDNESS = PotionEffectTypeWrapper(15, "blindness")
    """
    Blinds an entity.
    """
    NIGHT_VISION = PotionEffectTypeWrapper(16, "night_vision")
    """
    Allows an entity to see in the dark.
    """
    HUNGER = PotionEffectTypeWrapper(17, "hunger")
    """
    Increases hunger.
    """
    WEAKNESS = PotionEffectTypeWrapper(18, "weakness")
    """
    Decreases damage dealt by an entity.
    """
    POISON = PotionEffectTypeWrapper(19, "poison")
    """
    Deals damage to an entity over time.
    """
    WITHER = PotionEffectTypeWrapper(20, "wither")
    """
    Deals damage to an entity over time and gives the health to the
    shooter.
    """
    HEALTH_BOOST = PotionEffectTypeWrapper(21, "health_boost")
    """
    Increases the maximum health of an entity.
    """
    ABSORPTION = PotionEffectTypeWrapper(22, "absorption")
    """
    Increases the maximum health of an entity with health that cannot be
    regenerated, but is refilled every 30 seconds.
    """
    SATURATION = PotionEffectTypeWrapper(23, "saturation")
    """
    Increases the food level of an entity each tick.
    """
    GLOWING = PotionEffectTypeWrapper(24, "glowing")
    """
    Outlines the entity so that it can be seen from afar.
    """
    LEVITATION = PotionEffectTypeWrapper(25, "levitation")
    """
    Causes the entity to float into the air.
    """
    LUCK = PotionEffectTypeWrapper(26, "luck")
    """
    Loot table luck.
    """
    UNLUCK = PotionEffectTypeWrapper(27, "unluck")
    """
    Loot table unluck.
    """
    SLOW_FALLING = PotionEffectTypeWrapper(28, "slow_falling")
    """
    Slows entity fall rate.
    """
    CONDUIT_POWER = PotionEffectTypeWrapper(29, "conduit_power")
    """
    Effects granted by a nearby conduit. Includes enhanced underwater abilities.
    """
    DOLPHINS_GRACE = PotionEffectTypeWrapper(30, "dolphins_grace")
    """
    Increses underwater movement speed.
    Squee'ek uh'k kk'kkkk squeek eee'eek.
    """
    BAD_OMEN = PotionEffectTypeWrapper(31, "bad_omen")
    """
    Triggers a raid when the player enters a village.
    oof.
    """
    HERO_OF_THE_VILLAGE = PotionEffectTypeWrapper(32, "hero_of_the_village")
    """
    Reduces the cost of villager trades.
    \o/.
    """
    DARKNESS = PotionEffectTypeWrapper(33, "darkness")
    """
    Causes the player's vision to dim occasionally.
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


    def getKey(self) -> "NamespacedKey":
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
    def getByKey(key: "NamespacedKey") -> "PotionEffectType":
        """
        Gets the PotionEffectType at the specified key

        Arguments
        - key: key to fetch

        Returns
        - Resulting PotionEffectType, or null if not found
        """
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
