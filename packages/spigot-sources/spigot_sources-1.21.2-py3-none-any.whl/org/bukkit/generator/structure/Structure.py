"""
Python module generated from Java source file org.bukkit.generator.structure.Structure

Java source file obtained from artifact spigot-api version 1.21.2-R0.1-20241023.084343-5

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Keyed
from org.bukkit import NamespacedKey
from org.bukkit import Registry
from org.bukkit.generator.structure import *
from typing import Any, Callable, Iterable, Tuple


class Structure(Keyed):
    """
    Represent a Structure from the world.
    
    Listed structures are present in the default server. Depending on the server
    there might be additional structures present (for example structures added by
    data packs), which can be received via Registry.STRUCTURE.
    """

    PILLAGER_OUTPOST = getStructure("pillager_outpost")
    MINESHAFT = getStructure("mineshaft")
    MINESHAFT_MESA = getStructure("mineshaft_mesa")
    MANSION = getStructure("mansion")
    JUNGLE_PYRAMID = getStructure("jungle_pyramid")
    DESERT_PYRAMID = getStructure("desert_pyramid")
    IGLOO = getStructure("igloo")
    SHIPWRECK = getStructure("shipwreck")
    SHIPWRECK_BEACHED = getStructure("shipwreck_beached")
    SWAMP_HUT = getStructure("swamp_hut")
    STRONGHOLD = getStructure("stronghold")
    MONUMENT = getStructure("monument")
    OCEAN_RUIN_COLD = getStructure("ocean_ruin_cold")
    OCEAN_RUIN_WARM = getStructure("ocean_ruin_warm")
    FORTRESS = getStructure("fortress")
    NETHER_FOSSIL = getStructure("nether_fossil")
    END_CITY = getStructure("end_city")
    BURIED_TREASURE = getStructure("buried_treasure")
    BASTION_REMNANT = getStructure("bastion_remnant")
    VILLAGE_PLAINS = getStructure("village_plains")
    VILLAGE_DESERT = getStructure("village_desert")
    VILLAGE_SAVANNA = getStructure("village_savanna")
    VILLAGE_SNOWY = getStructure("village_snowy")
    VILLAGE_TAIGA = getStructure("village_taiga")
    RUINED_PORTAL = getStructure("ruined_portal")
    RUINED_PORTAL_DESERT = getStructure("ruined_portal_desert")
    RUINED_PORTAL_JUNGLE = getStructure("ruined_portal_jungle")
    RUINED_PORTAL_SWAMP = getStructure("ruined_portal_swamp")
    RUINED_PORTAL_MOUNTAIN = getStructure("ruined_portal_mountain")
    RUINED_PORTAL_OCEAN = getStructure("ruined_portal_ocean")
    RUINED_PORTAL_NETHER = getStructure("ruined_portal_nether")
    ANCIENT_CITY = getStructure("ancient_city")
    TRAIL_RUINS = getStructure("trail_ruins")
    TRIAL_CHAMBERS = getStructure("trial_chambers")


    def getStructureType(self) -> "StructureType":
        """
        Returns the type of the structure.

        Returns
        - the type of structure
        """
        ...
