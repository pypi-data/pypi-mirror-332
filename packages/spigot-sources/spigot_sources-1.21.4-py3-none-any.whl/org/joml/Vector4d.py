"""
Python module generated from Java source file org.joml.Vector4d

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


class Vector4d(Externalizable, Cloneable, Vector4dc):
    """
    Contains the definition of a Vector comprising 4 doubles and associated transformations.

    Author(s)
    - F. Neurath
    """

    def __init__(self):
        """
        Create a new Vector4d of `(0, 0, 0, 1)`.
        """
        ...


    def __init__(self, v: "Vector4dc"):
        """
        Create a new Vector4d with the same values as `v`.

        Arguments
        - v: the Vector4dc to copy the values from
        """
        ...


    def __init__(self, v: "Vector4ic"):
        """
        Create a new Vector4d with the same values as `v`.

        Arguments
        - v: the Vector4ic to copy the values from
        """
        ...


    def __init__(self, v: "Vector3dc", w: float):
        """
        Create a new Vector4d with the first three components from the
        given `v` and the given `w`.

        Arguments
        - v: the Vector3dc
        - w: the w component
        """
        ...


    def __init__(self, v: "Vector3ic", w: float):
        """
        Create a new Vector4d with the first three components from the
        given `v` and the given `w`.

        Arguments
        - v: the Vector3ic
        - w: the w component
        """
        ...


    def __init__(self, v: "Vector2dc", z: float, w: float):
        """
        Create a new Vector4d with the first two components from the
        given `v` and the given `z` and `w`.

        Arguments
        - v: the Vector2dc
        - z: the z component
        - w: the w component
        """
        ...


    def __init__(self, v: "Vector2ic", z: float, w: float):
        """
        Create a new Vector4d with the first two components from the
        given `v` and the given `z` and `w`.

        Arguments
        - v: the Vector2ic
        - z: the z component
        - w: the w component
        """
        ...


    def __init__(self, d: float):
        """
        Create a new Vector4d and initialize all four components with the given value.

        Arguments
        - d: the value of all four components
        """
        ...


    def __init__(self, v: "Vector4fc"):
        """
        Create a new Vector4d with the same values as `v`.

        Arguments
        - v: the Vector4fc to copy the values from
        """
        ...


    def __init__(self, v: "Vector3fc", w: float):
        """
        Create a new Vector4d with the x, y, and z components from the
        given `v` and the w component from the given `w`.

        Arguments
        - v: the Vector3fc
        - w: the w component
        """
        ...


    def __init__(self, v: "Vector2fc", z: float, w: float):
        """
        Create a new Vector4d with the x and y components from the
        given `v` and the z and w components from the given `z` and `w`.

        Arguments
        - v: the Vector2fc
        - z: the z component
        - w: the w component
        """
        ...


    def __init__(self, x: float, y: float, z: float, w: float):
        """
        Create a new Vector4d with the given component values.

        Arguments
        - x: the x component
        - y: the y component
        - z: the z component
        - w: the w component
        """
        ...


    def __init__(self, xyzw: list[float]):
        """
        Create a new Vector4d and initialize its four components from the first
        four elements of the given array.

        Arguments
        - xyzw: the array containing at least four elements
        """
        ...


    def __init__(self, xyzw: list[float]):
        """
        Create a new Vector4d and initialize its four components from the first
        four elements of the given array.

        Arguments
        - xyzw: the array containing at least four elements
        """
        ...


    def __init__(self, buffer: "ByteBuffer"):
        """
        Create a new Vector4d and read this vector from the supplied ByteBuffer
        at the current buffer ByteBuffer.position() position.
        
        This method will not increment the position of the given ByteBuffer.
        
        In order to specify the offset into the ByteBuffer at which
        the vector is read, use .Vector4d(int, ByteBuffer), taking
        the absolute position as parameter.

        Arguments
        - buffer: values will be read in `x, y, z, w` order

        See
        - .Vector4d(int, ByteBuffer)
        """
        ...


    def __init__(self, index: int, buffer: "ByteBuffer"):
        """
        Create a new Vector4d and read this vector from the supplied ByteBuffer
        starting at the specified absolute buffer position/index.
        
        This method will not increment the position of the given ByteBuffer.

        Arguments
        - index: the absolute position into the ByteBuffer
        - buffer: values will be read in `x, y, z, w` order
        """
        ...


    def __init__(self, buffer: "DoubleBuffer"):
        """
        Create a new Vector4d and read this vector from the supplied DoubleBuffer
        at the current buffer DoubleBuffer.position() position.
        
        This method will not increment the position of the given DoubleBuffer.
        
        In order to specify the offset into the DoubleBuffer at which
        the vector is read, use .Vector4d(int, DoubleBuffer), taking
        the absolute position as parameter.

        Arguments
        - buffer: values will be read in `x, y, z, w` order

        See
        - .Vector4d(int, DoubleBuffer)
        """
        ...


    def __init__(self, index: int, buffer: "DoubleBuffer"):
        """
        Create a new Vector4d and read this vector from the supplied DoubleBuffer
        starting at the specified absolute buffer position/index.
        
        This method will not increment the position of the given DoubleBuffer.

        Arguments
        - index: the absolute position into the DoubleBuffer
        - buffer: values will be read in `x, y, z, w` order
        """
        ...


    def x(self) -> float:
        ...


    def y(self) -> float:
        ...


    def z(self) -> float:
        ...


    def w(self) -> float:
        ...


    def xyz(self, dest: "Vector3f") -> "Vector3f":
        """
        Copy the `(x, y, z)` components of `this` into the supplied `dest` vector
        and return it.
        
        Note that due to the given vector `dest` storing the components in float-precision,
        there is the possibility to lose precision.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def xyz(self, dest: "Vector3d") -> "Vector3d":
        """
        Copy the `(x, y, z)` components of `this` into the supplied `dest` vector
        and return it.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
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


    def set(self, v: "Vector4dc") -> "Vector4d":
        """
        Set this vector to the values of the given `v`.

        Arguments
        - v: the vector whose values will be copied into this

        Returns
        - this
        """
        ...


    def set(self, v: "Vector4fc") -> "Vector4d":
        """
        Set this vector to the values of the given `v`.

        Arguments
        - v: the vector whose values will be copied into this

        Returns
        - this
        """
        ...


    def set(self, v: "Vector4ic") -> "Vector4d":
        """
        Set this vector to the values of the given `v`.

        Arguments
        - v: the vector whose values will be copied into this

        Returns
        - this
        """
        ...


    def set(self, v: "Vector3dc", w: float) -> "Vector4d":
        """
        Set the x, y, and z components of this to the components of
        `v` and the w component to `w`.

        Arguments
        - v: the Vector3dc to copy
        - w: the w component

        Returns
        - this
        """
        ...


    def set(self, v: "Vector3ic", w: float) -> "Vector4d":
        """
        Set the x, y, and z components of this to the components of
        `v` and the w component to `w`.

        Arguments
        - v: the Vector3ic to copy
        - w: the w component

        Returns
        - this
        """
        ...


    def set(self, v: "Vector3fc", w: float) -> "Vector4d":
        """
        Set the x, y, and z components of this to the components of
        `v` and the w component to `w`.

        Arguments
        - v: the Vector3fc to copy
        - w: the w component

        Returns
        - this
        """
        ...


    def set(self, v: "Vector2dc", z: float, w: float) -> "Vector4d":
        """
        Set the x and y components from the given `v`
        and the z and w components to the given `z` and `w`.

        Arguments
        - v: the Vector2dc
        - z: the z component
        - w: the w component

        Returns
        - this
        """
        ...


    def set(self, v: "Vector2ic", z: float, w: float) -> "Vector4d":
        """
        Set the x and y components from the given `v`
        and the z and w components to the given `z` and `w`.

        Arguments
        - v: the Vector2ic
        - z: the z component
        - w: the w component

        Returns
        - this
        """
        ...


    def set(self, d: float) -> "Vector4d":
        """
        Set the x, y, z, and w components to the supplied value.

        Arguments
        - d: the value of all four components

        Returns
        - this
        """
        ...


    def set(self, v: "Vector2fc", z: float, w: float) -> "Vector4d":
        """
        Set the x and y components from the given `v`
        and the z and w components to the given `z` and `w`.

        Arguments
        - v: the Vector2fc
        - z: the z components
        - w: the w components

        Returns
        - this
        """
        ...


    def set(self, x: float, y: float, z: float, w: float) -> "Vector4d":
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


    def set(self, x: float, y: float, z: float) -> "Vector4d":
        """
        Set the x, y, z components to the supplied values.

        Arguments
        - x: the x component
        - y: the y component
        - z: the z component

        Returns
        - this
        """
        ...


    def set(self, xyzw: list[float]) -> "Vector4d":
        """
        Set the four components of this vector to the first four elements of the given array.

        Arguments
        - xyzw: the array containing at least four elements

        Returns
        - this
        """
        ...


    def set(self, xyzw: list[float]) -> "Vector4d":
        """
        Set the four components of this vector to the first four elements of the given array.

        Arguments
        - xyzw: the array containing at least four elements

        Returns
        - this
        """
        ...


    def set(self, buffer: "ByteBuffer") -> "Vector4d":
        """
        Read this vector from the supplied ByteBuffer at the current
        buffer ByteBuffer.position() position.
        
        This method will not increment the position of the given ByteBuffer.
        
        In order to specify the offset into the ByteBuffer at which
        the vector is read, use .set(int, ByteBuffer), taking
        the absolute position as parameter.

        Arguments
        - buffer: values will be read in `x, y, z, w` order

        Returns
        - this

        See
        - .set(int, ByteBuffer)
        """
        ...


    def set(self, index: int, buffer: "ByteBuffer") -> "Vector4d":
        """
        Read this vector from the supplied ByteBuffer starting at the specified
        absolute buffer position/index.
        
        This method will not increment the position of the given ByteBuffer.

        Arguments
        - index: the absolute position into the ByteBuffer
        - buffer: values will be read in `x, y, z, w` order

        Returns
        - this
        """
        ...


    def set(self, buffer: "DoubleBuffer") -> "Vector4d":
        """
        Read this vector from the supplied DoubleBuffer at the current
        buffer DoubleBuffer.position() position.
        
        This method will not increment the position of the given DoubleBuffer.
        
        In order to specify the offset into the DoubleBuffer at which
        the vector is read, use .set(int, DoubleBuffer), taking
        the absolute position as parameter.

        Arguments
        - buffer: values will be read in `x, y, z, w` order

        Returns
        - this

        See
        - .set(int, DoubleBuffer)
        """
        ...


    def set(self, index: int, buffer: "DoubleBuffer") -> "Vector4d":
        """
        Read this vector from the supplied DoubleBuffer starting at the specified
        absolute buffer position/index.
        
        This method will not increment the position of the given DoubleBuffer.

        Arguments
        - index: the absolute position into the DoubleBuffer
        - buffer: values will be read in `x, y, z, w` order

        Returns
        - this
        """
        ...


    def setFromAddress(self, address: int) -> "Vector4d":
        """
        Set the values of this vector by reading 4 double values from off-heap memory,
        starting at the given address.
        
        This method will throw an UnsupportedOperationException when JOML is used with `-Djoml.nounsafe`.
        
        *This method is unsafe as it can result in a crash of the JVM process when the specified address range does not belong to this process.*

        Arguments
        - address: the off-heap memory address to read the vector values from

        Returns
        - this
        """
        ...


    def setComponent(self, component: int, value: float) -> "Vector4d":
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


    def getToAddress(self, address: int) -> "Vector4dc":
        ...


    def sub(self, v: "Vector4dc") -> "Vector4d":
        """
        Subtract the supplied vector from this one.

        Arguments
        - v: the vector to subtract

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


    def sub(self, v: "Vector4fc") -> "Vector4d":
        """
        Subtract the supplied vector from this one.

        Arguments
        - v: the vector to subtract

        Returns
        - this
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


    def sub(self, x: float, y: float, z: float, w: float) -> "Vector4d":
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


    def sub(self, x: float, y: float, z: float, w: float, dest: "Vector4d") -> "Vector4d":
        ...


    def add(self, v: "Vector4dc") -> "Vector4d":
        """
        Add the supplied vector to this one.

        Arguments
        - v: the vector to add

        Returns
        - this
        """
        ...


    def add(self, v: "Vector4dc", dest: "Vector4d") -> "Vector4d":
        ...


    def add(self, v: "Vector4fc", dest: "Vector4d") -> "Vector4d":
        ...


    def add(self, x: float, y: float, z: float, w: float) -> "Vector4d":
        """
        Add `(x, y, z, w)` to this.

        Arguments
        - x: the x component to add
        - y: the y component to add
        - z: the z component to add
        - w: the w component to add

        Returns
        - this
        """
        ...


    def add(self, x: float, y: float, z: float, w: float, dest: "Vector4d") -> "Vector4d":
        ...


    def add(self, v: "Vector4fc") -> "Vector4d":
        """
        Add the supplied vector to this one.

        Arguments
        - v: the vector to add

        Returns
        - this
        """
        ...


    def fma(self, a: "Vector4dc", b: "Vector4dc") -> "Vector4d":
        """
        Add the component-wise multiplication of `a * b` to this vector.

        Arguments
        - a: the first multiplicand
        - b: the second multiplicand

        Returns
        - this
        """
        ...


    def fma(self, a: float, b: "Vector4dc") -> "Vector4d":
        """
        Add the component-wise multiplication of `a * b` to this vector.

        Arguments
        - a: the first multiplicand
        - b: the second multiplicand

        Returns
        - this
        """
        ...


    def fma(self, a: "Vector4dc", b: "Vector4dc", dest: "Vector4d") -> "Vector4d":
        ...


    def fma(self, a: float, b: "Vector4dc", dest: "Vector4d") -> "Vector4d":
        ...


    def mulAdd(self, a: "Vector4dc", b: "Vector4dc") -> "Vector4d":
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


    def mulAdd(self, a: float, b: "Vector4dc") -> "Vector4d":
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


    def mulAdd(self, a: "Vector4dc", b: "Vector4dc", dest: "Vector4d") -> "Vector4d":
        ...


    def mulAdd(self, a: float, b: "Vector4dc", dest: "Vector4d") -> "Vector4d":
        ...


    def mul(self, v: "Vector4dc") -> "Vector4d":
        """
        Multiply this vector component-wise by the given vector.

        Arguments
        - v: the vector to multiply by

        Returns
        - this
        """
        ...


    def mul(self, v: "Vector4dc", dest: "Vector4d") -> "Vector4d":
        ...


    def div(self, v: "Vector4dc") -> "Vector4d":
        """
        Divide this vector component-wise by the given Vector4dc.

        Arguments
        - v: the vector to divide by

        Returns
        - this
        """
        ...


    def div(self, v: "Vector4dc", dest: "Vector4d") -> "Vector4d":
        ...


    def mul(self, v: "Vector4fc") -> "Vector4d":
        """
        Multiply this vector component-wise by the given Vector4fc.

        Arguments
        - v: the vector to multiply by

        Returns
        - this
        """
        ...


    def mul(self, v: "Vector4fc", dest: "Vector4d") -> "Vector4d":
        ...


    def mul(self, mat: "Matrix4dc") -> "Vector4d":
        """
        Multiply the given matrix mat with this vector.
        
        Note that this method performs the operation `M * this`, where `M` is the provided matrix
        and thus interprets `this` as a *column* vector.

        Arguments
        - mat: the matrix to multiply `this` by

        Returns
        - this
        """
        ...


    def mul(self, mat: "Matrix4dc", dest: "Vector4d") -> "Vector4d":
        ...


    def mulTranspose(self, mat: "Matrix4dc") -> "Vector4d":
        """
        Multiply the transpose of the given matrix `mat` with this vector.
        
        Note that this method performs the operation `M^T * this`, where `M` is the provided matrix
        and thus interprets `this` as a *column* vector.

        Arguments
        - mat: the matrix whose transpose to multiply the vector with

        Returns
        - this
        """
        ...


    def mulTranspose(self, mat: "Matrix4dc", dest: "Vector4d") -> "Vector4d":
        ...


    def mulTranslation(self, mat: "Matrix4dc", dest: "Vector4d") -> "Vector4d":
        ...


    def mulTranslation(self, mat: "Matrix4fc", dest: "Vector4d") -> "Vector4d":
        ...


    def mulAffine(self, mat: "Matrix4dc", dest: "Vector4d") -> "Vector4d":
        ...


    def mulGeneric(self, mat: "Matrix4dc") -> "Vector4d":
        """
        Multiply the given matrix `mat` with this vector.
        
        This method does not make any assumptions or optimizations about the properties of the specified matrix.
        
        Note that this method performs the operation `M * this`, where `M` is the provided matrix
        and thus interprets `this` as a *column* vector.

        Arguments
        - mat: the matrix whose transpose to multiply the vector with

        Returns
        - this
        """
        ...


    def mulGeneric(self, mat: "Matrix4dc", dest: "Vector4d") -> "Vector4d":
        ...


    def mulAffineTranspose(self, mat: "Matrix4dc", dest: "Vector4d") -> "Vector4d":
        ...


    def mulGenericTranspose(self, mat: "Matrix4dc", dest: "Vector4d") -> "Vector4d":
        ...


    def mul(self, mat: "Matrix4x3dc") -> "Vector4d":
        """
        Multiply the given matrix mat with this vector.
        
        Note that this method performs the operation `M * this`, where `M` is the provided matrix
        and thus interprets `this` as a *column* vector.

        Arguments
        - mat: the matrix to multiply the vector with

        Returns
        - this
        """
        ...


    def mul(self, mat: "Matrix4x3dc", dest: "Vector4d") -> "Vector4d":
        ...


    def mulGeneric(self, mat: "Matrix4x3dc", dest: "Vector4d") -> "Vector4d":
        ...


    def mulTranslation(self, mat: "Matrix4x3dc", dest: "Vector4d") -> "Vector4d":
        ...


    def mul(self, mat: "Matrix4x3fc") -> "Vector4d":
        """
        Multiply the given matrix mat with this vector.
        
        Note that this method performs the operation `M * this`, where `M` is the provided matrix
        and thus interprets `this` as a *column* vector.

        Arguments
        - mat: the matrix to multiply the vector with

        Returns
        - this
        """
        ...


    def mul(self, mat: "Matrix4x3fc", dest: "Vector4d") -> "Vector4d":
        ...


    def mulGeneric(self, mat: "Matrix4x3fc", dest: "Vector4d") -> "Vector4d":
        ...


    def mulTranslation(self, mat: "Matrix4x3fc", dest: "Vector4d") -> "Vector4d":
        ...


    def mul(self, mat: "Matrix4fc") -> "Vector4d":
        """
        Multiply the given matrix mat with this vector.
        
        Note that this method performs the operation `M * this`, where `M` is the provided matrix
        and thus interprets `this` as a *column* vector.

        Arguments
        - mat: the matrix to multiply `this` by

        Returns
        - this
        """
        ...


    def mul(self, mat: "Matrix4fc", dest: "Vector4d") -> "Vector4d":
        ...


    def mulAffine(self, mat: "Matrix4fc") -> "Vector4d":
        """
        Multiply the given affine matrix `mat` with this vector.
        
        This method only works if the given matrix _only_ represents an affine transformation.
        
        Note that this method performs the operation `M * this`, where `M` is the provided matrix
        and thus interprets `this` as a *column* vector.

        Arguments
        - mat: the affine matrix to multiply the vector with

        Returns
        - this
        """
        ...


    def mulAffine(self, mat: "Matrix4fc", dest: "Vector4d") -> "Vector4d":
        ...


    def mulGeneric(self, mat: "Matrix4fc") -> "Vector4d":
        """
        Multiply the given matrix `mat` with this vector.
        
        This method does not make any assumptions or optimizations about the properties of the specified matrix.
        
        Note that this method performs the operation `M * this`, where `M` is the provided matrix
        and thus interprets `this` as a *column* vector.

        Arguments
        - mat: the matrix whose transpose to multiply the vector with

        Returns
        - this
        """
        ...


    def mulGeneric(self, mat: "Matrix4fc", dest: "Vector4d") -> "Vector4d":
        ...


    def mulProjectGeneric(self, mat: "Matrix4dc") -> "Vector4d":
        """
        Multiply the given matrix `mat` with this vector, perform perspective division.
        
        This method does not make any assumptions or optimizations about the properties of the specified matrix.
        
        Note that this method performs the operation `M * this`, where `M` is the provided matrix
        and thus interprets `this` as a *column* vector.

        Arguments
        - mat: the matrix to multiply this vector by

        Returns
        - this
        """
        ...


    def mulProjectGeneric(self, mat: "Matrix4dc", dest: "Vector4d") -> "Vector4d":
        ...


    def mulProjectTranslation(self, mat: "Matrix4dc") -> "Vector4d":
        """
        Multiply the given matrix `mat`, which is assumed to only contain translation,
        with this vector, perform perspective division.
        
        This method does not make any assumptions or optimizations about the properties of the specified matrix.
        
        Note that this method performs the operation `M * this`, where `M` is the provided matrix
        and thus interprets `this` as a *column* vector.

        Arguments
        - mat: the matrix to multiply this vector by

        Returns
        - this
        """
        ...


    def mulProjectTranslation(self, mat: "Matrix4dc", dest: "Vector4d") -> "Vector4d":
        ...


    def mulProjectTranslation(self, mat: "Matrix4dc", dest: "Vector3d") -> "Vector3d":
        ...


    def mulProjectAffine(self, mat: "Matrix4dc") -> "Vector4d":
        """
        Multiply the given affine matrix `mat`, with this vector, perform perspective division.
        
        This method only works if the given matrix _only_ represents an affine transformation.
        
        Note that this method performs the operation `M * this`, where `M` is the provided matrix
        and thus interprets `this` as a *column* vector.

        Arguments
        - mat: the matrix to multiply this vector by

        Returns
        - this
        """
        ...


    def mulProjectAffine(self, mat: "Matrix4dc", dest: "Vector4d") -> "Vector4d":
        ...


    def mulProjectAffine(self, mat: "Matrix4dc", dest: "Vector3d") -> "Vector3d":
        ...


    def mulProject(self, mat: "Matrix4dc") -> "Vector4d":
        """
        Multiply the given matrix `mat` with this vector and perform perspective division.
        
        Note that this method performs the operation `M * this`, where `M` is the provided matrix
        and thus interprets `this` as a *column* vector.

        Arguments
        - mat: the matrix to multiply this vector by

        Returns
        - this
        """
        ...


    def mulProject(self, mat: "Matrix4dc", dest: "Vector4d") -> "Vector4d":
        ...


    def mulProject(self, mat: "Matrix4dc", dest: "Vector3d") -> "Vector3d":
        ...


    def mulProjectGeneric(self, mat: "Matrix4dc", dest: "Vector3d") -> "Vector3d":
        ...


    def mul(self, scalar: float) -> "Vector4d":
        """
        Multiply this vector by the given scalar value.

        Arguments
        - scalar: the scalar to multiply by

        Returns
        - this
        """
        ...


    def mul(self, scalar: float, dest: "Vector4d") -> "Vector4d":
        ...


    def div(self, scalar: float) -> "Vector4d":
        """
        Divide this vector by the given scalar value.

        Arguments
        - scalar: the scalar to divide by

        Returns
        - this
        """
        ...


    def div(self, scalar: float, dest: "Vector4d") -> "Vector4d":
        ...


    def rotate(self, quat: "Quaterniondc") -> "Vector4d":
        """
        Transform this vector by the given quaternion `quat` and store the result in `this`.

        Arguments
        - quat: the quaternion to transform this vector

        Returns
        - this

        See
        - Quaterniond.transform(Vector4d)
        """
        ...


    def rotate(self, quat: "Quaterniondc", dest: "Vector4d") -> "Vector4d":
        ...


    def rotateAxis(self, angle: float, x: float, y: float, z: float) -> "Vector4d":
        """
        Rotate this vector the specified radians around the given rotation axis.
        
        This vector's `w` component is ignored.
        
        If the rotation axis is either `(1, 0, 0)`, `(0, 1, 0)` or `(0, 0, 1)`.
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


    def rotateAxis(self, angle: float, aX: float, aY: float, aZ: float, dest: "Vector4d") -> "Vector4d":
        ...


    def rotateX(self, angle: float) -> "Vector4d":
        """
        Rotate this vector the specified radians around the X axis.

        Arguments
        - angle: the angle in radians

        Returns
        - this
        """
        ...


    def rotateX(self, angle: float, dest: "Vector4d") -> "Vector4d":
        ...


    def rotateY(self, angle: float) -> "Vector4d":
        """
        Rotate this vector the specified radians around the Y axis.

        Arguments
        - angle: the angle in radians

        Returns
        - this
        """
        ...


    def rotateY(self, angle: float, dest: "Vector4d") -> "Vector4d":
        ...


    def rotateZ(self, angle: float) -> "Vector4d":
        """
        Rotate this vector the specified radians around the Z axis.

        Arguments
        - angle: the angle in radians

        Returns
        - this
        """
        ...


    def rotateZ(self, angle: float, dest: "Vector4d") -> "Vector4d":
        ...


    def lengthSquared(self) -> float:
        ...


    @staticmethod
    def lengthSquared(x: float, y: float, z: float, w: float) -> float:
        """
        Get the length squared of a 4-dimensional double-precision vector.

    Author(s)
        - F. Neurath

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
    def length(x: float, y: float, z: float, w: float) -> float:
        """
        Get the length of a 4-dimensional double-precision vector.

    Author(s)
        - F. Neurath

        Arguments
        - x: The vector's x component
        - y: The vector's y component
        - z: The vector's z component
        - w: The vector's w component

        Returns
        - the length of the given vector
        """
        ...


    def normalize(self) -> "Vector4d":
        """
        Normalizes this vector.

        Returns
        - this
        """
        ...


    def normalize(self, dest: "Vector4d") -> "Vector4d":
        ...


    def normalize(self, length: float) -> "Vector4d":
        """
        Scale this vector to have the given length.

        Arguments
        - length: the desired length

        Returns
        - this
        """
        ...


    def normalize(self, length: float, dest: "Vector4d") -> "Vector4d":
        ...


    def normalize3(self) -> "Vector4d":
        """
        Normalize this vector by computing only the norm of `(x, y, z)`.

        Returns
        - this
        """
        ...


    def normalize3(self, dest: "Vector4d") -> "Vector4d":
        ...


    def distance(self, v: "Vector4dc") -> float:
        ...


    def distance(self, x: float, y: float, z: float, w: float) -> float:
        ...


    def distanceSquared(self, v: "Vector4dc") -> float:
        ...


    def distanceSquared(self, x: float, y: float, z: float, w: float) -> float:
        ...


    @staticmethod
    def distance(x1: float, y1: float, z1: float, w1: float, x2: float, y2: float, z2: float, w2: float) -> float:
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
    def distanceSquared(x1: float, y1: float, z1: float, w1: float, x2: float, y2: float, z2: float, w2: float) -> float:
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


    def dot(self, v: "Vector4dc") -> float:
        ...


    def dot(self, x: float, y: float, z: float, w: float) -> float:
        ...


    def angleCos(self, v: "Vector4dc") -> float:
        ...


    def angle(self, v: "Vector4dc") -> float:
        ...


    def zero(self) -> "Vector4d":
        """
        Set all components to zero.

        Returns
        - this
        """
        ...


    def negate(self) -> "Vector4d":
        """
        Negate this vector.

        Returns
        - this
        """
        ...


    def negate(self, dest: "Vector4d") -> "Vector4d":
        ...


    def min(self, v: "Vector4dc") -> "Vector4d":
        """
        Set the components of this vector to be the component-wise minimum of this and the other vector.

        Arguments
        - v: the other vector

        Returns
        - this
        """
        ...


    def min(self, v: "Vector4dc", dest: "Vector4d") -> "Vector4d":
        ...


    def max(self, v: "Vector4dc") -> "Vector4d":
        """
        Set the components of this vector to be the component-wise maximum of this and the other vector.

        Arguments
        - v: the other vector

        Returns
        - this
        """
        ...


    def max(self, v: "Vector4dc", dest: "Vector4d") -> "Vector4d":
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


    def hashCode(self) -> int:
        ...


    def equals(self, obj: "Object") -> bool:
        ...


    def equals(self, v: "Vector4dc", delta: float) -> bool:
        ...


    def equals(self, x: float, y: float, z: float, w: float) -> bool:
        ...


    def smoothStep(self, v: "Vector4dc", t: float, dest: "Vector4d") -> "Vector4d":
        ...


    def hermite(self, t0: "Vector4dc", v1: "Vector4dc", t1: "Vector4dc", t: float, dest: "Vector4d") -> "Vector4d":
        ...


    def lerp(self, other: "Vector4dc", t: float) -> "Vector4d":
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


    def lerp(self, other: "Vector4dc", t: float, dest: "Vector4d") -> "Vector4d":
        ...


    def get(self, component: int) -> float:
        ...


    def get(self, mode: int, dest: "Vector4i") -> "Vector4i":
        ...


    def get(self, dest: "Vector4f") -> "Vector4f":
        ...


    def get(self, dest: "Vector4d") -> "Vector4d":
        ...


    def maxComponent(self) -> int:
        ...


    def minComponent(self) -> int:
        ...


    def floor(self) -> "Vector4d":
        """
        Set each component of this vector to the largest (closest to positive
        infinity) `double` value that is less than or equal to that
        component and is equal to a mathematical integer.

        Returns
        - this
        """
        ...


    def floor(self, dest: "Vector4d") -> "Vector4d":
        ...


    def ceil(self) -> "Vector4d":
        """
        Set each component of this vector to the smallest (closest to negative
        infinity) `double` value that is greater than or equal to that
        component and is equal to a mathematical integer.

        Returns
        - this
        """
        ...


    def ceil(self, dest: "Vector4d") -> "Vector4d":
        ...


    def round(self) -> "Vector4d":
        """
        Set each component of this vector to the closest double that is equal to
        a mathematical integer, with ties rounding to positive infinity.

        Returns
        - this
        """
        ...


    def round(self, dest: "Vector4d") -> "Vector4d":
        ...


    def isFinite(self) -> bool:
        ...


    def absolute(self) -> "Vector4d":
        """
        Compute the absolute of each of this vector's components.

        Returns
        - this
        """
        ...


    def absolute(self, dest: "Vector4d") -> "Vector4d":
        ...


    def clone(self) -> "Object":
        ...
