"""
Python module generated from Java source file org.bukkit.block.Biome

Java source file obtained from artifact spigot-api version 1.18.2-R0.1-20220607.160742-53

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
    RIVER = 7
    NETHER_WASTES = 8
    THE_END = 9
    FROZEN_OCEAN = 10
    FROZEN_RIVER = 11
    SNOWY_PLAINS = 12
    MUSHROOM_FIELDS = 13
    BEACH = 14
    JUNGLE = 15
    SPARSE_JUNGLE = 16
    DEEP_OCEAN = 17
    STONY_SHORE = 18
    SNOWY_BEACH = 19
    BIRCH_FOREST = 20
    DARK_FOREST = 21
    SNOWY_TAIGA = 22
    OLD_GROWTH_PINE_TAIGA = 23
    WINDSWEPT_FOREST = 24
    SAVANNA = 25
    SAVANNA_PLATEAU = 26
    BADLANDS = 27
    WOODED_BADLANDS = 28
    SMALL_END_ISLANDS = 29
    END_MIDLANDS = 30
    END_HIGHLANDS = 31
    END_BARRENS = 32
    WARM_OCEAN = 33
    LUKEWARM_OCEAN = 34
    COLD_OCEAN = 35
    DEEP_LUKEWARM_OCEAN = 36
    DEEP_COLD_OCEAN = 37
    DEEP_FROZEN_OCEAN = 38
    THE_VOID = 39
    SUNFLOWER_PLAINS = 40
    WINDSWEPT_GRAVELLY_HILLS = 41
    FLOWER_FOREST = 42
    ICE_SPIKES = 43
    OLD_GROWTH_BIRCH_FOREST = 44
    OLD_GROWTH_SPRUCE_TAIGA = 45
    WINDSWEPT_SAVANNA = 46
    ERODED_BADLANDS = 47
    BAMBOO_JUNGLE = 48
    SOUL_SAND_VALLEY = 49
    CRIMSON_FOREST = 50
    WARPED_FOREST = 51
    BASALT_DELTAS = 52
    DRIPSTONE_CAVES = 53
    LUSH_CAVES = 54
    MEADOW = 55
    GROVE = 56
    SNOWY_SLOPES = 57
    FROZEN_PEAKS = 58
    JAGGED_PEAKS = 59
    STONY_PEAKS = 60
    CUSTOM = 61
    """
    Represents a custom Biome
    """


    def getKey(self) -> "NamespacedKey":
        ...
