"""
Python module generated from Java source file org.bukkit.util.noise.PerlinOctaveGenerator

Java source file obtained from artifact spigot-api version 1.20.3-R0.1-20231207.085553-9

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util import Random
from org.bukkit import World
from org.bukkit.util.noise import *
from typing import Any, Callable, Iterable, Tuple


class PerlinOctaveGenerator(OctaveGenerator):
    """
    Creates perlin noise through unbiased octaves
    """

    def __init__(self, world: "World", octaves: int):
        """
        Creates a perlin octave generator for the given world

        Arguments
        - world: World to construct this generator for
        - octaves: Amount of octaves to create
        """
        ...


    def __init__(self, seed: int, octaves: int):
        """
        Creates a perlin octave generator for the given world

        Arguments
        - seed: Seed to construct this generator for
        - octaves: Amount of octaves to create
        """
        ...


    def __init__(self, rand: "Random", octaves: int):
        """
        Creates a perlin octave generator for the given Random

        Arguments
        - rand: Random object to construct this generator for
        - octaves: Amount of octaves to create
        """
        ...
