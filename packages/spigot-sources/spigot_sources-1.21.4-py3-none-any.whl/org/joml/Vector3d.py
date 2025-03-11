"""
Python module generated from Java source file org.joml.Vector3d

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


class Vector3d(Externalizable, Cloneable, Vector3dc):
    """
    Contains the definition of a Vector comprising 3 doubles and associated
    transformations.

    Author(s)
    - F. Neurath
    """

    def __init__(self):
        """
        Create a new Vector3d with all components set to zero.
        """
        ...


    def __init__(self, d: float):
        """
        Create a new Vector3d and initialize all three components with the given value.

        Arguments
        - d: the value of all three components
        """
        ...


    def __init__(self, x: float, y: float, z: float):
        """
        Create a new Vector3d with the given component values.

        Arguments
        - x: the value of x
        - y: the value of y
        - z: the value of z
        """
        ...


    def __init__(self, v: "Vector3fc"):
        """
        Create a new Vector3d whose values will be copied from the given vector.

        Arguments
        - v: provides the initial values for the new vector
        """
        ...


    def __init__(self, v: "Vector3ic"):
        """
        Create a new Vector3d whose values will be copied from the given vector.

        Arguments
        - v: provides the initial values for the new vector
        """
        ...


    def __init__(self, v: "Vector2fc", z: float):
        """
        Create a new Vector3d with the first two components from the
        given `v` and the given `z`

        Arguments
        - v: the Vector2fc to copy the values from
        - z: the z component
        """
        ...


    def __init__(self, v: "Vector2ic", z: float):
        """
        Create a new Vector3d with the first two components from the
        given `v` and the given `z`

        Arguments
        - v: the Vector2ic to copy the values from
        - z: the z component
        """
        ...


    def __init__(self, v: "Vector3dc"):
        """
        Create a new Vector3d whose values will be copied from the given vector.

        Arguments
        - v: provides the initial values for the new vector
        """
        ...


    def __init__(self, v: "Vector2dc", z: float):
        """
        Create a new Vector3d with the first two components from the
        given `v` and the given `z`

        Arguments
        - v: the Vector2d to copy the values from
        - z: the z component
        """
        ...


    def __init__(self, xyz: list[float]):
        """
        Create a new Vector3d and initialize its three components from the first
        three elements of the given array.

        Arguments
        - xyz: the array containing at least three elements
        """
        ...


    def __init__(self, xyz: list[float]):
        """
        Create a new Vector3d and initialize its three components from the first
        three elements of the given array.

        Arguments
        - xyz: the array containing at least three elements
        """
        ...


    def __init__(self, buffer: "ByteBuffer"):
        """
        Create a new Vector3d and read this vector from the supplied ByteBuffer
        at the current buffer ByteBuffer.position() position.
        
        This method will not increment the position of the given ByteBuffer.
        
        In order to specify the offset into the ByteBuffer at which
        the vector is read, use .Vector3d(int, ByteBuffer), taking
        the absolute position as parameter.

        Arguments
        - buffer: values will be read in `x, y, z` order

        See
        - .Vector3d(int, ByteBuffer)
        """
        ...


    def __init__(self, index: int, buffer: "ByteBuffer"):
        """
        Create a new Vector3d and read this vector from the supplied ByteBuffer
        starting at the specified absolute buffer position/index.
        
        This method will not increment the position of the given ByteBuffer.

        Arguments
        - index: the absolute position into the ByteBuffer
        - buffer: values will be read in `x, y, z` order
        """
        ...


    def __init__(self, buffer: "DoubleBuffer"):
        """
        Create a new Vector3d and read this vector from the supplied DoubleBuffer
        at the current buffer DoubleBuffer.position() position.
        
        This method will not increment the position of the given DoubleBuffer.
        
        In order to specify the offset into the DoubleBuffer at which
        the vector is read, use .Vector3d(int, DoubleBuffer), taking
        the absolute position as parameter.

        Arguments
        - buffer: values will be read in `x, y, z` order

        See
        - .Vector3d(int, DoubleBuffer)
        """
        ...


    def __init__(self, index: int, buffer: "DoubleBuffer"):
        """
        Create a new Vector3d and read this vector from the supplied DoubleBuffer
        starting at the specified absolute buffer position/index.
        
        This method will not increment the position of the given DoubleBuffer.

        Arguments
        - index: the absolute position into the DoubleBuffer
        - buffer: values will be read in `x, y, z` order
        """
        ...


    def x(self) -> float:
        ...


    def y(self) -> float:
        ...


    def z(self) -> float:
        ...


    def xy(self, dest: "Vector2f") -> "Vector2f":
        """
        Copy the `(x, y)` components of `this` into the supplied `dest` vector
        and return it.
        
        Note that due to the given vector `dest` storing the components in float-precision,
        there is the possibility to lose precision.

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


    def set(self, v: "Vector4dc") -> "Vector3d":
        """
        Set this vector to the `(x, y, z)` components of `v`.

        Arguments
        - v: the vector to copy from

        Returns
        - this
        """
        ...


    def set(self, v: "Vector4fc") -> "Vector3d":
        """
        Set this vector to the `(x, y, z)` components of `v`.

        Arguments
        - v: the vector to copy from

        Returns
        - this
        """
        ...


    def set(self, v: "Vector4ic") -> "Vector3d":
        """
        Set this vector to the `(x, y, z)` components of `v`.

        Arguments
        - v: the vector to copy from

        Returns
        - this
        """
        ...


    def set(self, v: "Vector3dc") -> "Vector3d":
        """
        Set the x, y and z components to match the supplied vector.

        Arguments
        - v: the vector to set this vector's components from

        Returns
        - this
        """
        ...


    def set(self, v: "Vector3ic") -> "Vector3d":
        """
        Set the x, y and z components to match the supplied vector.

        Arguments
        - v: the vector to set this vector's components from

        Returns
        - this
        """
        ...


    def set(self, v: "Vector2dc", z: float) -> "Vector3d":
        """
        Set the first two components from the given `v`
        and the z component from the given `z`

        Arguments
        - v: the Vector2dc to copy the values from
        - z: the z component

        Returns
        - this
        """
        ...


    def set(self, v: "Vector2ic", z: float) -> "Vector3d":
        """
        Set the first two components from the given `v`
        and the z component from the given `z`

        Arguments
        - v: the Vector2ic to copy the values from
        - z: the z component

        Returns
        - this
        """
        ...


    def set(self, v: "Vector3fc") -> "Vector3d":
        """
        Set the x, y and z components to match the supplied vector.

        Arguments
        - v: the vector to set this vector's components from

        Returns
        - this
        """
        ...


    def set(self, v: "Vector2fc", z: float) -> "Vector3d":
        """
        Set the first two components from the given `v`
        and the z component from the given `z`

        Arguments
        - v: the Vector2fc to copy the values from
        - z: the z component

        Returns
        - this
        """
        ...


    def set(self, d: float) -> "Vector3d":
        """
        Set the x, y, and z components to the supplied value.

        Arguments
        - d: the value of all three components

        Returns
        - this
        """
        ...


    def set(self, x: float, y: float, z: float) -> "Vector3d":
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


    def set(self, xyz: list[float]) -> "Vector3d":
        """
        Set the three components of this vector to the first three elements of the given array.

        Arguments
        - xyz: the array containing at least three elements

        Returns
        - this
        """
        ...


    def set(self, xyz: list[float]) -> "Vector3d":
        """
        Set the three components of this vector to the first three elements of the given array.

        Arguments
        - xyz: the array containing at least three elements

        Returns
        - this
        """
        ...


    def set(self, buffer: "ByteBuffer") -> "Vector3d":
        """
        Read this vector from the supplied ByteBuffer at the current
        buffer ByteBuffer.position() position.
        
        This method will not increment the position of the given ByteBuffer.
        
        In order to specify the offset into the ByteBuffer at which
        the vector is read, use .set(int, ByteBuffer), taking
        the absolute position as parameter.

        Arguments
        - buffer: values will be read in `x, y, z` order

        Returns
        - this

        See
        - .set(int, ByteBuffer)
        """
        ...


    def set(self, index: int, buffer: "ByteBuffer") -> "Vector3d":
        """
        Read this vector from the supplied ByteBuffer starting at the specified
        absolute buffer position/index.
        
        This method will not increment the position of the given ByteBuffer.

        Arguments
        - index: the absolute position into the ByteBuffer
        - buffer: values will be read in `x, y, z` order

        Returns
        - this
        """
        ...


    def set(self, buffer: "DoubleBuffer") -> "Vector3d":
        """
        Read this vector from the supplied DoubleBuffer at the current
        buffer DoubleBuffer.position() position.
        
        This method will not increment the position of the given DoubleBuffer.
        
        In order to specify the offset into the DoubleBuffer at which
        the vector is read, use .set(int, DoubleBuffer), taking
        the absolute position as parameter.

        Arguments
        - buffer: values will be read in `x, y, z` order

        Returns
        - this

        See
        - .set(int, DoubleBuffer)
        """
        ...


    def set(self, index: int, buffer: "DoubleBuffer") -> "Vector3d":
        """
        Read this vector from the supplied DoubleBuffer starting at the specified
        absolute buffer position/index.
        
        This method will not increment the position of the given DoubleBuffer.

        Arguments
        - index: the absolute position into the DoubleBuffer
        - buffer: values will be read in `x, y, z` order

        Returns
        - this
        """
        ...


    def setFromAddress(self, address: int) -> "Vector3d":
        """
        Set the values of this vector by reading 3 double values from off-heap memory,
        starting at the given address.
        
        This method will throw an UnsupportedOperationException when JOML is used with `-Djoml.nounsafe`.
        
        *This method is unsafe as it can result in a crash of the JVM process when the specified address range does not belong to this process.*

        Arguments
        - address: the off-heap memory address to read the vector values from

        Returns
        - this
        """
        ...


    def setComponent(self, component: int, value: float) -> "Vector3d":
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


    def get(self, buffer: "ByteBuffer") -> "ByteBuffer":
        ...


    def get(self, index: int, buffer: "ByteBuffer") -> "ByteBuffer":
        ...


    def get(self, buffer: "DoubleBuffer") -> "DoubleBuffer":
        ...


    def get(self, index: int, buffer: "DoubleBuffer") -> "DoubleBuffer":
        ...


    def getf(self, buffer: "ByteBuffer") -> "ByteBuffer":
        ...


    def getf(self, index: int, buffer: "ByteBuffer") -> "ByteBuffer":
        ...


    def get(self, buffer: "FloatBuffer") -> "FloatBuffer":
        ...


    def get(self, index: int, buffer: "FloatBuffer") -> "FloatBuffer":
        ...


    def getToAddress(self, address: int) -> "Vector3dc":
        ...


    def sub(self, v: "Vector3dc") -> "Vector3d":
        """
        Subtract the supplied vector from this one.

        Arguments
        - v: the vector to subtract from this

        Returns
        - this
        """
        ...


    def sub(self, v: "Vector3dc", dest: "Vector3d") -> "Vector3d":
        ...


    def sub(self, v: "Vector3fc") -> "Vector3d":
        """
        Subtract the supplied vector from this one.

        Arguments
        - v: the vector to subtract from this

        Returns
        - this
        """
        ...


    def sub(self, v: "Vector3fc", dest: "Vector3d") -> "Vector3d":
        ...


    def sub(self, x: float, y: float, z: float) -> "Vector3d":
        """
        Subtract `(x, y, z)` from this vector.

        Arguments
        - x: the x component to subtract
        - y: the y component to subtract
        - z: the z component to subtract

        Returns
        - this
        """
        ...


    def sub(self, x: float, y: float, z: float, dest: "Vector3d") -> "Vector3d":
        ...


    def add(self, v: "Vector3dc") -> "Vector3d":
        """
        Add the supplied vector to this one.

        Arguments
        - v: the vector to add

        Returns
        - this
        """
        ...


    def add(self, v: "Vector3dc", dest: "Vector3d") -> "Vector3d":
        ...


    def add(self, v: "Vector3fc") -> "Vector3d":
        """
        Add the supplied vector to this one.

        Arguments
        - v: the vector to add

        Returns
        - this
        """
        ...


    def add(self, v: "Vector3fc", dest: "Vector3d") -> "Vector3d":
        ...


    def add(self, x: float, y: float, z: float) -> "Vector3d":
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


    def add(self, x: float, y: float, z: float, dest: "Vector3d") -> "Vector3d":
        ...


    def fma(self, a: "Vector3dc", b: "Vector3dc") -> "Vector3d":
        """
        Add the component-wise multiplication of `a * b` to this vector.

        Arguments
        - a: the first multiplicand
        - b: the second multiplicand

        Returns
        - this
        """
        ...


    def fma(self, a: float, b: "Vector3dc") -> "Vector3d":
        """
        Add the component-wise multiplication of `a * b` to this vector.

        Arguments
        - a: the first multiplicand
        - b: the second multiplicand

        Returns
        - this
        """
        ...


    def fma(self, a: "Vector3fc", b: "Vector3fc") -> "Vector3d":
        """
        Add the component-wise multiplication of `a * b` to this vector.

        Arguments
        - a: the first multiplicand
        - b: the second multiplicand

        Returns
        - this
        """
        ...


    def fma(self, a: "Vector3fc", b: "Vector3fc", dest: "Vector3d") -> "Vector3d":
        ...


    def fma(self, a: float, b: "Vector3fc") -> "Vector3d":
        """
        Add the component-wise multiplication of `a * b` to this vector.

        Arguments
        - a: the first multiplicand
        - b: the second multiplicand

        Returns
        - this
        """
        ...


    def fma(self, a: "Vector3dc", b: "Vector3dc", dest: "Vector3d") -> "Vector3d":
        ...


    def fma(self, a: float, b: "Vector3dc", dest: "Vector3d") -> "Vector3d":
        ...


    def fma(self, a: "Vector3dc", b: "Vector3fc", dest: "Vector3d") -> "Vector3d":
        ...


    def fma(self, a: float, b: "Vector3fc", dest: "Vector3d") -> "Vector3d":
        ...


    def mulAdd(self, a: "Vector3dc", b: "Vector3dc") -> "Vector3d":
        """
        Add the component-wise multiplication of `this * a` to `b`
        and store the result in `this`.

        Arguments
        - a: the multiplicand
        - b: the addend

        Returns
        - this
        """
        ...


    def mulAdd(self, a: float, b: "Vector3dc") -> "Vector3d":
        """
        Add the component-wise multiplication of `this * a` to `b`
        and store the result in `this`.

        Arguments
        - a: the multiplicand
        - b: the addend

        Returns
        - this
        """
        ...


    def mulAdd(self, a: "Vector3dc", b: "Vector3dc", dest: "Vector3d") -> "Vector3d":
        ...


    def mulAdd(self, a: float, b: "Vector3dc", dest: "Vector3d") -> "Vector3d":
        ...


    def mulAdd(self, a: "Vector3fc", b: "Vector3dc", dest: "Vector3d") -> "Vector3d":
        ...


    def mul(self, v: "Vector3dc") -> "Vector3d":
        """
        Multiply this vector component-wise by another Vector3dc.

        Arguments
        - v: the vector to multiply by

        Returns
        - this
        """
        ...


    def mul(self, v: "Vector3fc") -> "Vector3d":
        """
        Multiply this vector component-wise by another Vector3fc.

        Arguments
        - v: the vector to multiply by

        Returns
        - this
        """
        ...


    def mul(self, v: "Vector3fc", dest: "Vector3d") -> "Vector3d":
        ...


    def mul(self, v: "Vector3dc", dest: "Vector3d") -> "Vector3d":
        ...


    def div(self, v: "Vector3dc") -> "Vector3d":
        """
        Divide this vector component-wise by another Vector3dc.

        Arguments
        - v: the vector to divide by

        Returns
        - this
        """
        ...


    def div(self, v: "Vector3fc") -> "Vector3d":
        """
        Divide this vector component-wise by another Vector3fc.

        Arguments
        - v: the vector to divide by

        Returns
        - this
        """
        ...


    def div(self, v: "Vector3fc", dest: "Vector3d") -> "Vector3d":
        ...


    def div(self, v: "Vector3dc", dest: "Vector3d") -> "Vector3d":
        ...


    def mulProject(self, mat: "Matrix4dc", w: float, dest: "Vector3d") -> "Vector3d":
        ...


    def mulProject(self, mat: "Matrix4dc") -> "Vector3d":
        """
        Multiply the given matrix `mat` with this vector and perform perspective division.
        
        This method uses `w=1.0` as the fourth vector component.
        
        Note that this method performs the operation `M * this`, where `M` is the provided matrix
        and thus interprets `this` as a *column* vector.

        Arguments
        - mat: the matrix to multiply this vector by

        Returns
        - this
        """
        ...


    def mulProject(self, mat: "Matrix4dc", dest: "Vector3d") -> "Vector3d":
        ...


    def mulProject(self, mat: "Matrix4fc") -> "Vector3d":
        """
        Multiply the given matrix `mat` with this vector and perform perspective division.
        
        This method uses `w=1.0` as the fourth vector component.
        
        Note that this method performs the operation `M * this`, where `M` is the provided matrix
        and thus interprets `this` as a *column* vector.

        Arguments
        - mat: the matrix to multiply this vector by

        Returns
        - this
        """
        ...


    def mulProject(self, mat: "Matrix4fc", dest: "Vector3d") -> "Vector3d":
        ...


    def mulProjectTranslation(self, mat: "Matrix4dc") -> "Vector3d":
        """
        Multiply the given matrix `mat` with this vector and perform perspective division.
        
        This method assumes that the matrix `mat` represents only a translation.
        
        This method uses `w=1.0` as the fourth vector component.
        
        Note that this method performs the operation `M * this`, where `M` is the provided matrix
        and thus interprets `this` as a *column* vector.

        Arguments
        - mat: the matrix to multiply this vector by

        Returns
        - this
        """
        ...


    def mulProjectTranslation(self, mat: "Matrix4dc", dest: "Vector3d") -> "Vector3d":
        ...


    def mulProjectTranslation(self, mat: "Matrix4fc") -> "Vector3d":
        """
        Multiply the given matrix `mat` with this vector and perform perspective division.
        
        This method assumes that the matrix `mat` represents only a translation.
        
        This method uses `w=1.0` as the fourth vector component.
        
        Note that this method performs the operation `M * this`, where `M` is the provided matrix
        and thus interprets `this` as a *column* vector.

        Arguments
        - mat: the matrix to multiply this vector by

        Returns
        - this
        """
        ...


    def mulProjectTranslation(self, mat: "Matrix4fc", dest: "Vector3d") -> "Vector3d":
        ...


    def mulProjectAffine(self, mat: "Matrix4dc") -> "Vector3d":
        """
        Multiply the given matrix `mat` with this vector and perform perspective division.
        
        This method assumes that the matrix `mat` represents only an affine transformation.
        
        This method uses `w=1.0` as the fourth vector component.
        
        Note that this method performs the operation `M * this`, where `M` is the provided matrix
        and thus interprets `this` as a *column* vector.

        Arguments
        - mat: the matrix to multiply this vector by

        Returns
        - this
        """
        ...


    def mulProjectAffine(self, mat: "Matrix4dc", dest: "Vector3d") -> "Vector3d":
        ...


    def mulProjectAffine(self, mat: "Matrix4fc") -> "Vector3d":
        """
        Multiply the given matrix `mat` with this vector and perform perspective division.
        
        This method assumes that the matrix `mat` represents only an affine transformation.
        
        This method uses `w=1.0` as the fourth vector component.
        
        Note that this method performs the operation `M * this`, where `M` is the provided matrix
        and thus interprets `this` as a *column* vector.

        Arguments
        - mat: the matrix to multiply this vector by

        Returns
        - this
        """
        ...


    def mulProjectAffine(self, mat: "Matrix4fc", dest: "Vector3d") -> "Vector3d":
        ...


    def mulProjectGeneric(self, mat: "Matrix4dc") -> "Vector3d":
        """
        Multiply the given matrix `mat` with this vector and perform perspective division.
        
        This method makes no assumptions about the properties of the matrix `mat`.
        
        This method uses `w=1.0` as the fourth vector component.
        
        Note that this method performs the operation `M * this`, where `M` is the provided matrix
        and thus interprets `this` as a *column* vector.

        Arguments
        - mat: the matrix to multiply this vector by

        Returns
        - this
        """
        ...


    def mulProjectGeneric(self, mat: "Matrix4dc", dest: "Vector3d") -> "Vector3d":
        ...


    def mulProjectGeneric(self, mat: "Matrix4fc") -> "Vector3d":
        """
        Multiply the given matrix `mat` with this vector and perform perspective division.
        
        This method makes no assumptions about the properties of the matrix `mat`.
        
        This method uses `w=1.0` as the fourth vector component.
        
        Note that this method performs the operation `M * this`, where `M` is the provided matrix
        and thus interprets `this` as a *column* vector.

        Arguments
        - mat: the matrix to multiply this vector by

        Returns
        - this
        """
        ...


    def mulProjectGeneric(self, mat: "Matrix4fc", dest: "Vector3d") -> "Vector3d":
        ...


    def mul(self, mat: "Matrix3fc") -> "Vector3d":
        """
        Multiply the given matrix `mat` with this vector.

        Arguments
        - mat: the matrix to multiply this vector by

        Returns
        - this
        """
        ...


    def mul(self, mat: "Matrix3dc") -> "Vector3d":
        """
        Multiply the given matrix `mat` with this vector.

        Arguments
        - mat: the matrix to multiply this vector by

        Returns
        - this
        """
        ...


    def mul(self, mat: "Matrix3dc", dest: "Vector3d") -> "Vector3d":
        ...


    def mul(self, mat: "Matrix3dc", dest: "Vector3f") -> "Vector3f":
        ...


    def mul(self, mat: "Matrix3fc", dest: "Vector3d") -> "Vector3d":
        ...


    def mul(self, mat: "Matrix3x2dc") -> "Vector3d":
        """
        Multiply the given matrix with this vector by assuming a third row in the matrix of `(0, 0, 1)`
        and store the result in `this`.

        Arguments
        - mat: the matrix

        Returns
        - this
        """
        ...


    def mul(self, mat: "Matrix3x2dc", dest: "Vector3d") -> "Vector3d":
        ...


    def mul(self, mat: "Matrix3x2fc") -> "Vector3d":
        """
        Multiply the given matrix with this vector by assuming a third row in the matrix of `(0, 0, 1)`
        and store the result in `this`.

        Arguments
        - mat: the matrix

        Returns
        - this
        """
        ...


    def mul(self, mat: "Matrix3x2fc", dest: "Vector3d") -> "Vector3d":
        ...


    def mulTranspose(self, mat: "Matrix3dc") -> "Vector3d":
        """
        Multiply the transpose of the given matrix with this vector and store the result in `this`.
        
        Note that this method performs the operation `M^T * this`, where `M` is the provided matrix
        and thus interprets `this` as a *column* vector.

        Arguments
        - mat: the matrix

        Returns
        - this
        """
        ...


    def mulTranspose(self, mat: "Matrix3dc", dest: "Vector3d") -> "Vector3d":
        ...


    def mulTranspose(self, mat: "Matrix3fc") -> "Vector3d":
        """
        Multiply the transpose of the given matrix with this vector and store the result in `this`.
        
        Note that this method performs the operation `M^T * this`, where `M` is the provided matrix
        and thus interprets `this` as a *column* vector.

        Arguments
        - mat: the matrix

        Returns
        - this
        """
        ...


    def mulTranspose(self, mat: "Matrix3fc", dest: "Vector3d") -> "Vector3d":
        ...


    def mulPosition(self, mat: "Matrix4dc") -> "Vector3d":
        """
        Multiply the given 4x4 matrix `mat` with `this`.
        
        This method assumes the `w` component of `this` to be `1.0`.

        Arguments
        - mat: the matrix to multiply this vector by

        Returns
        - this
        """
        ...


    def mulPosition(self, mat: "Matrix4dc", dest: "Vector3d") -> "Vector3d":
        ...


    def mulPosition(self, mat: "Matrix4fc", dest: "Vector3d") -> "Vector3d":
        ...


    def mulPosition(self, mat: "Matrix4fc") -> "Vector3d":
        """
        Multiply the given 4x4 matrix `mat` with `this`.
        
        This method assumes the `w` component of `this` to be `1.0`.

        Arguments
        - mat: the matrix to multiply this vector by

        Returns
        - this
        """
        ...


    def mulPositionTranslation(self, mat: "Matrix4dc") -> "Vector3d":
        """
        Multiply the given 4x4 matrix `mat` with `this`.
        
        This method assumes that the matrix `mat` represents only a translation.
        
        This method assumes the `w` component of `this` to be `1.0`.
        
        Note that this method performs the operation `M * this`, where `M` is the provided matrix
        and thus interprets `this` as a *column* vector.

        Arguments
        - mat: the matrix to multiply this vector by

        Returns
        - this
        """
        ...


    def mulPositionTranslation(self, mat: "Matrix4dc", dest: "Vector3d") -> "Vector3d":
        ...


    def mulPositionTranslation(self, mat: "Matrix4fc") -> "Vector3d":
        """
        Multiply the given 4x4 matrix `mat` with `this`.
        
        This method assumes that the matrix `mat` represents only a translation.
        
        This method assumes the `w` component of `this` to be `1.0`.
        
        Note that this method performs the operation `M * this`, where `M` is the provided matrix
        and thus interprets `this` as a *column* vector.

        Arguments
        - mat: the matrix to multiply this vector by

        Returns
        - this
        """
        ...


    def mulPositionTranslation(self, mat: "Matrix4fc", dest: "Vector3d") -> "Vector3d":
        ...


    def mulPositionGeneric(self, mat: "Matrix4dc") -> "Vector3d":
        """
        Multiply the given 4x4 matrix `mat` with `this`.
        
        This method makes no assumptions about the properties of the matrix `mat`.
        
        This method assumes the `w` component of `this` to be `1.0`.
        
        Note that this method performs the operation `M * this`, where `M` is the provided matrix
        and thus interprets `this` as a *column* vector.

        Arguments
        - mat: the matrix to multiply this vector by

        Returns
        - this
        """
        ...


    def mulPositionGeneric(self, mat: "Matrix4dc", dest: "Vector3d") -> "Vector3d":
        ...


    def mulPositionGeneric(self, mat: "Matrix4fc") -> "Vector3d":
        """
        Multiply the given 4x4 matrix `mat` with `this`.
        
        This method makes no assumptions about the properties of the matrix `mat`.
        
        This method assumes the `w` component of `this` to be `1.0`.
        
        Note that this method performs the operation `M * this`, where `M` is the provided matrix
        and thus interprets `this` as a *column* vector.

        Arguments
        - mat: the matrix to multiply this vector by

        Returns
        - this
        """
        ...


    def mulPositionGeneric(self, mat: "Matrix4fc", dest: "Vector3d") -> "Vector3d":
        ...


    def mulPosition(self, mat: "Matrix4x3dc") -> "Vector3d":
        """
        Multiply the given 4x3 matrix `mat` with `this`.
        
        This method assumes the `w` component of `this` to be `1.0`.

        Arguments
        - mat: the matrix to multiply this vector by

        Returns
        - this
        """
        ...


    def mulPositionTranslation(self, mat: "Matrix4x3dc", dest: "Vector3d") -> "Vector3d":
        ...


    def mulPositionTranslation(self, mat: "Matrix4x3dc") -> "Vector3d":
        """
        Multiply the given 4x3 matrix `mat`, representing only a translation, with `this`.
        
        This method only works when `mat` only represents a translation.
        
        This method assumes the `w` component of `this` to be `1.0`.

        Arguments
        - mat: the matrix to multiply this vector by

        Returns
        - this
        """
        ...


    def mulPositionGeneric(self, mat: "Matrix4x3dc", dest: "Vector3d") -> "Vector3d":
        ...


    def mulPositionGeneric(self, mat: "Matrix4x3dc") -> "Vector3d":
        """
        Multiply the given 4x3 matrix `mat` with `this`.
        
        This method makes no assumptions about the properties of the matrix `mat`.
        
        This method assumes the `w` component of `this` to be `1.0`.

        Arguments
        - mat: the matrix to multiply this vector by

        Returns
        - this
        """
        ...


    def mulPosition(self, mat: "Matrix4x3fc") -> "Vector3d":
        """
        Multiply the given 4x3 matrix `mat` with `this`.
        
        This method assumes the `w` component of `this` to be `1.0`.

        Arguments
        - mat: the matrix to multiply this vector by

        Returns
        - this
        """
        ...


    def mulPositionTranslation(self, mat: "Matrix4x3fc") -> "Vector3d":
        """
        Multiply the given 4x3 matrix `mat`, representing only a translation, with `this`.
        
        This method only works when `mat` only represents a translation.
        
        This method assumes the `w` component of `this` to be `1.0`.

        Arguments
        - mat: the matrix to multiply this vector by

        Returns
        - this
        """
        ...


    def mulPositionTranslation(self, mat: "Matrix4x3fc", dest: "Vector3d") -> "Vector3d":
        ...


    def mulPositionGeneric(self, mat: "Matrix4x3fc") -> "Vector3d":
        """
        Multiply the given 4x3 matrix `mat` with `this`.
        
        This method makes no assumptions about the properties of the matrix `mat`.
        
        This method assumes the `w` component of `this` to be `1.0`.

        Arguments
        - mat: the matrix to multiply this vector by

        Returns
        - this
        """
        ...


    def mulPositionGeneric(self, mat: "Matrix4x3fc", dest: "Vector3d") -> "Vector3d":
        ...


    def mulPosition(self, mat: "Matrix4x3dc", dest: "Vector3d") -> "Vector3d":
        ...


    def mulPosition(self, mat: "Matrix4x3fc", dest: "Vector3d") -> "Vector3d":
        ...


    def mulTransposePosition(self, mat: "Matrix4dc") -> "Vector3d":
        """
        Multiply the transpose of the given 4x4 matrix `mat` with `this`.
        
        This method assumes the `w` component of `this` to be `1.0`.
        
        Note that this method performs the operation `M^T * this`, where `M` is the provided matrix
        and thus interprets `this` as a *column* vector.

        Arguments
        - mat: the matrix whose transpose to multiply this vector by

        Returns
        - this
        """
        ...


    def mulTransposePosition(self, mat: "Matrix4dc", dest: "Vector3d") -> "Vector3d":
        ...


    def mulTransposePosition(self, mat: "Matrix4fc") -> "Vector3d":
        """
        Multiply the transpose of the given 4x4 matrix `mat` with `this`.
        
        This method assumes the `w` component of `this` to be `1.0`.
        
        Note that this method performs the operation `M^T * this`, where `M` is the provided matrix
        and thus interprets `this` as a *column* vector.

        Arguments
        - mat: the matrix whose transpose to multiply this vector by

        Returns
        - this
        """
        ...


    def mulTransposePosition(self, mat: "Matrix4fc", dest: "Vector3d") -> "Vector3d":
        ...


    def mulPositionW(self, mat: "Matrix4fc") -> float:
        """
        Multiply the given 4x4 matrix `mat` with `this` and return the *w* component
        of the resulting 4D vector.
        
        This method assumes the `w` component of `this` to be `1.0`.

        Arguments
        - mat: the matrix to multiply this vector by

        Returns
        - the *w* component of the resulting 4D vector after multiplication
        """
        ...


    def mulPositionW(self, mat: "Matrix4fc", dest: "Vector3d") -> float:
        ...


    def mulPositionW(self, mat: "Matrix4dc") -> float:
        """
        Multiply the given 4x4 matrix `mat` with `this` and return the *w* component
        of the resulting 4D vector.
        
        This method assumes the `w` component of `this` to be `1.0`.

        Arguments
        - mat: the matrix to multiply this vector by

        Returns
        - the *w* component of the resulting 4D vector after multiplication
        """
        ...


    def mulPositionW(self, mat: "Matrix4dc", dest: "Vector3d") -> float:
        ...


    def mulDirection(self, mat: "Matrix4fc") -> "Vector3d":
        """
        Multiply the given 4x4 matrix `mat` with `this`.
        
        This method assumes the `w` component of `this` to be `0.0`.

        Arguments
        - mat: the matrix to multiply this vector by

        Returns
        - this
        """
        ...


    def mulDirection(self, mat: "Matrix4dc") -> "Vector3d":
        """
        Multiply the given 4x4 matrix `mat` with `this`.
        
        This method assumes the `w` component of `this` to be `0.0`.

        Arguments
        - mat: the matrix to multiply this vector by

        Returns
        - this
        """
        ...


    def mulDirection(self, mat: "Matrix4x3dc") -> "Vector3d":
        """
        Multiply the given 4x3 matrix `mat` with `this`.
        
        This method assumes the `w` component of `this` to be `0.0`.

        Arguments
        - mat: the matrix to multiply this vector by

        Returns
        - this
        """
        ...


    def mulDirection(self, mat: "Matrix4x3fc") -> "Vector3d":
        """
        Multiply the given 4x3 matrix `mat` with `this`.
        
        This method assumes the `w` component of `this` to be `0.0`.

        Arguments
        - mat: the matrix to multiply this vector by

        Returns
        - this
        """
        ...


    def mulDirection(self, mat: "Matrix4dc", dest: "Vector3d") -> "Vector3d":
        ...


    def mulDirection(self, mat: "Matrix4fc", dest: "Vector3d") -> "Vector3d":
        ...


    def mulDirection(self, mat: "Matrix4x3dc", dest: "Vector3d") -> "Vector3d":
        ...


    def mulDirection(self, mat: "Matrix4x3fc", dest: "Vector3d") -> "Vector3d":
        ...


    def mulTransposeDirection(self, mat: "Matrix4dc") -> "Vector3d":
        """
        Multiply the transpose of the given 4x4 matrix `mat` with `this`.
        
        This method assumes the `w` component of `this` to be `0.0`.
        
        Note that this method performs the operation `M^T * this`, where `M` is the provided matrix
        and thus interprets `this` as a *column* vector.

        Arguments
        - mat: the matrix whose transpose to multiply this vector by

        Returns
        - this
        """
        ...


    def mulTransposeDirection(self, mat: "Matrix4dc", dest: "Vector3d") -> "Vector3d":
        ...


    def mulTransposeDirection(self, mat: "Matrix4fc") -> "Vector3d":
        """
        Multiply the transpose of the given 4x4 matrix `mat` with `this`.
        
        This method assumes the `w` component of `this` to be `0.0`.
        
        Note that this method performs the operation `M^T * this`, where `M` is the provided matrix
        and thus interprets `this` as a *column* vector.

        Arguments
        - mat: the matrix whose transpose to multiply this vector by

        Returns
        - this
        """
        ...


    def mulTransposeDirection(self, mat: "Matrix4fc", dest: "Vector3d") -> "Vector3d":
        ...


    def mul(self, scalar: float) -> "Vector3d":
        """
        Multiply this vector by the given scalar value.

        Arguments
        - scalar: the scalar to multiply this vector by

        Returns
        - this
        """
        ...


    def mul(self, scalar: float, dest: "Vector3d") -> "Vector3d":
        ...


    def mul(self, x: float, y: float, z: float) -> "Vector3d":
        """
        Multiply the components of this vector by the given scalar values and store the result in `this`.

        Arguments
        - x: the x component to multiply this vector by
        - y: the y component to multiply this vector by
        - z: the z component to multiply this vector by

        Returns
        - this
        """
        ...


    def mul(self, x: float, y: float, z: float, dest: "Vector3d") -> "Vector3d":
        ...


    def rotate(self, quat: "Quaterniondc") -> "Vector3d":
        """
        Rotate this vector by the given quaternion `quat` and store the result in `this`.

        Arguments
        - quat: the quaternion to rotate this vector

        Returns
        - this

        See
        - Quaterniond.transform(Vector3d)
        """
        ...


    def rotate(self, quat: "Quaterniondc", dest: "Vector3d") -> "Vector3d":
        ...


    def rotationTo(self, toDir: "Vector3dc", dest: "Quaterniond") -> "Quaterniond":
        ...


    def rotationTo(self, toDirX: float, toDirY: float, toDirZ: float, dest: "Quaterniond") -> "Quaterniond":
        ...


    def rotateAxis(self, angle: float, x: float, y: float, z: float) -> "Vector3d":
        """
        Rotate this vector the specified radians around the given rotation axis.
        
        If the rotation axis is either `(1, 0, 0)`, `(0, 1, 0)` or `(0, 0, 1)`,
        then .rotateX(double) rotateX(), .rotateY(double) rotateY() or
        .rotateZ(double) rotateZ(), respectively, should be used instead.

        Arguments
        - angle: the angle in radians
        - x: the x component of the rotation axis
        - y: the y component of the rotation axis
        - z: the z component of the rotation axis

        Returns
        - this
        """
        ...


    def rotateAxis(self, angle: float, aX: float, aY: float, aZ: float, dest: "Vector3d") -> "Vector3d":
        ...


    def rotateX(self, angle: float) -> "Vector3d":
        """
        Rotate this vector the specified radians around the X axis.

        Arguments
        - angle: the angle in radians

        Returns
        - this
        """
        ...


    def rotateX(self, angle: float, dest: "Vector3d") -> "Vector3d":
        ...


    def rotateY(self, angle: float) -> "Vector3d":
        """
        Rotate this vector the specified radians around the Y axis.

        Arguments
        - angle: the angle in radians

        Returns
        - this
        """
        ...


    def rotateY(self, angle: float, dest: "Vector3d") -> "Vector3d":
        ...


    def rotateZ(self, angle: float) -> "Vector3d":
        """
        Rotate this vector the specified radians around the Z axis.

        Arguments
        - angle: the angle in radians

        Returns
        - this
        """
        ...


    def rotateZ(self, angle: float, dest: "Vector3d") -> "Vector3d":
        ...


    def div(self, scalar: float) -> "Vector3d":
        """
        Divide this vector by the given scalar value.

        Arguments
        - scalar: the scalar to divide this vector by

        Returns
        - this
        """
        ...


    def div(self, scalar: float, dest: "Vector3d") -> "Vector3d":
        ...


    def div(self, x: float, y: float, z: float) -> "Vector3d":
        """
        Divide the components of this vector by the given scalar values and store the result in `this`.

        Arguments
        - x: the x component to divide this vector by
        - y: the y component to divide this vector by
        - z: the z component to divide this vector by

        Returns
        - this
        """
        ...


    def div(self, x: float, y: float, z: float, dest: "Vector3d") -> "Vector3d":
        ...


    def lengthSquared(self) -> float:
        ...


    @staticmethod
    def lengthSquared(x: float, y: float, z: float) -> float:
        """
        Get the length squared of a 3-dimensional double-precision vector.

    Author(s)
        - F. Neurath

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
    def length(x: float, y: float, z: float) -> float:
        """
        Get the length of a 3-dimensional double-precision vector.

    Author(s)
        - F. Neurath

        Arguments
        - x: The vector's x component
        - y: The vector's y component
        - z: The vector's z component

        Returns
        - the length of the given vector
        """
        ...


    def normalize(self) -> "Vector3d":
        """
        Normalize this vector.

        Returns
        - this
        """
        ...


    def normalize(self, dest: "Vector3d") -> "Vector3d":
        ...


    def normalize(self, length: float) -> "Vector3d":
        """
        Scale this vector to have the given length.

        Arguments
        - length: the desired length

        Returns
        - this
        """
        ...


    def normalize(self, length: float, dest: "Vector3d") -> "Vector3d":
        ...


    def cross(self, v: "Vector3dc") -> "Vector3d":
        """
        Set this vector to be the cross product of this and v2.

        Arguments
        - v: the other vector

        Returns
        - this
        """
        ...


    def cross(self, x: float, y: float, z: float) -> "Vector3d":
        """
        Set this vector to be the cross product of itself and `(x, y, z)`.

        Arguments
        - x: the x component of the other vector
        - y: the y component of the other vector
        - z: the z component of the other vector

        Returns
        - this
        """
        ...


    def cross(self, v: "Vector3dc", dest: "Vector3d") -> "Vector3d":
        ...


    def cross(self, x: float, y: float, z: float, dest: "Vector3d") -> "Vector3d":
        ...


    def distance(self, v: "Vector3dc") -> float:
        ...


    def distance(self, x: float, y: float, z: float) -> float:
        ...


    def distanceSquared(self, v: "Vector3dc") -> float:
        ...


    def distanceSquared(self, x: float, y: float, z: float) -> float:
        ...


    @staticmethod
    def distance(x1: float, y1: float, z1: float, x2: float, y2: float, z2: float) -> float:
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
    def distanceSquared(x1: float, y1: float, z1: float, x2: float, y2: float, z2: float) -> float:
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


    def dot(self, v: "Vector3dc") -> float:
        ...


    def dot(self, x: float, y: float, z: float) -> float:
        ...


    def angleCos(self, v: "Vector3dc") -> float:
        ...


    def angle(self, v: "Vector3dc") -> float:
        ...


    def angleSigned(self, v: "Vector3dc", n: "Vector3dc") -> float:
        ...


    def angleSigned(self, x: float, y: float, z: float, nx: float, ny: float, nz: float) -> float:
        ...


    def min(self, v: "Vector3dc") -> "Vector3d":
        """
        Set the components of this vector to be the component-wise minimum of this and the other vector.

        Arguments
        - v: the other vector

        Returns
        - this
        """
        ...


    def min(self, v: "Vector3dc", dest: "Vector3d") -> "Vector3d":
        ...


    def max(self, v: "Vector3dc") -> "Vector3d":
        """
        Set the components of this vector to be the component-wise maximum of this and the other vector.

        Arguments
        - v: the other vector

        Returns
        - this
        """
        ...


    def max(self, v: "Vector3dc", dest: "Vector3d") -> "Vector3d":
        ...


    def zero(self) -> "Vector3d":
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


    def negate(self) -> "Vector3d":
        """
        Negate this vector.

        Returns
        - this
        """
        ...


    def negate(self, dest: "Vector3d") -> "Vector3d":
        ...


    def absolute(self) -> "Vector3d":
        """
        Set `this` vector's components to their respective absolute values.

        Returns
        - this
        """
        ...


    def absolute(self, dest: "Vector3d") -> "Vector3d":
        ...


    def hashCode(self) -> int:
        ...


    def equals(self, obj: "Object") -> bool:
        ...


    def equals(self, v: "Vector3dc", delta: float) -> bool:
        ...


    def equals(self, x: float, y: float, z: float) -> bool:
        ...


    def reflect(self, normal: "Vector3dc") -> "Vector3d":
        """
        Reflect this vector about the given normal vector.

        Arguments
        - normal: the vector to reflect about

        Returns
        - this
        """
        ...


    def reflect(self, x: float, y: float, z: float) -> "Vector3d":
        """
        Reflect this vector about the given normal vector.

        Arguments
        - x: the x component of the normal
        - y: the y component of the normal
        - z: the z component of the normal

        Returns
        - this
        """
        ...


    def reflect(self, normal: "Vector3dc", dest: "Vector3d") -> "Vector3d":
        ...


    def reflect(self, x: float, y: float, z: float, dest: "Vector3d") -> "Vector3d":
        ...


    def half(self, other: "Vector3dc") -> "Vector3d":
        """
        Compute the half vector between this and the other vector.

        Arguments
        - other: the other vector

        Returns
        - this
        """
        ...


    def half(self, x: float, y: float, z: float) -> "Vector3d":
        """
        Compute the half vector between this and the vector `(x, y, z)`.

        Arguments
        - x: the x component of the other vector
        - y: the y component of the other vector
        - z: the z component of the other vector

        Returns
        - this
        """
        ...


    def half(self, other: "Vector3dc", dest: "Vector3d") -> "Vector3d":
        ...


    def half(self, x: float, y: float, z: float, dest: "Vector3d") -> "Vector3d":
        ...


    def smoothStep(self, v: "Vector3dc", t: float, dest: "Vector3d") -> "Vector3d":
        ...


    def hermite(self, t0: "Vector3dc", v1: "Vector3dc", t1: "Vector3dc", t: float, dest: "Vector3d") -> "Vector3d":
        ...


    def lerp(self, other: "Vector3dc", t: float) -> "Vector3d":
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


    def lerp(self, other: "Vector3dc", t: float, dest: "Vector3d") -> "Vector3d":
        ...


    def get(self, component: int) -> float:
        ...


    def get(self, mode: int, dest: "Vector3i") -> "Vector3i":
        ...


    def get(self, dest: "Vector3f") -> "Vector3f":
        ...


    def get(self, dest: "Vector3d") -> "Vector3d":
        ...


    def maxComponent(self) -> int:
        ...


    def minComponent(self) -> int:
        ...


    def orthogonalize(self, v: "Vector3dc", dest: "Vector3d") -> "Vector3d":
        ...


    def orthogonalize(self, v: "Vector3dc") -> "Vector3d":
        """
        Transform `this` vector so that it is orthogonal to the given vector `v` and normalize the result.
        
        Reference: <a href="https://en.wikipedia.org/wiki/Gram%E2%80%93Schmidt_process">Gram–Schmidt process</a>

        Arguments
        - v: the reference vector which the result should be orthogonal to

        Returns
        - this
        """
        ...


    def orthogonalizeUnit(self, v: "Vector3dc", dest: "Vector3d") -> "Vector3d":
        ...


    def orthogonalizeUnit(self, v: "Vector3dc") -> "Vector3d":
        """
        Transform `this` vector so that it is orthogonal to the given unit vector `v` and normalize the result.
        
        The vector `v` is assumed to be a .normalize() unit vector.
        
        Reference: <a href="https://en.wikipedia.org/wiki/Gram%E2%80%93Schmidt_process">Gram–Schmidt process</a>

        Arguments
        - v: the reference unit vector which the result should be orthogonal to

        Returns
        - this
        """
        ...


    def floor(self) -> "Vector3d":
        """
        Set each component of this vector to the largest (closest to positive
        infinity) `double` value that is less than or equal to that
        component and is equal to a mathematical integer.

        Returns
        - this
        """
        ...


    def floor(self, dest: "Vector3d") -> "Vector3d":
        ...


    def ceil(self) -> "Vector3d":
        """
        Set each component of this vector to the smallest (closest to negative
        infinity) `double` value that is greater than or equal to that
        component and is equal to a mathematical integer.

        Returns
        - this
        """
        ...


    def ceil(self, dest: "Vector3d") -> "Vector3d":
        ...


    def round(self) -> "Vector3d":
        """
        Set each component of this vector to the closest double that is equal to
        a mathematical integer, with ties rounding to positive infinity.

        Returns
        - this
        """
        ...


    def round(self, dest: "Vector3d") -> "Vector3d":
        ...


    def isFinite(self) -> bool:
        ...


    def clone(self) -> "Object":
        ...
