"""
Python module generated from Java source file org.bukkit.entity.SpawnCategory

Java source file obtained from artifact spigot-api version 1.19.4-R0.1-20230607.155743-88

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit.entity import *
from typing import Any, Callable, Iterable, Tuple


class SpawnCategory(Enum):
    """
    Represents groups of entities with shared spawn behaviors and mob caps.

    See
    - <a href="https://minecraft.fandom.com/wiki/Spawn.Java_Edition_mob_cap">Minecraft Wiki</a>
    """

    MONSTER = 0
    """
    Entities related to Monsters, eg: Witch, Zombie, Creeper, etc.
    """
    ANIMAL = 1
    """
    Entities related to Animals, eg: Strider, Cow, Turtle, etc.
    """
    WATER_ANIMAL = 2
    """
    Entities related to Water Animals, eg: Squid or Dolphin.
    """
    WATER_AMBIENT = 3
    """
    Entities related to Water Ambient, eg: Cod, PufferFish, Tropical Fish,
    Salmon, etc.
    """
    WATER_UNDERGROUND_CREATURE = 4
    """
    Entities related to Water Underground, eg: Glow Squid.
    """
    AMBIENT = 5
    """
    Entities related to Ambient, eg: Bat.
    """
    AXOLOTL = 6
    """
    All the Axolotl are represented by this Category.
    """
    MISC = 7
    """
    Entities not related to a mob, eg: Player, ArmorStand, Boat, etc.
    """
