"""
Python module generated from Java source file org.bukkit.generator.BiomeProvider

Java source file obtained from artifact spigot-api version 1.21.2-R0.1-20241023.084343-5

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block import Biome
from org.bukkit.generator import *
from typing import Any, Callable, Iterable, Tuple


class BiomeProvider:
    """
    Class for providing biomes.
    """

    def getBiome(self, worldInfo: "WorldInfo", x: int, y: int, z: int) -> "Biome":
        """
        Return the Biome which should be present at the provided location.
        
        Notes:
        
        This method **must** be completely thread safe and able to handle
        multiple concurrent callers.
        
        This method should only return biomes which are present in the list
        returned by .getBiomes(WorldInfo)
        
        This method should **never** return Biome.CUSTOM.

        Arguments
        - worldInfo: The world info of the world the biome will be used for
        - x: The X-coordinate from world origin
        - y: The Y-coordinate from world origin
        - z: The Z-coordinate from world origin

        Returns
        - Biome for the given location
        """
        ...


    def getBiome(self, worldInfo: "WorldInfo", x: int, y: int, z: int, biomeParameterPoint: "BiomeParameterPoint") -> "Biome":
        """
        Return the Biome which should be present at the provided location.
        
        Notes:
        
        This method **must** be completely thread safe and able to handle
        multiple concurrent callers.
        
        This method should only return biomes which are present in the list
        returned by .getBiomes(WorldInfo)
        
        This method should **never** return Biome.CUSTOM.
        Only this method is called if both this and
        .getBiome(WorldInfo, int, int, int) are overridden.

        Arguments
        - worldInfo: The world info of the world the biome will be used for
        - x: The X-coordinate from world origin
        - y: The Y-coordinate from world origin
        - z: The Z-coordinate from world origin
        - biomeParameterPoint: The parameter point that is provided by default
                              for this location (contains temperature, humidity,
                              continentalness, erosion, depth and weirdness)

        Returns
        - Biome for the given location

        See
        - .getBiome(WorldInfo, int, int, int)
        """
        ...


    def getBiomes(self, worldInfo: "WorldInfo") -> list["Biome"]:
        """
        Returns a list with every biome the BiomeProvider will use for
        the given world.
        
        Notes:
        
        This method only gets called once, when the world is loaded. Returning
        another list or modifying the values from the initial returned list later
        one, are not respected.
        
        This method should **never** return a list which contains
        Biome.CUSTOM.

        Arguments
        - worldInfo: The world info of the world the list will be used for

        Returns
        - A list with every biome the BiomeProvider uses
        """
        ...
