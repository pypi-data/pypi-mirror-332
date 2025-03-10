"""
Python module generated from Java source file org.bukkit.util.noise.OctaveGenerator

Java source file obtained from artifact spigot-api version 1.19.4-R0.1-20230607.155743-88

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.util.noise import *
from typing import Any, Callable, Iterable, Tuple


class OctaveGenerator:
    """
    Creates noise using unbiased octaves
    """

    def setScale(self, scale: float) -> None:
        """
        Sets the scale used for all coordinates passed to this generator.
        
        This is the equivalent to setting each coordinate to the specified
        value.

        Arguments
        - scale: New value to scale each coordinate by
        """
        ...


    def getXScale(self) -> float:
        """
        Gets the scale used for each X-coordinates passed

        Returns
        - X scale
        """
        ...


    def setXScale(self, scale: float) -> None:
        """
        Sets the scale used for each X-coordinates passed

        Arguments
        - scale: New X scale
        """
        ...


    def getYScale(self) -> float:
        """
        Gets the scale used for each Y-coordinates passed

        Returns
        - Y scale
        """
        ...


    def setYScale(self, scale: float) -> None:
        """
        Sets the scale used for each Y-coordinates passed

        Arguments
        - scale: New Y scale
        """
        ...


    def getZScale(self) -> float:
        """
        Gets the scale used for each Z-coordinates passed

        Returns
        - Z scale
        """
        ...


    def setZScale(self, scale: float) -> None:
        """
        Sets the scale used for each Z-coordinates passed

        Arguments
        - scale: New Z scale
        """
        ...


    def getOctaves(self) -> list["NoiseGenerator"]:
        """
        Gets a clone of the individual octaves used within this generator

        Returns
        - Clone of the individual octaves
        """
        ...


    def noise(self, x: float, frequency: float, amplitude: float) -> float:
        """
        Generates noise for the 1D coordinates using the specified number of
        octaves and parameters

        Arguments
        - x: X-coordinate
        - frequency: How much to alter the frequency by each octave
        - amplitude: How much to alter the amplitude by each octave

        Returns
        - Resulting noise
        """
        ...


    def noise(self, x: float, frequency: float, amplitude: float, normalized: bool) -> float:
        """
        Generates noise for the 1D coordinates using the specified number of
        octaves and parameters

        Arguments
        - x: X-coordinate
        - frequency: How much to alter the frequency by each octave
        - amplitude: How much to alter the amplitude by each octave
        - normalized: If True, normalize the value to [-1, 1]

        Returns
        - Resulting noise
        """
        ...


    def noise(self, x: float, y: float, frequency: float, amplitude: float) -> float:
        """
        Generates noise for the 2D coordinates using the specified number of
        octaves and parameters

        Arguments
        - x: X-coordinate
        - y: Y-coordinate
        - frequency: How much to alter the frequency by each octave
        - amplitude: How much to alter the amplitude by each octave

        Returns
        - Resulting noise
        """
        ...


    def noise(self, x: float, y: float, frequency: float, amplitude: float, normalized: bool) -> float:
        """
        Generates noise for the 2D coordinates using the specified number of
        octaves and parameters

        Arguments
        - x: X-coordinate
        - y: Y-coordinate
        - frequency: How much to alter the frequency by each octave
        - amplitude: How much to alter the amplitude by each octave
        - normalized: If True, normalize the value to [-1, 1]

        Returns
        - Resulting noise
        """
        ...


    def noise(self, x: float, y: float, z: float, frequency: float, amplitude: float) -> float:
        """
        Generates noise for the 3D coordinates using the specified number of
        octaves and parameters

        Arguments
        - x: X-coordinate
        - y: Y-coordinate
        - z: Z-coordinate
        - frequency: How much to alter the frequency by each octave
        - amplitude: How much to alter the amplitude by each octave

        Returns
        - Resulting noise
        """
        ...


    def noise(self, x: float, y: float, z: float, frequency: float, amplitude: float, normalized: bool) -> float:
        """
        Generates noise for the 3D coordinates using the specified number of
        octaves and parameters

        Arguments
        - x: X-coordinate
        - y: Y-coordinate
        - z: Z-coordinate
        - frequency: How much to alter the frequency by each octave
        - amplitude: How much to alter the amplitude by each octave
        - normalized: If True, normalize the value to [-1, 1]

        Returns
        - Resulting noise
        """
        ...
