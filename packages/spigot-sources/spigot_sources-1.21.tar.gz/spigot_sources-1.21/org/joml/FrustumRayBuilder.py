"""
Python module generated from Java source file org.joml.FrustumRayBuilder

Java source file obtained from artifact joml version 1.10.5

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.joml import *
from typing import Any, Callable, Iterable, Tuple


class FrustumRayBuilder:
    """
    Provides methods to compute rays through an arbitrary perspective transformation defined by a Matrix4fc.
    
    This can be used to compute the eye-rays in simple software-based raycasting/raytracing.
    
    To obtain the origin of the rays call .origin(Vector3f).
    Then to compute the directions of subsequent rays use .dir(float, float, Vector3f).

    Author(s)
    - Kai Burjack
    """

    def __init__(self):
        """
        Create a new FrustumRayBuilder with an undefined frustum.
        
        Before obtaining ray directions, make sure to define the frustum using .set(Matrix4fc).
        """
        ...


    def __init__(self, m: "Matrix4fc"):
        """
        Create a new FrustumRayBuilder from the given Matrix4fc matrix by extracing the matrix's frustum.

        Arguments
        - m: the Matrix4fc to create the frustum from
        """
        ...


    def set(self, m: "Matrix4fc") -> "FrustumRayBuilder":
        """
        Update the stored frustum corner rays and origin of `this` FrustumRayBuilder with the given Matrix4fc matrix.
        
        Reference: <a href="http://gamedevs.org/uploads/fast-extraction-viewing-frustum-planes-from-world-view-projection-matrix.pdf">
        Fast Extraction of Viewing Frustum Planes from the World-View-Projection Matrix</a>
        
        Reference: <a href="http://geomalgorithms.com/a05-_intersect-1.html">http://geomalgorithms.com</a>

        Arguments
        - m: the Matrix4fc matrix to update the frustum corner rays and origin with

        Returns
        - this
        """
        ...


    def origin(self, origin: "Vector3f") -> "Vector3fc":
        """
        Store the eye/origin of the perspective frustum in the given `origin`.

        Arguments
        - origin: will hold the perspective origin

        Returns
        - the `origin` vector
        """
        ...


    def dir(self, x: float, y: float, dir: "Vector3f") -> "Vector3fc":
        """
        Obtain the normalized direction of a ray starting at the center of the coordinate system and going 
        through the near frustum plane.
        
        The parameters `x` and `y` are used to interpolate the generated ray direction
        from the bottom-left to the top-right frustum corners.

        Arguments
        - x: the interpolation factor along the left-to-right frustum planes, within `[0..1]`
        - y: the interpolation factor along the bottom-to-top frustum planes, within `[0..1]`
        - dir: will hold the normalized ray direction

        Returns
        - the `dir` vector
        """
        ...
