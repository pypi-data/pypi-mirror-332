"""
Python module generated from Java source file org.joml.sampling.PoissonSampling

Java source file obtained from artifact joml version 1.10.5

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.joml import Random
from org.joml import Vector2f
from org.joml.sampling import *
from typing import Any, Callable, Iterable, Tuple


class PoissonSampling:
    """
    Generates Poisson samples.
    
    The algorithm implemented here is based on <a href= "http://www.cs.ubc.ca/~rbridson/docs/bridson-siggraph07-poissondisk.pdf">Fast Poisson Disk Sampling in Arbitrary
    Dimensions</a>.

    Author(s)
    - Kai Burjack
    """

    class Disk:
        """
        Generates Poisson samples on a disk.
        
        The algorithm implemented here is based on <a href= "http://www.cs.ubc.ca/~rbridson/docs/bridson-siggraph07-poissondisk.pdf">Fast Poisson Disk Sampling in Arbitrary
        Dimensions</a>.

    Author(s)
        - Kai Burjack
        """

        def __init__(self, seed: int, diskRadius: float, minDist: float, k: int, callback: "Callback2d"):
            """
            Create a new instance of Disk which computes poisson-distributed samples on a disk with the given radius `diskRadius` and notifies the given
            `callback` for each found sample point.
            
            The samples are distributed evenly on the disk with a minimum distance to one another of at least `minDist`.

            Arguments
            - seed: the seed to initialize the random number generator with
            - diskRadius: the disk radius
            - minDist: the minimum distance between any two generated samples
            - k: determines how many samples are tested before rejection. Higher values produce better results. Typical values are 20 to 30
            - callback: will be notified about each sample point
            """
            ...
