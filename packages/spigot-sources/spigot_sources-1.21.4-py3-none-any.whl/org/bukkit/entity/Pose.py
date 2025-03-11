"""
Python module generated from Java source file org.bukkit.entity.Pose

Java source file obtained from artifact spigot-api version 1.21.4-R0.1-20250303.102353-42

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
    CROAKING = 8
    """
    Entity is croaking.
    """
    USING_TONGUE = 9
    """
    Entity is using its tongue.
    """
    SITTING = 10
    """
    Entity is sitting.
    """
    ROARING = 11
    """
    Entity is roaring.
    """
    SNIFFING = 12
    """
    Entity is sniffing.
    """
    EMERGING = 13
    """
    Entity is emerging.
    """
    DIGGING = 14
    """
    Entity is digging.
    """
    SLIDING = 15
    """
    Entity is sliding.
    """
    SHOOTING = 16
    """
    Entity is shooting.
    """
    INHALING = 17
    """
    Entity is inhaling.
    """
