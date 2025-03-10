"""
Python module generated from Java source file org.bukkit.attribute.Attribute

Java source file obtained from artifact spigot-api version 1.20.5-R0.1-20240429.101539-37

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit import Bukkit
from org.bukkit import Keyed
from org.bukkit import NamespacedKey
from org.bukkit import Translatable
from org.bukkit.attribute import *
from typing import Any, Callable, Iterable, Tuple


class Attribute(Enum):
    """
    Types of attributes which may be present on an Attributable.
    """

    GENERIC_MAX_HEALTH = ("generic.max_health")
    """
    Maximum health of an Entity.
    """
    GENERIC_FOLLOW_RANGE = ("generic.follow_range")
    """
    Range at which an Entity will follow others.
    """
    GENERIC_KNOCKBACK_RESISTANCE = ("generic.knockback_resistance")
    """
    Resistance of an Entity to knockback.
    """
    GENERIC_MOVEMENT_SPEED = ("generic.movement_speed")
    """
    Movement speed of an Entity.
    """
    GENERIC_FLYING_SPEED = ("generic.flying_speed")
    """
    Flying speed of an Entity.
    """
    GENERIC_ATTACK_DAMAGE = ("generic.attack_damage")
    """
    Attack damage of an Entity.
    """
    GENERIC_ATTACK_KNOCKBACK = ("generic.attack_knockback")
    """
    Attack knockback of an Entity.
    """
    GENERIC_ATTACK_SPEED = ("generic.attack_speed")
    """
    Attack speed of an Entity.
    """
    GENERIC_ARMOR = ("generic.armor")
    """
    Armor bonus of an Entity.
    """
    GENERIC_ARMOR_TOUGHNESS = ("generic.armor_toughness")
    """
    Armor durability bonus of an Entity.
    """
    GENERIC_FALL_DAMAGE_MULTIPLIER = ("generic.fall_damage_multiplier")
    """
    The fall damage multiplier of an Entity.
    """
    GENERIC_LUCK = ("generic.luck")
    """
    Luck bonus of an Entity.
    """
    GENERIC_MAX_ABSORPTION = ("generic.max_absorption")
    """
    Maximum absorption of an Entity.
    """
    GENERIC_SAFE_FALL_DISTANCE = ("generic.safe_fall_distance")
    """
    The distance which an Entity can fall without damage.
    """
    GENERIC_SCALE = ("generic.scale")
    """
    The relative scale of an Entity.
    """
    GENERIC_STEP_HEIGHT = ("generic.step_height")
    """
    The height which an Entity can walk over.
    """
    GENERIC_GRAVITY = ("generic.gravity")
    """
    The gravity applied to an Entity.
    """
    GENERIC_JUMP_STRENGTH = ("generic.jump_strength")
    """
    Strength with which an Entity will jump.
    """
    PLAYER_BLOCK_INTERACTION_RANGE = ("player.block_interaction_range")
    """
    The block reach distance of a Player.
    """
    PLAYER_ENTITY_INTERACTION_RANGE = ("player.entity_interaction_range")
    """
    The entity reach distance of a Player.
    """
    PLAYER_BLOCK_BREAK_SPEED = ("player.block_break_speed")
    """
    Block break speed of a Player.
    """
    ZOMBIE_SPAWN_REINFORCEMENTS = ("zombie.spawn_reinforcements")
    """
    Chance of a zombie to spawn reinforcements.
    """


    def getKey(self) -> "NamespacedKey":
        ...


    def getTranslationKey(self) -> str:
        ...
