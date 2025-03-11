"""
Python module generated from Java source file org.bukkit.generator.BiomeParameterPoint

Java source file obtained from artifact spigot-api version 1.21.1-R0.1-20241022.152140-54

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.generator import *
from typing import Any, Callable, Iterable, Tuple


class BiomeParameterPoint:
    """
    Represents the biome noise parameters which may be passed to a world
    generator.
    """

    def getTemperature(self) -> float:
        """
        Gets the temperature of the biome at this point that is suggested by the
        NoiseGenerator.

        Returns
        - The temperature of the biome at this point
        """
        ...


    def getMaxTemperature(self) -> float:
        """
        Gets the maximum temperature that is possible.

        Returns
        - The maximum temperature
        """
        ...


    def getMinTemperature(self) -> float:
        """
        Gets the minimum temperature that is possible.

        Returns
        - The minimum temperature
        """
        ...


    def getHumidity(self) -> float:
        """
        Gets the humidity of the biome at this point that is suggested by the
        NoiseGenerator.

        Returns
        - The humidity of the biome at this point
        """
        ...


    def getMaxHumidity(self) -> float:
        """
        Gets the maximum humidity that is possible.

        Returns
        - The maximum humidity
        """
        ...


    def getMinHumidity(self) -> float:
        """
        Gets the minimum humidity that is possible.

        Returns
        - The minimum humidity
        """
        ...


    def getContinentalness(self) -> float:
        """
        Gets the continentalness of the biome at this point that is suggested by
        the NoiseGenerator.

        Returns
        - The continentalness of the biome at this point
        """
        ...


    def getMaxContinentalness(self) -> float:
        """
        Gets the maximum continentalness that is possible.

        Returns
        - The maximum continentalness
        """
        ...


    def getMinContinentalness(self) -> float:
        """
        Gets the minimum continentalness that is possible.

        Returns
        - The minimum continentalness
        """
        ...


    def getErosion(self) -> float:
        """
        Gets the erosion of the biome at this point that is suggested by the
        NoiseGenerator.

        Returns
        - The erosion of the biome at this point
        """
        ...


    def getMaxErosion(self) -> float:
        """
        Gets the maximum erosion that is possible.

        Returns
        - The maximum erosion
        """
        ...


    def getMinErosion(self) -> float:
        """
        Gets the minimum erosion that is possible.

        Returns
        - The minimum erosion
        """
        ...


    def getDepth(self) -> float:
        """
        Gets the depth of the biome at this point that is suggested by the
        NoiseGenerator.

        Returns
        - The depth of the biome at this point
        """
        ...


    def getMaxDepth(self) -> float:
        """
        Gets the maximum depth that is possible.

        Returns
        - The maximum depth
        """
        ...


    def getMinDepth(self) -> float:
        """
        Gets the minimum depth that is possible.

        Returns
        - The minimum depth
        """
        ...


    def getWeirdness(self) -> float:
        """
        Gets the weirdness of the biome at this point that is suggested by the
        NoiseGenerator.

        Returns
        - The weirdness of the biome at this point
        """
        ...


    def getMaxWeirdness(self) -> float:
        """
        Gets the maximum weirdness that is possible.

        Returns
        - The maximum weirdness
        """
        ...


    def getMinWeirdness(self) -> float:
        """
        Gets the minimum weirdness that is possible.

        Returns
        - The minimum weirdness
        """
        ...
