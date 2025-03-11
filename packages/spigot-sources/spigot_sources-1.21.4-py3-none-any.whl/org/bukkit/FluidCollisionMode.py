"""
Python module generated from Java source file org.bukkit.FluidCollisionMode

Java source file obtained from artifact spigot-api version 1.21.4-R0.1-20250303.102353-42

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit import *
from typing import Any, Callable, Iterable, Tuple


class FluidCollisionMode(Enum):
    """
    Determines the collision behavior when fluids get hit during ray tracing.
    """

    NEVER = 0
    """
    Ignore fluids.
    """
    SOURCE_ONLY = 1
    """
    Only collide with source fluid blocks.
    """
    ALWAYS = 2
    """
    Collide with all fluids.
    """
