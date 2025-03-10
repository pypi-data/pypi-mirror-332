"""
Python module generated from Java source file org.bukkit.entity.Pose

Java source file obtained from artifact spigot-api version 1.17.1-R0.1-20211121.234319-104

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit.entity import *
from typing import Any, Callable, Iterable, Tuple


class Pose(Enum):
    """
    Represents an entity body pose.
    """

    STANDING = 0
    """
    Entity is standing normally.
    """
    FALL_FLYING = 1
    """
    Entity is gliding.
    """
    SLEEPING = 2
    """
    Entity is sleeping.
    """
    SWIMMING = 3
    """
    Entity is swimming.
    """
    SPIN_ATTACK = 4
    """
    Entity is riptiding with a trident.
    """
    SNEAKING = 5
    """
    Entity is sneaking.
    """
    LONG_JUMPING = 6
    """
    Entity is long jumping.
    """
    DYING = 7
    """
    Entity is dead.
    """
