"""
Python module generated from Java source file org.bukkit.block.Biome

Java source file obtained from artifact spigot-api version 1.17.1-R0.1-20211121.234319-104

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
    MOUNTAINS = 3
    FOREST = 4
    TAIGA = 5
    SWAMP = 6
    RIVER = 7
    NETHER_WASTES = 8
    THE_END = 9
    FROZEN_OCEAN = 10
    FROZEN_RIVER = 11
    SNOWY_TUNDRA = 12
    SNOWY_MOUNTAINS = 13
    MUSHROOM_FIELDS = 14
    MUSHROOM_FIELD_SHORE = 15
    BEACH = 16
    DESERT_HILLS = 17
    WOODED_HILLS = 18
    TAIGA_HILLS = 19
    MOUNTAIN_EDGE = 20
    JUNGLE = 21
    JUNGLE_HILLS = 22
    JUNGLE_EDGE = 23
    DEEP_OCEAN = 24
    STONE_SHORE = 25
    SNOWY_BEACH = 26
    BIRCH_FOREST = 27
    BIRCH_FOREST_HILLS = 28
    DARK_FOREST = 29
    SNOWY_TAIGA = 30
    SNOWY_TAIGA_HILLS = 31
    GIANT_TREE_TAIGA = 32
    GIANT_TREE_TAIGA_HILLS = 33
    WOODED_MOUNTAINS = 34
    SAVANNA = 35
    SAVANNA_PLATEAU = 36
    BADLANDS = 37
    WOODED_BADLANDS_PLATEAU = 38
    BADLANDS_PLATEAU = 39
    SMALL_END_ISLANDS = 40
    END_MIDLANDS = 41
    END_HIGHLANDS = 42
    END_BARRENS = 43
    WARM_OCEAN = 44
    LUKEWARM_OCEAN = 45
    COLD_OCEAN = 46
    DEEP_WARM_OCEAN = 47
    DEEP_LUKEWARM_OCEAN = 48
    DEEP_COLD_OCEAN = 49
    DEEP_FROZEN_OCEAN = 50
    THE_VOID = 51
    SUNFLOWER_PLAINS = 52
    DESERT_LAKES = 53
    GRAVELLY_MOUNTAINS = 54
    FLOWER_FOREST = 55
    TAIGA_MOUNTAINS = 56
    SWAMP_HILLS = 57
    ICE_SPIKES = 58
    MODIFIED_JUNGLE = 59
    MODIFIED_JUNGLE_EDGE = 60
    TALL_BIRCH_FOREST = 61
    TALL_BIRCH_HILLS = 62
    DARK_FOREST_HILLS = 63
    SNOWY_TAIGA_MOUNTAINS = 64
    GIANT_SPRUCE_TAIGA = 65
    GIANT_SPRUCE_TAIGA_HILLS = 66
    MODIFIED_GRAVELLY_MOUNTAINS = 67
    SHATTERED_SAVANNA = 68
    SHATTERED_SAVANNA_PLATEAU = 69
    ERODED_BADLANDS = 70
    MODIFIED_WOODED_BADLANDS_PLATEAU = 71
    MODIFIED_BADLANDS_PLATEAU = 72
    BAMBOO_JUNGLE = 73
    BAMBOO_JUNGLE_HILLS = 74
    SOUL_SAND_VALLEY = 75
    CRIMSON_FOREST = 76
    WARPED_FOREST = 77
    BASALT_DELTAS = 78
    DRIPSTONE_CAVES = 79
    LUSH_CAVES = 80
    CUSTOM = 81
    """
    Represents a custom Biome
    """


    def getKey(self) -> "NamespacedKey":
        ...
