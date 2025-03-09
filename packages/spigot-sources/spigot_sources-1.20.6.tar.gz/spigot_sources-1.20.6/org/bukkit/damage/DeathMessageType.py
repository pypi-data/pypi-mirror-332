"""
Python module generated from Java source file org.bukkit.damage.DeathMessageType

Java source file obtained from artifact spigot-api version 1.20.6-R0.1-20240613.150924-57

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit.damage import *
from typing import Any, Callable, Iterable, Tuple


class DeathMessageType(Enum):
    """
    Represents a type of death message used by a DamageSource.
    """

    DEFAULT = 0
    """
    No special death message logic is applied.
    """
    FALL_VARIANTS = 1
    """
    Shows a variant of fall damage death instead of a regular death message.
    
    **Example:** death.fell.assist.item
    """
    INTENTIONAL_GAME_DESIGN = 2
    """
    Shows the intentional game design death message instead of a regular
    death message.
    """
