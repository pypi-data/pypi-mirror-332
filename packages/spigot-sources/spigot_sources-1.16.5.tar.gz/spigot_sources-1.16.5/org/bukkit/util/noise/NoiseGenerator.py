"""
Python module generated from Java source file org.bukkit.util.noise.NoiseGenerator

Java source file obtained from artifact spigot-api version 1.16.5-R0.1-20210611.041013-99

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.util.noise import *
from typing import Any, Callable, Iterable, Tuple


class NoiseGenerator:
    """
    Base class for all noise generators
    """

    @staticmethod
    def floor(x: float) -> int:
        """
        Speedy floor, faster than (int)Math.floor(x)

        Arguments
        - x: Value to floor

        Returns
        - Floored value
        """
        ...


    def noise(self, x: float) -> float:
        """
        Computes and returns the 1D noise for the given coordinate in 1D space

        Arguments
        - x: X coordinate

        Returns
        - Noise at given location, from range -1 to 1
        """
        ...


    def noise(self, x: float, y: float) -> float:
        """
        Computes and returns the 2D noise for the given coordinates in 2D space

        Arguments
        - x: X coordinate
        - y: Y coordinate

        Returns
        - Noise at given location, from range -1 to 1
        """
        ...


    def noise(self, x: float, y: float, z: float) -> float:
        """
        Computes and returns the 3D noise for the given coordinates in 3D space

        Arguments
        - x: X coordinate
        - y: Y coordinate
        - z: Z coordinate

        Returns
        - Noise at given location, from range -1 to 1
        """
        ...


    def noise(self, x: float, octaves: int, frequency: float, amplitude: float) -> float:
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


    def noise(self, x: float, octaves: int, frequency: float, amplitude: float, normalized: bool) -> float:
        """
        Generates noise for the 1D coordinates using the specified number of
        octaves and parameters

        Arguments
        - x: X-coordinate
        - octaves: Number of octaves to use
        - frequency: How much to alter the frequency by each octave
        - amplitude: How much to alter the amplitude by each octave
        - normalized: If True, normalize the value to [-1, 1]

        Returns
        - Resulting noise
        """
        ...


    def noise(self, x: float, y: float, octaves: int, frequency: float, amplitude: float) -> float:
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


    def noise(self, x: float, y: float, octaves: int, frequency: float, amplitude: float, normalized: bool) -> float:
        """
        Generates noise for the 2D coordinates using the specified number of
        octaves and parameters

        Arguments
        - x: X-coordinate
        - y: Y-coordinate
        - octaves: Number of octaves to use
        - frequency: How much to alter the frequency by each octave
        - amplitude: How much to alter the amplitude by each octave
        - normalized: If True, normalize the value to [-1, 1]

        Returns
        - Resulting noise
        """
        ...


    def noise(self, x: float, y: float, z: float, octaves: int, frequency: float, amplitude: float) -> float:
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


    def noise(self, x: float, y: float, z: float, octaves: int, frequency: float, amplitude: float, normalized: bool) -> float:
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
        - normalized: If True, normalize the value to [-1, 1]

        Returns
        - Resulting noise
        """
        ...
