"""
Python module generated from Java source file org.joml.Vector3dc

Java source file obtained from artifact joml version 1.10.5

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util import *
from org.joml import *
from typing import Any, Callable, Iterable, Tuple


class Vector3dc:
    """
    Interface to a read-only view of a 3-dimensional vector of double-precision floats.

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


    def get(self, buffer: "ByteBuffer") -> "ByteBuffer":
        """
        Store this vector into the supplied ByteBuffer at the current
        buffer ByteBuffer.position() position.
        
        This method will not increment the position of the given ByteBuffer.
        
        In order to specify the offset into the ByteBuffer at which
        the vector is stored, use .get(int, ByteBuffer), taking
        the absolute position as parameter.

        Arguments
        - buffer: will receive the values of this vector in `x, y, z` order

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
        - buffer: will receive the values of this vector in `x, y, z` order

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
        - buffer: will receive the values of this vector in `x, y, z` order

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
        - buffer: will receive the values of this vector in `x, y, z` order

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
        - buffer: will receive the values of this vector in `x, y, z` order

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
        - buffer: will receive the values of this vector in `x, y, z` order

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
        - buffer: will receive the values of this vector in `x, y, z` order

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
        - buffer: will receive the values of this vector in `x, y, z` order

        Returns
        - the passed in buffer
        """
        ...


    def getToAddress(self, address: int) -> "Vector3dc":
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


    def sub(self, v: "Vector3dc", dest: "Vector3d") -> "Vector3d":
        """
        Subtract the supplied vector from this one and store the result in `dest`.

        Arguments
        - v: the vector to subtract from `this`
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def sub(self, v: "Vector3fc", dest: "Vector3d") -> "Vector3d":
        """
        Subtract the supplied vector from this one and store the result in `dest`.

        Arguments
        - v: the vector to subtract from `this`
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def sub(self, x: float, y: float, z: float, dest: "Vector3d") -> "Vector3d":
        """
        Subtract `(x, y, z)` from this vector and store the result in `dest`.

        Arguments
        - x: the x component to subtract
        - y: the y component to subtract
        - z: the z component to subtract
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def add(self, v: "Vector3dc", dest: "Vector3d") -> "Vector3d":
        """
        Add the supplied vector to this one and store the result in `dest`.

        Arguments
        - v: the vector to add
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def add(self, v: "Vector3fc", dest: "Vector3d") -> "Vector3d":
        """
        Add the supplied vector to this one and store the result in `dest`.

        Arguments
        - v: the vector to add
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def add(self, x: float, y: float, z: float, dest: "Vector3d") -> "Vector3d":
        """
        Increment the components of this vector by the given values and store the result in `dest`.

        Arguments
        - x: the x component to add
        - y: the y component to add
        - z: the z component to add
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def fma(self, a: "Vector3dc", b: "Vector3dc", dest: "Vector3d") -> "Vector3d":
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


    def fma(self, a: float, b: "Vector3dc", dest: "Vector3d") -> "Vector3d":
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


    def fma(self, a: "Vector3dc", b: "Vector3fc", dest: "Vector3d") -> "Vector3d":
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


    def fma(self, a: "Vector3fc", b: "Vector3fc", dest: "Vector3d") -> "Vector3d":
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


    def fma(self, a: float, b: "Vector3fc", dest: "Vector3d") -> "Vector3d":
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


    def mulAdd(self, a: "Vector3dc", b: "Vector3dc", dest: "Vector3d") -> "Vector3d":
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


    def mulAdd(self, a: float, b: "Vector3dc", dest: "Vector3d") -> "Vector3d":
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


    def mulAdd(self, a: "Vector3fc", b: "Vector3dc", dest: "Vector3d") -> "Vector3d":
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


    def mul(self, v: "Vector3fc", dest: "Vector3d") -> "Vector3d":
        """
        Multiply this Vector3d component-wise by another Vector3f and store the result in `dest`.

        Arguments
        - v: the vector to multiply by
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mul(self, v: "Vector3dc", dest: "Vector3d") -> "Vector3d":
        """
        Multiply this by `v` component-wise and store the result into `dest`.

        Arguments
        - v: the vector to multiply by
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def div(self, v: "Vector3fc", dest: "Vector3d") -> "Vector3d":
        """
        Divide this Vector3d component-wise by another Vector3f and store the result in `dest`.

        Arguments
        - v: the vector to divide by
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def div(self, v: "Vector3dc", dest: "Vector3d") -> "Vector3d":
        """
        Divide this by `v` component-wise and store the result into `dest`.

        Arguments
        - v: the vector to divide by
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mulProject(self, mat: "Matrix4dc", w: float, dest: "Vector3d") -> "Vector3d":
        """
        Multiply the given matrix `mat` with this Vector3d, perform perspective division
        and store the result in `dest`.
        
        This method uses the given `w` as the fourth vector component.

        Arguments
        - mat: the matrix to multiply this vector by
        - w: the w component to use
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mulProject(self, mat: "Matrix4dc", dest: "Vector3d") -> "Vector3d":
        """
        Multiply the given matrix `mat` with this Vector3d, perform perspective division
        and store the result in `dest`.
        
        This method uses `w=1.0` as the fourth vector component.

        Arguments
        - mat: the matrix to multiply this vector by
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mulProject(self, mat: "Matrix4fc", dest: "Vector3d") -> "Vector3d":
        """
        Multiply the given matrix `mat` with this Vector3d, perform perspective division
        and store the result in `dest`.
        
        This method uses `w=1.0` as the fourth vector component.

        Arguments
        - mat: the matrix to multiply this vector by
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mul(self, mat: "Matrix3dc", dest: "Vector3d") -> "Vector3d":
        """
        Multiply the given matrix `mat` with `this` and store the
        result in `dest`.

        Arguments
        - mat: the matrix to multiply this vector by
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mul(self, mat: "Matrix3dc", dest: "Vector3f") -> "Vector3f":
        """
        Multiply the given matrix `mat` with `this` and store the
        result in `dest`.

        Arguments
        - mat: the matrix to multiply this vector by
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mul(self, mat: "Matrix3fc", dest: "Vector3d") -> "Vector3d":
        """
        Multiply the given matrix `mat` with `this` and store the
        result in `dest`.

        Arguments
        - mat: the matrix to multiply this vector by
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mul(self, mat: "Matrix3x2dc", dest: "Vector3d") -> "Vector3d":
        """
        Multiply the given matrix `mat` with `this` by assuming a
        third row in the matrix of `(0, 0, 1)` and store the result in `dest`.

        Arguments
        - mat: the matrix to multiply this vector by
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mul(self, mat: "Matrix3x2fc", dest: "Vector3d") -> "Vector3d":
        """
        Multiply the given matrix `mat` with `this` by assuming a
        third row in the matrix of `(0, 0, 1)` and store the result in `dest`.

        Arguments
        - mat: the matrix to multiply this vector by
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mulTranspose(self, mat: "Matrix3dc", dest: "Vector3d") -> "Vector3d":
        """
        Multiply the transpose of the given matrix with this Vector3f and store the result in `dest`.

        Arguments
        - mat: the matrix
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mulTranspose(self, mat: "Matrix3fc", dest: "Vector3d") -> "Vector3d":
        """
        Multiply the transpose of the given matrix with this Vector3f and store the result in `dest`.

        Arguments
        - mat: the matrix
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mulPosition(self, mat: "Matrix4dc", dest: "Vector3d") -> "Vector3d":
        """
        Multiply the given 4x4 matrix `mat` with `this` and store the
        result in `dest`.
        
        This method assumes the `w` component of `this` to be `1.0`.

        Arguments
        - mat: the matrix to multiply this vector by
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mulPosition(self, mat: "Matrix4fc", dest: "Vector3d") -> "Vector3d":
        """
        Multiply the given 4x4 matrix `mat` with `this` and store the
        result in `dest`.
        
        This method assumes the `w` component of `this` to be `1.0`.

        Arguments
        - mat: the matrix to multiply this vector by
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mulPosition(self, mat: "Matrix4x3dc", dest: "Vector3d") -> "Vector3d":
        """
        Multiply the given 4x3 matrix `mat` with `this` and store the
        result in `dest`.
        
        This method assumes the `w` component of `this` to be `1.0`.

        Arguments
        - mat: the matrix to multiply this vector by
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mulPosition(self, mat: "Matrix4x3fc", dest: "Vector3d") -> "Vector3d":
        """
        Multiply the given 4x3 matrix `mat` with `this` and store the
        result in `dest`.
        
        This method assumes the `w` component of `this` to be `1.0`.

        Arguments
        - mat: the matrix to multiply this vector by
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mulTransposePosition(self, mat: "Matrix4dc", dest: "Vector3d") -> "Vector3d":
        """
        Multiply the transpose of the given 4x4 matrix `mat` with `this` and store the
        result in `dest`.
        
        This method assumes the `w` component of `this` to be `1.0`.

        Arguments
        - mat: the matrix whose transpose to multiply this vector by
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mulTransposePosition(self, mat: "Matrix4fc", dest: "Vector3d") -> "Vector3d":
        """
        Multiply the transpose of the given 4x4 matrix `mat` with `this` and store the
        result in `dest`.
        
        This method assumes the `w` component of `this` to be `1.0`.

        Arguments
        - mat: the matrix whose transpose to multiply this vector by
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mulPositionW(self, mat: "Matrix4fc", dest: "Vector3d") -> float:
        """
        Multiply the given 4x4 matrix `mat` with `this`, store the
        result in `dest` and return the *w* component of the resulting 4D vector.
        
        This method assumes the `w` component of `this` to be `1.0`.

        Arguments
        - mat: the matrix to multiply this vector by
        - dest: will hold the `(x, y, z)` components of the resulting vector

        Returns
        - the *w* component of the resulting 4D vector after multiplication
        """
        ...


    def mulPositionW(self, mat: "Matrix4dc", dest: "Vector3d") -> float:
        """
        Multiply the given 4x4 matrix `mat` with `this`, store the
        result in `dest` and return the *w* component of the resulting 4D vector.
        
        This method assumes the `w` component of `this` to be `1.0`.

        Arguments
        - mat: the matrix to multiply this vector by
        - dest: will hold the `(x, y, z)` components of the resulting vector

        Returns
        - the *w* component of the resulting 4D vector after multiplication
        """
        ...


    def mulDirection(self, mat: "Matrix4dc", dest: "Vector3d") -> "Vector3d":
        """
        Multiply the given 4x4 matrix `mat` with `this` and store the
        result in `dest`.
        
        This method assumes the `w` component of `this` to be `0.0`.

        Arguments
        - mat: the matrix to multiply this vector by
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mulDirection(self, mat: "Matrix4fc", dest: "Vector3d") -> "Vector3d":
        """
        Multiply the given 4x4 matrix `mat` with `this` and store the
        result in `dest`.
        
        This method assumes the `w` component of `this` to be `0.0`.

        Arguments
        - mat: the matrix to multiply this vector by
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mulDirection(self, mat: "Matrix4x3dc", dest: "Vector3d") -> "Vector3d":
        """
        Multiply the given 4x3 matrix `mat` with `this` and store the
        result in `dest`.
        
        This method assumes the `w` component of `this` to be `0.0`.

        Arguments
        - mat: the matrix to multiply this vector by
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mulDirection(self, mat: "Matrix4x3fc", dest: "Vector3d") -> "Vector3d":
        """
        Multiply the given 4x3 matrix `mat` with `this` and store the
        result in `dest`.
        
        This method assumes the `w` component of `this` to be `0.0`.

        Arguments
        - mat: the matrix to multiply this vector by
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mulTransposeDirection(self, mat: "Matrix4dc", dest: "Vector3d") -> "Vector3d":
        """
        Multiply the transpose of the given 4x4 matrix `mat` with `this` and store the
        result in `dest`.
        
        This method assumes the `w` component of `this` to be `0.0`.

        Arguments
        - mat: the matrix whose transpose to multiply this vector by
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mulTransposeDirection(self, mat: "Matrix4fc", dest: "Vector3d") -> "Vector3d":
        """
        Multiply the transpose of the given 4x4 matrix `mat` with `this` and store the
        result in `dest`.
        
        This method assumes the `w` component of `this` to be `0.0`.

        Arguments
        - mat: the matrix whose transpose to multiply this vector by
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mul(self, scalar: float, dest: "Vector3d") -> "Vector3d":
        """
        Multiply this Vector3d by the given scalar value and store the result in `dest`.

        Arguments
        - scalar: the scalar factor
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mul(self, x: float, y: float, z: float, dest: "Vector3d") -> "Vector3d":
        """
        Multiply the components of this Vector3f by the given scalar values and store the result in `dest`.

        Arguments
        - x: the x component to multiply this vector by
        - y: the y component to multiply this vector by
        - z: the z component to multiply this vector by
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def rotate(self, quat: "Quaterniondc", dest: "Vector3d") -> "Vector3d":
        """
        Rotate this vector by the given quaternion `quat` and store the result in `dest`.

        Arguments
        - quat: the quaternion to rotate this vector
        - dest: will hold the result

        Returns
        - dest

        See
        - Quaterniond.transform(Vector3d)
        """
        ...


    def rotationTo(self, toDir: "Vector3dc", dest: "Quaterniond") -> "Quaterniond":
        """
        Compute the quaternion representing a rotation of `this` vector to point along `toDir`
        and store the result in `dest`.
        
        Because there can be multiple possible rotations, this method chooses the one with the shortest arc.

        Arguments
        - toDir: the destination direction
        - dest: will hold the result

        Returns
        - dest

        See
        - Quaterniond.rotationTo(Vector3dc, Vector3dc)
        """
        ...


    def rotationTo(self, toDirX: float, toDirY: float, toDirZ: float, dest: "Quaterniond") -> "Quaterniond":
        """
        Compute the quaternion representing a rotation of `this` vector to point along `(toDirX, toDirY, toDirZ)`
        and store the result in `dest`.
        
        Because there can be multiple possible rotations, this method chooses the one with the shortest arc.

        Arguments
        - toDirX: the x coordinate of the destination direction
        - toDirY: the y coordinate of the destination direction
        - toDirZ: the z coordinate of the destination direction
        - dest: will hold the result

        Returns
        - dest

        See
        - Quaterniond.rotationTo(double, double, double, double, double, double)
        """
        ...


    def rotateAxis(self, angle: float, aX: float, aY: float, aZ: float, dest: "Vector3d") -> "Vector3d":
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


    def rotateX(self, angle: float, dest: "Vector3d") -> "Vector3d":
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


    def rotateY(self, angle: float, dest: "Vector3d") -> "Vector3d":
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


    def rotateZ(self, angle: float, dest: "Vector3d") -> "Vector3d":
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


    def div(self, scalar: float, dest: "Vector3d") -> "Vector3d":
        """
        Divide this Vector3d by the given scalar value and store the result in `dest`.

        Arguments
        - scalar: the scalar to divide this vector by
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def div(self, x: float, y: float, z: float, dest: "Vector3d") -> "Vector3d":
        """
        Divide the components of this Vector3f by the given scalar values and store the result in `dest`.

        Arguments
        - x: the x component to divide this vector by
        - y: the y component to divide this vector by
        - z: the z component to divide this vector by
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


    def normalize(self, dest: "Vector3d") -> "Vector3d":
        """
        Normalize this vector and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def normalize(self, length: float, dest: "Vector3d") -> "Vector3d":
        """
        Scale this vector to have the given length and store the result in `dest`.

        Arguments
        - length: the desired length
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def cross(self, v: "Vector3dc", dest: "Vector3d") -> "Vector3d":
        """
        Calculate the cross product of this and v2 and store the result in `dest`.

        Arguments
        - v: the other vector
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def cross(self, x: float, y: float, z: float, dest: "Vector3d") -> "Vector3d":
        """
        Compute the cross product of this vector and `(x, y, z)` and store the result in `dest`.

        Arguments
        - x: the x component of the other vector
        - y: the y component of the other vector
        - z: the z component of the other vector
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def distance(self, v: "Vector3dc") -> float:
        """
        Return the distance between this vector and `v`.

        Arguments
        - v: the other vector

        Returns
        - the distance
        """
        ...


    def distance(self, x: float, y: float, z: float) -> float:
        """
        Return the distance between `this` vector and `(x, y, z)`.

        Arguments
        - x: the x component of the other vector
        - y: the y component of the other vector
        - z: the z component of the other vector

        Returns
        - the euclidean distance
        """
        ...


    def distanceSquared(self, v: "Vector3dc") -> float:
        """
        Return the square of the distance between this vector and `v`.

        Arguments
        - v: the other vector

        Returns
        - the squared of the distance
        """
        ...


    def distanceSquared(self, x: float, y: float, z: float) -> float:
        """
        Return the square of the distance between `this` vector and `(x, y, z)`.

        Arguments
        - x: the x component of the other vector
        - y: the y component of the other vector
        - z: the z component of the other vector

        Returns
        - the square of the distance
        """
        ...


    def dot(self, v: "Vector3dc") -> float:
        """
        Return the dot product of this vector and the supplied vector.

        Arguments
        - v: the other vector

        Returns
        - the dot product
        """
        ...


    def dot(self, x: float, y: float, z: float) -> float:
        """
        Return the dot product of this vector and the vector `(x, y, z)`.

        Arguments
        - x: the x component of the other vector
        - y: the y component of the other vector
        - z: the z component of the other vector

        Returns
        - the dot product
        """
        ...


    def angleCos(self, v: "Vector3dc") -> float:
        """
        Return the cosine of the angle between `this` vector and
        the supplied vector. Use this instead of `Math.cos(angle(v))`.

        Arguments
        - v: the other vector

        Returns
        - the cosine of the angle

        See
        - .angle(Vector3dc)
        """
        ...


    def angle(self, v: "Vector3dc") -> float:
        """
        Return the angle between this vector and the supplied vector.

        Arguments
        - v: the other vector

        Returns
        - the angle, in radians

        See
        - .angleCos(Vector3dc)
        """
        ...


    def angleSigned(self, v: "Vector3dc", n: "Vector3dc") -> float:
        """
        Return the signed angle between this vector and the supplied vector with
        respect to the plane with the given normal vector `n`.

        Arguments
        - v: the other vector
        - n: the plane's normal vector

        Returns
        - the angle, in radians

        See
        - .angleCos(Vector3dc)
        """
        ...


    def angleSigned(self, x: float, y: float, z: float, nx: float, ny: float, nz: float) -> float:
        """
        Return the signed angle between this vector and the supplied vector with
        respect to the plane with the given normal vector `(nx, ny, nz)`.

        Arguments
        - x: the x coordinate of the other vector
        - y: the y coordinate of the other vector
        - z: the z coordinate of the other vector
        - nx: the x coordinate of the plane's normal vector
        - ny: the y coordinate of the plane's normal vector
        - nz: the z coordinate of the plane's normal vector

        Returns
        - the angle, in radians
        """
        ...


    def min(self, v: "Vector3dc", dest: "Vector3d") -> "Vector3d":
        """
        Set the components of `dest` to be the component-wise minimum of this and the other vector.

        Arguments
        - v: the other vector
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def max(self, v: "Vector3dc", dest: "Vector3d") -> "Vector3d":
        """
        Set the components of `dest` to be the component-wise maximum of this and the other vector.

        Arguments
        - v: the other vector
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def negate(self, dest: "Vector3d") -> "Vector3d":
        """
        Negate this vector and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def absolute(self, dest: "Vector3d") -> "Vector3d":
        """
        Compute the absolute values of the individual components of `this` and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def reflect(self, normal: "Vector3dc", dest: "Vector3d") -> "Vector3d":
        """
        Reflect this vector about the given normal vector and store the result in `dest`.

        Arguments
        - normal: the vector to reflect about
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def reflect(self, x: float, y: float, z: float, dest: "Vector3d") -> "Vector3d":
        """
        Reflect this vector about the given normal vector and store the result in `dest`.

        Arguments
        - x: the x component of the normal
        - y: the y component of the normal
        - z: the z component of the normal
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def half(self, other: "Vector3dc", dest: "Vector3d") -> "Vector3d":
        """
        Compute the half vector between this and the other vector and store the result in `dest`.

        Arguments
        - other: the other vector
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def half(self, x: float, y: float, z: float, dest: "Vector3d") -> "Vector3d":
        """
        Compute the half vector between this and the vector `(x, y, z)` 
        and store the result in `dest`.

        Arguments
        - x: the x component of the other vector
        - y: the y component of the other vector
        - z: the z component of the other vector
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def smoothStep(self, v: "Vector3dc", t: float, dest: "Vector3d") -> "Vector3d":
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


    def hermite(self, t0: "Vector3dc", v1: "Vector3dc", t1: "Vector3dc", t: float, dest: "Vector3d") -> "Vector3d":
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


    def lerp(self, other: "Vector3dc", t: float, dest: "Vector3d") -> "Vector3d":
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
        - component: the component, within `[0..2]`

        Returns
        - the value

        Raises
        - IllegalArgumentException: if `component` is not within `[0..2]`
        """
        ...


    def get(self, mode: int, dest: "Vector3i") -> "Vector3i":
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


    def get(self, dest: "Vector3f") -> "Vector3f":
        """
        Set the components of the given vector `dest` to those of `this` vector.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def get(self, dest: "Vector3d") -> "Vector3d":
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
        - the component index, within `[0..2]`
        """
        ...


    def minComponent(self) -> int:
        """
        Determine the component with the smallest (towards zero) absolute value.

        Returns
        - the component index, within `[0..2]`
        """
        ...


    def orthogonalize(self, v: "Vector3dc", dest: "Vector3d") -> "Vector3d":
        """
        Transform `this` vector so that it is orthogonal to the given vector `v`, normalize the result and store it into `dest`.
        
        Reference: <a href="https://en.wikipedia.org/wiki/Gram%E2%80%93Schmidt_process">Gram–Schmidt process</a>

        Arguments
        - v: the reference vector which the result should be orthogonal to
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def orthogonalizeUnit(self, v: "Vector3dc", dest: "Vector3d") -> "Vector3d":
        """
        Transform `this` vector so that it is orthogonal to the given unit vector `v`, normalize the result and store it into `dest`.
        
        The vector `v` is assumed to be a .normalize(Vector3d) unit vector.
        
        Reference: <a href="https://en.wikipedia.org/wiki/Gram%E2%80%93Schmidt_process">Gram–Schmidt process</a>

        Arguments
        - v: the reference unit vector which the result should be orthogonal to
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def floor(self, dest: "Vector3d") -> "Vector3d":
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


    def ceil(self, dest: "Vector3d") -> "Vector3d":
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


    def round(self, dest: "Vector3d") -> "Vector3d":
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


    def equals(self, v: "Vector3dc", delta: float) -> bool:
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


    def equals(self, x: float, y: float, z: float) -> bool:
        """
        Compare the vector components of `this` vector with the given `(x, y, z)`
        and return whether all of them are equal.

        Arguments
        - x: the x component to compare to
        - y: the y component to compare to
        - z: the z component to compare to

        Returns
        - `True` if all the vector components are equal
        """
        ...
