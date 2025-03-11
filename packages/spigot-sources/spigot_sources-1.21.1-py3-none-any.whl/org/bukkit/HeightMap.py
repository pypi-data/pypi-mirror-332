"""
Python module generated from Java source file org.bukkit.HeightMap

Java source file obtained from artifact spigot-api version 1.21.1-R0.1-20241022.152140-54

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit import *
from typing import Any, Callable, Iterable, Tuple


class HeightMap(Enum):
    """
    Further information regarding heightmaps.

    See
    - <a href="https://minecraft.wiki/w/Chunk_format">Minecraft Wiki</a>
    """

    MOTION_BLOCKING = 0
    """
    The highest block that blocks motion or contains a fluid.
    """
    MOTION_BLOCKING_NO_LEAVES = 1
    """
    The highest block that blocks motion or contains a fluid or is in the
    Tag.LEAVES.
    """
    OCEAN_FLOOR = 2
    """
    The highest non-air block, solid block.
    """
    OCEAN_FLOOR_WG = 3
    """
    The highest block that is neither air nor contains a fluid, for worldgen.
    """
    WORLD_SURFACE = 4
    """
    The highest non-air block.
    """
    WORLD_SURFACE_WG = 5
    """
    The highest non-air block, for worldgen.
    """
