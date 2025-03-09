"""
Python module generated from Java source file org.joml.Vector2f

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


class Vector2f(Externalizable, Cloneable, Vector2fc):
    """
    Represents a 2D vector with single-precision.

    Author(s)
    - F. Neurath
    """

    def __init__(self):
        """
        Create a new Vector2f and initialize its components to zero.
        """
        ...


    def __init__(self, d: float):
        """
        Create a new Vector2f and initialize both of its components with the given value.

        Arguments
        - d: the value of both components
        """
        ...


    def __init__(self, x: float, y: float):
        """
        Create a new Vector2f and initialize its components to the given values.

        Arguments
        - x: the x component
        - y: the y component
        """
        ...


    def __init__(self, v: "Vector2fc"):
        """
        Create a new Vector2f and initialize its components to the one of the given vector.

        Arguments
        - v: the Vector2fc to copy the values from
        """
        ...


    def __init__(self, v: "Vector2ic"):
        """
        Create a new Vector2f and initialize its components to the one of the given vector.

        Arguments
        - v: the Vector2ic to copy the values from
        """
        ...


    def __init__(self, xy: list[float]):
        """
        Create a new Vector2f and initialize its two components from the first
        two elements of the given array.

        Arguments
        - xy: the array containing at least two elements
        """
        ...


    def __init__(self, buffer: "ByteBuffer"):
        """
        Create a new Vector2f and read this vector from the supplied ByteBuffer
        at the current buffer ByteBuffer.position() position.
        
        This method will not increment the position of the given ByteBuffer.
        
        In order to specify the offset into the ByteBuffer at which
        the vector is read, use .Vector2f(int, ByteBuffer), taking
        the absolute position as parameter.

        Arguments
        - buffer: values will be read in `x, y` order

        See
        - .Vector2f(int, ByteBuffer)
        """
        ...


    def __init__(self, index: int, buffer: "ByteBuffer"):
        """
        Create a new Vector2f and read this vector from the supplied ByteBuffer
        starting at the specified absolute buffer position/index.
        
        This method will not increment the position of the given ByteBuffer.

        Arguments
        - index: the absolute position into the ByteBuffer
        - buffer: values will be read in `x, y` order
        """
        ...


    def __init__(self, buffer: "FloatBuffer"):
        """
        Create a new Vector2f and read this vector from the supplied FloatBuffer
        at the current buffer FloatBuffer.position() position.
        
        This method will not increment the position of the given FloatBuffer.
        
        In order to specify the offset into the FloatBuffer at which
        the vector is read, use .Vector2f(int, FloatBuffer), taking
        the absolute position as parameter.

        Arguments
        - buffer: values will be read in `x, y` order

        See
        - .Vector2f(int, FloatBuffer)
        """
        ...


    def __init__(self, index: int, buffer: "FloatBuffer"):
        """
        Create a new Vector2f and read this vector from the supplied FloatBuffer
        starting at the specified absolute buffer position/index.
        
        This method will not increment the position of the given FloatBuffer.

        Arguments
        - index: the absolute position into the FloatBuffer
        - buffer: values will be read in `x, y` order
        """
        ...


    def x(self) -> float:
        ...


    def y(self) -> float:
        ...


    def set(self, d: float) -> "Vector2f":
        """
        Set the x and y components to the supplied value.

        Arguments
        - d: the value of both components

        Returns
        - this
        """
        ...


    def set(self, x: float, y: float) -> "Vector2f":
        """
        Set the x and y components to the supplied values.

        Arguments
        - x: the x component
        - y: the y component

        Returns
        - this
        """
        ...


    def set(self, d: float) -> "Vector2f":
        """
        Set the x and y components to the supplied value.

        Arguments
        - d: the value of both components

        Returns
        - this
        """
        ...


    def set(self, x: float, y: float) -> "Vector2f":
        """
        Set the x and y components to the supplied values.

        Arguments
        - x: the x component
        - y: the y component

        Returns
        - this
        """
        ...


    def set(self, v: "Vector2fc") -> "Vector2f":
        """
        Set this Vector2f to the values of v.

        Arguments
        - v: the vector to copy from

        Returns
        - this
        """
        ...


    def set(self, v: "Vector2ic") -> "Vector2f":
        """
        Set this Vector2f to the values of v.

        Arguments
        - v: the vector to copy from

        Returns
        - this
        """
        ...


    def set(self, v: "Vector2dc") -> "Vector2f":
        """
        Set this Vector2f to the values of v.
        
        Note that due to the given vector `v` storing the components in double-precision,
        there is the possibility to lose precision.

        Arguments
        - v: the vector to copy from

        Returns
        - this
        """
        ...


    def set(self, xy: list[float]) -> "Vector2f":
        """
        Set the two components of this vector to the first two elements of the given array.

        Arguments
        - xy: the array containing at least two elements

        Returns
        - this
        """
        ...


    def set(self, buffer: "ByteBuffer") -> "Vector2f":
        """
        Read this vector from the supplied ByteBuffer at the current
        buffer ByteBuffer.position() position.
        
        This method will not increment the position of the given ByteBuffer.
        
        In order to specify the offset into the ByteBuffer at which
        the vector is read, use .set(int, ByteBuffer), taking
        the absolute position as parameter.

        Arguments
        - buffer: values will be read in `x, y` order

        Returns
        - this

        See
        - .set(int, ByteBuffer)
        """
        ...


    def set(self, index: int, buffer: "ByteBuffer") -> "Vector2f":
        """
        Read this vector from the supplied ByteBuffer starting at the specified
        absolute buffer position/index.
        
        This method will not increment the position of the given ByteBuffer.

        Arguments
        - index: the absolute position into the ByteBuffer
        - buffer: values will be read in `x, y` order

        Returns
        - this
        """
        ...


    def set(self, buffer: "FloatBuffer") -> "Vector2f":
        """
        Read this vector from the supplied FloatBuffer at the current
        buffer FloatBuffer.position() position.
        
        This method will not increment the position of the given FloatBuffer.
        
        In order to specify the offset into the FloatBuffer at which
        the vector is read, use .set(int, FloatBuffer), taking
        the absolute position as parameter.

        Arguments
        - buffer: values will be read in `x, y` order

        Returns
        - this

        See
        - .set(int, FloatBuffer)
        """
        ...


    def set(self, index: int, buffer: "FloatBuffer") -> "Vector2f":
        """
        Read this vector from the supplied FloatBuffer starting at the specified
        absolute buffer position/index.
        
        This method will not increment the position of the given FloatBuffer.

        Arguments
        - index: the absolute position into the FloatBuffer
        - buffer: values will be read in `x, y` order

        Returns
        - this
        """
        ...


    def setFromAddress(self, address: int) -> "Vector2f":
        """
        Set the values of this vector by reading 2 float values from off-heap memory,
        starting at the given address.
        
        This method will throw an UnsupportedOperationException when JOML is used with `-Djoml.nounsafe`.
        
        *This method is unsafe as it can result in a crash of the JVM process when the specified address range does not belong to this process.*

        Arguments
        - address: the off-heap memory address to read the vector values from

        Returns
        - this
        """
        ...


    def get(self, component: int) -> float:
        ...


    def get(self, mode: int, dest: "Vector2i") -> "Vector2i":
        ...


    def get(self, dest: "Vector2f") -> "Vector2f":
        ...


    def get(self, dest: "Vector2d") -> "Vector2d":
        ...


    def setComponent(self, component: int, value: float) -> "Vector2f":
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


    def get(self, buffer: "FloatBuffer") -> "FloatBuffer":
        ...


    def get(self, index: int, buffer: "FloatBuffer") -> "FloatBuffer":
        ...


    def getToAddress(self, address: int) -> "Vector2fc":
        ...


    def perpendicular(self) -> "Vector2f":
        """
        Set this vector to be one of its perpendicular vectors.

        Returns
        - this
        """
        ...


    def sub(self, v: "Vector2fc") -> "Vector2f":
        """
        Subtract `v` from this vector.

        Arguments
        - v: the vector to subtract

        Returns
        - this
        """
        ...


    def sub(self, v: "Vector2fc", dest: "Vector2f") -> "Vector2f":
        ...


    def sub(self, x: float, y: float) -> "Vector2f":
        """
        Subtract `(x, y)` from this vector.

        Arguments
        - x: the x component to subtract
        - y: the y component to subtract

        Returns
        - this
        """
        ...


    def sub(self, x: float, y: float, dest: "Vector2f") -> "Vector2f":
        ...


    def dot(self, v: "Vector2fc") -> float:
        ...


    def angle(self, v: "Vector2fc") -> float:
        ...


    def lengthSquared(self) -> float:
        ...


    @staticmethod
    def lengthSquared(x: float, y: float) -> float:
        """
        Get the length squared of a 2-dimensional single-precision vector.

    Author(s)
        - F. Neurath

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
    def length(x: float, y: float) -> float:
        """
        Get the length of a 2-dimensional single-precision vector.

    Author(s)
        - F. Neurath

        Arguments
        - x: The vector's x component
        - y: The vector's y component

        Returns
        - the length of the given vector
        """
        ...


    def distance(self, v: "Vector2fc") -> float:
        ...


    def distanceSquared(self, v: "Vector2fc") -> float:
        ...


    def distance(self, x: float, y: float) -> float:
        ...


    def distanceSquared(self, x: float, y: float) -> float:
        ...


    @staticmethod
    def distance(x1: float, y1: float, x2: float, y2: float) -> float:
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
    def distanceSquared(x1: float, y1: float, x2: float, y2: float) -> float:
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


    def normalize(self) -> "Vector2f":
        """
        Normalize this vector.

        Returns
        - this
        """
        ...


    def normalize(self, dest: "Vector2f") -> "Vector2f":
        ...


    def normalize(self, length: float) -> "Vector2f":
        """
        Scale this vector to have the given length.

        Arguments
        - length: the desired length

        Returns
        - this
        """
        ...


    def normalize(self, length: float, dest: "Vector2f") -> "Vector2f":
        ...


    def add(self, v: "Vector2fc") -> "Vector2f":
        """
        Add `v` to this vector.

        Arguments
        - v: the vector to add

        Returns
        - this
        """
        ...


    def add(self, v: "Vector2fc", dest: "Vector2f") -> "Vector2f":
        ...


    def add(self, x: float, y: float) -> "Vector2f":
        """
        Increment the components of this vector by the given values.

        Arguments
        - x: the x component to add
        - y: the y component to add

        Returns
        - this
        """
        ...


    def add(self, x: float, y: float, dest: "Vector2f") -> "Vector2f":
        ...


    def zero(self) -> "Vector2f":
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


    def negate(self) -> "Vector2f":
        """
        Negate this vector.

        Returns
        - this
        """
        ...


    def negate(self, dest: "Vector2f") -> "Vector2f":
        ...


    def mul(self, scalar: float) -> "Vector2f":
        """
        Multiply the components of this vector by the given scalar.

        Arguments
        - scalar: the value to multiply this vector's components by

        Returns
        - this
        """
        ...


    def mul(self, scalar: float, dest: "Vector2f") -> "Vector2f":
        ...


    def mul(self, x: float, y: float) -> "Vector2f":
        """
        Multiply the components of this Vector2f by the given scalar values and store the result in `this`.

        Arguments
        - x: the x component to multiply this vector by
        - y: the y component to multiply this vector by

        Returns
        - this
        """
        ...


    def mul(self, x: float, y: float, dest: "Vector2f") -> "Vector2f":
        ...


    def mul(self, v: "Vector2fc") -> "Vector2f":
        """
        Multiply this Vector2f component-wise by another Vector2f.

        Arguments
        - v: the vector to multiply by

        Returns
        - this
        """
        ...


    def mul(self, v: "Vector2fc", dest: "Vector2f") -> "Vector2f":
        ...


    def div(self, v: "Vector2fc") -> "Vector2f":
        """
        Divide this Vector2f component-wise by another Vector2fc.

        Arguments
        - v: the vector to divide by

        Returns
        - this
        """
        ...


    def div(self, v: "Vector2fc", dest: "Vector2f") -> "Vector2f":
        ...


    def div(self, scalar: float) -> "Vector2f":
        """
        Divide all components of this Vector2f by the given scalar
        value.

        Arguments
        - scalar: the scalar to divide by

        Returns
        - this
        """
        ...


    def div(self, scalar: float, dest: "Vector2f") -> "Vector2f":
        ...


    def div(self, x: float, y: float) -> "Vector2f":
        """
        Divide the components of this Vector2f by the given scalar values and store the result in `this`.

        Arguments
        - x: the x component to divide this vector by
        - y: the y component to divide this vector by

        Returns
        - this
        """
        ...


    def div(self, x: float, y: float, dest: "Vector2f") -> "Vector2f":
        ...


    def mul(self, mat: "Matrix2fc") -> "Vector2f":
        """
        Multiply the given matrix with this Vector2f and store the result in `this`.

        Arguments
        - mat: the matrix

        Returns
        - this
        """
        ...


    def mul(self, mat: "Matrix2fc", dest: "Vector2f") -> "Vector2f":
        ...


    def mul(self, mat: "Matrix2dc") -> "Vector2f":
        """
        Multiply the given matrix with this Vector2f and store the result in `this`.

        Arguments
        - mat: the matrix

        Returns
        - this
        """
        ...


    def mul(self, mat: "Matrix2dc", dest: "Vector2f") -> "Vector2f":
        ...


    def mulTranspose(self, mat: "Matrix2fc") -> "Vector2f":
        """
        Multiply the transpose of the given matrix with this Vector2f store the result in `this`.

        Arguments
        - mat: the matrix

        Returns
        - this
        """
        ...


    def mulTranspose(self, mat: "Matrix2fc", dest: "Vector2f") -> "Vector2f":
        ...


    def mulPosition(self, mat: "Matrix3x2fc") -> "Vector2f":
        """
        Multiply the given 3x2 matrix `mat` with `this`.
        
        This method assumes the `z` component of `this` to be `1.0`.

        Arguments
        - mat: the matrix to multiply this vector by

        Returns
        - this
        """
        ...


    def mulPosition(self, mat: "Matrix3x2fc", dest: "Vector2f") -> "Vector2f":
        ...


    def mulDirection(self, mat: "Matrix3x2fc") -> "Vector2f":
        """
        Multiply the given 3x2 matrix `mat` with `this`.
        
        This method assumes the `z` component of `this` to be `0.0`.

        Arguments
        - mat: the matrix to multiply this vector by

        Returns
        - this
        """
        ...


    def mulDirection(self, mat: "Matrix3x2fc", dest: "Vector2f") -> "Vector2f":
        ...


    def lerp(self, other: "Vector2fc", t: float) -> "Vector2f":
        """
        Linearly interpolate `this` and `other` using the given interpolation factor `t`
        and store the result in `this`.
        
        If `t` is `0.0` then the result is `this`. If the interpolation factor is `1.0`
        then the result is `other`.

        Arguments
        - other: the other vector
        - t: the interpolation factor between 0.0 and 1.0

        Returns
        - this
        """
        ...


    def lerp(self, other: "Vector2fc", t: float, dest: "Vector2f") -> "Vector2f":
        ...


    def hashCode(self) -> int:
        ...


    def equals(self, obj: "Object") -> bool:
        ...


    def equals(self, v: "Vector2fc", delta: float) -> bool:
        ...


    def equals(self, x: float, y: float) -> bool:
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


    def fma(self, a: "Vector2fc", b: "Vector2fc") -> "Vector2f":
        """
        Add the component-wise multiplication of `a * b` to this vector.

        Arguments
        - a: the first multiplicand
        - b: the second multiplicand

        Returns
        - this
        """
        ...


    def fma(self, a: float, b: "Vector2fc") -> "Vector2f":
        """
        Add the component-wise multiplication of `a * b` to this vector.

        Arguments
        - a: the first multiplicand
        - b: the second multiplicand

        Returns
        - this
        """
        ...


    def fma(self, a: "Vector2fc", b: "Vector2fc", dest: "Vector2f") -> "Vector2f":
        ...


    def fma(self, a: float, b: "Vector2fc", dest: "Vector2f") -> "Vector2f":
        ...


    def min(self, v: "Vector2fc") -> "Vector2f":
        """
        Set the components of this vector to be the component-wise minimum of this and the other vector.

        Arguments
        - v: the other vector

        Returns
        - this
        """
        ...


    def min(self, v: "Vector2fc", dest: "Vector2f") -> "Vector2f":
        ...


    def max(self, v: "Vector2fc") -> "Vector2f":
        """
        Set the components of this vector to be the component-wise maximum of this and the other vector.

        Arguments
        - v: the other vector

        Returns
        - this
        """
        ...


    def max(self, v: "Vector2fc", dest: "Vector2f") -> "Vector2f":
        ...


    def maxComponent(self) -> int:
        ...


    def minComponent(self) -> int:
        ...


    def floor(self) -> "Vector2f":
        """
        Set each component of this vector to the largest (closest to positive
        infinity) `float` value that is less than or equal to that
        component and is equal to a mathematical integer.

        Returns
        - this
        """
        ...


    def floor(self, dest: "Vector2f") -> "Vector2f":
        ...


    def ceil(self) -> "Vector2f":
        """
        Ceil each component of this vector

        Returns
        - this
        """
        ...


    def ceil(self, dest: "Vector2f") -> "Vector2f":
        ...


    def round(self) -> "Vector2f":
        """
        Set each component of this vector to the closest float that is equal to
        a mathematical integer, with ties rounding to positive infinity.

        Returns
        - this
        """
        ...


    def round(self, dest: "Vector2f") -> "Vector2f":
        ...


    def isFinite(self) -> bool:
        ...


    def absolute(self) -> "Vector2f":
        """
        Set `this` vector's components to their respective absolute values.

        Returns
        - this
        """
        ...


    def absolute(self, dest: "Vector2f") -> "Vector2f":
        ...


    def clone(self) -> "Object":
        ...
