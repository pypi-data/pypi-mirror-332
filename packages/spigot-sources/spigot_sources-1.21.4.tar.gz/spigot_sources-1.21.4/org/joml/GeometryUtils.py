"""
Python module generated from Java source file org.joml.GeometryUtils

Java source file obtained from artifact joml version 1.10.8

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.joml import *
from typing import Any, Callable, Iterable, Tuple


class GeometryUtils:
    """
    Useful geometry methods.

    Author(s)
    - Richard Greenlees
    """

    @staticmethod
    def perpendicular(x: float, y: float, z: float, dest1: "Vector3f", dest2: "Vector3f") -> None:
        """
        Compute two arbitrary vectors perpendicular to the given normalized vector `(x, y, z)`, and store them in `dest1` and `dest2`,
        respectively.
        
        The computed vectors will themselves be perpendicular to each another and normalized. So the tree vectors `(x, y, z)`, `dest1` and
        `dest2` form an orthonormal basis.

        Arguments
        - x: the x coordinate of the normalized input vector
        - y: the y coordinate of the normalized input vector
        - z: the z coordinate of the normalized input vector
        - dest1: will hold the first perpendicular vector
        - dest2: will hold the second perpendicular vector
        """
        ...


    @staticmethod
    def perpendicular(v: "Vector3fc", dest1: "Vector3f", dest2: "Vector3f") -> None:
        """
        Compute two arbitrary vectors perpendicular to the given normalized vector `v`, and store them in `dest1` and `dest2`,
        respectively.
        
        The computed vectors will themselves be perpendicular to each another and normalized. So the tree vectors `v`, `dest1` and
        `dest2` form an orthonormal basis.

        Arguments
        - v: the Vector3f.normalize() normalized input vector
        - dest1: will hold the first perpendicular vector
        - dest2: will hold the second perpendicular vector
        """
        ...


    @staticmethod
    def normal(v0: "Vector3fc", v1: "Vector3fc", v2: "Vector3fc", dest: "Vector3f") -> None:
        """
        Calculate the normal of a surface defined by points `v1`, `v2` and `v3` and store it in `dest`.

        Arguments
        - v0: the first position
        - v1: the second position
        - v2: the third position
        - dest: will hold the result
        """
        ...


    @staticmethod
    def normal(v0X: float, v0Y: float, v0Z: float, v1X: float, v1Y: float, v1Z: float, v2X: float, v2Y: float, v2Z: float, dest: "Vector3f") -> None:
        """
        Calculate the normal of a surface defined by points `(v1X, v1Y, v1Z)`, `(v2X, v2Y, v2Z)` and `(v3X, v3Y, v3Z)`
        and store it in `dest`.

        Arguments
        - v0X: the x coordinate of the first position
        - v0Y: the y coordinate of the first position
        - v0Z: the z coordinate of the first position
        - v1X: the x coordinate of the second position
        - v1Y: the y coordinate of the second position
        - v1Z: the z coordinate of the second position
        - v2X: the x coordinate of the third position
        - v2Y: the y coordinate of the third position
        - v2Z: the z coordinate of the third position
        - dest: will hold the result
        """
        ...


    @staticmethod
    def tangent(v1: "Vector3fc", uv1: "Vector2fc", v2: "Vector3fc", uv2: "Vector2fc", v3: "Vector3fc", uv3: "Vector2fc", dest: "Vector3f") -> None:
        """
        Calculate the surface tangent for the three supplied vertices and UV coordinates and store the result in `dest`.

        Arguments
        - v1: XYZ of first vertex
        - uv1: UV of first vertex
        - v2: XYZ of second vertex
        - uv2: UV of second vertex
        - v3: XYZ of third vertex
        - uv3: UV of third vertex
        - dest: the tangent will be stored here
        """
        ...


    @staticmethod
    def bitangent(v1: "Vector3fc", uv1: "Vector2fc", v2: "Vector3fc", uv2: "Vector2fc", v3: "Vector3fc", uv3: "Vector2fc", dest: "Vector3f") -> None:
        """
        Calculate the surface bitangent for the three supplied vertices and UV coordinates and store the result in `dest`.

        Arguments
        - v1: XYZ of first vertex
        - uv1: UV of first vertex
        - v2: XYZ of second vertex
        - uv2: UV of second vertex
        - v3: XYZ of third vertex
        - uv3: UV of third vertex
        - dest: the binormal will be stored here
        """
        ...


    @staticmethod
    def tangentBitangent(v1: "Vector3fc", uv1: "Vector2fc", v2: "Vector3fc", uv2: "Vector2fc", v3: "Vector3fc", uv3: "Vector2fc", destTangent: "Vector3f", destBitangent: "Vector3f") -> None:
        """
        Calculate the surface tangent and bitangent for the three supplied vertices and UV coordinates and store the result in `dest`.

        Arguments
        - v1: XYZ of first vertex
        - uv1: UV of first vertex
        - v2: XYZ of second vertex
        - uv2: UV of second vertex
        - v3: XYZ of third vertex
        - uv3: UV of third vertex
        - destTangent: the tangent will be stored here
        - destBitangent: the bitangent will be stored here
        """
        ...
