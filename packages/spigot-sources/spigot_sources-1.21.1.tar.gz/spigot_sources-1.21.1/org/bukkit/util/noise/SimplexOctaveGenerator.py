"""
Python module generated from Java source file org.bukkit.util.noise.SimplexOctaveGenerator

Java source file obtained from artifact spigot-api version 1.21.1-R0.1-20241022.152140-54

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util import Random
from org.bukkit import World
from org.bukkit.util.noise import *
from typing import Any, Callable, Iterable, Tuple


class SimplexOctaveGenerator(OctaveGenerator):
    """
    Creates simplex noise through unbiased octaves
    """

    def __init__(self, world: "World", octaves: int):
        """
        Creates a simplex octave generator for the given world

        Arguments
        - world: World to construct this generator for
        - octaves: Amount of octaves to create
        """
        ...


    def __init__(self, seed: int, octaves: int):
        """
        Creates a simplex octave generator for the given world

        Arguments
        - seed: Seed to construct this generator for
        - octaves: Amount of octaves to create
        """
        ...


    def __init__(self, rand: "Random", octaves: int):
        """
        Creates a simplex octave generator for the given Random

        Arguments
        - rand: Random object to construct this generator for
        - octaves: Amount of octaves to create
        """
        ...


    def setScale(self, scale: float) -> None:
        ...


    def getWScale(self) -> float:
        """
        Gets the scale used for each W-coordinates passed

        Returns
        - W scale
        """
        ...


    def setWScale(self, scale: float) -> None:
        """
        Sets the scale used for each W-coordinates passed

        Arguments
        - scale: New W scale
        """
        ...


    def noise(self, x: float, y: float, z: float, w: float, frequency: float, amplitude: float) -> float:
        """
        Generates noise for the 3D coordinates using the specified number of
        octaves and parameters

        Arguments
        - x: X-coordinate
        - y: Y-coordinate
        - z: Z-coordinate
        - w: W-coordinate
        - frequency: How much to alter the frequency by each octave
        - amplitude: How much to alter the amplitude by each octave

        Returns
        - Resulting noise
        """
        ...


    def noise(self, x: float, y: float, z: float, w: float, frequency: float, amplitude: float, normalized: bool) -> float:
        """
        Generates noise for the 3D coordinates using the specified number of
        octaves and parameters

        Arguments
        - x: X-coordinate
        - y: Y-coordinate
        - z: Z-coordinate
        - w: W-coordinate
        - frequency: How much to alter the frequency by each octave
        - amplitude: How much to alter the amplitude by each octave
        - normalized: If True, normalize the value to [-1, 1]

        Returns
        - Resulting noise
        """
        ...
