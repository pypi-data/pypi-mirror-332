"""
Python module generated from Java source file org.joml.Vector2L

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


class Vector2L(Externalizable, Cloneable, Vector2Lc):
    """
    Contains the definition of a vector comprising 2 longs and associated
    transformations.

    Author(s)
    - Kai Burjack
    """

    def __init__(self):
        """
        Create a new Vector2L and initialize its components to zero.
        """
        ...


    def __init__(self, s: int):
        """
        Create a new Vector2L and initialize both of its components with
        the given value.

        Arguments
        - s: the value of both components
        """
        ...


    def __init__(self, x: int, y: int):
        """
        Create a new Vector2L and initialize its components to the given values.

        Arguments
        - x: the x component
        - y: the y component
        """
        ...


    def __init__(self, x: float, y: float, mode: int):
        """
        Create a new Vector2L and initialize its component values and
        round using the given RoundingMode.

        Arguments
        - x: the x component
        - y: the y component
        - mode: the RoundingMode to use
        """
        ...


    def __init__(self, x: float, y: float, mode: int):
        """
        Create a new Vector2L and initialize its component values and
        round using the given RoundingMode.

        Arguments
        - x: the x component
        - y: the y component
        - mode: the RoundingMode to use
        """
        ...


    def __init__(self, v: "Vector2Lc"):
        """
        Create a new Vector2L and initialize its components to the one of
        the given vector.

        Arguments
        - v: the Vector2Lc to copy the values from
        """
        ...


    def __init__(self, v: "Vector2ic"):
        """
        Create a new Vector2L and initialize its components to the one of
        the given vector.

        Arguments
        - v: the Vector2ic to copy the values from
        """
        ...


    def __init__(self, v: "Vector2fc", mode: int):
        """
        Create a new Vector2L and initialize its components to the rounded value of
        the given vector.

        Arguments
        - v: the Vector2fc to round and copy the values from
        - mode: the RoundingMode to use
        """
        ...


    def __init__(self, v: "Vector2dc", mode: int):
        """
        Create a new Vector2L and initialize its components to the rounded value of
        the given vector.

        Arguments
        - v: the Vector2dc to round and copy the values from
        - mode: the RoundingMode to use
        """
        ...


    def __init__(self, xy: list[int]):
        """
        Create a new Vector2L and initialize its two components from the first
        two elements of the given array.

        Arguments
        - xy: the array containing at least three elements
        """
        ...


    def __init__(self, buffer: "ByteBuffer"):
        """
        Create a new Vector2L and read this vector from the supplied
        ByteBuffer at the current buffer
        ByteBuffer.position() position.
        
        This method will not increment the position of the given ByteBuffer.
        
        In order to specify the offset into the ByteBuffer at which the vector is
        read, use .Vector2L(int, ByteBuffer), taking the absolute
        position as parameter.

        Arguments
        - buffer: values will be read in `x, y` order

        See
        - .Vector2L(int, ByteBuffer)
        """
        ...


    def __init__(self, index: int, buffer: "ByteBuffer"):
        """
        Create a new Vector2L and read this vector from the supplied
        ByteBuffer starting at the specified absolute buffer
        position/index.
        
        This method will not increment the position of the given ByteBuffer.

        Arguments
        - index: the absolute position into the ByteBuffer
        - buffer: values will be read in `x, y` order
        """
        ...


    def __init__(self, buffer: "LongBuffer"):
        """
        Create a new Vector2L and read this vector from the supplied
        LongBuffer at the current buffer
        LongBuffer.position() position.
        
        This method will not increment the position of the given IntBuffer.
        
        In order to specify the offset into the IntBuffer at which the vector is
        read, use .Vector2L(int, LongBuffer), taking the absolute position
        as parameter.

        Arguments
        - buffer: values will be read in `x, y` order

        See
        - .Vector2L(int, LongBuffer)
        """
        ...


    def __init__(self, index: int, buffer: "LongBuffer"):
        """
        Create a new Vector2L and read this vector from the supplied
        LongBuffer starting at the specified absolute buffer
        position/index.
        
        This method will not increment the position of the given IntBuffer.

        Arguments
        - index: the absolute position into the IntBuffer
        - buffer: values will be read in `x, y` order
        """
        ...


    def x(self) -> int:
        ...


    def y(self) -> int:
        ...


    def set(self, s: int) -> "Vector2L":
        """
        Set the x and y components to the supplied value.

        Arguments
        - s: scalar value of both components

        Returns
        - this
        """
        ...


    def set(self, x: int, y: int) -> "Vector2L":
        """
        Set the x and y components to the supplied values.

        Arguments
        - x: the x component
        - y: the y component

        Returns
        - this
        """
        ...


    def set(self, v: "Vector2Lc") -> "Vector2L":
        """
        Set this vector to the values of v.

        Arguments
        - v: the vector to copy from

        Returns
        - this
        """
        ...


    def set(self, v: "Vector2ic") -> "Vector2L":
        """
        Set this vector to the values of v.

        Arguments
        - v: the vector to copy from

        Returns
        - this
        """
        ...


    def set(self, v: "Vector2dc") -> "Vector2L":
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


    def set(self, v: "Vector2dc", mode: int) -> "Vector2L":
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


    def set(self, v: "Vector2fc", mode: int) -> "Vector2L":
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


    def set(self, xy: list[int]) -> "Vector2L":
        """
        Set the two components of this vector to the first two elements of the given array.

        Arguments
        - xy: the array containing at least two elements

        Returns
        - this
        """
        ...


    def set(self, buffer: "ByteBuffer") -> "Vector2L":
        """
        Read this vector from the supplied ByteBuffer at the current
        buffer ByteBuffer.position() position.
        
        This method will not increment the position of the given ByteBuffer.
        
        In order to specify the offset into the ByteBuffer at which the vector is
        read, use .set(int, ByteBuffer), taking the absolute position as
        parameter.

        Arguments
        - buffer: values will be read in `x, y` order

        Returns
        - this

        See
        - .set(int, ByteBuffer)
        """
        ...


    def set(self, index: int, buffer: "ByteBuffer") -> "Vector2L":
        """
        Read this vector from the supplied ByteBuffer starting at the
        specified absolute buffer position/index.
        
        This method will not increment the position of the given ByteBuffer.

        Arguments
        - index: the absolute position into the ByteBuffer
        - buffer: values will be read in `x, y` order

        Returns
        - this
        """
        ...


    def set(self, buffer: "LongBuffer") -> "Vector2L":
        """
        Read this vector from the supplied LongBuffer at the current
        buffer LongBuffer.position() position.
        
        This method will not increment the position of the given IntBuffer.
        
        In order to specify the offset into the IntBuffer at which the vector is
        read, use .set(int, LongBuffer), taking the absolute position as
        parameter.

        Arguments
        - buffer: values will be read in `x, y` order

        Returns
        - this

        See
        - .set(int, LongBuffer)
        """
        ...


    def set(self, index: int, buffer: "LongBuffer") -> "Vector2L":
        """
        Read this vector from the supplied LongBuffer starting at the
        specified absolute buffer position/index.
        
        This method will not increment the position of the given IntBuffer.

        Arguments
        - index: the absolute position into the IntBuffer
        - buffer: values will be read in `x, y` order

        Returns
        - this
        """
        ...


    def setFromAddress(self, address: int) -> "Vector2L":
        """
        Set the values of this vector by reading 2 integer values from off-heap memory,
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


    def setComponent(self, component: int, value: int) -> "Vector2L":
        """
        Set the value of the specified component of this vector.

        Arguments
        - component: the component whose value to set, within `[0..1]`
        - value: the value to set

        Returns
        - this

        Raises
        - IllegalArgumentException: if `component` is not within `[0..1]`
        """
        ...


    def get(self, buffer: "ByteBuffer") -> "ByteBuffer":
        ...


    def get(self, index: int, buffer: "ByteBuffer") -> "ByteBuffer":
        ...


    def get(self, buffer: "LongBuffer") -> "LongBuffer":
        ...


    def get(self, index: int, buffer: "LongBuffer") -> "LongBuffer":
        ...


    def getToAddress(self, address: int) -> "Vector2Lc":
        ...


    def sub(self, v: "Vector2Lc") -> "Vector2L":
        """
        Subtract the supplied vector from this one and store the result in
        `this`.

        Arguments
        - v: the vector to subtract

        Returns
        - this
        """
        ...


    def sub(self, v: "Vector2Lc", dest: "Vector2L") -> "Vector2L":
        ...


    def sub(self, v: "Vector2ic") -> "Vector2L":
        """
        Subtract the supplied vector from this one and store the result in
        `this`.

        Arguments
        - v: the vector to subtract

        Returns
        - this
        """
        ...


    def sub(self, v: "Vector2ic", dest: "Vector2L") -> "Vector2L":
        ...


    def sub(self, x: int, y: int) -> "Vector2L":
        """
        Decrement the components of this vector by the given values.

        Arguments
        - x: the x component to subtract
        - y: the y component to subtract

        Returns
        - this
        """
        ...


    def sub(self, x: int, y: int, dest: "Vector2L") -> "Vector2L":
        ...


    def lengthSquared(self) -> int:
        ...


    @staticmethod
    def lengthSquared(x: int, y: int) -> int:
        """
        Get the length squared of a 2-dimensional single-precision vector.

        Arguments
        - x: The vector's x component
        - y: The vector's y component

        Returns
        - the length squared of the given vector
        """
        ...


    def length(self) -> float:
        ...


    @staticmethod
    def length(x: int, y: int) -> float:
        """
        Get the length of a 2-dimensional single-precision vector.

        Arguments
        - x: The vector's x component
        - y: The vector's y component

        Returns
        - the length squared of the given vector
        """
        ...


    def distance(self, v: "Vector2Lc") -> float:
        ...


    def distance(self, x: int, y: int) -> float:
        ...


    def distanceSquared(self, v: "Vector2Lc") -> int:
        ...


    def distanceSquared(self, x: int, y: int) -> int:
        ...


    def gridDistance(self, v: "Vector2Lc") -> int:
        ...


    def gridDistance(self, x: int, y: int) -> int:
        ...


    @staticmethod
    def distance(x1: int, y1: int, x2: int, y2: int) -> float:
        """
        Return the distance between `(x1, y1)` and `(x2, y2)`.

        Arguments
        - x1: the x component of the first vector
        - y1: the y component of the first vector
        - x2: the x component of the second vector
        - y2: the y component of the second vector

        Returns
        - the euclidean distance
        """
        ...


    @staticmethod
    def distanceSquared(x1: int, y1: int, x2: int, y2: int) -> int:
        """
        Return the squared distance between `(x1, y1)` and `(x2, y2)`.

        Arguments
        - x1: the x component of the first vector
        - y1: the y component of the first vector
        - x2: the x component of the second vector
        - y2: the y component of the second vector

        Returns
        - the euclidean distance squared
        """
        ...


    def add(self, v: "Vector2Lc") -> "Vector2L":
        """
        Add `v` to this vector.

        Arguments
        - v: the vector to add

        Returns
        - this
        """
        ...


    def add(self, v: "Vector2Lc", dest: "Vector2L") -> "Vector2L":
        ...


    def add(self, v: "Vector2ic") -> "Vector2L":
        """
        Add `v` to this vector.

        Arguments
        - v: the vector to add

        Returns
        - this
        """
        ...


    def add(self, v: "Vector2ic", dest: "Vector2L") -> "Vector2L":
        ...


    def add(self, x: int, y: int) -> "Vector2L":
        """
        Increment the components of this vector by the given values.

        Arguments
        - x: the x component to add
        - y: the y component to add

        Returns
        - this
        """
        ...


    def add(self, x: int, y: int, dest: "Vector2L") -> "Vector2L":
        ...


    def mul(self, scalar: int) -> "Vector2L":
        """
        Multiply all components of this vector by the given scalar
        value.

        Arguments
        - scalar: the scalar to multiply this vector by

        Returns
        - this
        """
        ...


    def mul(self, scalar: int, dest: "Vector2L") -> "Vector2L":
        ...


    def mul(self, v: "Vector2Lc") -> "Vector2L":
        """
        Add the supplied vector by this one.

        Arguments
        - v: the vector to multiply

        Returns
        - this
        """
        ...


    def mul(self, v: "Vector2Lc", dest: "Vector2L") -> "Vector2L":
        ...


    def mul(self, v: "Vector2ic") -> "Vector2L":
        """
        Add the supplied vector by this one.

        Arguments
        - v: the vector to multiply

        Returns
        - this
        """
        ...


    def mul(self, v: "Vector2ic", dest: "Vector2L") -> "Vector2L":
        ...


    def mul(self, x: int, y: int) -> "Vector2L":
        """
        Multiply the components of this vector by the given values.

        Arguments
        - x: the x component to multiply
        - y: the y component to multiply

        Returns
        - this
        """
        ...


    def mul(self, x: int, y: int, dest: "Vector2L") -> "Vector2L":
        ...


    def div(self, scalar: float) -> "Vector2L":
        """
        Divide all components of this vector by the given scalar value.

        Arguments
        - scalar: the scalar to divide by

        Returns
        - a vector holding the result
        """
        ...


    def div(self, scalar: float, dest: "Vector2L") -> "Vector2L":
        ...


    def div(self, scalar: int) -> "Vector2L":
        """
        Divide all components of this vector by the given scalar value.

        Arguments
        - scalar: the scalar to divide by

        Returns
        - a vector holding the result
        """
        ...


    def div(self, scalar: int, dest: "Vector2L") -> "Vector2L":
        ...


    def zero(self) -> "Vector2L":
        """
        Set all components to zero.

        Returns
        - this
        """
        ...


    def writeExternal(self, out: "ObjectOutput") -> None:
        ...


    def readExternal(self, in: "ObjectInput") -> None:
        ...


    def negate(self) -> "Vector2L":
        """
        Negate this vector.

        Returns
        - this
        """
        ...


    def negate(self, dest: "Vector2L") -> "Vector2L":
        ...


    def min(self, v: "Vector2Lc") -> "Vector2L":
        """
        Set the components of this vector to be the component-wise minimum of this and the other vector.

        Arguments
        - v: the other vector

        Returns
        - this
        """
        ...


    def min(self, v: "Vector2Lc", dest: "Vector2L") -> "Vector2L":
        ...


    def max(self, v: "Vector2Lc") -> "Vector2L":
        """
        Set the components of this vector to be the component-wise maximum of this and the other vector.

        Arguments
        - v: the other vector

        Returns
        - this
        """
        ...


    def max(self, v: "Vector2Lc", dest: "Vector2L") -> "Vector2L":
        ...


    def maxComponent(self) -> int:
        ...


    def minComponent(self) -> int:
        ...


    def absolute(self) -> "Vector2L":
        """
        Set `this` vector's components to their respective absolute values.

        Returns
        - this
        """
        ...


    def absolute(self, dest: "Vector2L") -> "Vector2L":
        ...


    def hashCode(self) -> int:
        ...


    def equals(self, obj: "Object") -> bool:
        ...


    def equals(self, x: int, y: int) -> bool:
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


    def clone(self) -> "Object":
        ...
