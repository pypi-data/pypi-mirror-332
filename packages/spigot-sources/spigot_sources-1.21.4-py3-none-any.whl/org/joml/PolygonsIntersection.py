"""
Python module generated from Java source file org.joml.PolygonsIntersection

Java source file obtained from artifact joml version 1.10.8

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util import BitSet
from java.util import Collections
from java.util import Comparator
from org.joml import *
from typing import Any, Callable, Iterable, Tuple


class PolygonsIntersection:
    """
    Class for polygon/point intersection tests when testing many points against one or many static concave or convex, simple polygons.
    
    This is an implementation of the algorithm described in <a href="http://alienryderflex.com/polygon/">http://alienryderflex.com</a> and augmented with using a
    custom interval tree to avoid testing all polygon edges against a point, but only those that intersect the imaginary ray along the same y co-ordinate of the
    search point. This algorithm additionally also supports multiple polygons.
    
    This class is thread-safe and can be used in a multithreaded environment when testing many points against the same polygon concurrently.
    
    Reference: <a href="http://alienryderflex.com/polygon/">http://alienryderflex.com</a>

    Author(s)
    - Kai Burjack
    """

    def __init__(self, verticesXY: list[float], polygons: list[int], count: int):
        """
        Create a new PolygonsIntersection object with the given polygon vertices.
        
        The `verticesXY` array contains the x and y coordinates of all vertices. This array will not be copied so its content must remain constant for
        as long as the PolygonPointIntersection is used with it.

        Arguments
        - verticesXY: contains the x and y coordinates of all vertices
        - polygons: defines the start vertices of a new polygon. The first vertex of the first polygon is always the
                   vertex with index 0. In order to define a hole simply define a polygon that is completely inside another polygon
        - count: the number of vertices to use from the `verticesXY` array, staring with index 0
        """
        ...


    def testPoint(self, x: float, y: float) -> bool:
        """
        Test whether the given point `(x, y)` lies inside any polygon stored in this PolygonsIntersection object.
        
        This method is thread-safe and can be used to test many points concurrently.
        
        In order to obtain the index of the polygon the point is inside of, use .testPoint(float, float, BitSet)

        Arguments
        - x: the x coordinate of the point to test
        - y: the y coordinate of the point to test

        Returns
        - `True` iff the point lies inside any polygon; `False` otherwise

        See
        - .testPoint(float, float, BitSet)
        """
        ...


    def testPoint(self, x: float, y: float, inPolys: "BitSet") -> bool:
        """
        Test whether the given point `(x, y)` lies inside any polygon stored in this PolygonsIntersection object.
        
        This method is thread-safe and can be used to test many points concurrently.

        Arguments
        - x: the x coordinate of the point to test
        - y: the y coordinate of the point to test
        - inPolys: if not `null` then the *i*-th bit is set if the given point is inside the *i*-th polygon

        Returns
        - `True` iff the point lies inside the polygon and not inside a hole; `False` otherwise
        """
        ...
