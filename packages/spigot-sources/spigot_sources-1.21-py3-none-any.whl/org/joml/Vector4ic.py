"""
Python module generated from Java source file org.joml.Vector4ic

Java source file obtained from artifact joml version 1.10.5

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.joml import *
from typing import Any, Callable, Iterable, Tuple


class Vector4ic:
    """
    Interface to a read-only view of a 4-dimensional vector of integers.

    Author(s)
    - Kai Burjack
    """

    def x(self) -> int:
        """
        Returns
        - the value of the x component
        """
        ...


    def y(self) -> int:
        """
        Returns
        - the value of the y component
        """
        ...


    def z(self) -> int:
        """
        Returns
        - the value of the z component
        """
        ...


    def w(self) -> int:
        """
        Returns
        - the value of the w component
        """
        ...


    def get(self, buffer: "IntBuffer") -> "IntBuffer":
        """
        Store this vector into the supplied IntBuffer at the current
        buffer IntBuffer.position() position.
        
        This method will not increment the position of the given IntBuffer.
        
        In order to specify the offset into the IntBuffer at which the vector is
        stored, use .get(int, IntBuffer), taking the absolute position as
        parameter.

        Arguments
        - buffer: will receive the values of this vector in `x, y, z, w` order

        Returns
        - the passed in buffer

        See
        - .get(int, IntBuffer)
        """
        ...


    def get(self, index: int, buffer: "IntBuffer") -> "IntBuffer":
        """
        Store this vector into the supplied IntBuffer starting at the
        specified absolute buffer position/index.
        
        This method will not increment the position of the given IntBuffer.

        Arguments
        - index: the absolute position into the IntBuffer
        - buffer: will receive the values of this vector in `x, y, z, w` order

        Returns
        - the passed in buffer
        """
        ...


    def get(self, buffer: "ByteBuffer") -> "ByteBuffer":
        """
        Store this vector into the supplied ByteBuffer at the current
        buffer ByteBuffer.position() position.
        
        This method will not increment the position of the given ByteBuffer.
        
        In order to specify the offset into the ByteBuffer at which the vector is
        stored, use .get(int, ByteBuffer), taking the absolute position
        as parameter.

        Arguments
        - buffer: will receive the values of this vector in `x, y, z, w` order

        Returns
        - the passed in buffer

        See
        - .get(int, ByteBuffer)
        """
        ...


    def get(self, index: int, buffer: "ByteBuffer") -> "ByteBuffer":
        """
        Store this vector into the supplied ByteBuffer starting at the
        specified absolute buffer position/index.
        
        This method will not increment the position of the given ByteBuffer.

        Arguments
        - index: the absolute position into the ByteBuffer
        - buffer: will receive the values of this vector in `x, y, z, w` order

        Returns
        - the passed in buffer
        """
        ...


    def getToAddress(self, address: int) -> "Vector4ic":
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


    def sub(self, v: "Vector4ic", dest: "Vector4i") -> "Vector4i":
        """
        Subtract the supplied vector from this one and store the result in
        `dest`.

        Arguments
        - v: the vector to subtract from `this`
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def sub(self, x: int, y: int, z: int, w: int, dest: "Vector4i") -> "Vector4i":
        """
        Subtract `(x, y, z, w)` from this and store the result in
        `dest`.

        Arguments
        - x: the x component to subtract
        - y: the y component to subtract
        - z: the z component to subtract
        - w: the w component to subtract
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def add(self, v: "Vector4ic", dest: "Vector4i") -> "Vector4i":
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


    def add(self, x: int, y: int, z: int, w: int, dest: "Vector4i") -> "Vector4i":
        """
        Increment the components of this vector by the given values and store the
        result in `dest`.

        Arguments
        - x: the x component to add
        - y: the y component to add
        - z: the z component to add
        - w: the w component to add
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mul(self, v: "Vector4ic", dest: "Vector4i") -> "Vector4i":
        """
        Multiply this Vector4i component-wise by another Vector4ic and store the
        result in `dest`.

        Arguments
        - v: the other vector
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def div(self, v: "Vector4ic", dest: "Vector4i") -> "Vector4i":
        """
        Divide this Vector4i component-wise by another Vector4ic and store the
        result in `dest`.

        Arguments
        - v: the vector to divide by
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mul(self, scalar: int, dest: "Vector4i") -> "Vector4i":
        """
        Multiply all components of this Vector4i by the given scalar
        value and store the result in `dest`.

        Arguments
        - scalar: the scalar to multiply by
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def div(self, scalar: float, dest: "Vector4i") -> "Vector4i":
        """
        Divide all components of this Vector4i by the given scalar value
        and store the result in `dest`.

        Arguments
        - scalar: the scalar to divide by
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def div(self, scalar: int, dest: "Vector4i") -> "Vector4i":
        """
        Divide all components of this Vector4i by the given scalar value
        and store the result in `dest`.

        Arguments
        - scalar: the scalar to divide by
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def lengthSquared(self) -> int:
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


    def distance(self, v: "Vector4ic") -> float:
        """
        Return the distance between this Vector and `v`.

        Arguments
        - v: the other vector

        Returns
        - the distance
        """
        ...


    def distance(self, x: int, y: int, z: int, w: int) -> float:
        """
        Return the distance between `this` vector and `(x, y, z, w)`.

        Arguments
        - x: the x component of the other vector
        - y: the y component of the other vector
        - z: the z component of the other vector
        - w: the w component of the other vector

        Returns
        - the euclidean distance
        """
        ...


    def gridDistance(self, v: "Vector4ic") -> int:
        """
        Return the grid distance in between (aka 1-Norm, Minkowski or Manhattan distance)
        `(x, y)`.

        Arguments
        - v: the other vector

        Returns
        - the grid distance
        """
        ...


    def gridDistance(self, x: int, y: int, z: int, w: int) -> int:
        """
        Return the grid distance in between (aka 1-Norm, Minkowski or Manhattan distance)
        `(x, y)`.

        Arguments
        - x: the x component of the other vector
        - y: the y component of the other vector
        - z: the z component of the other vector
        - w: the w component of the other vector

        Returns
        - the grid distance
        """
        ...


    def distanceSquared(self, v: "Vector4ic") -> int:
        """
        Return the square of the distance between this vector and `v`.

        Arguments
        - v: the other vector

        Returns
        - the squared of the distance
        """
        ...


    def distanceSquared(self, x: int, y: int, z: int, w: int) -> int:
        """
        Return the square of the distance between `this` vector and
        `(x, y, z, w)`.

        Arguments
        - x: the x component of the other vector
        - y: the y component of the other vector
        - z: the z component of the other vector
        - w: the w component of the other vector

        Returns
        - the square of the distance
        """
        ...


    def dot(self, v: "Vector4ic") -> int:
        """
        Compute the dot product (inner product) of this vector and `v`.

        Arguments
        - v: the other vector

        Returns
        - the dot product
        """
        ...


    def negate(self, dest: "Vector4i") -> "Vector4i":
        """
        Negate this vector and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def min(self, v: "Vector4ic", dest: "Vector4i") -> "Vector4i":
        """
        Set the components of `dest` to be the component-wise minimum of this and the other vector.

        Arguments
        - v: the other vector
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def max(self, v: "Vector4ic", dest: "Vector4i") -> "Vector4i":
        """
        Set the components of `dest` to be the component-wise maximum of this and the other vector.

        Arguments
        - v: the other vector
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def get(self, component: int) -> int:
        """
        Get the value of the specified component of this vector.

        Arguments
        - component: the component, within `[0..3]`

        Returns
        - the value

        Raises
        - IllegalArgumentException: if `component` is not within `[0..3]`
        """
        ...


    def maxComponent(self) -> int:
        """
        Determine the component with the biggest absolute value.

        Returns
        - the component index, within `[0..3]`
        """
        ...


    def minComponent(self) -> int:
        """
        Determine the component with the smallest (towards zero) absolute value.

        Returns
        - the component index, within `[0..3]`
        """
        ...


    def absolute(self, dest: "Vector4i") -> "Vector4i":
        """
        Compute the absolute of each of this vector's components
        and store the result into `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def equals(self, x: int, y: int, z: int, w: int) -> bool:
        """
        Compare the vector components of `this` vector with the given `(x, y, z, w)`
        and return whether all of them are equal.

        Arguments
        - x: the x component to compare to
        - y: the y component to compare to
        - z: the z component to compare to
        - w: the w component to compare to

        Returns
        - `True` if all the vector components are equal
        """
        ...
