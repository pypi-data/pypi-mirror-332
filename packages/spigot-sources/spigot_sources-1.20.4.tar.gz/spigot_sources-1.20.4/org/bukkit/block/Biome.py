"""
Python module generated from Java source file org.bukkit.block.Biome

Java source file obtained from artifact spigot-api version 1.20.4-R0.1-20240423.152506-123

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from java.util import Locale
from org.bukkit import Keyed
from org.bukkit import NamespacedKey
from org.bukkit.block import *
from typing import Any, Callable, Iterable, Tuple


class Biome(Enum):
    """
    Holds all accepted Biomes in the default server
    """

    OCEAN = 0
    PLAINS = 1
    DESERT = 2
    WINDSWEPT_HILLS = 3
    FOREST = 4
    TAIGA = 5
    SWAMP = 6
    MANGROVE_SWAMP = 7
    RIVER = 8
    NETHER_WASTES = 9
    THE_END = 10
    FROZEN_OCEAN = 11
    FROZEN_RIVER = 12
    SNOWY_PLAINS = 13
    MUSHROOM_FIELDS = 14
    BEACH = 15
    JUNGLE = 16
    SPARSE_JUNGLE = 17
    DEEP_OCEAN = 18
    STONY_SHORE = 19
    SNOWY_BEACH = 20
    BIRCH_FOREST = 21
    DARK_FOREST = 22
    SNOWY_TAIGA = 23
    OLD_GROWTH_PINE_TAIGA = 24
    WINDSWEPT_FOREST = 25
    SAVANNA = 26
    SAVANNA_PLATEAU = 27
    BADLANDS = 28
    WOODED_BADLANDS = 29
    SMALL_END_ISLANDS = 30
    END_MIDLANDS = 31
    END_HIGHLANDS = 32
    END_BARRENS = 33
    WARM_OCEAN = 34
    LUKEWARM_OCEAN = 35
    COLD_OCEAN = 36
    DEEP_LUKEWARM_OCEAN = 37
    DEEP_COLD_OCEAN = 38
    DEEP_FROZEN_OCEAN = 39
    THE_VOID = 40
    SUNFLOWER_PLAINS = 41
    WINDSWEPT_GRAVELLY_HILLS = 42
    FLOWER_FOREST = 43
    ICE_SPIKES = 44
    OLD_GROWTH_BIRCH_FOREST = 45
    OLD_GROWTH_SPRUCE_TAIGA = 46
    WINDSWEPT_SAVANNA = 47
    ERODED_BADLANDS = 48
    BAMBOO_JUNGLE = 49
    SOUL_SAND_VALLEY = 50
    CRIMSON_FOREST = 51
    WARPED_FOREST = 52
    BASALT_DELTAS = 53
    DRIPSTONE_CAVES = 54
    LUSH_CAVES = 55
    DEEP_DARK = 56
    MEADOW = 57
    GROVE = 58
    SNOWY_SLOPES = 59
    FROZEN_PEAKS = 60
    JAGGED_PEAKS = 61
    STONY_PEAKS = 62
    CHERRY_GROVE = 63
    CUSTOM = 64
    """
    Represents a custom Biome
    """


    def getKey(self) -> "NamespacedKey":
        ...
