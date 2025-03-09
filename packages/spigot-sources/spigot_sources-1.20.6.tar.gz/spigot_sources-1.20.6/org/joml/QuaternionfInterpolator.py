"""
Python module generated from Java source file org.joml.QuaternionfInterpolator

Java source file obtained from artifact joml version 1.10.5

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.joml import *
from typing import Any, Callable, Iterable, Tuple


class QuaternionfInterpolator:
    """
    Computes the weighted average of multiple rotations represented as Quaternionf instances.
    
    Instances of this class are *not* thread-safe.

    Author(s)
    - Kai Burjack
    """

    def computeWeightedAverage(self, qs: list["Quaternionfc"], weights: list[float], maxSvdIterations: int, dest: "Quaternionf") -> "Quaternionf":
        """
        Compute the weighted average of all of the quaternions given in `qs` using the specified interpolation factors `weights`, and store the result in `dest`.

        Arguments
        - qs: the quaternions to interpolate over
        - weights: the weights of each individual quaternion in `qs`
        - maxSvdIterations: the maximum number of iterations in the Singular Value Decomposition step used by this method
        - dest: will hold the result

        Returns
        - dest
        """
        ...
