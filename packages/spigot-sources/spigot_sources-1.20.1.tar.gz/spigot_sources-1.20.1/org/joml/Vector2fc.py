"""
Python module generated from Java source file org.joml.Vector2fc

Java source file obtained from artifact joml version 1.10.5

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util import *
from org.joml import *
from typing import Any, Callable, Iterable, Tuple


class Vector2fc:
    """
    Interface to a read-only view of a 2-dimensional vector of single-precision floats.

    Author(s)
    - Kai Burjack
    """

    def x(self) -> float:
        """
        Returns
        - the value of the x component
        """
        ...


    def y(self) -> float:
        """
        Returns
        - the value of the y component
        """
        ...


    def get(self, buffer: "ByteBuffer") -> "ByteBuffer":
        """
        Store this vector into the supplied ByteBuffer at the current
        buffer ByteBuffer.position() position.
        
        This method will not increment the position of the given ByteBuffer.
        
        In order to specify the offset into the ByteBuffer at which
        the vector is stored, use .get(int, ByteBuffer), taking
        the absolute position as parameter.

        Arguments
        - buffer: will receive the values of this vector in `x, y` order

        Returns
        - the passed in buffer

        See
        - .get(int, ByteBuffer)
        """
        ...


    def get(self, index: int, buffer: "ByteBuffer") -> "ByteBuffer":
        """
        Store this vector into the supplied ByteBuffer starting at the specified
        absolute buffer position/index.
        
        This method will not increment the position of the given ByteBuffer.

        Arguments
        - index: the absolute position into the ByteBuffer
        - buffer: will receive the values of this vector in `x, y` order

        Returns
        - the passed in buffer
        """
        ...


    def get(self, buffer: "FloatBuffer") -> "FloatBuffer":
        """
        Store this vector into the supplied FloatBuffer at the current
        buffer FloatBuffer.position() position.
        
        This method will not increment the position of the given FloatBuffer.
        
        In order to specify the offset into the FloatBuffer at which
        the vector is stored, use .get(int, FloatBuffer), taking
        the absolute position as parameter.

        Arguments
        - buffer: will receive the values of this vector in `x, y` order

        Returns
        - the passed in buffer

        See
        - .get(int, FloatBuffer)
        """
        ...


    def get(self, index: int, buffer: "FloatBuffer") -> "FloatBuffer":
        """
        Store this vector into the supplied FloatBuffer starting at the specified
        absolute buffer position/index.
        
        This method will not increment the position of the given FloatBuffer.

        Arguments
        - index: the absolute position into the FloatBuffer
        - buffer: will receive the values of this vector in `x, y` order

        Returns
        - the passed in buffer
        """
        ...


    def getToAddress(self, address: int) -> "Vector2fc":
        """
        Store this vector at the given off-heap memory address.
        
        This method will throw an UnsupportedOperationException when JOML is used with `-Djoml.nounsafe`.
        
        *This method is unsafe as it can result in a crash of the JVM process when the specified address range does not belong to this process.*

        Arguments
        - address: the off-heap address where to store this vector

        Returns
        - this
        """
        ...


    def sub(self, v: "Vector2fc", dest: "Vector2f") -> "Vector2f":
        """
        Subtract `v` from `this` vector and store the result in `dest`.

        Arguments
        - v: the vector to subtract
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def sub(self, x: float, y: float, dest: "Vector2f") -> "Vector2f":
        """
        Subtract `(x, y)` from this vector and store the result in `dest`.

        Arguments
        - x: the x component to subtract
        - y: the y component to subtract
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def dot(self, v: "Vector2fc") -> float:
        """
        Return the dot product of this vector and `v`.

        Arguments
        - v: the other vector

        Returns
        - the dot product
        """
        ...


    def angle(self, v: "Vector2fc") -> float:
        """
        Return the angle between this vector and the supplied vector.

        Arguments
        - v: the other vector

        Returns
        - the angle, in radians
        """
        ...


    def lengthSquared(self) -> float:
        """
        Return the length squared of this vector.

        Returns
        - the length squared
        """
        ...


    def length(self) -> float:
        """
        Return the length of this vector.

        Returns
        - the length
        """
        ...


    def distance(self, v: "Vector2fc") -> float:
        """
        Return the distance between this and `v`.

        Arguments
        - v: the other vector

        Returns
        - the distance
        """
        ...


    def distanceSquared(self, v: "Vector2fc") -> float:
        """
        Return the distance squared between this and `v`.

        Arguments
        - v: the other vector

        Returns
        - the distance squared
        """
        ...


    def distance(self, x: float, y: float) -> float:
        """
        Return the distance between `this` vector and `(x, y)`.

        Arguments
        - x: the x component of the other vector
        - y: the y component of the other vector

        Returns
        - the euclidean distance
        """
        ...


    def distanceSquared(self, x: float, y: float) -> float:
        """
        Return the distance squared between `this` vector and `(x, y)`.

        Arguments
        - x: the x component of the other vector
        - y: the y component of the other vector

        Returns
        - the euclidean distance squared
        """
        ...


    def normalize(self, dest: "Vector2f") -> "Vector2f":
        """
        Normalize this vector and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def normalize(self, length: float, dest: "Vector2f") -> "Vector2f":
        """
        Scale this vector to have the given length and store the result in `dest`.

        Arguments
        - length: the desired length
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def add(self, v: "Vector2fc", dest: "Vector2f") -> "Vector2f":
        """
        Add the supplied vector to this one and store the result in
        `dest`.

        Arguments
        - v: the vector to add
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def add(self, x: float, y: float, dest: "Vector2f") -> "Vector2f":
        """
        Increment the components of this vector by the given values and store the result in `dest`.

        Arguments
        - x: the x component to add
        - y: the y component to add
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def negate(self, dest: "Vector2f") -> "Vector2f":
        """
        Negate this vector and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mul(self, scalar: float, dest: "Vector2f") -> "Vector2f":
        """
        Multiply the components of this vector by the given scalar and store the result in `dest`.

        Arguments
        - scalar: the value to multiply this vector's components by
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mul(self, x: float, y: float, dest: "Vector2f") -> "Vector2f":
        """
        Multiply the components of this Vector2f by the given scalar values and store the result in `dest`.

        Arguments
        - x: the x component to multiply this vector by
        - y: the y component to multiply this vector by
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mul(self, v: "Vector2fc", dest: "Vector2f") -> "Vector2f":
        """
        Multiply this Vector2f component-wise by another Vector2f and store the result in `dest`.

        Arguments
        - v: the vector to multiply by
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def div(self, scalar: float, dest: "Vector2f") -> "Vector2f":
        """
        Divide all components of this Vector2f by the given scalar
        value and store the result in `dest`.

        Arguments
        - scalar: the scalar to divide by
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def div(self, v: "Vector2fc", dest: "Vector2f") -> "Vector2f":
        """
        Divide this Vector2f component-wise by another Vector2fc
        and store the result in `dest`.

        Arguments
        - v: the vector to divide by
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def div(self, x: float, y: float, dest: "Vector2f") -> "Vector2f":
        """
        Divide the components of this Vector2f by the given scalar values and store the result in `dest`.

        Arguments
        - x: the x component to divide this vector by
        - y: the y component to divide this vector by
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mul(self, mat: "Matrix2fc", dest: "Vector2f") -> "Vector2f":
        """
        Multiply the given matrix with this Vector2f and store the result in `dest`.

        Arguments
        - mat: the matrix
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mul(self, mat: "Matrix2dc", dest: "Vector2f") -> "Vector2f":
        """
        Multiply the given matrix with this Vector2f and store the result in `dest`.

        Arguments
        - mat: the matrix
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mulTranspose(self, mat: "Matrix2fc", dest: "Vector2f") -> "Vector2f":
        """
        Multiply the transpose of the given matrix with this Vector3f and store the result in `dest`.

        Arguments
        - mat: the matrix
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mulPosition(self, mat: "Matrix3x2fc", dest: "Vector2f") -> "Vector2f":
        """
        Multiply the given 3x2 matrix `mat` with `this` and store the
        result in `dest`.
        
        This method assumes the `z` component of `this` to be `1.0`.

        Arguments
        - mat: the matrix to multiply this vector by
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mulDirection(self, mat: "Matrix3x2fc", dest: "Vector2f") -> "Vector2f":
        """
        Multiply the given 3x2 matrix `mat` with `this` and store the
        result in `dest`.
        
        This method assumes the `z` component of `this` to be `0.0`.

        Arguments
        - mat: the matrix to multiply this vector by
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def lerp(self, other: "Vector2fc", t: float, dest: "Vector2f") -> "Vector2f":
        """
        Linearly interpolate `this` and `other` using the given interpolation factor `t`
        and store the result in `dest`.
        
        If `t` is `0.0` then the result is `this`. If the interpolation factor is `1.0`
        then the result is `other`.

        Arguments
        - other: the other vector
        - t: the interpolation factor between 0.0 and 1.0
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def fma(self, a: "Vector2fc", b: "Vector2fc", dest: "Vector2f") -> "Vector2f":
        """
        Add the component-wise multiplication of `a * b` to this vector
        and store the result in `dest`.

        Arguments
        - a: the first multiplicand
        - b: the second multiplicand
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def fma(self, a: float, b: "Vector2fc", dest: "Vector2f") -> "Vector2f":
        """
        Add the component-wise multiplication of `a * b` to this vector
        and store the result in `dest`.

        Arguments
        - a: the first multiplicand
        - b: the second multiplicand
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def min(self, v: "Vector2fc", dest: "Vector2f") -> "Vector2f":
        """
        Set the components of `dest` to be the component-wise minimum of this and the other vector.

        Arguments
        - v: the other vector
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def max(self, v: "Vector2fc", dest: "Vector2f") -> "Vector2f":
        """
        Set the components of `dest` to be the component-wise maximum of this and the other vector.

        Arguments
        - v: the other vector
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def maxComponent(self) -> int:
        """
        Determine the component with the biggest absolute value.

        Returns
        - the component index, within `[0..1]`
        """
        ...


    def minComponent(self) -> int:
        """
        Determine the component with the smallest (towards zero) absolute value.

        Returns
        - the component index, within `[0..1]`
        """
        ...


    def get(self, component: int) -> float:
        """
        Get the value of the specified component of this vector.

        Arguments
        - component: the component, within `[0..1]`

        Returns
        - the value

        Raises
        - IllegalArgumentException: if `component` is not within `[0..1]`
        """
        ...


    def get(self, mode: int, dest: "Vector2i") -> "Vector2i":
        """
        Set the components of the given vector `dest` to those of `this` vector
        using the given RoundingMode.

        Arguments
        - mode: the RoundingMode to use
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def get(self, dest: "Vector2f") -> "Vector2f":
        """
        Set the components of the given vector `dest` to those of `this` vector.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def get(self, dest: "Vector2d") -> "Vector2d":
        """
        Set the components of the given vector `dest` to those of `this` vector.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def floor(self, dest: "Vector2f") -> "Vector2f":
        """
        Compute for each component of this vector the largest (closest to positive
        infinity) `float` value that is less than or equal to that
        component and is equal to a mathematical integer and store the result in
        `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def ceil(self, dest: "Vector2f") -> "Vector2f":
        """
        Compute for each component of this vector the smallest (closest to negative
        infinity) `float` value that is greater than or equal to that
        component and is equal to a mathematical integer and store the result in
        `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def round(self, dest: "Vector2f") -> "Vector2f":
        """
        Compute for each component of this vector the closest float that is equal to
        a mathematical integer, with ties rounding to positive infinity and store
        the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def isFinite(self) -> bool:
        """
        Determine whether all components are finite floating-point values, that
        is, they are not Float.isNaN() NaN and not
        Float.isInfinite() infinity.

        Returns
        - `True` if all components are finite floating-point values;
                `False` otherwise
        """
        ...


    def absolute(self, dest: "Vector2f") -> "Vector2f":
        """
        Compute the absolute of each of this vector's components
        and store the result into `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def equals(self, v: "Vector2fc", delta: float) -> bool:
        """
        Compare the vector components of `this` vector with the given vector using the given `delta`
        and return whether all of them are equal within a maximum difference of `delta`.
        
        Please note that this method is not used by any data structure such as ArrayList HashSet or HashMap
        and their operations, such as ArrayList.contains(Object) or HashSet.remove(Object), since those
        data structures only use the Object.equals(Object) and Object.hashCode() methods.

        Arguments
        - v: the other vector
        - delta: the allowed maximum difference

        Returns
        - `True` whether all of the vector components are equal; `False` otherwise
        """
        ...


    def equals(self, x: float, y: float) -> bool:
        """
        Compare the vector components of `this` vector with the given `(x, y)`
        and return whether all of them are equal.

        Arguments
        - x: the x component to compare to
        - y: the y component to compare to

        Returns
        - `True` if all the vector components are equal
        """
        ...
