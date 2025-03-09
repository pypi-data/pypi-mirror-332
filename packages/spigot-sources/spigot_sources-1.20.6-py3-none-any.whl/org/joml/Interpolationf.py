"""
Python module generated from Java source file org.joml.Interpolationf

Java source file obtained from artifact joml version 1.10.5

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.joml import *
from typing import Any, Callable, Iterable, Tuple


class Interpolationf:
    """
    Contains various interpolation functions.

    Author(s)
    - Kai Burjack
    """

    @staticmethod
    def interpolateTriangle(v0X: float, v0Y: float, f0: float, v1X: float, v1Y: float, f1: float, v2X: float, v2Y: float, f2: float, x: float, y: float) -> float:
        """
        Bilinearly interpolate the single scalar value *f* over the given triangle.
        
        Reference: <a href="https://en.wikipedia.org/wiki/Barycentric_coordinate_system">https://en.wikipedia.org/</a>

        Arguments
        - v0X: the x coordinate of the first triangle vertex
        - v0Y: the y coordinate of the first triangle vertex
        - f0: the value of *f* at the first vertex
        - v1X: the x coordinate of the second triangle vertex
        - v1Y: the y coordinate of the second triangle vertex
        - f1: the value of *f* at the second vertex
        - v2X: the x coordinate of the third triangle vertex
        - v2Y: the y coordinate of the third triangle vertex
        - f2: the value of *f* at the third vertex
        - x: the x coordinate of the point to interpolate *f* at
        - y: the y coordinate of the point to interpolate *f* at

        Returns
        - the interpolated value of *f*
        """
        ...


    @staticmethod
    def interpolateTriangle(v0X: float, v0Y: float, f0X: float, f0Y: float, v1X: float, v1Y: float, f1X: float, f1Y: float, v2X: float, v2Y: float, f2X: float, f2Y: float, x: float, y: float, dest: "Vector2f") -> "Vector2f":
        """
        Bilinearly interpolate the two-dimensional vector *f* over the given triangle and store the result in `dest`.
        
        Reference: <a href="https://en.wikipedia.org/wiki/Barycentric_coordinate_system">https://en.wikipedia.org/</a>

        Arguments
        - v0X: the x coordinate of the first triangle vertex
        - v0Y: the y coordinate of the first triangle vertex
        - f0X: the x component of the value of *f* at the first vertex
        - f0Y: the y component of the value of *f* at the first vertex
        - v1X: the x coordinate of the second triangle vertex
        - v1Y: the y coordinate of the second triangle vertex
        - f1X: the x component of the value of *f* at the second vertex
        - f1Y: the y component of the value of *f* at the second vertex
        - v2X: the x coordinate of the third triangle vertex
        - v2Y: the y coordinate of the third triangle vertex
        - f2X: the x component of the value of *f* at the third vertex
        - f2Y: the y component of the value of *f* at the third vertex
        - x: the x coordinate of the point to interpolate *f* at
        - y: the y coordinate of the point to interpolate *f* at
        - dest: will hold the interpolation result

        Returns
        - dest
        """
        ...


    @staticmethod
    def dFdxLinear(v0X: float, v0Y: float, f0X: float, f0Y: float, v1X: float, v1Y: float, f1X: float, f1Y: float, v2X: float, v2Y: float, f2X: float, f2Y: float, dest: "Vector2f") -> "Vector2f":
        """
        Compute the first-order derivative of a linear two-dimensional function *f* with respect to X
        and store the result in `dest`.
        
        This method computes the constant rate of change for *f* given the three values of *f*
        at the specified three inputs `(v0X, v0Y)`, `(v1X, v1Y)` and `(v2X, v2Y)`.

        Arguments
        - v0X: the x coordinate of the first triangle vertex
        - v0Y: the y coordinate of the first triangle vertex
        - f0X: the x component of the value of *f* at the first vertex
        - f0Y: the y component of the value of *f* at the first vertex
        - v1X: the x coordinate of the second triangle vertex
        - v1Y: the y coordinate of the second triangle vertex
        - f1X: the x component of the value of *f* at the second vertex
        - f1Y: the y component of the value of *f* at the second vertex
        - v2X: the x coordinate of the third triangle vertex
        - v2Y: the y coordinate of the third triangle vertex
        - f2X: the x component of the value of *f* at the third vertex
        - f2Y: the y component of the value of *f* at the third vertex
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    @staticmethod
    def dFdyLinear(v0X: float, v0Y: float, f0X: float, f0Y: float, v1X: float, v1Y: float, f1X: float, f1Y: float, v2X: float, v2Y: float, f2X: float, f2Y: float, dest: "Vector2f") -> "Vector2f":
        """
        Compute the first-order derivative of a linear two-dimensional function *f* with respect to Y
        and store the result in `dest`.
        
        This method computes the constant rate of change for *f* given the three values of *f*
        at the specified three inputs `(v0X, v0Y)`, `(v1X, v1Y)` and `(v2X, v2Y)`.

        Arguments
        - v0X: the x coordinate of the first triangle vertex
        - v0Y: the y coordinate of the first triangle vertex
        - f0X: the x component of the value of *f* at the first vertex
        - f0Y: the y component of the value of *f* at the first vertex
        - v1X: the x coordinate of the second triangle vertex
        - v1Y: the y coordinate of the second triangle vertex
        - f1X: the x component of the value of *f* at the second vertex
        - f1Y: the y component of the value of *f* at the second vertex
        - v2X: the x coordinate of the third triangle vertex
        - v2Y: the y coordinate of the third triangle vertex
        - f2X: the x component of the value of *f* at the third vertex
        - f2Y: the y component of the value of *f* at the third vertex
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    @staticmethod
    def interpolateTriangle(v0X: float, v0Y: float, f0X: float, f0Y: float, f0Z: float, v1X: float, v1Y: float, f1X: float, f1Y: float, f1Z: float, v2X: float, v2Y: float, f2X: float, f2Y: float, f2Z: float, x: float, y: float, dest: "Vector3f") -> "Vector3f":
        """
        Bilinearly interpolate the three-dimensional vector *f* over the given triangle and store the result in `dest`.
        
        Reference: <a href="https://en.wikipedia.org/wiki/Barycentric_coordinate_system">https://en.wikipedia.org/</a>

        Arguments
        - v0X: the x coordinate of the first triangle vertex
        - v0Y: the y coordinate of the first triangle vertex
        - f0X: the x component of the value of *f* at the first vertex
        - f0Y: the y component of the value of *f* at the first vertex
        - f0Z: the z component of the value of *f* at the first vertex
        - v1X: the x coordinate of the second triangle vertex
        - v1Y: the y coordinate of the second triangle vertex
        - f1X: the x component of the value of *f* at the second vertex
        - f1Y: the y component of the value of *f* at the second vertex
        - f1Z: the z component of the value of *f* at the second vertex
        - v2X: the x coordinate of the third triangle vertex
        - v2Y: the y coordinate of the third triangle vertex
        - f2X: the x component of the value of *f* at the third vertex
        - f2Y: the y component of the value of *f* at the third vertex
        - f2Z: the z component of the value of *f* at the third vertex
        - x: the x coordinate of the point to interpolate *f* at
        - y: the y coordinate of the point to interpolate *f* at
        - dest: will hold the interpolation result

        Returns
        - dest
        """
        ...


    @staticmethod
    def interpolationFactorsTriangle(v0X: float, v0Y: float, v1X: float, v1Y: float, v2X: float, v2Y: float, x: float, y: float, dest: "Vector3f") -> "Vector3f":
        """
        Compute the interpolation factors `(t0, t1, t2)` in order to interpolate an arbitrary value over a given 
        triangle at the given point `(x, y)`.
        
        This method takes in the 2D vertex positions of the three vertices of a triangle and stores in `dest` the 
        factors `(t0, t1, t2)` in the equation `v' = v0 * t0 + v1 * t1 + v2 * t2` where `(v0, v1, v2)` are
        arbitrary (scalar or vector) values associated with the respective vertices of the triangle. The computed value `v'`
        is the interpolated value at the given position `(x, y)`.

        Arguments
        - v0X: the x coordinate of the first triangle vertex
        - v0Y: the y coordinate of the first triangle vertex
        - v1X: the x coordinate of the second triangle vertex
        - v1Y: the y coordinate of the second triangle vertex
        - v2X: the x coordinate of the third triangle vertex
        - v2Y: the y coordinate of the third triangle vertex
        - x: the x coordinate of the point to interpolate at
        - y: the y coordinate of the point to interpolate at
        - dest: will hold the interpolation factors `(t0, t1, t2)`

        Returns
        - dest
        """
        ...
