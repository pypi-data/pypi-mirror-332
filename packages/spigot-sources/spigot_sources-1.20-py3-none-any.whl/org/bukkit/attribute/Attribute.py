"""
Python module generated from Java source file org.bukkit.attribute.Attribute

Java source file obtained from artifact spigot-api version 1.20-R0.1-20230612.113428-32

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit import Keyed
from org.bukkit import NamespacedKey
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
    GENERIC_LUCK = ("generic.luck")
    """
    Luck bonus of an Entity.
    """
    HORSE_JUMP_STRENGTH = ("horse.jump_strength")
    """
    Strength with which a horse will jump.
    """
    ZOMBIE_SPAWN_REINFORCEMENTS = ("zombie.spawn_reinforcements")
    """
    Chance of a zombie to spawn reinforcements.
    """


    def getKey(self) -> "NamespacedKey":
        ...
