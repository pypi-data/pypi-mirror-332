"""
Python module generated from Java source file org.bukkit.util.noise.PerlinNoiseGenerator

Java source file obtained from artifact spigot-api version 1.20.1-R0.1-20230921.163938-66

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util import Random
from org.bukkit import World
from org.bukkit.util.noise import *
from typing import Any, Callable, Iterable, Tuple


class PerlinNoiseGenerator(NoiseGenerator):
    """
    Generates noise using the "classic" perlin generator

    See
    - SimplexNoiseGenerator "Improved" and faster version with slightly
        different results
    """

    def __init__(self, world: "World"):
        """
        Creates a seeded perlin noise generator for the given world

        Arguments
        - world: World to construct this generator for
        """
        ...


    def __init__(self, seed: int):
        """
        Creates a seeded perlin noise generator for the given seed

        Arguments
        - seed: Seed to construct this generator for
        """
        ...


    def __init__(self, rand: "Random"):
        """
        Creates a seeded perlin noise generator with the given Random

        Arguments
        - rand: Random to construct with
        """
        ...


    @staticmethod
    def getNoise(x: float) -> float:
        """
        Computes and returns the 1D unseeded perlin noise for the given
        coordinates in 1D space

        Arguments
        - x: X coordinate

        Returns
        - Noise at given location, from range -1 to 1
        """
        ...


    @staticmethod
    def getNoise(x: float, y: float) -> float:
        """
        Computes and returns the 2D unseeded perlin noise for the given
        coordinates in 2D space

        Arguments
        - x: X coordinate
        - y: Y coordinate

        Returns
        - Noise at given location, from range -1 to 1
        """
        ...


    @staticmethod
    def getNoise(x: float, y: float, z: float) -> float:
        """
        Computes and returns the 3D unseeded perlin noise for the given
        coordinates in 3D space

        Arguments
        - x: X coordinate
        - y: Y coordinate
        - z: Z coordinate

        Returns
        - Noise at given location, from range -1 to 1
        """
        ...


    @staticmethod
    def getInstance() -> "PerlinNoiseGenerator":
        """
        Gets the singleton unseeded instance of this generator

        Returns
        - Singleton
        """
        ...


    def noise(self, x: float, y: float, z: float) -> float:
        ...


    @staticmethod
    def getNoise(x: float, octaves: int, frequency: float, amplitude: float) -> float:
        """
        Generates noise for the 1D coordinates using the specified number of
        octaves and parameters

        Arguments
        - x: X-coordinate
        - octaves: Number of octaves to use
        - frequency: How much to alter the frequency by each octave
        - amplitude: How much to alter the amplitude by each octave

        Returns
        - Resulting noise
        """
        ...


    @staticmethod
    def getNoise(x: float, y: float, octaves: int, frequency: float, amplitude: float) -> float:
        """
        Generates noise for the 2D coordinates using the specified number of
        octaves and parameters

        Arguments
        - x: X-coordinate
        - y: Y-coordinate
        - octaves: Number of octaves to use
        - frequency: How much to alter the frequency by each octave
        - amplitude: How much to alter the amplitude by each octave

        Returns
        - Resulting noise
        """
        ...


    @staticmethod
    def getNoise(x: float, y: float, z: float, octaves: int, frequency: float, amplitude: float) -> float:
        """
        Generates noise for the 3D coordinates using the specified number of
        octaves and parameters

        Arguments
        - x: X-coordinate
        - y: Y-coordinate
        - z: Z-coordinate
        - octaves: Number of octaves to use
        - frequency: How much to alter the frequency by each octave
        - amplitude: How much to alter the amplitude by each octave

        Returns
        - Resulting noise
        """
        ...
