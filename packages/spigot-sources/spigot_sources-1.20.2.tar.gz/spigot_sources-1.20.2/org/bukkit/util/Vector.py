"""
Python module generated from Java source file org.bukkit.util.Vector

Java source file obtained from artifact spigot-api version 1.20.2-R0.1-20231205.164257-71

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.base import Preconditions
from com.google.common.primitives import Doubles
from java.util import Random
from org.bukkit import Location
from org.bukkit import World
from org.bukkit.configuration.serialization import ConfigurationSerializable
from org.bukkit.configuration.serialization import SerializableAs
from org.bukkit.util import *
from org.joml import RoundingMode
from org.joml import Vector3d
from org.joml import Vector3f
from org.joml import Vector3i
from typing import Any, Callable, Iterable, Tuple


class Vector(Cloneable, ConfigurationSerializable):
    """
    Represents a mutable vector. Because the components of Vectors are mutable,
    storing Vectors long term may be dangerous if passing code modifies the
    Vector later. If you want to keep around a Vector, it may be wise to call
    `clone()` in order to get a copy.
    """

    def __init__(self):
        """
        Construct the vector with all components as 0.
        """
        ...


    def __init__(self, x: int, y: int, z: int):
        """
        Construct the vector with provided integer components.

        Arguments
        - x: X component
        - y: Y component
        - z: Z component
        """
        ...


    def __init__(self, x: float, y: float, z: float):
        """
        Construct the vector with provided double components.

        Arguments
        - x: X component
        - y: Y component
        - z: Z component
        """
        ...


    def __init__(self, x: float, y: float, z: float):
        """
        Construct the vector with provided float components.

        Arguments
        - x: X component
        - y: Y component
        - z: Z component
        """
        ...


    def add(self, vec: "Vector") -> "Vector":
        """
        Adds a vector to this one

        Arguments
        - vec: The other vector

        Returns
        - the same vector
        """
        ...


    def subtract(self, vec: "Vector") -> "Vector":
        """
        Subtracts a vector from this one.

        Arguments
        - vec: The other vector

        Returns
        - the same vector
        """
        ...


    def multiply(self, vec: "Vector") -> "Vector":
        """
        Multiplies the vector by another.

        Arguments
        - vec: The other vector

        Returns
        - the same vector
        """
        ...


    def divide(self, vec: "Vector") -> "Vector":
        """
        Divides the vector by another.

        Arguments
        - vec: The other vector

        Returns
        - the same vector
        """
        ...


    def copy(self, vec: "Vector") -> "Vector":
        """
        Copies another vector

        Arguments
        - vec: The other vector

        Returns
        - the same vector
        """
        ...


    def length(self) -> float:
        """
        Gets the magnitude of the vector, defined as sqrt(x^2+y^2+z^2). The
        value of this method is not cached and uses a costly square-root
        function, so do not repeatedly call this method to get the vector's
        magnitude. NaN will be returned if the inner result of the sqrt()
        function overflows, which will be caused if the length is too long.

        Returns
        - the magnitude
        """
        ...


    def lengthSquared(self) -> float:
        """
        Gets the magnitude of the vector squared.

        Returns
        - the magnitude
        """
        ...


    def distance(self, o: "Vector") -> float:
        """
        Get the distance between this vector and another. The value of this
        method is not cached and uses a costly square-root function, so do not
        repeatedly call this method to get the vector's magnitude. NaN will be
        returned if the inner result of the sqrt() function overflows, which
        will be caused if the distance is too long.

        Arguments
        - o: The other vector

        Returns
        - the distance
        """
        ...


    def distanceSquared(self, o: "Vector") -> float:
        """
        Get the squared distance between this vector and another.

        Arguments
        - o: The other vector

        Returns
        - the distance
        """
        ...


    def angle(self, other: "Vector") -> float:
        """
        Gets the angle between this vector and another in radians.

        Arguments
        - other: The other vector

        Returns
        - angle in radians
        """
        ...


    def midpoint(self, other: "Vector") -> "Vector":
        """
        Sets this vector to the midpoint between this vector and another.

        Arguments
        - other: The other vector

        Returns
        - this same vector (now a midpoint)
        """
        ...


    def getMidpoint(self, other: "Vector") -> "Vector":
        """
        Gets a new midpoint vector between this vector and another.

        Arguments
        - other: The other vector

        Returns
        - a new midpoint vector
        """
        ...


    def multiply(self, m: int) -> "Vector":
        """
        Performs scalar multiplication, multiplying all components with a
        scalar.

        Arguments
        - m: The factor

        Returns
        - the same vector
        """
        ...


    def multiply(self, m: float) -> "Vector":
        """
        Performs scalar multiplication, multiplying all components with a
        scalar.

        Arguments
        - m: The factor

        Returns
        - the same vector
        """
        ...


    def multiply(self, m: float) -> "Vector":
        """
        Performs scalar multiplication, multiplying all components with a
        scalar.

        Arguments
        - m: The factor

        Returns
        - the same vector
        """
        ...


    def dot(self, other: "Vector") -> float:
        """
        Calculates the dot product of this vector with another. The dot product
        is defined as x1*x2+y1*y2+z1*z2. The returned value is a scalar.

        Arguments
        - other: The other vector

        Returns
        - dot product
        """
        ...


    def crossProduct(self, o: "Vector") -> "Vector":
        """
        Calculates the cross product of this vector with another. The cross
        product is defined as:
        
        - x = y1 * z2 - y2 * z1
        - y = z1 * x2 - z2 * x1
        - z = x1 * y2 - x2 * y1

        Arguments
        - o: The other vector

        Returns
        - the same vector
        """
        ...


    def getCrossProduct(self, o: "Vector") -> "Vector":
        """
        Calculates the cross product of this vector with another without mutating
        the original. The cross product is defined as:
        
        - x = y1 * z2 - y2 * z1
        - y = z1 * x2 - z2 * x1
        - z = x1 * y2 - x2 * y1

        Arguments
        - o: The other vector

        Returns
        - a new vector
        """
        ...


    def normalize(self) -> "Vector":
        """
        Converts this vector to a unit vector (a vector with length of 1).

        Returns
        - the same vector
        """
        ...


    def zero(self) -> "Vector":
        """
        Zero this vector's components.

        Returns
        - the same vector
        """
        ...


    def isZero(self) -> bool:
        """
        Check whether or not each component of this vector is equal to 0.

        Returns
        - True if equal to zero, False if at least one component is non-zero
        """
        ...


    def isInAABB(self, min: "Vector", max: "Vector") -> bool:
        """
        Returns whether this vector is in an axis-aligned bounding box.
        
        The minimum and maximum vectors given must be truly the minimum and
        maximum X, Y and Z components.

        Arguments
        - min: Minimum vector
        - max: Maximum vector

        Returns
        - whether this vector is in the AABB
        """
        ...


    def isInSphere(self, origin: "Vector", radius: float) -> bool:
        """
        Returns whether this vector is within a sphere.

        Arguments
        - origin: Sphere origin.
        - radius: Sphere radius

        Returns
        - whether this vector is in the sphere
        """
        ...


    def isNormalized(self) -> bool:
        """
        Returns if a vector is normalized

        Returns
        - whether the vector is normalised
        """
        ...


    def rotateAroundX(self, angle: float) -> "Vector":
        """
        Rotates the vector around the x axis.
        
        This piece of math is based on the standard rotation matrix for vectors
        in three dimensional space. This matrix can be found here:
        <a href="https://en.wikipedia.org/wiki/Rotation_matrix#Basic_rotations">Rotation
        Matrix</a>.

        Arguments
        - angle: the angle to rotate the vector about. This angle is passed
        in radians

        Returns
        - the same vector
        """
        ...


    def rotateAroundY(self, angle: float) -> "Vector":
        """
        Rotates the vector around the y axis.
        
        This piece of math is based on the standard rotation matrix for vectors
        in three dimensional space. This matrix can be found here:
        <a href="https://en.wikipedia.org/wiki/Rotation_matrix#Basic_rotations">Rotation
        Matrix</a>.

        Arguments
        - angle: the angle to rotate the vector about. This angle is passed
        in radians

        Returns
        - the same vector
        """
        ...


    def rotateAroundZ(self, angle: float) -> "Vector":
        """
        Rotates the vector around the z axis
        
        This piece of math is based on the standard rotation matrix for vectors
        in three dimensional space. This matrix can be found here:
        <a href="https://en.wikipedia.org/wiki/Rotation_matrix#Basic_rotations">Rotation
        Matrix</a>.

        Arguments
        - angle: the angle to rotate the vector about. This angle is passed
        in radians

        Returns
        - the same vector
        """
        ...


    def rotateAroundAxis(self, axis: "Vector", angle: float) -> "Vector":
        """
        Rotates the vector around a given arbitrary axis in 3 dimensional space.
        
        
        Rotation will follow the general Right-Hand-Rule, which means rotation
        will be counterclockwise when the axis is pointing towards the observer.
        
        This method will always make sure the provided axis is a unit vector, to
        not modify the length of the vector when rotating. If you are experienced
        with the scaling of a non-unit axis vector, you can use
        Vector.rotateAroundNonUnitAxis(Vector, double).

        Arguments
        - axis: the axis to rotate the vector around. If the passed vector is
        not of length 1, it gets copied and normalized before using it for the
        rotation. Please use Vector.normalize() on the instance before
        passing it to this method
        - angle: the angle to rotate the vector around the axis

        Returns
        - the same vector

        Raises
        - IllegalArgumentException: if the provided axis vector instance is
        null
        """
        ...


    def rotateAroundNonUnitAxis(self, axis: "Vector", angle: float) -> "Vector":
        """
        Rotates the vector around a given arbitrary axis in 3 dimensional space.
        
        
        Rotation will follow the general Right-Hand-Rule, which means rotation
        will be counterclockwise when the axis is pointing towards the observer.
        
        Note that the vector length will change accordingly to the axis vector
        length. If the provided axis is not a unit vector, the rotated vector
        will not have its previous length. The scaled length of the resulting
        vector will be related to the axis vector. If you are not perfectly sure
        about the scaling of the vector, use
        Vector.rotateAroundAxis(Vector, double)

        Arguments
        - axis: the axis to rotate the vector around.
        - angle: the angle to rotate the vector around the axis

        Returns
        - the same vector

        Raises
        - IllegalArgumentException: if the provided axis vector instance is
        null
        """
        ...


    def getX(self) -> float:
        """
        Gets the X component.

        Returns
        - The X component.
        """
        ...


    def getBlockX(self) -> int:
        """
        Gets the floored value of the X component, indicating the block that
        this vector is contained with.

        Returns
        - block X
        """
        ...


    def getY(self) -> float:
        """
        Gets the Y component.

        Returns
        - The Y component.
        """
        ...


    def getBlockY(self) -> int:
        """
        Gets the floored value of the Y component, indicating the block that
        this vector is contained with.

        Returns
        - block y
        """
        ...


    def getZ(self) -> float:
        """
        Gets the Z component.

        Returns
        - The Z component.
        """
        ...


    def getBlockZ(self) -> int:
        """
        Gets the floored value of the Z component, indicating the block that
        this vector is contained with.

        Returns
        - block z
        """
        ...


    def setX(self, x: int) -> "Vector":
        """
        Set the X component.

        Arguments
        - x: The new X component.

        Returns
        - This vector.
        """
        ...


    def setX(self, x: float) -> "Vector":
        """
        Set the X component.

        Arguments
        - x: The new X component.

        Returns
        - This vector.
        """
        ...


    def setX(self, x: float) -> "Vector":
        """
        Set the X component.

        Arguments
        - x: The new X component.

        Returns
        - This vector.
        """
        ...


    def setY(self, y: int) -> "Vector":
        """
        Set the Y component.

        Arguments
        - y: The new Y component.

        Returns
        - This vector.
        """
        ...


    def setY(self, y: float) -> "Vector":
        """
        Set the Y component.

        Arguments
        - y: The new Y component.

        Returns
        - This vector.
        """
        ...


    def setY(self, y: float) -> "Vector":
        """
        Set the Y component.

        Arguments
        - y: The new Y component.

        Returns
        - This vector.
        """
        ...


    def setZ(self, z: int) -> "Vector":
        """
        Set the Z component.

        Arguments
        - z: The new Z component.

        Returns
        - This vector.
        """
        ...


    def setZ(self, z: float) -> "Vector":
        """
        Set the Z component.

        Arguments
        - z: The new Z component.

        Returns
        - This vector.
        """
        ...


    def setZ(self, z: float) -> "Vector":
        """
        Set the Z component.

        Arguments
        - z: The new Z component.

        Returns
        - This vector.
        """
        ...


    def equals(self, obj: "Object") -> bool:
        """
        Checks to see if two objects are equal.
        
        Only two Vectors can ever return True. This method uses a fuzzy match
        to account for floating point errors. The epsilon can be retrieved
        with epsilon.
        """
        ...


    def hashCode(self) -> int:
        """
        Returns a hash code for this vector

        Returns
        - hash code
        """
        ...


    def clone(self) -> "Vector":
        """
        Get a new vector.

        Returns
        - vector
        """
        ...


    def toString(self) -> str:
        """
        Returns this vector's components as x,y,z.
        """
        ...


    def toLocation(self, world: "World") -> "Location":
        """
        Gets a Location version of this vector with yaw and pitch being 0.

        Arguments
        - world: The world to link the location to.

        Returns
        - the location
        """
        ...


    def toLocation(self, world: "World", yaw: float, pitch: float) -> "Location":
        """
        Gets a Location version of this vector.

        Arguments
        - world: The world to link the location to.
        - yaw: The desired yaw.
        - pitch: The desired pitch.

        Returns
        - the location
        """
        ...


    def toBlockVector(self) -> "BlockVector":
        """
        Get the block vector of this vector.

        Returns
        - A block vector.
        """
        ...


    def toVector3f(self) -> "Vector3f":
        """
        Get this vector as a JOML Vector3f.

        Returns
        - the JOML vector
        """
        ...


    def toVector3d(self) -> "Vector3d":
        """
        Get this vector as a JOML Vector3d.

        Returns
        - the JOML vector
        """
        ...


    def toVector3i(self, roundingMode: int) -> "Vector3i":
        """
        Get this vector as a JOML Vector3i.

        Arguments
        - roundingMode: the RoundingMode to use for this vector's components

        Returns
        - the JOML vector
        """
        ...


    def toVector3i(self) -> "Vector3i":
        """
        Get this vector as a JOML Vector3i with its components floored.

        Returns
        - the JOML vector

        See
        - .toVector3i(int)
        """
        ...


    def checkFinite(self) -> None:
        """
        Check if each component of this Vector is finite.

        Raises
        - IllegalArgumentException: if any component is not finite
        """
        ...


    @staticmethod
    def getEpsilon() -> float:
        """
        Get the threshold used for equals().

        Returns
        - The epsilon.
        """
        ...


    @staticmethod
    def getMinimum(v1: "Vector", v2: "Vector") -> "Vector":
        """
        Gets the minimum components of two vectors.

        Arguments
        - v1: The first vector.
        - v2: The second vector.

        Returns
        - minimum
        """
        ...


    @staticmethod
    def getMaximum(v1: "Vector", v2: "Vector") -> "Vector":
        """
        Gets the maximum components of two vectors.

        Arguments
        - v1: The first vector.
        - v2: The second vector.

        Returns
        - maximum
        """
        ...


    @staticmethod
    def getRandom() -> "Vector":
        """
        Gets a random vector with components having a random value between 0
        and 1.

        Returns
        - A random vector.
        """
        ...


    @staticmethod
    def fromJOML(vector: "Vector3f") -> "Vector":
        """
        Gets a vector with components that match the provided JOML Vector3f.

        Arguments
        - vector: the vector to match

        Returns
        - the new vector
        """
        ...


    @staticmethod
    def fromJOML(vector: "Vector3d") -> "Vector":
        """
        Gets a vector with components that match the provided JOML Vector3d.

        Arguments
        - vector: the vector to match

        Returns
        - the new vector
        """
        ...


    @staticmethod
    def fromJOML(vector: "Vector3i") -> "Vector":
        """
        Gets a vector with components that match the provided JOML Vector3i.

        Arguments
        - vector: the vector to match

        Returns
        - the new vector
        """
        ...


    def serialize(self) -> dict[str, "Object"]:
        ...


    @staticmethod
    def deserialize(args: dict[str, "Object"]) -> "Vector":
        ...
