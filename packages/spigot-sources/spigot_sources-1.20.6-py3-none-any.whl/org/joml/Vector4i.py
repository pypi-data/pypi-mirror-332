"""
Python module generated from Java source file org.joml.Vector4i

Java source file obtained from artifact joml version 1.10.5

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


class Vector4i(Externalizable, Cloneable, Vector4ic):
    """
    Contains the definition of a Vector comprising 4 ints and associated
    transformations.

    Author(s)
    - Hans Uhlig
    """

    def __init__(self):
        """
        Create a new Vector4i of `(0, 0, 0, 1)`.
        """
        ...


    def __init__(self, v: "Vector4ic"):
        """
        Create a new Vector4i with the same values as `v`.

        Arguments
        - v: the Vector4ic to copy the values from
        """
        ...


    def __init__(self, v: "Vector3ic", w: int):
        """
        Create a new Vector4i with the first three components from the
        given `v` and the given `w`.

        Arguments
        - v: the Vector3ic
        - w: the w component
        """
        ...


    def __init__(self, v: "Vector2ic", z: int, w: int):
        """
        Create a new Vector4i with the first two components from the
        given `v` and the given `z`, and `w`.

        Arguments
        - v: the Vector2ic
        - z: the z component
        - w: the w component
        """
        ...


    def __init__(self, v: "Vector3fc", w: float, mode: int):
        """
        Create a new Vector4i with the first three components from the
        given `v` and the given `w` and round using the given RoundingMode.

        Arguments
        - v: the Vector3fc to copy the values from
        - w: the w component
        - mode: the RoundingMode to use
        """
        ...


    def __init__(self, v: "Vector4fc", mode: int):
        """
        Create a new Vector4i and initialize its components to the rounded value of
        the given vector.

        Arguments
        - v: the Vector4fc to round and copy the values from
        - mode: the RoundingMode to use
        """
        ...


    def __init__(self, v: "Vector4dc", mode: int):
        """
        Create a new Vector4i and initialize its components to the rounded value of
        the given vector.

        Arguments
        - v: the Vector4dc to round and copy the values from
        - mode: the RoundingMode to use
        """
        ...


    def __init__(self, s: int):
        """
        Create a new Vector4i and initialize all four components with the
        given value.

        Arguments
        - s: scalar value of all four components
        """
        ...


    def __init__(self, x: int, y: int, z: int, w: int):
        """
        Create a new Vector4i with the given component values.

        Arguments
        - x: the x component
        - y: the y component
        - z: the z component
        - w: the w component
        """
        ...


    def __init__(self, xyzw: list[int]):
        """
        Create a new Vector4i and initialize its four components from the first
        four elements of the given array.

        Arguments
        - xyzw: the array containing at least four elements
        """
        ...


    def __init__(self, buffer: "ByteBuffer"):
        """
        Create a new Vector4i and read this vector from the supplied
        ByteBuffer at the current buffer
        ByteBuffer.position() position.
        
        This method will not increment the position of the given ByteBuffer.
        
        In order to specify the offset into the ByteBuffer at which the vector is
        read, use .Vector4i(int, ByteBuffer), taking the absolute
        position as parameter.

        Arguments
        - buffer: values will be read in `x, y, z, w` order

        See
        - .Vector4i(int, ByteBuffer)
        """
        ...


    def __init__(self, index: int, buffer: "ByteBuffer"):
        """
        Create a new Vector4i and read this vector from the supplied
        ByteBuffer starting at the specified absolute buffer
        position/index.
        
        This method will not increment the position of the given ByteBuffer.

        Arguments
        - index: the absolute position into the ByteBuffer
        - buffer: values will be read in `x, y, z, w` order
        """
        ...


    def __init__(self, buffer: "IntBuffer"):
        """
        Create a new Vector4i and read this vector from the supplied
        IntBuffer at the current buffer
        IntBuffer.position() position.
        
        This method will not increment the position of the given IntBuffer.
        
        In order to specify the offset into the IntBuffer at which the vector is
        read, use .Vector4i(int, IntBuffer), taking the absolute position
        as parameter.

        Arguments
        - buffer: values will be read in `x, y, z, w` order

        See
        - .Vector4i(int, IntBuffer)
        """
        ...


    def __init__(self, index: int, buffer: "IntBuffer"):
        """
        Create a new Vector4i and read this vector from the supplied
        IntBuffer starting at the specified absolute buffer
        position/index.
        
        This method will not increment the position of the given IntBuffer.

        Arguments
        - index: the absolute position into the IntBuffer
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


    def set(self, v: "Vector4ic") -> "Vector4i":
        """
        Set this Vector4i to the values of the given `v`.

        Arguments
        - v: the vector whose values will be copied into this

        Returns
        - this
        """
        ...


    def set(self, v: "Vector4dc") -> "Vector4i":
        """
        Set this Vector4i to the values of v using RoundingMode.TRUNCATE rounding.
        
        Note that due to the given vector `v` storing the components
        in double-precision, there is the possibility to lose precision.

        Arguments
        - v: the vector to copy from

        Returns
        - this
        """
        ...


    def set(self, v: "Vector4dc", mode: int) -> "Vector4i":
        """
        Set this Vector4i to the values of v using the given RoundingMode.
        
        Note that due to the given vector `v` storing the components
        in double-precision, there is the possibility to lose precision.

        Arguments
        - v: the vector to copy from
        - mode: the RoundingMode to use

        Returns
        - this
        """
        ...


    def set(self, v: "Vector4fc", mode: int) -> "Vector4i":
        """
        Set this Vector4i to the values of v using the given RoundingMode.
        
        Note that due to the given vector `v` storing the components
        in double-precision, there is the possibility to lose precision.

        Arguments
        - v: the vector to copy from
        - mode: the RoundingMode to use

        Returns
        - this
        """
        ...


    def set(self, v: "Vector3ic", w: int) -> "Vector4i":
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


    def set(self, v: "Vector2ic", z: int, w: int) -> "Vector4i":
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


    def set(self, s: int) -> "Vector4i":
        """
        Set the x, y, z, and w components to the supplied value.

        Arguments
        - s: the value of all four components

        Returns
        - this
        """
        ...


    def set(self, x: int, y: int, z: int, w: int) -> "Vector4i":
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


    def set(self, xyzw: list[int]) -> "Vector4i":
        """
        Set the four components of this vector to the first four elements of the given array.

        Arguments
        - xyzw: the array containing at least four elements

        Returns
        - this
        """
        ...


    def set(self, buffer: "ByteBuffer") -> "Vector4i":
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


    def set(self, index: int, buffer: "ByteBuffer") -> "Vector4i":
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


    def set(self, buffer: "IntBuffer") -> "Vector4i":
        """
        Read this vector from the supplied IntBuffer at the current
        buffer IntBuffer.position() position.
        
        This method will not increment the position of the given IntBuffer.
        
        In order to specify the offset into the IntBuffer at which the vector is
        read, use .set(int, IntBuffer), taking the absolute position as
        parameter.

        Arguments
        - buffer: values will be read in `x, y, z, w` order

        Returns
        - this

        See
        - .set(int, IntBuffer)
        """
        ...


    def set(self, index: int, buffer: "IntBuffer") -> "Vector4i":
        """
        Read this vector from the supplied IntBuffer starting at the
        specified absolute buffer position/index.
        
        This method will not increment the position of the given IntBuffer.

        Arguments
        - index: the absolute position into the IntBuffer
        - buffer: values will be read in `x, y, z, w` order

        Returns
        - this
        """
        ...


    def setFromAddress(self, address: int) -> "Vector4i":
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


    def setComponent(self, component: int, value: int) -> "Vector4i":
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


    def get(self, buffer: "IntBuffer") -> "IntBuffer":
        ...


    def get(self, index: int, buffer: "IntBuffer") -> "IntBuffer":
        ...


    def get(self, buffer: "ByteBuffer") -> "ByteBuffer":
        ...


    def get(self, index: int, buffer: "ByteBuffer") -> "ByteBuffer":
        ...


    def getToAddress(self, address: int) -> "Vector4ic":
        ...


    def sub(self, v: "Vector4ic") -> "Vector4i":
        """
        Subtract the supplied vector from this one.

        Arguments
        - v: the vector to subtract

        Returns
        - this
        """
        ...


    def sub(self, x: int, y: int, z: int, w: int) -> "Vector4i":
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


    def sub(self, v: "Vector4ic", dest: "Vector4i") -> "Vector4i":
        ...


    def sub(self, x: int, y: int, z: int, w: int, dest: "Vector4i") -> "Vector4i":
        ...


    def add(self, v: "Vector4ic") -> "Vector4i":
        """
        Add the supplied vector to this one.

        Arguments
        - v: the vector to add

        Returns
        - this
        """
        ...


    def add(self, v: "Vector4ic", dest: "Vector4i") -> "Vector4i":
        ...


    def add(self, x: int, y: int, z: int, w: int) -> "Vector4i":
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


    def add(self, x: int, y: int, z: int, w: int, dest: "Vector4i") -> "Vector4i":
        ...


    def mul(self, v: "Vector4ic") -> "Vector4i":
        """
        Multiply this Vector4i component-wise by another Vector4i.

        Arguments
        - v: the other vector

        Returns
        - this
        """
        ...


    def mul(self, v: "Vector4ic", dest: "Vector4i") -> "Vector4i":
        ...


    def div(self, v: "Vector4ic") -> "Vector4i":
        """
        Divide this Vector4i component-wise by another Vector4i.

        Arguments
        - v: the vector to divide by

        Returns
        - this
        """
        ...


    def div(self, v: "Vector4ic", dest: "Vector4i") -> "Vector4i":
        ...


    def mul(self, scalar: int) -> "Vector4i":
        """
        Multiply all components of this Vector4i by the given scalar
        value.

        Arguments
        - scalar: the scalar to multiply by

        Returns
        - this
        """
        ...


    def mul(self, scalar: int, dest: "Vector4i") -> "Vector4i":
        ...


    def div(self, scalar: float) -> "Vector4i":
        """
        Divide all components of this Vector3i by the given scalar value.

        Arguments
        - scalar: the scalar to divide by

        Returns
        - this
        """
        ...


    def div(self, scalar: float, dest: "Vector4i") -> "Vector4i":
        ...


    def div(self, scalar: int) -> "Vector4i":
        """
        Divide all components of this Vector4i by the given scalar value.

        Arguments
        - scalar: the scalar to divide by

        Returns
        - this
        """
        ...


    def div(self, scalar: int, dest: "Vector4i") -> "Vector4i":
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


    def distance(self, v: "Vector4ic") -> float:
        ...


    def distance(self, x: int, y: int, z: int, w: int) -> float:
        ...


    def gridDistance(self, v: "Vector4ic") -> int:
        ...


    def gridDistance(self, x: int, y: int, z: int, w: int) -> int:
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


    def dot(self, v: "Vector4ic") -> int:
        ...


    def zero(self) -> "Vector4i":
        """
        Set all components to zero.

        Returns
        - this
        """
        ...


    def negate(self) -> "Vector4i":
        """
        Negate this vector.

        Returns
        - this
        """
        ...


    def negate(self, dest: "Vector4i") -> "Vector4i":
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


    def min(self, v: "Vector4ic") -> "Vector4i":
        """
        Set the components of this vector to be the component-wise minimum of this and the other vector.

        Arguments
        - v: the other vector

        Returns
        - this
        """
        ...


    def min(self, v: "Vector4ic", dest: "Vector4i") -> "Vector4i":
        ...


    def max(self, v: "Vector4ic") -> "Vector4i":
        """
        Set the components of this vector to be the component-wise maximum of this and the other vector.

        Arguments
        - v: the other vector

        Returns
        - this
        """
        ...


    def max(self, v: "Vector4ic", dest: "Vector4i") -> "Vector4i":
        ...


    def absolute(self) -> "Vector4i":
        """
        Compute the absolute of each of this vector's components.

        Returns
        - this
        """
        ...


    def absolute(self, dest: "Vector4i") -> "Vector4i":
        ...


    def hashCode(self) -> int:
        ...


    def equals(self, obj: "Object") -> bool:
        ...


    def equals(self, x: int, y: int, z: int, w: int) -> bool:
        ...


    def clone(self) -> "Object":
        ...
