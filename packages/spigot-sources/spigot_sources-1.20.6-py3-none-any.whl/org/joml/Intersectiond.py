"""
Python module generated from Java source file org.joml.Intersectiond

Java source file obtained from artifact joml version 1.10.5

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.joml import *
from typing import Any, Callable, Iterable, Tuple


class Intersectiond:
    """
    Contains intersection and distance tests for some 2D and 3D geometric primitives.

    Author(s)
    - Kai Burjack
    """

    POINT_ON_TRIANGLE_VERTEX_0 = 1
    """
    Return value of
    .findClosestPointOnTriangle(double, double, double, double, double, double, double, double, double, double, double, double, Vector3d),
    .findClosestPointOnTriangle(Vector3dc, Vector3dc, Vector3dc, Vector3dc, Vector3d),
    .findClosestPointOnTriangle(double, double, double, double, double, double, double, double, Vector2d) and
    .findClosestPointOnTriangle(Vector2dc, Vector2dc, Vector2dc, Vector2dc, Vector2d) or
    .intersectSweptSphereTriangle
    to signal that the closest point is the first vertex of the triangle.
    """
    POINT_ON_TRIANGLE_VERTEX_1 = 2
    """
    Return value of
    .findClosestPointOnTriangle(double, double, double, double, double, double, double, double, double, double, double, double, Vector3d),
    .findClosestPointOnTriangle(Vector3dc, Vector3dc, Vector3dc, Vector3dc, Vector3d),
    .findClosestPointOnTriangle(double, double, double, double, double, double, double, double, Vector2d) and
    .findClosestPointOnTriangle(Vector2dc, Vector2dc, Vector2dc, Vector2dc, Vector2d) or
    .intersectSweptSphereTriangle
    to signal that the closest point is the second vertex of the triangle.
    """
    POINT_ON_TRIANGLE_VERTEX_2 = 3
    """
    Return value of
    .findClosestPointOnTriangle(double, double, double, double, double, double, double, double, double, double, double, double, Vector3d),
    .findClosestPointOnTriangle(Vector3dc, Vector3dc, Vector3dc, Vector3dc, Vector3d),
    .findClosestPointOnTriangle(double, double, double, double, double, double, double, double, Vector2d) and
    .findClosestPointOnTriangle(Vector2dc, Vector2dc, Vector2dc, Vector2dc, Vector2d) or
    .intersectSweptSphereTriangle
    to signal that the closest point is the third vertex of the triangle.
    """
    POINT_ON_TRIANGLE_EDGE_01 = 4
    """
    Return value of
    .findClosestPointOnTriangle(double, double, double, double, double, double, double, double, double, double, double, double, Vector3d),
    .findClosestPointOnTriangle(Vector3dc, Vector3dc, Vector3dc, Vector3dc, Vector3d),
    .findClosestPointOnTriangle(double, double, double, double, double, double, double, double, Vector2d) and
    .findClosestPointOnTriangle(Vector2dc, Vector2dc, Vector2dc, Vector2dc, Vector2d) or
    .intersectSweptSphereTriangle
    to signal that the closest point lies on the edge between the first and second vertex of the triangle.
    """
    POINT_ON_TRIANGLE_EDGE_12 = 5
    """
    Return value of
    .findClosestPointOnTriangle(double, double, double, double, double, double, double, double, double, double, double, double, Vector3d),
    .findClosestPointOnTriangle(Vector3dc, Vector3dc, Vector3dc, Vector3dc, Vector3d),
    .findClosestPointOnTriangle(double, double, double, double, double, double, double, double, Vector2d) and
    .findClosestPointOnTriangle(Vector2dc, Vector2dc, Vector2dc, Vector2dc, Vector2d) or
    .intersectSweptSphereTriangle
    to signal that the closest point lies on the edge between the second and third vertex of the triangle.
    """
    POINT_ON_TRIANGLE_EDGE_20 = 6
    """
    Return value of
    .findClosestPointOnTriangle(double, double, double, double, double, double, double, double, double, double, double, double, Vector3d),
    .findClosestPointOnTriangle(Vector3dc, Vector3dc, Vector3dc, Vector3dc, Vector3d),
    .findClosestPointOnTriangle(double, double, double, double, double, double, double, double, Vector2d) and
    .findClosestPointOnTriangle(Vector2dc, Vector2dc, Vector2dc, Vector2dc, Vector2d) or
    .intersectSweptSphereTriangle
    to signal that the closest point lies on the edge between the third and first vertex of the triangle.
    """
    POINT_ON_TRIANGLE_FACE = 7
    """
    Return value of
    .findClosestPointOnTriangle(double, double, double, double, double, double, double, double, double, double, double, double, Vector3d),
    .findClosestPointOnTriangle(Vector3dc, Vector3dc, Vector3dc, Vector3dc, Vector3d),
    .findClosestPointOnTriangle(double, double, double, double, double, double, double, double, Vector2d) and
    .findClosestPointOnTriangle(Vector2dc, Vector2dc, Vector2dc, Vector2dc, Vector2d) or 
    .intersectSweptSphereTriangle
    to signal that the closest point lies on the face of the triangle.
    """
    AAR_SIDE_MINX = 0
    """
    Return value of .intersectRayAar(double, double, double, double, double, double, double, double, Vector2d) and
    .intersectRayAar(Vector2dc, Vector2dc, Vector2dc, Vector2dc, Vector2d)
    to indicate that the ray intersects the side of the axis-aligned rectangle with the minimum x coordinate.
    """
    AAR_SIDE_MINY = 1
    """
    Return value of .intersectRayAar(double, double, double, double, double, double, double, double, Vector2d) and
    .intersectRayAar(Vector2dc, Vector2dc, Vector2dc, Vector2dc, Vector2d)
    to indicate that the ray intersects the side of the axis-aligned rectangle with the minimum y coordinate.
    """
    AAR_SIDE_MAXX = 2
    """
    Return value of .intersectRayAar(double, double, double, double, double, double, double, double, Vector2d) and
    .intersectRayAar(Vector2dc, Vector2dc, Vector2dc, Vector2dc, Vector2d)
    to indicate that the ray intersects the side of the axis-aligned rectangle with the maximum x coordinate.
    """
    AAR_SIDE_MAXY = 3
    """
    Return value of .intersectRayAar(double, double, double, double, double, double, double, double, Vector2d) and
    .intersectRayAar(Vector2dc, Vector2dc, Vector2dc, Vector2dc, Vector2d)
    to indicate that the ray intersects the side of the axis-aligned rectangle with the maximum y coordinate.
    """
    OUTSIDE = -1
    """
    Return value of .intersectLineSegmentAab(double, double, double, double, double, double, double, double, double, double, double, double, Vector2d) and
    .intersectLineSegmentAab(Vector3dc, Vector3dc, Vector3dc, Vector3dc, Vector2d) to indicate that the line segment does not intersect the axis-aligned box;
    or return value of .intersectLineSegmentAar(double, double, double, double, double, double, double, double, Vector2d) and
    .intersectLineSegmentAar(Vector2dc, Vector2dc, Vector2dc, Vector2dc, Vector2d) to indicate that the line segment does not intersect the axis-aligned rectangle.
    """
    ONE_INTERSECTION = 1
    """
    Return value of .intersectLineSegmentAab(double, double, double, double, double, double, double, double, double, double, double, double, Vector2d) and
    .intersectLineSegmentAab(Vector3dc, Vector3dc, Vector3dc, Vector3dc, Vector2d) to indicate that one end point of the line segment lies inside of the axis-aligned box;
    or return value of .intersectLineSegmentAar(double, double, double, double, double, double, double, double, Vector2d) and
    .intersectLineSegmentAar(Vector2dc, Vector2dc, Vector2dc, Vector2dc, Vector2d) to indicate that one end point of the line segment lies inside of the axis-aligned rectangle.
    """
    TWO_INTERSECTION = 2
    """
    Return value of .intersectLineSegmentAab(double, double, double, double, double, double, double, double, double, double, double, double, Vector2d) and
    .intersectLineSegmentAab(Vector3dc, Vector3dc, Vector3dc, Vector3dc, Vector2d) to indicate that the line segment intersects two sides of the axis-aligned box
    or lies on an edge or a side of the box;
    or return value of .intersectLineSegmentAar(double, double, double, double, double, double, double, double, Vector2d) and
    .intersectLineSegmentAar(Vector2dc, Vector2dc, Vector2dc, Vector2dc, Vector2d) to indicate that the line segment intersects two edges of the axis-aligned rectangle
    or lies on an edge of the rectangle.
    """
    INSIDE = 3
    """
    Return value of .intersectLineSegmentAab(double, double, double, double, double, double, double, double, double, double, double, double, Vector2d) and
    .intersectLineSegmentAab(Vector3dc, Vector3dc, Vector3dc, Vector3dc, Vector2d) to indicate that the line segment lies completely inside of the axis-aligned box;
    or return value of .intersectLineSegmentAar(double, double, double, double, double, double, double, double, Vector2d) and
    .intersectLineSegmentAar(Vector2dc, Vector2dc, Vector2dc, Vector2dc, Vector2d) to indicate that the line segment lies completely inside of the axis-aligned rectangle.
    """


    @staticmethod
    def testPlaneSphere(a: float, b: float, c: float, d: float, centerX: float, centerY: float, centerZ: float, radius: float) -> bool:
        """
        Test whether the plane with the general plane equation *a*x + b*y + c*z + d = 0* intersects the sphere with center
        `(centerX, centerY, centerZ)` and `radius`.
        
        Reference: <a href="http://math.stackexchange.com/questions/943383/determine-circle-of-intersection-of-plane-and-sphere">http://math.stackexchange.com</a>

        Arguments
        - a: the x factor in the plane equation
        - b: the y factor in the plane equation
        - c: the z factor in the plane equation
        - d: the constant in the plane equation
        - centerX: the x coordinate of the sphere's center
        - centerY: the y coordinate of the sphere's center
        - centerZ: the z coordinate of the sphere's center
        - radius: the radius of the sphere

        Returns
        - `True` iff the plane intersects the sphere; `False` otherwise
        """
        ...


    @staticmethod
    def intersectPlaneSphere(a: float, b: float, c: float, d: float, centerX: float, centerY: float, centerZ: float, radius: float, intersectionCenterAndRadius: "Vector4d") -> bool:
        """
        Test whether the plane with the general plane equation *a*x + b*y + c*z + d = 0* intersects the sphere with center
        `(centerX, centerY, centerZ)` and `radius`, and store the center of the circle of
        intersection in the `(x, y, z)` components of the supplied vector and the radius of that circle in the w component.
        
        Reference: <a href="http://math.stackexchange.com/questions/943383/determine-circle-of-intersection-of-plane-and-sphere">http://math.stackexchange.com</a>

        Arguments
        - a: the x factor in the plane equation
        - b: the y factor in the plane equation
        - c: the z factor in the plane equation
        - d: the constant in the plane equation
        - centerX: the x coordinate of the sphere's center
        - centerY: the y coordinate of the sphere's center
        - centerZ: the z coordinate of the sphere's center
        - radius: the radius of the sphere
        - intersectionCenterAndRadius: will hold the center of the circle of intersection in the `(x, y, z)` components and the radius in the w component

        Returns
        - `True` iff the plane intersects the sphere; `False` otherwise
        """
        ...


    @staticmethod
    def intersectPlaneSweptSphere(a: float, b: float, c: float, d: float, cX: float, cY: float, cZ: float, radius: float, vX: float, vY: float, vZ: float, pointAndTime: "Vector4d") -> bool:
        """
        Test whether the plane with the general plane equation *a*x + b*y + c*z + d = 0* intersects the moving sphere with center
        `(cX, cY, cZ)`, `radius` and velocity `(vX, vY, vZ)`, and store the point of intersection
        in the `(x, y, z)` components of the supplied vector and the time of intersection in the w component.
        
        The normal vector `(a, b, c)` of the plane equation needs to be normalized.
        
        Reference: Book "Real-Time Collision Detection" chapter 5.5.3 "Intersecting Moving Sphere Against Plane"

        Arguments
        - a: the x factor in the plane equation
        - b: the y factor in the plane equation
        - c: the z factor in the plane equation
        - d: the constant in the plane equation
        - cX: the x coordinate of the center position of the sphere at t=0
        - cY: the y coordinate of the center position of the sphere at t=0
        - cZ: the z coordinate of the center position of the sphere at t=0
        - radius: the sphere's radius
        - vX: the x component of the velocity of the sphere
        - vY: the y component of the velocity of the sphere
        - vZ: the z component of the velocity of the sphere
        - pointAndTime: will hold the point and time of intersection (if any)

        Returns
        - `True` iff the sphere intersects the plane; `False` otherwise
        """
        ...


    @staticmethod
    def testPlaneSweptSphere(a: float, b: float, c: float, d: float, t0X: float, t0Y: float, t0Z: float, r: float, t1X: float, t1Y: float, t1Z: float) -> bool:
        """
        Test whether the plane with the general plane equation *a*x + b*y + c*z + d = 0* intersects the sphere moving from center
        position `(t0X, t0Y, t0Z)` to `(t1X, t1Y, t1Z)` and having the given `radius`.
        
        The normal vector `(a, b, c)` of the plane equation needs to be normalized.
        
        Reference: Book "Real-Time Collision Detection" chapter 5.5.3 "Intersecting Moving Sphere Against Plane"

        Arguments
        - a: the x factor in the plane equation
        - b: the y factor in the plane equation
        - c: the z factor in the plane equation
        - d: the constant in the plane equation
        - t0X: the x coordinate of the start position of the sphere
        - t0Y: the y coordinate of the start position of the sphere
        - t0Z: the z coordinate of the start position of the sphere
        - r: the sphere's radius
        - t1X: the x coordinate of the end position of the sphere
        - t1Y: the y coordinate of the end position of the sphere
        - t1Z: the z coordinate of the end position of the sphere

        Returns
        - `True` if the sphere intersects the plane; `False` otherwise
        """
        ...


    @staticmethod
    def testAabPlane(minX: float, minY: float, minZ: float, maxX: float, maxY: float, maxZ: float, a: float, b: float, c: float, d: float) -> bool:
        """
        Test whether the axis-aligned box with minimum corner `(minX, minY, minZ)` and maximum corner `(maxX, maxY, maxZ)`
        intersects the plane with the general equation *a*x + b*y + c*z + d = 0*.
        
        Reference: <a href="http://www.lighthouse3d.com/tutorials/view-frustum-culling/geometric-approach-testing-boxes-ii/">http://www.lighthouse3d.com</a> ("Geometric Approach - Testing Boxes II")

        Arguments
        - minX: the x coordinate of the minimum corner of the axis-aligned box
        - minY: the y coordinate of the minimum corner of the axis-aligned box
        - minZ: the z coordinate of the minimum corner of the axis-aligned box
        - maxX: the x coordinate of the maximum corner of the axis-aligned box
        - maxY: the y coordinate of the maximum corner of the axis-aligned box
        - maxZ: the z coordinate of the maximum corner of the axis-aligned box
        - a: the x factor in the plane equation
        - b: the y factor in the plane equation
        - c: the z factor in the plane equation
        - d: the constant in the plane equation

        Returns
        - `True` iff the axis-aligned box intersects the plane; `False` otherwise
        """
        ...


    @staticmethod
    def testAabPlane(min: "Vector3dc", max: "Vector3dc", a: float, b: float, c: float, d: float) -> bool:
        """
        Test whether the axis-aligned box with minimum corner `min` and maximum corner `max`
        intersects the plane with the general equation *a*x + b*y + c*z + d = 0*.
        
        Reference: <a href="http://www.lighthouse3d.com/tutorials/view-frustum-culling/geometric-approach-testing-boxes-ii/">http://www.lighthouse3d.com</a> ("Geometric Approach - Testing Boxes II")

        Arguments
        - min: the minimum corner of the axis-aligned box
        - max: the maximum corner of the axis-aligned box
        - a: the x factor in the plane equation
        - b: the y factor in the plane equation
        - c: the z factor in the plane equation
        - d: the constant in the plane equation

        Returns
        - `True` iff the axis-aligned box intersects the plane; `False` otherwise
        """
        ...


    @staticmethod
    def testAabAab(minXA: float, minYA: float, minZA: float, maxXA: float, maxYA: float, maxZA: float, minXB: float, minYB: float, minZB: float, maxXB: float, maxYB: float, maxZB: float) -> bool:
        """
        Test whether the axis-aligned box with minimum corner `(minXA, minYA, minZA)` and maximum corner `(maxXA, maxYA, maxZA)`
        intersects the axis-aligned box with minimum corner `(minXB, minYB, minZB)` and maximum corner `(maxXB, maxYB, maxZB)`.

        Arguments
        - minXA: the x coordinate of the minimum corner of the first axis-aligned box
        - minYA: the y coordinate of the minimum corner of the first axis-aligned box
        - minZA: the z coordinate of the minimum corner of the first axis-aligned box
        - maxXA: the x coordinate of the maximum corner of the first axis-aligned box
        - maxYA: the y coordinate of the maximum corner of the first axis-aligned box
        - maxZA: the z coordinate of the maximum corner of the first axis-aligned box
        - minXB: the x coordinate of the minimum corner of the second axis-aligned box
        - minYB: the y coordinate of the minimum corner of the second axis-aligned box
        - minZB: the z coordinate of the minimum corner of the second axis-aligned box
        - maxXB: the x coordinate of the maximum corner of the second axis-aligned box
        - maxYB: the y coordinate of the maximum corner of the second axis-aligned box
        - maxZB: the z coordinate of the maximum corner of the second axis-aligned box

        Returns
        - `True` iff both axis-aligned boxes intersect; `False` otherwise
        """
        ...


    @staticmethod
    def testAabAab(minA: "Vector3dc", maxA: "Vector3dc", minB: "Vector3dc", maxB: "Vector3dc") -> bool:
        """
        Test whether the axis-aligned box with minimum corner `minA` and maximum corner `maxA`
        intersects the axis-aligned box with minimum corner `minB` and maximum corner `maxB`.

        Arguments
        - minA: the minimum corner of the first axis-aligned box
        - maxA: the maximum corner of the first axis-aligned box
        - minB: the minimum corner of the second axis-aligned box
        - maxB: the maximum corner of the second axis-aligned box

        Returns
        - `True` iff both axis-aligned boxes intersect; `False` otherwise
        """
        ...


    @staticmethod
    def testObOb(b0c: "Vector3d", b0uX: "Vector3d", b0uY: "Vector3d", b0uZ: "Vector3d", b0hs: "Vector3d", b1c: "Vector3d", b1uX: "Vector3d", b1uY: "Vector3d", b1uZ: "Vector3d", b1hs: "Vector3d") -> bool:
        """
        Test whether two oriented boxes given via their center position, orientation and half-size, intersect.
        
        The orientation of a box is given as three unit vectors spanning the local orthonormal basis of the box.
        
        The size is given as the half-size along each of the unit vectors defining the orthonormal basis.
        
        Reference: Book "Real-Time Collision Detection" chapter 4.4.1 "OBB-OBB Intersection"

        Arguments
        - b0c: the center of the first box
        - b0uX: the local X unit vector of the first box
        - b0uY: the local Y unit vector of the first box
        - b0uZ: the local Z unit vector of the first box
        - b0hs: the half-size of the first box
        - b1c: the center of the second box
        - b1uX: the local X unit vector of the second box
        - b1uY: the local Y unit vector of the second box
        - b1uZ: the local Z unit vector of the second box
        - b1hs: the half-size of the second box

        Returns
        - `True` if both boxes intersect; `False` otherwise
        """
        ...


    @staticmethod
    def testObOb(b0cX: float, b0cY: float, b0cZ: float, b0uXx: float, b0uXy: float, b0uXz: float, b0uYx: float, b0uYy: float, b0uYz: float, b0uZx: float, b0uZy: float, b0uZz: float, b0hsX: float, b0hsY: float, b0hsZ: float, b1cX: float, b1cY: float, b1cZ: float, b1uXx: float, b1uXy: float, b1uXz: float, b1uYx: float, b1uYy: float, b1uYz: float, b1uZx: float, b1uZy: float, b1uZz: float, b1hsX: float, b1hsY: float, b1hsZ: float) -> bool:
        """
        Test whether two oriented boxes given via their center position, orientation and half-size, intersect.
        
        The orientation of a box is given as three unit vectors spanning the local orthonormal basis of the box.
        
        The size is given as the half-size along each of the unit vectors defining the orthonormal basis.
        
        Reference: Book "Real-Time Collision Detection" chapter 4.4.1 "OBB-OBB Intersection"

        Arguments
        - b0cX: the x coordinate of the center of the first box
        - b0cY: the y coordinate of the center of the first box
        - b0cZ: the z coordinate of the center of the first box
        - b0uXx: the x coordinate of the local X unit vector of the first box
        - b0uXy: the y coordinate of the local X unit vector of the first box
        - b0uXz: the z coordinate of the local X unit vector of the first box
        - b0uYx: the x coordinate of the local Y unit vector of the first box
        - b0uYy: the y coordinate of the local Y unit vector of the first box
        - b0uYz: the z coordinate of the local Y unit vector of the first box
        - b0uZx: the x coordinate of the local Z unit vector of the first box
        - b0uZy: the y coordinate of the local Z unit vector of the first box
        - b0uZz: the z coordinate of the local Z unit vector of the first box
        - b0hsX: the half-size of the first box along its local X axis
        - b0hsY: the half-size of the first box along its local Y axis
        - b0hsZ: the half-size of the first box along its local Z axis
        - b1cX: the x coordinate of the center of the second box
        - b1cY: the y coordinate of the center of the second box
        - b1cZ: the z coordinate of the center of the second box
        - b1uXx: the x coordinate of the local X unit vector of the second box
        - b1uXy: the y coordinate of the local X unit vector of the second box
        - b1uXz: the z coordinate of the local X unit vector of the second box
        - b1uYx: the x coordinate of the local Y unit vector of the second box
        - b1uYy: the y coordinate of the local Y unit vector of the second box
        - b1uYz: the z coordinate of the local Y unit vector of the second box
        - b1uZx: the x coordinate of the local Z unit vector of the second box
        - b1uZy: the y coordinate of the local Z unit vector of the second box
        - b1uZz: the z coordinate of the local Z unit vector of the second box
        - b1hsX: the half-size of the second box along its local X axis
        - b1hsY: the half-size of the second box along its local Y axis
        - b1hsZ: the half-size of the second box along its local Z axis

        Returns
        - `True` if both boxes intersect; `False` otherwise
        """
        ...


    @staticmethod
    def intersectSphereSphere(aX: float, aY: float, aZ: float, radiusSquaredA: float, bX: float, bY: float, bZ: float, radiusSquaredB: float, centerAndRadiusOfIntersectionCircle: "Vector4d") -> bool:
        """
        Test whether the one sphere with center `(aX, aY, aZ)` and square radius `radiusSquaredA` intersects the other
        sphere with center `(bX, bY, bZ)` and square radius `radiusSquaredB`, and store the center of the circle of
        intersection in the `(x, y, z)` components of the supplied vector and the radius of that circle in the w component.
        
        The normal vector of the circle of intersection can simply be obtained by subtracting the center of either sphere from the other.
        
        Reference: <a href="http://gamedev.stackexchange.com/questions/75756/sphere-sphere-intersection-and-circle-sphere-intersection">http://gamedev.stackexchange.com</a>

        Arguments
        - aX: the x coordinate of the first sphere's center
        - aY: the y coordinate of the first sphere's center
        - aZ: the z coordinate of the first sphere's center
        - radiusSquaredA: the square of the first sphere's radius
        - bX: the x coordinate of the second sphere's center
        - bY: the y coordinate of the second sphere's center
        - bZ: the z coordinate of the second sphere's center
        - radiusSquaredB: the square of the second sphere's radius
        - centerAndRadiusOfIntersectionCircle: will hold the center of the circle of intersection in the `(x, y, z)` components and the radius in the w component

        Returns
        - `True` iff both spheres intersect; `False` otherwise
        """
        ...


    @staticmethod
    def intersectSphereSphere(centerA: "Vector3dc", radiusSquaredA: float, centerB: "Vector3dc", radiusSquaredB: float, centerAndRadiusOfIntersectionCircle: "Vector4d") -> bool:
        """
        Test whether the one sphere with center `centerA` and square radius `radiusSquaredA` intersects the other
        sphere with center `centerB` and square radius `radiusSquaredB`, and store the center of the circle of
        intersection in the `(x, y, z)` components of the supplied vector and the radius of that circle in the w component.
        
        The normal vector of the circle of intersection can simply be obtained by subtracting the center of either sphere from the other.
        
        Reference: <a href="http://gamedev.stackexchange.com/questions/75756/sphere-sphere-intersection-and-circle-sphere-intersection">http://gamedev.stackexchange.com</a>

        Arguments
        - centerA: the first sphere's center
        - radiusSquaredA: the square of the first sphere's radius
        - centerB: the second sphere's center
        - radiusSquaredB: the square of the second sphere's radius
        - centerAndRadiusOfIntersectionCircle: will hold the center of the circle of intersection in the `(x, y, z)` components and the radius in the w component

        Returns
        - `True` iff both spheres intersect; `False` otherwise
        """
        ...


    @staticmethod
    def intersectSphereTriangle(sX: float, sY: float, sZ: float, sR: float, v0X: float, v0Y: float, v0Z: float, v1X: float, v1Y: float, v1Z: float, v2X: float, v2Y: float, v2Z: float, result: "Vector3d") -> int:
        """
        Test whether the given sphere with center `(sX, sY, sZ)` intersects the triangle given by its three vertices, and if they intersect
        store the point of intersection into `result`.
        
        This method also returns whether the point of intersection is on one of the triangle's vertices, edges or on the face.
        
        Reference: Book "Real-Time Collision Detection" chapter 5.2.7 "Testing Sphere Against Triangle"

        Arguments
        - sX: the x coordinate of the sphere's center
        - sY: the y coordinate of the sphere's center
        - sZ: the z coordinate of the sphere's center
        - sR: the sphere's radius
        - v0X: the x coordinate of the first vertex of the triangle
        - v0Y: the y coordinate of the first vertex of the triangle
        - v0Z: the z coordinate of the first vertex of the triangle
        - v1X: the x coordinate of the second vertex of the triangle
        - v1Y: the y coordinate of the second vertex of the triangle
        - v1Z: the z coordinate of the second vertex of the triangle
        - v2X: the x coordinate of the third vertex of the triangle
        - v2Y: the y coordinate of the third vertex of the triangle
        - v2Z: the z coordinate of the third vertex of the triangle
        - result: will hold the point of intersection

        Returns
        - one of .POINT_ON_TRIANGLE_VERTEX_0, .POINT_ON_TRIANGLE_VERTEX_1, .POINT_ON_TRIANGLE_VERTEX_2,
                       .POINT_ON_TRIANGLE_EDGE_01, .POINT_ON_TRIANGLE_EDGE_12, .POINT_ON_TRIANGLE_EDGE_20 or
                       .POINT_ON_TRIANGLE_FACE or `0`
        """
        ...


    @staticmethod
    def testSphereSphere(aX: float, aY: float, aZ: float, radiusSquaredA: float, bX: float, bY: float, bZ: float, radiusSquaredB: float) -> bool:
        """
        Test whether the one sphere with center `(aX, aY, aZ)` and square radius `radiusSquaredA` intersects the other
        sphere with center `(bX, bY, bZ)` and square radius `radiusSquaredB`.
        
        Reference: <a href="http://gamedev.stackexchange.com/questions/75756/sphere-sphere-intersection-and-circle-sphere-intersection">http://gamedev.stackexchange.com</a>

        Arguments
        - aX: the x coordinate of the first sphere's center
        - aY: the y coordinate of the first sphere's center
        - aZ: the z coordinate of the first sphere's center
        - radiusSquaredA: the square of the first sphere's radius
        - bX: the x coordinate of the second sphere's center
        - bY: the y coordinate of the second sphere's center
        - bZ: the z coordinate of the second sphere's center
        - radiusSquaredB: the square of the second sphere's radius

        Returns
        - `True` iff both spheres intersect; `False` otherwise
        """
        ...


    @staticmethod
    def testSphereSphere(centerA: "Vector3dc", radiusSquaredA: float, centerB: "Vector3dc", radiusSquaredB: float) -> bool:
        """
        Test whether the one sphere with center `centerA` and square radius `radiusSquaredA` intersects the other
        sphere with center `centerB` and square radius `radiusSquaredB`.
        
        Reference: <a href="http://gamedev.stackexchange.com/questions/75756/sphere-sphere-intersection-and-circle-sphere-intersection">http://gamedev.stackexchange.com</a>

        Arguments
        - centerA: the first sphere's center
        - radiusSquaredA: the square of the first sphere's radius
        - centerB: the second sphere's center
        - radiusSquaredB: the square of the second sphere's radius

        Returns
        - `True` iff both spheres intersect; `False` otherwise
        """
        ...


    @staticmethod
    def distancePointPlane(pointX: float, pointY: float, pointZ: float, a: float, b: float, c: float, d: float) -> float:
        """
        Determine the signed distance of the given point `(pointX, pointY, pointZ)` to the plane specified via its general plane equation
        *a*x + b*y + c*z + d = 0*.

        Arguments
        - pointX: the x coordinate of the point
        - pointY: the y coordinate of the point
        - pointZ: the z coordinate of the point
        - a: the x factor in the plane equation
        - b: the y factor in the plane equation
        - c: the z factor in the plane equation
        - d: the constant in the plane equation

        Returns
        - the distance between the point and the plane
        """
        ...


    @staticmethod
    def distancePointPlane(pointX: float, pointY: float, pointZ: float, v0X: float, v0Y: float, v0Z: float, v1X: float, v1Y: float, v1Z: float, v2X: float, v2Y: float, v2Z: float) -> float:
        """
        Determine the signed distance of the given point `(pointX, pointY, pointZ)` to the plane of the triangle specified by its three points
        `(v0X, v0Y, v0Z)`, `(v1X, v1Y, v1Z)` and `(v2X, v2Y, v2Z)`.
        
        If the point lies on the front-facing side of the triangle's plane, that is, if the triangle has counter-clockwise winding order
        as seen from the point, then this method returns a positive number.

        Arguments
        - pointX: the x coordinate of the point
        - pointY: the y coordinate of the point
        - pointZ: the z coordinate of the point
        - v0X: the x coordinate of the first vertex of the triangle
        - v0Y: the y coordinate of the first vertex of the triangle
        - v0Z: the z coordinate of the first vertex of the triangle
        - v1X: the x coordinate of the second vertex of the triangle
        - v1Y: the y coordinate of the second vertex of the triangle
        - v1Z: the z coordinate of the second vertex of the triangle
        - v2X: the x coordinate of the third vertex of the triangle
        - v2Y: the y coordinate of the third vertex of the triangle
        - v2Z: the z coordinate of the third vertex of the triangle

        Returns
        - the signed distance between the point and the plane of the triangle
        """
        ...


    @staticmethod
    def intersectRayPlane(originX: float, originY: float, originZ: float, dirX: float, dirY: float, dirZ: float, pointX: float, pointY: float, pointZ: float, normalX: float, normalY: float, normalZ: float, epsilon: float) -> float:
        """
        Test whether the ray with given origin `(originX, originY, originZ)` and direction `(dirX, dirY, dirZ)` intersects the plane
        containing the given point `(pointX, pointY, pointZ)` and having the normal `(normalX, normalY, normalZ)`, and return the
        value of the parameter *t* in the ray equation *p(t) = origin + t * dir* of the intersection point.
        
        This method returns `-1.0` if the ray does not intersect the plane, because it is either parallel to the plane or its direction points
        away from the plane or the ray's origin is on the *negative* side of the plane (i.e. the plane's normal points away from the ray's origin).
        
        Reference: <a href="https://www.siggraph.org/education/materials/HyperGraph/raytrace/rayplane_intersection.htm">https://www.siggraph.org/</a>

        Arguments
        - originX: the x coordinate of the ray's origin
        - originY: the y coordinate of the ray's origin
        - originZ: the z coordinate of the ray's origin
        - dirX: the x coordinate of the ray's direction
        - dirY: the y coordinate of the ray's direction
        - dirZ: the z coordinate of the ray's direction
        - pointX: the x coordinate of a point on the plane
        - pointY: the y coordinate of a point on the plane
        - pointZ: the z coordinate of a point on the plane
        - normalX: the x coordinate of the plane's normal
        - normalY: the y coordinate of the plane's normal
        - normalZ: the z coordinate of the plane's normal
        - epsilon: some small epsilon for when the ray is parallel to the plane

        Returns
        - the value of the parameter *t* in the ray equation *p(t) = origin + t * dir* of the intersection point, if the ray
                intersects the plane; `-1.0` otherwise
        """
        ...


    @staticmethod
    def intersectRayPlane(origin: "Vector3dc", dir: "Vector3dc", point: "Vector3dc", normal: "Vector3dc", epsilon: float) -> float:
        """
        Test whether the ray with given `origin` and direction `dir` intersects the plane
        containing the given `point` and having the given `normal`, and return the
        value of the parameter *t* in the ray equation *p(t) = origin + t * dir* of the intersection point.
        
        This method returns `-1.0` if the ray does not intersect the plane, because it is either parallel to the plane or its direction points
        away from the plane or the ray's origin is on the *negative* side of the plane (i.e. the plane's normal points away from the ray's origin).
        
        Reference: <a href="https://www.siggraph.org/education/materials/HyperGraph/raytrace/rayplane_intersection.htm">https://www.siggraph.org/</a>

        Arguments
        - origin: the ray's origin
        - dir: the ray's direction
        - point: a point on the plane
        - normal: the plane's normal
        - epsilon: some small epsilon for when the ray is parallel to the plane

        Returns
        - the value of the parameter *t* in the ray equation *p(t) = origin + t * dir* of the intersection point, if the ray
                intersects the plane; `-1.0` otherwise
        """
        ...


    @staticmethod
    def intersectRayPlane(originX: float, originY: float, originZ: float, dirX: float, dirY: float, dirZ: float, a: float, b: float, c: float, d: float, epsilon: float) -> float:
        """
        Test whether the ray with given origin `(originX, originY, originZ)` and direction `(dirX, dirY, dirZ)` intersects the plane
        given as the general plane equation *a*x + b*y + c*z + d = 0*, and return the
        value of the parameter *t* in the ray equation *p(t) = origin + t * dir* of the intersection point.
        
        This method returns `-1.0` if the ray does not intersect the plane, because it is either parallel to the plane or its direction points
        away from the plane or the ray's origin is on the *negative* side of the plane (i.e. the plane's normal points away from the ray's origin).
        
        Reference: <a href="https://www.siggraph.org/education/materials/HyperGraph/raytrace/rayplane_intersection.htm">https://www.siggraph.org/</a>

        Arguments
        - originX: the x coordinate of the ray's origin
        - originY: the y coordinate of the ray's origin
        - originZ: the z coordinate of the ray's origin
        - dirX: the x coordinate of the ray's direction
        - dirY: the y coordinate of the ray's direction
        - dirZ: the z coordinate of the ray's direction
        - a: the x factor in the plane equation
        - b: the y factor in the plane equation
        - c: the z factor in the plane equation
        - d: the constant in the plane equation
        - epsilon: some small epsilon for when the ray is parallel to the plane

        Returns
        - the value of the parameter *t* in the ray equation *p(t) = origin + t * dir* of the intersection point, if the ray
                intersects the plane; `-1.0` otherwise
        """
        ...


    @staticmethod
    def testAabSphere(minX: float, minY: float, minZ: float, maxX: float, maxY: float, maxZ: float, centerX: float, centerY: float, centerZ: float, radiusSquared: float) -> bool:
        """
        Test whether the axis-aligned box with minimum corner `(minX, minY, minZ)` and maximum corner `(maxX, maxY, maxZ)`
        intersects the sphere with the given center `(centerX, centerY, centerZ)` and square radius `radiusSquared`.
        
        Reference: <a href="http://stackoverflow.com/questions/4578967/cube-sphere-intersection-test#answer-4579069">http://stackoverflow.com</a>

        Arguments
        - minX: the x coordinate of the minimum corner of the axis-aligned box
        - minY: the y coordinate of the minimum corner of the axis-aligned box
        - minZ: the z coordinate of the minimum corner of the axis-aligned box
        - maxX: the x coordinate of the maximum corner of the axis-aligned box
        - maxY: the y coordinate of the maximum corner of the axis-aligned box
        - maxZ: the z coordinate of the maximum corner of the axis-aligned box
        - centerX: the x coordinate of the sphere's center
        - centerY: the y coordinate of the sphere's center
        - centerZ: the z coordinate of the sphere's center
        - radiusSquared: the square of the sphere's radius

        Returns
        - `True` iff the axis-aligned box intersects the sphere; `False` otherwise
        """
        ...


    @staticmethod
    def testAabSphere(min: "Vector3dc", max: "Vector3dc", center: "Vector3dc", radiusSquared: float) -> bool:
        """
        Test whether the axis-aligned box with minimum corner `min` and maximum corner `max`
        intersects the sphere with the given `center` and square radius `radiusSquared`.
        
        Reference: <a href="http://stackoverflow.com/questions/4578967/cube-sphere-intersection-test#answer-4579069">http://stackoverflow.com</a>

        Arguments
        - min: the minimum corner of the axis-aligned box
        - max: the maximum corner of the axis-aligned box
        - center: the sphere's center
        - radiusSquared: the squared of the sphere's radius

        Returns
        - `True` iff the axis-aligned box intersects the sphere; `False` otherwise
        """
        ...


    @staticmethod
    def findClosestPointOnPlane(aX: float, aY: float, aZ: float, nX: float, nY: float, nZ: float, pX: float, pY: float, pZ: float, result: "Vector3d") -> "Vector3d":
        """
        Find the point on the given plane which is closest to the specified point `(pX, pY, pZ)` and store the result in `result`.

        Arguments
        - aX: the x coordinate of one point on the plane
        - aY: the y coordinate of one point on the plane
        - aZ: the z coordinate of one point on the plane
        - nX: the x coordinate of the unit normal of the plane
        - nY: the y coordinate of the unit normal of the plane
        - nZ: the z coordinate of the unit normal of the plane
        - pX: the x coordinate of the point
        - pY: the y coordinate of the point
        - pZ: the z coordinate of the point
        - result: will hold the result

        Returns
        - result
        """
        ...


    @staticmethod
    def findClosestPointOnLineSegment(aX: float, aY: float, aZ: float, bX: float, bY: float, bZ: float, pX: float, pY: float, pZ: float, result: "Vector3d") -> "Vector3d":
        """
        Find the point on the given line segment which is closest to the specified point `(pX, pY, pZ)`, and store the result in `result`.

        Arguments
        - aX: the x coordinate of the first end point of the line segment
        - aY: the y coordinate of the first end point of the line segment
        - aZ: the z coordinate of the first end point of the line segment
        - bX: the x coordinate of the second end point of the line segment
        - bY: the y coordinate of the second end point of the line segment
        - bZ: the z coordinate of the second end point of the line segment
        - pX: the x coordinate of the point
        - pY: the y coordinate of the point
        - pZ: the z coordinate of the point
        - result: will hold the result

        Returns
        - result
        """
        ...


    @staticmethod
    def findClosestPointsLineSegments(a0X: float, a0Y: float, a0Z: float, a1X: float, a1Y: float, a1Z: float, b0X: float, b0Y: float, b0Z: float, b1X: float, b1Y: float, b1Z: float, resultA: "Vector3d", resultB: "Vector3d") -> float:
        """
        Find the closest points on the two line segments, store the point on the first line segment in `resultA` and 
        the point on the second line segment in `resultB`, and return the square distance between both points.
        
        Reference: Book "Real-Time Collision Detection" chapter 5.1.9 "Closest Points of Two Line Segments"

        Arguments
        - a0X: the x coordinate of the first line segment's first end point
        - a0Y: the y coordinate of the first line segment's first end point
        - a0Z: the z coordinate of the first line segment's first end point
        - a1X: the x coordinate of the first line segment's second end point
        - a1Y: the y coordinate of the first line segment's second end point
        - a1Z: the z coordinate of the first line segment's second end point
        - b0X: the x coordinate of the second line segment's first end point
        - b0Y: the y coordinate of the second line segment's first end point
        - b0Z: the z coordinate of the second line segment's first end point
        - b1X: the x coordinate of the second line segment's second end point
        - b1Y: the y coordinate of the second line segment's second end point
        - b1Z: the z coordinate of the second line segment's second end point
        - resultA: will hold the point on the first line segment
        - resultB: will hold the point on the second line segment

        Returns
        - the square distance between the two closest points
        """
        ...


    @staticmethod
    def findClosestPointsLineSegmentTriangle(aX: float, aY: float, aZ: float, bX: float, bY: float, bZ: float, v0X: float, v0Y: float, v0Z: float, v1X: float, v1Y: float, v1Z: float, v2X: float, v2Y: float, v2Z: float, lineSegmentResult: "Vector3d", triangleResult: "Vector3d") -> float:
        """
        Find the closest points on a line segment and a triangle.
        
        Reference: Book "Real-Time Collision Detection" chapter 5.1.10 "Closest Points of a Line Segment and a Triangle"

        Arguments
        - aX: the x coordinate of the line segment's first end point
        - aY: the y coordinate of the line segment's first end point
        - aZ: the z coordinate of the line segment's first end point
        - bX: the x coordinate of the line segment's second end point
        - bY: the y coordinate of the line segment's second end point
        - bZ: the z coordinate of the line segment's second end point
        - v0X: the x coordinate of the triangle's first vertex
        - v0Y: the y coordinate of the triangle's first vertex
        - v0Z: the z coordinate of the triangle's first vertex
        - v1X: the x coordinate of the triangle's second vertex
        - v1Y: the y coordinate of the triangle's second vertex
        - v1Z: the z coordinate of the triangle's second vertex
        - v2X: the x coordinate of the triangle's third vertex
        - v2Y: the y coordinate of the triangle's third vertex
        - v2Z: the z coordinate of the triangle's third vertex
        - lineSegmentResult: will hold the closest point on the line segment
        - triangleResult: will hold the closest point on the triangle

        Returns
        - the square distance of the closest points
        """
        ...


    @staticmethod
    def findClosestPointOnTriangle(v0X: float, v0Y: float, v0Z: float, v1X: float, v1Y: float, v1Z: float, v2X: float, v2Y: float, v2Z: float, pX: float, pY: float, pZ: float, result: "Vector3d") -> int:
        """
        Determine the closest point on the triangle with the given vertices `(v0X, v0Y, v0Z)`, `(v1X, v1Y, v1Z)`, `(v2X, v2Y, v2Z)`
        between that triangle and the given point `(pX, pY, pZ)` and store that point into the given `result`.
        
        Additionally, this method returns whether the closest point is a vertex (.POINT_ON_TRIANGLE_VERTEX_0, .POINT_ON_TRIANGLE_VERTEX_1, .POINT_ON_TRIANGLE_VERTEX_2)
        of the triangle, lies on an edge (.POINT_ON_TRIANGLE_EDGE_01, .POINT_ON_TRIANGLE_EDGE_12, .POINT_ON_TRIANGLE_EDGE_20)
        or on the .POINT_ON_TRIANGLE_FACE face of the triangle.
        
        Reference: Book "Real-Time Collision Detection" chapter 5.1.5 "Closest Point on Triangle to Point"

        Arguments
        - v0X: the x coordinate of the first vertex of the triangle
        - v0Y: the y coordinate of the first vertex of the triangle
        - v0Z: the z coordinate of the first vertex of the triangle
        - v1X: the x coordinate of the second vertex of the triangle
        - v1Y: the y coordinate of the second vertex of the triangle
        - v1Z: the z coordinate of the second vertex of the triangle
        - v2X: the x coordinate of the third vertex of the triangle
        - v2Y: the y coordinate of the third vertex of the triangle
        - v2Z: the z coordinate of the third vertex of the triangle
        - pX: the x coordinate of the point
        - pY: the y coordinate of the point
        - pZ: the y coordinate of the point
        - result: will hold the closest point

        Returns
        - one of .POINT_ON_TRIANGLE_VERTEX_0, .POINT_ON_TRIANGLE_VERTEX_1, .POINT_ON_TRIANGLE_VERTEX_2,
                       .POINT_ON_TRIANGLE_EDGE_01, .POINT_ON_TRIANGLE_EDGE_12, .POINT_ON_TRIANGLE_EDGE_20 or
                       .POINT_ON_TRIANGLE_FACE
        """
        ...


    @staticmethod
    def findClosestPointOnTriangle(v0: "Vector3dc", v1: "Vector3dc", v2: "Vector3dc", p: "Vector3dc", result: "Vector3d") -> int:
        """
        Determine the closest point on the triangle with the vertices `v0`, `v1`, `v2`
        between that triangle and the given point `p` and store that point into the given `result`.
        
        Additionally, this method returns whether the closest point is a vertex (.POINT_ON_TRIANGLE_VERTEX_0, .POINT_ON_TRIANGLE_VERTEX_1, .POINT_ON_TRIANGLE_VERTEX_2)
        of the triangle, lies on an edge (.POINT_ON_TRIANGLE_EDGE_01, .POINT_ON_TRIANGLE_EDGE_12, .POINT_ON_TRIANGLE_EDGE_20)
        or on the .POINT_ON_TRIANGLE_FACE face of the triangle.
        
        Reference: Book "Real-Time Collision Detection" chapter 5.1.5 "Closest Point on Triangle to Point"

        Arguments
        - v0: the first vertex of the triangle
        - v1: the second vertex of the triangle
        - v2: the third vertex of the triangle
        - p: the point
        - result: will hold the closest point

        Returns
        - one of .POINT_ON_TRIANGLE_VERTEX_0, .POINT_ON_TRIANGLE_VERTEX_1, .POINT_ON_TRIANGLE_VERTEX_2,
                       .POINT_ON_TRIANGLE_EDGE_01, .POINT_ON_TRIANGLE_EDGE_12, .POINT_ON_TRIANGLE_EDGE_20 or
                       .POINT_ON_TRIANGLE_FACE
        """
        ...


    @staticmethod
    def findClosestPointOnRectangle(aX: float, aY: float, aZ: float, bX: float, bY: float, bZ: float, cX: float, cY: float, cZ: float, pX: float, pY: float, pZ: float, res: "Vector3d") -> "Vector3d":
        """
        Find the point on a given rectangle, specified via three of its corners, which is closest to the specified point
        `(pX, pY, pZ)` and store the result into `res`.
        
        Reference: Book "Real-Time Collision Detection" chapter 5.1.4.2 "Closest Point on 3D Rectangle to Point"

        Arguments
        - aX: the x coordinate of the first corner point of the rectangle
        - aY: the y coordinate of the first corner point of the rectangle
        - aZ: the z coordinate of the first corner point of the rectangle
        - bX: the x coordinate of the second corner point of the rectangle
        - bY: the y coordinate of the second corner point of the rectangle
        - bZ: the z coordinate of the second corner point of the rectangle
        - cX: the x coordinate of the third corner point of the rectangle
        - cY: the y coordinate of the third corner point of the rectangle
        - cZ: the z coordinate of the third corner point of the rectangle
        - pX: the x coordinate of the point
        - pY: the y coordinate of the point
        - pZ: the z coordinate of the point
        - res: will hold the result

        Returns
        - res
        """
        ...


    @staticmethod
    def intersectSweptSphereTriangle(centerX: float, centerY: float, centerZ: float, radius: float, velX: float, velY: float, velZ: float, v0X: float, v0Y: float, v0Z: float, v1X: float, v1Y: float, v1Z: float, v2X: float, v2Y: float, v2Z: float, epsilon: float, maxT: float, pointAndTime: "Vector4d") -> int:
        """
        Determine the point of intersection between a sphere with the given center `(centerX, centerY, centerZ)` and `radius` moving
        with the given velocity `(velX, velY, velZ)` and the triangle specified via its three vertices `(v0X, v0Y, v0Z)`, `(v1X, v1Y, v1Z)`, `(v2X, v2Y, v2Z)`.
        
        The vertices of the triangle must be specified in counter-clockwise winding order.
        
        An intersection is only considered if the time of intersection is smaller than the given `maxT` value.
        
        Reference: <a href="http://www.peroxide.dk/papers/collision/collision.pdf">Improved Collision detection and Response</a>

        Arguments
        - centerX: the x coordinate of the sphere's center
        - centerY: the y coordinate of the sphere's center
        - centerZ: the z coordinate of the sphere's center
        - radius: the radius of the sphere
        - velX: the x component of the velocity of the sphere
        - velY: the y component of the velocity of the sphere
        - velZ: the z component of the velocity of the sphere
        - v0X: the x coordinate of the first triangle vertex
        - v0Y: the y coordinate of the first triangle vertex
        - v0Z: the z coordinate of the first triangle vertex
        - v1X: the x coordinate of the second triangle vertex
        - v1Y: the y coordinate of the second triangle vertex
        - v1Z: the z coordinate of the second triangle vertex
        - v2X: the x coordinate of the third triangle vertex
        - v2Y: the y coordinate of the third triangle vertex
        - v2Z: the z coordinate of the third triangle vertex
        - epsilon: a small epsilon when testing spheres that move almost parallel to the triangle
        - maxT: the maximum intersection time
        - pointAndTime: iff the moving sphere and the triangle intersect, this will hold the point of intersection in the `(x, y, z)` components
                     and the time of intersection in the `w` component

        Returns
        - .POINT_ON_TRIANGLE_FACE if the intersection point lies on the triangle's face,
                or .POINT_ON_TRIANGLE_VERTEX_0, .POINT_ON_TRIANGLE_VERTEX_1 or .POINT_ON_TRIANGLE_VERTEX_2 if the intersection point is a vertex,
                or .POINT_ON_TRIANGLE_EDGE_01, .POINT_ON_TRIANGLE_EDGE_12 or .POINT_ON_TRIANGLE_EDGE_20 if the intersection point lies on an edge;
                or `0` if no intersection
        """
        ...


    @staticmethod
    def testPointInTriangle(pX: float, pY: float, pZ: float, v0X: float, v0Y: float, v0Z: float, v1X: float, v1Y: float, v1Z: float, v2X: float, v2Y: float, v2Z: float) -> bool:
        """
        Test whether the projection of the given point `(pX, pY, pZ)` lies inside of the triangle defined by the three vertices
        `(v0X, v0Y, v0Z)`, `(v1X, v1Y, v1Z)` and `(v2X, v2Y, v2Z)`.
        
        Reference: <a href="http://www.peroxide.dk/papers/collision/collision.pdf">Improved Collision detection and Response</a>

        Arguments
        - pX: the x coordinate of the point to test
        - pY: the y coordinate of the point to test
        - pZ: the z coordinate of the point to test
        - v0X: the x coordinate of the first vertex
        - v0Y: the y coordinate of the first vertex
        - v0Z: the z coordinate of the first vertex
        - v1X: the x coordinate of the second vertex
        - v1Y: the y coordinate of the second vertex
        - v1Z: the z coordinate of the second vertex
        - v2X: the x coordinate of the third vertex
        - v2Y: the y coordinate of the third vertex
        - v2Z: the z coordinate of the third vertex

        Returns
        - `True` if the projection of the given point lies inside of the given triangle; `False` otherwise
        """
        ...


    @staticmethod
    def intersectRaySphere(originX: float, originY: float, originZ: float, dirX: float, dirY: float, dirZ: float, centerX: float, centerY: float, centerZ: float, radiusSquared: float, result: "Vector2d") -> bool:
        """
        Test whether the given ray with the origin `(originX, originY, originZ)` and normalized direction `(dirX, dirY, dirZ)`
        intersects the given sphere with center `(centerX, centerY, centerZ)` and square radius `radiusSquared`,
        and store the values of the parameter *t* in the ray equation *p(t) = origin + t * dir* for both points (near
        and far) of intersections into the given `result` vector.
        
        This method returns `True` for a ray whose origin lies inside the sphere.
        
        Reference: <a href="http://www.scratchapixel.com/lessons/3d-basic-rendering/minimal-ray-tracer-rendering-simple-shapes/ray-sphere-intersection">http://www.scratchapixel.com/</a>

        Arguments
        - originX: the x coordinate of the ray's origin
        - originY: the y coordinate of the ray's origin
        - originZ: the z coordinate of the ray's origin
        - dirX: the x coordinate of the ray's normalized direction
        - dirY: the y coordinate of the ray's normalized direction
        - dirZ: the z coordinate of the ray's normalized direction
        - centerX: the x coordinate of the sphere's center
        - centerY: the y coordinate of the sphere's center
        - centerZ: the z coordinate of the sphere's center
        - radiusSquared: the sphere radius squared
        - result: a vector that will contain the values of the parameter *t* in the ray equation
                     *p(t) = origin + t * dir* for both points (near, far) of intersections with the sphere

        Returns
        - `True` if the ray intersects the sphere; `False` otherwise
        """
        ...


    @staticmethod
    def intersectRaySphere(origin: "Vector3dc", dir: "Vector3dc", center: "Vector3dc", radiusSquared: float, result: "Vector2d") -> bool:
        """
        Test whether the ray with the given `origin` and normalized direction `dir`
        intersects the sphere with the given `center` and square radius `radiusSquared`,
        and store the values of the parameter *t* in the ray equation *p(t) = origin + t * dir* for both points (near
        and far) of intersections into the given `result` vector.
        
        This method returns `True` for a ray whose origin lies inside the sphere.
        
        Reference: <a href="http://www.scratchapixel.com/lessons/3d-basic-rendering/minimal-ray-tracer-rendering-simple-shapes/ray-sphere-intersection">http://www.scratchapixel.com/</a>

        Arguments
        - origin: the ray's origin
        - dir: the ray's normalized direction
        - center: the sphere's center
        - radiusSquared: the sphere radius squared
        - result: a vector that will contain the values of the parameter *t* in the ray equation
                     *p(t) = origin + t * dir* for both points (near, far) of intersections with the sphere

        Returns
        - `True` if the ray intersects the sphere; `False` otherwise
        """
        ...


    @staticmethod
    def testRaySphere(originX: float, originY: float, originZ: float, dirX: float, dirY: float, dirZ: float, centerX: float, centerY: float, centerZ: float, radiusSquared: float) -> bool:
        """
        Test whether the given ray with the origin `(originX, originY, originZ)` and normalized direction `(dirX, dirY, dirZ)`
        intersects the given sphere with center `(centerX, centerY, centerZ)` and square radius `radiusSquared`.
        
        This method returns `True` for a ray whose origin lies inside the sphere.
        
        Reference: <a href="http://www.scratchapixel.com/lessons/3d-basic-rendering/minimal-ray-tracer-rendering-simple-shapes/ray-sphere-intersection">http://www.scratchapixel.com/</a>

        Arguments
        - originX: the x coordinate of the ray's origin
        - originY: the y coordinate of the ray's origin
        - originZ: the z coordinate of the ray's origin
        - dirX: the x coordinate of the ray's normalized direction
        - dirY: the y coordinate of the ray's normalized direction
        - dirZ: the z coordinate of the ray's normalized direction
        - centerX: the x coordinate of the sphere's center
        - centerY: the y coordinate of the sphere's center
        - centerZ: the z coordinate of the sphere's center
        - radiusSquared: the sphere radius squared

        Returns
        - `True` if the ray intersects the sphere; `False` otherwise
        """
        ...


    @staticmethod
    def testRaySphere(origin: "Vector3dc", dir: "Vector3dc", center: "Vector3dc", radiusSquared: float) -> bool:
        """
        Test whether the ray with the given `origin` and normalized direction `dir`
        intersects the sphere with the given `center` and square radius.
        
        This method returns `True` for a ray whose origin lies inside the sphere.
        
        Reference: <a href="http://www.scratchapixel.com/lessons/3d-basic-rendering/minimal-ray-tracer-rendering-simple-shapes/ray-sphere-intersection">http://www.scratchapixel.com/</a>

        Arguments
        - origin: the ray's origin
        - dir: the ray's normalized direction
        - center: the sphere's center
        - radiusSquared: the sphere radius squared

        Returns
        - `True` if the ray intersects the sphere; `False` otherwise
        """
        ...


    @staticmethod
    def testLineSegmentSphere(p0X: float, p0Y: float, p0Z: float, p1X: float, p1Y: float, p1Z: float, centerX: float, centerY: float, centerZ: float, radiusSquared: float) -> bool:
        """
        Test whether the line segment with the end points `(p0X, p0Y, p0Z)` and `(p1X, p1Y, p1Z)`
        intersects the given sphere with center `(centerX, centerY, centerZ)` and square radius `radiusSquared`.
        
        Reference: <a href="http://paulbourke.net/geometry/circlesphere/index.html#linesphere">http://paulbourke.net/</a>

        Arguments
        - p0X: the x coordinate of the line segment's first end point
        - p0Y: the y coordinate of the line segment's first end point
        - p0Z: the z coordinate of the line segment's first end point
        - p1X: the x coordinate of the line segment's second end point
        - p1Y: the y coordinate of the line segment's second end point
        - p1Z: the z coordinate of the line segment's second end point
        - centerX: the x coordinate of the sphere's center
        - centerY: the y coordinate of the sphere's center
        - centerZ: the z coordinate of the sphere's center
        - radiusSquared: the sphere radius squared

        Returns
        - `True` if the line segment intersects the sphere; `False` otherwise
        """
        ...


    @staticmethod
    def testLineSegmentSphere(p0: "Vector3dc", p1: "Vector3dc", center: "Vector3dc", radiusSquared: float) -> bool:
        """
        Test whether the line segment with the end points `p0` and `p1`
        intersects the given sphere with center `center` and square radius `radiusSquared`.
        
        Reference: <a href="http://paulbourke.net/geometry/circlesphere/index.html#linesphere">http://paulbourke.net/</a>

        Arguments
        - p0: the line segment's first end point
        - p1: the line segment's second end point
        - center: the sphere's center
        - radiusSquared: the sphere radius squared

        Returns
        - `True` if the line segment intersects the sphere; `False` otherwise
        """
        ...


    @staticmethod
    def intersectRayAab(originX: float, originY: float, originZ: float, dirX: float, dirY: float, dirZ: float, minX: float, minY: float, minZ: float, maxX: float, maxY: float, maxZ: float, result: "Vector2d") -> bool:
        """
        Test whether the given ray with the origin `(originX, originY, originZ)` and direction `(dirX, dirY, dirZ)`
        intersects the axis-aligned box given as its minimum corner `(minX, minY, minZ)` and maximum corner `(maxX, maxY, maxZ)`,
        and return the values of the parameter *t* in the ray equation *p(t) = origin + t * dir* of the near and far point of intersection.
        
        This method returns `True` for a ray whose origin lies inside the axis-aligned box.
        
        If many boxes need to be tested against the same ray, then the RayAabIntersection class is likely more efficient.
        
        Reference: <a href="https://dl.acm.org/citation.cfm?id=1198748">An Efficient and Robust Ray–Box Intersection</a>

        Arguments
        - originX: the x coordinate of the ray's origin
        - originY: the y coordinate of the ray's origin
        - originZ: the z coordinate of the ray's origin
        - dirX: the x coordinate of the ray's direction
        - dirY: the y coordinate of the ray's direction
        - dirZ: the z coordinate of the ray's direction
        - minX: the x coordinate of the minimum corner of the axis-aligned box
        - minY: the y coordinate of the minimum corner of the axis-aligned box
        - minZ: the z coordinate of the minimum corner of the axis-aligned box
        - maxX: the x coordinate of the maximum corner of the axis-aligned box
        - maxY: the y coordinate of the maximum corner of the axis-aligned box
        - maxZ: the y coordinate of the maximum corner of the axis-aligned box
        - result: a vector which will hold the resulting values of the parameter
                     *t* in the ray equation *p(t) = origin + t * dir* of the near and far point of intersection
                     iff the ray intersects the axis-aligned box

        Returns
        - `True` if the given ray intersects the axis-aligned box; `False` otherwise

        See
        - RayAabIntersection
        """
        ...


    @staticmethod
    def intersectRayAab(origin: "Vector3dc", dir: "Vector3dc", min: "Vector3dc", max: "Vector3dc", result: "Vector2d") -> bool:
        """
        Test whether the ray with the given `origin` and direction `dir`
        intersects the axis-aligned box specified as its minimum corner `min` and maximum corner `max`,
        and return the values of the parameter *t* in the ray equation *p(t) = origin + t * dir* of the near and far point of intersection..
        
        This method returns `True` for a ray whose origin lies inside the axis-aligned box.
        
        If many boxes need to be tested against the same ray, then the RayAabIntersection class is likely more efficient.
        
        Reference: <a href="https://dl.acm.org/citation.cfm?id=1198748">An Efficient and Robust Ray–Box Intersection</a>

        Arguments
        - origin: the ray's origin
        - dir: the ray's direction
        - min: the minimum corner of the axis-aligned box
        - max: the maximum corner of the axis-aligned box
        - result: a vector which will hold the resulting values of the parameter
                     *t* in the ray equation *p(t) = origin + t * dir* of the near and far point of intersection
                     iff the ray intersects the axis-aligned box

        Returns
        - `True` if the given ray intersects the axis-aligned box; `False` otherwise

        See
        - RayAabIntersection
        """
        ...


    @staticmethod
    def intersectLineSegmentAab(p0X: float, p0Y: float, p0Z: float, p1X: float, p1Y: float, p1Z: float, minX: float, minY: float, minZ: float, maxX: float, maxY: float, maxZ: float, result: "Vector2d") -> int:
        """
        Determine whether the undirected line segment with the end points `(p0X, p0Y, p0Z)` and `(p1X, p1Y, p1Z)`
        intersects the axis-aligned box given as its minimum corner `(minX, minY, minZ)` and maximum corner `(maxX, maxY, maxZ)`,
        and return the values of the parameter *t* in the ray equation *p(t) = origin + p0 * (p1 - p0)* of the near and far point of intersection.
        
        This method returns `True` for a line segment whose either end point lies inside the axis-aligned box.
        
        Reference: <a href="https://dl.acm.org/citation.cfm?id=1198748">An Efficient and Robust Ray–Box Intersection</a>

        Arguments
        - p0X: the x coordinate of the line segment's first end point
        - p0Y: the y coordinate of the line segment's first end point
        - p0Z: the z coordinate of the line segment's first end point
        - p1X: the x coordinate of the line segment's second end point
        - p1Y: the y coordinate of the line segment's second end point
        - p1Z: the z coordinate of the line segment's second end point
        - minX: the x coordinate of one corner of the axis-aligned box
        - minY: the y coordinate of one corner of the axis-aligned box
        - minZ: the z coordinate of one corner of the axis-aligned box
        - maxX: the x coordinate of the opposite corner of the axis-aligned box
        - maxY: the y coordinate of the opposite corner of the axis-aligned box
        - maxZ: the y coordinate of the opposite corner of the axis-aligned box
        - result: a vector which will hold the resulting values of the parameter
                     *t* in the ray equation *p(t) = p0 + t * (p1 - p0)* of the near and far point of intersection
                     iff the line segment intersects the axis-aligned box

        Returns
        - .INSIDE if the line segment lies completely inside of the axis-aligned box; or
                .OUTSIDE if the line segment lies completely outside of the axis-aligned box; or
                .ONE_INTERSECTION if one of the end points of the line segment lies inside of the axis-aligned box; or
                .TWO_INTERSECTION if the line segment intersects two sides of the axis-aligned box
                or lies on an edge or a side of the box

        See
        - .intersectLineSegmentAab(Vector3dc, Vector3dc, Vector3dc, Vector3dc, Vector2d)
        """
        ...


    @staticmethod
    def intersectLineSegmentAab(p0: "Vector3dc", p1: "Vector3dc", min: "Vector3dc", max: "Vector3dc", result: "Vector2d") -> int:
        """
        Determine whether the undirected line segment with the end points `p0` and `p1`
        intersects the axis-aligned box given as its minimum corner `min` and maximum corner `max`,
        and return the values of the parameter *t* in the ray equation *p(t) = origin + p0 * (p1 - p0)* of the near and far point of intersection.
        
        This method returns `True` for a line segment whose either end point lies inside the axis-aligned box.
        
        Reference: <a href="https://dl.acm.org/citation.cfm?id=1198748">An Efficient and Robust Ray–Box Intersection</a>

        Arguments
        - p0: the line segment's first end point
        - p1: the line segment's second end point
        - min: the minimum corner of the axis-aligned box
        - max: the maximum corner of the axis-aligned box
        - result: a vector which will hold the resulting values of the parameter
                     *t* in the ray equation *p(t) = p0 + t * (p1 - p0)* of the near and far point of intersection
                     iff the line segment intersects the axis-aligned box

        Returns
        - .INSIDE if the line segment lies completely inside of the axis-aligned box; or
                .OUTSIDE if the line segment lies completely outside of the axis-aligned box; or
                .ONE_INTERSECTION if one of the end points of the line segment lies inside of the axis-aligned box; or
                .TWO_INTERSECTION if the line segment intersects two sides of the axis-aligned box
                or lies on an edge or a side of the box

        See
        - .intersectLineSegmentAab(Vector3dc, Vector3dc, Vector3dc, Vector3dc, Vector2d)
        """
        ...


    @staticmethod
    def testRayAab(originX: float, originY: float, originZ: float, dirX: float, dirY: float, dirZ: float, minX: float, minY: float, minZ: float, maxX: float, maxY: float, maxZ: float) -> bool:
        """
        Test whether the given ray with the origin `(originX, originY, originZ)` and direction `(dirX, dirY, dirZ)`
        intersects the axis-aligned box given as its minimum corner `(minX, minY, minZ)` and maximum corner `(maxX, maxY, maxZ)`.
        
        This method returns `True` for a ray whose origin lies inside the axis-aligned box.
        
        If many boxes need to be tested against the same ray, then the RayAabIntersection class is likely more efficient.
        
        Reference: <a href="https://dl.acm.org/citation.cfm?id=1198748">An Efficient and Robust Ray–Box Intersection</a>

        Arguments
        - originX: the x coordinate of the ray's origin
        - originY: the y coordinate of the ray's origin
        - originZ: the z coordinate of the ray's origin
        - dirX: the x coordinate of the ray's direction
        - dirY: the y coordinate of the ray's direction
        - dirZ: the z coordinate of the ray's direction
        - minX: the x coordinate of the minimum corner of the axis-aligned box
        - minY: the y coordinate of the minimum corner of the axis-aligned box
        - minZ: the z coordinate of the minimum corner of the axis-aligned box
        - maxX: the x coordinate of the maximum corner of the axis-aligned box
        - maxY: the y coordinate of the maximum corner of the axis-aligned box
        - maxZ: the y coordinate of the maximum corner of the axis-aligned box

        Returns
        - `True` if the given ray intersects the axis-aligned box; `False` otherwise

        See
        - RayAabIntersection
        """
        ...


    @staticmethod
    def testRayAab(origin: "Vector3dc", dir: "Vector3dc", min: "Vector3dc", max: "Vector3dc") -> bool:
        """
        Test whether the ray with the given `origin` and direction `dir`
        intersects the axis-aligned box specified as its minimum corner `min` and maximum corner `max`.
        
        This method returns `True` for a ray whose origin lies inside the axis-aligned box.
        
        If many boxes need to be tested against the same ray, then the RayAabIntersection class is likely more efficient.
        
        Reference: <a href="https://dl.acm.org/citation.cfm?id=1198748">An Efficient and Robust Ray–Box Intersection</a>

        Arguments
        - origin: the ray's origin
        - dir: the ray's direction
        - min: the minimum corner of the axis-aligned box
        - max: the maximum corner of the axis-aligned box

        Returns
        - `True` if the given ray intersects the axis-aligned box; `False` otherwise

        See
        - RayAabIntersection
        """
        ...


    @staticmethod
    def testRayTriangleFront(originX: float, originY: float, originZ: float, dirX: float, dirY: float, dirZ: float, v0X: float, v0Y: float, v0Z: float, v1X: float, v1Y: float, v1Z: float, v2X: float, v2Y: float, v2Z: float, epsilon: float) -> bool:
        """
        Test whether the given ray with the origin `(originX, originY, originZ)` and direction `(dirX, dirY, dirZ)`
        intersects the frontface of the triangle consisting of the three vertices `(v0X, v0Y, v0Z)`, `(v1X, v1Y, v1Z)` and `(v2X, v2Y, v2Z)`.
        
        This is an implementation of the <a href="http://www.graphics.cornell.edu/pubs/1997/MT97.pdf">
        Fast, Minimum Storage Ray/Triangle Intersection</a> method.
        
        This test implements backface culling, that is, it will return `False` when the triangle is in clockwise
        winding order assuming a *right-handed* coordinate system when seen along the ray's direction, even if the ray intersects the triangle.
        This is in compliance with how OpenGL handles backface culling with default frontface/backface settings.

        Arguments
        - originX: the x coordinate of the ray's origin
        - originY: the y coordinate of the ray's origin
        - originZ: the z coordinate of the ray's origin
        - dirX: the x coordinate of the ray's direction
        - dirY: the y coordinate of the ray's direction
        - dirZ: the z coordinate of the ray's direction
        - v0X: the x coordinate of the first vertex
        - v0Y: the y coordinate of the first vertex
        - v0Z: the z coordinate of the first vertex
        - v1X: the x coordinate of the second vertex
        - v1Y: the y coordinate of the second vertex
        - v1Z: the z coordinate of the second vertex
        - v2X: the x coordinate of the third vertex
        - v2Y: the y coordinate of the third vertex
        - v2Z: the z coordinate of the third vertex
        - epsilon: a small epsilon when testing rays that are almost parallel to the triangle

        Returns
        - `True` if the given ray intersects the frontface of the triangle; `False` otherwise

        See
        - .testRayTriangleFront(Vector3dc, Vector3dc, Vector3dc, Vector3dc, Vector3dc, double)
        """
        ...


    @staticmethod
    def testRayTriangleFront(origin: "Vector3dc", dir: "Vector3dc", v0: "Vector3dc", v1: "Vector3dc", v2: "Vector3dc", epsilon: float) -> bool:
        """
        Test whether the ray with the given `origin` and the given `dir` intersects the frontface of the triangle consisting of the three vertices
        `v0`, `v1` and `v2`.
        
        This is an implementation of the <a href="http://www.graphics.cornell.edu/pubs/1997/MT97.pdf">
        Fast, Minimum Storage Ray/Triangle Intersection</a> method.
        
        This test implements backface culling, that is, it will return `False` when the triangle is in clockwise
        winding order assuming a *right-handed* coordinate system when seen along the ray's direction, even if the ray intersects the triangle.
        This is in compliance with how OpenGL handles backface culling with default frontface/backface settings.

        Arguments
        - origin: the ray's origin
        - dir: the ray's direction
        - v0: the position of the first vertex
        - v1: the position of the second vertex
        - v2: the position of the third vertex
        - epsilon: a small epsilon when testing rays that are almost parallel to the triangle

        Returns
        - `True` if the given ray intersects the frontface of the triangle; `False` otherwise

        See
        - .testRayTriangleFront(double, double, double, double, double, double, double, double, double, double, double, double, double, double, double, double)
        """
        ...


    @staticmethod
    def testRayTriangle(originX: float, originY: float, originZ: float, dirX: float, dirY: float, dirZ: float, v0X: float, v0Y: float, v0Z: float, v1X: float, v1Y: float, v1Z: float, v2X: float, v2Y: float, v2Z: float, epsilon: float) -> bool:
        """
        Test whether the given ray with the origin `(originX, originY, originZ)` and direction `(dirX, dirY, dirZ)`
        intersects the triangle consisting of the three vertices `(v0X, v0Y, v0Z)`, `(v1X, v1Y, v1Z)` and `(v2X, v2Y, v2Z)`.
        
        This is an implementation of the <a href="http://www.graphics.cornell.edu/pubs/1997/MT97.pdf">
        Fast, Minimum Storage Ray/Triangle Intersection</a> method.
        
        This test does not take into account the winding order of the triangle, so a ray will intersect a front-facing triangle as well as a back-facing triangle.

        Arguments
        - originX: the x coordinate of the ray's origin
        - originY: the y coordinate of the ray's origin
        - originZ: the z coordinate of the ray's origin
        - dirX: the x coordinate of the ray's direction
        - dirY: the y coordinate of the ray's direction
        - dirZ: the z coordinate of the ray's direction
        - v0X: the x coordinate of the first vertex
        - v0Y: the y coordinate of the first vertex
        - v0Z: the z coordinate of the first vertex
        - v1X: the x coordinate of the second vertex
        - v1Y: the y coordinate of the second vertex
        - v1Z: the z coordinate of the second vertex
        - v2X: the x coordinate of the third vertex
        - v2Y: the y coordinate of the third vertex
        - v2Z: the z coordinate of the third vertex
        - epsilon: a small epsilon when testing rays that are almost parallel to the triangle

        Returns
        - `True` if the given ray intersects the frontface of the triangle; `False` otherwise

        See
        - .testRayTriangle(Vector3dc, Vector3dc, Vector3dc, Vector3dc, Vector3dc, double)
        """
        ...


    @staticmethod
    def testRayTriangle(origin: "Vector3dc", dir: "Vector3dc", v0: "Vector3dc", v1: "Vector3dc", v2: "Vector3dc", epsilon: float) -> bool:
        """
        Test whether the ray with the given `origin` and the given `dir` intersects the frontface of the triangle consisting of the three vertices
        `v0`, `v1` and `v2`.
        
        This is an implementation of the <a href="http://www.graphics.cornell.edu/pubs/1997/MT97.pdf">
        Fast, Minimum Storage Ray/Triangle Intersection</a> method.
        
        This test does not take into account the winding order of the triangle, so a ray will intersect a front-facing triangle as well as a back-facing triangle.

        Arguments
        - origin: the ray's origin
        - dir: the ray's direction
        - v0: the position of the first vertex
        - v1: the position of the second vertex
        - v2: the position of the third vertex
        - epsilon: a small epsilon when testing rays that are almost parallel to the triangle

        Returns
        - `True` if the given ray intersects the frontface of the triangle; `False` otherwise

        See
        - .testRayTriangle(double, double, double, double, double, double, double, double, double, double, double, double, double, double, double, double)
        """
        ...


    @staticmethod
    def intersectRayTriangleFront(originX: float, originY: float, originZ: float, dirX: float, dirY: float, dirZ: float, v0X: float, v0Y: float, v0Z: float, v1X: float, v1Y: float, v1Z: float, v2X: float, v2Y: float, v2Z: float, epsilon: float) -> float:
        """
        Determine whether the given ray with the origin `(originX, originY, originZ)` and direction `(dirX, dirY, dirZ)`
        intersects the frontface of the triangle consisting of the three vertices `(v0X, v0Y, v0Z)`, `(v1X, v1Y, v1Z)` and `(v2X, v2Y, v2Z)`
        and return the value of the parameter *t* in the ray equation *p(t) = origin + t * dir* of the point of intersection.
        
        This is an implementation of the <a href="http://www.graphics.cornell.edu/pubs/1997/MT97.pdf">
        Fast, Minimum Storage Ray/Triangle Intersection</a> method.
        
        This test implements backface culling, that is, it will return `False` when the triangle is in clockwise
        winding order assuming a *right-handed* coordinate system when seen along the ray's direction, even if the ray intersects the triangle.
        This is in compliance with how OpenGL handles backface culling with default frontface/backface settings.

        Arguments
        - originX: the x coordinate of the ray's origin
        - originY: the y coordinate of the ray's origin
        - originZ: the z coordinate of the ray's origin
        - dirX: the x coordinate of the ray's direction
        - dirY: the y coordinate of the ray's direction
        - dirZ: the z coordinate of the ray's direction
        - v0X: the x coordinate of the first vertex
        - v0Y: the y coordinate of the first vertex
        - v0Z: the z coordinate of the first vertex
        - v1X: the x coordinate of the second vertex
        - v1Y: the y coordinate of the second vertex
        - v1Z: the z coordinate of the second vertex
        - v2X: the x coordinate of the third vertex
        - v2Y: the y coordinate of the third vertex
        - v2Z: the z coordinate of the third vertex
        - epsilon: a small epsilon when testing rays that are almost parallel to the triangle

        Returns
        - the value of the parameter *t* in the ray equation *p(t) = origin + t * dir* of the point of intersection
                if the ray intersects the frontface of the triangle; `-1.0` otherwise

        See
        - .testRayTriangleFront(Vector3dc, Vector3dc, Vector3dc, Vector3dc, Vector3dc, double)
        """
        ...


    @staticmethod
    def intersectRayTriangleFront(origin: "Vector3dc", dir: "Vector3dc", v0: "Vector3dc", v1: "Vector3dc", v2: "Vector3dc", epsilon: float) -> float:
        """
        Determine whether the ray with the given `origin` and the given `dir` intersects the frontface of the triangle consisting of the three vertices
        `v0`, `v1` and `v2` and return the value of the parameter *t* in the ray equation *p(t) = origin + t * dir* of the point of intersection.
        
        This is an implementation of the <a href="http://www.graphics.cornell.edu/pubs/1997/MT97.pdf">
        Fast, Minimum Storage Ray/Triangle Intersection</a> method.
        
        This test implements backface culling, that is, it will return `False` when the triangle is in clockwise
        winding order assuming a *right-handed* coordinate system when seen along the ray's direction, even if the ray intersects the triangle.
        This is in compliance with how OpenGL handles backface culling with default frontface/backface settings.

        Arguments
        - origin: the ray's origin
        - dir: the ray's direction
        - v0: the position of the first vertex
        - v1: the position of the second vertex
        - v2: the position of the third vertex
        - epsilon: a small epsilon when testing rays that are almost parallel to the triangle

        Returns
        - the value of the parameter *t* in the ray equation *p(t) = origin + t * dir* of the point of intersection
                if the ray intersects the frontface of the triangle; `-1.0` otherwise

        See
        - .intersectRayTriangleFront(double, double, double, double, double, double, double, double, double, double, double, double, double, double, double, double)
        """
        ...


    @staticmethod
    def intersectRayTriangle(originX: float, originY: float, originZ: float, dirX: float, dirY: float, dirZ: float, v0X: float, v0Y: float, v0Z: float, v1X: float, v1Y: float, v1Z: float, v2X: float, v2Y: float, v2Z: float, epsilon: float) -> float:
        """
        Determine whether the given ray with the origin `(originX, originY, originZ)` and direction `(dirX, dirY, dirZ)`
        intersects the triangle consisting of the three vertices `(v0X, v0Y, v0Z)`, `(v1X, v1Y, v1Z)` and `(v2X, v2Y, v2Z)`
        and return the value of the parameter *t* in the ray equation *p(t) = origin + t * dir* of the point of intersection.
        
        This is an implementation of the <a href="http://www.graphics.cornell.edu/pubs/1997/MT97.pdf">
        Fast, Minimum Storage Ray/Triangle Intersection</a> method.
        
        This test does not take into account the winding order of the triangle, so a ray will intersect a front-facing triangle as well as a back-facing triangle.

        Arguments
        - originX: the x coordinate of the ray's origin
        - originY: the y coordinate of the ray's origin
        - originZ: the z coordinate of the ray's origin
        - dirX: the x coordinate of the ray's direction
        - dirY: the y coordinate of the ray's direction
        - dirZ: the z coordinate of the ray's direction
        - v0X: the x coordinate of the first vertex
        - v0Y: the y coordinate of the first vertex
        - v0Z: the z coordinate of the first vertex
        - v1X: the x coordinate of the second vertex
        - v1Y: the y coordinate of the second vertex
        - v1Z: the z coordinate of the second vertex
        - v2X: the x coordinate of the third vertex
        - v2Y: the y coordinate of the third vertex
        - v2Z: the z coordinate of the third vertex
        - epsilon: a small epsilon when testing rays that are almost parallel to the triangle

        Returns
        - the value of the parameter *t* in the ray equation *p(t) = origin + t * dir* of the point of intersection
                if the ray intersects the triangle; `-1.0` otherwise

        See
        - .testRayTriangle(Vector3dc, Vector3dc, Vector3dc, Vector3dc, Vector3dc, double)
        """
        ...


    @staticmethod
    def intersectRayTriangle(origin: "Vector3dc", dir: "Vector3dc", v0: "Vector3dc", v1: "Vector3dc", v2: "Vector3dc", epsilon: float) -> float:
        """
        Determine whether the ray with the given `origin` and the given `dir` intersects the triangle consisting of the three vertices
        `v0`, `v1` and `v2` and return the value of the parameter *t* in the ray equation *p(t) = origin + t * dir* of the point of intersection.
        
        This is an implementation of the <a href="http://www.graphics.cornell.edu/pubs/1997/MT97.pdf">
        Fast, Minimum Storage Ray/Triangle Intersection</a> method.
        
        This test does not take into account the winding order of the triangle, so a ray will intersect a front-facing triangle as well as a back-facing triangle.

        Arguments
        - origin: the ray's origin
        - dir: the ray's direction
        - v0: the position of the first vertex
        - v1: the position of the second vertex
        - v2: the position of the third vertex
        - epsilon: a small epsilon when testing rays that are almost parallel to the triangle

        Returns
        - the value of the parameter *t* in the ray equation *p(t) = origin + t * dir* of the point of intersection
                if the ray intersects the triangle; `-1.0` otherwise

        See
        - .intersectRayTriangle(double, double, double, double, double, double, double, double, double, double, double, double, double, double, double, double)
        """
        ...


    @staticmethod
    def testLineSegmentTriangle(p0X: float, p0Y: float, p0Z: float, p1X: float, p1Y: float, p1Z: float, v0X: float, v0Y: float, v0Z: float, v1X: float, v1Y: float, v1Z: float, v2X: float, v2Y: float, v2Z: float, epsilon: float) -> bool:
        """
        Test whether the line segment with the end points `(p0X, p0Y, p0Z)` and `(p1X, p1Y, p1Z)`
        intersects the triangle consisting of the three vertices `(v0X, v0Y, v0Z)`, `(v1X, v1Y, v1Z)` and `(v2X, v2Y, v2Z)`,
        regardless of the winding order of the triangle or the direction of the line segment between its two end points.
        
        Reference: <a href="http://www.graphics.cornell.edu/pubs/1997/MT97.pdf">
        Fast, Minimum Storage Ray/Triangle Intersection</a>

        Arguments
        - p0X: the x coordinate of the line segment's first end point
        - p0Y: the y coordinate of the line segment's first end point
        - p0Z: the z coordinate of the line segment's first end point
        - p1X: the x coordinate of the line segment's second end point
        - p1Y: the y coordinate of the line segment's second end point
        - p1Z: the z coordinate of the line segment's second end point
        - v0X: the x coordinate of the first vertex
        - v0Y: the y coordinate of the first vertex
        - v0Z: the z coordinate of the first vertex
        - v1X: the x coordinate of the second vertex
        - v1Y: the y coordinate of the second vertex
        - v1Z: the z coordinate of the second vertex
        - v2X: the x coordinate of the third vertex
        - v2Y: the y coordinate of the third vertex
        - v2Z: the z coordinate of the third vertex
        - epsilon: a small epsilon when testing line segments that are almost parallel to the triangle

        Returns
        - `True` if the given line segment intersects the triangle; `False` otherwise

        See
        - .testLineSegmentTriangle(Vector3dc, Vector3dc, Vector3dc, Vector3dc, Vector3dc, double)
        """
        ...


    @staticmethod
    def testLineSegmentTriangle(p0: "Vector3dc", p1: "Vector3dc", v0: "Vector3dc", v1: "Vector3dc", v2: "Vector3dc", epsilon: float) -> bool:
        """
        Test whether the line segment with the end points `p0` and `p1`
        intersects the triangle consisting of the three vertices `(v0X, v0Y, v0Z)`, `(v1X, v1Y, v1Z)` and `(v2X, v2Y, v2Z)`,
        regardless of the winding order of the triangle or the direction of the line segment between its two end points.
        
        Reference: <a href="http://www.graphics.cornell.edu/pubs/1997/MT97.pdf">
        Fast, Minimum Storage Ray/Triangle Intersection</a>

        Arguments
        - p0: the line segment's first end point
        - p1: the line segment's second end point
        - v0: the position of the first vertex
        - v1: the position of the second vertex
        - v2: the position of the third vertex
        - epsilon: a small epsilon when testing line segments that are almost parallel to the triangle

        Returns
        - `True` if the given line segment intersects the triangle; `False` otherwise

        See
        - .testLineSegmentTriangle(double, double, double, double, double, double, double, double, double, double, double, double, double, double, double, double)
        """
        ...


    @staticmethod
    def intersectLineSegmentTriangle(p0X: float, p0Y: float, p0Z: float, p1X: float, p1Y: float, p1Z: float, v0X: float, v0Y: float, v0Z: float, v1X: float, v1Y: float, v1Z: float, v2X: float, v2Y: float, v2Z: float, epsilon: float, intersectionPoint: "Vector3d") -> bool:
        """
        Determine whether the line segment with the end points `(p0X, p0Y, p0Z)` and `(p1X, p1Y, p1Z)`
        intersects the triangle consisting of the three vertices `(v0X, v0Y, v0Z)`, `(v1X, v1Y, v1Z)` and `(v2X, v2Y, v2Z)`,
        regardless of the winding order of the triangle or the direction of the line segment between its two end points,
        and return the point of intersection.
        
        Reference: <a href="http://www.graphics.cornell.edu/pubs/1997/MT97.pdf">
        Fast, Minimum Storage Ray/Triangle Intersection</a>

        Arguments
        - p0X: the x coordinate of the line segment's first end point
        - p0Y: the y coordinate of the line segment's first end point
        - p0Z: the z coordinate of the line segment's first end point
        - p1X: the x coordinate of the line segment's second end point
        - p1Y: the y coordinate of the line segment's second end point
        - p1Z: the z coordinate of the line segment's second end point
        - v0X: the x coordinate of the first vertex
        - v0Y: the y coordinate of the first vertex
        - v0Z: the z coordinate of the first vertex
        - v1X: the x coordinate of the second vertex
        - v1Y: the y coordinate of the second vertex
        - v1Z: the z coordinate of the second vertex
        - v2X: the x coordinate of the third vertex
        - v2Y: the y coordinate of the third vertex
        - v2Z: the z coordinate of the third vertex
        - epsilon: a small epsilon when testing line segments that are almost parallel to the triangle
        - intersectionPoint: the point of intersection

        Returns
        - `True` if the given line segment intersects the triangle; `False` otherwise

        See
        - .intersectLineSegmentTriangle(Vector3dc, Vector3dc, Vector3dc, Vector3dc, Vector3dc, double, Vector3d)
        """
        ...


    @staticmethod
    def intersectLineSegmentTriangle(p0: "Vector3dc", p1: "Vector3dc", v0: "Vector3dc", v1: "Vector3dc", v2: "Vector3dc", epsilon: float, intersectionPoint: "Vector3d") -> bool:
        """
        Determine whether the line segment with the end points `p0` and `p1`
        intersects the triangle consisting of the three vertices `(v0X, v0Y, v0Z)`, `(v1X, v1Y, v1Z)` and `(v2X, v2Y, v2Z)`,
        regardless of the winding order of the triangle or the direction of the line segment between its two end points,
        and return the point of intersection.
        
        Reference: <a href="http://www.graphics.cornell.edu/pubs/1997/MT97.pdf">
        Fast, Minimum Storage Ray/Triangle Intersection</a>

        Arguments
        - p0: the line segment's first end point
        - p1: the line segment's second end point
        - v0: the position of the first vertex
        - v1: the position of the second vertex
        - v2: the position of the third vertex
        - epsilon: a small epsilon when testing line segments that are almost parallel to the triangle
        - intersectionPoint: the point of intersection

        Returns
        - `True` if the given line segment intersects the triangle; `False` otherwise

        See
        - .intersectLineSegmentTriangle(double, double, double, double, double, double, double, double, double, double, double, double, double, double, double, double, Vector3d)
        """
        ...


    @staticmethod
    def intersectLineSegmentPlane(p0X: float, p0Y: float, p0Z: float, p1X: float, p1Y: float, p1Z: float, a: float, b: float, c: float, d: float, intersectionPoint: "Vector3d") -> bool:
        """
        Determine whether the line segment with the end points `(p0X, p0Y, p0Z)` and `(p1X, p1Y, p1Z)`
        intersects the plane given as the general plane equation *a*x + b*y + c*z + d = 0*,
        and return the point of intersection.

        Arguments
        - p0X: the x coordinate of the line segment's first end point
        - p0Y: the y coordinate of the line segment's first end point
        - p0Z: the z coordinate of the line segment's first end point
        - p1X: the x coordinate of the line segment's second end point
        - p1Y: the y coordinate of the line segment's second end point
        - p1Z: the z coordinate of the line segment's second end point
        - a: the x factor in the plane equation
        - b: the y factor in the plane equation
        - c: the z factor in the plane equation
        - d: the constant in the plane equation
        - intersectionPoint: the point of intersection

        Returns
        - `True` if the given line segment intersects the plane; `False` otherwise
        """
        ...


    @staticmethod
    def testLineCircle(a: float, b: float, c: float, centerX: float, centerY: float, radius: float) -> bool:
        """
        Test whether the line with the general line equation *a*x + b*y + c = 0* intersects the circle with center
        `(centerX, centerY)` and `radius`.
        
        Reference: <a href="http://math.stackexchange.com/questions/943383/determine-circle-of-intersection-of-plane-and-sphere">http://math.stackexchange.com</a>

        Arguments
        - a: the x factor in the line equation
        - b: the y factor in the line equation
        - c: the constant in the line equation
        - centerX: the x coordinate of the circle's center
        - centerY: the y coordinate of the circle's center
        - radius: the radius of the circle

        Returns
        - `True` iff the line intersects the circle; `False` otherwise
        """
        ...


    @staticmethod
    def intersectLineCircle(a: float, b: float, c: float, centerX: float, centerY: float, radius: float, intersectionCenterAndHL: "Vector3d") -> bool:
        """
        Test whether the line with the general line equation *a*x + b*y + c = 0* intersects the circle with center
        `(centerX, centerY)` and `radius`, and store the center of the line segment of
        intersection in the `(x, y)` components of the supplied vector and the half-length of that line segment in the z component.
        
        Reference: <a href="http://math.stackexchange.com/questions/943383/determine-circle-of-intersection-of-plane-and-sphere">http://math.stackexchange.com</a>

        Arguments
        - a: the x factor in the line equation
        - b: the y factor in the line equation
        - c: the constant in the line equation
        - centerX: the x coordinate of the circle's center
        - centerY: the y coordinate of the circle's center
        - radius: the radius of the circle
        - intersectionCenterAndHL: will hold the center of the line segment of intersection in the `(x, y)` components and the half-length in the z component

        Returns
        - `True` iff the line intersects the circle; `False` otherwise
        """
        ...


    @staticmethod
    def intersectLineCircle(x0: float, y0: float, x1: float, y1: float, centerX: float, centerY: float, radius: float, intersectionCenterAndHL: "Vector3d") -> bool:
        """
        Test whether the line defined by the two points `(x0, y0)` and `(x1, y1)` intersects the circle with center
        `(centerX, centerY)` and `radius`, and store the center of the line segment of
        intersection in the `(x, y)` components of the supplied vector and the half-length of that line segment in the z component.
        
        Reference: <a href="http://math.stackexchange.com/questions/943383/determine-circle-of-intersection-of-plane-and-sphere">http://math.stackexchange.com</a>

        Arguments
        - x0: the x coordinate of the first point on the line
        - y0: the y coordinate of the first point on the line
        - x1: the x coordinate of the second point on the line
        - y1: the y coordinate of the second point on the line
        - centerX: the x coordinate of the circle's center
        - centerY: the y coordinate of the circle's center
        - radius: the radius of the circle
        - intersectionCenterAndHL: will hold the center of the line segment of intersection in the `(x, y)` components and the half-length in the z component

        Returns
        - `True` iff the line intersects the circle; `False` otherwise
        """
        ...


    @staticmethod
    def testAarLine(minX: float, minY: float, maxX: float, maxY: float, a: float, b: float, c: float) -> bool:
        """
        Test whether the axis-aligned rectangle with minimum corner `(minX, minY)` and maximum corner `(maxX, maxY)`
        intersects the line with the general equation *a*x + b*y + c = 0*.
        
        Reference: <a href="http://www.lighthouse3d.com/tutorials/view-frustum-culling/geometric-approach-testing-boxes-ii/">http://www.lighthouse3d.com</a> ("Geometric Approach - Testing Boxes II")

        Arguments
        - minX: the x coordinate of the minimum corner of the axis-aligned rectangle
        - minY: the y coordinate of the minimum corner of the axis-aligned rectangle
        - maxX: the x coordinate of the maximum corner of the axis-aligned rectangle
        - maxY: the y coordinate of the maximum corner of the axis-aligned rectangle
        - a: the x factor in the line equation
        - b: the y factor in the line equation
        - c: the constant in the plane equation

        Returns
        - `True` iff the axis-aligned rectangle intersects the line; `False` otherwise
        """
        ...


    @staticmethod
    def testAarLine(min: "Vector2dc", max: "Vector2dc", a: float, b: float, c: float) -> bool:
        """
        Test whether the axis-aligned rectangle with minimum corner `min` and maximum corner `max`
        intersects the line with the general equation *a*x + b*y + c = 0*.
        
        Reference: <a href="http://www.lighthouse3d.com/tutorials/view-frustum-culling/geometric-approach-testing-boxes-ii/">http://www.lighthouse3d.com</a> ("Geometric Approach - Testing Boxes II")

        Arguments
        - min: the minimum corner of the axis-aligned rectangle
        - max: the maximum corner of the axis-aligned rectangle
        - a: the x factor in the line equation
        - b: the y factor in the line equation
        - c: the constant in the line equation

        Returns
        - `True` iff the axis-aligned rectangle intersects the line; `False` otherwise
        """
        ...


    @staticmethod
    def testAarLine(minX: float, minY: float, maxX: float, maxY: float, x0: float, y0: float, x1: float, y1: float) -> bool:
        """
        Test whether the axis-aligned rectangle with minimum corner `(minX, minY)` and maximum corner `(maxX, maxY)`
        intersects the line defined by the two points `(x0, y0)` and `(x1, y1)`.
        
        Reference: <a href="http://www.lighthouse3d.com/tutorials/view-frustum-culling/geometric-approach-testing-boxes-ii/">http://www.lighthouse3d.com</a> ("Geometric Approach - Testing Boxes II")

        Arguments
        - minX: the x coordinate of the minimum corner of the axis-aligned rectangle
        - minY: the y coordinate of the minimum corner of the axis-aligned rectangle
        - maxX: the x coordinate of the maximum corner of the axis-aligned rectangle
        - maxY: the y coordinate of the maximum corner of the axis-aligned rectangle
        - x0: the x coordinate of the first point on the line
        - y0: the y coordinate of the first point on the line
        - x1: the x coordinate of the second point on the line
        - y1: the y coordinate of the second point on the line

        Returns
        - `True` iff the axis-aligned rectangle intersects the line; `False` otherwise
        """
        ...


    @staticmethod
    def testAarAar(minXA: float, minYA: float, maxXA: float, maxYA: float, minXB: float, minYB: float, maxXB: float, maxYB: float) -> bool:
        """
        Test whether the axis-aligned rectangle with minimum corner `(minXA, minYA)` and maximum corner `(maxXA, maxYA)`
        intersects the axis-aligned rectangle with minimum corner `(minXB, minYB)` and maximum corner `(maxXB, maxYB)`.

        Arguments
        - minXA: the x coordinate of the minimum corner of the first axis-aligned rectangle
        - minYA: the y coordinate of the minimum corner of the first axis-aligned rectangle
        - maxXA: the x coordinate of the maximum corner of the first axis-aligned rectangle
        - maxYA: the y coordinate of the maximum corner of the first axis-aligned rectangle
        - minXB: the x coordinate of the minimum corner of the second axis-aligned rectangle
        - minYB: the y coordinate of the minimum corner of the second axis-aligned rectangle
        - maxXB: the x coordinate of the maximum corner of the second axis-aligned rectangle
        - maxYB: the y coordinate of the maximum corner of the second axis-aligned rectangle

        Returns
        - `True` iff both axis-aligned rectangles intersect; `False` otherwise
        """
        ...


    @staticmethod
    def testAarAar(minA: "Vector2dc", maxA: "Vector2dc", minB: "Vector2dc", maxB: "Vector2dc") -> bool:
        """
        Test whether the axis-aligned rectangle with minimum corner `minA` and maximum corner `maxA`
        intersects the axis-aligned rectangle with minimum corner `minB` and maximum corner `maxB`.

        Arguments
        - minA: the minimum corner of the first axis-aligned rectangle
        - maxA: the maximum corner of the first axis-aligned rectangle
        - minB: the minimum corner of the second axis-aligned rectangle
        - maxB: the maximum corner of the second axis-aligned rectangle

        Returns
        - `True` iff both axis-aligned rectangles intersect; `False` otherwise
        """
        ...


    @staticmethod
    def testMovingCircleCircle(aX: float, aY: float, maX: float, maY: float, aR: float, bX: float, bY: float, bR: float) -> bool:
        """
        Test whether a given circle with center `(aX, aY)` and radius `aR` and travelled distance vector `(maX, maY)`
        intersects a given static circle with center `(bX, bY)` and radius `bR`.
        
        Note that the case of two moving circles can always be reduced to this case by expressing the moved distance of one of the circles relative
        to the other.
        
        Reference: <a href="https://www.gamasutra.com/view/feature/131424/pool_hall_lessons_fast_accurate_.php?page=2">https://www.gamasutra.com</a>

        Arguments
        - aX: the x coordinate of the first circle's center
        - aY: the y coordinate of the first circle's center
        - maX: the x coordinate of the first circle's travelled distance vector
        - maY: the y coordinate of the first circle's travelled distance vector
        - aR: the radius of the first circle
        - bX: the x coordinate of the second circle's center
        - bY: the y coordinate of the second circle's center
        - bR: the radius of the second circle

        Returns
        - `True` if both circle intersect; `False` otherwise
        """
        ...


    @staticmethod
    def testMovingCircleCircle(centerA: "Vector2d", moveA: "Vector2d", aR: float, centerB: "Vector2d", bR: float) -> bool:
        """
        Test whether a given circle with center `centerA` and radius `aR` and travelled distance vector `moveA`
        intersects a given static circle with center `centerB` and radius `bR`.
        
        Note that the case of two moving circles can always be reduced to this case by expressing the moved distance of one of the circles relative
        to the other.
        
        Reference: <a href="https://www.gamasutra.com/view/feature/131424/pool_hall_lessons_fast_accurate_.php?page=2">https://www.gamasutra.com</a>

        Arguments
        - centerA: the coordinates of the first circle's center
        - moveA: the coordinates of the first circle's travelled distance vector
        - aR: the radius of the first circle
        - centerB: the coordinates of the second circle's center
        - bR: the radius of the second circle

        Returns
        - `True` if both circle intersect; `False` otherwise
        """
        ...


    @staticmethod
    def intersectCircleCircle(aX: float, aY: float, radiusSquaredA: float, bX: float, bY: float, radiusSquaredB: float, intersectionCenterAndHL: "Vector3d") -> bool:
        """
        Test whether the one circle with center `(aX, aY)` and square radius `radiusSquaredA` intersects the other
        circle with center `(bX, bY)` and square radius `radiusSquaredB`, and store the center of the line segment of
        intersection in the `(x, y)` components of the supplied vector and the half-length of that line segment in the z component.
        
        This method returns `False` when one circle contains the other circle.
        
        Reference: <a href="http://gamedev.stackexchange.com/questions/75756/sphere-sphere-intersection-and-circle-sphere-intersection">http://gamedev.stackexchange.com</a>

        Arguments
        - aX: the x coordinate of the first circle's center
        - aY: the y coordinate of the first circle's center
        - radiusSquaredA: the square of the first circle's radius
        - bX: the x coordinate of the second circle's center
        - bY: the y coordinate of the second circle's center
        - radiusSquaredB: the square of the second circle's radius
        - intersectionCenterAndHL: will hold the center of the circle of intersection in the `(x, y, z)` components and the radius in the w component

        Returns
        - `True` iff both circles intersect; `False` otherwise
        """
        ...


    @staticmethod
    def intersectCircleCircle(centerA: "Vector2dc", radiusSquaredA: float, centerB: "Vector2dc", radiusSquaredB: float, intersectionCenterAndHL: "Vector3d") -> bool:
        """
        Test whether the one circle with center `centerA` and square radius `radiusSquaredA` intersects the other
        circle with center `centerB` and square radius `radiusSquaredB`, and store the center of the line segment of
        intersection in the `(x, y)` components of the supplied vector and the half-length of that line segment in the z component.
        
        This method returns `False` when one circle contains the other circle.
        
        Reference: <a href="http://gamedev.stackexchange.com/questions/75756/sphere-sphere-intersection-and-circle-sphere-intersection">http://gamedev.stackexchange.com</a>

        Arguments
        - centerA: the first circle's center
        - radiusSquaredA: the square of the first circle's radius
        - centerB: the second circle's center
        - radiusSquaredB: the square of the second circle's radius
        - intersectionCenterAndHL: will hold the center of the line segment of intersection in the `(x, y)` components and the half-length in the z component

        Returns
        - `True` iff both circles intersect; `False` otherwise
        """
        ...


    @staticmethod
    def testCircleCircle(aX: float, aY: float, rA: float, bX: float, bY: float, rB: float) -> bool:
        """
        Test whether the one circle with center `(aX, aY)` and radius `rA` intersects the other circle with center `(bX, bY)` and radius `rB`.
        
        This method returns `True` when one circle contains the other circle.
        
        Reference: <a href="http://math.stackexchange.com/questions/275514/two-circles-overlap">http://math.stackexchange.com/</a>

        Arguments
        - aX: the x coordinate of the first circle's center
        - aY: the y coordinate of the first circle's center
        - rA: the square of the first circle's radius
        - bX: the x coordinate of the second circle's center
        - bY: the y coordinate of the second circle's center
        - rB: the square of the second circle's radius

        Returns
        - `True` iff both circles intersect; `False` otherwise
        """
        ...


    @staticmethod
    def testCircleCircle(centerA: "Vector2dc", radiusSquaredA: float, centerB: "Vector2dc", radiusSquaredB: float) -> bool:
        """
        Test whether the one circle with center `centerA` and square radius `radiusSquaredA` intersects the other
        circle with center `centerB` and square radius `radiusSquaredB`.
        
        This method returns `True` when one circle contains the other circle.
        
        Reference: <a href="http://gamedev.stackexchange.com/questions/75756/sphere-sphere-intersection-and-circle-sphere-intersection">http://gamedev.stackexchange.com</a>

        Arguments
        - centerA: the first circle's center
        - radiusSquaredA: the square of the first circle's radius
        - centerB: the second circle's center
        - radiusSquaredB: the square of the second circle's radius

        Returns
        - `True` iff both circles intersect; `False` otherwise
        """
        ...


    @staticmethod
    def distancePointLine(pointX: float, pointY: float, a: float, b: float, c: float) -> float:
        """
        Determine the signed distance of the given point `(pointX, pointY)` to the line specified via its general plane equation
        *a*x + b*y + c = 0*.
        
        Reference: <a href="http://mathworld.wolfram.com/Point-LineDistance2-Dimensional.html">http://mathworld.wolfram.com</a>

        Arguments
        - pointX: the x coordinate of the point
        - pointY: the y coordinate of the point
        - a: the x factor in the plane equation
        - b: the y factor in the plane equation
        - c: the constant in the plane equation

        Returns
        - the distance between the point and the line
        """
        ...


    @staticmethod
    def distancePointLine(pointX: float, pointY: float, x0: float, y0: float, x1: float, y1: float) -> float:
        """
        Determine the signed distance of the given point `(pointX, pointY)` to the line defined by the two points `(x0, y0)` and `(x1, y1)`.
        
        Reference: <a href="http://mathworld.wolfram.com/Point-LineDistance2-Dimensional.html">http://mathworld.wolfram.com</a>

        Arguments
        - pointX: the x coordinate of the point
        - pointY: the y coordinate of the point
        - x0: the x coordinate of the first point on the line
        - y0: the y coordinate of the first point on the line
        - x1: the x coordinate of the second point on the line
        - y1: the y coordinate of the second point on the line

        Returns
        - the distance between the point and the line
        """
        ...


    @staticmethod
    def distancePointLine(pX: float, pY: float, pZ: float, x0: float, y0: float, z0: float, x1: float, y1: float, z1: float) -> float:
        """
        Compute the distance of the given point `(pX, pY, pZ)` to the line defined by the two points `(x0, y0, z0)` and `(x1, y1, z1)`.
        
        Reference: <a href="http://mathworld.wolfram.com/Point-LineDistance3-Dimensional.html">http://mathworld.wolfram.com</a>

        Arguments
        - pX: the x coordinate of the point
        - pY: the y coordinate of the point
        - pZ: the z coordinate of the point
        - x0: the x coordinate of the first point on the line
        - y0: the y coordinate of the first point on the line
        - z0: the z coordinate of the first point on the line
        - x1: the x coordinate of the second point on the line
        - y1: the y coordinate of the second point on the line
        - z1: the z coordinate of the second point on the line

        Returns
        - the distance between the point and the line
        """
        ...


    @staticmethod
    def intersectRayLine(originX: float, originY: float, dirX: float, dirY: float, pointX: float, pointY: float, normalX: float, normalY: float, epsilon: float) -> float:
        """
        Test whether the ray with given origin `(originX, originY)` and direction `(dirX, dirY)` intersects the line
        containing the given point `(pointX, pointY)` and having the normal `(normalX, normalY)`, and return the
        value of the parameter *t* in the ray equation *p(t) = origin + t * dir* of the intersection point.
        
        This method returns `-1.0` if the ray does not intersect the line, because it is either parallel to the line or its direction points
        away from the line or the ray's origin is on the *negative* side of the line (i.e. the line's normal points away from the ray's origin).

        Arguments
        - originX: the x coordinate of the ray's origin
        - originY: the y coordinate of the ray's origin
        - dirX: the x coordinate of the ray's direction
        - dirY: the y coordinate of the ray's direction
        - pointX: the x coordinate of a point on the line
        - pointY: the y coordinate of a point on the line
        - normalX: the x coordinate of the line's normal
        - normalY: the y coordinate of the line's normal
        - epsilon: some small epsilon for when the ray is parallel to the line

        Returns
        - the value of the parameter *t* in the ray equation *p(t) = origin + t * dir* of the intersection point, if the ray
                intersects the line; `-1.0` otherwise
        """
        ...


    @staticmethod
    def intersectRayLine(origin: "Vector2dc", dir: "Vector2dc", point: "Vector2dc", normal: "Vector2dc", epsilon: float) -> float:
        """
        Test whether the ray with given `origin` and direction `dir` intersects the line
        containing the given `point` and having the given `normal`, and return the
        value of the parameter *t* in the ray equation *p(t) = origin + t * dir* of the intersection point.
        
        This method returns `-1.0` if the ray does not intersect the line, because it is either parallel to the line or its direction points
        away from the line or the ray's origin is on the *negative* side of the line (i.e. the line's normal points away from the ray's origin).

        Arguments
        - origin: the ray's origin
        - dir: the ray's direction
        - point: a point on the line
        - normal: the line's normal
        - epsilon: some small epsilon for when the ray is parallel to the line

        Returns
        - the value of the parameter *t* in the ray equation *p(t) = origin + t * dir* of the intersection point, if the ray
                intersects the line; `-1.0` otherwise
        """
        ...


    @staticmethod
    def intersectRayLineSegment(originX: float, originY: float, dirX: float, dirY: float, aX: float, aY: float, bX: float, bY: float) -> float:
        """
        Determine whether the ray with given origin `(originX, originY)` and direction `(dirX, dirY)` intersects the undirected line segment
        given by the two end points `(aX, bY)` and `(bX, bY)`, and return the value of the parameter *t* in the ray equation
        *p(t) = origin + t * dir* of the intersection point, if any.
        
        This method returns `-1.0` if the ray does not intersect the line segment.

        Arguments
        - originX: the x coordinate of the ray's origin
        - originY: the y coordinate of the ray's origin
        - dirX: the x coordinate of the ray's direction
        - dirY: the y coordinate of the ray's direction
        - aX: the x coordinate of the line segment's first end point
        - aY: the y coordinate of the line segment's first end point
        - bX: the x coordinate of the line segment's second end point
        - bY: the y coordinate of the line segment's second end point

        Returns
        - the value of the parameter *t* in the ray equation *p(t) = origin + t * dir* of the intersection point, if the ray
                intersects the line segment; `-1.0` otherwise

        See
        - .intersectRayLineSegment(Vector2dc, Vector2dc, Vector2dc, Vector2dc)
        """
        ...


    @staticmethod
    def intersectRayLineSegment(origin: "Vector2dc", dir: "Vector2dc", a: "Vector2dc", b: "Vector2dc") -> float:
        """
        Determine whether the ray with given `origin` and direction `dir` intersects the undirected line segment
        given by the two end points `a` and `b`, and return the value of the parameter *t* in the ray equation
        *p(t) = origin + t * dir* of the intersection point, if any.
        
        This method returns `-1.0` if the ray does not intersect the line segment.

        Arguments
        - origin: the ray's origin
        - dir: the ray's direction
        - a: the line segment's first end point
        - b: the line segment's second end point

        Returns
        - the value of the parameter *t* in the ray equation *p(t) = origin + t * dir* of the intersection point, if the ray
                intersects the line segment; `-1.0` otherwise

        See
        - .intersectRayLineSegment(double, double, double, double, double, double, double, double)
        """
        ...


    @staticmethod
    def testAarCircle(minX: float, minY: float, maxX: float, maxY: float, centerX: float, centerY: float, radiusSquared: float) -> bool:
        """
        Test whether the axis-aligned rectangle with minimum corner `(minX, minY)` and maximum corner `(maxX, maxY)`
        intersects the circle with the given center `(centerX, centerY)` and square radius `radiusSquared`.
        
        Reference: <a href="http://stackoverflow.com/questions/4578967/cube-sphere-intersection-test#answer-4579069">http://stackoverflow.com</a>

        Arguments
        - minX: the x coordinate of the minimum corner of the axis-aligned rectangle
        - minY: the y coordinate of the minimum corner of the axis-aligned rectangle
        - maxX: the x coordinate of the maximum corner of the axis-aligned rectangle
        - maxY: the y coordinate of the maximum corner of the axis-aligned rectangle
        - centerX: the x coordinate of the circle's center
        - centerY: the y coordinate of the circle's center
        - radiusSquared: the square of the circle's radius

        Returns
        - `True` iff the axis-aligned rectangle intersects the circle; `False` otherwise
        """
        ...


    @staticmethod
    def testAarCircle(min: "Vector2dc", max: "Vector2dc", center: "Vector2dc", radiusSquared: float) -> bool:
        """
        Test whether the axis-aligned rectangle with minimum corner `min` and maximum corner `max`
        intersects the circle with the given `center` and square radius `radiusSquared`.
        
        Reference: <a href="http://stackoverflow.com/questions/4578967/cube-sphere-intersection-test#answer-4579069">http://stackoverflow.com</a>

        Arguments
        - min: the minimum corner of the axis-aligned rectangle
        - max: the maximum corner of the axis-aligned rectangle
        - center: the circle's center
        - radiusSquared: the squared of the circle's radius

        Returns
        - `True` iff the axis-aligned rectangle intersects the circle; `False` otherwise
        """
        ...


    @staticmethod
    def findClosestPointOnTriangle(v0X: float, v0Y: float, v1X: float, v1Y: float, v2X: float, v2Y: float, pX: float, pY: float, result: "Vector2d") -> int:
        """
        Determine the closest point on the triangle with the given vertices `(v0X, v0Y)`, `(v1X, v1Y)`, `(v2X, v2Y)`
        between that triangle and the given point `(pX, pY)` and store that point into the given `result`.
        
        Additionally, this method returns whether the closest point is a vertex (.POINT_ON_TRIANGLE_VERTEX_0, .POINT_ON_TRIANGLE_VERTEX_1, .POINT_ON_TRIANGLE_VERTEX_2)
        of the triangle, lies on an edge (.POINT_ON_TRIANGLE_EDGE_01, .POINT_ON_TRIANGLE_EDGE_12, .POINT_ON_TRIANGLE_EDGE_20)
        or on the .POINT_ON_TRIANGLE_FACE face of the triangle.
        
        Reference: Book "Real-Time Collision Detection" chapter 5.1.5 "Closest Point on Triangle to Point"

        Arguments
        - v0X: the x coordinate of the first vertex of the triangle
        - v0Y: the y coordinate of the first vertex of the triangle
        - v1X: the x coordinate of the second vertex of the triangle
        - v1Y: the y coordinate of the second vertex of the triangle
        - v2X: the x coordinate of the third vertex of the triangle
        - v2Y: the y coordinate of the third vertex of the triangle
        - pX: the x coordinate of the point
        - pY: the y coordinate of the point
        - result: will hold the closest point

        Returns
        - one of .POINT_ON_TRIANGLE_VERTEX_0, .POINT_ON_TRIANGLE_VERTEX_1, .POINT_ON_TRIANGLE_VERTEX_2,
                       .POINT_ON_TRIANGLE_EDGE_01, .POINT_ON_TRIANGLE_EDGE_12, .POINT_ON_TRIANGLE_EDGE_20 or
                       .POINT_ON_TRIANGLE_FACE
        """
        ...


    @staticmethod
    def findClosestPointOnTriangle(v0: "Vector2dc", v1: "Vector2dc", v2: "Vector2dc", p: "Vector2dc", result: "Vector2d") -> int:
        """
        Determine the closest point on the triangle with the vertices `v0`, `v1`, `v2`
        between that triangle and the given point `p` and store that point into the given `result`.
        
        Additionally, this method returns whether the closest point is a vertex (.POINT_ON_TRIANGLE_VERTEX_0, .POINT_ON_TRIANGLE_VERTEX_1, .POINT_ON_TRIANGLE_VERTEX_2)
        of the triangle, lies on an edge (.POINT_ON_TRIANGLE_EDGE_01, .POINT_ON_TRIANGLE_EDGE_12, .POINT_ON_TRIANGLE_EDGE_20)
        or on the .POINT_ON_TRIANGLE_FACE face of the triangle.
        
        Reference: Book "Real-Time Collision Detection" chapter 5.1.5 "Closest Point on Triangle to Point"

        Arguments
        - v0: the first vertex of the triangle
        - v1: the second vertex of the triangle
        - v2: the third vertex of the triangle
        - p: the point
        - result: will hold the closest point

        Returns
        - one of .POINT_ON_TRIANGLE_VERTEX_0, .POINT_ON_TRIANGLE_VERTEX_1, .POINT_ON_TRIANGLE_VERTEX_2,
                       .POINT_ON_TRIANGLE_EDGE_01, .POINT_ON_TRIANGLE_EDGE_12, .POINT_ON_TRIANGLE_EDGE_20 or
                       .POINT_ON_TRIANGLE_FACE
        """
        ...


    @staticmethod
    def intersectRayCircle(originX: float, originY: float, dirX: float, dirY: float, centerX: float, centerY: float, radiusSquared: float, result: "Vector2d") -> bool:
        """
        Test whether the given ray with the origin `(originX, originY)` and direction `(dirX, dirY)`
        intersects the given circle with center `(centerX, centerY)` and square radius `radiusSquared`,
        and store the values of the parameter *t* in the ray equation *p(t) = origin + t * dir* for both points (near
        and far) of intersections into the given `result` vector.
        
        This method returns `True` for a ray whose origin lies inside the circle.
        
        Reference: <a href="http://www.scratchapixel.com/lessons/3d-basic-rendering/minimal-ray-tracer-rendering-simple-shapes/ray-sphere-intersection">http://www.scratchapixel.com/</a>

        Arguments
        - originX: the x coordinate of the ray's origin
        - originY: the y coordinate of the ray's origin
        - dirX: the x coordinate of the ray's direction
        - dirY: the y coordinate of the ray's direction
        - centerX: the x coordinate of the circle's center
        - centerY: the y coordinate of the circle's center
        - radiusSquared: the circle radius squared
        - result: a vector that will contain the values of the parameter *t* in the ray equation
                     *p(t) = origin + t * dir* for both points (near, far) of intersections with the circle

        Returns
        - `True` if the ray intersects the circle; `False` otherwise
        """
        ...


    @staticmethod
    def intersectRayCircle(origin: "Vector2dc", dir: "Vector2dc", center: "Vector2dc", radiusSquared: float, result: "Vector2d") -> bool:
        """
        Test whether the ray with the given `origin` and direction `dir`
        intersects the circle with the given `center` and square radius `radiusSquared`,
        and store the values of the parameter *t* in the ray equation *p(t) = origin + t * dir* for both points (near
        and far) of intersections into the given `result` vector.
        
        This method returns `True` for a ray whose origin lies inside the circle.
        
        Reference: <a href="http://www.scratchapixel.com/lessons/3d-basic-rendering/minimal-ray-tracer-rendering-simple-shapes/ray-sphere-intersection">http://www.scratchapixel.com/</a>

        Arguments
        - origin: the ray's origin
        - dir: the ray's direction
        - center: the circle's center
        - radiusSquared: the circle radius squared
        - result: a vector that will contain the values of the parameter *t* in the ray equation
                     *p(t) = origin + t * dir* for both points (near, far) of intersections with the circle

        Returns
        - `True` if the ray intersects the circle; `False` otherwise
        """
        ...


    @staticmethod
    def testRayCircle(originX: float, originY: float, dirX: float, dirY: float, centerX: float, centerY: float, radiusSquared: float) -> bool:
        """
        Test whether the given ray with the origin `(originX, originY)` and direction `(dirX, dirY)`
        intersects the given circle with center `(centerX, centerY)` and square radius `radiusSquared`.
        
        This method returns `True` for a ray whose origin lies inside the circle.
        
        Reference: <a href="http://www.scratchapixel.com/lessons/3d-basic-rendering/minimal-ray-tracer-rendering-simple-shapes/ray-sphere-intersection">http://www.scratchapixel.com/</a>

        Arguments
        - originX: the x coordinate of the ray's origin
        - originY: the y coordinate of the ray's origin
        - dirX: the x coordinate of the ray's direction
        - dirY: the y coordinate of the ray's direction
        - centerX: the x coordinate of the circle's center
        - centerY: the y coordinate of the circle's center
        - radiusSquared: the circle radius squared

        Returns
        - `True` if the ray intersects the circle; `False` otherwise
        """
        ...


    @staticmethod
    def testRayCircle(origin: "Vector2dc", dir: "Vector2dc", center: "Vector2dc", radiusSquared: float) -> bool:
        """
        Test whether the ray with the given `origin` and direction `dir`
        intersects the circle with the given `center` and square radius.
        
        This method returns `True` for a ray whose origin lies inside the circle.
        
        Reference: <a href="http://www.scratchapixel.com/lessons/3d-basic-rendering/minimal-ray-tracer-rendering-simple-shapes/ray-sphere-intersection">http://www.scratchapixel.com/</a>

        Arguments
        - origin: the ray's origin
        - dir: the ray's direction
        - center: the circle's center
        - radiusSquared: the circle radius squared

        Returns
        - `True` if the ray intersects the circle; `False` otherwise
        """
        ...


    @staticmethod
    def intersectRayAar(originX: float, originY: float, dirX: float, dirY: float, minX: float, minY: float, maxX: float, maxY: float, result: "Vector2d") -> int:
        """
        Determine whether the given ray with the origin `(originX, originY)` and direction `(dirX, dirY)`
        intersects the axis-aligned rectangle given as its minimum corner `(minX, minY)` and maximum corner `(maxX, maxY)`,
        and return the values of the parameter *t* in the ray equation *p(t) = origin + t * dir* of the near and far point of intersection
        as well as the side of the axis-aligned rectangle the ray intersects.
        
        This method also detects an intersection for a ray whose origin lies inside the axis-aligned rectangle.
        
        Reference: <a href="https://dl.acm.org/citation.cfm?id=1198748">An Efficient and Robust Ray–Box Intersection</a>

        Arguments
        - originX: the x coordinate of the ray's origin
        - originY: the y coordinate of the ray's origin
        - dirX: the x coordinate of the ray's direction
        - dirY: the y coordinate of the ray's direction
        - minX: the x coordinate of the minimum corner of the axis-aligned rectangle
        - minY: the y coordinate of the minimum corner of the axis-aligned rectangle
        - maxX: the x coordinate of the maximum corner of the axis-aligned rectangle
        - maxY: the y coordinate of the maximum corner of the axis-aligned rectangle
        - result: a vector which will hold the values of the parameter *t* in the ray equation
                     *p(t) = origin + t * dir* of the near and far point of intersection

        Returns
        - the side on which the near intersection occurred as one of
                .AAR_SIDE_MINX, .AAR_SIDE_MINY, .AAR_SIDE_MAXX or .AAR_SIDE_MAXY;
                or `-1` if the ray does not intersect the axis-aligned rectangle;

        See
        - .intersectRayAar(Vector2dc, Vector2dc, Vector2dc, Vector2dc, Vector2d)
        """
        ...


    @staticmethod
    def intersectRayAar(origin: "Vector2dc", dir: "Vector2dc", min: "Vector2dc", max: "Vector2dc", result: "Vector2d") -> int:
        """
        Determine whether the given ray with the given `origin` and direction `dir`
        intersects the axis-aligned rectangle given as its minimum corner `min` and maximum corner `max`,
        and return the values of the parameter *t* in the ray equation *p(t) = origin + t * dir* of the near and far point of intersection
        as well as the side of the axis-aligned rectangle the ray intersects.
        
        This method also detects an intersection for a ray whose origin lies inside the axis-aligned rectangle.
        
        Reference: <a href="https://dl.acm.org/citation.cfm?id=1198748">An Efficient and Robust Ray–Box Intersection</a>

        Arguments
        - origin: the ray's origin
        - dir: the ray's direction
        - min: the minimum corner of the axis-aligned rectangle
        - max: the maximum corner of the axis-aligned rectangle
        - result: a vector which will hold the values of the parameter *t* in the ray equation
                     *p(t) = origin + t * dir* of the near and far point of intersection

        Returns
        - the side on which the near intersection occurred as one of
                .AAR_SIDE_MINX, .AAR_SIDE_MINY, .AAR_SIDE_MAXX or .AAR_SIDE_MAXY;
                or `-1` if the ray does not intersect the axis-aligned rectangle;

        See
        - .intersectRayAar(double, double, double, double, double, double, double, double, Vector2d)
        """
        ...


    @staticmethod
    def intersectLineSegmentAar(p0X: float, p0Y: float, p1X: float, p1Y: float, minX: float, minY: float, maxX: float, maxY: float, result: "Vector2d") -> int:
        """
        Determine whether the undirected line segment with the end points `(p0X, p0Y)` and `(p1X, p1Y)`
        intersects the axis-aligned rectangle given as its minimum corner `(minX, minY)` and maximum corner `(maxX, maxY)`,
        and store the values of the parameter *t* in the ray equation *p(t) = p0 + t * (p1 - p0)* of the near and far point of intersection
        into `result`.
        
        This method also detects an intersection of a line segment whose either end point lies inside the axis-aligned rectangle.
        
        Reference: <a href="https://dl.acm.org/citation.cfm?id=1198748">An Efficient and Robust Ray–Box Intersection</a>

        Arguments
        - p0X: the x coordinate of the line segment's first end point
        - p0Y: the y coordinate of the line segment's first end point
        - p1X: the x coordinate of the line segment's second end point
        - p1Y: the y coordinate of the line segment's second end point
        - minX: the x coordinate of the minimum corner of the axis-aligned rectangle
        - minY: the y coordinate of the minimum corner of the axis-aligned rectangle
        - maxX: the x coordinate of the maximum corner of the axis-aligned rectangle
        - maxY: the y coordinate of the maximum corner of the axis-aligned rectangle
        - result: a vector which will hold the values of the parameter *t* in the ray equation
                     *p(t) = p0 + t * (p1 - p0)* of the near and far point of intersection

        Returns
        - .INSIDE if the line segment lies completely inside of the axis-aligned rectangle; or
                .OUTSIDE if the line segment lies completely outside of the axis-aligned rectangle; or
                .ONE_INTERSECTION if one of the end points of the line segment lies inside of the axis-aligned rectangle; or
                .TWO_INTERSECTION if the line segment intersects two edges of the axis-aligned rectangle or lies on one edge of the rectangle

        See
        - .intersectLineSegmentAar(Vector2dc, Vector2dc, Vector2dc, Vector2dc, Vector2d)
        """
        ...


    @staticmethod
    def intersectLineSegmentAar(p0: "Vector2dc", p1: "Vector2dc", min: "Vector2dc", max: "Vector2dc", result: "Vector2d") -> int:
        """
        Determine whether the undirected line segment with the end points `p0` and `p1`
        intersects the axis-aligned rectangle given as its minimum corner `min` and maximum corner `max`,
        and store the values of the parameter *t* in the ray equation *p(t) = p0 + t * (p1 - p0)* of the near and far point of intersection
        into `result`.
        
        This method also detects an intersection of a line segment whose either end point lies inside the axis-aligned rectangle.
        
        Reference: <a href="https://dl.acm.org/citation.cfm?id=1198748">An Efficient and Robust Ray–Box Intersection</a>
        
        #see .intersectLineSegmentAar(double, double, double, double, double, double, double, double, Vector2d)

        Arguments
        - p0: the line segment's first end point
        - p1: the line segment's second end point
        - min: the minimum corner of the axis-aligned rectangle
        - max: the maximum corner of the axis-aligned rectangle
        - result: a vector which will hold the values of the parameter *t* in the ray equation
                     *p(t) = p0 + t * (p1 - p0)* of the near and far point of intersection

        Returns
        - .INSIDE if the line segment lies completely inside of the axis-aligned rectangle; or
                .OUTSIDE if the line segment lies completely outside of the axis-aligned rectangle; or
                .ONE_INTERSECTION if one of the end points of the line segment lies inside of the axis-aligned rectangle; or
                .TWO_INTERSECTION if the line segment intersects two edges of the axis-aligned rectangle
        """
        ...


    @staticmethod
    def testRayAar(originX: float, originY: float, dirX: float, dirY: float, minX: float, minY: float, maxX: float, maxY: float) -> bool:
        """
        Test whether the given ray with the origin `(originX, originY)` and direction `(dirX, dirY)`
        intersects the given axis-aligned rectangle given as its minimum corner `(minX, minY)` and maximum corner `(maxX, maxY)`.
        
        This method returns `True` for a ray whose origin lies inside the axis-aligned rectangle.
        
        Reference: <a href="https://dl.acm.org/citation.cfm?id=1198748">An Efficient and Robust Ray–Box Intersection</a>

        Arguments
        - originX: the x coordinate of the ray's origin
        - originY: the y coordinate of the ray's origin
        - dirX: the x coordinate of the ray's direction
        - dirY: the y coordinate of the ray's direction
        - minX: the x coordinate of the minimum corner of the axis-aligned rectangle
        - minY: the y coordinate of the minimum corner of the axis-aligned rectangle
        - maxX: the x coordinate of the maximum corner of the axis-aligned rectangle
        - maxY: the y coordinate of the maximum corner of the axis-aligned rectangle

        Returns
        - `True` if the given ray intersects the axis-aligned rectangle; `False` otherwise

        See
        - .testRayAar(Vector2dc, Vector2dc, Vector2dc, Vector2dc)
        """
        ...


    @staticmethod
    def testRayAar(origin: "Vector2dc", dir: "Vector2dc", min: "Vector2dc", max: "Vector2dc") -> bool:
        """
        Test whether the ray with the given `origin` and direction `dir`
        intersects the given axis-aligned rectangle specified as its minimum corner `min` and maximum corner `max`.
        
        This method returns `True` for a ray whose origin lies inside the axis-aligned rectangle.
        
        Reference: <a href="https://dl.acm.org/citation.cfm?id=1198748">An Efficient and Robust Ray–Box Intersection</a>

        Arguments
        - origin: the ray's origin
        - dir: the ray's direction
        - min: the minimum corner of the axis-aligned rectangle
        - max: the maximum corner of the axis-aligned rectangle

        Returns
        - `True` if the given ray intersects the axis-aligned rectangle; `False` otherwise

        See
        - .testRayAar(double, double, double, double, double, double, double, double)
        """
        ...


    @staticmethod
    def testPointTriangle(pX: float, pY: float, v0X: float, v0Y: float, v1X: float, v1Y: float, v2X: float, v2Y: float) -> bool:
        """
        Test whether the given point `(pX, pY)` lies inside the triangle with the vertices `(v0X, v0Y)`, `(v1X, v1Y)`, `(v2X, v2Y)`.

        Arguments
        - pX: the x coordinate of the point
        - pY: the y coordinate of the point
        - v0X: the x coordinate of the first vertex of the triangle
        - v0Y: the y coordinate of the first vertex of the triangle
        - v1X: the x coordinate of the second vertex of the triangle
        - v1Y: the y coordinate of the second vertex of the triangle
        - v2X: the x coordinate of the third vertex of the triangle
        - v2Y: the y coordinate of the third vertex of the triangle

        Returns
        - `True` iff the point lies inside the triangle; `False` otherwise
        """
        ...


    @staticmethod
    def testPointTriangle(point: "Vector2dc", v0: "Vector2dc", v1: "Vector2dc", v2: "Vector2dc") -> bool:
        """
        Test whether the given `point` lies inside the triangle with the vertices `v0`, `v1`, `v2`.

        Arguments
        - v0: the first vertex of the triangle
        - v1: the second vertex of the triangle
        - v2: the third vertex of the triangle
        - point: the point

        Returns
        - `True` iff the point lies inside the triangle; `False` otherwise
        """
        ...


    @staticmethod
    def testPointAar(pX: float, pY: float, minX: float, minY: float, maxX: float, maxY: float) -> bool:
        """
        Test whether the given point `(pX, pY)` lies inside the axis-aligned rectangle with the minimum corner `(minX, minY)`
        and maximum corner `(maxX, maxY)`.

        Arguments
        - pX: the x coordinate of the point
        - pY: the y coordinate of the point
        - minX: the x coordinate of the minimum corner of the axis-aligned rectangle
        - minY: the y coordinate of the minimum corner of the axis-aligned rectangle
        - maxX: the x coordinate of the maximum corner of the axis-aligned rectangle
        - maxY: the y coordinate of the maximum corner of the axis-aligned rectangle

        Returns
        - `True` iff the point lies inside the axis-aligned rectangle; `False` otherwise
        """
        ...


    @staticmethod
    def testPointCircle(pX: float, pY: float, centerX: float, centerY: float, radiusSquared: float) -> bool:
        """
        Test whether the point `(pX, pY)` lies inside the circle with center `(centerX, centerY)` and square radius `radiusSquared`.

        Arguments
        - pX: the x coordinate of the point
        - pY: the y coordinate of the point
        - centerX: the x coordinate of the circle's center
        - centerY: the y coordinate of the circle's center
        - radiusSquared: the square radius of the circle

        Returns
        - `True` iff the point lies inside the circle; `False` otherwise
        """
        ...


    @staticmethod
    def testCircleTriangle(centerX: float, centerY: float, radiusSquared: float, v0X: float, v0Y: float, v1X: float, v1Y: float, v2X: float, v2Y: float) -> bool:
        """
        Test whether the circle with center `(centerX, centerY)` and square radius `radiusSquared` intersects the triangle with counter-clockwise vertices
        `(v0X, v0Y)`, `(v1X, v1Y)`, `(v2X, v2Y)`.
        
        The vertices of the triangle must be specified in counter-clockwise order.
        
        Reference: <a href="http://www.phatcode.net/articles.php?id=459">http://www.phatcode.net/</a>

        Arguments
        - centerX: the x coordinate of the circle's center
        - centerY: the y coordinate of the circle's center
        - radiusSquared: the square radius of the circle
        - v0X: the x coordinate of the first vertex of the triangle
        - v0Y: the y coordinate of the first vertex of the triangle
        - v1X: the x coordinate of the second vertex of the triangle
        - v1Y: the y coordinate of the second vertex of the triangle
        - v2X: the x coordinate of the third vertex of the triangle
        - v2Y: the y coordinate of the third vertex of the triangle

        Returns
        - `True` iff the circle intersects the triangle; `False` otherwise
        """
        ...


    @staticmethod
    def testCircleTriangle(center: "Vector2dc", radiusSquared: float, v0: "Vector2dc", v1: "Vector2dc", v2: "Vector2dc") -> bool:
        """
        Test whether the circle with given `center` and square radius `radiusSquared` intersects the triangle with counter-clockwise vertices
        `v0`, `v1`, `v2`.
        
        The vertices of the triangle must be specified in counter-clockwise order.
        
        Reference: <a href="http://www.phatcode.net/articles.php?id=459">http://www.phatcode.net/</a>

        Arguments
        - center: the circle's center
        - radiusSquared: the square radius of the circle
        - v0: the first vertex of the triangle
        - v1: the second vertex of the triangle
        - v2: the third vertex of the triangle

        Returns
        - `True` iff the circle intersects the triangle; `False` otherwise
        """
        ...


    @staticmethod
    def intersectPolygonRay(verticesXY: list[float], originX: float, originY: float, dirX: float, dirY: float, p: "Vector2d") -> int:
        """
        Determine whether the polygon specified by the given sequence of `(x, y)` coordinate pairs intersects with the ray
        with given origin `(originX, originY, originZ)` and direction `(dirX, dirY, dirZ)`, and store the point of intersection
        into the given vector `p`.
        
        If the polygon intersects the ray, this method returns the index of the polygon edge intersecting the ray, that is, the index of the 
        first vertex of the directed line segment. The second vertex is always that index + 1, modulus the number of polygon vertices.

        Arguments
        - verticesXY: the sequence of `(x, y)` coordinate pairs of all vertices of the polygon
        - originX: the x coordinate of the ray's origin
        - originY: the y coordinate of the ray's origin
        - dirX: the x coordinate of the ray's direction
        - dirY: the y coordinate of the ray's direction
        - p: will hold the point of intersection

        Returns
        - the index of the first vertex of the polygon edge that intersects the ray; or `-1` if the ray does not intersect the polygon
        """
        ...


    @staticmethod
    def intersectPolygonRay(vertices: list["Vector2dc"], originX: float, originY: float, dirX: float, dirY: float, p: "Vector2d") -> int:
        """
        Determine whether the polygon specified by the given sequence of `vertices` intersects with the ray
        with given origin `(originX, originY, originZ)` and direction `(dirX, dirY, dirZ)`, and store the point of intersection
        into the given vector `p`.
        
        If the polygon intersects the ray, this method returns the index of the polygon edge intersecting the ray, that is, the index of the 
        first vertex of the directed line segment. The second vertex is always that index + 1, modulus the number of polygon vertices.

        Arguments
        - vertices: the sequence of `(x, y)` coordinate pairs of all vertices of the polygon
        - originX: the x coordinate of the ray's origin
        - originY: the y coordinate of the ray's origin
        - dirX: the x coordinate of the ray's direction
        - dirY: the y coordinate of the ray's direction
        - p: will hold the point of intersection

        Returns
        - the index of the first vertex of the polygon edge that intersects the ray; or `-1` if the ray does not intersect the polygon
        """
        ...


    @staticmethod
    def intersectLineLine(ps1x: float, ps1y: float, pe1x: float, pe1y: float, ps2x: float, ps2y: float, pe2x: float, pe2y: float, p: "Vector2d") -> bool:
        """
        Determine whether the two lines, specified via two points lying on each line, intersect each other, and store the point of intersection
        into the given vector `p`.

        Arguments
        - ps1x: the x coordinate of the first point on the first line
        - ps1y: the y coordinate of the first point on the first line
        - pe1x: the x coordinate of the second point on the first line
        - pe1y: the y coordinate of the second point on the first line
        - ps2x: the x coordinate of the first point on the second line
        - ps2y: the y coordinate of the first point on the second line
        - pe2x: the x coordinate of the second point on the second line
        - pe2y: the y coordinate of the second point on the second line
        - p: will hold the point of intersection

        Returns
        - `True` iff the two lines intersect; `False` otherwise
        """
        ...


    @staticmethod
    def testPolygonPolygon(v1s: list["Vector2d"], v2s: list["Vector2d"]) -> bool:
        """
        Test if the two convex polygons, given via their vertices, intersect.

        Arguments
        - v1s: the vertices of the first convex polygon
        - v2s: the vertices of the second convex polygon

        Returns
        - `True` if the convex polygons intersect; `False` otherwise
        """
        ...
