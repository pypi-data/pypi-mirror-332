"""
Python module generated from Java source file org.bukkit.StructureType

Java source file obtained from artifact spigot-api version 1.21.2-R0.1-20241023.084343-5

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.base import Preconditions
from com.google.common.base import Strings
from com.google.common.collect import ImmutableMap
from java.util import Objects
from org.bukkit import *
from org.bukkit.map import MapCursor
from typing import Any, Callable, Iterable, Tuple


class StructureType(Keyed):

    MINESHAFT = register(StructureType("mineshaft", MapCursor.Type.RED_X))
    """
    Mineshafts are underground structures which consist of branching mining
    tunnels with wooden supports and broken rails.
    
    They are the only place where cave spider spawners and minecarts with
    chests can be found naturally.
    """
    VILLAGE = register(StructureType("village", MapCursor.Type.MANSION))
    """
    Villages are naturally generating structures that form above ground.
    
    They are usually generated in desert, plains, taiga, and savanna biomes
    and are a site for villager spawns, with whom the player can trade.
    """
    NETHER_FORTRESS = register(StructureType("fortress", MapCursor.Type.RED_X))
    """
    Nether fortresses are very large complexes that mainly consist of
    netherbricks.
    
    They contain blaze spawners, nether wart farms, and loot chests. They are
    only generated in the nether dimension.
    """
    STRONGHOLD = register(StructureType("stronghold", MapCursor.Type.MANSION))
    """
    Strongholds are underground structures that consist of many rooms,
    libraries, and an end portal room.
    
    They can be found using an Material.ENDER_EYE.
    """
    JUNGLE_PYRAMID = register(StructureType("jungle_pyramid", MapCursor.Type.RED_X))
    """
    Jungle pyramids (also known as jungle temples) are found in jungles.
    
    They are usually composed of cobblestone and mossy cobblestone. They
    consist of three floors, with the bottom floor containing treasure
    chests.
    """
    OCEAN_RUIN = register(StructureType("ocean_ruin", MapCursor.Type.MONUMENT))
    """
    Ocean ruins are clusters of many different blocks that generate
    underwater in ocean biomes (as well as on the surface of beaches).
    
    They come in my different variations. The cold variants consist primarily
    of stone brick, and the warm variants consist of sandstone.
    """
    DESERT_PYRAMID = register(StructureType("desert_pyramid", MapCursor.Type.RED_X))
    """
    Desert pyramids (also known as desert temples) are found in deserts.
    
    They are usually composed of sandstone and stained terracotta.
    """
    IGLOO = register(StructureType("igloo", MapCursor.Type.RED_X))
    """
    Igloos are structures that generate in snowy biomes.
    
    They consist of the house, as well as a basement.
    """
    SWAMP_HUT = register(StructureType("swamp_hut", MapCursor.Type.RED_X))
    """
    Swamp huts (also known as witch huts) generate in swamp biomes and have
    the ability to spawn witches.
    """
    OCEAN_MONUMENT = register(StructureType("monument", MapCursor.Type.MONUMENT))
    """
    Ocean monuments are underwater structures.
    
    They are usually composed on all three different prismarine types and sea
    lanterns. They are the only place guardians and elder guardians spawn
    naturally.
    """
    END_CITY = register(StructureType("end_city", MapCursor.Type.RED_X))
    """
    End Cities are tall castle-like structures that generate in the outer
    island of the End dimension.
    
    They consist primarily of end stone bricks, purpur blocks, and end rods.
    They are the only place where shulkers can be found.
    """
    WOODLAND_MANSION = register(StructureType("mansion", MapCursor.Type.MANSION))
    """
    Mansions (also known as woodland mansions) are massive house structures
    that generate in dark forests, containing a wide variety of rooms.
    
    They are the only place where evokers, vindicators, and vexes spawn
    naturally (but only once)
    """
    BURIED_TREASURE = register(StructureType("buried_treasure", MapCursor.Type.RED_X))
    """
    Buried treasure consists of a single chest buried in the beach sand or
    gravel, with random loot in it.
    """
    SHIPWRECK = register(StructureType("shipwreck", MapCursor.Type.RED_X))
    """
    Shipwrecks are structures that generate on the floor of oceans or
    beaches.
    
    They are made up of wood materials, and contain 1-3 loot chests. They can
    generate sideways, upside-down, or upright.
    """
    PILLAGER_OUTPOST = register(StructureType("pillager_outpost", MapCursor.Type.RED_X))
    """
    Pillager outposts may contain crossbows.
    """
    NETHER_FOSSIL = register(StructureType("nether_fossil", MapCursor.Type.RED_X))
    """
    Nether fossils.
    """
    RUINED_PORTAL = register(StructureType("ruined_portal", MapCursor.Type.RED_X))
    """
    Ruined portal.
    """
    BASTION_REMNANT = register(StructureType("bastion_remnant", MapCursor.Type.RED_X))
    """
    Bastion remnant.
    """


    def getName(self) -> str:
        """
        Get the name of this structure. This is case-sensitive when used in
        commands.

        Returns
        - the name of this structure
        """
        ...


    def getMapIcon(self) -> "MapCursor.Type":
        """
        Get the org.bukkit.map.MapCursor.Type that this structure can use on maps. If
        this is null, this structure will not appear on explorer maps.

        Returns
        - the org.bukkit.map.MapCursor.Type or null.
        """
        ...


    def equals(self, other: "Object") -> bool:
        ...


    def hashCode(self) -> int:
        ...


    def toString(self) -> str:
        ...


    @staticmethod
    def getStructureTypes() -> dict[str, "StructureType"]:
        """
        Get all registered StructureTypes.

        Returns
        - an immutable copy of registered structure types.
        """
        ...


    def getKey(self) -> "NamespacedKey":
        ...
