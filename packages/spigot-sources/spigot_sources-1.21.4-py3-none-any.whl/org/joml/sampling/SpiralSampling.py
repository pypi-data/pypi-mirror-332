"""
Python module generated from Java source file org.joml.sampling.SpiralSampling

Java source file obtained from artifact joml version 1.10.8

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.joml import Random
from org.joml.sampling import *
from typing import Any, Callable, Iterable, Tuple


class SpiralSampling:
    """
    Creates samples on a spiral around a center point.

    Author(s)
    - Kai Burjack
    """

    def __init__(self, seed: int):
        """
        Create a new instance of SpiralSampling and initialize the random number generator with the given `seed`.

        Arguments
        - seed: the seed to initialize the random number generator with
        """
        ...


    def createEquiAngle(self, radius: float, numRotations: int, numSamples: int, callback: "Callback2d") -> None:
        """
        Create `numSamples` number of samples on a spiral with maximum radius `radius` around the center using `numRotations` number of rotations
        along the spiral, and call the given `callback` for each sample generated.
        
        The generated sample points are distributed with equal angle differences around the spiral, so they concentrate towards the center.

        Arguments
        - radius: the maximum radius of the spiral
        - numRotations: the number of rotations of the spiral
        - numSamples: the number of samples to generate
        - callback: will be called for each sample generated
        """
        ...


    def createEquiAngle(self, radius: float, numRotations: int, numSamples: int, jitter: float, callback: "Callback2d") -> None:
        """
        Create `numSamples` number of samples on a spiral with maximum radius `radius` around the center using `numRotations` number of rotations
        along the spiral, and call the given `callback` for each sample generated.
        
        The generated sample points are distributed with equal angle differences around the spiral, so they concentrate towards the center.
        
        Additionally, the radius of each sample point is jittered by the given `jitter` factor.

        Arguments
        - radius: the maximum radius of the spiral
        - numRotations: the number of rotations of the spiral
        - numSamples: the number of samples to generate
        - jitter: the factor by which the radius of each sample point is jittered. Possible values are `[0..1]`
        - callback: will be called for each sample generated
        """
        ...
