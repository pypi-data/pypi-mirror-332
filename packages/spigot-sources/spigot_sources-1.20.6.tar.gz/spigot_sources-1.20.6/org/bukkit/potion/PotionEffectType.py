"""
Python module generated from Java source file org.bukkit.potion.PotionEffectType

Java source file obtained from artifact spigot-api version 1.20.6-R0.1-20240613.150924-57

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.base import Preconditions
from com.google.common.collect import BiMap
from com.google.common.collect import HashBiMap
from com.google.common.collect import Lists
from java.util import Locale
from org.bukkit import Color
from org.bukkit import Keyed
from org.bukkit import NamespacedKey
from org.bukkit import Registry
from org.bukkit import Translatable
from org.bukkit.potion import *
from typing import Any, Callable, Iterable, Tuple


class PotionEffectType(Keyed, Translatable):
    """
    Represents a type of potion and its effect on an entity.
    """

    SPEED = getPotionEffectType(1, "speed")
    """
    Increases movement speed.
    """
    SLOWNESS = getPotionEffectType(2, "slowness")
    """
    Decreases movement speed.
    """
    HASTE = getPotionEffectType(3, "haste")
    """
    Increases dig speed.
    """
    MINING_FATIGUE = getPotionEffectType(4, "mining_fatigue")
    """
    Decreases dig speed.
    """
    STRENGTH = getPotionEffectType(5, "strength")
    """
    Increases damage dealt.
    """
    INSTANT_HEALTH = getPotionEffectType(6, "instant_health")
    """
    Heals an entity.
    """
    INSTANT_DAMAGE = getPotionEffectType(7, "instant_damage")
    """
    Hurts an entity.
    """
    JUMP_BOOST = getPotionEffectType(8, "jump_boost")
    """
    Increases jump height.
    """
    NAUSEA = getPotionEffectType(9, "nausea")
    """
    Warps vision on the client.
    """
    REGENERATION = getPotionEffectType(10, "regeneration")
    """
    Regenerates health.
    """
    RESISTANCE = getPotionEffectType(11, "resistance")
    """
    Decreases damage dealt to an entity.
    """
    FIRE_RESISTANCE = getPotionEffectType(12, "fire_resistance")
    """
    Stops fire damage.
    """
    WATER_BREATHING = getPotionEffectType(13, "water_breathing")
    """
    Allows breathing underwater.
    """
    INVISIBILITY = getPotionEffectType(14, "invisibility")
    """
    Grants invisibility.
    """
    BLINDNESS = getPotionEffectType(15, "blindness")
    """
    Blinds an entity.
    """
    NIGHT_VISION = getPotionEffectType(16, "night_vision")
    """
    Allows an entity to see in the dark.
    """
    HUNGER = getPotionEffectType(17, "hunger")
    """
    Increases hunger.
    """
    WEAKNESS = getPotionEffectType(18, "weakness")
    """
    Decreases damage dealt by an entity.
    """
    POISON = getPotionEffectType(19, "poison")
    """
    Deals damage to an entity over time.
    """
    WITHER = getPotionEffectType(20, "wither")
    """
    Deals damage to an entity over time and gives the health to the
    shooter.
    """
    HEALTH_BOOST = getPotionEffectType(21, "health_boost")
    """
    Increases the maximum health of an entity.
    """
    ABSORPTION = getPotionEffectType(22, "absorption")
    """
    Increases the maximum health of an entity with health that cannot be
    regenerated, but is refilled every 30 seconds.
    """
    SATURATION = getPotionEffectType(23, "saturation")
    """
    Increases the food level of an entity each tick.
    """
    GLOWING = getPotionEffectType(24, "glowing")
    """
    Outlines the entity so that it can be seen from afar.
    """
    LEVITATION = getPotionEffectType(25, "levitation")
    """
    Causes the entity to float into the air.
    """
    LUCK = getPotionEffectType(26, "luck")
    """
    Loot table luck.
    """
    UNLUCK = getPotionEffectType(27, "unluck")
    """
    Loot table unluck.
    """
    SLOW_FALLING = getPotionEffectType(28, "slow_falling")
    """
    Slows entity fall rate.
    """
    CONDUIT_POWER = getPotionEffectType(29, "conduit_power")
    """
    Effects granted by a nearby conduit. Includes enhanced underwater abilities.
    """
    DOLPHINS_GRACE = getPotionEffectType(30, "dolphins_grace")
    """
    Increses underwater movement speed.
    Squee'ek uh'k kk'kkkk squeek eee'eek.
    """
    BAD_OMEN = getPotionEffectType(31, "bad_omen")
    """
    Triggers an ominous event when the player enters a village or trial chambers.
    oof.
    """
    HERO_OF_THE_VILLAGE = getPotionEffectType(32, "hero_of_the_village")
    """
    Reduces the cost of villager trades.
    \o/.
    """
    DARKNESS = getPotionEffectType(33, "darkness")
    """
    Causes the player's vision to dim occasionally.
    """
    TRIAL_OMEN = getPotionEffectType(34, "trial_omen")
    """
    Causes trial spawners to become ominous.
    """
    RAID_OMEN = getPotionEffectType(35, "raid_omen")
    """
    Triggers a raid when a player enters a village.
    """
    WIND_CHARGED = getPotionEffectType(36, "wind_charged")
    """
    Emits a wind burst upon death.
    """
    WEAVING = getPotionEffectType(37, "weaving")
    """
    Creates cobwebs upon death.
    """
    OOZING = getPotionEffectType(38, "oozing")
    """
    Causes slimes to spawn upon death.
    """
    INFESTED = getPotionEffectType(39, "infested")
    """
    Chance of spawning silverfish when hurt.
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


    def isInstant(self) -> bool:
        """
        Returns whether the effect of this type happens once, immediately.

        Returns
        - whether this type is normally instant
        """
        ...


    def getCategory(self) -> "PotionEffectTypeCategory":
        """
        Returns the PotionEffectTypeCategory category of this effect type.

        Returns
        - the category
        """
        ...


    def getColor(self) -> "Color":
        """
        Returns the color of this effect type.

        Returns
        - the color
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

        Deprecated
        - only for backwards compatibility, use .getKey() instead.
        """
        ...


    @staticmethod
    def getByKey(key: "NamespacedKey") -> "PotionEffectType":
        """
        Gets the PotionEffectType at the specified key

        Arguments
        - key: key to fetch

        Returns
        - Resulting PotionEffectType, or null if not found

        Deprecated
        - only for backwards compatibility, use Registry.get(NamespacedKey) instead.
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

        Deprecated
        - only for backwards compatibility, use Registry.get(NamespacedKey) instead.
        """
        ...


    @staticmethod
    def values() -> list["PotionEffectType"]:
        """
        Returns
        - an array of all known PotionEffectTypes.

        Deprecated
        - use Registry.iterator().
        """
        ...
