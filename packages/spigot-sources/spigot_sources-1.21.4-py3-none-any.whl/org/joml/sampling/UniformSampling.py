"""
Python module generated from Java source file org.joml.sampling.UniformSampling

Java source file obtained from artifact joml version 1.10.8

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.joml import Random
from org.joml.sampling import *
from typing import Any, Callable, Iterable, Tuple


class UniformSampling:
    """
    Generates uniform samples.

    Author(s)
    - Kai Burjack
    """

    class Disk:
        """
        Generates uniform samples on a unit disk.

    Author(s)
        - Kai Burjack
        """

        def __init__(self, seed: int, numSamples: int, callback: "Callback2d"):
            """
            Create a new instance of Disk, initialize the random number generator with the given `seed` and generate `numSamples` number of sample
            positions on the unit disk, and call the given `callback` for each sample generate.

            Arguments
            - seed: the seed to initialize the random number generator with
            - numSamples: the number of samples to generate
            - callback: will be called for each sample generated
            """
            ...


    class Sphere:
        """
        Generates uniform samples on a unit sphere.

    Author(s)
        - Kai Burjack
        """

        def __init__(self, seed: int, numSamples: int, callback: "Callback3d"):
            """
            Create a new instance of Sphere, initialize the random number generator with the given `seed` and generate `numSamples` number of sample
            positions on the unit sphere, and call the given `callback` for each sample generate.

            Arguments
            - seed: the seed to initialize the random number generator with
            - numSamples: the number of samples to generate
            - callback: will be called for each sample generated
            """
            ...


        def generate(self, numSamples: int, callback: "Callback3d") -> None:
            """
            Create `numSamples` number of samples which are uniformly distributed on a unit sphere, and call the given `callback` for each sample generated.
            
            Reference: <a href="http://mathworld.wolfram.com/SpherePointPicking.html">http://mathworld.wolfram.com/</a>

            Arguments
            - numSamples: the number of samples to generate
            - callback: will be called for each sample generated
            """
            ...
