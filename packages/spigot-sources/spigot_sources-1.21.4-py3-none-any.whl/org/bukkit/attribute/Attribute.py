"""
Python module generated from Java source file org.bukkit.attribute.Attribute

Java source file obtained from artifact spigot-api version 1.21.4-R0.1-20250303.102353-42

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.base import Preconditions
from com.google.common.collect import Lists
from java.util import Locale
from org.bukkit import Bukkit
from org.bukkit import Keyed
from org.bukkit import NamespacedKey
from org.bukkit import Registry
from org.bukkit import Translatable
from org.bukkit.attribute import *
from org.bukkit.registry import RegistryAware
from org.bukkit.util import OldEnum
from typing import Any, Callable, Iterable, Tuple


class Attribute(OldEnum, Keyed, Translatable, RegistryAware):
    """
    Types of attributes which may be present on an Attributable.
    """

    MAX_HEALTH = getAttribute("max_health")
    """
    Maximum health of an Entity.
    """
    FOLLOW_RANGE = getAttribute("follow_range")
    """
    Range at which an Entity will follow others.
    """
    KNOCKBACK_RESISTANCE = getAttribute("knockback_resistance")
    """
    Resistance of an Entity to knockback.
    """
    MOVEMENT_SPEED = getAttribute("movement_speed")
    """
    Movement speed of an Entity.
    """
    FLYING_SPEED = getAttribute("flying_speed")
    """
    Flying speed of an Entity.
    """
    ATTACK_DAMAGE = getAttribute("attack_damage")
    """
    Attack damage of an Entity.
    """
    ATTACK_KNOCKBACK = getAttribute("attack_knockback")
    """
    Attack knockback of an Entity.
    """
    ATTACK_SPEED = getAttribute("attack_speed")
    """
    Attack speed of an Entity.
    """
    ARMOR = getAttribute("armor")
    """
    Armor bonus of an Entity.
    """
    ARMOR_TOUGHNESS = getAttribute("armor_toughness")
    """
    Armor durability bonus of an Entity.
    """
    FALL_DAMAGE_MULTIPLIER = getAttribute("fall_damage_multiplier")
    """
    The fall damage multiplier of an Entity.
    """
    LUCK = getAttribute("luck")
    """
    Luck bonus of an Entity.
    """
    MAX_ABSORPTION = getAttribute("max_absorption")
    """
    Maximum absorption of an Entity.
    """
    SAFE_FALL_DISTANCE = getAttribute("safe_fall_distance")
    """
    The distance which an Entity can fall without damage.
    """
    SCALE = getAttribute("scale")
    """
    The relative scale of an Entity.
    """
    STEP_HEIGHT = getAttribute("step_height")
    """
    The height which an Entity can walk over.
    """
    GRAVITY = getAttribute("gravity")
    """
    The gravity applied to an Entity.
    """
    JUMP_STRENGTH = getAttribute("jump_strength")
    """
    Strength with which an Entity will jump.
    """
    BURNING_TIME = getAttribute("burning_time")
    """
    How long an entity remains burning after ignition.
    """
    EXPLOSION_KNOCKBACK_RESISTANCE = getAttribute("explosion_knockback_resistance")
    """
    Resistance to knockback from explosions.
    """
    MOVEMENT_EFFICIENCY = getAttribute("movement_efficiency")
    """
    Movement speed through difficult terrain.
    """
    OXYGEN_BONUS = getAttribute("oxygen_bonus")
    """
    Oxygen use underwater.
    """
    WATER_MOVEMENT_EFFICIENCY = getAttribute("water_movement_efficiency")
    """
    Movement speed through water.
    """
    TEMPT_RANGE = getAttribute("tempt_range")
    """
    Range at which mobs will be tempted by items.
    """
    BLOCK_INTERACTION_RANGE = getAttribute("block_interaction_range")
    """
    The block reach distance of a Player.
    """
    ENTITY_INTERACTION_RANGE = getAttribute("entity_interaction_range")
    """
    The entity reach distance of a Player.
    """
    BLOCK_BREAK_SPEED = getAttribute("block_break_speed")
    """
    Block break speed of a Player.
    """
    MINING_EFFICIENCY = getAttribute("mining_efficiency")
    """
    Mining speed for correct tools.
    """
    SNEAKING_SPEED = getAttribute("sneaking_speed")
    """
    Sneaking speed.
    """
    SUBMERGED_MINING_SPEED = getAttribute("submerged_mining_speed")
    """
    Underwater mining speed.
    """
    SWEEPING_DAMAGE_RATIO = getAttribute("sweeping_damage_ratio")
    """
    Sweeping damage.
    """
    SPAWN_REINFORCEMENTS = getAttribute("spawn_reinforcements")
    """
    Chance of a zombie to spawn reinforcements.
    """


    @staticmethod
    def getAttribute(key: str) -> "Attribute":
        ...


    def getKey(self) -> "NamespacedKey":
        """
        See
        - .isRegistered()

        Deprecated
        - A key might not always be present, use .getKeyOrThrow() instead.
        """
        ...


    @staticmethod
    def valueOf(name: str) -> "Attribute":
        """
        Arguments
        - name: of the attribute.

        Returns
        - the attribute with the given name.

        Deprecated
        - only for backwards compatibility, use Registry.get(NamespacedKey) instead.
        """
        ...


    @staticmethod
    def values() -> list["Attribute"]:
        """
        Returns
        - an array of all known attributes.

        Deprecated
        - use Registry.iterator().
        """
        ...
