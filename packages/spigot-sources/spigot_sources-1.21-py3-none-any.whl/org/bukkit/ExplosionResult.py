"""
Python module generated from Java source file org.bukkit.ExplosionResult

Java source file obtained from artifact spigot-api version 1.21-R0.1-20240807.214924-87

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit import *
from typing import Any, Callable, Iterable, Tuple


class ExplosionResult(Enum):
    """
    Represents the outcome of an explosion.
    """

    KEEP = 0
    """
    Represents an explosion where no change took place.
    
    This is the case when org.bukkit.GameRule.MOB_GRIEFING is
    disabled.
    """
    DESTROY = 1
    """
    Represents an explosion where all destroyed blocks drop their items.
    
    This is the case when
    org.bukkit.GameRule.TNT_EXPLOSION_DROP_DECAY or
    org.bukkit.GameRule.BLOCK_EXPLOSION_DROP_DECAY is disabled.
    """
    DESTROY_WITH_DECAY = 2
    """
    Represents an explosion where explosions cause only some blocks to drop.
    """
    TRIGGER_BLOCK = 3
    """
    Represents an explosion where a block change/update has happened.
    
    For example, when a wind charge is used it will cause nearby buttons,
    levers and bells to be activated.
    """
