"""
Python module generated from Java source file org.bukkit.util.noise.SimplexNoiseGenerator

Java source file obtained from artifact spigot-api version 1.21.2-R0.1-20241023.084343-5

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util import Random
from org.bukkit import World
from org.bukkit.util.noise import *
from typing import Any, Callable, Iterable, Tuple


class SimplexNoiseGenerator(PerlinNoiseGenerator):
    """
    Generates simplex-based noise.
    
    This is a modified version of the freely published version in the paper by
    Stefan Gustavson at
    <a href="http://staffwww.itn.liu.se/~stegu/simplexnoise/simplexnoise.pdf">
    http://staffwww.itn.liu.se/~stegu/simplexnoise/simplexnoise.pdf</a>
    """

    def __init__(self, world: "World"):
        """
        Creates a seeded simplex noise generator for the given world

        Arguments
        - world: World to construct this generator for
        """
        ...


    def __init__(self, seed: int):
        """
        Creates a seeded simplex noise generator for the given seed

        Arguments
        - seed: Seed to construct this generator for
        """
        ...


    def __init__(self, rand: "Random"):
        """
        Creates a seeded simplex noise generator with the given Random

        Arguments
        - rand: Random to construct with
        """
        ...


    @staticmethod
    def getNoise(xin: float) -> float:
        """
        Computes and returns the 1D unseeded simplex noise for the given
        coordinates in 1D space

        Arguments
        - xin: X coordinate

        Returns
        - Noise at given location, from range -1 to 1
        """
        ...


    @staticmethod
    def getNoise(xin: float, yin: float) -> float:
        """
        Computes and returns the 2D unseeded simplex noise for the given
        coordinates in 2D space

        Arguments
        - xin: X coordinate
        - yin: Y coordinate

        Returns
        - Noise at given location, from range -1 to 1
        """
        ...


    @staticmethod
    def getNoise(xin: float, yin: float, zin: float) -> float:
        """
        Computes and returns the 3D unseeded simplex noise for the given
        coordinates in 3D space

        Arguments
        - xin: X coordinate
        - yin: Y coordinate
        - zin: Z coordinate

        Returns
        - Noise at given location, from range -1 to 1
        """
        ...


    @staticmethod
    def getNoise(x: float, y: float, z: float, w: float) -> float:
        """
        Computes and returns the 4D simplex noise for the given coordinates in
        4D space

        Arguments
        - x: X coordinate
        - y: Y coordinate
        - z: Z coordinate
        - w: W coordinate

        Returns
        - Noise at given location, from range -1 to 1
        """
        ...


    def noise(self, xin: float, yin: float, zin: float) -> float:
        ...


    def noise(self, xin: float, yin: float) -> float:
        ...


    def noise(self, x: float, y: float, z: float, w: float) -> float:
        """
        Computes and returns the 4D simplex noise for the given coordinates in
        4D space

        Arguments
        - x: X coordinate
        - y: Y coordinate
        - z: Z coordinate
        - w: W coordinate

        Returns
        - Noise at given location, from range -1 to 1
        """
        ...


    @staticmethod
    def getInstance() -> "SimplexNoiseGenerator":
        """
        Gets the singleton unseeded instance of this generator

        Returns
        - Singleton
        """
        ...
