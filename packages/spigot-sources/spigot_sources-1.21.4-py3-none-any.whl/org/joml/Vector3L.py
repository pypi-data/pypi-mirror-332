"""
Python module generated from Java source file org.joml.Vector3L

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


class Vector3L(Externalizable, Cloneable, Vector3Lc):
    """
    Contains the definition of a vector comprising 3 longs and associated
    transformations.

    Author(s)
    - Kai Burjack
    """

    def __init__(self):
        """
        Create a new Vector3L of `(0, 0, 0)`.
        """
        ...


    def __init__(self, d: int):
        """
        Create a new Vector3L and initialize all three components with
        the given value.

        Arguments
        - d: the value of all three components
        """
        ...


    def __init__(self, x: int, y: int, z: int):
        """
        Create a new Vector3L with the given component values.

        Arguments
        - x: the value of x
        - y: the value of y
        - z: the value of z
        """
        ...


    def __init__(self, v: "Vector3Lc"):
        """
        Create a new Vector3L with the same values as `v`.

        Arguments
        - v: the Vector3Lc to copy the values from
        """
        ...


    def __init__(self, v: "Vector2ic", z: int):
        """
        Create a new Vector3L with the first two components from the
        given `v` and the given `z`

        Arguments
        - v: the Vector2ic to copy the values from
        - z: the z component
        """
        ...


    def __init__(self, x: float, y: float, z: float, mode: int):
        """
        Create a new Vector3L with the given component values and
        round using the given RoundingMode.

        Arguments
        - x: the value of x
        - y: the value of y
        - z: the value of z
        - mode: the RoundingMode to use
        """
        ...


    def __init__(self, x: float, y: float, z: float, mode: int):
        """
        Create a new Vector3L with the given component values and
        round using the given RoundingMode.

        Arguments
        - x: the value of x
        - y: the value of y
        - z: the value of z
        - mode: the RoundingMode to use
        """
        ...


    def __init__(self, v: "Vector2fc", z: float, mode: int):
        """
        Create a new Vector3L with the first two components from the
        given `v` and the given `z` and round using the given RoundingMode.

        Arguments
        - v: the Vector2fc to copy the values from
        - z: the z component
        - mode: the RoundingMode to use
        """
        ...


    def __init__(self, v: "Vector3fc", mode: int):
        """
        Create a new Vector3L and initialize its components to the rounded value of
        the given vector.

        Arguments
        - v: the Vector3fc to round and copy the values from
        - mode: the RoundingMode to use
        """
        ...


    def __init__(self, v: "Vector2dc", z: float, mode: int):
        """
        Create a new Vector3L with the first two components from the
        given `v` and the given `z` and round using the given RoundingMode.

        Arguments
        - v: the Vector2dc to copy the values from
        - z: the z component
        - mode: the RoundingMode to use
        """
        ...


    def __init__(self, v: "Vector3dc", mode: int):
        """
        Create a new Vector3L and initialize its components to the rounded value of
        the given vector.

        Arguments
        - v: the Vector3dc to round and copy the values from
        - mode: the RoundingMode to use
        """
        ...


    def __init__(self, xyz: list[int]):
        """
        Create a new Vector3L and initialize its three components from the first
        three elements of the given array.

        Arguments
        - xyz: the array containing at least three elements
        """
        ...


    def __init__(self, buffer: "ByteBuffer"):
        """
        Create a new Vector3L and read this vector from the supplied
        ByteBuffer at the current buffer
        ByteBuffer.position() position.
        
        This method will not increment the position of the given ByteBuffer.
        
        In order to specify the offset into the ByteBuffer at which the vector is
        read, use .Vector3L(int, ByteBuffer), taking the absolute
        position as parameter.

        Arguments
        - buffer: values will be read in `x, y, z` order

        See
        - .Vector3L(int, ByteBuffer)
        """
        ...


    def __init__(self, index: int, buffer: "ByteBuffer"):
        """
        Create a new Vector3L and read this vector from the supplied
        ByteBuffer starting at the specified absolute buffer
        position/index.
        
        This method will not increment the position of the given ByteBuffer.

        Arguments
        - index: the absolute position into the ByteBuffer
        - buffer: values will be read in `x, y, z` order
        """
        ...


    def __init__(self, buffer: "LongBuffer"):
        """
        Create a new Vector3L and read this vector from the supplied
        LongBuffer at the current buffer
        LongBuffer.position() position.
        
        This method will not increment the position of the given LongBuffer.
        
        In order to specify the offset into the LongBuffer at which the vector is
        read, use .Vector3L(int, LongBuffer), taking the absolute position
        as parameter.

        Arguments
        - buffer: values will be read in `x, y, z` order

        See
        - .Vector3L(int, LongBuffer)
        """
        ...


    def __init__(self, index: int, buffer: "LongBuffer"):
        """
        Create a new Vector3L and read this vector from the supplied
        LongBuffer starting at the specified absolute buffer
        position/index.
        
        This method will not increment the position of the given LongBuffer.

        Arguments
        - index: the absolute position into the LongBuffer
        - buffer: values will be read in `x, y, z` order
        """
        ...


    def x(self) -> int:
        ...


    def y(self) -> int:
        ...


    def z(self) -> int:
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


    def set(self, v: "Vector3Lc") -> "Vector3L":
        """
        Set the x, y and z components to match the supplied vector.

        Arguments
        - v: contains the values of x, y and z to set

        Returns
        - this
        """
        ...


    def set(self, v: "Vector3dc") -> "Vector3L":
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


    def set(self, v: "Vector3dc", mode: int) -> "Vector3L":
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


    def set(self, v: "Vector3fc", mode: int) -> "Vector3L":
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


    def set(self, v: "Vector2ic", z: int) -> "Vector3L":
        """
        Set the first two components from the given `v` and the z
        component from the given `z`

        Arguments
        - v: the Vector2ic to copy the values from
        - z: the z component

        Returns
        - this
        """
        ...


    def set(self, d: int) -> "Vector3L":
        """
        Set the x, y, and z components to the supplied value.

        Arguments
        - d: the value of all three components

        Returns
        - this
        """
        ...


    def set(self, x: int, y: int, z: int) -> "Vector3L":
        """
        Set the x, y and z components to the supplied values.

        Arguments
        - x: the x component
        - y: the y component
        - z: the z component

        Returns
        - this
        """
        ...


    def set(self, xyz: list[int]) -> "Vector3L":
        """
        Set the three components of this vector to the first three elements of the given array.

        Arguments
        - xyz: the array containing at least three elements

        Returns
        - this
        """
        ...


    def set(self, buffer: "ByteBuffer") -> "Vector3L":
        """
        Read this vector from the supplied ByteBuffer at the current
        buffer ByteBuffer.position() position.
        
        This method will not increment the position of the given ByteBuffer.
        
        In order to specify the offset into the ByteBuffer at which the vector is
        read, use .set(int, ByteBuffer), taking the absolute position as
        parameter.

        Arguments
        - buffer: values will be read in `x, y, z` order

        Returns
        - this

        See
        - .set(int, ByteBuffer)
        """
        ...


    def set(self, index: int, buffer: "ByteBuffer") -> "Vector3L":
        """
        Read this vector from the supplied ByteBuffer starting at the
        specified absolute buffer position/index.
        
        This method will not increment the position of the given ByteBuffer.

        Arguments
        - index: the absolute position into the ByteBuffer
        - buffer: values will be read in `x, y, z` order

        Returns
        - this
        """
        ...


    def set(self, buffer: "LongBuffer") -> "Vector3L":
        """
        Read this vector from the supplied LongBuffer at the current
        buffer LongBuffer.position() position.
        
        This method will not increment the position of the given LongBuffer.
        
        In order to specify the offset into the LongBuffer at which the vector is
        read, use .set(int, LongBuffer), taking the absolute position as
        parameter.

        Arguments
        - buffer: values will be read in `x, y, z` order

        Returns
        - this

        See
        - .set(int, LongBuffer)
        """
        ...


    def set(self, index: int, buffer: "LongBuffer") -> "Vector3L":
        """
        Read this vector from the supplied LongBuffer starting at the
        specified absolute buffer position/index.
        
        This method will not increment the position of the given LongBuffer.

        Arguments
        - index: the absolute position into the LongBuffer
        - buffer: values will be read in `x, y, z` order

        Returns
        - this
        """
        ...


    def setFromAddress(self, address: int) -> "Vector3L":
        """
        Set the values of this vector by reading 3 integer values from off-heap memory,
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


    def setComponent(self, component: int, value: int) -> "Vector3L":
        """
        Set the value of the specified component of this vector.

        Arguments
        - component: the component whose value to set, within `[0..2]`
        - value: the value to set

        Returns
        - this

        Raises
        - IllegalArgumentException: if `component` is not within `[0..2]`
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


    def getToAddress(self, address: int) -> "Vector3Lc":
        ...


    def sub(self, v: "Vector3Lc") -> "Vector3L":
        """
        Subtract the supplied vector from this one and store the result in
        `this`.

        Arguments
        - v: the vector to subtract

        Returns
        - this
        """
        ...


    def sub(self, v: "Vector3Lc", dest: "Vector3L") -> "Vector3L":
        ...


    def sub(self, x: int, y: int, z: int) -> "Vector3L":
        """
        Decrement the components of this vector by the given values.

        Arguments
        - x: the x component to subtract
        - y: the y component to subtract
        - z: the z component to subtract

        Returns
        - this
        """
        ...


    def sub(self, x: int, y: int, z: int, dest: "Vector3L") -> "Vector3L":
        ...


    def add(self, v: "Vector3Lc") -> "Vector3L":
        """
        Add the supplied vector to this one.

        Arguments
        - v: the vector to add

        Returns
        - this
        """
        ...


    def add(self, v: "Vector3Lc", dest: "Vector3L") -> "Vector3L":
        ...


    def add(self, x: int, y: int, z: int) -> "Vector3L":
        """
        Increment the components of this vector by the given values.

        Arguments
        - x: the x component to add
        - y: the y component to add
        - z: the z component to add

        Returns
        - this
        """
        ...


    def add(self, x: int, y: int, z: int, dest: "Vector3L") -> "Vector3L":
        ...


    def mul(self, scalar: int) -> "Vector3L":
        """
        Multiply all components of this vector by the given scalar
        value.

        Arguments
        - scalar: the scalar to multiply this vector by

        Returns
        - this
        """
        ...


    def mul(self, scalar: int, dest: "Vector3L") -> "Vector3L":
        ...


    def mul(self, v: "Vector3Lc") -> "Vector3L":
        """
        Multiply all components of this vector by the given vector.

        Arguments
        - v: the vector to multiply

        Returns
        - this
        """
        ...


    def mul(self, v: "Vector3Lc", dest: "Vector3L") -> "Vector3L":
        ...


    def mul(self, x: int, y: int, z: int) -> "Vector3L":
        """
        Multiply the components of this vector by the given values.

        Arguments
        - x: the x component to multiply
        - y: the y component to multiply
        - z: the z component to multiply

        Returns
        - this
        """
        ...


    def mul(self, x: int, y: int, z: int, dest: "Vector3L") -> "Vector3L":
        ...


    def div(self, scalar: float) -> "Vector3L":
        """
        Divide all components of this vector by the given scalar value.

        Arguments
        - scalar: the scalar to divide by

        Returns
        - this
        """
        ...


    def div(self, scalar: float, dest: "Vector3L") -> "Vector3L":
        ...


    def div(self, scalar: int) -> "Vector3L":
        """
        Divide all components of this vector by the given scalar value.

        Arguments
        - scalar: the scalar to divide by

        Returns
        - this
        """
        ...


    def div(self, scalar: int, dest: "Vector3L") -> "Vector3L":
        ...


    def lengthSquared(self) -> int:
        ...


    @staticmethod
    def lengthSquared(x: int, y: int, z: int) -> int:
        """
        Get the length squared of a 3-dimensional single-precision vector.

        Arguments
        - x: The vector's x component
        - y: The vector's y component
        - z: The vector's z component

        Returns
        - the length squared of the given vector
        """
        ...


    def length(self) -> float:
        ...


    @staticmethod
    def length(x: int, y: int, z: int) -> float:
        """
        Get the length of a 3-dimensional single-precision vector.

        Arguments
        - x: The vector's x component
        - y: The vector's y component
        - z: The vector's z component

        Returns
        - the length squared of the given vector
        """
        ...


    def distance(self, v: "Vector3Lc") -> float:
        ...


    def distance(self, x: int, y: int, z: int) -> float:
        ...


    def gridDistance(self, v: "Vector3Lc") -> int:
        ...


    def gridDistance(self, x: int, y: int, z: int) -> int:
        ...


    def distanceSquared(self, v: "Vector3Lc") -> int:
        ...


    def distanceSquared(self, x: int, y: int, z: int) -> int:
        ...


    @staticmethod
    def distance(x1: int, y1: int, z1: int, x2: int, y2: int, z2: int) -> float:
        """
        Return the distance between `(x1, y1, z1)` and `(x2, y2, z2)`.

        Arguments
        - x1: the x component of the first vector
        - y1: the y component of the first vector
        - z1: the z component of the first vector
        - x2: the x component of the second vector
        - y2: the y component of the second vector
        - z2: the z component of the second vector

        Returns
        - the euclidean distance
        """
        ...


    @staticmethod
    def distanceSquared(x1: int, y1: int, z1: int, x2: int, y2: int, z2: int) -> int:
        """
        Return the squared distance between `(x1, y1, z1)` and `(x2, y2, z2)`.

        Arguments
        - x1: the x component of the first vector
        - y1: the y component of the first vector
        - z1: the z component of the first vector
        - x2: the x component of the second vector
        - y2: the y component of the second vector
        - z2: the z component of the second vector

        Returns
        - the euclidean distance squared
        """
        ...


    def zero(self) -> "Vector3L":
        """
        Set all components to zero.

        Returns
        - this
        """
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


    def negate(self) -> "Vector3L":
        """
        Negate this vector.

        Returns
        - this
        """
        ...


    def negate(self, dest: "Vector3L") -> "Vector3L":
        ...


    def min(self, v: "Vector3Lc") -> "Vector3L":
        """
        Set the components of this vector to be the component-wise minimum of this and the other vector.

        Arguments
        - v: the other vector

        Returns
        - this
        """
        ...


    def min(self, v: "Vector3Lc", dest: "Vector3L") -> "Vector3L":
        ...


    def max(self, v: "Vector3Lc") -> "Vector3L":
        """
        Set the components of this vector to be the component-wise maximum of this and the other vector.

        Arguments
        - v: the other vector

        Returns
        - this
        """
        ...


    def max(self, v: "Vector3Lc", dest: "Vector3L") -> "Vector3L":
        ...


    def maxComponent(self) -> int:
        ...


    def minComponent(self) -> int:
        ...


    def absolute(self) -> "Vector3L":
        """
        Set `this` vector's components to their respective absolute values.

        Returns
        - this
        """
        ...


    def absolute(self, dest: "Vector3L") -> "Vector3L":
        ...


    def hashCode(self) -> int:
        ...


    def equals(self, obj: "Object") -> bool:
        ...


    def equals(self, x: int, y: int, z: int) -> bool:
        ...


    def clone(self) -> "Object":
        ...
