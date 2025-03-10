"""
Python module generated from Java source file org.joml.RayAabIntersection

Java source file obtained from artifact joml version 1.10.5

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.joml import *
from typing import Any, Callable, Iterable, Tuple


class RayAabIntersection:
    """
    This is an implementation of the <a
    href="http://www.cg.cs.tu-bs.de/media/publications/fast-rayaxis-aligned-bounding-box-overlap-tests-using-ray-slopes.pdf">Fast Ray/Axis-Aligned Bounding Box
    Overlap Tests using Ray Slopes</a> paper.
    
    It is an efficient implementation when testing many axis-aligned boxes against the same ray.
    
    This class is thread-safe and can be used in a multithreaded environment when testing many axis-aligned boxes against the same ray concurrently.

    Author(s)
    - Kai Burjack
    """

    def __init__(self):
        """
        Create a new RayAabIntersection without initializing a ray.
        
        Before using the .test(float, float, float, float, float, float) intersect() method,
        the method .set(float, float, float, float, float, float) set() must be called in order to
        initialize the created RayAabIntersection instance with a ray.

        See
        - .set(float, float, float, float, float, float)
        """
        ...


    def __init__(self, originX: float, originY: float, originZ: float, dirX: float, dirY: float, dirZ: float):
        """
        Create a new RayAabIntersection and initialize it with a ray with origin `(originX, originY, originZ)`
        and direction `(dirX, dirY, dirZ)`.
        
        In order to change the direction and/or origin of the ray later, use .set(float, float, float, float, float, float) set().

        Arguments
        - originX: the x coordinate of the origin
        - originY: the y coordinate of the origin
        - originZ: the z coordinate of the origin
        - dirX: the x coordinate of the direction
        - dirY: the y coordinate of the direction
        - dirZ: the z coordinate of the direction

        See
        - .set(float, float, float, float, float, float)
        """
        ...


    def set(self, originX: float, originY: float, originZ: float, dirX: float, dirY: float, dirZ: float) -> None:
        """
        Update the ray stored by this RayAabIntersection with the new origin `(originX, originY, originZ)`
        and direction `(dirX, dirY, dirZ)`.

        Arguments
        - originX: the x coordinate of the ray origin
        - originY: the y coordinate of the ray origin
        - originZ: the z coordinate of the ray origin
        - dirX: the x coordinate of the ray direction
        - dirY: the y coordinate of the ray direction
        - dirZ: the z coordinate of the ray direction
        """
        ...


    def test(self, minX: float, minY: float, minZ: float, maxX: float, maxY: float, maxZ: float) -> bool:
        """
        Test whether the ray stored in this RayAabIntersection intersect the axis-aligned box
        given via its minimum corner `(minX, minY, minZ)` and its maximum corner `(maxX, maxY, maxZ)`.
        
        This implementation uses a tableswitch to dispatch to the correct intersection method.
        
        This method is thread-safe and can be used to test many axis-aligned boxes concurrently.

        Arguments
        - minX: the x coordinate of the minimum corner
        - minY: the y coordinate of the minimum corner
        - minZ: the z coordinate of the minimum corner
        - maxX: the x coordinate of the maximum corner
        - maxY: the y coordinate of the maximum corner
        - maxZ: the z coordinate of the maximum corner

        Returns
        - `True` iff the ray intersects the given axis-aligned box; `False` otherwise
        """
        ...
