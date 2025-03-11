"""
Python module generated from Java source file org.bukkit.generator.structure.StructureType

Java source file obtained from artifact spigot-api version 1.21.4-R0.1-20250303.102353-42

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Keyed
from org.bukkit import NamespacedKey
from org.bukkit import Registry
from org.bukkit.generator.structure import *
from org.bukkit.registry import RegistryAware
from typing import Any, Callable, Iterable, Tuple


class StructureType(Keyed, RegistryAware):
    """
    Represent a StructureType of a Structure.
    
    Listed structure types are present in the default server. Depending on the
    server there might be additional structure types present (for example
    structure types added by data packs), which can be received via
    Registry.STRUCTURE_TYPE.
    """

    BURIED_TREASURE = getStructureType("buried_treasure")
    DESERT_PYRAMID = getStructureType("desert_pyramid")
    END_CITY = getStructureType("end_city")
    FORTRESS = getStructureType("fortress")
    IGLOO = getStructureType("igloo")
    JIGSAW = getStructureType("jigsaw")
    JUNGLE_TEMPLE = getStructureType("jungle_temple")
    MINESHAFT = getStructureType("mineshaft")
    NETHER_FOSSIL = getStructureType("nether_fossil")
    OCEAN_MONUMENT = getStructureType("ocean_monument")
    OCEAN_RUIN = getStructureType("ocean_ruin")
    RUINED_PORTAL = getStructureType("ruined_portal")
    SHIPWRECK = getStructureType("shipwreck")
    STRONGHOLD = getStructureType("stronghold")
    SWAMP_HUT = getStructureType("swamp_hut")
    WOODLAND_MANSION = getStructureType("woodland_mansion")


    def getKey(self) -> "NamespacedKey":
        """
        See
        - .isRegistered()

        Deprecated
        - A key might not always be present, use .getKeyOrThrow() instead.
        """
        ...
