"""
Python module generated from Java source file org.joml.FrustumIntersection

Java source file obtained from artifact joml version 1.10.5

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.joml import *
from typing import Any, Callable, Iterable, Tuple


class FrustumIntersection:
    """
    Efficiently performs frustum intersection tests by caching the frustum planes of an arbitrary transformation Matrix4fc matrix.
    
    This class is preferred over the frustum intersection methods in Matrix4fc when many objects need to be culled by the same static frustum.

    Author(s)
    - Kai Burjack
    """

    PLANE_NX = 0
    """
    Return value of .intersectAab(float, float, float, float, float, float) intersectAab()
    and its different overloads identifying the plane with equation `x=-1` when using the identity frustum.
    """
    PLANE_PX = 1
    """
    Return value of .intersectAab(float, float, float, float, float, float) intersectAab()
    and its different overloads identifying the plane with equation `x=1` when using the identity frustum.
    """
    PLANE_NY = 2
    """
    Return value of .intersectAab(float, float, float, float, float, float) intersectAab()
    and its different overloads identifying the plane with equation `y=-1` when using the identity frustum.
    """
    PLANE_PY = 3
    """
    Return value of .intersectAab(float, float, float, float, float, float) intersectAab()
    and its different overloads identifying the plane with equation `y=1` when using the identity frustum.
    """
    PLANE_NZ = 4
    """
    Return value of .intersectAab(float, float, float, float, float, float) intersectAab()
    and its different overloads identifying the plane with equation `z=-1` when using the identity frustum.
    """
    PLANE_PZ = 5
    """
    Return value of .intersectAab(float, float, float, float, float, float) intersectAab()
    and its different overloads identifying the plane with equation `z=1` when using the identity frustum.
    """
    INTERSECT = -1
    """
    Return value of .intersectAab(float, float, float, float, float, float) intersectAab()
    and its different overloads indicating that the axis-aligned box intersects the frustum.
    """
    INSIDE = -2
    """
    Return value of .intersectAab(float, float, float, float, float, float) intersectAab()
    and its different overloads indicating that the axis-aligned box is fully inside of the frustum.
    """
    OUTSIDE = -3
    """
    Return value of .intersectSphere(Vector3fc, float) or .intersectSphere(float, float, float, float)
    indicating that the sphere is completely outside of the frustum.
    """
    PLANE_MASK_NX = 1 << PLANE_NX
    """
    The value in a bitmask for
    .intersectAab(float, float, float, float, float, float, int) intersectAab()
    that identifies the plane with equation `x=-1` when using the identity frustum.
    """
    PLANE_MASK_PX = 1 << PLANE_PX
    """
    The value in a bitmask for
    .intersectAab(float, float, float, float, float, float, int) intersectAab()
    that identifies the plane with equation `x=1` when using the identity frustum.
    """
    PLANE_MASK_NY = 1 << PLANE_NY
    """
    The value in a bitmask for
    .intersectAab(float, float, float, float, float, float, int) intersectAab()
    that identifies the plane with equation `y=-1` when using the identity frustum.
    """
    PLANE_MASK_PY = 1 << PLANE_PY
    """
    The value in a bitmask for
    .intersectAab(float, float, float, float, float, float, int) intersectAab()
    that identifies the plane with equation `y=1` when using the identity frustum.
    """
    PLANE_MASK_NZ = 1 << PLANE_NZ
    """
    The value in a bitmask for
    .intersectAab(float, float, float, float, float, float, int) intersectAab()
    that identifies the plane with equation `z=-1` when using the identity frustum.
    """
    PLANE_MASK_PZ = 1 << PLANE_PZ
    """
    The value in a bitmask for
    .intersectAab(float, float, float, float, float, float, int) intersectAab()
    that identifies the plane with equation `z=1` when using the identity frustum.
    """


    def __init__(self):
        """
        Create a new FrustumIntersection with undefined frustum planes.
        
        Before using any of the frustum culling methods, make sure to define the frustum planes using .set(Matrix4fc).
        """
        ...


    def __init__(self, m: "Matrix4fc"):
        """
        Create a new FrustumIntersection from the given Matrix4fc matrix by extracing the matrix's frustum planes.
        
        In order to update the compute frustum planes later on, call .set(Matrix4fc).

        Arguments
        - m: the Matrix4fc to create the frustum culler from

        See
        - .set(Matrix4fc)
        """
        ...


    def __init__(self, m: "Matrix4fc", allowTestSpheres: bool):
        """
        Create a new FrustumIntersection from the given Matrix4fc matrix by extracing the matrix's frustum planes.
        
        In order to update the compute frustum planes later on, call .set(Matrix4fc).

        Arguments
        - m: the Matrix4fc to create the frustum culler from
        - allowTestSpheres: whether the methods .testSphere(Vector3fc, float), .testSphere(float, float, float, float),
                 .intersectSphere(Vector3fc, float) or .intersectSphere(float, float, float, float) will used.
                 If no spheres need to be tested, then `False` should be used

        See
        - .set(Matrix4fc)
        """
        ...


    def set(self, m: "Matrix4fc") -> "FrustumIntersection":
        """
        Update the stored frustum planes of `this` FrustumIntersection with the given Matrix4fc matrix.
        
        Reference: <a href="http://gamedevs.org/uploads/fast-extraction-viewing-frustum-planes-from-world-view-projection-matrix.pdf">
        Fast Extraction of Viewing Frustum Planes from the World-View-Projection Matrix</a>

        Arguments
        - m: the Matrix4fc matrix to update `this` frustum culler's frustum planes from

        Returns
        - this
        """
        ...


    def set(self, m: "Matrix4fc", allowTestSpheres: bool) -> "FrustumIntersection":
        """
        Update the stored frustum planes of `this` FrustumIntersection with the given Matrix4fc matrix and
        allow to optimize the frustum plane extraction in the case when no intersection test is needed for spheres.
        
        Reference: <a href="http://gamedevs.org/uploads/fast-extraction-viewing-frustum-planes-from-world-view-projection-matrix.pdf">
        Fast Extraction of Viewing Frustum Planes from the World-View-Projection Matrix</a>

        Arguments
        - m: the Matrix4fc matrix to update `this` frustum culler's frustum planes from
        - allowTestSpheres: whether the methods .testSphere(Vector3fc, float), .testSphere(float, float, float, float),
                 .intersectSphere(Vector3fc, float) or .intersectSphere(float, float, float, float) will be used.
                 If no spheres need to be tested, then `False` should be used

        Returns
        - this
        """
        ...


    def testPoint(self, point: "Vector3fc") -> bool:
        """
        Test whether the given point is within the frustum defined by `this` frustum culler.

        Arguments
        - point: the point to test

        Returns
        - `True` if the given point is inside the frustum; `False` otherwise
        """
        ...


    def testPoint(self, x: float, y: float, z: float) -> bool:
        """
        Test whether the given point `(x, y, z)` is within the frustum defined by `this` frustum culler.

        Arguments
        - x: the x-coordinate of the point
        - y: the y-coordinate of the point
        - z: the z-coordinate of the point

        Returns
        - `True` if the given point is inside the frustum; `False` otherwise
        """
        ...


    def testSphere(self, center: "Vector3fc", radius: float) -> bool:
        """
        Test whether the given sphere is partly or completely within or outside of the frustum defined by `this` frustum culler.
        
        The algorithm implemented by this method is conservative. This means that in certain circumstances a *False positive*
        can occur, when the method returns `True` for spheres that do not intersect the frustum.
        See <a href="http://iquilezles.org/www/articles/frustumcorrect/frustumcorrect.htm">iquilezles.org</a> for an examination of this problem.

        Arguments
        - center: the sphere's center
        - radius: the sphere's radius

        Returns
        - `True` if the given sphere is partly or completely inside the frustum;
                `False` otherwise
        """
        ...


    def testSphere(self, x: float, y: float, z: float, r: float) -> bool:
        """
        Test whether the given sphere is partly or completely within or outside of the frustum defined by `this` frustum culler.
        
        The algorithm implemented by this method is conservative. This means that in certain circumstances a *False positive*
        can occur, when the method returns `True` for spheres that do not intersect the frustum.
        See <a href="http://iquilezles.org/www/articles/frustumcorrect/frustumcorrect.htm">iquilezles.org</a> for an examination of this problem.

        Arguments
        - x: the x-coordinate of the sphere's center
        - y: the y-coordinate of the sphere's center
        - z: the z-coordinate of the sphere's center
        - r: the sphere's radius

        Returns
        - `True` if the given sphere is partly or completely inside the frustum;
                `False` otherwise
        """
        ...


    def intersectSphere(self, center: "Vector3fc", radius: float) -> int:
        """
        Determine whether the given sphere is partly or completely within or outside of the frustum defined by `this` frustum culler.
        
        The algorithm implemented by this method is conservative. This means that in certain circumstances a *False positive*
        can occur, when the method returns .INTERSECT for spheres that do not intersect the frustum.
        See <a href="http://iquilezles.org/www/articles/frustumcorrect/frustumcorrect.htm">iquilezles.org</a> for an examination of this problem.

        Arguments
        - center: the sphere's center
        - radius: the sphere's radius

        Returns
        - .INSIDE if the given sphere is completely inside the frustum, or .INTERSECT if the sphere intersects
                the frustum, or .OUTSIDE if the sphere is outside of the frustum
        """
        ...


    def intersectSphere(self, x: float, y: float, z: float, r: float) -> int:
        """
        Determine whether the given sphere is partly or completely within or outside of the frustum defined by `this` frustum culler.
        
        The algorithm implemented by this method is conservative. This means that in certain circumstances a *False positive*
        can occur, when the method returns .INTERSECT for spheres that do not intersect the frustum.
        See <a href="http://iquilezles.org/www/articles/frustumcorrect/frustumcorrect.htm">iquilezles.org</a> for an examination of this problem.

        Arguments
        - x: the x-coordinate of the sphere's center
        - y: the y-coordinate of the sphere's center
        - z: the z-coordinate of the sphere's center
        - r: the sphere's radius

        Returns
        - .INSIDE if the given sphere is completely inside the frustum, or .INTERSECT if the sphere intersects
                the frustum, or .OUTSIDE if the sphere is outside of the frustum
        """
        ...


    def testAab(self, min: "Vector3fc", max: "Vector3fc") -> bool:
        """
        Test whether the given axis-aligned box is partly or completely within or outside of the frustum defined by `this` frustum culler.
        The box is specified via its `min` and `max` corner coordinates.
        
        The algorithm implemented by this method is conservative. This means that in certain circumstances a *False positive*
        can occur, when the method returns `True` for boxes that do not intersect the frustum.
        See <a href="http://iquilezles.org/www/articles/frustumcorrect/frustumcorrect.htm">iquilezles.org</a> for an examination of this problem.

        Arguments
        - min: the minimum corner coordinates of the axis-aligned box
        - max: the maximum corner coordinates of the axis-aligned box

        Returns
        - `True` if the axis-aligned box is completely or partly inside of the frustum; `False` otherwise
        """
        ...


    def testAab(self, minX: float, minY: float, minZ: float, maxX: float, maxY: float, maxZ: float) -> bool:
        """
        Test whether the given axis-aligned box is partly or completely within or outside of the frustum defined by `this` frustum culler.
        The box is specified via its min and max corner coordinates.
        
        The algorithm implemented by this method is conservative. This means that in certain circumstances a *False positive*
        can occur, when the method returns `True` for boxes that do not intersect the frustum.
        See <a href="http://iquilezles.org/www/articles/frustumcorrect/frustumcorrect.htm">iquilezles.org</a> for an examination of this problem.
        
        Reference: <a href="http://old.cescg.org/CESCG-2002/DSykoraJJelinek/">Efficient View Frustum Culling</a>

        Arguments
        - minX: the x-coordinate of the minimum corner
        - minY: the y-coordinate of the minimum corner
        - minZ: the z-coordinate of the minimum corner
        - maxX: the x-coordinate of the maximum corner
        - maxY: the y-coordinate of the maximum corner
        - maxZ: the z-coordinate of the maximum corner

        Returns
        - `True` if the axis-aligned box is completely or partly inside of the frustum; `False` otherwise
        """
        ...


    def testPlaneXY(self, min: "Vector2fc", max: "Vector2fc") -> bool:
        """
        Test whether the given XY-plane (at `Z = 0`) is partly or completely within or outside of the frustum defined by `this` frustum culler.
        The plane is specified via its `min` and `max` corner coordinates.
        
        The algorithm implemented by this method is conservative. This means that in certain circumstances a *False positive*
        can occur, when the method returns `True` for planes that do not intersect the frustum.
        See <a href="http://iquilezles.org/www/articles/frustumcorrect/frustumcorrect.htm">iquilezles.org</a> for an examination of this problem.

        Arguments
        - min: the minimum corner coordinates of the XY-plane
        - max: the maximum corner coordinates of the XY-plane

        Returns
        - `True` if the XY-plane is completely or partly inside of the frustum; `False` otherwise
        """
        ...


    def testPlaneXY(self, minX: float, minY: float, maxX: float, maxY: float) -> bool:
        """
        Test whether the given XY-plane (at `Z = 0`) is partly or completely within or outside of the frustum defined by `this` frustum culler.
        The plane is specified via its min and max corner coordinates.
        
        The algorithm implemented by this method is conservative. This means that in certain circumstances a *False positive*
        can occur, when the method returns `True` for planes that do not intersect the frustum.
        See <a href="http://iquilezles.org/www/articles/frustumcorrect/frustumcorrect.htm">iquilezles.org</a> for an examination of this problem.
        
        Reference: <a href="http://old.cescg.org/CESCG-2002/DSykoraJJelinek/">Efficient View Frustum Culling</a>

        Arguments
        - minX: the x-coordinate of the minimum corner
        - minY: the y-coordinate of the minimum corner
        - maxX: the x-coordinate of the maximum corner
        - maxY: the y-coordinate of the maximum corner

        Returns
        - `True` if the XY-plane is completely or partly inside of the frustum; `False` otherwise
        """
        ...


    def testPlaneXZ(self, minX: float, minZ: float, maxX: float, maxZ: float) -> bool:
        """
        Test whether the given XZ-plane (at `Y = 0`) is partly or completely within or outside of the frustum defined by `this` frustum culler.
        The plane is specified via its min and max corner coordinates.
        
        The algorithm implemented by this method is conservative. This means that in certain circumstances a *False positive*
        can occur, when the method returns `True` for planes that do not intersect the frustum.
        See <a href="http://iquilezles.org/www/articles/frustumcorrect/frustumcorrect.htm">iquilezles.org</a> for an examination of this problem.
        
        Reference: <a href="http://old.cescg.org/CESCG-2002/DSykoraJJelinek/">Efficient View Frustum Culling</a>

        Arguments
        - minX: the x-coordinate of the minimum corner
        - minZ: the z-coordinate of the minimum corner
        - maxX: the x-coordinate of the maximum corner
        - maxZ: the z-coordinate of the maximum corner

        Returns
        - `True` if the XZ-plane is completely or partly inside of the frustum; `False` otherwise
        """
        ...


    def intersectAab(self, min: "Vector3fc", max: "Vector3fc") -> int:
        """
        Determine whether the given axis-aligned box is partly or completely within or outside of the frustum defined by `this` frustum culler
        and, if the box is not inside this frustum, return the index of the plane that culled it.
        The box is specified via its `min` and `max` corner coordinates.
        
        The algorithm implemented by this method is conservative. This means that in certain circumstances a *False positive*
        can occur, when the method returns .INTERSECT for boxes that do not intersect the frustum.
        See <a href="http://iquilezles.org/www/articles/frustumcorrect/frustumcorrect.htm">iquilezles.org</a> for an examination of this problem.

        Arguments
        - min: the minimum corner coordinates of the axis-aligned box
        - max: the maximum corner coordinates of the axis-aligned box

        Returns
        - the index of the first plane that culled the box, if the box does not intersect the frustum;
                or .INTERSECT if the box intersects the frustum, or .INSIDE if the box is fully inside of the frustum.
                The plane index is one of .PLANE_NX, .PLANE_PX, .PLANE_NY, .PLANE_PY, .PLANE_NZ and .PLANE_PZ
        """
        ...


    def intersectAab(self, minX: float, minY: float, minZ: float, maxX: float, maxY: float, maxZ: float) -> int:
        """
        Determine whether the given axis-aligned box is partly or completely within or outside of the frustum defined by `this` frustum culler
        and, if the box is not inside this frustum, return the index of the plane that culled it.
        The box is specified via its min and max corner coordinates.
        
        The algorithm implemented by this method is conservative. This means that in certain circumstances a *False positive*
        can occur, when the method returns .INTERSECT for boxes that do not intersect the frustum.
        See <a href="http://iquilezles.org/www/articles/frustumcorrect/frustumcorrect.htm">iquilezles.org</a> for an examination of this problem.
        
        Reference: <a href="http://old.cescg.org/CESCG-2002/DSykoraJJelinek/">Efficient View Frustum Culling</a>

        Arguments
        - minX: the x-coordinate of the minimum corner
        - minY: the y-coordinate of the minimum corner
        - minZ: the z-coordinate of the minimum corner
        - maxX: the x-coordinate of the maximum corner
        - maxY: the y-coordinate of the maximum corner
        - maxZ: the z-coordinate of the maximum corner

        Returns
        - the index of the first plane that culled the box, if the box does not intersect the frustum,
                or .INTERSECT if the box intersects the frustum, or .INSIDE if the box is fully inside of the frustum.
                The plane index is one of .PLANE_NX, .PLANE_PX, .PLANE_NY, .PLANE_PY, .PLANE_NZ and .PLANE_PZ
        """
        ...


    def distanceToPlane(self, minX: float, minY: float, minZ: float, maxX: float, maxY: float, maxZ: float, plane: int) -> float:
        """
        Compute the signed distance from the given axis-aligned box to the `plane`.

        Arguments
        - minX: the x-coordinate of the minimum corner
        - minY: the y-coordinate of the minimum corner
        - minZ: the z-coordinate of the minimum corner
        - maxX: the x-coordinate of the maximum corner
        - maxY: the y-coordinate of the maximum corner
        - maxZ: the z-coordinate of the maximum corner
        - plane: one of 
                 .PLANE_NX, .PLANE_PX,
                 .PLANE_NY, .PLANE_PY, 
                 .PLANE_NZ and .PLANE_PZ

        Returns
        - the signed distance of the axis-aligned box to the plane
        """
        ...


    def intersectAab(self, min: "Vector3fc", max: "Vector3fc", mask: int) -> int:
        """
        Determine whether the given axis-aligned box is partly or completely within or outside of the frustum defined by `this` frustum culler
        and, if the box is not inside this frustum, return the index of the plane that culled it.
        The box is specified via its `min` and `max` corner coordinates.
        
        This method differs from .intersectAab(Vector3fc, Vector3fc) in that
        it allows to mask-off planes that should not be calculated. For example, in order to only test a box against the
        left frustum plane, use a mask of .PLANE_MASK_NX. Or in order to test all planes *except* the left plane, use 
        a mask of `(~0 ^ PLANE_MASK_NX)`.
        
        The algorithm implemented by this method is conservative. This means that in certain circumstances a *False positive*
        can occur, when the method returns .INTERSECT for boxes that do not intersect the frustum.
        See <a href="http://iquilezles.org/www/articles/frustumcorrect/frustumcorrect.htm">iquilezles.org</a> for an examination of this problem.

        Arguments
        - min: the minimum corner coordinates of the axis-aligned box
        - max: the maximum corner coordinates of the axis-aligned box
        - mask: contains as bitset all the planes that should be tested.
                 This value can be any combination of 
                 .PLANE_MASK_NX, .PLANE_MASK_PX,
                 .PLANE_MASK_NY, .PLANE_MASK_PY, 
                 .PLANE_MASK_NZ and .PLANE_MASK_PZ

        Returns
        - the index of the first plane that culled the box, if the box does not intersect the frustum,
                or .INTERSECT if the box intersects the frustum, or .INSIDE if the box is fully inside of the frustum.
                The plane index is one of .PLANE_NX, .PLANE_PX, .PLANE_NY, .PLANE_PY, .PLANE_NZ and .PLANE_PZ
        """
        ...


    def intersectAab(self, minX: float, minY: float, minZ: float, maxX: float, maxY: float, maxZ: float, mask: int) -> int:
        """
        Determine whether the given axis-aligned box is partly or completely within or outside of the frustum defined by `this` frustum culler
        and, if the box is not inside this frustum, return the index of the plane that culled it.
        The box is specified via its min and max corner coordinates.
        
        This method differs from .intersectAab(float, float, float, float, float, float) in that
        it allows to mask-off planes that should not be calculated. For example, in order to only test a box against the
        left frustum plane, use a mask of .PLANE_MASK_NX. Or in order to test all planes *except* the left plane, use 
        a mask of `(~0 ^ PLANE_MASK_NX)`.
        
        The algorithm implemented by this method is conservative. This means that in certain circumstances a *False positive*
        can occur, when the method returns .INTERSECT for boxes that do not intersect the frustum.
        See <a href="http://iquilezles.org/www/articles/frustumcorrect/frustumcorrect.htm">iquilezles.org</a> for an examination of this problem.
        
        Reference: <a href="http://old.cescg.org/CESCG-2002/DSykoraJJelinek/">Efficient View Frustum Culling</a>

        Arguments
        - minX: the x-coordinate of the minimum corner
        - minY: the y-coordinate of the minimum corner
        - minZ: the z-coordinate of the minimum corner
        - maxX: the x-coordinate of the maximum corner
        - maxY: the y-coordinate of the maximum corner
        - maxZ: the z-coordinate of the maximum corner
        - mask: contains as bitset all the planes that should be tested.
                 This value can be any combination of 
                 .PLANE_MASK_NX, .PLANE_MASK_PX,
                 .PLANE_MASK_NY, .PLANE_MASK_PY, 
                 .PLANE_MASK_NZ and .PLANE_MASK_PZ

        Returns
        - the index of the first plane that culled the box, if the box does not intersect the frustum,
                or .INTERSECT if the box intersects the frustum, or .INSIDE if the box is fully inside of the frustum.
                The plane index is one of .PLANE_NX, .PLANE_PX, .PLANE_NY, .PLANE_PY, .PLANE_NZ and .PLANE_PZ
        """
        ...


    def intersectAab(self, min: "Vector3fc", max: "Vector3fc", mask: int, startPlane: int) -> int:
        """
        Determine whether the given axis-aligned box is partly or completely within or outside of the frustum defined by `this` frustum culler
        and, if the box is not inside this frustum, return the index of the plane that culled it.
        The box is specified via its `min` and `max` corner coordinates.
        
        This method differs from .intersectAab(Vector3fc, Vector3fc) in that
        it allows to mask-off planes that should not be calculated. For example, in order to only test a box against the
        left frustum plane, use a mask of .PLANE_MASK_NX. Or in order to test all planes *except* the left plane, use 
        a mask of `(~0 ^ PLANE_MASK_NX)`.
        
        In addition, the `startPlane` denotes the first frustum plane to test the box against. To use this effectively means to store the
        plane that previously culled an axis-aligned box (as returned by `intersectAab()`) and in the next frame use the return value
        as the argument to the `startPlane` parameter of this method. The assumption is that the plane that culled the object previously will also
        cull it now (temporal coherency) and the culling computation is likely reduced in that case.
        
        The algorithm implemented by this method is conservative. This means that in certain circumstances a *False positive*
        can occur, when the method returns .INTERSECT for boxes that do not intersect the frustum.
        See <a href="http://iquilezles.org/www/articles/frustumcorrect/frustumcorrect.htm">iquilezles.org</a> for an examination of this problem.

        Arguments
        - min: the minimum corner coordinates of the axis-aligned box
        - max: the maximum corner coordinates of the axis-aligned box
        - mask: contains as bitset all the planes that should be tested.
                 This value can be any combination of 
                 .PLANE_MASK_NX, .PLANE_MASK_PX,
                 .PLANE_MASK_NY, .PLANE_MASK_PY, 
                 .PLANE_MASK_NZ and .PLANE_MASK_PZ
        - startPlane: the first frustum plane to test the axis-aligned box against. It is one of
                 .PLANE_NX, .PLANE_PX, .PLANE_NY, .PLANE_PY, .PLANE_NZ and .PLANE_PZ

        Returns
        - the index of the first plane that culled the box, if the box does not intersect the frustum,
                or .INTERSECT if the box intersects the frustum, or .INSIDE if the box is fully inside of the frustum.
                The plane index is one of .PLANE_NX, .PLANE_PX, .PLANE_NY, .PLANE_PY, .PLANE_NZ and .PLANE_PZ
        """
        ...


    def intersectAab(self, minX: float, minY: float, minZ: float, maxX: float, maxY: float, maxZ: float, mask: int, startPlane: int) -> int:
        """
        Determine whether the given axis-aligned box is partly or completely within or outside of the frustum defined by `this` frustum culler
        and, if the box is not inside this frustum, return the index of the plane that culled it.
        The box is specified via its min and max corner coordinates.
        
        This method differs from .intersectAab(float, float, float, float, float, float) in that
        it allows to mask-off planes that should not be calculated. For example, in order to only test a box against the
        left frustum plane, use a mask of .PLANE_MASK_NX. Or in order to test all planes *except* the left plane, use 
        a mask of `(~0 ^ PLANE_MASK_NX)`.
        
        In addition, the `startPlane` denotes the first frustum plane to test the box against. To use this effectively means to store the
        plane that previously culled an axis-aligned box (as returned by `intersectAab()`) and in the next frame use the return value
        as the argument to the `startPlane` parameter of this method. The assumption is that the plane that culled the object previously will also
        cull it now (temporal coherency) and the culling computation is likely reduced in that case.
        
        The algorithm implemented by this method is conservative. This means that in certain circumstances a *False positive*
        can occur, when the method returns .INTERSECT for boxes that do not intersect the frustum.
        See <a href="http://iquilezles.org/www/articles/frustumcorrect/frustumcorrect.htm">iquilezles.org</a> for an examination of this problem.
        
        Reference: <a href="http://old.cescg.org/CESCG-2002/DSykoraJJelinek/">Efficient View Frustum Culling</a>

        Arguments
        - minX: the x-coordinate of the minimum corner
        - minY: the y-coordinate of the minimum corner
        - minZ: the z-coordinate of the minimum corner
        - maxX: the x-coordinate of the maximum corner
        - maxY: the y-coordinate of the maximum corner
        - maxZ: the z-coordinate of the maximum corner
        - mask: contains as bitset all the planes that should be tested.
                 This value can be any combination of 
                 .PLANE_MASK_NX, .PLANE_MASK_PX,
                 .PLANE_MASK_NY, .PLANE_MASK_PY, 
                 .PLANE_MASK_NZ and .PLANE_MASK_PZ
        - startPlane: the first frustum plane to test the axis-aligned box against. It is one of
                 .PLANE_NX, .PLANE_PX, .PLANE_NY, .PLANE_PY, .PLANE_NZ and .PLANE_PZ

        Returns
        - the index of the first plane that culled the box, if the box does not intersect the frustum,
                or .INTERSECT if the box intersects the frustum, or .INSIDE if the box is fully inside of the frustum.
                The plane index is one of .PLANE_NX, .PLANE_PX, .PLANE_NY, .PLANE_PY, .PLANE_NZ and .PLANE_PZ
        """
        ...


    def testLineSegment(self, a: "Vector3fc", b: "Vector3fc") -> bool:
        """
        Test whether the given line segment, defined by the end points `a` and `b`, 
        is partly or completely within the frustum defined by `this` frustum culler.

        Arguments
        - a: the line segment's first end point
        - b: the line segment's second end point

        Returns
        - `True` if the given line segment is partly or completely inside the frustum;
                `False` otherwise
        """
        ...


    def testLineSegment(self, aX: float, aY: float, aZ: float, bX: float, bY: float, bZ: float) -> bool:
        """
        Test whether the given line segment, defined by the end points `(aX, aY, aZ)` and `(bX, bY, bZ)`, 
        is partly or completely within the frustum defined by `this` frustum culler.

        Arguments
        - aX: the x coordinate of the line segment's first end point
        - aY: the y coordinate of the line segment's first end point
        - aZ: the z coordinate of the line segment's first end point
        - bX: the x coordinate of the line segment's second end point
        - bY: the y coordinate of the line segment's second end point
        - bZ: the z coordinate of the line segment's second end point

        Returns
        - `True` if the given line segment is partly or completely inside the frustum;
                `False` otherwise
        """
        ...
