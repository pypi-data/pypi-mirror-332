"""
Python module generated from Java source file org.joml.Random

Java source file obtained from artifact joml version 1.10.5

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.joml import *
from typing import Any, Callable, Iterable, Tuple


class Random:
    """
    Pseudo-random number generator.

    Author(s)
    - Kai Burjack
    """

    def __init__(self):
        """
        Create a new instance of Random and initialize it with a random seed.
        """
        ...


    def __init__(self, seed: int):
        """
        Create a new instance of Random and initialize it with the given `seed`.

        Arguments
        - seed: the seed number
        """
        ...


    @staticmethod
    def newSeed() -> int:
        ...


    def nextFloat(self) -> float:
        """
        Generate a uniformly distributed floating-point number in the half-open range [0, 1).

        Returns
        - a random float in the range [0..1)
        """
        ...


    def nextInt(self, n: int) -> int:
        """
        Generate a uniformly distributed integer in the half-open range [0, n).

        Arguments
        - n: the upper limit (exclusive) of the generated integer

        Returns
        - a random integer in the range [0..n)
        """
        ...
