"""
Python module generated from Java source file org.bukkit.block.Biome

Java source file obtained from artifact spigot-api version 1.21.3-R0.1-20241203.162251-46

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.base import Preconditions
from com.google.common.collect import Lists
from java.util import Locale
from org.bukkit import Bukkit
from org.bukkit import FeatureFlag
from org.bukkit import Keyed
from org.bukkit import MinecraftExperimental
from org.bukkit import NamespacedKey
from org.bukkit import Registry
from org.bukkit.block import *
from org.bukkit.packs import DataPack
from org.bukkit.util import OldEnum
from typing import Any, Callable, Iterable, Tuple


class Biome(OldEnum, Keyed):
    """
    Holds all accepted Biomes in the server.
    
    The Biomes listed in this interface are present in the default server
    or can be enabled via a FeatureFlag.
    There may be additional biomes present in the server, for example from a DataPack
    which can be accessed via Registry.BIOME.
    """

    OCEAN = getBiome("ocean")
    PLAINS = getBiome("plains")
    DESERT = getBiome("desert")
    WINDSWEPT_HILLS = getBiome("windswept_hills")
    FOREST = getBiome("forest")
    TAIGA = getBiome("taiga")
    SWAMP = getBiome("swamp")
    MANGROVE_SWAMP = getBiome("mangrove_swamp")
    RIVER = getBiome("river")
    NETHER_WASTES = getBiome("nether_wastes")
    THE_END = getBiome("the_end")
    FROZEN_OCEAN = getBiome("frozen_ocean")
    FROZEN_RIVER = getBiome("frozen_river")
    SNOWY_PLAINS = getBiome("snowy_plains")
    MUSHROOM_FIELDS = getBiome("mushroom_fields")
    BEACH = getBiome("beach")
    JUNGLE = getBiome("jungle")
    SPARSE_JUNGLE = getBiome("sparse_jungle")
    DEEP_OCEAN = getBiome("deep_ocean")
    STONY_SHORE = getBiome("stony_shore")
    SNOWY_BEACH = getBiome("snowy_beach")
    BIRCH_FOREST = getBiome("birch_forest")
    DARK_FOREST = getBiome("dark_forest")
    SNOWY_TAIGA = getBiome("snowy_taiga")
    OLD_GROWTH_PINE_TAIGA = getBiome("old_growth_pine_taiga")
    WINDSWEPT_FOREST = getBiome("windswept_forest")
    SAVANNA = getBiome("savanna")
    SAVANNA_PLATEAU = getBiome("savanna_plateau")
    BADLANDS = getBiome("badlands")
    WOODED_BADLANDS = getBiome("wooded_badlands")
    SMALL_END_ISLANDS = getBiome("small_end_islands")
    END_MIDLANDS = getBiome("end_midlands")
    END_HIGHLANDS = getBiome("end_highlands")
    END_BARRENS = getBiome("end_barrens")
    WARM_OCEAN = getBiome("warm_ocean")
    LUKEWARM_OCEAN = getBiome("lukewarm_ocean")
    COLD_OCEAN = getBiome("cold_ocean")
    DEEP_LUKEWARM_OCEAN = getBiome("deep_lukewarm_ocean")
    DEEP_COLD_OCEAN = getBiome("deep_cold_ocean")
    DEEP_FROZEN_OCEAN = getBiome("deep_frozen_ocean")
    THE_VOID = getBiome("the_void")
    SUNFLOWER_PLAINS = getBiome("sunflower_plains")
    WINDSWEPT_GRAVELLY_HILLS = getBiome("windswept_gravelly_hills")
    FLOWER_FOREST = getBiome("flower_forest")
    ICE_SPIKES = getBiome("ice_spikes")
    OLD_GROWTH_BIRCH_FOREST = getBiome("old_growth_birch_forest")
    OLD_GROWTH_SPRUCE_TAIGA = getBiome("old_growth_spruce_taiga")
    WINDSWEPT_SAVANNA = getBiome("windswept_savanna")
    ERODED_BADLANDS = getBiome("eroded_badlands")
    BAMBOO_JUNGLE = getBiome("bamboo_jungle")
    SOUL_SAND_VALLEY = getBiome("soul_sand_valley")
    CRIMSON_FOREST = getBiome("crimson_forest")
    WARPED_FOREST = getBiome("warped_forest")
    BASALT_DELTAS = getBiome("basalt_deltas")
    DRIPSTONE_CAVES = getBiome("dripstone_caves")
    LUSH_CAVES = getBiome("lush_caves")
    DEEP_DARK = getBiome("deep_dark")
    MEADOW = getBiome("meadow")
    GROVE = getBiome("grove")
    SNOWY_SLOPES = getBiome("snowy_slopes")
    FROZEN_PEAKS = getBiome("frozen_peaks")
    JAGGED_PEAKS = getBiome("jagged_peaks")
    STONY_PEAKS = getBiome("stony_peaks")
    CHERRY_GROVE = getBiome("cherry_grove")
    PALE_GARDEN = Registry.BIOME.get(NamespacedKey.minecraft("pale_garden"))
    CUSTOM = Bukkit.getUnsafe().getCustomBiome()
    """
    Represents a custom Biome

    Deprecated
    - Biome is no longer an enum, custom biomes will have their own biome instance.
    """


    @staticmethod
    def getBiome(key: str) -> "Biome":
        ...


    @staticmethod
    def valueOf(name: str) -> "Biome":
        """
        Arguments
        - name: of the biome.

        Returns
        - the biome with the given name.

        Deprecated
        - only for backwards compatibility, use Registry.get(NamespacedKey) instead.
        """
        ...


    @staticmethod
    def values() -> list["Biome"]:
        """
        Returns
        - an array of all known biomes.

        Deprecated
        - use Registry.iterator().
        """
        ...
