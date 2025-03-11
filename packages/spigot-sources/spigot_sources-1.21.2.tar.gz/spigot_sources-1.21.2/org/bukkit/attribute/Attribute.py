"""
Python module generated from Java source file org.bukkit.attribute.Attribute

Java source file obtained from artifact spigot-api version 1.21.2-R0.1-20241023.084343-5

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

    GENERIC_MAX_HEALTH = ("max_health")
    """
    Maximum health of an Entity.
    """
    GENERIC_FOLLOW_RANGE = ("follow_range")
    """
    Range at which an Entity will follow others.
    """
    GENERIC_KNOCKBACK_RESISTANCE = ("knockback_resistance")
    """
    Resistance of an Entity to knockback.
    """
    GENERIC_MOVEMENT_SPEED = ("movement_speed")
    """
    Movement speed of an Entity.
    """
    GENERIC_FLYING_SPEED = ("flying_speed")
    """
    Flying speed of an Entity.
    """
    GENERIC_ATTACK_DAMAGE = ("attack_damage")
    """
    Attack damage of an Entity.
    """
    GENERIC_ATTACK_KNOCKBACK = ("attack_knockback")
    """
    Attack knockback of an Entity.
    """
    GENERIC_ATTACK_SPEED = ("attack_speed")
    """
    Attack speed of an Entity.
    """
    GENERIC_ARMOR = ("armor")
    """
    Armor bonus of an Entity.
    """
    GENERIC_ARMOR_TOUGHNESS = ("armor_toughness")
    """
    Armor durability bonus of an Entity.
    """
    GENERIC_FALL_DAMAGE_MULTIPLIER = ("fall_damage_multiplier")
    """
    The fall damage multiplier of an Entity.
    """
    GENERIC_LUCK = ("luck")
    """
    Luck bonus of an Entity.
    """
    GENERIC_MAX_ABSORPTION = ("max_absorption")
    """
    Maximum absorption of an Entity.
    """
    GENERIC_SAFE_FALL_DISTANCE = ("safe_fall_distance")
    """
    The distance which an Entity can fall without damage.
    """
    GENERIC_SCALE = ("scale")
    """
    The relative scale of an Entity.
    """
    GENERIC_STEP_HEIGHT = ("step_height")
    """
    The height which an Entity can walk over.
    """
    GENERIC_GRAVITY = ("gravity")
    """
    The gravity applied to an Entity.
    """
    GENERIC_JUMP_STRENGTH = ("jump_strength")
    """
    Strength with which an Entity will jump.
    """
    GENERIC_BURNING_TIME = ("burning_time")
    """
    How long an entity remains burning after ingition.
    """
    GENERIC_EXPLOSION_KNOCKBACK_RESISTANCE = ("explosion_knockback_resistance")
    """
    Resistance to knockback from explosions.
    """
    GENERIC_MOVEMENT_EFFICIENCY = ("movement_efficiency")
    """
    Movement speed through difficult terrain.
    """
    GENERIC_OXYGEN_BONUS = ("oxygen_bonus")
    """
    Oxygen use underwater.
    """
    GENERIC_WATER_MOVEMENT_EFFICIENCY = ("water_movement_efficiency")
    """
    Movement speed through water.
    """
    GENERIC_TEMPT_RANGE = ("tempt_range")
    """
    Range at which mobs will be tempted by items.
    """
    PLAYER_BLOCK_INTERACTION_RANGE = ("block_interaction_range")
    """
    The block reach distance of a Player.
    """
    PLAYER_ENTITY_INTERACTION_RANGE = ("entity_interaction_range")
    """
    The entity reach distance of a Player.
    """
    PLAYER_BLOCK_BREAK_SPEED = ("block_break_speed")
    """
    Block break speed of a Player.
    """
    PLAYER_MINING_EFFICIENCY = ("mining_efficiency")
    """
    Mining speed for correct tools.
    """
    PLAYER_SNEAKING_SPEED = ("sneaking_speed")
    """
    Sneaking speed.
    """
    PLAYER_SUBMERGED_MINING_SPEED = ("submerged_mining_speed")
    """
    Underwater mining speed.
    """
    PLAYER_SWEEPING_DAMAGE_RATIO = ("sweeping_damage_ratio")
    """
    Sweeping damage.
    """
    ZOMBIE_SPAWN_REINFORCEMENTS = ("spawn_reinforcements")
    """
    Chance of a zombie to spawn reinforcements.
    """


    def getKey(self) -> "NamespacedKey":
        ...


    def getTranslationKey(self) -> str:
        ...
