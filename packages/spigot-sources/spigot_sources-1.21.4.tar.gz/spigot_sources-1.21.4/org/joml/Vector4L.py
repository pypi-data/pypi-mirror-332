"""
Python module generated from Java source file org.joml.Vector4L

Java source file obtained from artifact joml version 1.10.8

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.io import Externalizable
from java.io import IOException
from java.io import ObjectInput
from java.io import ObjectOutput
from java.text import DecimalFormat
from java.text import NumberFormat
from org.joml import *
from typing import Any, Callable, Iterable, Tuple


class Vector4L(Externalizable, Cloneable, Vector4Lc):
    """
    Contains the definition of a vector comprising 4 longs and associated
    transformations.

    Author(s)
    - Kai Burjack
    """

    def __init__(self):
        """
        Create a new Vector4L of `(0, 0, 0, 1)`.
        """
        ...


    def __init__(self, v: "Vector4Lc"):
        """
        Create a new Vector4L with the same values as `v`.

        Arguments
        - v: the Vector4Lc to copy the values from
        """
        ...


    def __init__(self, v: "Vector4ic"):
        """
        Create a new Vector4L with the same values as `v`.

        Arguments
        - v: the Vector4ic to copy the values from
        """
        ...


    def __init__(self, v: "Vector3Lc", w: int):
        """
        Create a new Vector4L with the first three components from the
        given `v` and the given `w`.

        Arguments
        - v: the Vector3Lc
        - w: the w component
        """
        ...


    def __init__(self, v: "Vector3ic", w: int):
        """
        Create a new Vector4L with the first three components from the
        given `v` and the given `w`.

        Arguments
        - v: the Vector3ic
        - w: the w component
        """
        ...


    def __init__(self, v: "Vector2Lc", z: int, w: int):
        """
        Create a new Vector4L with the first two components from the
        given `v` and the given `z`, and `w`.

        Arguments
        - v: the Vector2ic
        - z: the z component
        - w: the w component
        """
        ...


    def __init__(self, v: "Vector2ic", z: int, w: int):
        """
        Create a new Vector4L with the first two components from the
        given `v` and the given `z`, and `w`.

        Arguments
        - v: the Vector2ic
        - z: the z component
        - w: the w component
        """
        ...


    def __init__(self, v: "Vector3fc", w: float, mode: int):
        """
        Create a new Vector4L with the first three components from the
        given `v` and the given `w` and round using the given RoundingMode.

        Arguments
        - v: the Vector3fc to copy the values from
        - w: the w component
        - mode: the RoundingMode to use
        """
        ...


    def __init__(self, v: "Vector4fc", mode: int):
        """
        Create a new Vector4L and initialize its components to the rounded value of
        the given vector.

        Arguments
        - v: the Vector4fc to round and copy the values from
        - mode: the RoundingMode to use
        """
        ...


    def __init__(self, v: "Vector4dc", mode: int):
        """
        Create a new Vector4L and initialize its components to the rounded value of
        the given vector.

        Arguments
        - v: the Vector4dc to round and copy the values from
        - mode: the RoundingMode to use
        """
        ...


    def __init__(self, s: int):
        """
        Create a new Vector4L and initialize all four components with the
        given value.

        Arguments
        - s: scalar value of all four components
        """
        ...


    def __init__(self, x: int, y: int, z: int, w: int):
        """
        Create a new Vector4L with the given component values.

        Arguments
        - x: the x component
        - y: the y component
        - z: the z component
        - w: the w component
        """
        ...


    def __init__(self, xyzw: list[int]):
        """
        Create a new Vector4L and initialize its four components from the first
        four elements of the given array.

        Arguments
        - xyzw: the array containing at least four elements
        """
        ...


    def __init__(self, buffer: "ByteBuffer"):
        """
        Create a new Vector4L and read this vector from the supplied
        ByteBuffer at the current buffer
        ByteBuffer.position() position.
        
        This method will not increment the position of the given ByteBuffer.
        
        In order to specify the offset into the ByteBuffer at which the vector is
        read, use .Vector4L(int, ByteBuffer), taking the absolute
        position as parameter.

        Arguments
        - buffer: values will be read in `x, y, z, w` order

        See
        - .Vector4L(int, ByteBuffer)
        """
        ...


    def __init__(self, index: int, buffer: "ByteBuffer"):
        """
        Create a new Vector4L and read this vector from the supplied
        ByteBuffer starting at the specified absolute buffer
        position/index.
        
        This method will not increment the position of the given ByteBuffer.

        Arguments
        - index: the absolute position into the ByteBuffer
        - buffer: values will be read in `x, y, z, w` order
        """
        ...


    def __init__(self, buffer: "LongBuffer"):
        """
        Create a new Vector4L and read this vector from the supplied
        LongBuffer at the current buffer
        LongBuffer.position() position.
        
        This method will not increment the position of the given LongBuffer.
        
        In order to specify the offset into the LongBuffer at which the vector is
        read, use .Vector4L(int, LongBuffer), taking the absolute position
        as parameter.

        Arguments
        - buffer: values will be read in `x, y, z, w` order

        See
        - .Vector4L(int, LongBuffer)
        """
        ...


    def __init__(self, index: int, buffer: "LongBuffer"):
        """
        Create a new Vector4L and read this vector from the supplied
        LongBuffer starting at the specified absolute buffer
        position/index.
        
        This method will not increment the position of the given LongBuffer.

        Arguments
        - index: the absolute position into the LongBuffer
        - buffer: values will be read in `x, y, z, w` order
        """
        ...


    def x(self) -> int:
        ...


    def y(self) -> int:
        ...


    def z(self) -> int:
        ...


    def w(self) -> int:
        ...


    def xyz(self, dest: "Vector3f") -> "Vector3f":
        """
        Copy the `(x, y, z)` components of `this` into the supplied `dest` vector
        and return it.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def xyz(self, dest: "Vector3d") -> "Vector3d":
        """
        Copy the `(x, y, z)` components of `this` into the supplied `dest` vector
        and return it.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def xyz(self, dest: "Vector3L") -> "Vector3L":
        """
        Copy the `(x, y, z)` components of `this` into the supplied `dest` vector
        and return it.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def xy(self, dest: "Vector2f") -> "Vector2f":
        """
        Copy the `(x, y)` components of `this` into the supplied `dest` vector
        and return it.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def xy(self, dest: "Vector2d") -> "Vector2d":
        """
        Copy the `(x, y)` components of `this` into the supplied `dest` vector
        and return it.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def xy(self, dest: "Vector2L") -> "Vector2L":
        """
        Copy the `(x, y)` components of `this` into the supplied `dest` vector
        and return it.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def set(self, v: "Vector4Lc") -> "Vector4L":
        """
        Set this vector to the values of the given `v`.

        Arguments
        - v: the vector whose values will be copied into this

        Returns
        - this
        """
        ...


    def set(self, v: "Vector4ic") -> "Vector4L":
        """
        Set this vector to the values of the given `v`.

        Arguments
        - v: the vector whose values will be copied into this

        Returns
        - this
        """
        ...


    def set(self, v: "Vector4dc") -> "Vector4L":
        """
        Set this vector to the values of v using RoundingMode.TRUNCATE rounding.
        
        Note that due to the given vector `v` storing the components
        in double-precision, there is the possibility to lose precision.

        Arguments
        - v: the vector to copy from

        Returns
        - this
        """
        ...


    def set(self, v: "Vector4dc", mode: int) -> "Vector4L":
        """
        Set this vector to the values of v using the given RoundingMode.
        
        Note that due to the given vector `v` storing the components
        in double-precision, there is the possibility to lose precision.

        Arguments
        - v: the vector to copy from
        - mode: the RoundingMode to use

        Returns
        - this
        """
        ...


    def set(self, v: "Vector4fc", mode: int) -> "Vector4L":
        """
        Set this vector to the values of v using the given RoundingMode.
        
        Note that due to the given vector `v` storing the components
        in double-precision, there is the possibility to lose precision.

        Arguments
        - v: the vector to copy from
        - mode: the RoundingMode to use

        Returns
        - this
        """
        ...


    def set(self, v: "Vector3ic", w: int) -> "Vector4L":
        """
        Set the first three components of this to the components of
        `v` and the last component to `w`.

        Arguments
        - v: the Vector3ic to copy
        - w: the w component

        Returns
        - this
        """
        ...


    def set(self, v: "Vector2ic", z: int, w: int) -> "Vector4L":
        """
        Sets the first two components of this to the components of given
        `v` and last two components to the given `z`, and
        `w`.

        Arguments
        - v: the Vector2ic
        - z: the z component
        - w: the w component

        Returns
        - this
        """
        ...


    def set(self, s: int) -> "Vector4L":
        """
        Set the x, y, z, and w components to the supplied value.

        Arguments
        - s: the value of all four components

        Returns
        - this
        """
        ...


    def set(self, x: int, y: int, z: int, w: int) -> "Vector4L":
        """
        Set the x, y, z, and w components to the supplied values.

        Arguments
        - x: the x component
        - y: the y component
        - z: the z component
        - w: the w component

        Returns
        - this
        """
        ...


    def set(self, xyzw: list[int]) -> "Vector4L":
        """
        Set the four components of this vector to the first four elements of the given array.

        Arguments
        - xyzw: the array containing at least four elements

        Returns
        - this
        """
        ...


    def set(self, buffer: "ByteBuffer") -> "Vector4L":
        """
        Read this vector from the supplied ByteBuffer at the current
        buffer ByteBuffer.position() position.
        
        This method will not increment the position of the given ByteBuffer.
        
        In order to specify the offset into the ByteBuffer at which the vector is
        read, use .set(int, ByteBuffer), taking the absolute position as
        parameter.

        Arguments
        - buffer: values will be read in `x, y, z, w` order

        Returns
        - this

        See
        - .set(int, ByteBuffer)
        """
        ...


    def set(self, index: int, buffer: "ByteBuffer") -> "Vector4L":
        """
        Read this vector from the supplied ByteBuffer starting at the
        specified absolute buffer position/index.
        
        This method will not increment the position of the given ByteBuffer.

        Arguments
        - index: the absolute position into the ByteBuffer
        - buffer: values will be read in `x, y, z, w` order

        Returns
        - this
        """
        ...


    def set(self, buffer: "LongBuffer") -> "Vector4L":
        """
        Read this vector from the supplied LongBuffer at the current
        buffer LongBuffer.position() position.
        
        This method will not increment the position of the given LongBuffer.
        
        In order to specify the offset into the LongBuffer at which the vector is
        read, use .set(int, LongBuffer), taking the absolute position as
        parameter.

        Arguments
        - buffer: values will be read in `x, y, z, w` order

        Returns
        - this

        See
        - .set(int, LongBuffer)
        """
        ...


    def set(self, index: int, buffer: "LongBuffer") -> "Vector4L":
        """
        Read this vector from the supplied LongBuffer starting at the
        specified absolute buffer position/index.
        
        This method will not increment the position of the given LongBuffer.

        Arguments
        - index: the absolute position into the LongBuffer
        - buffer: values will be read in `x, y, z, w` order

        Returns
        - this
        """
        ...


    def setFromAddress(self, address: int) -> "Vector4L":
        """
        Set the values of this vector by reading 4 integer values from off-heap memory,
        starting at the given address.
        
        This method will throw an UnsupportedOperationException when JOML is used with `-Djoml.nounsafe`.
        
        *This method is unsafe as it can result in a crash of the JVM process when the specified address range does not belong to this process.*

        Arguments
        - address: the off-heap memory address to read the vector values from

        Returns
        - this
        """
        ...


    def get(self, component: int) -> int:
        ...


    def maxComponent(self) -> int:
        ...


    def minComponent(self) -> int:
        ...


    def setComponent(self, component: int, value: int) -> "Vector4L":
        """
        Set the value of the specified component of this vector.

        Arguments
        - component: the component whose value to set, within `[0..3]`
        - value: the value to set

        Returns
        - this

        Raises
        - IllegalArgumentException: if `component` is not within `[0..3]`
        """
        ...


    def get(self, buffer: "LongBuffer") -> "LongBuffer":
        ...


    def get(self, index: int, buffer: "LongBuffer") -> "LongBuffer":
        ...


    def get(self, buffer: "ByteBuffer") -> "ByteBuffer":
        ...


    def get(self, index: int, buffer: "ByteBuffer") -> "ByteBuffer":
        ...


    def getToAddress(self, address: int) -> "Vector4Lc":
        ...


    def sub(self, v: "Vector4Lc") -> "Vector4L":
        """
        Subtract the supplied vector from this one.

        Arguments
        - v: the vector to subtract

        Returns
        - this
        """
        ...


    def sub(self, v: "Vector4Lc", dest: "Vector4L") -> "Vector4L":
        ...


    def sub(self, v: "Vector4ic") -> "Vector4L":
        """
        Subtract the supplied vector from this one.

        Arguments
        - v: the vector to subtract

        Returns
        - this
        """
        ...


    def sub(self, v: "Vector4ic", dest: "Vector4L") -> "Vector4L":
        ...


    def sub(self, x: int, y: int, z: int, w: int) -> "Vector4L":
        """
        Subtract `(x, y, z, w)` from this.

        Arguments
        - x: the x component to subtract
        - y: the y component to subtract
        - z: the z component to subtract
        - w: the w component to subtract

        Returns
        - this
        """
        ...


    def sub(self, x: int, y: int, z: int, w: int, dest: "Vector4L") -> "Vector4L":
        ...


    def add(self, v: "Vector4Lc") -> "Vector4L":
        """
        Add the supplied vector to this one.

        Arguments
        - v: the vector to add

        Returns
        - this
        """
        ...


    def add(self, v: "Vector4Lc", dest: "Vector4L") -> "Vector4L":
        ...


    def add(self, v: "Vector4ic") -> "Vector4L":
        """
        Add the supplied vector to this one.

        Arguments
        - v: the vector to add

        Returns
        - this
        """
        ...


    def add(self, v: "Vector4ic", dest: "Vector4L") -> "Vector4L":
        ...


    def add(self, x: int, y: int, z: int, w: int) -> "Vector4L":
        """
        Increment the components of this vector by the given values.

        Arguments
        - x: the x component to add
        - y: the y component to add
        - z: the z component to add
        - w: the w component to add

        Returns
        - this
        """
        ...


    def add(self, x: int, y: int, z: int, w: int, dest: "Vector4L") -> "Vector4L":
        ...


    def mul(self, v: "Vector4Lc") -> "Vector4L":
        """
        Multiply this Vector4L component-wise by another vector.

        Arguments
        - v: the other vector

        Returns
        - this
        """
        ...


    def mul(self, v: "Vector4Lc", dest: "Vector4L") -> "Vector4L":
        ...


    def mul(self, v: "Vector4ic") -> "Vector4L":
        """
        Multiply this Vector4L component-wise by another vector.

        Arguments
        - v: the other vector

        Returns
        - this
        """
        ...


    def mul(self, v: "Vector4ic", dest: "Vector4L") -> "Vector4L":
        ...


    def div(self, v: "Vector4Lc") -> "Vector4L":
        """
        Divide this Vector4L component-wise by another vector.

        Arguments
        - v: the vector to divide by

        Returns
        - this
        """
        ...


    def div(self, v: "Vector4Lc", dest: "Vector4L") -> "Vector4L":
        ...


    def div(self, v: "Vector4ic") -> "Vector4L":
        """
        Divide this Vector4L component-wise by another vector.

        Arguments
        - v: the vector to divide by

        Returns
        - this
        """
        ...


    def div(self, v: "Vector4ic", dest: "Vector4L") -> "Vector4L":
        ...


    def mul(self, scalar: int) -> "Vector4L":
        """
        Multiply all components of this vector by the given scalar
        value.

        Arguments
        - scalar: the scalar to multiply by

        Returns
        - this
        """
        ...


    def mul(self, scalar: int, dest: "Vector4L") -> "Vector4L":
        ...


    def div(self, scalar: float) -> "Vector4L":
        """
        Divide all components of this vector by the given scalar value.

        Arguments
        - scalar: the scalar to divide by

        Returns
        - this
        """
        ...


    def div(self, scalar: float, dest: "Vector4L") -> "Vector4L":
        ...


    def div(self, scalar: int) -> "Vector4L":
        """
        Divide all components of this vector by the given scalar value.

        Arguments
        - scalar: the scalar to divide by

        Returns
        - this
        """
        ...


    def div(self, scalar: int, dest: "Vector4L") -> "Vector4L":
        ...


    def lengthSquared(self) -> int:
        ...


    @staticmethod
    def lengthSquared(x: int, y: int, z: int, w: int) -> int:
        """
        Get the length squared of a 4-dimensional single-precision vector.

        Arguments
        - x: The vector's x component
        - y: The vector's y component
        - z: The vector's z component
        - w: The vector's w component

        Returns
        - the length squared of the given vector
        """
        ...


    def length(self) -> float:
        ...


    @staticmethod
    def length(x: int, y: int, z: int, w: int) -> float:
        """
        Get the length of a 4-dimensional single-precision vector.

        Arguments
        - x: The vector's x component
        - y: The vector's y component
        - z: The vector's z component
        - w: The vector's w component

        Returns
        - the length squared of the given vector
        """
        ...


    def distance(self, v: "Vector4Lc") -> float:
        ...


    def distance(self, v: "Vector4ic") -> float:
        ...


    def distance(self, x: int, y: int, z: int, w: int) -> float:
        ...


    def gridDistance(self, v: "Vector4Lc") -> int:
        ...


    def gridDistance(self, v: "Vector4ic") -> int:
        ...


    def gridDistance(self, x: int, y: int, z: int, w: int) -> int:
        ...


    def distanceSquared(self, v: "Vector4Lc") -> int:
        ...


    def distanceSquared(self, v: "Vector4ic") -> int:
        ...


    def distanceSquared(self, x: int, y: int, z: int, w: int) -> int:
        ...


    @staticmethod
    def distance(x1: int, y1: int, z1: int, w1: int, x2: int, y2: int, z2: int, w2: int) -> float:
        """
        Return the distance between `(x1, y1, z1, w1)` and `(x2, y2, z2, w2)`.

        Arguments
        - x1: the x component of the first vector
        - y1: the y component of the first vector
        - z1: the z component of the first vector
        - w1: the w component of the first vector
        - x2: the x component of the second vector
        - y2: the y component of the second vector
        - z2: the z component of the second vector
        - w2: the 2 component of the second vector

        Returns
        - the euclidean distance
        """
        ...


    @staticmethod
    def distanceSquared(x1: int, y1: int, z1: int, w1: int, x2: int, y2: int, z2: int, w2: int) -> int:
        """
        Return the squared distance between `(x1, y1, z1, w1)` and `(x2, y2, z2, w2)`.

        Arguments
        - x1: the x component of the first vector
        - y1: the y component of the first vector
        - z1: the z component of the first vector
        - w1: the w component of the first vector
        - x2: the x component of the second vector
        - y2: the y component of the second vector
        - z2: the z component of the second vector
        - w2: the w component of the second vector

        Returns
        - the euclidean distance squared
        """
        ...


    def dot(self, v: "Vector4Lc") -> int:
        ...


    def dot(self, v: "Vector4ic") -> int:
        ...


    def zero(self) -> "Vector4L":
        """
        Set all components to zero.

        Returns
        - this
        """
        ...


    def negate(self) -> "Vector4L":
        """
        Negate this vector.

        Returns
        - this
        """
        ...


    def negate(self, dest: "Vector4L") -> "Vector4L":
        ...


    def toString(self) -> str:
        """
        Return a string representation of this vector.
        
        This method creates a new DecimalFormat on every invocation with the format string "`0.000E0;-`".

        Returns
        - the string representation
        """
        ...


    def toString(self, formatter: "NumberFormat") -> str:
        """
        Return a string representation of this vector by formatting the vector components with the given NumberFormat.

        Arguments
        - formatter: the NumberFormat used to format the vector components with

        Returns
        - the string representation
        """
        ...


    def writeExternal(self, out: "ObjectOutput") -> None:
        ...


    def readExternal(self, in: "ObjectInput") -> None:
        ...


    def min(self, v: "Vector4Lc") -> "Vector4L":
        """
        Set the components of this vector to be the component-wise minimum of this and the other vector.

        Arguments
        - v: the other vector

        Returns
        - this
        """
        ...


    def min(self, v: "Vector4Lc", dest: "Vector4L") -> "Vector4L":
        ...


    def max(self, v: "Vector4Lc") -> "Vector4L":
        """
        Set the components of this vector to be the component-wise maximum of this and the other vector.

        Arguments
        - v: the other vector

        Returns
        - this
        """
        ...


    def max(self, v: "Vector4Lc", dest: "Vector4L") -> "Vector4L":
        ...


    def absolute(self) -> "Vector4L":
        """
        Compute the absolute of each of this vector's components.

        Returns
        - this
        """
        ...


    def absolute(self, dest: "Vector4L") -> "Vector4L":
        ...


    def hashCode(self) -> int:
        ...


    def equals(self, obj: "Object") -> bool:
        ...


    def equals(self, x: int, y: int, z: int, w: int) -> bool:
        ...


    def clone(self) -> "Object":
        ...
