"""
Python module generated from Java source file org.joml.Vector4dc

Java source file obtained from artifact joml version 1.10.5

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util import *
from org.joml import *
from typing import Any, Callable, Iterable, Tuple


class Vector4dc:
    """
    Interface to a read-only view of a 4-dimensional vector of double-precision floats.

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


    def z(self) -> float:
        """
        Returns
        - the value of the z component
        """
        ...


    def w(self) -> float:
        """
        Returns
        - the value of the w component
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
        - buffer: will receive the values of this vector in `x, y, z, w` order

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
        - buffer: will receive the values of this vector in `x, y, z, w` order

        Returns
        - the passed in buffer
        """
        ...


    def get(self, buffer: "DoubleBuffer") -> "DoubleBuffer":
        """
        Store this vector into the supplied DoubleBuffer at the current
        buffer DoubleBuffer.position() position.
        
        This method will not increment the position of the given DoubleBuffer.
        
        In order to specify the offset into the DoubleBuffer at which
        the vector is stored, use .get(int, DoubleBuffer), taking
        the absolute position as parameter.

        Arguments
        - buffer: will receive the values of this vector in `x, y, z, w` order

        Returns
        - the passed in buffer

        See
        - .get(int, DoubleBuffer)
        """
        ...


    def get(self, index: int, buffer: "DoubleBuffer") -> "DoubleBuffer":
        """
        Store this vector into the supplied DoubleBuffer starting at the specified
        absolute buffer position/index.
        
        This method will not increment the position of the given DoubleBuffer.

        Arguments
        - index: the absolute position into the DoubleBuffer
        - buffer: will receive the values of this vector in `x, y, z, w` order

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
        
        Please note that due to this vector storing double values those values will potentially
        lose precision when they are converted to float values before being put into the given FloatBuffer.

        Arguments
        - buffer: will receive the values of this vector in `x, y, z, w` order

        Returns
        - the passed in buffer

        See
        - .get(int, DoubleBuffer)
        """
        ...


    def get(self, index: int, buffer: "FloatBuffer") -> "FloatBuffer":
        """
        Store this vector into the supplied FloatBuffer starting at the specified
        absolute buffer position/index.
        
        This method will not increment the position of the given FloatBuffer.
        
        Please note that due to this vector storing double values those values will potentially
        lose precision when they are converted to float values before being put into the given FloatBuffer.

        Arguments
        - index: the absolute position into the FloatBuffer
        - buffer: will receive the values of this vector in `x, y, z, w` order

        Returns
        - the passed in buffer
        """
        ...


    def getf(self, buffer: "ByteBuffer") -> "ByteBuffer":
        """
        Store this vector into the supplied ByteBuffer at the current
        buffer ByteBuffer.position() position.
        
        This method will not increment the position of the given ByteBuffer.
        
        In order to specify the offset into the ByteBuffer at which
        the vector is stored, use .get(int, ByteBuffer), taking
        the absolute position as parameter.
        
        Please note that due to this vector storing double values those values will potentially
        lose precision when they are converted to float values before being put into the given ByteBuffer.

        Arguments
        - buffer: will receive the values of this vector in `x, y, z, w` order

        Returns
        - the passed in buffer

        See
        - .get(int, ByteBuffer)
        """
        ...


    def getf(self, index: int, buffer: "ByteBuffer") -> "ByteBuffer":
        """
        Store this vector into the supplied ByteBuffer starting at the specified
        absolute buffer position/index.
        
        This method will not increment the position of the given ByteBuffer.
        
        Please note that due to this vector storing double values those values will potentially
        lose precision when they are converted to float values before being put into the given ByteBuffer.

        Arguments
        - index: the absolute position into the ByteBuffer
        - buffer: will receive the values of this vector in `x, y, z, w` order

        Returns
        - the passed in buffer
        """
        ...


    def getToAddress(self, address: int) -> "Vector4dc":
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


    def sub(self, v: "Vector4dc", dest: "Vector4d") -> "Vector4d":
        """
        Subtract the supplied vector from this one and store the result in `dest`.

        Arguments
        - v: the vector to subtract
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def sub(self, v: "Vector4fc", dest: "Vector4d") -> "Vector4d":
        """
        Subtract the supplied vector from this one and store the result in `dest`.

        Arguments
        - v: the vector to subtract
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def sub(self, x: float, y: float, z: float, w: float, dest: "Vector4d") -> "Vector4d":
        """
        Subtract `(x, y, z, w)` from this and store the result in `dest`.

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


    def add(self, v: "Vector4dc", dest: "Vector4d") -> "Vector4d":
        """
        Add the supplied vector to this one and store the result in `dest`.

        Arguments
        - v: the vector to add
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def add(self, v: "Vector4fc", dest: "Vector4d") -> "Vector4d":
        """
        Add the supplied vector to this one and store the result in `dest`.

        Arguments
        - v: the vector to add
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def add(self, x: float, y: float, z: float, w: float, dest: "Vector4d") -> "Vector4d":
        """
        Add `(x, y, z, w)` to this and store the result in `dest`.

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


    def fma(self, a: "Vector4dc", b: "Vector4dc", dest: "Vector4d") -> "Vector4d":
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


    def fma(self, a: float, b: "Vector4dc", dest: "Vector4d") -> "Vector4d":
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


    def mul(self, v: "Vector4dc", dest: "Vector4d") -> "Vector4d":
        """
        Multiply this Vector4d component-wise by the given Vector4dc and store the result in `dest`.

        Arguments
        - v: the vector to multiply this by
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mul(self, v: "Vector4fc", dest: "Vector4d") -> "Vector4d":
        """
        Multiply this Vector4d component-wise by the given Vector4fc and store the result in `dest`.

        Arguments
        - v: the vector to multiply this by
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def div(self, v: "Vector4dc", dest: "Vector4d") -> "Vector4d":
        """
        Divide this Vector4d component-wise by the given Vector4dc and store the result in `dest`.

        Arguments
        - v: the vector to divide this by
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mul(self, mat: "Matrix4dc", dest: "Vector4d") -> "Vector4d":
        """
        Multiply the given matrix mat with this Vector4d and store the result in `dest`.

        Arguments
        - mat: the matrix to multiply `this` by
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mul(self, mat: "Matrix4x3dc", dest: "Vector4d") -> "Vector4d":
        """
        Multiply the given matrix mat with this Vector4d and store the result in
        `dest`.

        Arguments
        - mat: the matrix to multiply the vector with
        - dest: the destination vector to hold the result

        Returns
        - dest
        """
        ...


    def mul(self, mat: "Matrix4x3fc", dest: "Vector4d") -> "Vector4d":
        """
        Multiply the given matrix mat with this Vector4d and store the result in
        `dest`.

        Arguments
        - mat: the matrix to multiply the vector with
        - dest: the destination vector to hold the result

        Returns
        - dest
        """
        ...


    def mul(self, mat: "Matrix4fc", dest: "Vector4d") -> "Vector4d":
        """
        Multiply the given matrix mat with this Vector4d and store the result in `dest`.

        Arguments
        - mat: the matrix to multiply `this` by
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mulTranspose(self, mat: "Matrix4dc", dest: "Vector4d") -> "Vector4d":
        """
        Multiply the transpose of the given matrix `mat` with this Vector4d and store the result in
        `dest`.

        Arguments
        - mat: the matrix whose transpose to multiply the vector with
        - dest: the destination vector to hold the result

        Returns
        - dest
        """
        ...


    def mulAffine(self, mat: "Matrix4dc", dest: "Vector4d") -> "Vector4d":
        """
        Multiply the given affine matrix mat with this Vector4d and store the result in
        `dest`.

        Arguments
        - mat: the affine matrix to multiply the vector with
        - dest: the destination vector to hold the result

        Returns
        - dest
        """
        ...


    def mulAffineTranspose(self, mat: "Matrix4dc", dest: "Vector4d") -> "Vector4d":
        """
        Multiply the transpose of the given affine matrix `mat` with this Vector4d and store the result in
        `dest`.

        Arguments
        - mat: the affine matrix whose transpose to multiply the vector with
        - dest: the destination vector to hold the result

        Returns
        - dest
        """
        ...


    def mulProject(self, mat: "Matrix4dc", dest: "Vector4d") -> "Vector4d":
        """
        Multiply the given matrix `mat` with this Vector4d, perform perspective division
        and store the result in `dest`.

        Arguments
        - mat: the matrix to multiply this vector by
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mulProject(self, mat: "Matrix4dc", dest: "Vector3d") -> "Vector3d":
        """
        Multiply the given matrix `mat` with this Vector4d, perform perspective division
        and store the `(x, y, z)` result in `dest`.

        Arguments
        - mat: the matrix to multiply this vector by
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mulAdd(self, a: "Vector4dc", b: "Vector4dc", dest: "Vector4d") -> "Vector4d":
        """
        Add the component-wise multiplication of `this * a` to `b`
        and store the result in `dest`.

        Arguments
        - a: the multiplicand
        - b: the addend
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mulAdd(self, a: float, b: "Vector4dc", dest: "Vector4d") -> "Vector4d":
        """
        Add the component-wise multiplication of `this * a` to `b`
        and store the result in `dest`.

        Arguments
        - a: the multiplicand
        - b: the addend
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mul(self, scalar: float, dest: "Vector4d") -> "Vector4d":
        """
        Multiply this Vector4d by the given scalar value and store the result in `dest`.

        Arguments
        - scalar: the factor to multiply by
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def div(self, scalar: float, dest: "Vector4d") -> "Vector4d":
        """
        Divide this Vector4d by the given scalar value and store the result in `dest`.

        Arguments
        - scalar: the factor to divide by
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def rotate(self, quat: "Quaterniondc", dest: "Vector4d") -> "Vector4d":
        """
        Transform this vector by the given quaternion `quat` and store the result in `dest`.

        Arguments
        - quat: the quaternion to transform this vector
        - dest: will hold the result

        Returns
        - dest

        See
        - Quaterniond.transform(Vector4d)
        """
        ...


    def rotateAxis(self, angle: float, aX: float, aY: float, aZ: float, dest: "Vector4d") -> "Vector4d":
        """
        Rotate this vector the specified radians around the given rotation axis and store the result
        into `dest`.

        Arguments
        - angle: the angle in radians
        - aX: the x component of the rotation axis
        - aY: the y component of the rotation axis
        - aZ: the z component of the rotation axis
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def rotateX(self, angle: float, dest: "Vector4d") -> "Vector4d":
        """
        Rotate this vector the specified radians around the X axis and store the result
        into `dest`.

        Arguments
        - angle: the angle in radians
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def rotateY(self, angle: float, dest: "Vector4d") -> "Vector4d":
        """
        Rotate this vector the specified radians around the Y axis and store the result
        into `dest`.

        Arguments
        - angle: the angle in radians
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def rotateZ(self, angle: float, dest: "Vector4d") -> "Vector4d":
        """
        Rotate this vector the specified radians around the Z axis and store the result
        into `dest`.

        Arguments
        - angle: the angle in radians
        - dest: will hold the result

        Returns
        - dest
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


    def normalize(self, dest: "Vector4d") -> "Vector4d":
        """
        Normalizes this vector and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def normalize(self, length: float, dest: "Vector4d") -> "Vector4d":
        """
        Scale this vector to have the given length and store the result in `dest`.

        Arguments
        - length: the desired length
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def normalize3(self, dest: "Vector4d") -> "Vector4d":
        """
        Normalize this vector by computing only the norm of `(x, y, z)` and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def distance(self, v: "Vector4dc") -> float:
        """
        Return the distance between this Vector and `v`.

        Arguments
        - v: the other vector

        Returns
        - the distance
        """
        ...


    def distance(self, x: float, y: float, z: float, w: float) -> float:
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


    def distanceSquared(self, v: "Vector4dc") -> float:
        """
        Return the square of the distance between this vector and `v`.

        Arguments
        - v: the other vector

        Returns
        - the squared of the distance
        """
        ...


    def distanceSquared(self, x: float, y: float, z: float, w: float) -> float:
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


    def dot(self, v: "Vector4dc") -> float:
        """
        Compute the dot product (inner product) of this vector and `v`.

        Arguments
        - v: the other vector

        Returns
        - the dot product
        """
        ...


    def dot(self, x: float, y: float, z: float, w: float) -> float:
        """
        Compute the dot product (inner product) of this vector and `(x, y, z, w)`.

        Arguments
        - x: the x component of the other vector
        - y: the y component of the other vector
        - z: the z component of the other vector
        - w: the w component of the other vector

        Returns
        - the dot product
        """
        ...


    def angleCos(self, v: "Vector4dc") -> float:
        """
        Return the cosine of the angle between this vector and the supplied vector.
        
        Use this instead of `Math.cos(angle(v))`.

        Arguments
        - v: the other vector

        Returns
        - the cosine of the angle

        See
        - .angle(Vector4dc)
        """
        ...


    def angle(self, v: "Vector4dc") -> float:
        """
        Return the angle between this vector and the supplied vector.

        Arguments
        - v: the other vector

        Returns
        - the angle, in radians

        See
        - .angleCos(Vector4dc)
        """
        ...


    def negate(self, dest: "Vector4d") -> "Vector4d":
        """
        Negate this vector and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def min(self, v: "Vector4dc", dest: "Vector4d") -> "Vector4d":
        """
        Set the components of `dest` to be the component-wise minimum of this and the other vector.

        Arguments
        - v: the other vector
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def max(self, v: "Vector4dc", dest: "Vector4d") -> "Vector4d":
        """
        Set the components of `dest` to be the component-wise maximum of this and the other vector.

        Arguments
        - v: the other vector
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def smoothStep(self, v: "Vector4dc", t: float, dest: "Vector4d") -> "Vector4d":
        """
        Compute a smooth-step (i.e. hermite with zero tangents) interpolation
        between `this` vector and the given vector `v` and
        store the result in `dest`.

        Arguments
        - v: the other vector
        - t: the interpolation factor, within `[0..1]`
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def hermite(self, t0: "Vector4dc", v1: "Vector4dc", t1: "Vector4dc", t: float, dest: "Vector4d") -> "Vector4d":
        """
        Compute a hermite interpolation between `this` vector and its
        associated tangent `t0` and the given vector `v`
        with its tangent `t1` and store the result in
        `dest`.

        Arguments
        - t0: the tangent of `this` vector
        - v1: the other vector
        - t1: the tangent of the other vector
        - t: the interpolation factor, within `[0..1]`
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def lerp(self, other: "Vector4dc", t: float, dest: "Vector4d") -> "Vector4d":
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


    def get(self, component: int) -> float:
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


    def get(self, mode: int, dest: "Vector4i") -> "Vector4i":
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


    def get(self, dest: "Vector4f") -> "Vector4f":
        """
        Set the components of the given vector `dest` to those of `this` vector.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def get(self, dest: "Vector4d") -> "Vector4d":
        """
        Set the components of the given vector `dest` to those of `this` vector.

        Arguments
        - dest: will hold the result

        Returns
        - dest
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


    def floor(self, dest: "Vector4d") -> "Vector4d":
        """
        Compute for each component of this vector the largest (closest to positive
        infinity) `double` value that is less than or equal to that
        component and is equal to a mathematical integer and store the result in
        `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def ceil(self, dest: "Vector4d") -> "Vector4d":
        """
        Compute for each component of this vector the smallest (closest to negative
        infinity) `double` value that is greater than or equal to that
        component and is equal to a mathematical integer and store the result in
        `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def round(self, dest: "Vector4d") -> "Vector4d":
        """
        Compute for each component of this vector the closest double that is equal to
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
        is, they are not Double.isNaN() NaN and not
        Double.isInfinite() infinity.

        Returns
        - `True` if all components are finite floating-point values;
                `False` otherwise
        """
        ...


    def absolute(self, dest: "Vector4d") -> "Vector4d":
        """
        Compute the absolute of each of this vector's components
        and store the result into `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def equals(self, v: "Vector4dc", delta: float) -> bool:
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


    def equals(self, x: float, y: float, z: float, w: float) -> bool:
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
