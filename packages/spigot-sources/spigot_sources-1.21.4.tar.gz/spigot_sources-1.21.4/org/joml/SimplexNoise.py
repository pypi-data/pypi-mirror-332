"""
Python module generated from Java source file org.joml.SimplexNoise

Java source file obtained from artifact joml version 1.10.8

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.joml import *
from typing import Any, Callable, Iterable, Tuple


class SimplexNoise:
    """
    A simplex noise algorithm for 2D, 3D and 4D input.
    
    It was originally authored by Stefan Gustavson.
    
    The original implementation can be found here: <a
    href="http://staffwww.itn.liu.se/~stegu/simplexnoise/SimplexNoise.java">http://http://staffwww.itn.liu.se/</a>.
    """

    @staticmethod
    def noise(x: float, y: float) -> float:
        """
        Compute 2D simplex noise for the given input vector `(x, y)`.
        
        The result is in the range `[-1..+1]`.

        Arguments
        - x: the x coordinate
        - y: the y coordinate

        Returns
        - the noise value (within `[-1..+1]`)
        """
        ...


    @staticmethod
    def noise(x: float, y: float, z: float) -> float:
        """
        Compute 3D simplex noise for the given input vector `(x, y, z)`.
        
        The result is in the range `[-1..+1]`.

        Arguments
        - x: the x coordinate
        - y: the y coordinate
        - z: the z coordinate

        Returns
        - the noise value (within `[-1..+1]`)
        """
        ...


    @staticmethod
    def noise(x: float, y: float, z: float, w: float) -> float:
        """
        Compute 4D simplex noise for the given input vector `(x, y, z, w)`.
        
        The result is in the range `[-1..+1]`.

        Arguments
        - x: the x coordinate
        - y: the y coordinate
        - z: the z coordinate
        - w: the w coordinate

        Returns
        - the noise value (within `[-1..+1]`)
        """
        ...
