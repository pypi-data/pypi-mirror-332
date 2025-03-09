"""
Python module generated from Java source file org.bukkit.damage.DamageScaling

Java source file obtained from artifact spigot-api version 1.20.6-R0.1-20240613.150924-57

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit.damage import *
from org.bukkit.entity import Player
from typing import Any, Callable, Iterable, Tuple


class DamageScaling(Enum):
    """
    A means of damage scaling with respect to the server's difficulty.
    """

    NEVER = 0
    """
    Damage is not scaled.
    """
    WHEN_CAUSED_BY_LIVING_NON_PLAYER = 1
    """
    Damage is scaled only when the
    DamageSource.getCausingEntity() causing entity is not a
    Player.
    """
    ALWAYS = 2
    """
    Damage is always scaled.
    """
