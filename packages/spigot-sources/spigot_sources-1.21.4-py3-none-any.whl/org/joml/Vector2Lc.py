"""
Python module generated from Java source file org.joml.Vector2Lc

Java source file obtained from artifact joml version 1.10.8

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.joml import *
from typing import Any, Callable, Iterable, Tuple


class Vector2Lc:
    """
    Interface to a read-only view of a 2-dimensional vector of integers.

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


    def get(self, buffer: "ByteBuffer") -> "ByteBuffer":
        """
        Store this vector into the supplied ByteBuffer at the current
        buffer ByteBuffer.position() position.
        
        This method will not increment the position of the given ByteBuffer.
        
        In order to specify the offset into the ByteBuffer at which the vector is
        stored, use .get(int, ByteBuffer), taking the absolute position
        as parameter.

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
        Store this vector into the supplied ByteBuffer starting at the
        specified absolute buffer position/index.
        
        This method will not increment the position of the given ByteBuffer.

        Arguments
        - index: the absolute position into the ByteBuffer
        - buffer: will receive the values of this vector in `x, y` order

        Returns
        - the passed in buffer
        """
        ...


    def get(self, buffer: "LongBuffer") -> "LongBuffer":
        """
        Store this vector into the supplied LongBuffer at the current
        buffer LongBuffer.position() position.
        
        This method will not increment the position of the given IntBuffer.
        
        In order to specify the offset into the IntBuffer at which the vector is
        stored, use .get(int, LongBuffer), taking the absolute position as
        parameter.

        Arguments
        - buffer: will receive the values of this vector in `x, y` order

        Returns
        - the passed in buffer

        See
        - .get(int, LongBuffer)
        """
        ...


    def get(self, index: int, buffer: "LongBuffer") -> "LongBuffer":
        """
        Store this vector into the supplied LongBuffer starting at the
        specified absolute buffer position/index.
        
        This method will not increment the position of the given IntBuffer.

        Arguments
        - index: the absolute position into the IntBuffer
        - buffer: will receive the values of this vector in `x, y` order

        Returns
        - the passed in buffer
        """
        ...


    def getToAddress(self, address: int) -> "Vector2Lc":
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


    def sub(self, v: "Vector2Lc", dest: "Vector2L") -> "Vector2L":
        """
        Subtract the supplied vector from this one and store the result in
        `dest`.

        Arguments
        - v: the vector to subtract
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def sub(self, x: int, y: int, dest: "Vector2L") -> "Vector2L":
        """
        Decrement the components of this vector by the given values and store the
        result in `dest`.

        Arguments
        - x: the x component to subtract
        - y: the y component to subtract
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


    def distance(self, v: "Vector2Lc") -> float:
        """
        Return the distance between this Vector and `v`.

        Arguments
        - v: the other vector

        Returns
        - the distance
        """
        ...


    def distance(self, x: int, y: int) -> float:
        """
        Return the distance between `this` vector and `(x, y)`.

        Arguments
        - x: the x component of the other vector
        - y: the y component of the other vector

        Returns
        - the euclidean distance
        """
        ...


    def distanceSquared(self, v: "Vector2Lc") -> int:
        """
        Return the square of the distance between this vector and `v`.

        Arguments
        - v: the other vector

        Returns
        - the squared of the distance
        """
        ...


    def distanceSquared(self, x: int, y: int) -> int:
        """
        Return the square of the distance between `this` vector and
        `(x, y)`.

        Arguments
        - x: the x component of the other vector
        - y: the y component of the other vector

        Returns
        - the square of the distance
        """
        ...


    def gridDistance(self, v: "Vector2Lc") -> int:
        """
        Return the grid distance in between (aka 1-Norm, Minkowski or Manhattan distance)
        `(x, y)`.

        Arguments
        - v: the other vector

        Returns
        - the grid distance
        """
        ...


    def gridDistance(self, x: int, y: int) -> int:
        """
        Return the grid distance in between (aka 1-Norm, Minkowski or Manhattan distance)
        `(x, y)`.

        Arguments
        - x: the x component of the other vector
        - y: the y component of the other vector

        Returns
        - the grid distance
        """
        ...


    def add(self, v: "Vector2Lc", dest: "Vector2L") -> "Vector2L":
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


    def add(self, x: int, y: int, dest: "Vector2L") -> "Vector2L":
        """
        Increment the components of this vector by the given values and store the
        result in `dest`.

        Arguments
        - x: the x component to add
        - y: the y component to add
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mul(self, scalar: int, dest: "Vector2L") -> "Vector2L":
        """
        Multiply all components of this Vector2Lc by the given scalar
        value and store the result in `dest`.

        Arguments
        - scalar: the scalar to multiply this vector by
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mul(self, v: "Vector2Lc", dest: "Vector2L") -> "Vector2L":
        """
        Multiply the supplied vector by this one and store the result in
        `dest`.

        Arguments
        - v: the vector to multiply
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mul(self, x: int, y: int, dest: "Vector2L") -> "Vector2L":
        """
        Multiply the components of this vector by the given values and store the
        result in `dest`.

        Arguments
        - x: the x component to multiply
        - y: the y component to multiply
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def div(self, scalar: float, dest: "Vector2L") -> "Vector2L":
        """
        Divide all components of this vector by the given scalar value
        and store the result in `dest`.

        Arguments
        - scalar: the scalar to divide by
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def div(self, scalar: int, dest: "Vector2L") -> "Vector2L":
        """
        Divide all components of this vector by the given scalar value
        and store the result in `dest`.

        Arguments
        - scalar: the scalar to divide by
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def negate(self, dest: "Vector2L") -> "Vector2L":
        """
        Negate this vector and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def min(self, v: "Vector2Lc", dest: "Vector2L") -> "Vector2L":
        """
        Set the components of `dest` to be the component-wise minimum of this and the other vector.

        Arguments
        - v: the other vector
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def max(self, v: "Vector2Lc", dest: "Vector2L") -> "Vector2L":
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


    def absolute(self, dest: "Vector2L") -> "Vector2L":
        """
        Compute the absolute of each of this vector's components
        and store the result into `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def get(self, component: int) -> int:
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


    def equals(self, x: int, y: int) -> bool:
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
