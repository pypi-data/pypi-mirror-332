"""
Python module generated from Java source file org.joml.sampling.StratifiedSampling

Java source file obtained from artifact joml version 1.10.5

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.joml import Random
from org.joml.sampling import *
from typing import Any, Callable, Iterable, Tuple


class StratifiedSampling:
    """
    Creates samples on a unit quad using an NxN strata grid.

    Author(s)
    - Kai Burjack
    """

    def __init__(self, seed: int):
        """
        Create a new instance of StratifiedSampling and initialize the random number generator with the given
        `seed`.

        Arguments
        - seed: the seed to initialize the random number generator with
        """
        ...


    def generateRandom(self, n: int, callback: "Callback2d") -> None:
        """
        Generate `n * n` random sample positions in the unit square of `x, y = [-1..+1]`.
        
        Each sample within its stratum is distributed randomly.

        Arguments
        - n: the number of strata in each dimension
        - callback: will be called for each generated sample position
        """
        ...


    def generateCentered(self, n: int, centering: float, callback: "Callback2d") -> None:
        """
        Generate `n * n` random sample positions in the unit square of `x, y = [-1..+1]`.
        
        Each sample within its stratum is confined to be within `[-centering/2..1-centering]` of its stratum.

        Arguments
        - n: the number of strata in each dimension
        - centering: determines how much the random samples in each stratum are confined to be near the center of the
                   stratum. Possible values are `[0..1]`
        - callback: will be called for each generated sample position
        """
        ...
