"""
Python module generated from Java source file org.bukkit.util.BiomeSearchResult

Java source file obtained from artifact spigot-api version 1.20.4-R0.1-20240423.152506-123

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Location
from org.bukkit import World
from org.bukkit.block import Biome
from org.bukkit.util import *
from typing import Any, Callable, Iterable, Tuple


class BiomeSearchResult:
    """
    Holds the result of searching for a biome.

    See
    - World.locateNearestBiome(Location, int, int, int, Biome...)
    """

    def getBiome(self) -> "Biome":
        """
        Return the biome which was found.

        Returns
        - the found biome.
        """
        ...


    def getLocation(self) -> "Location":
        """
        Return the location of the biome.

        Returns
        - the location the biome was found.
        """
        ...
