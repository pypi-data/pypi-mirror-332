"""
Python module generated from Java source file org.joml.Matrix4x3d

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
from org.intellij.lang.annotations import MagicConstant
from org.joml import *
from typing import Any, Callable, Iterable, Tuple


class Matrix4x3d(Externalizable, Cloneable, Matrix4x3dc):
    """
    Contains the definition of an affine 4x3 matrix (4 columns, 3 rows) of doubles, and associated functions to transform
    it. The matrix is column-major to match OpenGL's interpretation, and it looks like this:
    
         m00  m10  m20  m30
         m01  m11  m21  m31
         m02  m12  m22  m32

    Author(s)
    - Kai Burjack
    """

    def __init__(self):
        """
        Create a new Matrix4x3d and set it to .identity() identity.
        """
        ...


    def __init__(self, mat: "Matrix4x3dc"):
        """
        Create a new Matrix4x3d and make it a copy of the given matrix.

        Arguments
        - mat: the Matrix4x3dc to copy the values from
        """
        ...


    def __init__(self, mat: "Matrix4x3fc"):
        """
        Create a new Matrix4x3d and make it a copy of the given matrix.

        Arguments
        - mat: the Matrix4x3fc to copy the values from
        """
        ...


    def __init__(self, mat: "Matrix3dc"):
        """
        Create a new Matrix4x3d by setting its left 3x3 submatrix to the values of the given Matrix3dc
        and the rest to identity.

        Arguments
        - mat: the Matrix3dc
        """
        ...


    def __init__(self, mat: "Matrix3fc"):
        """
        Create a new Matrix4x3d by setting its left 3x3 submatrix to the values of the given Matrix3fc
        and the rest to identity.

        Arguments
        - mat: the Matrix3dc
        """
        ...


    def __init__(self, m00: float, m01: float, m02: float, m10: float, m11: float, m12: float, m20: float, m21: float, m22: float, m30: float, m31: float, m32: float):
        """
        Create a new 4x4 matrix using the supplied double values.

        Arguments
        - m00: the value of m00
        - m01: the value of m01
        - m02: the value of m02
        - m10: the value of m10
        - m11: the value of m11
        - m12: the value of m12
        - m20: the value of m20
        - m21: the value of m21
        - m22: the value of m22
        - m30: the value of m30
        - m31: the value of m31
        - m32: the value of m32
        """
        ...


    def __init__(self, buffer: "DoubleBuffer"):
        """
        Create a new Matrix4x3d by reading its 12 double components from the given DoubleBuffer
        at the buffer's current position.
        
        That DoubleBuffer is expected to hold the values in column-major order.
        
        The buffer's position will not be changed by this method.

        Arguments
        - buffer: the DoubleBuffer to read the matrix values from
        """
        ...


    def assume(self, properties: int) -> "Matrix4x3d":
        """
        Assume the given properties about this matrix.
        
        Use one or multiple of 0, Matrix4x3dc.PROPERTY_IDENTITY,
        Matrix4x3dc.PROPERTY_TRANSLATION, Matrix4x3dc.PROPERTY_ORTHONORMAL.

        Arguments
        - properties: bitset of the properties to assume about this matrix

        Returns
        - this
        """
        ...


    def determineProperties(self) -> "Matrix4x3d":
        """
        Compute and set the matrix properties returned by .properties() based
        on the current matrix element values.

        Returns
        - this
        """
        ...


    def properties(self) -> int:
        ...


    def m00(self) -> float:
        ...


    def m01(self) -> float:
        ...


    def m02(self) -> float:
        ...


    def m10(self) -> float:
        ...


    def m11(self) -> float:
        ...


    def m12(self) -> float:
        ...


    def m20(self) -> float:
        ...


    def m21(self) -> float:
        ...


    def m22(self) -> float:
        ...


    def m30(self) -> float:
        ...


    def m31(self) -> float:
        ...


    def m32(self) -> float:
        ...


    def m00(self, m00: float) -> "Matrix4x3d":
        """
        Set the value of the matrix element at column 0 and row 0.

        Arguments
        - m00: the new value

        Returns
        - this
        """
        ...


    def m01(self, m01: float) -> "Matrix4x3d":
        """
        Set the value of the matrix element at column 0 and row 1.

        Arguments
        - m01: the new value

        Returns
        - this
        """
        ...


    def m02(self, m02: float) -> "Matrix4x3d":
        """
        Set the value of the matrix element at column 0 and row 2.

        Arguments
        - m02: the new value

        Returns
        - this
        """
        ...


    def m10(self, m10: float) -> "Matrix4x3d":
        """
        Set the value of the matrix element at column 1 and row 0.

        Arguments
        - m10: the new value

        Returns
        - this
        """
        ...


    def m11(self, m11: float) -> "Matrix4x3d":
        """
        Set the value of the matrix element at column 1 and row 1.

        Arguments
        - m11: the new value

        Returns
        - this
        """
        ...


    def m12(self, m12: float) -> "Matrix4x3d":
        """
        Set the value of the matrix element at column 1 and row 2.

        Arguments
        - m12: the new value

        Returns
        - this
        """
        ...


    def m20(self, m20: float) -> "Matrix4x3d":
        """
        Set the value of the matrix element at column 2 and row 0.

        Arguments
        - m20: the new value

        Returns
        - this
        """
        ...


    def m21(self, m21: float) -> "Matrix4x3d":
        """
        Set the value of the matrix element at column 2 and row 1.

        Arguments
        - m21: the new value

        Returns
        - this
        """
        ...


    def m22(self, m22: float) -> "Matrix4x3d":
        """
        Set the value of the matrix element at column 2 and row 2.

        Arguments
        - m22: the new value

        Returns
        - this
        """
        ...


    def m30(self, m30: float) -> "Matrix4x3d":
        """
        Set the value of the matrix element at column 3 and row 0.

        Arguments
        - m30: the new value

        Returns
        - this
        """
        ...


    def m31(self, m31: float) -> "Matrix4x3d":
        """
        Set the value of the matrix element at column 3 and row 1.

        Arguments
        - m31: the new value

        Returns
        - this
        """
        ...


    def m32(self, m32: float) -> "Matrix4x3d":
        """
        Set the value of the matrix element at column 3 and row 2.

        Arguments
        - m32: the new value

        Returns
        - this
        """
        ...


    def identity(self) -> "Matrix4x3d":
        """
        Reset this matrix to the identity.
        
        Please note that if a call to .identity() is immediately followed by a call to:
        .translate(double, double, double) translate, 
        .rotate(double, double, double, double) rotate,
        .scale(double, double, double) scale,
        .ortho(double, double, double, double, double, double) ortho,
        .ortho2D(double, double, double, double) ortho2D,
        .lookAt(double, double, double, double, double, double, double, double, double) lookAt,
        .lookAlong(double, double, double, double, double, double) lookAlong,
        or any of their overloads, then the call to .identity() can be omitted and the subsequent call replaced with:
        .translation(double, double, double) translation,
        .rotation(double, double, double, double) rotation,
        .scaling(double, double, double) scaling,
        .setOrtho(double, double, double, double, double, double) setOrtho,
        .setOrtho2D(double, double, double, double) setOrtho2D,
        .setLookAt(double, double, double, double, double, double, double, double, double) setLookAt,
        .setLookAlong(double, double, double, double, double, double) setLookAlong,
        or any of their overloads.

        Returns
        - this
        """
        ...


    def set(self, m: "Matrix4x3dc") -> "Matrix4x3d":
        """
        Store the values of the given matrix `m` into `this` matrix.

        Arguments
        - m: the matrix to copy the values from

        Returns
        - this
        """
        ...


    def set(self, m: "Matrix4x3fc") -> "Matrix4x3d":
        """
        Store the values of the given matrix `m` into `this` matrix.

        Arguments
        - m: the matrix to copy the values from

        Returns
        - this
        """
        ...


    def set(self, m: "Matrix4dc") -> "Matrix4x3d":
        """
        Store the values of the upper 4x3 submatrix of `m` into `this` matrix.

        Arguments
        - m: the matrix to copy the values from

        Returns
        - this

        See
        - Matrix4dc.get4x3(Matrix4x3d)
        """
        ...


    def get(self, dest: "Matrix4d") -> "Matrix4d":
        ...


    def set(self, mat: "Matrix3dc") -> "Matrix4x3d":
        """
        Set the left 3x3 submatrix of this Matrix4x3d to the given Matrix3dc 
        and the rest to identity.

        Arguments
        - mat: the Matrix3dc

        Returns
        - this

        See
        - .Matrix4x3d(Matrix3dc)
        """
        ...


    def set(self, mat: "Matrix3fc") -> "Matrix4x3d":
        """
        Set the left 3x3 submatrix of this Matrix4x3d to the given Matrix3fc 
        and the rest to identity.

        Arguments
        - mat: the Matrix3fc

        Returns
        - this

        See
        - .Matrix4x3d(Matrix3fc)
        """
        ...


    def set(self, col0: "Vector3dc", col1: "Vector3dc", col2: "Vector3dc", col3: "Vector3dc") -> "Matrix4x3d":
        """
        Set the four columns of this matrix to the supplied vectors, respectively.

        Arguments
        - col0: the first column
        - col1: the second column
        - col2: the third column
        - col3: the fourth column

        Returns
        - this
        """
        ...


    def set3x3(self, mat: "Matrix4x3dc") -> "Matrix4x3d":
        """
        Set the left 3x3 submatrix of this Matrix4x3d to that of the given Matrix4x3dc 
        and don't change the other elements.

        Arguments
        - mat: the Matrix4x3dc

        Returns
        - this
        """
        ...


    def set(self, axisAngle: "AxisAngle4f") -> "Matrix4x3d":
        """
        Set this matrix to be equivalent to the rotation specified by the given AxisAngle4f.

        Arguments
        - axisAngle: the AxisAngle4f

        Returns
        - this
        """
        ...


    def set(self, axisAngle: "AxisAngle4d") -> "Matrix4x3d":
        """
        Set this matrix to be equivalent to the rotation specified by the given AxisAngle4d.

        Arguments
        - axisAngle: the AxisAngle4d

        Returns
        - this
        """
        ...


    def set(self, q: "Quaternionfc") -> "Matrix4x3d":
        """
        Set this matrix to be equivalent to the rotation - and possibly scaling - specified by the given Quaternionfc.
        
        This method is equivalent to calling: `rotation(q)`

        Arguments
        - q: the Quaternionfc

        Returns
        - this

        See
        - .rotation(Quaternionfc)
        """
        ...


    def set(self, q: "Quaterniondc") -> "Matrix4x3d":
        """
        Set this matrix to be equivalent to the rotation - and possibly scaling - specified by the given Quaterniondc.
        
        This method is equivalent to calling: `rotation(q)`

        Arguments
        - q: the Quaterniondc

        Returns
        - this
        """
        ...


    def mul(self, right: "Matrix4x3dc") -> "Matrix4x3d":
        """
        Multiply this matrix by the supplied `right` matrix.
        
        If `M` is `this` matrix and `R` the `right` matrix,
        then the new matrix will be `M * R`. So when transforming a
        vector `v` with the new matrix by using `M * R * v`, the
        transformation of the right matrix will be applied first!

        Arguments
        - right: the right operand of the multiplication

        Returns
        - this
        """
        ...


    def mul(self, right: "Matrix4x3dc", dest: "Matrix4x3d") -> "Matrix4x3d":
        ...


    def mul(self, right: "Matrix4x3fc") -> "Matrix4x3d":
        """
        Multiply this matrix by the supplied `right` matrix.
        
        If `M` is `this` matrix and `R` the `right` matrix,
        then the new matrix will be `M * R`. So when transforming a
        vector `v` with the new matrix by using `M * R * v`, the
        transformation of the right matrix will be applied first!

        Arguments
        - right: the right operand of the multiplication

        Returns
        - this
        """
        ...


    def mul(self, right: "Matrix4x3fc", dest: "Matrix4x3d") -> "Matrix4x3d":
        ...


    def mulTranslation(self, right: "Matrix4x3dc", dest: "Matrix4x3d") -> "Matrix4x3d":
        ...


    def mulTranslation(self, right: "Matrix4x3fc", dest: "Matrix4x3d") -> "Matrix4x3d":
        ...


    def mulOrtho(self, view: "Matrix4x3dc") -> "Matrix4x3d":
        """
        Multiply `this` orthographic projection matrix by the supplied `view` matrix.
        
        If `M` is `this` matrix and `V` the `view` matrix,
        then the new matrix will be `M * V`. So when transforming a
        vector `v` with the new matrix by using `M * V * v`, the
        transformation of the `view` matrix will be applied first!

        Arguments
        - view: the matrix which to multiply `this` with

        Returns
        - this
        """
        ...


    def mulOrtho(self, view: "Matrix4x3dc", dest: "Matrix4x3d") -> "Matrix4x3d":
        ...


    def mul3x3(self, rm00: float, rm01: float, rm02: float, rm10: float, rm11: float, rm12: float, rm20: float, rm21: float, rm22: float) -> "Matrix4x3d":
        """
        Multiply `this` by the 4x3 matrix with the column vectors `(rm00, rm01, rm02)`,
        `(rm10, rm11, rm12)`, `(rm20, rm21, rm22)` and `(0, 0, 0)`.
        
        If `M` is `this` matrix and `R` the specified matrix,
        then the new matrix will be `M * R`. So when transforming a
        vector `v` with the new matrix by using `M * R * v`, the
        transformation of the `R` matrix will be applied first!

        Arguments
        - rm00: the value of the m00 element
        - rm01: the value of the m01 element
        - rm02: the value of the m02 element
        - rm10: the value of the m10 element
        - rm11: the value of the m11 element
        - rm12: the value of the m12 element
        - rm20: the value of the m20 element
        - rm21: the value of the m21 element
        - rm22: the value of the m22 element

        Returns
        - this
        """
        ...


    def mul3x3(self, rm00: float, rm01: float, rm02: float, rm10: float, rm11: float, rm12: float, rm20: float, rm21: float, rm22: float, dest: "Matrix4x3d") -> "Matrix4x3d":
        ...


    def fma(self, other: "Matrix4x3dc", otherFactor: float) -> "Matrix4x3d":
        """
        Component-wise add `this` and `other`
        by first multiplying each component of `other` by `otherFactor` and
        adding that result to `this`.
        
        The matrix `other` will not be changed.

        Arguments
        - other: the other matrix
        - otherFactor: the factor to multiply each of the other matrix's components

        Returns
        - this
        """
        ...


    def fma(self, other: "Matrix4x3dc", otherFactor: float, dest: "Matrix4x3d") -> "Matrix4x3d":
        ...


    def fma(self, other: "Matrix4x3fc", otherFactor: float) -> "Matrix4x3d":
        """
        Component-wise add `this` and `other`
        by first multiplying each component of `other` by `otherFactor` and
        adding that result to `this`.
        
        The matrix `other` will not be changed.

        Arguments
        - other: the other matrix
        - otherFactor: the factor to multiply each of the other matrix's components

        Returns
        - this
        """
        ...


    def fma(self, other: "Matrix4x3fc", otherFactor: float, dest: "Matrix4x3d") -> "Matrix4x3d":
        ...


    def add(self, other: "Matrix4x3dc") -> "Matrix4x3d":
        """
        Component-wise add `this` and `other`.

        Arguments
        - other: the other addend

        Returns
        - this
        """
        ...


    def add(self, other: "Matrix4x3dc", dest: "Matrix4x3d") -> "Matrix4x3d":
        ...


    def add(self, other: "Matrix4x3fc") -> "Matrix4x3d":
        """
        Component-wise add `this` and `other`.

        Arguments
        - other: the other addend

        Returns
        - this
        """
        ...


    def add(self, other: "Matrix4x3fc", dest: "Matrix4x3d") -> "Matrix4x3d":
        ...


    def sub(self, subtrahend: "Matrix4x3dc") -> "Matrix4x3d":
        """
        Component-wise subtract `subtrahend` from `this`.

        Arguments
        - subtrahend: the subtrahend

        Returns
        - this
        """
        ...


    def sub(self, subtrahend: "Matrix4x3dc", dest: "Matrix4x3d") -> "Matrix4x3d":
        ...


    def sub(self, subtrahend: "Matrix4x3fc") -> "Matrix4x3d":
        """
        Component-wise subtract `subtrahend` from `this`.

        Arguments
        - subtrahend: the subtrahend

        Returns
        - this
        """
        ...


    def sub(self, subtrahend: "Matrix4x3fc", dest: "Matrix4x3d") -> "Matrix4x3d":
        ...


    def mulComponentWise(self, other: "Matrix4x3dc") -> "Matrix4x3d":
        """
        Component-wise multiply `this` by `other`.

        Arguments
        - other: the other matrix

        Returns
        - this
        """
        ...


    def mulComponentWise(self, other: "Matrix4x3dc", dest: "Matrix4x3d") -> "Matrix4x3d":
        ...


    def set(self, m00: float, m01: float, m02: float, m10: float, m11: float, m12: float, m20: float, m21: float, m22: float, m30: float, m31: float, m32: float) -> "Matrix4x3d":
        """
        Set the values within this matrix to the supplied double values. The matrix will look like this:
        
        m00, m10, m20, m30
        m01, m11, m21, m31
        m02, m12, m22, m32

        Arguments
        - m00: the new value of m00
        - m01: the new value of m01
        - m02: the new value of m02
        - m10: the new value of m10
        - m11: the new value of m11
        - m12: the new value of m12
        - m20: the new value of m20
        - m21: the new value of m21
        - m22: the new value of m22
        - m30: the new value of m30
        - m31: the new value of m31
        - m32: the new value of m32

        Returns
        - this
        """
        ...


    def set(self, m: list[float], off: int) -> "Matrix4x3d":
        """
        Set the values in the matrix using a double array that contains the matrix elements in column-major order.
        
        The results will look like this:
        
        0, 3, 6, 9
        1, 4, 7, 10
        2, 5, 8, 11

        Arguments
        - m: the array to read the matrix values from
        - off: the offset into the array

        Returns
        - this

        See
        - .set(double[])
        """
        ...


    def set(self, m: list[float]) -> "Matrix4x3d":
        """
        Set the values in the matrix using a double array that contains the matrix elements in column-major order.
        
        The results will look like this:
        
        0, 3, 6, 9
        1, 4, 7, 10
        2, 5, 8, 11

        Arguments
        - m: the array to read the matrix values from

        Returns
        - this

        See
        - .set(double[], int)
        """
        ...


    def set(self, m: list[float], off: int) -> "Matrix4x3d":
        """
        Set the values in the matrix using a float array that contains the matrix elements in column-major order.
        
        The results will look like this:
        
        0, 3, 6, 9
        1, 4, 7, 10
        2, 5, 8, 11

        Arguments
        - m: the array to read the matrix values from
        - off: the offset into the array

        Returns
        - this

        See
        - .set(float[])
        """
        ...


    def set(self, m: list[float]) -> "Matrix4x3d":
        """
        Set the values in the matrix using a float array that contains the matrix elements in column-major order.
        
        The results will look like this:
        
        0, 3, 6, 9
        1, 4, 7, 10
        2, 5, 8, 11

        Arguments
        - m: the array to read the matrix values from

        Returns
        - this

        See
        - .set(float[], int)
        """
        ...


    def set(self, buffer: "DoubleBuffer") -> "Matrix4x3d":
        """
        Set the values of this matrix by reading 12 double values from the given DoubleBuffer in column-major order,
        starting at its current position.
        
        The DoubleBuffer is expected to contain the values in column-major order.
        
        The position of the DoubleBuffer will not be changed by this method.

        Arguments
        - buffer: the DoubleBuffer to read the matrix values from in column-major order

        Returns
        - this
        """
        ...


    def set(self, buffer: "FloatBuffer") -> "Matrix4x3d":
        """
        Set the values of this matrix by reading 12 float values from the given FloatBuffer in column-major order,
        starting at its current position.
        
        The FloatBuffer is expected to contain the values in column-major order.
        
        The position of the FloatBuffer will not be changed by this method.

        Arguments
        - buffer: the FloatBuffer to read the matrix values from in column-major order

        Returns
        - this
        """
        ...


    def set(self, buffer: "ByteBuffer") -> "Matrix4x3d":
        """
        Set the values of this matrix by reading 12 double values from the given ByteBuffer in column-major order,
        starting at its current position.
        
        The ByteBuffer is expected to contain the values in column-major order.
        
        The position of the ByteBuffer will not be changed by this method.

        Arguments
        - buffer: the ByteBuffer to read the matrix values from in column-major order

        Returns
        - this
        """
        ...


    def set(self, index: int, buffer: "DoubleBuffer") -> "Matrix4x3d":
        """
        Set the values of this matrix by reading 12 double values from the given DoubleBuffer in column-major order,
        starting at the specified absolute buffer position/index.
        
        The DoubleBuffer is expected to contain the values in column-major order.
        
        The position of the DoubleBuffer will not be changed by this method.

        Arguments
        - index: the absolute position into the DoubleBuffer
        - buffer: the DoubleBuffer to read the matrix values from in column-major order

        Returns
        - this
        """
        ...


    def set(self, index: int, buffer: "FloatBuffer") -> "Matrix4x3d":
        """
        Set the values of this matrix by reading 12 float values from the given FloatBuffer in column-major order,
        starting at the specified absolute buffer position/index.
        
        The FloatBuffer is expected to contain the values in column-major order.
        
        The position of the FloatBuffer will not be changed by this method.

        Arguments
        - index: the absolute position into the FloatBuffer
        - buffer: the FloatBuffer to read the matrix values from in column-major order

        Returns
        - this
        """
        ...


    def set(self, index: int, buffer: "ByteBuffer") -> "Matrix4x3d":
        """
        Set the values of this matrix by reading 12 double values from the given ByteBuffer in column-major order,
        starting at the specified absolute buffer position/index.
        
        The ByteBuffer is expected to contain the values in column-major order.
        
        The position of the ByteBuffer will not be changed by this method.

        Arguments
        - index: the absolute position into the ByteBuffer
        - buffer: the ByteBuffer to read the matrix values from in column-major order

        Returns
        - this
        """
        ...


    def setFloats(self, buffer: "ByteBuffer") -> "Matrix4x3d":
        """
        Set the values of this matrix by reading 12 float values from the given ByteBuffer in column-major order,
        starting at its current position.
        
        The ByteBuffer is expected to contain the values in column-major order.
        
        The position of the ByteBuffer will not be changed by this method.

        Arguments
        - buffer: the ByteBuffer to read the matrix values from in column-major order

        Returns
        - this
        """
        ...


    def setFloats(self, index: int, buffer: "ByteBuffer") -> "Matrix4x3d":
        """
        Set the values of this matrix by reading 12 float values from the given ByteBuffer in column-major order,
        starting at the specified absolute buffer position/index.
        
        The ByteBuffer is expected to contain the values in column-major order.
        
        The position of the ByteBuffer will not be changed by this method.

        Arguments
        - index: the absolute position into the ByteBuffer
        - buffer: the ByteBuffer to read the matrix values from in column-major order

        Returns
        - this
        """
        ...


    def setFromAddress(self, address: int) -> "Matrix4x3d":
        """
        Set the values of this matrix by reading 12 double values from off-heap memory in column-major order,
        starting at the given address.
        
        This method will throw an UnsupportedOperationException when JOML is used with `-Djoml.nounsafe`.
        
        *This method is unsafe as it can result in a crash of the JVM process when the specified address range does not belong to this process.*

        Arguments
        - address: the off-heap memory address to read the matrix values from in column-major order

        Returns
        - this
        """
        ...


    def setTransposedFromAddress(self, address: int) -> "Matrix4x3d":
        """
        Set the values of this matrix by reading 12 double values from off-heap memory in row-major order,
        starting at the given address.
        
        This method will throw an UnsupportedOperationException when JOML is used with `-Djoml.nounsafe`.
        
        *This method is unsafe as it can result in a crash of the JVM process when the specified address range does not belong to this process.*

        Arguments
        - address: the off-heap memory address to read the matrix values from in row-major order

        Returns
        - this
        """
        ...


    def determinant(self) -> float:
        ...


    def invert(self) -> "Matrix4x3d":
        """
        Invert this matrix.

        Returns
        - this
        """
        ...


    def invert(self, dest: "Matrix4x3d") -> "Matrix4x3d":
        ...


    def invertOrtho(self, dest: "Matrix4x3d") -> "Matrix4x3d":
        ...


    def invertOrtho(self) -> "Matrix4x3d":
        """
        Invert `this` orthographic projection matrix.
        
        This method can be used to quickly obtain the inverse of an orthographic projection matrix.

        Returns
        - this
        """
        ...


    def transpose3x3(self) -> "Matrix4x3d":
        """
        Transpose only the left 3x3 submatrix of this matrix and set the rest of the matrix elements to identity.

        Returns
        - this
        """
        ...


    def transpose3x3(self, dest: "Matrix4x3d") -> "Matrix4x3d":
        ...


    def transpose3x3(self, dest: "Matrix3d") -> "Matrix3d":
        ...


    def translation(self, x: float, y: float, z: float) -> "Matrix4x3d":
        """
        Set this matrix to be a simple translation matrix.
        
        The resulting matrix can be multiplied against another transformation
        matrix to obtain an additional translation.

        Arguments
        - x: the offset to translate in x
        - y: the offset to translate in y
        - z: the offset to translate in z

        Returns
        - this
        """
        ...


    def translation(self, offset: "Vector3fc") -> "Matrix4x3d":
        """
        Set this matrix to be a simple translation matrix.
        
        The resulting matrix can be multiplied against another transformation
        matrix to obtain an additional translation.

        Arguments
        - offset: the offsets in x, y and z to translate

        Returns
        - this
        """
        ...


    def translation(self, offset: "Vector3dc") -> "Matrix4x3d":
        """
        Set this matrix to be a simple translation matrix.
        
        The resulting matrix can be multiplied against another transformation
        matrix to obtain an additional translation.

        Arguments
        - offset: the offsets in x, y and z to translate

        Returns
        - this
        """
        ...


    def setTranslation(self, x: float, y: float, z: float) -> "Matrix4x3d":
        """
        Set only the translation components `(m30, m31, m32)` of this matrix to the given values `(x, y, z)`.
        
        To build a translation matrix instead, use .translation(double, double, double).
        To apply a translation, use .translate(double, double, double).

        Arguments
        - x: the units to translate in x
        - y: the units to translate in y
        - z: the units to translate in z

        Returns
        - this

        See
        - .translate(double, double, double)
        """
        ...


    def setTranslation(self, xyz: "Vector3dc") -> "Matrix4x3d":
        """
        Set only the translation components `(m30, m31, m32)` of this matrix to the given values `(xyz.x, xyz.y, xyz.z)`.
        
        To build a translation matrix instead, use .translation(Vector3dc).
        To apply a translation, use .translate(Vector3dc).

        Arguments
        - xyz: the units to translate in `(x, y, z)`

        Returns
        - this

        See
        - .translate(Vector3dc)
        """
        ...


    def getTranslation(self, dest: "Vector3d") -> "Vector3d":
        ...


    def getScale(self, dest: "Vector3d") -> "Vector3d":
        ...


    def toString(self) -> str:
        """
        Return a string representation of this matrix.
        
        This method creates a new DecimalFormat on every invocation with the format string "`0.000E0;-`".

        Returns
        - the string representation
        """
        ...


    def toString(self, formatter: "NumberFormat") -> str:
        """
        Return a string representation of this matrix by formatting the matrix elements with the given NumberFormat.

        Arguments
        - formatter: the NumberFormat used to format the matrix values with

        Returns
        - the string representation
        """
        ...


    def get(self, dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Get the current values of `this` matrix and store them into
        `dest`.
        
        This is the reverse method of .set(Matrix4x3dc) and allows to obtain
        intermediate calculation results when chaining multiple transformations.

        Arguments
        - dest: the destination matrix

        Returns
        - the passed in destination

        See
        - .set(Matrix4x3dc)
        """
        ...


    def getUnnormalizedRotation(self, dest: "Quaternionf") -> "Quaternionf":
        ...


    def getNormalizedRotation(self, dest: "Quaternionf") -> "Quaternionf":
        ...


    def getUnnormalizedRotation(self, dest: "Quaterniond") -> "Quaterniond":
        ...


    def getNormalizedRotation(self, dest: "Quaterniond") -> "Quaterniond":
        ...


    def get(self, buffer: "DoubleBuffer") -> "DoubleBuffer":
        ...


    def get(self, index: int, buffer: "DoubleBuffer") -> "DoubleBuffer":
        ...


    def get(self, buffer: "FloatBuffer") -> "FloatBuffer":
        ...


    def get(self, index: int, buffer: "FloatBuffer") -> "FloatBuffer":
        ...


    def get(self, buffer: "ByteBuffer") -> "ByteBuffer":
        ...


    def get(self, index: int, buffer: "ByteBuffer") -> "ByteBuffer":
        ...


    def getFloats(self, buffer: "ByteBuffer") -> "ByteBuffer":
        ...


    def getFloats(self, index: int, buffer: "ByteBuffer") -> "ByteBuffer":
        ...


    def getToAddress(self, address: int) -> "Matrix4x3dc":
        ...


    def getTransposedToAddress(self, address: int) -> "Matrix4x3dc":
        ...


    def get(self, arr: list[float], offset: int) -> list[float]:
        ...


    def get(self, arr: list[float]) -> list[float]:
        ...


    def get(self, arr: list[float], offset: int) -> list[float]:
        ...


    def get(self, arr: list[float]) -> list[float]:
        ...


    def get4x4(self, arr: list[float], offset: int) -> list[float]:
        ...


    def get4x4(self, arr: list[float]) -> list[float]:
        ...


    def get4x4(self, arr: list[float], offset: int) -> list[float]:
        ...


    def get4x4(self, arr: list[float]) -> list[float]:
        ...


    def get4x4(self, buffer: "DoubleBuffer") -> "DoubleBuffer":
        ...


    def get4x4(self, index: int, buffer: "DoubleBuffer") -> "DoubleBuffer":
        ...


    def get4x4(self, buffer: "ByteBuffer") -> "ByteBuffer":
        ...


    def get4x4(self, index: int, buffer: "ByteBuffer") -> "ByteBuffer":
        ...


    def getTransposed(self, buffer: "DoubleBuffer") -> "DoubleBuffer":
        ...


    def getTransposed(self, index: int, buffer: "DoubleBuffer") -> "DoubleBuffer":
        ...


    def getTransposed(self, buffer: "ByteBuffer") -> "ByteBuffer":
        ...


    def getTransposed(self, index: int, buffer: "ByteBuffer") -> "ByteBuffer":
        ...


    def getTransposed(self, buffer: "FloatBuffer") -> "FloatBuffer":
        ...


    def getTransposed(self, index: int, buffer: "FloatBuffer") -> "FloatBuffer":
        ...


    def getTransposedFloats(self, buffer: "ByteBuffer") -> "ByteBuffer":
        ...


    def getTransposedFloats(self, index: int, buffer: "ByteBuffer") -> "ByteBuffer":
        ...


    def getTransposed(self, arr: list[float], offset: int) -> list[float]:
        ...


    def getTransposed(self, arr: list[float]) -> list[float]:
        ...


    def zero(self) -> "Matrix4x3d":
        """
        Set all the values within this matrix to 0.

        Returns
        - this
        """
        ...


    def scaling(self, factor: float) -> "Matrix4x3d":
        """
        Set this matrix to be a simple scale matrix, which scales all axes uniformly by the given factor.
        
        The resulting matrix can be multiplied against another transformation
        matrix to obtain an additional scaling.
        
        In order to post-multiply a scaling transformation directly to a
        matrix, use .scale(double) scale() instead.

        Arguments
        - factor: the scale factor in x, y and z

        Returns
        - this

        See
        - .scale(double)
        """
        ...


    def scaling(self, x: float, y: float, z: float) -> "Matrix4x3d":
        """
        Set this matrix to be a simple scale matrix.

        Arguments
        - x: the scale in x
        - y: the scale in y
        - z: the scale in z

        Returns
        - this
        """
        ...


    def scaling(self, xyz: "Vector3dc") -> "Matrix4x3d":
        """
        Set this matrix to be a simple scale matrix which scales the base axes by
        `xyz.x`, `xyz.y` and `xyz.z`, respectively.
        
        The resulting matrix can be multiplied against another transformation
        matrix to obtain an additional scaling.
        
        In order to post-multiply a scaling transformation directly to a
        matrix use .scale(Vector3dc) scale() instead.

        Arguments
        - xyz: the scale in x, y and z, respectively

        Returns
        - this

        See
        - .scale(Vector3dc)
        """
        ...


    def rotation(self, angle: float, x: float, y: float, z: float) -> "Matrix4x3d":
        """
        Set this matrix to a rotation matrix which rotates the given radians about a given axis.
        
        When used with a right-handed coordinate system, the produced rotation will rotate a vector 
        counter-clockwise around the rotation axis, when viewing along the negative axis direction towards the origin.
        When used with a left-handed coordinate system, the rotation is clockwise.
        
        From <a href="http://en.wikipedia.org/wiki/Rotation_matrix#Rotation_matrix_from_axis_and_angle">Wikipedia</a>

        Arguments
        - angle: the angle in radians
        - x: the x-coordinate of the axis to rotate about
        - y: the y-coordinate of the axis to rotate about
        - z: the z-coordinate of the axis to rotate about

        Returns
        - this
        """
        ...


    def rotationX(self, ang: float) -> "Matrix4x3d":
        """
        Set this matrix to a rotation transformation about the X axis.
        
        When used with a right-handed coordinate system, the produced rotation will rotate a vector 
        counter-clockwise around the rotation axis, when viewing along the negative axis direction towards the origin.
        When used with a left-handed coordinate system, the rotation is clockwise.
        
        Reference: <a href="http://en.wikipedia.org/wiki/Rotation_matrix#Basic_rotations">http://en.wikipedia.org</a>

        Arguments
        - ang: the angle in radians

        Returns
        - this
        """
        ...


    def rotationY(self, ang: float) -> "Matrix4x3d":
        """
        Set this matrix to a rotation transformation about the Y axis.
        
        When used with a right-handed coordinate system, the produced rotation will rotate a vector 
        counter-clockwise around the rotation axis, when viewing along the negative axis direction towards the origin.
        When used with a left-handed coordinate system, the rotation is clockwise.
        
        Reference: <a href="http://en.wikipedia.org/wiki/Rotation_matrix#Basic_rotations">http://en.wikipedia.org</a>

        Arguments
        - ang: the angle in radians

        Returns
        - this
        """
        ...


    def rotationZ(self, ang: float) -> "Matrix4x3d":
        """
        Set this matrix to a rotation transformation about the Z axis.
        
        When used with a right-handed coordinate system, the produced rotation will rotate a vector 
        counter-clockwise around the rotation axis, when viewing along the negative axis direction towards the origin.
        When used with a left-handed coordinate system, the rotation is clockwise.
        
        Reference: <a href="http://en.wikipedia.org/wiki/Rotation_matrix#Basic_rotations">http://en.wikipedia.org</a>

        Arguments
        - ang: the angle in radians

        Returns
        - this
        """
        ...


    def rotationXYZ(self, angleX: float, angleY: float, angleZ: float) -> "Matrix4x3d":
        """
        Set this matrix to a rotation of `angleX` radians about the X axis, followed by a rotation
        of `angleY` radians about the Y axis and followed by a rotation of `angleZ` radians about the Z axis.
        
        When used with a right-handed coordinate system, the produced rotation will rotate a vector 
        counter-clockwise around the rotation axis, when viewing along the negative axis direction towards the origin.
        When used with a left-handed coordinate system, the rotation is clockwise.
        
        This method is equivalent to calling: `rotationX(angleX).rotateY(angleY).rotateZ(angleZ)`

        Arguments
        - angleX: the angle to rotate about X
        - angleY: the angle to rotate about Y
        - angleZ: the angle to rotate about Z

        Returns
        - this
        """
        ...


    def rotationZYX(self, angleZ: float, angleY: float, angleX: float) -> "Matrix4x3d":
        """
        Set this matrix to a rotation of `angleZ` radians about the Z axis, followed by a rotation
        of `angleY` radians about the Y axis and followed by a rotation of `angleX` radians about the X axis.
        
        When used with a right-handed coordinate system, the produced rotation will rotate a vector 
        counter-clockwise around the rotation axis, when viewing along the negative axis direction towards the origin.
        When used with a left-handed coordinate system, the rotation is clockwise.
        
        This method is equivalent to calling: `rotationZ(angleZ).rotateY(angleY).rotateX(angleX)`

        Arguments
        - angleZ: the angle to rotate about Z
        - angleY: the angle to rotate about Y
        - angleX: the angle to rotate about X

        Returns
        - this
        """
        ...


    def rotationYXZ(self, angleY: float, angleX: float, angleZ: float) -> "Matrix4x3d":
        """
        Set this matrix to a rotation of `angleY` radians about the Y axis, followed by a rotation
        of `angleX` radians about the X axis and followed by a rotation of `angleZ` radians about the Z axis.
        
        When used with a right-handed coordinate system, the produced rotation will rotate a vector 
        counter-clockwise around the rotation axis, when viewing along the negative axis direction towards the origin.
        When used with a left-handed coordinate system, the rotation is clockwise.
        
        This method is equivalent to calling: `rotationY(angleY).rotateX(angleX).rotateZ(angleZ)`

        Arguments
        - angleY: the angle to rotate about Y
        - angleX: the angle to rotate about X
        - angleZ: the angle to rotate about Z

        Returns
        - this
        """
        ...


    def setRotationXYZ(self, angleX: float, angleY: float, angleZ: float) -> "Matrix4x3d":
        """
        Set only the left 3x3 submatrix of this matrix to a rotation of `angleX` radians about the X axis, followed by a rotation
        of `angleY` radians about the Y axis and followed by a rotation of `angleZ` radians about the Z axis.
        
        When used with a right-handed coordinate system, the produced rotation will rotate a vector 
        counter-clockwise around the rotation axis, when viewing along the negative axis direction towards the origin.
        When used with a left-handed coordinate system, the rotation is clockwise.

        Arguments
        - angleX: the angle to rotate about X
        - angleY: the angle to rotate about Y
        - angleZ: the angle to rotate about Z

        Returns
        - this
        """
        ...


    def setRotationZYX(self, angleZ: float, angleY: float, angleX: float) -> "Matrix4x3d":
        """
        Set only the left 3x3 submatrix of this matrix to a rotation of `angleZ` radians about the Z axis, followed by a rotation
        of `angleY` radians about the Y axis and followed by a rotation of `angleX` radians about the X axis.
        
        When used with a right-handed coordinate system, the produced rotation will rotate a vector 
        counter-clockwise around the rotation axis, when viewing along the negative axis direction towards the origin.
        When used with a left-handed coordinate system, the rotation is clockwise.

        Arguments
        - angleZ: the angle to rotate about Z
        - angleY: the angle to rotate about Y
        - angleX: the angle to rotate about X

        Returns
        - this
        """
        ...


    def setRotationYXZ(self, angleY: float, angleX: float, angleZ: float) -> "Matrix4x3d":
        """
        Set only the left 3x3 submatrix of this matrix to a rotation of `angleY` radians about the Y axis, followed by a rotation
        of `angleX` radians about the X axis and followed by a rotation of `angleZ` radians about the Z axis.
        
        When used with a right-handed coordinate system, the produced rotation will rotate a vector 
        counter-clockwise around the rotation axis, when viewing along the negative axis direction towards the origin.
        When used with a left-handed coordinate system, the rotation is clockwise.

        Arguments
        - angleY: the angle to rotate about Y
        - angleX: the angle to rotate about X
        - angleZ: the angle to rotate about Z

        Returns
        - this
        """
        ...


    def rotation(self, angle: float, axis: "Vector3dc") -> "Matrix4x3d":
        """
        Set this matrix to a rotation matrix which rotates the given radians about a given axis.
        
        The axis described by the `axis` vector needs to be a unit vector.
        
        When used with a right-handed coordinate system, the produced rotation will rotate a vector 
        counter-clockwise around the rotation axis, when viewing along the negative axis direction towards the origin.
        When used with a left-handed coordinate system, the rotation is clockwise.

        Arguments
        - angle: the angle in radians
        - axis: the axis to rotate about

        Returns
        - this
        """
        ...


    def rotation(self, angle: float, axis: "Vector3fc") -> "Matrix4x3d":
        """
        Set this matrix to a rotation matrix which rotates the given radians about a given axis.
        
        The axis described by the `axis` vector needs to be a unit vector.
        
        When used with a right-handed coordinate system, the produced rotation will rotate a vector 
        counter-clockwise around the rotation axis, when viewing along the negative axis direction towards the origin.
        When used with a left-handed coordinate system, the rotation is clockwise.

        Arguments
        - angle: the angle in radians
        - axis: the axis to rotate about

        Returns
        - this
        """
        ...


    def transform(self, v: "Vector4d") -> "Vector4d":
        ...


    def transform(self, v: "Vector4dc", dest: "Vector4d") -> "Vector4d":
        ...


    def transformPosition(self, v: "Vector3d") -> "Vector3d":
        ...


    def transformPosition(self, v: "Vector3dc", dest: "Vector3d") -> "Vector3d":
        ...


    def transformDirection(self, v: "Vector3d") -> "Vector3d":
        ...


    def transformDirection(self, v: "Vector3dc", dest: "Vector3d") -> "Vector3d":
        ...


    def set3x3(self, mat: "Matrix3dc") -> "Matrix4x3d":
        """
        Set the left 3x3 submatrix of this Matrix4x3d to the given Matrix3dc and don't change the other elements.

        Arguments
        - mat: the 3x3 matrix

        Returns
        - this
        """
        ...


    def set3x3(self, mat: "Matrix3fc") -> "Matrix4x3d":
        """
        Set the left 3x3 submatrix of this Matrix4x3d to the given Matrix3fc and don't change the other elements.

        Arguments
        - mat: the 3x3 matrix

        Returns
        - this
        """
        ...


    def scale(self, xyz: "Vector3dc", dest: "Matrix4x3d") -> "Matrix4x3d":
        ...


    def scale(self, xyz: "Vector3dc") -> "Matrix4x3d":
        """
        Apply scaling to this matrix by scaling the base axes by the given `xyz.x`,
        `xyz.y` and `xyz.z` factors, respectively.
        
        If `M` is `this` matrix and `S` the scaling matrix,
        then the new matrix will be `M * S`. So when transforming a
        vector `v` with the new matrix by using `M * S * v`, the
        scaling will be applied first!

        Arguments
        - xyz: the factors of the x, y and z component, respectively

        Returns
        - this
        """
        ...


    def scale(self, x: float, y: float, z: float, dest: "Matrix4x3d") -> "Matrix4x3d":
        ...


    def scale(self, x: float, y: float, z: float) -> "Matrix4x3d":
        """
        Apply scaling to `this` matrix by scaling the base axes by the given x,
        y and z factors.
        
        If `M` is `this` matrix and `S` the scaling matrix,
        then the new matrix will be `M * S`. So when transforming a
        vector `v` with the new matrix by using `M * S * v`
        , the scaling will be applied first!

        Arguments
        - x: the factor of the x component
        - y: the factor of the y component
        - z: the factor of the z component

        Returns
        - this
        """
        ...


    def scale(self, xyz: float, dest: "Matrix4x3d") -> "Matrix4x3d":
        ...


    def scale(self, xyz: float) -> "Matrix4x3d":
        """
        Apply scaling to this matrix by uniformly scaling all base axes by the given xyz factor.
        
        If `M` is `this` matrix and `S` the scaling matrix,
        then the new matrix will be `M * S`. So when transforming a
        vector `v` with the new matrix by using `M * S * v`
        , the scaling will be applied first!

        Arguments
        - xyz: the factor for all components

        Returns
        - this

        See
        - .scale(double, double, double)
        """
        ...


    def scaleXY(self, x: float, y: float, dest: "Matrix4x3d") -> "Matrix4x3d":
        ...


    def scaleXY(self, x: float, y: float) -> "Matrix4x3d":
        """
        Apply scaling to this matrix by scaling the X axis by `x` and the Y axis by `y`.
        
        If `M` is `this` matrix and `S` the scaling matrix,
        then the new matrix will be `M * S`. So when transforming a
        vector `v` with the new matrix by using `M * S * v`, the
        scaling will be applied first!

        Arguments
        - x: the factor of the x component
        - y: the factor of the y component

        Returns
        - this
        """
        ...


    def scaleAround(self, sx: float, sy: float, sz: float, ox: float, oy: float, oz: float, dest: "Matrix4x3d") -> "Matrix4x3d":
        ...


    def scaleAround(self, sx: float, sy: float, sz: float, ox: float, oy: float, oz: float) -> "Matrix4x3d":
        """
        Apply scaling to this matrix by scaling the base axes by the given sx,
        sy and sz factors while using `(ox, oy, oz)` as the scaling origin.
        
        If `M` is `this` matrix and `S` the scaling matrix,
        then the new matrix will be `M * S`. So when transforming a
        vector `v` with the new matrix by using `M * S * v`, the
        scaling will be applied first!
        
        This method is equivalent to calling: `translate(ox, oy, oz).scale(sx, sy, sz).translate(-ox, -oy, -oz)`

        Arguments
        - sx: the scaling factor of the x component
        - sy: the scaling factor of the y component
        - sz: the scaling factor of the z component
        - ox: the x coordinate of the scaling origin
        - oy: the y coordinate of the scaling origin
        - oz: the z coordinate of the scaling origin

        Returns
        - this
        """
        ...


    def scaleAround(self, factor: float, ox: float, oy: float, oz: float) -> "Matrix4x3d":
        """
        Apply scaling to this matrix by scaling all three base axes by the given `factor`
        while using `(ox, oy, oz)` as the scaling origin.
        
        If `M` is `this` matrix and `S` the scaling matrix,
        then the new matrix will be `M * S`. So when transforming a
        vector `v` with the new matrix by using `M * S * v`, the
        scaling will be applied first!
        
        This method is equivalent to calling: `translate(ox, oy, oz).scale(factor).translate(-ox, -oy, -oz)`

        Arguments
        - factor: the scaling factor for all three axes
        - ox: the x coordinate of the scaling origin
        - oy: the y coordinate of the scaling origin
        - oz: the z coordinate of the scaling origin

        Returns
        - this
        """
        ...


    def scaleAround(self, factor: float, ox: float, oy: float, oz: float, dest: "Matrix4x3d") -> "Matrix4x3d":
        ...


    def scaleLocal(self, x: float, y: float, z: float, dest: "Matrix4x3d") -> "Matrix4x3d":
        ...


    def scaleLocal(self, x: float, y: float, z: float) -> "Matrix4x3d":
        """
        Pre-multiply scaling to this matrix by scaling the base axes by the given x,
        y and z factors.
        
        If `M` is `this` matrix and `S` the scaling matrix,
        then the new matrix will be `S * M`. So when transforming a
        vector `v` with the new matrix by using `S * M * v`, the
        scaling will be applied last!

        Arguments
        - x: the factor of the x component
        - y: the factor of the y component
        - z: the factor of the z component

        Returns
        - this
        """
        ...


    def rotate(self, ang: float, x: float, y: float, z: float, dest: "Matrix4x3d") -> "Matrix4x3d":
        ...


    def rotate(self, ang: float, x: float, y: float, z: float) -> "Matrix4x3d":
        """
        Apply rotation to this matrix by rotating the given amount of radians
        about the given axis specified as x, y and z components.
        
        When used with a right-handed coordinate system, the produced rotation will rotate a vector 
        counter-clockwise around the rotation axis, when viewing along the negative axis direction towards the origin.
        When used with a left-handed coordinate system, the rotation is clockwise.
        
        If `M` is `this` matrix and `R` the rotation matrix,
        then the new matrix will be `M * R`. So when transforming a
        vector `v` with the new matrix by using `M * R * v`
        , the rotation will be applied first!
        
        In order to set the matrix to a rotation matrix without post-multiplying the rotation
        transformation, use .rotation(double, double, double, double) rotation().

        Arguments
        - ang: the angle is in radians
        - x: the x component of the axis
        - y: the y component of the axis
        - z: the z component of the axis

        Returns
        - this

        See
        - .rotation(double, double, double, double)
        """
        ...


    def rotateTranslation(self, ang: float, x: float, y: float, z: float, dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Apply rotation to this matrix, which is assumed to only contain a translation, by rotating the given amount of radians
        about the specified `(x, y, z)` axis and store the result in `dest`.
        
        This method assumes `this` to only contain a translation.
        
        The axis described by the three components needs to be a unit vector.
        
        When used with a right-handed coordinate system, the produced rotation will rotate a vector 
        counter-clockwise around the rotation axis, when viewing along the negative axis direction towards the origin.
        When used with a left-handed coordinate system, the rotation is clockwise.
        
        If `M` is `this` matrix and `R` the rotation matrix,
        then the new matrix will be `M * R`. So when transforming a
        vector `v` with the new matrix by using `M * R * v`, the
        rotation will be applied first!
        
        In order to set the matrix to a rotation matrix without post-multiplying the rotation
        transformation, use .rotation(double, double, double, double) rotation().
        
        Reference: <a href="http://en.wikipedia.org/wiki/Rotation_matrix#Rotation_matrix_from_axis_and_angle">http://en.wikipedia.org</a>

        Arguments
        - ang: the angle in radians
        - x: the x component of the axis
        - y: the y component of the axis
        - z: the z component of the axis
        - dest: will hold the result

        Returns
        - dest

        See
        - .rotation(double, double, double, double)
        """
        ...


    def rotateAround(self, quat: "Quaterniondc", ox: float, oy: float, oz: float) -> "Matrix4x3d":
        """
        Apply the rotation transformation of the given Quaterniondc to this matrix while using `(ox, oy, oz)` as the rotation origin.
        
        When used with a right-handed coordinate system, the produced rotation will rotate a vector 
        counter-clockwise around the rotation axis, when viewing along the negative axis direction towards the origin.
        When used with a left-handed coordinate system, the rotation is clockwise.
        
        If `M` is `this` matrix and `Q` the rotation matrix obtained from the given quaternion,
        then the new matrix will be `M * Q`. So when transforming a
        vector `v` with the new matrix by using `M * Q * v`,
        the quaternion rotation will be applied first!
        
        This method is equivalent to calling: `translate(ox, oy, oz).rotate(quat).translate(-ox, -oy, -oz)`
        
        Reference: <a href="http://en.wikipedia.org/wiki/Rotation_matrix#Quaternion">http://en.wikipedia.org</a>

        Arguments
        - quat: the Quaterniondc
        - ox: the x coordinate of the rotation origin
        - oy: the y coordinate of the rotation origin
        - oz: the z coordinate of the rotation origin

        Returns
        - this
        """
        ...


    def rotateAround(self, quat: "Quaterniondc", ox: float, oy: float, oz: float, dest: "Matrix4x3d") -> "Matrix4x3d":
        ...


    def rotationAround(self, quat: "Quaterniondc", ox: float, oy: float, oz: float) -> "Matrix4x3d":
        """
        Set this matrix to a transformation composed of a rotation of the specified Quaterniondc while using `(ox, oy, oz)` as the rotation origin.
        
        When used with a right-handed coordinate system, the produced rotation will rotate a vector 
        counter-clockwise around the rotation axis, when viewing along the negative axis direction towards the origin.
        When used with a left-handed coordinate system, the rotation is clockwise.
        
        This method is equivalent to calling: `translation(ox, oy, oz).rotate(quat).translate(-ox, -oy, -oz)`
        
        Reference: <a href="http://en.wikipedia.org/wiki/Rotation_matrix#Quaternion">http://en.wikipedia.org</a>

        Arguments
        - quat: the Quaterniondc
        - ox: the x coordinate of the rotation origin
        - oy: the y coordinate of the rotation origin
        - oz: the z coordinate of the rotation origin

        Returns
        - this
        """
        ...


    def rotateLocal(self, ang: float, x: float, y: float, z: float, dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Pre-multiply a rotation to this matrix by rotating the given amount of radians
        about the specified `(x, y, z)` axis and store the result in `dest`.
        
        The axis described by the three components needs to be a unit vector.
        
        When used with a right-handed coordinate system, the produced rotation will rotate a vector 
        counter-clockwise around the rotation axis, when viewing along the negative axis direction towards the origin.
        When used with a left-handed coordinate system, the rotation is clockwise.
        
        If `M` is `this` matrix and `R` the rotation matrix,
        then the new matrix will be `R * M`. So when transforming a
        vector `v` with the new matrix by using `R * M * v`, the
        rotation will be applied last!
        
        In order to set the matrix to a rotation matrix without pre-multiplying the rotation
        transformation, use .rotation(double, double, double, double) rotation().
        
        Reference: <a href="http://en.wikipedia.org/wiki/Rotation_matrix#Rotation_matrix_from_axis_and_angle">http://en.wikipedia.org</a>

        Arguments
        - ang: the angle in radians
        - x: the x component of the axis
        - y: the y component of the axis
        - z: the z component of the axis
        - dest: will hold the result

        Returns
        - dest

        See
        - .rotation(double, double, double, double)
        """
        ...


    def rotateLocal(self, ang: float, x: float, y: float, z: float) -> "Matrix4x3d":
        """
        Pre-multiply a rotation to this matrix by rotating the given amount of radians
        about the specified `(x, y, z)` axis.
        
        The axis described by the three components needs to be a unit vector.
        
        When used with a right-handed coordinate system, the produced rotation will rotate a vector 
        counter-clockwise around the rotation axis, when viewing along the negative axis direction towards the origin.
        When used with a left-handed coordinate system, the rotation is clockwise.
        
        If `M` is `this` matrix and `R` the rotation matrix,
        then the new matrix will be `R * M`. So when transforming a
        vector `v` with the new matrix by using `R * M * v`, the
        rotation will be applied last!
        
        In order to set the matrix to a rotation matrix without pre-multiplying the rotation
        transformation, use .rotation(double, double, double, double) rotation().
        
        Reference: <a href="http://en.wikipedia.org/wiki/Rotation_matrix#Rotation_matrix_from_axis_and_angle">http://en.wikipedia.org</a>

        Arguments
        - ang: the angle in radians
        - x: the x component of the axis
        - y: the y component of the axis
        - z: the z component of the axis

        Returns
        - this

        See
        - .rotation(double, double, double, double)
        """
        ...


    def rotateLocalX(self, ang: float, dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Pre-multiply a rotation around the X axis to this matrix by rotating the given amount of radians
        about the X axis and store the result in `dest`.
        
        When used with a right-handed coordinate system, the produced rotation will rotate a vector 
        counter-clockwise around the rotation axis, when viewing along the negative axis direction towards the origin.
        When used with a left-handed coordinate system, the rotation is clockwise.
        
        If `M` is `this` matrix and `R` the rotation matrix,
        then the new matrix will be `R * M`. So when transforming a
        vector `v` with the new matrix by using `R * M * v`, the
        rotation will be applied last!
        
        In order to set the matrix to a rotation matrix without pre-multiplying the rotation
        transformation, use .rotationX(double) rotationX().
        
        Reference: <a href="http://en.wikipedia.org/wiki/Rotation_matrix#Rotation_matrix_from_axis_and_angle">http://en.wikipedia.org</a>

        Arguments
        - ang: the angle in radians to rotate about the X axis
        - dest: will hold the result

        Returns
        - dest

        See
        - .rotationX(double)
        """
        ...


    def rotateLocalX(self, ang: float) -> "Matrix4x3d":
        """
        Pre-multiply a rotation to this matrix by rotating the given amount of radians about the X axis.
        
        When used with a right-handed coordinate system, the produced rotation will rotate a vector 
        counter-clockwise around the rotation axis, when viewing along the negative axis direction towards the origin.
        When used with a left-handed coordinate system, the rotation is clockwise.
        
        If `M` is `this` matrix and `R` the rotation matrix,
        then the new matrix will be `R * M`. So when transforming a
        vector `v` with the new matrix by using `R * M * v`, the
        rotation will be applied last!
        
        In order to set the matrix to a rotation matrix without pre-multiplying the rotation
        transformation, use .rotationX(double) rotationX().
        
        Reference: <a href="http://en.wikipedia.org/wiki/Rotation_matrix#Rotation_matrix_from_axis_and_angle">http://en.wikipedia.org</a>

        Arguments
        - ang: the angle in radians to rotate about the X axis

        Returns
        - this

        See
        - .rotationX(double)
        """
        ...


    def rotateLocalY(self, ang: float, dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Pre-multiply a rotation around the Y axis to this matrix by rotating the given amount of radians
        about the Y axis and store the result in `dest`.
        
        When used with a right-handed coordinate system, the produced rotation will rotate a vector 
        counter-clockwise around the rotation axis, when viewing along the negative axis direction towards the origin.
        When used with a left-handed coordinate system, the rotation is clockwise.
        
        If `M` is `this` matrix and `R` the rotation matrix,
        then the new matrix will be `R * M`. So when transforming a
        vector `v` with the new matrix by using `R * M * v`, the
        rotation will be applied last!
        
        In order to set the matrix to a rotation matrix without pre-multiplying the rotation
        transformation, use .rotationY(double) rotationY().
        
        Reference: <a href="http://en.wikipedia.org/wiki/Rotation_matrix#Rotation_matrix_from_axis_and_angle">http://en.wikipedia.org</a>

        Arguments
        - ang: the angle in radians to rotate about the Y axis
        - dest: will hold the result

        Returns
        - dest

        See
        - .rotationY(double)
        """
        ...


    def rotateLocalY(self, ang: float) -> "Matrix4x3d":
        """
        Pre-multiply a rotation to this matrix by rotating the given amount of radians about the Y axis.
        
        When used with a right-handed coordinate system, the produced rotation will rotate a vector 
        counter-clockwise around the rotation axis, when viewing along the negative axis direction towards the origin.
        When used with a left-handed coordinate system, the rotation is clockwise.
        
        If `M` is `this` matrix and `R` the rotation matrix,
        then the new matrix will be `R * M`. So when transforming a
        vector `v` with the new matrix by using `R * M * v`, the
        rotation will be applied last!
        
        In order to set the matrix to a rotation matrix without pre-multiplying the rotation
        transformation, use .rotationY(double) rotationY().
        
        Reference: <a href="http://en.wikipedia.org/wiki/Rotation_matrix#Rotation_matrix_from_axis_and_angle">http://en.wikipedia.org</a>

        Arguments
        - ang: the angle in radians to rotate about the Y axis

        Returns
        - this

        See
        - .rotationY(double)
        """
        ...


    def rotateLocalZ(self, ang: float, dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Pre-multiply a rotation around the Z axis to this matrix by rotating the given amount of radians
        about the Z axis and store the result in `dest`.
        
        When used with a right-handed coordinate system, the produced rotation will rotate a vector 
        counter-clockwise around the rotation axis, when viewing along the negative axis direction towards the origin.
        When used with a left-handed coordinate system, the rotation is clockwise.
        
        If `M` is `this` matrix and `R` the rotation matrix,
        then the new matrix will be `R * M`. So when transforming a
        vector `v` with the new matrix by using `R * M * v`, the
        rotation will be applied last!
        
        In order to set the matrix to a rotation matrix without pre-multiplying the rotation
        transformation, use .rotationZ(double) rotationZ().
        
        Reference: <a href="http://en.wikipedia.org/wiki/Rotation_matrix#Rotation_matrix_from_axis_and_angle">http://en.wikipedia.org</a>

        Arguments
        - ang: the angle in radians to rotate about the Z axis
        - dest: will hold the result

        Returns
        - dest

        See
        - .rotationZ(double)
        """
        ...


    def rotateLocalZ(self, ang: float) -> "Matrix4x3d":
        """
        Pre-multiply a rotation to this matrix by rotating the given amount of radians about the Z axis.
        
        When used with a right-handed coordinate system, the produced rotation will rotate a vector 
        counter-clockwise around the rotation axis, when viewing along the negative axis direction towards the origin.
        When used with a left-handed coordinate system, the rotation is clockwise.
        
        If `M` is `this` matrix and `R` the rotation matrix,
        then the new matrix will be `R * M`. So when transforming a
        vector `v` with the new matrix by using `R * M * v`, the
        rotation will be applied last!
        
        In order to set the matrix to a rotation matrix without pre-multiplying the rotation
        transformation, use .rotationZ(double) rotationY().
        
        Reference: <a href="http://en.wikipedia.org/wiki/Rotation_matrix#Rotation_matrix_from_axis_and_angle">http://en.wikipedia.org</a>

        Arguments
        - ang: the angle in radians to rotate about the Z axis

        Returns
        - this

        See
        - .rotationY(double)
        """
        ...


    def translate(self, offset: "Vector3dc") -> "Matrix4x3d":
        """
        Apply a translation to this matrix by translating by the given number of
        units in x, y and z.
        
        If `M` is `this` matrix and `T` the translation
        matrix, then the new matrix will be `M * T`. So when
        transforming a vector `v` with the new matrix by using
        `M * T * v`, the translation will be applied first!
        
        In order to set the matrix to a translation transformation without post-multiplying
        it, use .translation(Vector3dc).

        Arguments
        - offset: the number of units in x, y and z by which to translate

        Returns
        - this

        See
        - .translation(Vector3dc)
        """
        ...


    def translate(self, offset: "Vector3dc", dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Apply a translation to this matrix by translating by the given number of
        units in x, y and z and store the result in `dest`.
        
        If `M` is `this` matrix and `T` the translation
        matrix, then the new matrix will be `M * T`. So when
        transforming a vector `v` with the new matrix by using
        `M * T * v`, the translation will be applied first!
        
        In order to set the matrix to a translation transformation without post-multiplying
        it, use .translation(Vector3dc).

        Arguments
        - offset: the number of units in x, y and z by which to translate
        - dest: will hold the result

        Returns
        - dest

        See
        - .translation(Vector3dc)
        """
        ...


    def translate(self, offset: "Vector3fc") -> "Matrix4x3d":
        """
        Apply a translation to this matrix by translating by the given number of
        units in x, y and z.
        
        If `M` is `this` matrix and `T` the translation
        matrix, then the new matrix will be `M * T`. So when
        transforming a vector `v` with the new matrix by using
        `M * T * v`, the translation will be applied first!
        
        In order to set the matrix to a translation transformation without post-multiplying
        it, use .translation(Vector3fc).

        Arguments
        - offset: the number of units in x, y and z by which to translate

        Returns
        - this

        See
        - .translation(Vector3fc)
        """
        ...


    def translate(self, offset: "Vector3fc", dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Apply a translation to this matrix by translating by the given number of
        units in x, y and z and store the result in `dest`.
        
        If `M` is `this` matrix and `T` the translation
        matrix, then the new matrix will be `M * T`. So when
        transforming a vector `v` with the new matrix by using
        `M * T * v`, the translation will be applied first!
        
        In order to set the matrix to a translation transformation without post-multiplying
        it, use .translation(Vector3fc).

        Arguments
        - offset: the number of units in x, y and z by which to translate
        - dest: will hold the result

        Returns
        - dest

        See
        - .translation(Vector3fc)
        """
        ...


    def translate(self, x: float, y: float, z: float, dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Apply a translation to this matrix by translating by the given number of
        units in x, y and z and store the result in `dest`.
        
        If `M` is `this` matrix and `T` the translation
        matrix, then the new matrix will be `M * T`. So when
        transforming a vector `v` with the new matrix by using
        `M * T * v`, the translation will be applied first!
        
        In order to set the matrix to a translation transformation without post-multiplying
        it, use .translation(double, double, double).

        Arguments
        - x: the offset to translate in x
        - y: the offset to translate in y
        - z: the offset to translate in z
        - dest: will hold the result

        Returns
        - dest

        See
        - .translation(double, double, double)
        """
        ...


    def translate(self, x: float, y: float, z: float) -> "Matrix4x3d":
        """
        Apply a translation to this matrix by translating by the given number of
        units in x, y and z.
        
        If `M` is `this` matrix and `T` the translation
        matrix, then the new matrix will be `M * T`. So when
        transforming a vector `v` with the new matrix by using
        `M * T * v`, the translation will be applied first!
        
        In order to set the matrix to a translation transformation without post-multiplying
        it, use .translation(double, double, double).

        Arguments
        - x: the offset to translate in x
        - y: the offset to translate in y
        - z: the offset to translate in z

        Returns
        - this

        See
        - .translation(double, double, double)
        """
        ...


    def translateLocal(self, offset: "Vector3fc") -> "Matrix4x3d":
        """
        Pre-multiply a translation to this matrix by translating by the given number of
        units in x, y and z.
        
        If `M` is `this` matrix and `T` the translation
        matrix, then the new matrix will be `T * M`. So when
        transforming a vector `v` with the new matrix by using
        `T * M * v`, the translation will be applied last!
        
        In order to set the matrix to a translation transformation without pre-multiplying
        it, use .translation(Vector3fc).

        Arguments
        - offset: the number of units in x, y and z by which to translate

        Returns
        - this

        See
        - .translation(Vector3fc)
        """
        ...


    def translateLocal(self, offset: "Vector3fc", dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Pre-multiply a translation to this matrix by translating by the given number of
        units in x, y and z and store the result in `dest`.
        
        If `M` is `this` matrix and `T` the translation
        matrix, then the new matrix will be `T * M`. So when
        transforming a vector `v` with the new matrix by using
        `T * M * v`, the translation will be applied last!
        
        In order to set the matrix to a translation transformation without pre-multiplying
        it, use .translation(Vector3fc).

        Arguments
        - offset: the number of units in x, y and z by which to translate
        - dest: will hold the result

        Returns
        - dest

        See
        - .translation(Vector3fc)
        """
        ...


    def translateLocal(self, offset: "Vector3dc") -> "Matrix4x3d":
        """
        Pre-multiply a translation to this matrix by translating by the given number of
        units in x, y and z.
        
        If `M` is `this` matrix and `T` the translation
        matrix, then the new matrix will be `T * M`. So when
        transforming a vector `v` with the new matrix by using
        `T * M * v`, the translation will be applied last!
        
        In order to set the matrix to a translation transformation without pre-multiplying
        it, use .translation(Vector3dc).

        Arguments
        - offset: the number of units in x, y and z by which to translate

        Returns
        - this

        See
        - .translation(Vector3dc)
        """
        ...


    def translateLocal(self, offset: "Vector3dc", dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Pre-multiply a translation to this matrix by translating by the given number of
        units in x, y and z and store the result in `dest`.
        
        If `M` is `this` matrix and `T` the translation
        matrix, then the new matrix will be `T * M`. So when
        transforming a vector `v` with the new matrix by using
        `T * M * v`, the translation will be applied last!
        
        In order to set the matrix to a translation transformation without pre-multiplying
        it, use .translation(Vector3dc).

        Arguments
        - offset: the number of units in x, y and z by which to translate
        - dest: will hold the result

        Returns
        - dest

        See
        - .translation(Vector3dc)
        """
        ...


    def translateLocal(self, x: float, y: float, z: float, dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Pre-multiply a translation to this matrix by translating by the given number of
        units in x, y and z and store the result in `dest`.
        
        If `M` is `this` matrix and `T` the translation
        matrix, then the new matrix will be `T * M`. So when
        transforming a vector `v` with the new matrix by using
        `T * M * v`, the translation will be applied last!
        
        In order to set the matrix to a translation transformation without pre-multiplying
        it, use .translation(double, double, double).

        Arguments
        - x: the offset to translate in x
        - y: the offset to translate in y
        - z: the offset to translate in z
        - dest: will hold the result

        Returns
        - dest

        See
        - .translation(double, double, double)
        """
        ...


    def translateLocal(self, x: float, y: float, z: float) -> "Matrix4x3d":
        """
        Pre-multiply a translation to this matrix by translating by the given number of
        units in x, y and z.
        
        If `M` is `this` matrix and `T` the translation
        matrix, then the new matrix will be `T * M`. So when
        transforming a vector `v` with the new matrix by using
        `T * M * v`, the translation will be applied last!
        
        In order to set the matrix to a translation transformation without pre-multiplying
        it, use .translation(double, double, double).

        Arguments
        - x: the offset to translate in x
        - y: the offset to translate in y
        - z: the offset to translate in z

        Returns
        - this

        See
        - .translation(double, double, double)
        """
        ...


    def writeExternal(self, out: "ObjectOutput") -> None:
        ...


    def readExternal(self, in: "ObjectInput") -> None:
        ...


    def rotateX(self, ang: float, dest: "Matrix4x3d") -> "Matrix4x3d":
        ...


    def rotateX(self, ang: float) -> "Matrix4x3d":
        """
        Apply rotation about the X axis to this matrix by rotating the given amount of radians.
        
        When used with a right-handed coordinate system, the produced rotation will rotate a vector 
        counter-clockwise around the rotation axis, when viewing along the negative axis direction towards the origin.
        When used with a left-handed coordinate system, the rotation is clockwise.
        
        If `M` is `this` matrix and `R` the rotation matrix,
        then the new matrix will be `M * R`. So when transforming a
        vector `v` with the new matrix by using `M * R * v`, the
        rotation will be applied first!
        
        Reference: <a href="http://en.wikipedia.org/wiki/Rotation_matrix#Basic_rotations">http://en.wikipedia.org</a>

        Arguments
        - ang: the angle in radians

        Returns
        - this
        """
        ...


    def rotateY(self, ang: float, dest: "Matrix4x3d") -> "Matrix4x3d":
        ...


    def rotateY(self, ang: float) -> "Matrix4x3d":
        """
        Apply rotation about the Y axis to this matrix by rotating the given amount of radians.
        
        When used with a right-handed coordinate system, the produced rotation will rotate a vector 
        counter-clockwise around the rotation axis, when viewing along the negative axis direction towards the origin.
        When used with a left-handed coordinate system, the rotation is clockwise.
        
        If `M` is `this` matrix and `R` the rotation matrix,
        then the new matrix will be `M * R`. So when transforming a
        vector `v` with the new matrix by using `M * R * v`, the
        rotation will be applied first!
        
        Reference: <a href="http://en.wikipedia.org/wiki/Rotation_matrix#Basic_rotations">http://en.wikipedia.org</a>

        Arguments
        - ang: the angle in radians

        Returns
        - this
        """
        ...


    def rotateZ(self, ang: float, dest: "Matrix4x3d") -> "Matrix4x3d":
        ...


    def rotateZ(self, ang: float) -> "Matrix4x3d":
        """
        Apply rotation about the Z axis to this matrix by rotating the given amount of radians.
        
        When used with a right-handed coordinate system, the produced rotation will rotate a vector 
        counter-clockwise around the rotation axis, when viewing along the negative axis direction towards the origin.
        When used with a left-handed coordinate system, the rotation is clockwise.
        
        If `M` is `this` matrix and `R` the rotation matrix,
        then the new matrix will be `M * R`. So when transforming a
        vector `v` with the new matrix by using `M * R * v`, the
        rotation will be applied first!
        
        Reference: <a href="http://en.wikipedia.org/wiki/Rotation_matrix#Basic_rotations">http://en.wikipedia.org</a>

        Arguments
        - ang: the angle in radians

        Returns
        - this
        """
        ...


    def rotateXYZ(self, angles: "Vector3d") -> "Matrix4x3d":
        """
        Apply rotation of `angles.x` radians about the X axis, followed by a rotation of `angles.y` radians about the Y axis and
        followed by a rotation of `angles.z` radians about the Z axis.
        
        When used with a right-handed coordinate system, the produced rotation will rotate a vector 
        counter-clockwise around the rotation axis, when viewing along the negative axis direction towards the origin.
        When used with a left-handed coordinate system, the rotation is clockwise.
        
        If `M` is `this` matrix and `R` the rotation matrix,
        then the new matrix will be `M * R`. So when transforming a
        vector `v` with the new matrix by using `M * R * v`, the
        rotation will be applied first!
        
        This method is equivalent to calling: `rotateX(angles.x).rotateY(angles.y).rotateZ(angles.z)`

        Arguments
        - angles: the Euler angles

        Returns
        - this
        """
        ...


    def rotateXYZ(self, angleX: float, angleY: float, angleZ: float) -> "Matrix4x3d":
        """
        Apply rotation of `angleX` radians about the X axis, followed by a rotation of `angleY` radians about the Y axis and
        followed by a rotation of `angleZ` radians about the Z axis.
        
        When used with a right-handed coordinate system, the produced rotation will rotate a vector 
        counter-clockwise around the rotation axis, when viewing along the negative axis direction towards the origin.
        When used with a left-handed coordinate system, the rotation is clockwise.
        
        If `M` is `this` matrix and `R` the rotation matrix,
        then the new matrix will be `M * R`. So when transforming a
        vector `v` with the new matrix by using `M * R * v`, the
        rotation will be applied first!
        
        This method is equivalent to calling: `rotateX(angleX).rotateY(angleY).rotateZ(angleZ)`

        Arguments
        - angleX: the angle to rotate about X
        - angleY: the angle to rotate about Y
        - angleZ: the angle to rotate about Z

        Returns
        - this
        """
        ...


    def rotateXYZ(self, angleX: float, angleY: float, angleZ: float, dest: "Matrix4x3d") -> "Matrix4x3d":
        ...


    def rotateZYX(self, angles: "Vector3d") -> "Matrix4x3d":
        """
        Apply rotation of `angles.z` radians about the Z axis, followed by a rotation of `angles.y` radians about the Y axis and
        followed by a rotation of `angles.x` radians about the X axis.
        
        When used with a right-handed coordinate system, the produced rotation will rotate a vector 
        counter-clockwise around the rotation axis, when viewing along the negative axis direction towards the origin.
        When used with a left-handed coordinate system, the rotation is clockwise.
        
        If `M` is `this` matrix and `R` the rotation matrix,
        then the new matrix will be `M * R`. So when transforming a
        vector `v` with the new matrix by using `M * R * v`, the
        rotation will be applied first!
        
        This method is equivalent to calling: `rotateZ(angles.z).rotateY(angles.y).rotateX(angles.x)`

        Arguments
        - angles: the Euler angles

        Returns
        - this
        """
        ...


    def rotateZYX(self, angleZ: float, angleY: float, angleX: float) -> "Matrix4x3d":
        """
        Apply rotation of `angleZ` radians about the Z axis, followed by a rotation of `angleY` radians about the Y axis and
        followed by a rotation of `angleX` radians about the X axis.
        
        When used with a right-handed coordinate system, the produced rotation will rotate a vector 
        counter-clockwise around the rotation axis, when viewing along the negative axis direction towards the origin.
        When used with a left-handed coordinate system, the rotation is clockwise.
        
        If `M` is `this` matrix and `R` the rotation matrix,
        then the new matrix will be `M * R`. So when transforming a
        vector `v` with the new matrix by using `M * R * v`, the
        rotation will be applied first!
        
        This method is equivalent to calling: `rotateZ(angleZ).rotateY(angleY).rotateX(angleX)`

        Arguments
        - angleZ: the angle to rotate about Z
        - angleY: the angle to rotate about Y
        - angleX: the angle to rotate about X

        Returns
        - this
        """
        ...


    def rotateZYX(self, angleZ: float, angleY: float, angleX: float, dest: "Matrix4x3d") -> "Matrix4x3d":
        ...


    def rotateYXZ(self, angles: "Vector3d") -> "Matrix4x3d":
        """
        Apply rotation of `angles.y` radians about the Y axis, followed by a rotation of `angles.x` radians about the X axis and
        followed by a rotation of `angles.z` radians about the Z axis.
        
        When used with a right-handed coordinate system, the produced rotation will rotate a vector 
        counter-clockwise around the rotation axis, when viewing along the negative axis direction towards the origin.
        When used with a left-handed coordinate system, the rotation is clockwise.
        
        If `M` is `this` matrix and `R` the rotation matrix,
        then the new matrix will be `M * R`. So when transforming a
        vector `v` with the new matrix by using `M * R * v`, the
        rotation will be applied first!
        
        This method is equivalent to calling: `rotateY(angles.y).rotateX(angles.x).rotateZ(angles.z)`

        Arguments
        - angles: the Euler angles

        Returns
        - this
        """
        ...


    def rotateYXZ(self, angleY: float, angleX: float, angleZ: float) -> "Matrix4x3d":
        """
        Apply rotation of `angleY` radians about the Y axis, followed by a rotation of `angleX` radians about the X axis and
        followed by a rotation of `angleZ` radians about the Z axis.
        
        When used with a right-handed coordinate system, the produced rotation will rotate a vector 
        counter-clockwise around the rotation axis, when viewing along the negative axis direction towards the origin.
        When used with a left-handed coordinate system, the rotation is clockwise.
        
        If `M` is `this` matrix and `R` the rotation matrix,
        then the new matrix will be `M * R`. So when transforming a
        vector `v` with the new matrix by using `M * R * v`, the
        rotation will be applied first!
        
        This method is equivalent to calling: `rotateY(angleY).rotateX(angleX).rotateZ(angleZ)`

        Arguments
        - angleY: the angle to rotate about Y
        - angleX: the angle to rotate about X
        - angleZ: the angle to rotate about Z

        Returns
        - this
        """
        ...


    def rotateYXZ(self, angleY: float, angleX: float, angleZ: float, dest: "Matrix4x3d") -> "Matrix4x3d":
        ...


    def rotation(self, angleAxis: "AxisAngle4f") -> "Matrix4x3d":
        """
        Set this matrix to a rotation transformation using the given AxisAngle4f.
        
        When used with a right-handed coordinate system, the produced rotation will rotate a vector 
        counter-clockwise around the rotation axis, when viewing along the negative axis direction towards the origin.
        When used with a left-handed coordinate system, the rotation is clockwise.
        
        The resulting matrix can be multiplied against another transformation
        matrix to obtain an additional rotation.
        
        In order to apply the rotation transformation to an existing transformation,
        use .rotate(AxisAngle4f) rotate() instead.
        
        Reference: <a href="http://en.wikipedia.org/wiki/Rotation_matrix#Axis_and_angle">http://en.wikipedia.org</a>

        Arguments
        - angleAxis: the AxisAngle4f (needs to be AxisAngle4f.normalize() normalized)

        Returns
        - this

        See
        - .rotate(AxisAngle4f)
        """
        ...


    def rotation(self, angleAxis: "AxisAngle4d") -> "Matrix4x3d":
        """
        Set this matrix to a rotation transformation using the given AxisAngle4d.
        
        When used with a right-handed coordinate system, the produced rotation will rotate a vector 
        counter-clockwise around the rotation axis, when viewing along the negative axis direction towards the origin.
        When used with a left-handed coordinate system, the rotation is clockwise.
        
        The resulting matrix can be multiplied against another transformation
        matrix to obtain an additional rotation.
        
        In order to apply the rotation transformation to an existing transformation,
        use .rotate(AxisAngle4d) rotate() instead.
        
        Reference: <a href="http://en.wikipedia.org/wiki/Rotation_matrix#Axis_and_angle">http://en.wikipedia.org</a>

        Arguments
        - angleAxis: the AxisAngle4d (needs to be AxisAngle4d.normalize() normalized)

        Returns
        - this

        See
        - .rotate(AxisAngle4d)
        """
        ...


    def rotation(self, quat: "Quaterniondc") -> "Matrix4x3d":
        """
        Set this matrix to the rotation - and possibly scaling - transformation of the given Quaterniondc.
        
        When used with a right-handed coordinate system, the produced rotation will rotate a vector 
        counter-clockwise around the rotation axis, when viewing along the negative axis direction towards the origin.
        When used with a left-handed coordinate system, the rotation is clockwise.
        
        The resulting matrix can be multiplied against another transformation
        matrix to obtain an additional rotation.
        
        In order to apply the rotation transformation to an existing transformation,
        use .rotate(Quaterniondc) rotate() instead.
        
        Reference: <a href="http://en.wikipedia.org/wiki/Rotation_matrix#Quaternion">http://en.wikipedia.org</a>

        Arguments
        - quat: the Quaterniondc

        Returns
        - this

        See
        - .rotate(Quaterniondc)
        """
        ...


    def rotation(self, quat: "Quaternionfc") -> "Matrix4x3d":
        """
        Set this matrix to the rotation - and possibly scaling - transformation of the given Quaternionfc.
        
        When used with a right-handed coordinate system, the produced rotation will rotate a vector 
        counter-clockwise around the rotation axis, when viewing along the negative axis direction towards the origin.
        When used with a left-handed coordinate system, the rotation is clockwise.
        
        The resulting matrix can be multiplied against another transformation
        matrix to obtain an additional rotation.
        
        In order to apply the rotation transformation to an existing transformation,
        use .rotate(Quaternionfc) rotate() instead.
        
        Reference: <a href="http://en.wikipedia.org/wiki/Rotation_matrix#Quaternion">http://en.wikipedia.org</a>

        Arguments
        - quat: the Quaternionfc

        Returns
        - this

        See
        - .rotate(Quaternionfc)
        """
        ...


    def translationRotateScale(self, tx: float, ty: float, tz: float, qx: float, qy: float, qz: float, qw: float, sx: float, sy: float, sz: float) -> "Matrix4x3d":
        """
        Set `this` matrix to `T * R * S`, where `T` is a translation by the given `(tx, ty, tz)`,
        `R` is a rotation transformation specified by the quaternion `(qx, qy, qz, qw)`, and `S` is a scaling transformation
        which scales the three axes x, y and z by `(sx, sy, sz)`.
        
        When transforming a vector by the resulting matrix the scaling transformation will be applied first, then the rotation and
        at last the translation.
        
        When used with a right-handed coordinate system, the produced rotation will rotate a vector 
        counter-clockwise around the rotation axis, when viewing along the negative axis direction towards the origin.
        When used with a left-handed coordinate system, the rotation is clockwise.
        
        This method is equivalent to calling: `translation(tx, ty, tz).rotate(quat).scale(sx, sy, sz)`

        Arguments
        - tx: the number of units by which to translate the x-component
        - ty: the number of units by which to translate the y-component
        - tz: the number of units by which to translate the z-component
        - qx: the x-coordinate of the vector part of the quaternion
        - qy: the y-coordinate of the vector part of the quaternion
        - qz: the z-coordinate of the vector part of the quaternion
        - qw: the scalar part of the quaternion
        - sx: the scaling factor for the x-axis
        - sy: the scaling factor for the y-axis
        - sz: the scaling factor for the z-axis

        Returns
        - this

        See
        - .scale(double, double, double)
        """
        ...


    def translationRotateScale(self, translation: "Vector3fc", quat: "Quaternionfc", scale: "Vector3fc") -> "Matrix4x3d":
        """
        Set `this` matrix to `T * R * S`, where `T` is the given `translation`,
        `R` is a rotation transformation specified by the given quaternion, and `S` is a scaling transformation
        which scales the axes by `scale`.
        
        When transforming a vector by the resulting matrix the scaling transformation will be applied first, then the rotation and
        at last the translation.
        
        When used with a right-handed coordinate system, the produced rotation will rotate a vector 
        counter-clockwise around the rotation axis, when viewing along the negative axis direction towards the origin.
        When used with a left-handed coordinate system, the rotation is clockwise.
        
        This method is equivalent to calling: `translation(translation).rotate(quat).scale(scale)`

        Arguments
        - translation: the translation
        - quat: the quaternion representing a rotation
        - scale: the scaling factors

        Returns
        - this

        See
        - .rotate(Quaternionfc)
        """
        ...


    def translationRotateScale(self, translation: "Vector3dc", quat: "Quaterniondc", scale: "Vector3dc") -> "Matrix4x3d":
        """
        Set `this` matrix to `T * R * S`, where `T` is the given `translation`,
        `R` is a rotation transformation specified by the given quaternion, and `S` is a scaling transformation
        which scales the axes by `scale`.
        
        When transforming a vector by the resulting matrix the scaling transformation will be applied first, then the rotation and
        at last the translation.
        
        When used with a right-handed coordinate system, the produced rotation will rotate a vector 
        counter-clockwise around the rotation axis, when viewing along the negative axis direction towards the origin.
        When used with a left-handed coordinate system, the rotation is clockwise.
        
        This method is equivalent to calling: `translation(translation).rotate(quat).scale(scale)`

        Arguments
        - translation: the translation
        - quat: the quaternion representing a rotation
        - scale: the scaling factors

        Returns
        - this

        See
        - .rotate(Quaterniondc)
        """
        ...


    def translationRotateScaleMul(self, tx: float, ty: float, tz: float, qx: float, qy: float, qz: float, qw: float, sx: float, sy: float, sz: float, m: "Matrix4x3dc") -> "Matrix4x3d":
        """
        Set `this` matrix to `T * R * S * M`, where `T` is a translation by the given `(tx, ty, tz)`,
        `R` is a rotation transformation specified by the quaternion `(qx, qy, qz, qw)`, `S` is a scaling transformation
        which scales the three axes x, y and z by `(sx, sy, sz)`.
        
        When transforming a vector by the resulting matrix the transformation described by `M` will be applied first, then the scaling, then rotation and
        at last the translation.
        
        When used with a right-handed coordinate system, the produced rotation will rotate a vector 
        counter-clockwise around the rotation axis, when viewing along the negative axis direction towards the origin.
        When used with a left-handed coordinate system, the rotation is clockwise.
        
        This method is equivalent to calling: `translation(tx, ty, tz).rotate(quat).scale(sx, sy, sz).mul(m)`

        Arguments
        - tx: the number of units by which to translate the x-component
        - ty: the number of units by which to translate the y-component
        - tz: the number of units by which to translate the z-component
        - qx: the x-coordinate of the vector part of the quaternion
        - qy: the y-coordinate of the vector part of the quaternion
        - qz: the z-coordinate of the vector part of the quaternion
        - qw: the scalar part of the quaternion
        - sx: the scaling factor for the x-axis
        - sy: the scaling factor for the y-axis
        - sz: the scaling factor for the z-axis
        - m: the matrix to multiply by

        Returns
        - this

        See
        - .mul(Matrix4x3dc)
        """
        ...


    def translationRotateScaleMul(self, translation: "Vector3dc", quat: "Quaterniondc", scale: "Vector3dc", m: "Matrix4x3dc") -> "Matrix4x3d":
        """
        Set `this` matrix to `T * R * S * M`, where `T` is the given `translation`,
        `R` is a rotation transformation specified by the given quaternion, `S` is a scaling transformation
        which scales the axes by `scale`.
        
        When transforming a vector by the resulting matrix the transformation described by `M` will be applied first, then the scaling, then rotation and
        at last the translation.
        
        When used with a right-handed coordinate system, the produced rotation will rotate a vector 
        counter-clockwise around the rotation axis, when viewing along the negative axis direction towards the origin.
        When used with a left-handed coordinate system, the rotation is clockwise.
        
        This method is equivalent to calling: `translation(translation).rotate(quat).scale(scale).mul(m)`

        Arguments
        - translation: the translation
        - quat: the quaternion representing a rotation
        - scale: the scaling factors
        - m: the matrix to multiply by

        Returns
        - this

        See
        - .mul(Matrix4x3dc)
        """
        ...


    def translationRotate(self, tx: float, ty: float, tz: float, quat: "Quaterniondc") -> "Matrix4x3d":
        """
        Set `this` matrix to `T * R`, where `T` is a translation by the given `(tx, ty, tz)` and
        `R` is a rotation transformation specified by the given quaternion.
        
        When transforming a vector by the resulting matrix the rotation transformation will be applied first and then the translation.
        
        When used with a right-handed coordinate system, the produced rotation will rotate a vector 
        counter-clockwise around the rotation axis, when viewing along the negative axis direction towards the origin.
        When used with a left-handed coordinate system, the rotation is clockwise.
        
        This method is equivalent to calling: `translation(tx, ty, tz).rotate(quat)`

        Arguments
        - tx: the number of units by which to translate the x-component
        - ty: the number of units by which to translate the y-component
        - tz: the number of units by which to translate the z-component
        - quat: the quaternion representing a rotation

        Returns
        - this

        See
        - .rotate(Quaterniondc)
        """
        ...


    def translationRotate(self, tx: float, ty: float, tz: float, qx: float, qy: float, qz: float, qw: float) -> "Matrix4x3d":
        """
        Set `this` matrix to `T * R`, where `T` is a translation by the given `(tx, ty, tz)` and
        `R` is a rotation - and possibly scaling - transformation specified by the quaternion `(qx, qy, qz, qw)`.
        
        When transforming a vector by the resulting matrix the rotation - and possibly scaling - transformation will be applied first and then the translation.
        
        When used with a right-handed coordinate system, the produced rotation will rotate a vector 
        counter-clockwise around the rotation axis, when viewing along the negative axis direction towards the origin.
        When used with a left-handed coordinate system, the rotation is clockwise.
        
        This method is equivalent to calling: `translation(tx, ty, tz).rotate(quat)`

        Arguments
        - tx: the number of units by which to translate the x-component
        - ty: the number of units by which to translate the y-component
        - tz: the number of units by which to translate the z-component
        - qx: the x-coordinate of the vector part of the quaternion
        - qy: the y-coordinate of the vector part of the quaternion
        - qz: the z-coordinate of the vector part of the quaternion
        - qw: the scalar part of the quaternion

        Returns
        - this

        See
        - .rotate(Quaterniondc)
        """
        ...


    def translationRotate(self, translation: "Vector3dc", quat: "Quaterniondc") -> "Matrix4x3d":
        """
        Set `this` matrix to `T * R`, where `T` is the given `translation` and
        `R` is a rotation transformation specified by the given quaternion.
        
        When transforming a vector by the resulting matrix the scaling transformation will be applied first, then the rotation and
        at last the translation.
        
        When used with a right-handed coordinate system, the produced rotation will rotate a vector 
        counter-clockwise around the rotation axis, when viewing along the negative axis direction towards the origin.
        When used with a left-handed coordinate system, the rotation is clockwise.
        
        This method is equivalent to calling: `translation(translation).rotate(quat)`

        Arguments
        - translation: the translation
        - quat: the quaternion representing a rotation

        Returns
        - this

        See
        - .rotate(Quaterniondc)
        """
        ...


    def translationRotateMul(self, tx: float, ty: float, tz: float, quat: "Quaternionfc", mat: "Matrix4x3dc") -> "Matrix4x3d":
        """
        Set `this` matrix to `T * R * M`, where `T` is a translation by the given `(tx, ty, tz)`,
        `R` is a rotation - and possibly scaling - transformation specified by the given quaternion and `M` is the given matrix `mat`.
        
        When transforming a vector by the resulting matrix the transformation described by `M` will be applied first, then the scaling, then rotation and
        at last the translation.
        
        When used with a right-handed coordinate system, the produced rotation will rotate a vector 
        counter-clockwise around the rotation axis, when viewing along the negative axis direction towards the origin.
        When used with a left-handed coordinate system, the rotation is clockwise.
        
        This method is equivalent to calling: `translation(tx, ty, tz).rotate(quat).mul(mat)`

        Arguments
        - tx: the number of units by which to translate the x-component
        - ty: the number of units by which to translate the y-component
        - tz: the number of units by which to translate the z-component
        - quat: the quaternion representing a rotation
        - mat: the matrix to multiply with

        Returns
        - this

        See
        - .mul(Matrix4x3dc)
        """
        ...


    def translationRotateMul(self, tx: float, ty: float, tz: float, qx: float, qy: float, qz: float, qw: float, mat: "Matrix4x3dc") -> "Matrix4x3d":
        """
        Set `this` matrix to `T * R * M`, where `T` is a translation by the given `(tx, ty, tz)`,
        `R` is a rotation - and possibly scaling - transformation specified by the quaternion `(qx, qy, qz, qw)` and `M` is the given matrix `mat`
        
        When transforming a vector by the resulting matrix the transformation described by `M` will be applied first, then the scaling, then rotation and
        at last the translation.
        
        When used with a right-handed coordinate system, the produced rotation will rotate a vector 
        counter-clockwise around the rotation axis, when viewing along the negative axis direction towards the origin.
        When used with a left-handed coordinate system, the rotation is clockwise.
        
        This method is equivalent to calling: `translation(tx, ty, tz).rotate(quat).mul(mat)`

        Arguments
        - tx: the number of units by which to translate the x-component
        - ty: the number of units by which to translate the y-component
        - tz: the number of units by which to translate the z-component
        - qx: the x-coordinate of the vector part of the quaternion
        - qy: the y-coordinate of the vector part of the quaternion
        - qz: the z-coordinate of the vector part of the quaternion
        - qw: the scalar part of the quaternion
        - mat: the matrix to multiply with

        Returns
        - this

        See
        - .mul(Matrix4x3dc)
        """
        ...


    def translationRotateInvert(self, tx: float, ty: float, tz: float, qx: float, qy: float, qz: float, qw: float) -> "Matrix4x3d":
        """
        Set `this` matrix to `(T * R)<sup>-1</sup>`, where `T` is a translation by the given `(tx, ty, tz)` and
        `R` is a rotation transformation specified by the quaternion `(qx, qy, qz, qw)`.
        
        This method is equivalent to calling: `translationRotate(...).invert()`

        Arguments
        - tx: the number of units by which to translate the x-component
        - ty: the number of units by which to translate the y-component
        - tz: the number of units by which to translate the z-component
        - qx: the x-coordinate of the vector part of the quaternion
        - qy: the y-coordinate of the vector part of the quaternion
        - qz: the z-coordinate of the vector part of the quaternion
        - qw: the scalar part of the quaternion

        Returns
        - this

        See
        - .invert()
        """
        ...


    def translationRotateInvert(self, translation: "Vector3dc", quat: "Quaterniondc") -> "Matrix4x3d":
        """
        Set `this` matrix to `(T * R)<sup>-1</sup>`, where `T` is the given `translation` and
        `R` is a rotation transformation specified by the given quaternion.
        
        This method is equivalent to calling: `translationRotate(...).invert()`

        Arguments
        - translation: the translation
        - quat: the quaternion representing a rotation

        Returns
        - this

        See
        - .invert()
        """
        ...


    def rotate(self, quat: "Quaterniondc", dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Apply the rotation - and possibly scaling - transformation of the given Quaterniondc to this matrix and store
        the result in `dest`.
        
        When used with a right-handed coordinate system, the produced rotation will rotate a vector 
        counter-clockwise around the rotation axis, when viewing along the negative axis direction towards the origin.
        When used with a left-handed coordinate system, the rotation is clockwise.
        
        If `M` is `this` matrix and `Q` the rotation matrix obtained from the given quaternion,
        then the new matrix will be `M * Q`. So when transforming a
        vector `v` with the new matrix by using `M * Q * v`,
        the quaternion rotation will be applied first!
        
        In order to set the matrix to a rotation transformation without post-multiplying,
        use .rotation(Quaterniondc).
        
        Reference: <a href="http://en.wikipedia.org/wiki/Rotation_matrix#Quaternion">http://en.wikipedia.org</a>

        Arguments
        - quat: the Quaterniondc
        - dest: will hold the result

        Returns
        - dest

        See
        - .rotation(Quaterniondc)
        """
        ...


    def rotate(self, quat: "Quaternionfc", dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Apply the rotation - and possibly scaling - transformation of the given Quaternionfc to this matrix and store
        the result in `dest`.
        
        When used with a right-handed coordinate system, the produced rotation will rotate a vector 
        counter-clockwise around the rotation axis, when viewing along the negative axis direction towards the origin.
        When used with a left-handed coordinate system, the rotation is clockwise.
        
        If `M` is `this` matrix and `Q` the rotation matrix obtained from the given quaternion,
        then the new matrix will be `M * Q`. So when transforming a
        vector `v` with the new matrix by using `M * Q * v`,
        the quaternion rotation will be applied first!
        
        In order to set the matrix to a rotation transformation without post-multiplying,
        use .rotation(Quaternionfc).
        
        Reference: <a href="http://en.wikipedia.org/wiki/Rotation_matrix#Quaternion">http://en.wikipedia.org</a>

        Arguments
        - quat: the Quaternionfc
        - dest: will hold the result

        Returns
        - dest

        See
        - .rotation(Quaternionfc)
        """
        ...


    def rotate(self, quat: "Quaterniondc") -> "Matrix4x3d":
        """
        Apply the rotation - and possibly scaling - transformation of the given Quaterniondc to this matrix.
        
        When used with a right-handed coordinate system, the produced rotation will rotate a vector 
        counter-clockwise around the rotation axis, when viewing along the negative axis direction towards the origin.
        When used with a left-handed coordinate system, the rotation is clockwise.
        
        If `M` is `this` matrix and `Q` the rotation matrix obtained from the given quaternion,
        then the new matrix will be `M * Q`. So when transforming a
        vector `v` with the new matrix by using `M * Q * v`,
        the quaternion rotation will be applied first!
        
        In order to set the matrix to a rotation transformation without post-multiplying,
        use .rotation(Quaterniondc).
        
        Reference: <a href="http://en.wikipedia.org/wiki/Rotation_matrix#Quaternion">http://en.wikipedia.org</a>

        Arguments
        - quat: the Quaterniondc

        Returns
        - this

        See
        - .rotation(Quaterniondc)
        """
        ...


    def rotate(self, quat: "Quaternionfc") -> "Matrix4x3d":
        """
        Apply the rotation - and possibly scaling - transformation of the given Quaternionfc to this matrix.
        
        When used with a right-handed coordinate system, the produced rotation will rotate a vector 
        counter-clockwise around the rotation axis, when viewing along the negative axis direction towards the origin.
        When used with a left-handed coordinate system, the rotation is clockwise.
        
        If `M` is `this` matrix and `Q` the rotation matrix obtained from the given quaternion,
        then the new matrix will be `M * Q`. So when transforming a
        vector `v` with the new matrix by using `M * Q * v`,
        the quaternion rotation will be applied first!
        
        In order to set the matrix to a rotation transformation without post-multiplying,
        use .rotation(Quaternionfc).
        
        Reference: <a href="http://en.wikipedia.org/wiki/Rotation_matrix#Quaternion">http://en.wikipedia.org</a>

        Arguments
        - quat: the Quaternionfc

        Returns
        - this

        See
        - .rotation(Quaternionfc)
        """
        ...


    def rotateTranslation(self, quat: "Quaterniondc", dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Apply the rotation - and possibly scaling - transformation of the given Quaterniondc to this matrix, which is assumed to only contain a translation, and store
        the result in `dest`.
        
        This method assumes `this` to only contain a translation.
        
        When used with a right-handed coordinate system, the produced rotation will rotate a vector 
        counter-clockwise around the rotation axis, when viewing along the negative axis direction towards the origin.
        When used with a left-handed coordinate system, the rotation is clockwise.
        
        If `M` is `this` matrix and `Q` the rotation matrix obtained from the given quaternion,
        then the new matrix will be `M * Q`. So when transforming a
        vector `v` with the new matrix by using `M * Q * v`,
        the quaternion rotation will be applied first!
        
        In order to set the matrix to a rotation transformation without post-multiplying,
        use .rotation(Quaterniondc).
        
        Reference: <a href="http://en.wikipedia.org/wiki/Rotation_matrix#Quaternion">http://en.wikipedia.org</a>

        Arguments
        - quat: the Quaterniondc
        - dest: will hold the result

        Returns
        - dest

        See
        - .rotation(Quaterniondc)
        """
        ...


    def rotateTranslation(self, quat: "Quaternionfc", dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Apply the rotation - and possibly scaling - transformation of the given Quaternionfc to this matrix, which is assumed to only contain a translation, and store
        the result in `dest`.
        
        This method assumes `this` to only contain a translation.
        
        When used with a right-handed coordinate system, the produced rotation will rotate a vector 
        counter-clockwise around the rotation axis, when viewing along the negative axis direction towards the origin.
        When used with a left-handed coordinate system, the rotation is clockwise.
        
        If `M` is `this` matrix and `Q` the rotation matrix obtained from the given quaternion,
        then the new matrix will be `M * Q`. So when transforming a
        vector `v` with the new matrix by using `M * Q * v`,
        the quaternion rotation will be applied first!
        
        In order to set the matrix to a rotation transformation without post-multiplying,
        use .rotation(Quaternionfc).
        
        Reference: <a href="http://en.wikipedia.org/wiki/Rotation_matrix#Quaternion">http://en.wikipedia.org</a>

        Arguments
        - quat: the Quaternionfc
        - dest: will hold the result

        Returns
        - dest

        See
        - .rotation(Quaternionfc)
        """
        ...


    def rotateLocal(self, quat: "Quaterniondc", dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Pre-multiply the rotation - and possibly scaling - transformation of the given Quaterniondc to this matrix and store
        the result in `dest`.
        
        When used with a right-handed coordinate system, the produced rotation will rotate a vector 
        counter-clockwise around the rotation axis, when viewing along the negative axis direction towards the origin.
        When used with a left-handed coordinate system, the rotation is clockwise.
        
        If `M` is `this` matrix and `Q` the rotation matrix obtained from the given quaternion,
        then the new matrix will be `Q * M`. So when transforming a
        vector `v` with the new matrix by using `Q * M * v`,
        the quaternion rotation will be applied last!
        
        In order to set the matrix to a rotation transformation without pre-multiplying,
        use .rotation(Quaterniondc).
        
        Reference: <a href="http://en.wikipedia.org/wiki/Rotation_matrix#Quaternion">http://en.wikipedia.org</a>

        Arguments
        - quat: the Quaterniondc
        - dest: will hold the result

        Returns
        - dest

        See
        - .rotation(Quaterniondc)
        """
        ...


    def rotateLocal(self, quat: "Quaterniondc") -> "Matrix4x3d":
        """
        Pre-multiply the rotation transformation of the given Quaterniondc to this matrix.
        
        When used with a right-handed coordinate system, the produced rotation will rotate a vector 
        counter-clockwise around the rotation axis, when viewing along the negative axis direction towards the origin.
        When used with a left-handed coordinate system, the rotation is clockwise.
        
        If `M` is `this` matrix and `Q` the rotation matrix obtained from the given quaternion,
        then the new matrix will be `Q * M`. So when transforming a
        vector `v` with the new matrix by using `Q * M * v`,
        the quaternion rotation will be applied last!
        
        In order to set the matrix to a rotation transformation without pre-multiplying,
        use .rotation(Quaterniondc).
        
        Reference: <a href="http://en.wikipedia.org/wiki/Rotation_matrix#Quaternion">http://en.wikipedia.org</a>

        Arguments
        - quat: the Quaterniondc

        Returns
        - this

        See
        - .rotation(Quaterniondc)
        """
        ...


    def rotateLocal(self, quat: "Quaternionfc", dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Pre-multiply the rotation - and possibly scaling - transformation of the given Quaternionfc to this matrix and store
        the result in `dest`.
        
        When used with a right-handed coordinate system, the produced rotation will rotate a vector 
        counter-clockwise around the rotation axis, when viewing along the negative axis direction towards the origin.
        When used with a left-handed coordinate system, the rotation is clockwise.
        
        If `M` is `this` matrix and `Q` the rotation matrix obtained from the given quaternion,
        then the new matrix will be `Q * M`. So when transforming a
        vector `v` with the new matrix by using `Q * M * v`,
        the quaternion rotation will be applied last!
        
        In order to set the matrix to a rotation transformation without pre-multiplying,
        use .rotation(Quaternionfc).
        
        Reference: <a href="http://en.wikipedia.org/wiki/Rotation_matrix#Quaternion">http://en.wikipedia.org</a>

        Arguments
        - quat: the Quaternionfc
        - dest: will hold the result

        Returns
        - dest

        See
        - .rotation(Quaternionfc)
        """
        ...


    def rotateLocal(self, quat: "Quaternionfc") -> "Matrix4x3d":
        """
        Pre-multiply the rotation - and possibly scaling - transformation of the given Quaternionfc to this matrix.
        
        When used with a right-handed coordinate system, the produced rotation will rotate a vector 
        counter-clockwise around the rotation axis, when viewing along the negative axis direction towards the origin.
        When used with a left-handed coordinate system, the rotation is clockwise.
        
        If `M` is `this` matrix and `Q` the rotation matrix obtained from the given quaternion,
        then the new matrix will be `Q * M`. So when transforming a
        vector `v` with the new matrix by using `Q * M * v`,
        the quaternion rotation will be applied last!
        
        In order to set the matrix to a rotation transformation without pre-multiplying,
        use .rotation(Quaternionfc).
        
        Reference: <a href="http://en.wikipedia.org/wiki/Rotation_matrix#Quaternion">http://en.wikipedia.org</a>

        Arguments
        - quat: the Quaternionfc

        Returns
        - this

        See
        - .rotation(Quaternionfc)
        """
        ...


    def rotate(self, axisAngle: "AxisAngle4f") -> "Matrix4x3d":
        """
        Apply a rotation transformation, rotating about the given AxisAngle4f, to this matrix.
        
        The axis described by the `axis` vector needs to be a unit vector.
        
        When used with a right-handed coordinate system, the produced rotation will rotate a vector 
        counter-clockwise around the rotation axis, when viewing along the negative axis direction towards the origin.
        When used with a left-handed coordinate system, the rotation is clockwise.
        
        If `M` is `this` matrix and `A` the rotation matrix obtained from the given AxisAngle4f,
        then the new matrix will be `M * A`. So when transforming a
        vector `v` with the new matrix by using `M * A * v`,
        the AxisAngle4f rotation will be applied first!
        
        In order to set the matrix to a rotation transformation without post-multiplying,
        use .rotation(AxisAngle4f).
        
        Reference: <a href="http://en.wikipedia.org/wiki/Rotation_matrix#Axis_and_angle">http://en.wikipedia.org</a>

        Arguments
        - axisAngle: the AxisAngle4f (needs to be AxisAngle4f.normalize() normalized)

        Returns
        - this

        See
        - .rotation(AxisAngle4f)
        """
        ...


    def rotate(self, axisAngle: "AxisAngle4f", dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Apply a rotation transformation, rotating about the given AxisAngle4f and store the result in `dest`.
        
        The axis described by the `axis` vector needs to be a unit vector.
        
        When used with a right-handed coordinate system, the produced rotation will rotate a vector 
        counter-clockwise around the rotation axis, when viewing along the negative axis direction towards the origin.
        When used with a left-handed coordinate system, the rotation is clockwise.
        
        If `M` is `this` matrix and `A` the rotation matrix obtained from the given AxisAngle4f,
        then the new matrix will be `M * A`. So when transforming a
        vector `v` with the new matrix by using `M * A * v`,
        the AxisAngle4f rotation will be applied first!
        
        In order to set the matrix to a rotation transformation without post-multiplying,
        use .rotation(AxisAngle4f).
        
        Reference: <a href="http://en.wikipedia.org/wiki/Rotation_matrix#Axis_and_angle">http://en.wikipedia.org</a>

        Arguments
        - axisAngle: the AxisAngle4f (needs to be AxisAngle4f.normalize() normalized)
        - dest: will hold the result

        Returns
        - dest

        See
        - .rotation(AxisAngle4f)
        """
        ...


    def rotate(self, axisAngle: "AxisAngle4d") -> "Matrix4x3d":
        """
        Apply a rotation transformation, rotating about the given AxisAngle4d, to this matrix.
        
        When used with a right-handed coordinate system, the produced rotation will rotate a vector 
        counter-clockwise around the rotation axis, when viewing along the negative axis direction towards the origin.
        When used with a left-handed coordinate system, the rotation is clockwise.
        
        If `M` is `this` matrix and `A` the rotation matrix obtained from the given AxisAngle4d,
        then the new matrix will be `M * A`. So when transforming a
        vector `v` with the new matrix by using `M * A * v`,
        the AxisAngle4d rotation will be applied first!
        
        In order to set the matrix to a rotation transformation without post-multiplying,
        use .rotation(AxisAngle4d).
        
        Reference: <a href="http://en.wikipedia.org/wiki/Rotation_matrix#Axis_and_angle">http://en.wikipedia.org</a>

        Arguments
        - axisAngle: the AxisAngle4d (needs to be AxisAngle4d.normalize() normalized)

        Returns
        - this

        See
        - .rotation(AxisAngle4d)
        """
        ...


    def rotate(self, axisAngle: "AxisAngle4d", dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Apply a rotation transformation, rotating about the given AxisAngle4d and store the result in `dest`.
        
        When used with a right-handed coordinate system, the produced rotation will rotate a vector 
        counter-clockwise around the rotation axis, when viewing along the negative axis direction towards the origin.
        When used with a left-handed coordinate system, the rotation is clockwise.
        
        If `M` is `this` matrix and `A` the rotation matrix obtained from the given AxisAngle4d,
        then the new matrix will be `M * A`. So when transforming a
        vector `v` with the new matrix by using `M * A * v`,
        the AxisAngle4d rotation will be applied first!
        
        In order to set the matrix to a rotation transformation without post-multiplying,
        use .rotation(AxisAngle4d).
        
        Reference: <a href="http://en.wikipedia.org/wiki/Rotation_matrix#Axis_and_angle">http://en.wikipedia.org</a>

        Arguments
        - axisAngle: the AxisAngle4d (needs to be AxisAngle4d.normalize() normalized)
        - dest: will hold the result

        Returns
        - dest

        See
        - .rotation(AxisAngle4d)
        """
        ...


    def rotate(self, angle: float, axis: "Vector3dc") -> "Matrix4x3d":
        """
        Apply a rotation transformation, rotating the given radians about the specified axis, to this matrix.
        
        When used with a right-handed coordinate system, the produced rotation will rotate a vector 
        counter-clockwise around the rotation axis, when viewing along the negative axis direction towards the origin.
        When used with a left-handed coordinate system, the rotation is clockwise.
        
        If `M` is `this` matrix and `A` the rotation matrix obtained from the given angle and axis,
        then the new matrix will be `M * A`. So when transforming a
        vector `v` with the new matrix by using `M * A * v`,
        the axis-angle rotation will be applied first!
        
        In order to set the matrix to a rotation transformation without post-multiplying,
        use .rotation(double, Vector3dc).
        
        Reference: <a href="http://en.wikipedia.org/wiki/Rotation_matrix#Axis_and_angle">http://en.wikipedia.org</a>

        Arguments
        - angle: the angle in radians
        - axis: the rotation axis (needs to be Vector3d.normalize() normalized)

        Returns
        - this

        See
        - .rotation(double, Vector3dc)
        """
        ...


    def rotate(self, angle: float, axis: "Vector3dc", dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Apply a rotation transformation, rotating the given radians about the specified axis and store the result in `dest`.
        
        When used with a right-handed coordinate system, the produced rotation will rotate a vector 
        counter-clockwise around the rotation axis, when viewing along the negative axis direction towards the origin.
        When used with a left-handed coordinate system, the rotation is clockwise.
        
        If `M` is `this` matrix and `A` the rotation matrix obtained from the given angle and axis,
        then the new matrix will be `M * A`. So when transforming a
        vector `v` with the new matrix by using `M * A * v`,
        the axis-angle rotation will be applied first!
        
        In order to set the matrix to a rotation transformation without post-multiplying,
        use .rotation(double, Vector3dc).
        
        Reference: <a href="http://en.wikipedia.org/wiki/Rotation_matrix#Axis_and_angle">http://en.wikipedia.org</a>

        Arguments
        - angle: the angle in radians
        - axis: the rotation axis (needs to be Vector3d.normalize() normalized)
        - dest: will hold the result

        Returns
        - dest

        See
        - .rotation(double, Vector3dc)
        """
        ...


    def rotate(self, angle: float, axis: "Vector3fc") -> "Matrix4x3d":
        """
        Apply a rotation transformation, rotating the given radians about the specified axis, to this matrix.
        
        When used with a right-handed coordinate system, the produced rotation will rotate a vector 
        counter-clockwise around the rotation axis, when viewing along the negative axis direction towards the origin.
        When used with a left-handed coordinate system, the rotation is clockwise.
        
        If `M` is `this` matrix and `A` the rotation matrix obtained from the given angle and axis,
        then the new matrix will be `M * A`. So when transforming a
        vector `v` with the new matrix by using `M * A * v`,
        the axis-angle rotation will be applied first!
        
        In order to set the matrix to a rotation transformation without post-multiplying,
        use .rotation(double, Vector3fc).
        
        Reference: <a href="http://en.wikipedia.org/wiki/Rotation_matrix#Axis_and_angle">http://en.wikipedia.org</a>

        Arguments
        - angle: the angle in radians
        - axis: the rotation axis (needs to be Vector3f.normalize() normalized)

        Returns
        - this

        See
        - .rotation(double, Vector3fc)
        """
        ...


    def rotate(self, angle: float, axis: "Vector3fc", dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Apply a rotation transformation, rotating the given radians about the specified axis and store the result in `dest`.
        
        When used with a right-handed coordinate system, the produced rotation will rotate a vector 
        counter-clockwise around the rotation axis, when viewing along the negative axis direction towards the origin.
        When used with a left-handed coordinate system, the rotation is clockwise.
        
        If `M` is `this` matrix and `A` the rotation matrix obtained from the given angle and axis,
        then the new matrix will be `M * A`. So when transforming a
        vector `v` with the new matrix by using `M * A * v`,
        the axis-angle rotation will be applied first!
        
        In order to set the matrix to a rotation transformation without post-multiplying,
        use .rotation(double, Vector3fc).
        
        Reference: <a href="http://en.wikipedia.org/wiki/Rotation_matrix#Axis_and_angle">http://en.wikipedia.org</a>

        Arguments
        - angle: the angle in radians
        - axis: the rotation axis (needs to be Vector3f.normalize() normalized)
        - dest: will hold the result

        Returns
        - dest

        See
        - .rotation(double, Vector3fc)
        """
        ...


    def getRow(self, row: int, dest: "Vector4d") -> "Vector4d":
        ...


    def setRow(self, row: int, src: "Vector4dc") -> "Matrix4x3d":
        """
        Set the row at the given `row` index, starting with `0`.

        Arguments
        - row: the row index in `[0..2]`
        - src: the row components to set

        Returns
        - this

        Raises
        - IndexOutOfBoundsException: if `row` is not in `[0..2]`
        """
        ...


    def getColumn(self, column: int, dest: "Vector3d") -> "Vector3d":
        ...


    def setColumn(self, column: int, src: "Vector3dc") -> "Matrix4x3d":
        """
        Set the column at the given `column` index, starting with `0`.

        Arguments
        - column: the column index in `[0..3]`
        - src: the column components to set

        Returns
        - this

        Raises
        - IndexOutOfBoundsException: if `column` is not in `[0..3]`
        """
        ...


    def normal(self) -> "Matrix4x3d":
        """
        Compute a normal matrix from the left 3x3 submatrix of `this`
        and store it into the left 3x3 submatrix of `this`.
        All other values of `this` will be set to .identity() identity.
        
        The normal matrix of `m` is the transpose of the inverse of `m`.
        
        Please note that, if `this` is an orthogonal matrix or a matrix whose columns are orthogonal vectors, 
        then this method *need not* be invoked, since in that case `this` itself is its normal matrix.
        In that case, use .set3x3(Matrix4x3dc) to set a given Matrix4x3d to only the left 3x3 submatrix
        of this matrix.

        Returns
        - this

        See
        - .set3x3(Matrix4x3dc)
        """
        ...


    def normal(self, dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Compute a normal matrix from the left 3x3 submatrix of `this`
        and store it into the left 3x3 submatrix of `dest`.
        All other values of `dest` will be set to .identity() identity.
        
        The normal matrix of `m` is the transpose of the inverse of `m`.
        
        Please note that, if `this` is an orthogonal matrix or a matrix whose columns are orthogonal vectors, 
        then this method *need not* be invoked, since in that case `this` itself is its normal matrix.
        In that case, use .set3x3(Matrix4x3dc) to set a given Matrix4x3d to only the left 3x3 submatrix
        of a given matrix.

        Arguments
        - dest: will hold the result

        Returns
        - dest

        See
        - .set3x3(Matrix4x3dc)
        """
        ...


    def normal(self, dest: "Matrix3d") -> "Matrix3d":
        ...


    def cofactor3x3(self) -> "Matrix4x3d":
        """
        Compute the cofactor matrix of the left 3x3 submatrix of `this`.
        
        The cofactor matrix can be used instead of .normal() to transform normals
        when the orientation of the normals with respect to the surface should be preserved.

        Returns
        - this
        """
        ...


    def cofactor3x3(self, dest: "Matrix3d") -> "Matrix3d":
        """
        Compute the cofactor matrix of the left 3x3 submatrix of `this`
        and store it into `dest`.
        
        The cofactor matrix can be used instead of .normal(Matrix3d) to transform normals
        when the orientation of the normals with respect to the surface should be preserved.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def cofactor3x3(self, dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Compute the cofactor matrix of the left 3x3 submatrix of `this`
        and store it into `dest`.
        All other values of `dest` will be set to .identity() identity.
        
        The cofactor matrix can be used instead of .normal(Matrix4x3d) to transform normals
        when the orientation of the normals with respect to the surface should be preserved.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def normalize3x3(self) -> "Matrix4x3d":
        """
        Normalize the left 3x3 submatrix of this matrix.
        
        The resulting matrix will map unit vectors to unit vectors, though a pair of orthogonal input unit
        vectors need not be mapped to a pair of orthogonal output vectors if the original matrix was not orthogonal itself
        (i.e. had *skewing*).

        Returns
        - this
        """
        ...


    def normalize3x3(self, dest: "Matrix4x3d") -> "Matrix4x3d":
        ...


    def normalize3x3(self, dest: "Matrix3d") -> "Matrix3d":
        ...


    def reflect(self, a: float, b: float, c: float, d: float, dest: "Matrix4x3d") -> "Matrix4x3d":
        ...


    def reflect(self, a: float, b: float, c: float, d: float) -> "Matrix4x3d":
        """
        Apply a mirror/reflection transformation to this matrix that reflects about the given plane
        specified via the equation `x*a + y*b + z*c + d = 0`.
        
        The vector `(a, b, c)` must be a unit vector.
        
        If `M` is `this` matrix and `R` the reflection matrix,
        then the new matrix will be `M * R`. So when transforming a
        vector `v` with the new matrix by using `M * R * v`, the
        reflection will be applied first!
        
        Reference: <a href="https://msdn.microsoft.com/en-us/library/windows/desktop/bb281733(v=vs.85).aspx">msdn.microsoft.com</a>

        Arguments
        - a: the x factor in the plane equation
        - b: the y factor in the plane equation
        - c: the z factor in the plane equation
        - d: the constant in the plane equation

        Returns
        - this
        """
        ...


    def reflect(self, nx: float, ny: float, nz: float, px: float, py: float, pz: float) -> "Matrix4x3d":
        """
        Apply a mirror/reflection transformation to this matrix that reflects about the given plane
        specified via the plane normal and a point on the plane.
        
        If `M` is `this` matrix and `R` the reflection matrix,
        then the new matrix will be `M * R`. So when transforming a
        vector `v` with the new matrix by using `M * R * v`, the
        reflection will be applied first!

        Arguments
        - nx: the x-coordinate of the plane normal
        - ny: the y-coordinate of the plane normal
        - nz: the z-coordinate of the plane normal
        - px: the x-coordinate of a point on the plane
        - py: the y-coordinate of a point on the plane
        - pz: the z-coordinate of a point on the plane

        Returns
        - this
        """
        ...


    def reflect(self, nx: float, ny: float, nz: float, px: float, py: float, pz: float, dest: "Matrix4x3d") -> "Matrix4x3d":
        ...


    def reflect(self, normal: "Vector3dc", point: "Vector3dc") -> "Matrix4x3d":
        """
        Apply a mirror/reflection transformation to this matrix that reflects about the given plane
        specified via the plane normal and a point on the plane.
        
        If `M` is `this` matrix and `R` the reflection matrix,
        then the new matrix will be `M * R`. So when transforming a
        vector `v` with the new matrix by using `M * R * v`, the
        reflection will be applied first!

        Arguments
        - normal: the plane normal
        - point: a point on the plane

        Returns
        - this
        """
        ...


    def reflect(self, orientation: "Quaterniondc", point: "Vector3dc") -> "Matrix4x3d":
        """
        Apply a mirror/reflection transformation to this matrix that reflects about a plane
        specified via the plane orientation and a point on the plane.
        
        This method can be used to build a reflection transformation based on the orientation of a mirror object in the scene.
        It is assumed that the default mirror plane's normal is `(0, 0, 1)`. So, if the given Quaterniondc is
        the identity (does not apply any additional rotation), the reflection plane will be `z=0`, offset by the given `point`.
        
        If `M` is `this` matrix and `R` the reflection matrix,
        then the new matrix will be `M * R`. So when transforming a
        vector `v` with the new matrix by using `M * R * v`, the
        reflection will be applied first!

        Arguments
        - orientation: the plane orientation relative to an implied normal vector of `(0, 0, 1)`
        - point: a point on the plane

        Returns
        - this
        """
        ...


    def reflect(self, orientation: "Quaterniondc", point: "Vector3dc", dest: "Matrix4x3d") -> "Matrix4x3d":
        ...


    def reflect(self, normal: "Vector3dc", point: "Vector3dc", dest: "Matrix4x3d") -> "Matrix4x3d":
        ...


    def reflection(self, a: float, b: float, c: float, d: float) -> "Matrix4x3d":
        """
        Set this matrix to a mirror/reflection transformation that reflects about the given plane
        specified via the equation `x*a + y*b + z*c + d = 0`.
        
        The vector `(a, b, c)` must be a unit vector.
        
        Reference: <a href="https://msdn.microsoft.com/en-us/library/windows/desktop/bb281733(v=vs.85).aspx">msdn.microsoft.com</a>

        Arguments
        - a: the x factor in the plane equation
        - b: the y factor in the plane equation
        - c: the z factor in the plane equation
        - d: the constant in the plane equation

        Returns
        - this
        """
        ...


    def reflection(self, nx: float, ny: float, nz: float, px: float, py: float, pz: float) -> "Matrix4x3d":
        """
        Set this matrix to a mirror/reflection transformation that reflects about the given plane
        specified via the plane normal and a point on the plane.

        Arguments
        - nx: the x-coordinate of the plane normal
        - ny: the y-coordinate of the plane normal
        - nz: the z-coordinate of the plane normal
        - px: the x-coordinate of a point on the plane
        - py: the y-coordinate of a point on the plane
        - pz: the z-coordinate of a point on the plane

        Returns
        - this
        """
        ...


    def reflection(self, normal: "Vector3dc", point: "Vector3dc") -> "Matrix4x3d":
        """
        Set this matrix to a mirror/reflection transformation that reflects about the given plane
        specified via the plane normal and a point on the plane.

        Arguments
        - normal: the plane normal
        - point: a point on the plane

        Returns
        - this
        """
        ...


    def reflection(self, orientation: "Quaterniondc", point: "Vector3dc") -> "Matrix4x3d":
        """
        Set this matrix to a mirror/reflection transformation that reflects about a plane
        specified via the plane orientation and a point on the plane.
        
        This method can be used to build a reflection transformation based on the orientation of a mirror object in the scene.
        It is assumed that the default mirror plane's normal is `(0, 0, 1)`. So, if the given Quaterniondc is
        the identity (does not apply any additional rotation), the reflection plane will be `z=0`, offset by the given `point`.

        Arguments
        - orientation: the plane orientation
        - point: a point on the plane

        Returns
        - this
        """
        ...


    def ortho(self, left: float, right: float, bottom: float, top: float, zNear: float, zFar: float, zZeroToOne: bool, dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Apply an orthographic projection transformation for a right-handed coordinate system
        using the given NDC z range to this matrix and store the result in `dest`.
        
        If `M` is `this` matrix and `O` the orthographic projection matrix,
        then the new matrix will be `M * O`. So when transforming a
        vector `v` with the new matrix by using `M * O * v`, the
        orthographic projection transformation will be applied first!
        
        In order to set the matrix to an orthographic projection without post-multiplying it,
        use .setOrtho(double, double, double, double, double, double, boolean) setOrtho().
        
        Reference: <a href="http://www.songho.ca/opengl/gl_projectionmatrix.html#ortho">http://www.songho.ca</a>

        Arguments
        - left: the distance from the center to the left frustum edge
        - right: the distance from the center to the right frustum edge
        - bottom: the distance from the center to the bottom frustum edge
        - top: the distance from the center to the top frustum edge
        - zNear: near clipping plane distance
        - zFar: far clipping plane distance
        - zZeroToOne: whether to use Vulkan's and Direct3D's NDC z range of `[0..+1]` when `True`
                   or whether to use OpenGL's NDC z range of `[-1..+1]` when `False`
        - dest: will hold the result

        Returns
        - dest

        See
        - .setOrtho(double, double, double, double, double, double, boolean)
        """
        ...


    def ortho(self, left: float, right: float, bottom: float, top: float, zNear: float, zFar: float, dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Apply an orthographic projection transformation for a right-handed coordinate system
        using OpenGL's NDC z range of `[-1..+1]` to this matrix and store the result in `dest`.
        
        If `M` is `this` matrix and `O` the orthographic projection matrix,
        then the new matrix will be `M * O`. So when transforming a
        vector `v` with the new matrix by using `M * O * v`, the
        orthographic projection transformation will be applied first!
        
        In order to set the matrix to an orthographic projection without post-multiplying it,
        use .setOrtho(double, double, double, double, double, double) setOrtho().
        
        Reference: <a href="http://www.songho.ca/opengl/gl_projectionmatrix.html#ortho">http://www.songho.ca</a>

        Arguments
        - left: the distance from the center to the left frustum edge
        - right: the distance from the center to the right frustum edge
        - bottom: the distance from the center to the bottom frustum edge
        - top: the distance from the center to the top frustum edge
        - zNear: near clipping plane distance
        - zFar: far clipping plane distance
        - dest: will hold the result

        Returns
        - dest

        See
        - .setOrtho(double, double, double, double, double, double)
        """
        ...


    def ortho(self, left: float, right: float, bottom: float, top: float, zNear: float, zFar: float, zZeroToOne: bool) -> "Matrix4x3d":
        """
        Apply an orthographic projection transformation for a right-handed coordinate system
        using the given NDC z range to this matrix.
        
        If `M` is `this` matrix and `O` the orthographic projection matrix,
        then the new matrix will be `M * O`. So when transforming a
        vector `v` with the new matrix by using `M * O * v`, the
        orthographic projection transformation will be applied first!
        
        In order to set the matrix to an orthographic projection without post-multiplying it,
        use .setOrtho(double, double, double, double, double, double, boolean) setOrtho().
        
        Reference: <a href="http://www.songho.ca/opengl/gl_projectionmatrix.html#ortho">http://www.songho.ca</a>

        Arguments
        - left: the distance from the center to the left frustum edge
        - right: the distance from the center to the right frustum edge
        - bottom: the distance from the center to the bottom frustum edge
        - top: the distance from the center to the top frustum edge
        - zNear: near clipping plane distance
        - zFar: far clipping plane distance
        - zZeroToOne: whether to use Vulkan's and Direct3D's NDC z range of `[0..+1]` when `True`
                   or whether to use OpenGL's NDC z range of `[-1..+1]` when `False`

        Returns
        - this

        See
        - .setOrtho(double, double, double, double, double, double, boolean)
        """
        ...


    def ortho(self, left: float, right: float, bottom: float, top: float, zNear: float, zFar: float) -> "Matrix4x3d":
        """
        Apply an orthographic projection transformation for a right-handed coordinate system
        using OpenGL's NDC z range of `[-1..+1]` to this matrix.
        
        If `M` is `this` matrix and `O` the orthographic projection matrix,
        then the new matrix will be `M * O`. So when transforming a
        vector `v` with the new matrix by using `M * O * v`, the
        orthographic projection transformation will be applied first!
        
        In order to set the matrix to an orthographic projection without post-multiplying it,
        use .setOrtho(double, double, double, double, double, double) setOrtho().
        
        Reference: <a href="http://www.songho.ca/opengl/gl_projectionmatrix.html#ortho">http://www.songho.ca</a>

        Arguments
        - left: the distance from the center to the left frustum edge
        - right: the distance from the center to the right frustum edge
        - bottom: the distance from the center to the bottom frustum edge
        - top: the distance from the center to the top frustum edge
        - zNear: near clipping plane distance
        - zFar: far clipping plane distance

        Returns
        - this

        See
        - .setOrtho(double, double, double, double, double, double)
        """
        ...


    def orthoLH(self, left: float, right: float, bottom: float, top: float, zNear: float, zFar: float, zZeroToOne: bool, dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Apply an orthographic projection transformation for a left-handed coordiante system
        using the given NDC z range to this matrix and store the result in `dest`.
        
        If `M` is `this` matrix and `O` the orthographic projection matrix,
        then the new matrix will be `M * O`. So when transforming a
        vector `v` with the new matrix by using `M * O * v`, the
        orthographic projection transformation will be applied first!
        
        In order to set the matrix to an orthographic projection without post-multiplying it,
        use .setOrthoLH(double, double, double, double, double, double, boolean) setOrthoLH().
        
        Reference: <a href="http://www.songho.ca/opengl/gl_projectionmatrix.html#ortho">http://www.songho.ca</a>

        Arguments
        - left: the distance from the center to the left frustum edge
        - right: the distance from the center to the right frustum edge
        - bottom: the distance from the center to the bottom frustum edge
        - top: the distance from the center to the top frustum edge
        - zNear: near clipping plane distance
        - zFar: far clipping plane distance
        - zZeroToOne: whether to use Vulkan's and Direct3D's NDC z range of `[0..+1]` when `True`
                   or whether to use OpenGL's NDC z range of `[-1..+1]` when `False`
        - dest: will hold the result

        Returns
        - dest

        See
        - .setOrthoLH(double, double, double, double, double, double, boolean)
        """
        ...


    def orthoLH(self, left: float, right: float, bottom: float, top: float, zNear: float, zFar: float, dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Apply an orthographic projection transformation for a left-handed coordiante system
        using OpenGL's NDC z range of `[-1..+1]` to this matrix and store the result in `dest`.
        
        If `M` is `this` matrix and `O` the orthographic projection matrix,
        then the new matrix will be `M * O`. So when transforming a
        vector `v` with the new matrix by using `M * O * v`, the
        orthographic projection transformation will be applied first!
        
        In order to set the matrix to an orthographic projection without post-multiplying it,
        use .setOrthoLH(double, double, double, double, double, double) setOrthoLH().
        
        Reference: <a href="http://www.songho.ca/opengl/gl_projectionmatrix.html#ortho">http://www.songho.ca</a>

        Arguments
        - left: the distance from the center to the left frustum edge
        - right: the distance from the center to the right frustum edge
        - bottom: the distance from the center to the bottom frustum edge
        - top: the distance from the center to the top frustum edge
        - zNear: near clipping plane distance
        - zFar: far clipping plane distance
        - dest: will hold the result

        Returns
        - dest

        See
        - .setOrthoLH(double, double, double, double, double, double)
        """
        ...


    def orthoLH(self, left: float, right: float, bottom: float, top: float, zNear: float, zFar: float, zZeroToOne: bool) -> "Matrix4x3d":
        """
        Apply an orthographic projection transformation for a left-handed coordiante system
        using the given NDC z range to this matrix.
        
        If `M` is `this` matrix and `O` the orthographic projection matrix,
        then the new matrix will be `M * O`. So when transforming a
        vector `v` with the new matrix by using `M * O * v`, the
        orthographic projection transformation will be applied first!
        
        In order to set the matrix to an orthographic projection without post-multiplying it,
        use .setOrthoLH(double, double, double, double, double, double, boolean) setOrthoLH().
        
        Reference: <a href="http://www.songho.ca/opengl/gl_projectionmatrix.html#ortho">http://www.songho.ca</a>

        Arguments
        - left: the distance from the center to the left frustum edge
        - right: the distance from the center to the right frustum edge
        - bottom: the distance from the center to the bottom frustum edge
        - top: the distance from the center to the top frustum edge
        - zNear: near clipping plane distance
        - zFar: far clipping plane distance
        - zZeroToOne: whether to use Vulkan's and Direct3D's NDC z range of `[0..+1]` when `True`
                   or whether to use OpenGL's NDC z range of `[-1..+1]` when `False`

        Returns
        - this

        See
        - .setOrthoLH(double, double, double, double, double, double, boolean)
        """
        ...


    def orthoLH(self, left: float, right: float, bottom: float, top: float, zNear: float, zFar: float) -> "Matrix4x3d":
        """
        Apply an orthographic projection transformation for a left-handed coordiante system
        using OpenGL's NDC z range of `[-1..+1]` to this matrix.
        
        If `M` is `this` matrix and `O` the orthographic projection matrix,
        then the new matrix will be `M * O`. So when transforming a
        vector `v` with the new matrix by using `M * O * v`, the
        orthographic projection transformation will be applied first!
        
        In order to set the matrix to an orthographic projection without post-multiplying it,
        use .setOrthoLH(double, double, double, double, double, double) setOrthoLH().
        
        Reference: <a href="http://www.songho.ca/opengl/gl_projectionmatrix.html#ortho">http://www.songho.ca</a>

        Arguments
        - left: the distance from the center to the left frustum edge
        - right: the distance from the center to the right frustum edge
        - bottom: the distance from the center to the bottom frustum edge
        - top: the distance from the center to the top frustum edge
        - zNear: near clipping plane distance
        - zFar: far clipping plane distance

        Returns
        - this

        See
        - .setOrthoLH(double, double, double, double, double, double)
        """
        ...


    def setOrtho(self, left: float, right: float, bottom: float, top: float, zNear: float, zFar: float, zZeroToOne: bool) -> "Matrix4x3d":
        """
        Set this matrix to be an orthographic projection transformation for a right-handed coordinate system
        using the given NDC z range.
        
        In order to apply the orthographic projection to an already existing transformation,
        use .ortho(double, double, double, double, double, double, boolean) ortho().
        
        Reference: <a href="http://www.songho.ca/opengl/gl_projectionmatrix.html#ortho">http://www.songho.ca</a>

        Arguments
        - left: the distance from the center to the left frustum edge
        - right: the distance from the center to the right frustum edge
        - bottom: the distance from the center to the bottom frustum edge
        - top: the distance from the center to the top frustum edge
        - zNear: near clipping plane distance
        - zFar: far clipping plane distance
        - zZeroToOne: whether to use Vulkan's and Direct3D's NDC z range of `[0..+1]` when `True`
                   or whether to use OpenGL's NDC z range of `[-1..+1]` when `False`

        Returns
        - this

        See
        - .ortho(double, double, double, double, double, double, boolean)
        """
        ...


    def setOrtho(self, left: float, right: float, bottom: float, top: float, zNear: float, zFar: float) -> "Matrix4x3d":
        """
        Set this matrix to be an orthographic projection transformation for a right-handed coordinate system
        using OpenGL's NDC z range of `[-1..+1]`.
        
        In order to apply the orthographic projection to an already existing transformation,
        use .ortho(double, double, double, double, double, double) ortho().
        
        Reference: <a href="http://www.songho.ca/opengl/gl_projectionmatrix.html#ortho">http://www.songho.ca</a>

        Arguments
        - left: the distance from the center to the left frustum edge
        - right: the distance from the center to the right frustum edge
        - bottom: the distance from the center to the bottom frustum edge
        - top: the distance from the center to the top frustum edge
        - zNear: near clipping plane distance
        - zFar: far clipping plane distance

        Returns
        - this

        See
        - .ortho(double, double, double, double, double, double)
        """
        ...


    def setOrthoLH(self, left: float, right: float, bottom: float, top: float, zNear: float, zFar: float, zZeroToOne: bool) -> "Matrix4x3d":
        """
        Set this matrix to be an orthographic projection transformation for a left-handed coordinate system
        using the given NDC z range.
        
        In order to apply the orthographic projection to an already existing transformation,
        use .orthoLH(double, double, double, double, double, double, boolean) orthoLH().
        
        Reference: <a href="http://www.songho.ca/opengl/gl_projectionmatrix.html#ortho">http://www.songho.ca</a>

        Arguments
        - left: the distance from the center to the left frustum edge
        - right: the distance from the center to the right frustum edge
        - bottom: the distance from the center to the bottom frustum edge
        - top: the distance from the center to the top frustum edge
        - zNear: near clipping plane distance
        - zFar: far clipping plane distance
        - zZeroToOne: whether to use Vulkan's and Direct3D's NDC z range of `[0..+1]` when `True`
                   or whether to use OpenGL's NDC z range of `[-1..+1]` when `False`

        Returns
        - this

        See
        - .orthoLH(double, double, double, double, double, double, boolean)
        """
        ...


    def setOrthoLH(self, left: float, right: float, bottom: float, top: float, zNear: float, zFar: float) -> "Matrix4x3d":
        """
        Set this matrix to be an orthographic projection transformation for a left-handed coordinate system
        using OpenGL's NDC z range of `[-1..+1]`.
        
        In order to apply the orthographic projection to an already existing transformation,
        use .orthoLH(double, double, double, double, double, double) orthoLH().
        
        Reference: <a href="http://www.songho.ca/opengl/gl_projectionmatrix.html#ortho">http://www.songho.ca</a>

        Arguments
        - left: the distance from the center to the left frustum edge
        - right: the distance from the center to the right frustum edge
        - bottom: the distance from the center to the bottom frustum edge
        - top: the distance from the center to the top frustum edge
        - zNear: near clipping plane distance
        - zFar: far clipping plane distance

        Returns
        - this

        See
        - .orthoLH(double, double, double, double, double, double)
        """
        ...


    def orthoSymmetric(self, width: float, height: float, zNear: float, zFar: float, zZeroToOne: bool, dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Apply a symmetric orthographic projection transformation for a right-handed coordinate system
        using the given NDC z range to this matrix and store the result in `dest`.
        
        This method is equivalent to calling .ortho(double, double, double, double, double, double, boolean, Matrix4x3d) ortho() with
        `left=-width/2`, `right=+width/2`, `bottom=-height/2` and `top=+height/2`.
        
        If `M` is `this` matrix and `O` the orthographic projection matrix,
        then the new matrix will be `M * O`. So when transforming a
        vector `v` with the new matrix by using `M * O * v`, the
        orthographic projection transformation will be applied first!
        
        In order to set the matrix to a symmetric orthographic projection without post-multiplying it,
        use .setOrthoSymmetric(double, double, double, double, boolean) setOrthoSymmetric().
        
        Reference: <a href="http://www.songho.ca/opengl/gl_projectionmatrix.html#ortho">http://www.songho.ca</a>

        Arguments
        - width: the distance between the right and left frustum edges
        - height: the distance between the top and bottom frustum edges
        - zNear: near clipping plane distance
        - zFar: far clipping plane distance
        - dest: will hold the result
        - zZeroToOne: whether to use Vulkan's and Direct3D's NDC z range of `[0..+1]` when `True`
                   or whether to use OpenGL's NDC z range of `[-1..+1]` when `False`

        Returns
        - dest

        See
        - .setOrthoSymmetric(double, double, double, double, boolean)
        """
        ...


    def orthoSymmetric(self, width: float, height: float, zNear: float, zFar: float, dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Apply a symmetric orthographic projection transformation for a right-handed coordinate system
        using OpenGL's NDC z range of `[-1..+1]` to this matrix and store the result in `dest`.
        
        This method is equivalent to calling .ortho(double, double, double, double, double, double, Matrix4x3d) ortho() with
        `left=-width/2`, `right=+width/2`, `bottom=-height/2` and `top=+height/2`.
        
        If `M` is `this` matrix and `O` the orthographic projection matrix,
        then the new matrix will be `M * O`. So when transforming a
        vector `v` with the new matrix by using `M * O * v`, the
        orthographic projection transformation will be applied first!
        
        In order to set the matrix to a symmetric orthographic projection without post-multiplying it,
        use .setOrthoSymmetric(double, double, double, double) setOrthoSymmetric().
        
        Reference: <a href="http://www.songho.ca/opengl/gl_projectionmatrix.html#ortho">http://www.songho.ca</a>

        Arguments
        - width: the distance between the right and left frustum edges
        - height: the distance between the top and bottom frustum edges
        - zNear: near clipping plane distance
        - zFar: far clipping plane distance
        - dest: will hold the result

        Returns
        - dest

        See
        - .setOrthoSymmetric(double, double, double, double)
        """
        ...


    def orthoSymmetric(self, width: float, height: float, zNear: float, zFar: float, zZeroToOne: bool) -> "Matrix4x3d":
        """
        Apply a symmetric orthographic projection transformation for a right-handed coordinate system
        using the given NDC z range to this matrix.
        
        This method is equivalent to calling .ortho(double, double, double, double, double, double, boolean) ortho() with
        `left=-width/2`, `right=+width/2`, `bottom=-height/2` and `top=+height/2`.
        
        If `M` is `this` matrix and `O` the orthographic projection matrix,
        then the new matrix will be `M * O`. So when transforming a
        vector `v` with the new matrix by using `M * O * v`, the
        orthographic projection transformation will be applied first!
        
        In order to set the matrix to a symmetric orthographic projection without post-multiplying it,
        use .setOrthoSymmetric(double, double, double, double, boolean) setOrthoSymmetric().
        
        Reference: <a href="http://www.songho.ca/opengl/gl_projectionmatrix.html#ortho">http://www.songho.ca</a>

        Arguments
        - width: the distance between the right and left frustum edges
        - height: the distance between the top and bottom frustum edges
        - zNear: near clipping plane distance
        - zFar: far clipping plane distance
        - zZeroToOne: whether to use Vulkan's and Direct3D's NDC z range of `[0..+1]` when `True`
                   or whether to use OpenGL's NDC z range of `[-1..+1]` when `False`

        Returns
        - this

        See
        - .setOrthoSymmetric(double, double, double, double, boolean)
        """
        ...


    def orthoSymmetric(self, width: float, height: float, zNear: float, zFar: float) -> "Matrix4x3d":
        """
        Apply a symmetric orthographic projection transformation for a right-handed coordinate system
        using OpenGL's NDC z range of `[-1..+1]` to this matrix.
        
        This method is equivalent to calling .ortho(double, double, double, double, double, double) ortho() with
        `left=-width/2`, `right=+width/2`, `bottom=-height/2` and `top=+height/2`.
        
        If `M` is `this` matrix and `O` the orthographic projection matrix,
        then the new matrix will be `M * O`. So when transforming a
        vector `v` with the new matrix by using `M * O * v`, the
        orthographic projection transformation will be applied first!
        
        In order to set the matrix to a symmetric orthographic projection without post-multiplying it,
        use .setOrthoSymmetric(double, double, double, double) setOrthoSymmetric().
        
        Reference: <a href="http://www.songho.ca/opengl/gl_projectionmatrix.html#ortho">http://www.songho.ca</a>

        Arguments
        - width: the distance between the right and left frustum edges
        - height: the distance between the top and bottom frustum edges
        - zNear: near clipping plane distance
        - zFar: far clipping plane distance

        Returns
        - this

        See
        - .setOrthoSymmetric(double, double, double, double)
        """
        ...


    def orthoSymmetricLH(self, width: float, height: float, zNear: float, zFar: float, zZeroToOne: bool, dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Apply a symmetric orthographic projection transformation for a left-handed coordinate system
        using the given NDC z range to this matrix and store the result in `dest`.
        
        This method is equivalent to calling .orthoLH(double, double, double, double, double, double, boolean, Matrix4x3d) orthoLH() with
        `left=-width/2`, `right=+width/2`, `bottom=-height/2` and `top=+height/2`.
        
        If `M` is `this` matrix and `O` the orthographic projection matrix,
        then the new matrix will be `M * O`. So when transforming a
        vector `v` with the new matrix by using `M * O * v`, the
        orthographic projection transformation will be applied first!
        
        In order to set the matrix to a symmetric orthographic projection without post-multiplying it,
        use .setOrthoSymmetricLH(double, double, double, double, boolean) setOrthoSymmetricLH().
        
        Reference: <a href="http://www.songho.ca/opengl/gl_projectionmatrix.html#ortho">http://www.songho.ca</a>

        Arguments
        - width: the distance between the right and left frustum edges
        - height: the distance between the top and bottom frustum edges
        - zNear: near clipping plane distance
        - zFar: far clipping plane distance
        - dest: will hold the result
        - zZeroToOne: whether to use Vulkan's and Direct3D's NDC z range of `[0..+1]` when `True`
                   or whether to use OpenGL's NDC z range of `[-1..+1]` when `False`

        Returns
        - dest

        See
        - .setOrthoSymmetricLH(double, double, double, double, boolean)
        """
        ...


    def orthoSymmetricLH(self, width: float, height: float, zNear: float, zFar: float, dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Apply a symmetric orthographic projection transformation for a left-handed coordinate system
        using OpenGL's NDC z range of `[-1..+1]` to this matrix and store the result in `dest`.
        
        This method is equivalent to calling .orthoLH(double, double, double, double, double, double, Matrix4x3d) orthoLH() with
        `left=-width/2`, `right=+width/2`, `bottom=-height/2` and `top=+height/2`.
        
        If `M` is `this` matrix and `O` the orthographic projection matrix,
        then the new matrix will be `M * O`. So when transforming a
        vector `v` with the new matrix by using `M * O * v`, the
        orthographic projection transformation will be applied first!
        
        In order to set the matrix to a symmetric orthographic projection without post-multiplying it,
        use .setOrthoSymmetricLH(double, double, double, double) setOrthoSymmetricLH().
        
        Reference: <a href="http://www.songho.ca/opengl/gl_projectionmatrix.html#ortho">http://www.songho.ca</a>

        Arguments
        - width: the distance between the right and left frustum edges
        - height: the distance between the top and bottom frustum edges
        - zNear: near clipping plane distance
        - zFar: far clipping plane distance
        - dest: will hold the result

        Returns
        - dest

        See
        - .setOrthoSymmetricLH(double, double, double, double)
        """
        ...


    def orthoSymmetricLH(self, width: float, height: float, zNear: float, zFar: float, zZeroToOne: bool) -> "Matrix4x3d":
        """
        Apply a symmetric orthographic projection transformation for a left-handed coordinate system
        using the given NDC z range to this matrix.
        
        This method is equivalent to calling .orthoLH(double, double, double, double, double, double, boolean) orthoLH() with
        `left=-width/2`, `right=+width/2`, `bottom=-height/2` and `top=+height/2`.
        
        If `M` is `this` matrix and `O` the orthographic projection matrix,
        then the new matrix will be `M * O`. So when transforming a
        vector `v` with the new matrix by using `M * O * v`, the
        orthographic projection transformation will be applied first!
        
        In order to set the matrix to a symmetric orthographic projection without post-multiplying it,
        use .setOrthoSymmetricLH(double, double, double, double, boolean) setOrthoSymmetricLH().
        
        Reference: <a href="http://www.songho.ca/opengl/gl_projectionmatrix.html#ortho">http://www.songho.ca</a>

        Arguments
        - width: the distance between the right and left frustum edges
        - height: the distance between the top and bottom frustum edges
        - zNear: near clipping plane distance
        - zFar: far clipping plane distance
        - zZeroToOne: whether to use Vulkan's and Direct3D's NDC z range of `[0..+1]` when `True`
                   or whether to use OpenGL's NDC z range of `[-1..+1]` when `False`

        Returns
        - this

        See
        - .setOrthoSymmetricLH(double, double, double, double, boolean)
        """
        ...


    def orthoSymmetricLH(self, width: float, height: float, zNear: float, zFar: float) -> "Matrix4x3d":
        """
        Apply a symmetric orthographic projection transformation for a left-handed coordinate system
        using OpenGL's NDC z range of `[-1..+1]` to this matrix.
        
        This method is equivalent to calling .orthoLH(double, double, double, double, double, double) orthoLH() with
        `left=-width/2`, `right=+width/2`, `bottom=-height/2` and `top=+height/2`.
        
        If `M` is `this` matrix and `O` the orthographic projection matrix,
        then the new matrix will be `M * O`. So when transforming a
        vector `v` with the new matrix by using `M * O * v`, the
        orthographic projection transformation will be applied first!
        
        In order to set the matrix to a symmetric orthographic projection without post-multiplying it,
        use .setOrthoSymmetricLH(double, double, double, double) setOrthoSymmetricLH().
        
        Reference: <a href="http://www.songho.ca/opengl/gl_projectionmatrix.html#ortho">http://www.songho.ca</a>

        Arguments
        - width: the distance between the right and left frustum edges
        - height: the distance between the top and bottom frustum edges
        - zNear: near clipping plane distance
        - zFar: far clipping plane distance

        Returns
        - this

        See
        - .setOrthoSymmetricLH(double, double, double, double)
        """
        ...


    def setOrthoSymmetric(self, width: float, height: float, zNear: float, zFar: float, zZeroToOne: bool) -> "Matrix4x3d":
        """
        Set this matrix to be a symmetric orthographic projection transformation for a right-handed coordinate system
        using the given NDC z range.
        
        This method is equivalent to calling .setOrtho(double, double, double, double, double, double, boolean) setOrtho() with
        `left=-width/2`, `right=+width/2`, `bottom=-height/2` and `top=+height/2`.
        
        In order to apply the symmetric orthographic projection to an already existing transformation,
        use .orthoSymmetric(double, double, double, double, boolean) orthoSymmetric().
        
        Reference: <a href="http://www.songho.ca/opengl/gl_projectionmatrix.html#ortho">http://www.songho.ca</a>

        Arguments
        - width: the distance between the right and left frustum edges
        - height: the distance between the top and bottom frustum edges
        - zNear: near clipping plane distance
        - zFar: far clipping plane distance
        - zZeroToOne: whether to use Vulkan's and Direct3D's NDC z range of `[0..+1]` when `True`
                   or whether to use OpenGL's NDC z range of `[-1..+1]` when `False`

        Returns
        - this

        See
        - .orthoSymmetric(double, double, double, double, boolean)
        """
        ...


    def setOrthoSymmetric(self, width: float, height: float, zNear: float, zFar: float) -> "Matrix4x3d":
        """
        Set this matrix to be a symmetric orthographic projection transformation for a right-handed coordinate system
        using OpenGL's NDC z range of `[-1..+1]`.
        
        This method is equivalent to calling .setOrtho(double, double, double, double, double, double) setOrtho() with
        `left=-width/2`, `right=+width/2`, `bottom=-height/2` and `top=+height/2`.
        
        In order to apply the symmetric orthographic projection to an already existing transformation,
        use .orthoSymmetric(double, double, double, double) orthoSymmetric().
        
        Reference: <a href="http://www.songho.ca/opengl/gl_projectionmatrix.html#ortho">http://www.songho.ca</a>

        Arguments
        - width: the distance between the right and left frustum edges
        - height: the distance between the top and bottom frustum edges
        - zNear: near clipping plane distance
        - zFar: far clipping plane distance

        Returns
        - this

        See
        - .orthoSymmetric(double, double, double, double)
        """
        ...


    def setOrthoSymmetricLH(self, width: float, height: float, zNear: float, zFar: float, zZeroToOne: bool) -> "Matrix4x3d":
        """
        Set this matrix to be a symmetric orthographic projection transformation for a left-handed coordinate system using the given NDC z range.
        
        This method is equivalent to calling .setOrtho(double, double, double, double, double, double, boolean) setOrtho() with
        `left=-width/2`, `right=+width/2`, `bottom=-height/2` and `top=+height/2`.
        
        In order to apply the symmetric orthographic projection to an already existing transformation,
        use .orthoSymmetricLH(double, double, double, double, boolean) orthoSymmetricLH().
        
        Reference: <a href="http://www.songho.ca/opengl/gl_projectionmatrix.html#ortho">http://www.songho.ca</a>

        Arguments
        - width: the distance between the right and left frustum edges
        - height: the distance between the top and bottom frustum edges
        - zNear: near clipping plane distance
        - zFar: far clipping plane distance
        - zZeroToOne: whether to use Vulkan's and Direct3D's NDC z range of `[0..+1]` when `True`
                   or whether to use OpenGL's NDC z range of `[-1..+1]` when `False`

        Returns
        - this

        See
        - .orthoSymmetricLH(double, double, double, double, boolean)
        """
        ...


    def setOrthoSymmetricLH(self, width: float, height: float, zNear: float, zFar: float) -> "Matrix4x3d":
        """
        Set this matrix to be a symmetric orthographic projection transformation for a left-handed coordinate system
        using OpenGL's NDC z range of `[-1..+1]`.
        
        This method is equivalent to calling .setOrthoLH(double, double, double, double, double, double) setOrthoLH() with
        `left=-width/2`, `right=+width/2`, `bottom=-height/2` and `top=+height/2`.
        
        In order to apply the symmetric orthographic projection to an already existing transformation,
        use .orthoSymmetricLH(double, double, double, double) orthoSymmetricLH().
        
        Reference: <a href="http://www.songho.ca/opengl/gl_projectionmatrix.html#ortho">http://www.songho.ca</a>

        Arguments
        - width: the distance between the right and left frustum edges
        - height: the distance between the top and bottom frustum edges
        - zNear: near clipping plane distance
        - zFar: far clipping plane distance

        Returns
        - this

        See
        - .orthoSymmetricLH(double, double, double, double)
        """
        ...


    def ortho2D(self, left: float, right: float, bottom: float, top: float, dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Apply an orthographic projection transformation for a right-handed coordinate system
        to this matrix and store the result in `dest`.
        
        This method is equivalent to calling .ortho(double, double, double, double, double, double, Matrix4x3d) ortho() with
        `zNear=-1` and `zFar=+1`.
        
        If `M` is `this` matrix and `O` the orthographic projection matrix,
        then the new matrix will be `M * O`. So when transforming a
        vector `v` with the new matrix by using `M * O * v`, the
        orthographic projection transformation will be applied first!
        
        In order to set the matrix to an orthographic projection without post-multiplying it,
        use .setOrtho2D(double, double, double, double) setOrtho().
        
        Reference: <a href="http://www.songho.ca/opengl/gl_projectionmatrix.html#ortho">http://www.songho.ca</a>

        Arguments
        - left: the distance from the center to the left frustum edge
        - right: the distance from the center to the right frustum edge
        - bottom: the distance from the center to the bottom frustum edge
        - top: the distance from the center to the top frustum edge
        - dest: will hold the result

        Returns
        - dest

        See
        - .setOrtho2D(double, double, double, double)
        """
        ...


    def ortho2D(self, left: float, right: float, bottom: float, top: float) -> "Matrix4x3d":
        """
        Apply an orthographic projection transformation for a right-handed coordinate system to this matrix.
        
        This method is equivalent to calling .ortho(double, double, double, double, double, double) ortho() with
        `zNear=-1` and `zFar=+1`.
        
        If `M` is `this` matrix and `O` the orthographic projection matrix,
        then the new matrix will be `M * O`. So when transforming a
        vector `v` with the new matrix by using `M * O * v`, the
        orthographic projection transformation will be applied first!
        
        In order to set the matrix to an orthographic projection without post-multiplying it,
        use .setOrtho2D(double, double, double, double) setOrtho2D().
        
        Reference: <a href="http://www.songho.ca/opengl/gl_projectionmatrix.html#ortho">http://www.songho.ca</a>

        Arguments
        - left: the distance from the center to the left frustum edge
        - right: the distance from the center to the right frustum edge
        - bottom: the distance from the center to the bottom frustum edge
        - top: the distance from the center to the top frustum edge

        Returns
        - this

        See
        - .setOrtho2D(double, double, double, double)
        """
        ...


    def ortho2DLH(self, left: float, right: float, bottom: float, top: float, dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Apply an orthographic projection transformation for a left-handed coordinate system to this matrix and store the result in `dest`.
        
        This method is equivalent to calling .orthoLH(double, double, double, double, double, double, Matrix4x3d) orthoLH() with
        `zNear=-1` and `zFar=+1`.
        
        If `M` is `this` matrix and `O` the orthographic projection matrix,
        then the new matrix will be `M * O`. So when transforming a
        vector `v` with the new matrix by using `M * O * v`, the
        orthographic projection transformation will be applied first!
        
        In order to set the matrix to an orthographic projection without post-multiplying it,
        use .setOrtho2DLH(double, double, double, double) setOrthoLH().
        
        Reference: <a href="http://www.songho.ca/opengl/gl_projectionmatrix.html#ortho">http://www.songho.ca</a>

        Arguments
        - left: the distance from the center to the left frustum edge
        - right: the distance from the center to the right frustum edge
        - bottom: the distance from the center to the bottom frustum edge
        - top: the distance from the center to the top frustum edge
        - dest: will hold the result

        Returns
        - dest

        See
        - .setOrtho2DLH(double, double, double, double)
        """
        ...


    def ortho2DLH(self, left: float, right: float, bottom: float, top: float) -> "Matrix4x3d":
        """
        Apply an orthographic projection transformation for a left-handed coordinate system to this matrix.
        
        This method is equivalent to calling .orthoLH(double, double, double, double, double, double) orthoLH() with
        `zNear=-1` and `zFar=+1`.
        
        If `M` is `this` matrix and `O` the orthographic projection matrix,
        then the new matrix will be `M * O`. So when transforming a
        vector `v` with the new matrix by using `M * O * v`, the
        orthographic projection transformation will be applied first!
        
        In order to set the matrix to an orthographic projection without post-multiplying it,
        use .setOrtho2DLH(double, double, double, double) setOrtho2DLH().
        
        Reference: <a href="http://www.songho.ca/opengl/gl_projectionmatrix.html#ortho">http://www.songho.ca</a>

        Arguments
        - left: the distance from the center to the left frustum edge
        - right: the distance from the center to the right frustum edge
        - bottom: the distance from the center to the bottom frustum edge
        - top: the distance from the center to the top frustum edge

        Returns
        - this

        See
        - .setOrtho2DLH(double, double, double, double)
        """
        ...


    def setOrtho2D(self, left: float, right: float, bottom: float, top: float) -> "Matrix4x3d":
        """
        Set this matrix to be an orthographic projection transformation for a right-handed coordinate system.
        
        This method is equivalent to calling .setOrtho(double, double, double, double, double, double) setOrtho() with
        `zNear=-1` and `zFar=+1`.
        
        In order to apply the orthographic projection to an already existing transformation,
        use .ortho2D(double, double, double, double) ortho2D().
        
        Reference: <a href="http://www.songho.ca/opengl/gl_projectionmatrix.html#ortho">http://www.songho.ca</a>

        Arguments
        - left: the distance from the center to the left frustum edge
        - right: the distance from the center to the right frustum edge
        - bottom: the distance from the center to the bottom frustum edge
        - top: the distance from the center to the top frustum edge

        Returns
        - this

        See
        - .ortho2D(double, double, double, double)
        """
        ...


    def setOrtho2DLH(self, left: float, right: float, bottom: float, top: float) -> "Matrix4x3d":
        """
        Set this matrix to be an orthographic projection transformation for a left-handed coordinate system.
        
        This method is equivalent to calling .setOrtho(double, double, double, double, double, double) setOrthoLH() with
        `zNear=-1` and `zFar=+1`.
        
        In order to apply the orthographic projection to an already existing transformation,
        use .ortho2DLH(double, double, double, double) ortho2DLH().
        
        Reference: <a href="http://www.songho.ca/opengl/gl_projectionmatrix.html#ortho">http://www.songho.ca</a>

        Arguments
        - left: the distance from the center to the left frustum edge
        - right: the distance from the center to the right frustum edge
        - bottom: the distance from the center to the bottom frustum edge
        - top: the distance from the center to the top frustum edge

        Returns
        - this

        See
        - .ortho2DLH(double, double, double, double)
        """
        ...


    def lookAlong(self, dir: "Vector3dc", up: "Vector3dc") -> "Matrix4x3d":
        """
        Apply a rotation transformation to this matrix to make `-z` point along `dir`. 
        
        If `M` is `this` matrix and `L` the lookalong rotation matrix,
        then the new matrix will be `M * L`. So when transforming a
        vector `v` with the new matrix by using `M * L * v`, the
        lookalong rotation transformation will be applied first!
        
        This is equivalent to calling
        .lookAt(Vector3dc, Vector3dc, Vector3dc) lookAt
        with `eye = (0, 0, 0)` and `center = dir`.
        
        In order to set the matrix to a lookalong transformation without post-multiplying it,
        use .setLookAlong(Vector3dc, Vector3dc) setLookAlong().

        Arguments
        - dir: the direction in space to look along
        - up: the direction of 'up'

        Returns
        - this

        See
        - .setLookAlong(Vector3dc, Vector3dc)
        """
        ...


    def lookAlong(self, dir: "Vector3dc", up: "Vector3dc", dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Apply a rotation transformation to this matrix to make `-z` point along `dir`
        and store the result in `dest`. 
        
        If `M` is `this` matrix and `L` the lookalong rotation matrix,
        then the new matrix will be `M * L`. So when transforming a
        vector `v` with the new matrix by using `M * L * v`, the
        lookalong rotation transformation will be applied first!
        
        This is equivalent to calling
        .lookAt(Vector3dc, Vector3dc, Vector3dc) lookAt
        with `eye = (0, 0, 0)` and `center = dir`.
        
        In order to set the matrix to a lookalong transformation without post-multiplying it,
        use .setLookAlong(Vector3dc, Vector3dc) setLookAlong().

        Arguments
        - dir: the direction in space to look along
        - up: the direction of 'up'
        - dest: will hold the result

        Returns
        - dest

        See
        - .setLookAlong(Vector3dc, Vector3dc)
        """
        ...


    def lookAlong(self, dirX: float, dirY: float, dirZ: float, upX: float, upY: float, upZ: float, dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Apply a rotation transformation to this matrix to make `-z` point along `dir`
        and store the result in `dest`. 
        
        If `M` is `this` matrix and `L` the lookalong rotation matrix,
        then the new matrix will be `M * L`. So when transforming a
        vector `v` with the new matrix by using `M * L * v`, the
        lookalong rotation transformation will be applied first!
        
        This is equivalent to calling
        .lookAt(double, double, double, double, double, double, double, double, double) lookAt()
        with `eye = (0, 0, 0)` and `center = dir`.
        
        In order to set the matrix to a lookalong transformation without post-multiplying it,
        use .setLookAlong(double, double, double, double, double, double) setLookAlong()

        Arguments
        - dirX: the x-coordinate of the direction to look along
        - dirY: the y-coordinate of the direction to look along
        - dirZ: the z-coordinate of the direction to look along
        - upX: the x-coordinate of the up vector
        - upY: the y-coordinate of the up vector
        - upZ: the z-coordinate of the up vector
        - dest: will hold the result

        Returns
        - dest

        See
        - .setLookAlong(double, double, double, double, double, double)
        """
        ...


    def lookAlong(self, dirX: float, dirY: float, dirZ: float, upX: float, upY: float, upZ: float) -> "Matrix4x3d":
        """
        Apply a rotation transformation to this matrix to make `-z` point along `dir`. 
        
        If `M` is `this` matrix and `L` the lookalong rotation matrix,
        then the new matrix will be `M * L`. So when transforming a
        vector `v` with the new matrix by using `M * L * v`, the
        lookalong rotation transformation will be applied first!
        
        This is equivalent to calling
        .lookAt(double, double, double, double, double, double, double, double, double) lookAt()
        with `eye = (0, 0, 0)` and `center = dir`.
        
        In order to set the matrix to a lookalong transformation without post-multiplying it,
        use .setLookAlong(double, double, double, double, double, double) setLookAlong()

        Arguments
        - dirX: the x-coordinate of the direction to look along
        - dirY: the y-coordinate of the direction to look along
        - dirZ: the z-coordinate of the direction to look along
        - upX: the x-coordinate of the up vector
        - upY: the y-coordinate of the up vector
        - upZ: the z-coordinate of the up vector

        Returns
        - this

        See
        - .setLookAlong(double, double, double, double, double, double)
        """
        ...


    def setLookAlong(self, dir: "Vector3dc", up: "Vector3dc") -> "Matrix4x3d":
        """
        Set this matrix to a rotation transformation to make `-z`
        point along `dir`.
        
        This is equivalent to calling
        .setLookAt(Vector3dc, Vector3dc, Vector3dc) setLookAt() 
        with `eye = (0, 0, 0)` and `center = dir`.
        
        In order to apply the lookalong transformation to any previous existing transformation,
        use .lookAlong(Vector3dc, Vector3dc).

        Arguments
        - dir: the direction in space to look along
        - up: the direction of 'up'

        Returns
        - this

        See
        - .lookAlong(Vector3dc, Vector3dc)
        """
        ...


    def setLookAlong(self, dirX: float, dirY: float, dirZ: float, upX: float, upY: float, upZ: float) -> "Matrix4x3d":
        """
        Set this matrix to a rotation transformation to make `-z`
        point along `dir`.
        
        This is equivalent to calling
        .setLookAt(double, double, double, double, double, double, double, double, double)
        setLookAt() with `eye = (0, 0, 0)` and `center = dir`.
        
        In order to apply the lookalong transformation to any previous existing transformation,
        use .lookAlong(double, double, double, double, double, double) lookAlong()

        Arguments
        - dirX: the x-coordinate of the direction to look along
        - dirY: the y-coordinate of the direction to look along
        - dirZ: the z-coordinate of the direction to look along
        - upX: the x-coordinate of the up vector
        - upY: the y-coordinate of the up vector
        - upZ: the z-coordinate of the up vector

        Returns
        - this

        See
        - .lookAlong(double, double, double, double, double, double)
        """
        ...


    def setLookAt(self, eye: "Vector3dc", center: "Vector3dc", up: "Vector3dc") -> "Matrix4x3d":
        """
        Set this matrix to be a "lookat" transformation for a right-handed coordinate system, that aligns
        `-z` with `center - eye`.
        
        In order to not make use of vectors to specify `eye`, `center` and `up` but use primitives,
        like in the GLU function, use .setLookAt(double, double, double, double, double, double, double, double, double) setLookAt()
        instead.
        
        In order to apply the lookat transformation to a previous existing transformation,
        use .lookAt(Vector3dc, Vector3dc, Vector3dc) lookAt().

        Arguments
        - eye: the position of the camera
        - center: the point in space to look at
        - up: the direction of 'up'

        Returns
        - this

        See
        - .lookAt(Vector3dc, Vector3dc, Vector3dc)
        """
        ...


    def setLookAt(self, eyeX: float, eyeY: float, eyeZ: float, centerX: float, centerY: float, centerZ: float, upX: float, upY: float, upZ: float) -> "Matrix4x3d":
        """
        Set this matrix to be a "lookat" transformation for a right-handed coordinate system, 
        that aligns `-z` with `center - eye`.
        
        In order to apply the lookat transformation to a previous existing transformation,
        use .lookAt(double, double, double, double, double, double, double, double, double) lookAt.

        Arguments
        - eyeX: the x-coordinate of the eye/camera location
        - eyeY: the y-coordinate of the eye/camera location
        - eyeZ: the z-coordinate of the eye/camera location
        - centerX: the x-coordinate of the point to look at
        - centerY: the y-coordinate of the point to look at
        - centerZ: the z-coordinate of the point to look at
        - upX: the x-coordinate of the up vector
        - upY: the y-coordinate of the up vector
        - upZ: the z-coordinate of the up vector

        Returns
        - this

        See
        - .lookAt(double, double, double, double, double, double, double, double, double)
        """
        ...


    def lookAt(self, eye: "Vector3dc", center: "Vector3dc", up: "Vector3dc", dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Apply a "lookat" transformation to this matrix for a right-handed coordinate system, 
        that aligns `-z` with `center - eye` and store the result in `dest`.
        
        If `M` is `this` matrix and `L` the lookat matrix,
        then the new matrix will be `M * L`. So when transforming a
        vector `v` with the new matrix by using `M * L * v`,
        the lookat transformation will be applied first!
        
        In order to set the matrix to a lookat transformation without post-multiplying it,
        use .setLookAt(Vector3dc, Vector3dc, Vector3dc).

        Arguments
        - eye: the position of the camera
        - center: the point in space to look at
        - up: the direction of 'up'
        - dest: will hold the result

        Returns
        - dest

        See
        - .setLookAlong(Vector3dc, Vector3dc)
        """
        ...


    def lookAt(self, eye: "Vector3dc", center: "Vector3dc", up: "Vector3dc") -> "Matrix4x3d":
        """
        Apply a "lookat" transformation to this matrix for a right-handed coordinate system, 
        that aligns `-z` with `center - eye`.
        
        If `M` is `this` matrix and `L` the lookat matrix,
        then the new matrix will be `M * L`. So when transforming a
        vector `v` with the new matrix by using `M * L * v`,
        the lookat transformation will be applied first!
        
        In order to set the matrix to a lookat transformation without post-multiplying it,
        use .setLookAt(Vector3dc, Vector3dc, Vector3dc).

        Arguments
        - eye: the position of the camera
        - center: the point in space to look at
        - up: the direction of 'up'

        Returns
        - this

        See
        - .setLookAlong(Vector3dc, Vector3dc)
        """
        ...


    def lookAt(self, eyeX: float, eyeY: float, eyeZ: float, centerX: float, centerY: float, centerZ: float, upX: float, upY: float, upZ: float, dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Apply a "lookat" transformation to this matrix for a right-handed coordinate system, 
        that aligns `-z` with `center - eye` and store the result in `dest`.
        
        If `M` is `this` matrix and `L` the lookat matrix,
        then the new matrix will be `M * L`. So when transforming a
        vector `v` with the new matrix by using `M * L * v`,
        the lookat transformation will be applied first!
        
        In order to set the matrix to a lookat transformation without post-multiplying it,
        use .setLookAt(double, double, double, double, double, double, double, double, double) setLookAt().

        Arguments
        - eyeX: the x-coordinate of the eye/camera location
        - eyeY: the y-coordinate of the eye/camera location
        - eyeZ: the z-coordinate of the eye/camera location
        - centerX: the x-coordinate of the point to look at
        - centerY: the y-coordinate of the point to look at
        - centerZ: the z-coordinate of the point to look at
        - upX: the x-coordinate of the up vector
        - upY: the y-coordinate of the up vector
        - upZ: the z-coordinate of the up vector
        - dest: will hold the result

        Returns
        - dest

        See
        - .setLookAt(double, double, double, double, double, double, double, double, double)
        """
        ...


    def lookAt(self, eyeX: float, eyeY: float, eyeZ: float, centerX: float, centerY: float, centerZ: float, upX: float, upY: float, upZ: float) -> "Matrix4x3d":
        """
        Apply a "lookat" transformation to this matrix for a right-handed coordinate system, 
        that aligns `-z` with `center - eye`.
        
        If `M` is `this` matrix and `L` the lookat matrix,
        then the new matrix will be `M * L`. So when transforming a
        vector `v` with the new matrix by using `M * L * v`,
        the lookat transformation will be applied first!
        
        In order to set the matrix to a lookat transformation without post-multiplying it,
        use .setLookAt(double, double, double, double, double, double, double, double, double) setLookAt().

        Arguments
        - eyeX: the x-coordinate of the eye/camera location
        - eyeY: the y-coordinate of the eye/camera location
        - eyeZ: the z-coordinate of the eye/camera location
        - centerX: the x-coordinate of the point to look at
        - centerY: the y-coordinate of the point to look at
        - centerZ: the z-coordinate of the point to look at
        - upX: the x-coordinate of the up vector
        - upY: the y-coordinate of the up vector
        - upZ: the z-coordinate of the up vector

        Returns
        - this

        See
        - .setLookAt(double, double, double, double, double, double, double, double, double)
        """
        ...


    def setLookAtLH(self, eye: "Vector3dc", center: "Vector3dc", up: "Vector3dc") -> "Matrix4x3d":
        """
        Set this matrix to be a "lookat" transformation for a left-handed coordinate system, that aligns
        `+z` with `center - eye`.
        
        In order to not make use of vectors to specify `eye`, `center` and `up` but use primitives,
        like in the GLU function, use .setLookAtLH(double, double, double, double, double, double, double, double, double) setLookAtLH()
        instead.
        
        In order to apply the lookat transformation to a previous existing transformation,
        use .lookAtLH(Vector3dc, Vector3dc, Vector3dc) lookAt().

        Arguments
        - eye: the position of the camera
        - center: the point in space to look at
        - up: the direction of 'up'

        Returns
        - this

        See
        - .lookAtLH(Vector3dc, Vector3dc, Vector3dc)
        """
        ...


    def setLookAtLH(self, eyeX: float, eyeY: float, eyeZ: float, centerX: float, centerY: float, centerZ: float, upX: float, upY: float, upZ: float) -> "Matrix4x3d":
        """
        Set this matrix to be a "lookat" transformation for a left-handed coordinate system, 
        that aligns `+z` with `center - eye`.
        
        In order to apply the lookat transformation to a previous existing transformation,
        use .lookAtLH(double, double, double, double, double, double, double, double, double) lookAtLH.

        Arguments
        - eyeX: the x-coordinate of the eye/camera location
        - eyeY: the y-coordinate of the eye/camera location
        - eyeZ: the z-coordinate of the eye/camera location
        - centerX: the x-coordinate of the point to look at
        - centerY: the y-coordinate of the point to look at
        - centerZ: the z-coordinate of the point to look at
        - upX: the x-coordinate of the up vector
        - upY: the y-coordinate of the up vector
        - upZ: the z-coordinate of the up vector

        Returns
        - this

        See
        - .lookAtLH(double, double, double, double, double, double, double, double, double)
        """
        ...


    def lookAtLH(self, eye: "Vector3dc", center: "Vector3dc", up: "Vector3dc", dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Apply a "lookat" transformation to this matrix for a left-handed coordinate system, 
        that aligns `+z` with `center - eye` and store the result in `dest`.
        
        If `M` is `this` matrix and `L` the lookat matrix,
        then the new matrix will be `M * L`. So when transforming a
        vector `v` with the new matrix by using `M * L * v`,
        the lookat transformation will be applied first!
        
        In order to set the matrix to a lookat transformation without post-multiplying it,
        use .setLookAtLH(Vector3dc, Vector3dc, Vector3dc).

        Arguments
        - eye: the position of the camera
        - center: the point in space to look at
        - up: the direction of 'up'
        - dest: will hold the result

        Returns
        - dest

        See
        - .lookAtLH(double, double, double, double, double, double, double, double, double)
        """
        ...


    def lookAtLH(self, eye: "Vector3dc", center: "Vector3dc", up: "Vector3dc") -> "Matrix4x3d":
        """
        Apply a "lookat" transformation to this matrix for a left-handed coordinate system, 
        that aligns `+z` with `center - eye`.
        
        If `M` is `this` matrix and `L` the lookat matrix,
        then the new matrix will be `M * L`. So when transforming a
        vector `v` with the new matrix by using `M * L * v`,
        the lookat transformation will be applied first!
        
        In order to set the matrix to a lookat transformation without post-multiplying it,
        use .setLookAtLH(Vector3dc, Vector3dc, Vector3dc).

        Arguments
        - eye: the position of the camera
        - center: the point in space to look at
        - up: the direction of 'up'

        Returns
        - this

        See
        - .lookAtLH(double, double, double, double, double, double, double, double, double)
        """
        ...


    def lookAtLH(self, eyeX: float, eyeY: float, eyeZ: float, centerX: float, centerY: float, centerZ: float, upX: float, upY: float, upZ: float, dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Apply a "lookat" transformation to this matrix for a left-handed coordinate system, 
        that aligns `+z` with `center - eye` and store the result in `dest`.
        
        If `M` is `this` matrix and `L` the lookat matrix,
        then the new matrix will be `M * L`. So when transforming a
        vector `v` with the new matrix by using `M * L * v`,
        the lookat transformation will be applied first!
        
        In order to set the matrix to a lookat transformation without post-multiplying it,
        use .setLookAtLH(double, double, double, double, double, double, double, double, double) setLookAtLH().

        Arguments
        - eyeX: the x-coordinate of the eye/camera location
        - eyeY: the y-coordinate of the eye/camera location
        - eyeZ: the z-coordinate of the eye/camera location
        - centerX: the x-coordinate of the point to look at
        - centerY: the y-coordinate of the point to look at
        - centerZ: the z-coordinate of the point to look at
        - upX: the x-coordinate of the up vector
        - upY: the y-coordinate of the up vector
        - upZ: the z-coordinate of the up vector
        - dest: will hold the result

        Returns
        - dest

        See
        - .setLookAtLH(double, double, double, double, double, double, double, double, double)
        """
        ...


    def lookAtLH(self, eyeX: float, eyeY: float, eyeZ: float, centerX: float, centerY: float, centerZ: float, upX: float, upY: float, upZ: float) -> "Matrix4x3d":
        """
        Apply a "lookat" transformation to this matrix for a left-handed coordinate system, 
        that aligns `+z` with `center - eye`.
        
        If `M` is `this` matrix and `L` the lookat matrix,
        then the new matrix will be `M * L`. So when transforming a
        vector `v` with the new matrix by using `M * L * v`,
        the lookat transformation will be applied first!
        
        In order to set the matrix to a lookat transformation without post-multiplying it,
        use .setLookAtLH(double, double, double, double, double, double, double, double, double) setLookAtLH().

        Arguments
        - eyeX: the x-coordinate of the eye/camera location
        - eyeY: the y-coordinate of the eye/camera location
        - eyeZ: the z-coordinate of the eye/camera location
        - centerX: the x-coordinate of the point to look at
        - centerY: the y-coordinate of the point to look at
        - centerZ: the z-coordinate of the point to look at
        - upX: the x-coordinate of the up vector
        - upY: the y-coordinate of the up vector
        - upZ: the z-coordinate of the up vector

        Returns
        - this

        See
        - .setLookAtLH(double, double, double, double, double, double, double, double, double)
        """
        ...


    def frustumPlane(self, which: int, dest: "Vector4d") -> "Vector4d":
        ...


    def positiveZ(self, dir: "Vector3d") -> "Vector3d":
        ...


    def normalizedPositiveZ(self, dir: "Vector3d") -> "Vector3d":
        ...


    def positiveX(self, dir: "Vector3d") -> "Vector3d":
        ...


    def normalizedPositiveX(self, dir: "Vector3d") -> "Vector3d":
        ...


    def positiveY(self, dir: "Vector3d") -> "Vector3d":
        ...


    def normalizedPositiveY(self, dir: "Vector3d") -> "Vector3d":
        ...


    def origin(self, origin: "Vector3d") -> "Vector3d":
        ...


    def shadow(self, light: "Vector4dc", a: float, b: float, c: float, d: float) -> "Matrix4x3d":
        """
        Apply a projection transformation to this matrix that projects onto the plane specified via the general plane equation
        `x*a + y*b + z*c + d = 0` as if casting a shadow from a given light position/direction `light`.
        
        If `light.w` is `0.0` the light is being treated as a directional light; if it is `1.0` it is a point light.
        
        If `M` is `this` matrix and `S` the shadow matrix,
        then the new matrix will be `M * S`. So when transforming a
        vector `v` with the new matrix by using `M * S * v`, the
        shadow projection will be applied first!
        
        Reference: <a href="ftp://ftp.sgi.com/opengl/contrib/blythe/advanced99/notes/node192.html">ftp.sgi.com</a>

        Arguments
        - light: the light's vector
        - a: the x factor in the plane equation
        - b: the y factor in the plane equation
        - c: the z factor in the plane equation
        - d: the constant in the plane equation

        Returns
        - this
        """
        ...


    def shadow(self, light: "Vector4dc", a: float, b: float, c: float, d: float, dest: "Matrix4x3d") -> "Matrix4x3d":
        ...


    def shadow(self, lightX: float, lightY: float, lightZ: float, lightW: float, a: float, b: float, c: float, d: float) -> "Matrix4x3d":
        """
        Apply a projection transformation to this matrix that projects onto the plane specified via the general plane equation
        `x*a + y*b + z*c + d = 0` as if casting a shadow from a given light position/direction `(lightX, lightY, lightZ, lightW)`.
        
        If `lightW` is `0.0` the light is being treated as a directional light; if it is `1.0` it is a point light.
        
        If `M` is `this` matrix and `S` the shadow matrix,
        then the new matrix will be `M * S`. So when transforming a
        vector `v` with the new matrix by using `M * S * v`, the
        shadow projection will be applied first!
        
        Reference: <a href="ftp://ftp.sgi.com/opengl/contrib/blythe/advanced99/notes/node192.html">ftp.sgi.com</a>

        Arguments
        - lightX: the x-component of the light's vector
        - lightY: the y-component of the light's vector
        - lightZ: the z-component of the light's vector
        - lightW: the w-component of the light's vector
        - a: the x factor in the plane equation
        - b: the y factor in the plane equation
        - c: the z factor in the plane equation
        - d: the constant in the plane equation

        Returns
        - this
        """
        ...


    def shadow(self, lightX: float, lightY: float, lightZ: float, lightW: float, a: float, b: float, c: float, d: float, dest: "Matrix4x3d") -> "Matrix4x3d":
        ...


    def shadow(self, light: "Vector4dc", planeTransform: "Matrix4x3dc", dest: "Matrix4x3d") -> "Matrix4x3d":
        ...


    def shadow(self, light: "Vector4dc", planeTransform: "Matrix4x3dc") -> "Matrix4x3d":
        """
        Apply a projection transformation to this matrix that projects onto the plane with the general plane equation
        `y = 0` as if casting a shadow from a given light position/direction `light`.
        
        Before the shadow projection is applied, the plane is transformed via the specified `planeTransformation`.
        
        If `light.w` is `0.0` the light is being treated as a directional light; if it is `1.0` it is a point light.
        
        If `M` is `this` matrix and `S` the shadow matrix,
        then the new matrix will be `M * S`. So when transforming a
        vector `v` with the new matrix by using `M * S * v`, the
        shadow projection will be applied first!

        Arguments
        - light: the light's vector
        - planeTransform: the transformation to transform the implied plane `y = 0` before applying the projection

        Returns
        - this
        """
        ...


    def shadow(self, lightX: float, lightY: float, lightZ: float, lightW: float, planeTransform: "Matrix4x3dc", dest: "Matrix4x3d") -> "Matrix4x3d":
        ...


    def shadow(self, lightX: float, lightY: float, lightZ: float, lightW: float, planeTransform: "Matrix4x3dc") -> "Matrix4x3d":
        """
        Apply a projection transformation to this matrix that projects onto the plane with the general plane equation
        `y = 0` as if casting a shadow from a given light position/direction `(lightX, lightY, lightZ, lightW)`.
        
        Before the shadow projection is applied, the plane is transformed via the specified `planeTransformation`.
        
        If `lightW` is `0.0` the light is being treated as a directional light; if it is `1.0` it is a point light.
        
        If `M` is `this` matrix and `S` the shadow matrix,
        then the new matrix will be `M * S`. So when transforming a
        vector `v` with the new matrix by using `M * S * v`, the
        shadow projection will be applied first!

        Arguments
        - lightX: the x-component of the light vector
        - lightY: the y-component of the light vector
        - lightZ: the z-component of the light vector
        - lightW: the w-component of the light vector
        - planeTransform: the transformation to transform the implied plane `y = 0` before applying the projection

        Returns
        - this
        """
        ...


    def billboardCylindrical(self, objPos: "Vector3dc", targetPos: "Vector3dc", up: "Vector3dc") -> "Matrix4x3d":
        """
        Set this matrix to a cylindrical billboard transformation that rotates the local +Z axis of a given object with position `objPos` towards
        a target position at `targetPos` while constraining a cylindrical rotation around the given `up` vector.
        
        This method can be used to create the complete model transformation for a given object, including the translation of the object to
        its position `objPos`.

        Arguments
        - objPos: the position of the object to rotate towards `targetPos`
        - targetPos: the position of the target (for example the camera) towards which to rotate the object
        - up: the rotation axis (must be Vector3d.normalize() normalized)

        Returns
        - this
        """
        ...


    def billboardSpherical(self, objPos: "Vector3dc", targetPos: "Vector3dc", up: "Vector3dc") -> "Matrix4x3d":
        """
        Set this matrix to a spherical billboard transformation that rotates the local +Z axis of a given object with position `objPos` towards
        a target position at `targetPos`.
        
        This method can be used to create the complete model transformation for a given object, including the translation of the object to
        its position `objPos`.
        
        If preserving an *up* vector is not necessary when rotating the +Z axis, then a shortest arc rotation can be obtained 
        using .billboardSpherical(Vector3dc, Vector3dc).

        Arguments
        - objPos: the position of the object to rotate towards `targetPos`
        - targetPos: the position of the target (for example the camera) towards which to rotate the object
        - up: the up axis used to orient the object

        Returns
        - this

        See
        - .billboardSpherical(Vector3dc, Vector3dc)
        """
        ...


    def billboardSpherical(self, objPos: "Vector3dc", targetPos: "Vector3dc") -> "Matrix4x3d":
        """
        Set this matrix to a spherical billboard transformation that rotates the local +Z axis of a given object with position `objPos` towards
        a target position at `targetPos` using a shortest arc rotation by not preserving any *up* vector of the object.
        
        This method can be used to create the complete model transformation for a given object, including the translation of the object to
        its position `objPos`.
        
        In order to specify an *up* vector which needs to be maintained when rotating the +Z axis of the object,
        use .billboardSpherical(Vector3dc, Vector3dc, Vector3dc).

        Arguments
        - objPos: the position of the object to rotate towards `targetPos`
        - targetPos: the position of the target (for example the camera) towards which to rotate the object

        Returns
        - this

        See
        - .billboardSpherical(Vector3dc, Vector3dc, Vector3dc)
        """
        ...


    def hashCode(self) -> int:
        ...


    def equals(self, obj: "Object") -> bool:
        ...


    def equals(self, m: "Matrix4x3dc", delta: float) -> bool:
        ...


    def pick(self, x: float, y: float, width: float, height: float, viewport: list[int], dest: "Matrix4x3d") -> "Matrix4x3d":
        ...


    def pick(self, x: float, y: float, width: float, height: float, viewport: list[int]) -> "Matrix4x3d":
        """
        Apply a picking transformation to this matrix using the given window coordinates `(x, y)` as the pick center
        and the given `(width, height)` as the size of the picking region in window coordinates.

        Arguments
        - x: the x coordinate of the picking region center in window coordinates
        - y: the y coordinate of the picking region center in window coordinates
        - width: the width of the picking region in window coordinates
        - height: the height of the picking region in window coordinates
        - viewport: the viewport described by `[x, y, width, height]`

        Returns
        - this
        """
        ...


    def swap(self, other: "Matrix4x3d") -> "Matrix4x3d":
        """
        Exchange the values of `this` matrix with the given `other` matrix.

        Arguments
        - other: the other matrix to exchange the values with

        Returns
        - this
        """
        ...


    def arcball(self, radius: float, centerX: float, centerY: float, centerZ: float, angleX: float, angleY: float, dest: "Matrix4x3d") -> "Matrix4x3d":
        ...


    def arcball(self, radius: float, center: "Vector3dc", angleX: float, angleY: float, dest: "Matrix4x3d") -> "Matrix4x3d":
        ...


    def arcball(self, radius: float, centerX: float, centerY: float, centerZ: float, angleX: float, angleY: float) -> "Matrix4x3d":
        """
        Apply an arcball view transformation to this matrix with the given `radius` and center `(centerX, centerY, centerZ)`
        position of the arcball and the specified X and Y rotation angles.
        
        This method is equivalent to calling: `translate(0, 0, -radius).rotateX(angleX).rotateY(angleY).translate(-centerX, -centerY, -centerZ)`

        Arguments
        - radius: the arcball radius
        - centerX: the x coordinate of the center position of the arcball
        - centerY: the y coordinate of the center position of the arcball
        - centerZ: the z coordinate of the center position of the arcball
        - angleX: the rotation angle around the X axis in radians
        - angleY: the rotation angle around the Y axis in radians

        Returns
        - this
        """
        ...


    def arcball(self, radius: float, center: "Vector3dc", angleX: float, angleY: float) -> "Matrix4x3d":
        """
        Apply an arcball view transformation to this matrix with the given `radius` and `center`
        position of the arcball and the specified X and Y rotation angles.
        
        This method is equivalent to calling: `translate(0, 0, -radius).rotateX(angleX).rotateY(angleY).translate(-center.x, -center.y, -center.z)`

        Arguments
        - radius: the arcball radius
        - center: the center position of the arcball
        - angleX: the rotation angle around the X axis in radians
        - angleY: the rotation angle around the Y axis in radians

        Returns
        - this
        """
        ...


    def transformAab(self, minX: float, minY: float, minZ: float, maxX: float, maxY: float, maxZ: float, outMin: "Vector3d", outMax: "Vector3d") -> "Matrix4x3d":
        ...


    def transformAab(self, min: "Vector3dc", max: "Vector3dc", outMin: "Vector3d", outMax: "Vector3d") -> "Matrix4x3d":
        ...


    def lerp(self, other: "Matrix4x3dc", t: float) -> "Matrix4x3d":
        """
        Linearly interpolate `this` and `other` using the given interpolation factor `t`
        and store the result in `this`.
        
        If `t` is `0.0` then the result is `this`. If the interpolation factor is `1.0`
        then the result is `other`.

        Arguments
        - other: the other matrix
        - t: the interpolation factor between 0.0 and 1.0

        Returns
        - this
        """
        ...


    def lerp(self, other: "Matrix4x3dc", t: float, dest: "Matrix4x3d") -> "Matrix4x3d":
        ...


    def rotateTowards(self, dir: "Vector3dc", up: "Vector3dc", dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Apply a model transformation to this matrix for a right-handed coordinate system, 
        that aligns the local `+Z` axis with `dir`
        and store the result in `dest`.
        
        If `M` is `this` matrix and `L` the lookat matrix,
        then the new matrix will be `M * L`. So when transforming a
        vector `v` with the new matrix by using `M * L * v`,
        the lookat transformation will be applied first!
        
        In order to set the matrix to a rotation transformation without post-multiplying it,
        use .rotationTowards(Vector3dc, Vector3dc) rotationTowards().
        
        This method is equivalent to calling: `mul(new Matrix4x3d().lookAt(new Vector3d(), new Vector3d(dir).negate(), up).invert(), dest)`

        Arguments
        - dir: the direction to rotate towards
        - up: the up vector
        - dest: will hold the result

        Returns
        - dest

        See
        - .rotationTowards(Vector3dc, Vector3dc)
        """
        ...


    def rotateTowards(self, dir: "Vector3dc", up: "Vector3dc") -> "Matrix4x3d":
        """
        Apply a model transformation to this matrix for a right-handed coordinate system, 
        that aligns the local `+Z` axis with `dir`.
        
        If `M` is `this` matrix and `L` the lookat matrix,
        then the new matrix will be `M * L`. So when transforming a
        vector `v` with the new matrix by using `M * L * v`,
        the lookat transformation will be applied first!
        
        In order to set the matrix to a rotation transformation without post-multiplying it,
        use .rotationTowards(Vector3dc, Vector3dc) rotationTowards().
        
        This method is equivalent to calling: `mul(new Matrix4x3d().lookAt(new Vector3d(), new Vector3d(dir).negate(), up).invert())`

        Arguments
        - dir: the direction to orient towards
        - up: the up vector

        Returns
        - this

        See
        - .rotationTowards(Vector3dc, Vector3dc)
        """
        ...


    def rotateTowards(self, dirX: float, dirY: float, dirZ: float, upX: float, upY: float, upZ: float) -> "Matrix4x3d":
        """
        Apply a model transformation to this matrix for a right-handed coordinate system, 
        that aligns the local `+Z` axis with `(dirX, dirY, dirZ)`.
        
        If `M` is `this` matrix and `L` the lookat matrix,
        then the new matrix will be `M * L`. So when transforming a
        vector `v` with the new matrix by using `M * L * v`,
        the lookat transformation will be applied first!
        
        In order to set the matrix to a rotation transformation without post-multiplying it,
        use .rotationTowards(double, double, double, double, double, double) rotationTowards().
        
        This method is equivalent to calling: `mul(new Matrix4x3d().lookAt(0, 0, 0, -dirX, -dirY, -dirZ, upX, upY, upZ).invert())`

        Arguments
        - dirX: the x-coordinate of the direction to rotate towards
        - dirY: the y-coordinate of the direction to rotate towards
        - dirZ: the z-coordinate of the direction to rotate towards
        - upX: the x-coordinate of the up vector
        - upY: the y-coordinate of the up vector
        - upZ: the z-coordinate of the up vector

        Returns
        - this

        See
        - .rotationTowards(double, double, double, double, double, double)
        """
        ...


    def rotateTowards(self, dirX: float, dirY: float, dirZ: float, upX: float, upY: float, upZ: float, dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Apply a model transformation to this matrix for a right-handed coordinate system, 
        that aligns the local `+Z` axis with `(dirX, dirY, dirZ)`
        and store the result in `dest`.
        
        If `M` is `this` matrix and `L` the lookat matrix,
        then the new matrix will be `M * L`. So when transforming a
        vector `v` with the new matrix by using `M * L * v`,
        the lookat transformation will be applied first!
        
        In order to set the matrix to a rotation transformation without post-multiplying it,
        use .rotationTowards(double, double, double, double, double, double) rotationTowards().
        
        This method is equivalent to calling: `mul(new Matrix4x3d().lookAt(0, 0, 0, -dirX, -dirY, -dirZ, upX, upY, upZ).invert(), dest)`

        Arguments
        - dirX: the x-coordinate of the direction to rotate towards
        - dirY: the y-coordinate of the direction to rotate towards
        - dirZ: the z-coordinate of the direction to rotate towards
        - upX: the x-coordinate of the up vector
        - upY: the y-coordinate of the up vector
        - upZ: the z-coordinate of the up vector
        - dest: will hold the result

        Returns
        - dest

        See
        - .rotationTowards(double, double, double, double, double, double)
        """
        ...


    def rotationTowards(self, dir: "Vector3dc", up: "Vector3dc") -> "Matrix4x3d":
        """
        Set this matrix to a model transformation for a right-handed coordinate system, 
        that aligns the local `-z` axis with `dir`.
        
        In order to apply the rotation transformation to a previous existing transformation,
        use .rotateTowards(double, double, double, double, double, double) rotateTowards.
        
        This method is equivalent to calling: `setLookAt(new Vector3d(), new Vector3d(dir).negate(), up).invert()`

        Arguments
        - dir: the direction to orient the local -z axis towards
        - up: the up vector

        Returns
        - this

        See
        - .rotateTowards(double, double, double, double, double, double)
        """
        ...


    def rotationTowards(self, dirX: float, dirY: float, dirZ: float, upX: float, upY: float, upZ: float) -> "Matrix4x3d":
        """
        Set this matrix to a model transformation for a right-handed coordinate system, 
        that aligns the local `-z` axis with `(dirX, dirY, dirZ)`.
        
        In order to apply the rotation transformation to a previous existing transformation,
        use .rotateTowards(double, double, double, double, double, double) rotateTowards.
        
        This method is equivalent to calling: `setLookAt(0, 0, 0, -dirX, -dirY, -dirZ, upX, upY, upZ).invert()`

        Arguments
        - dirX: the x-coordinate of the direction to rotate towards
        - dirY: the y-coordinate of the direction to rotate towards
        - dirZ: the z-coordinate of the direction to rotate towards
        - upX: the x-coordinate of the up vector
        - upY: the y-coordinate of the up vector
        - upZ: the z-coordinate of the up vector

        Returns
        - this

        See
        - .rotationTowards(double, double, double, double, double, double)
        """
        ...


    def translationRotateTowards(self, pos: "Vector3dc", dir: "Vector3dc", up: "Vector3dc") -> "Matrix4x3d":
        """
        Set this matrix to a model transformation for a right-handed coordinate system, 
        that translates to the given `pos` and aligns the local `-z`
        axis with `dir`.
        
        This method is equivalent to calling: `translation(pos).rotateTowards(dir, up)`

        Arguments
        - pos: the position to translate to
        - dir: the direction to rotate towards
        - up: the up vector

        Returns
        - this

        See
        - .rotateTowards(Vector3dc, Vector3dc)
        """
        ...


    def translationRotateTowards(self, posX: float, posY: float, posZ: float, dirX: float, dirY: float, dirZ: float, upX: float, upY: float, upZ: float) -> "Matrix4x3d":
        """
        Set this matrix to a model transformation for a right-handed coordinate system, 
        that translates to the given `(posX, posY, posZ)` and aligns the local `-z`
        axis with `(dirX, dirY, dirZ)`.
        
        This method is equivalent to calling: `translation(posX, posY, posZ).rotateTowards(dirX, dirY, dirZ, upX, upY, upZ)`

        Arguments
        - posX: the x-coordinate of the position to translate to
        - posY: the y-coordinate of the position to translate to
        - posZ: the z-coordinate of the position to translate to
        - dirX: the x-coordinate of the direction to rotate towards
        - dirY: the y-coordinate of the direction to rotate towards
        - dirZ: the z-coordinate of the direction to rotate towards
        - upX: the x-coordinate of the up vector
        - upY: the y-coordinate of the up vector
        - upZ: the z-coordinate of the up vector

        Returns
        - this

        See
        - .rotateTowards(double, double, double, double, double, double)
        """
        ...


    def getEulerAnglesZYX(self, dest: "Vector3d") -> "Vector3d":
        ...


    def getEulerAnglesXYZ(self, dest: "Vector3d") -> "Vector3d":
        ...


    def getEulerAnglesYXZ(self, dest: "Vector3d") -> "Vector3d":
        ...


    def obliqueZ(self, a: float, b: float) -> "Matrix4x3d":
        """
        Apply an oblique projection transformation to this matrix with the given values for `a` and
        `b`.
        
        If `M` is `this` matrix and `O` the oblique transformation matrix,
        then the new matrix will be `M * O`. So when transforming a
        vector `v` with the new matrix by using `M * O * v`, the
        oblique transformation will be applied first!
        
        The oblique transformation is defined as:
        ```
        x' = x + a*z
        y' = y + a*z
        z' = z
        ```
        or in matrix form:
        ```
        1 0 a 0
        0 1 b 0
        0 0 1 0
        ```

        Arguments
        - a: the value for the z factor that applies to x
        - b: the value for the z factor that applies to y

        Returns
        - this
        """
        ...


    def obliqueZ(self, a: float, b: float, dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Apply an oblique projection transformation to this matrix with the given values for `a` and
        `b` and store the result in `dest`.
        
        If `M` is `this` matrix and `O` the oblique transformation matrix,
        then the new matrix will be `M * O`. So when transforming a
        vector `v` with the new matrix by using `M * O * v`, the
        oblique transformation will be applied first!
        
        The oblique transformation is defined as:
        ```
        x' = x + a*z
        y' = y + a*z
        z' = z
        ```
        or in matrix form:
        ```
        1 0 a 0
        0 1 b 0
        0 0 1 0
        ```

        Arguments
        - a: the value for the z factor that applies to x
        - b: the value for the z factor that applies to y
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapXZY(self) -> "Matrix4x3d":
        """
        Multiply `this` by the matrix
        ```
        1 0 0 0
        0 0 1 0
        0 1 0 0
        ```

        Returns
        - this
        """
        ...


    def mapXZY(self, dest: "Matrix4x3d") -> "Matrix4x3d":
        ...


    def mapXZnY(self) -> "Matrix4x3d":
        """
        Multiply `this` by the matrix
        ```
        1 0  0 0
        0 0 -1 0
        0 1  0 0
        ```

        Returns
        - this
        """
        ...


    def mapXZnY(self, dest: "Matrix4x3d") -> "Matrix4x3d":
        ...


    def mapXnYnZ(self) -> "Matrix4x3d":
        """
        Multiply `this` by the matrix
        ```
        1  0  0 0
        0 -1  0 0
        0  0 -1 0
        ```

        Returns
        - this
        """
        ...


    def mapXnYnZ(self, dest: "Matrix4x3d") -> "Matrix4x3d":
        ...


    def mapXnZY(self) -> "Matrix4x3d":
        """
        Multiply `this` by the matrix
        ```
        1  0 0 0
        0  0 1 0
        0 -1 0 0
        ```

        Returns
        - this
        """
        ...


    def mapXnZY(self, dest: "Matrix4x3d") -> "Matrix4x3d":
        ...


    def mapXnZnY(self) -> "Matrix4x3d":
        """
        Multiply `this` by the matrix
        ```
        1  0  0 0
        0  0 -1 0
        0 -1  0 0
        ```

        Returns
        - this
        """
        ...


    def mapXnZnY(self, dest: "Matrix4x3d") -> "Matrix4x3d":
        ...


    def mapYXZ(self) -> "Matrix4x3d":
        """
        Multiply `this` by the matrix
        ```
        0 1 0 0
        1 0 0 0
        0 0 1 0
        ```

        Returns
        - this
        """
        ...


    def mapYXZ(self, dest: "Matrix4x3d") -> "Matrix4x3d":
        ...


    def mapYXnZ(self) -> "Matrix4x3d":
        """
        Multiply `this` by the matrix
        ```
        0 1  0 0
        1 0  0 0
        0 0 -1 0
        ```

        Returns
        - this
        """
        ...


    def mapYXnZ(self, dest: "Matrix4x3d") -> "Matrix4x3d":
        ...


    def mapYZX(self) -> "Matrix4x3d":
        """
        Multiply `this` by the matrix
        ```
        0 0 1 0
        1 0 0 0
        0 1 0 0
        ```

        Returns
        - this
        """
        ...


    def mapYZX(self, dest: "Matrix4x3d") -> "Matrix4x3d":
        ...


    def mapYZnX(self) -> "Matrix4x3d":
        """
        Multiply `this` by the matrix
        ```
        0 0 -1 0
        1 0  0 0
        0 1  0 0
        ```

        Returns
        - this
        """
        ...


    def mapYZnX(self, dest: "Matrix4x3d") -> "Matrix4x3d":
        ...


    def mapYnXZ(self) -> "Matrix4x3d":
        """
        Multiply `this` by the matrix
        ```
        0 -1 0 0
        1  0 0 0
        0  0 1 0
        ```

        Returns
        - this
        """
        ...


    def mapYnXZ(self, dest: "Matrix4x3d") -> "Matrix4x3d":
        ...


    def mapYnXnZ(self) -> "Matrix4x3d":
        """
        Multiply `this` by the matrix
        ```
        0 -1  0 0
        1  0  0 0
        0  0 -1 0
        ```

        Returns
        - this
        """
        ...


    def mapYnXnZ(self, dest: "Matrix4x3d") -> "Matrix4x3d":
        ...


    def mapYnZX(self) -> "Matrix4x3d":
        """
        Multiply `this` by the matrix
        ```
        0  0 1 0
        1  0 0 0
        0 -1 0 0
        ```

        Returns
        - this
        """
        ...


    def mapYnZX(self, dest: "Matrix4x3d") -> "Matrix4x3d":
        ...


    def mapYnZnX(self) -> "Matrix4x3d":
        """
        Multiply `this` by the matrix
        ```
        0  0 -1 0
        1  0  0 0
        0 -1  0 0
        ```

        Returns
        - this
        """
        ...


    def mapYnZnX(self, dest: "Matrix4x3d") -> "Matrix4x3d":
        ...


    def mapZXY(self) -> "Matrix4x3d":
        """
        Multiply `this` by the matrix
        ```
        0 1 0 0
        0 0 1 0
        1 0 0 0
        ```

        Returns
        - this
        """
        ...


    def mapZXY(self, dest: "Matrix4x3d") -> "Matrix4x3d":
        ...


    def mapZXnY(self) -> "Matrix4x3d":
        """
        Multiply `this` by the matrix
        ```
        0 1  0 0
        0 0 -1 0
        1 0  0 0
        ```

        Returns
        - this
        """
        ...


    def mapZXnY(self, dest: "Matrix4x3d") -> "Matrix4x3d":
        ...


    def mapZYX(self) -> "Matrix4x3d":
        """
        Multiply `this` by the matrix
        ```
        0 0 1 0
        0 1 0 0
        1 0 0 0
        ```

        Returns
        - this
        """
        ...


    def mapZYX(self, dest: "Matrix4x3d") -> "Matrix4x3d":
        ...


    def mapZYnX(self) -> "Matrix4x3d":
        """
        Multiply `this` by the matrix
        ```
        0 0 -1 0
        0 1  0 0
        1 0  0 0
        ```

        Returns
        - this
        """
        ...


    def mapZYnX(self, dest: "Matrix4x3d") -> "Matrix4x3d":
        ...


    def mapZnXY(self) -> "Matrix4x3d":
        """
        Multiply `this` by the matrix
        ```
        0 -1 0 0
        0  0 1 0
        1  0 0 0
        ```

        Returns
        - this
        """
        ...


    def mapZnXY(self, dest: "Matrix4x3d") -> "Matrix4x3d":
        ...


    def mapZnXnY(self) -> "Matrix4x3d":
        """
        Multiply `this` by the matrix
        ```
        0 -1  0 0
        0  0 -1 0
        1  0  0 0
        ```

        Returns
        - this
        """
        ...


    def mapZnXnY(self, dest: "Matrix4x3d") -> "Matrix4x3d":
        ...


    def mapZnYX(self) -> "Matrix4x3d":
        """
        Multiply `this` by the matrix
        ```
        0  0 1 0
        0 -1 0 0
        1  0 0 0
        ```

        Returns
        - this
        """
        ...


    def mapZnYX(self, dest: "Matrix4x3d") -> "Matrix4x3d":
        ...


    def mapZnYnX(self) -> "Matrix4x3d":
        """
        Multiply `this` by the matrix
        ```
        0  0 -1 0
        0 -1  0 0
        1  0  0 0
        ```

        Returns
        - this
        """
        ...


    def mapZnYnX(self, dest: "Matrix4x3d") -> "Matrix4x3d":
        ...


    def mapnXYnZ(self) -> "Matrix4x3d":
        """
        Multiply `this` by the matrix
        ```
        -1 0  0 0
         0 1  0 0
         0 0 -1 0
        ```

        Returns
        - this
        """
        ...


    def mapnXYnZ(self, dest: "Matrix4x3d") -> "Matrix4x3d":
        ...


    def mapnXZY(self) -> "Matrix4x3d":
        """
        Multiply `this` by the matrix
        ```
        -1 0 0 0
         0 0 1 0
         0 1 0 0
        ```

        Returns
        - this
        """
        ...


    def mapnXZY(self, dest: "Matrix4x3d") -> "Matrix4x3d":
        ...


    def mapnXZnY(self) -> "Matrix4x3d":
        """
        Multiply `this` by the matrix
        ```
        -1 0  0 0
         0 0 -1 0
         0 1  0 0
        ```

        Returns
        - this
        """
        ...


    def mapnXZnY(self, dest: "Matrix4x3d") -> "Matrix4x3d":
        ...


    def mapnXnYZ(self) -> "Matrix4x3d":
        """
        Multiply `this` by the matrix
        ```
        -1  0 0 0
         0 -1 0 0
         0  0 1 0
        ```

        Returns
        - this
        """
        ...


    def mapnXnYZ(self, dest: "Matrix4x3d") -> "Matrix4x3d":
        ...


    def mapnXnYnZ(self) -> "Matrix4x3d":
        """
        Multiply `this` by the matrix
        ```
        -1  0  0 0
         0 -1  0 0
         0  0 -1 0
        ```

        Returns
        - this
        """
        ...


    def mapnXnYnZ(self, dest: "Matrix4x3d") -> "Matrix4x3d":
        ...


    def mapnXnZY(self) -> "Matrix4x3d":
        """
        Multiply `this` by the matrix
        ```
        -1  0 0 0
         0  0 1 0
         0 -1 0 0
        ```

        Returns
        - this
        """
        ...


    def mapnXnZY(self, dest: "Matrix4x3d") -> "Matrix4x3d":
        ...


    def mapnXnZnY(self) -> "Matrix4x3d":
        """
        Multiply `this` by the matrix
        ```
        -1  0  0 0
         0  0 -1 0
         0 -1  0 0
        ```

        Returns
        - this
        """
        ...


    def mapnXnZnY(self, dest: "Matrix4x3d") -> "Matrix4x3d":
        ...


    def mapnYXZ(self) -> "Matrix4x3d":
        """
        Multiply `this` by the matrix
        ```
         0 1 0 0
        -1 0 0 0
         0 0 1 0
        ```

        Returns
        - this
        """
        ...


    def mapnYXZ(self, dest: "Matrix4x3d") -> "Matrix4x3d":
        ...


    def mapnYXnZ(self) -> "Matrix4x3d":
        """
        Multiply `this` by the matrix
        ```
         0 1  0 0
        -1 0  0 0
         0 0 -1 0
        ```

        Returns
        - this
        """
        ...


    def mapnYXnZ(self, dest: "Matrix4x3d") -> "Matrix4x3d":
        ...


    def mapnYZX(self) -> "Matrix4x3d":
        """
        Multiply `this` by the matrix
        ```
         0 0 1 0
        -1 0 0 0
         0 1 0 0
        ```

        Returns
        - this
        """
        ...


    def mapnYZX(self, dest: "Matrix4x3d") -> "Matrix4x3d":
        ...


    def mapnYZnX(self) -> "Matrix4x3d":
        """
        Multiply `this` by the matrix
        ```
         0 0 -1 0
        -1 0  0 0
         0 1  0 0
        ```

        Returns
        - this
        """
        ...


    def mapnYZnX(self, dest: "Matrix4x3d") -> "Matrix4x3d":
        ...


    def mapnYnXZ(self) -> "Matrix4x3d":
        """
        Multiply `this` by the matrix
        ```
         0 -1 0 0
        -1  0 0 0
         0  0 1 0
        ```

        Returns
        - this
        """
        ...


    def mapnYnXZ(self, dest: "Matrix4x3d") -> "Matrix4x3d":
        ...


    def mapnYnXnZ(self) -> "Matrix4x3d":
        """
        Multiply `this` by the matrix
        ```
         0 -1  0 0
        -1  0  0 0
         0  0 -1 0
        ```

        Returns
        - this
        """
        ...


    def mapnYnXnZ(self, dest: "Matrix4x3d") -> "Matrix4x3d":
        ...


    def mapnYnZX(self) -> "Matrix4x3d":
        """
        Multiply `this` by the matrix
        ```
         0  0 1 0
        -1  0 0 0
         0 -1 0 0
        ```

        Returns
        - this
        """
        ...


    def mapnYnZX(self, dest: "Matrix4x3d") -> "Matrix4x3d":
        ...


    def mapnYnZnX(self) -> "Matrix4x3d":
        """
        Multiply `this` by the matrix
        ```
         0  0 -1 0
        -1  0  0 0
         0 -1  0 0
        ```

        Returns
        - this
        """
        ...


    def mapnYnZnX(self, dest: "Matrix4x3d") -> "Matrix4x3d":
        ...


    def mapnZXY(self) -> "Matrix4x3d":
        """
        Multiply `this` by the matrix
        ```
         0 1 0 0
         0 0 1 0
        -1 0 0 0
        ```

        Returns
        - this
        """
        ...


    def mapnZXY(self, dest: "Matrix4x3d") -> "Matrix4x3d":
        ...


    def mapnZXnY(self) -> "Matrix4x3d":
        """
        Multiply `this` by the matrix
        ```
         0 1  0 0
         0 0 -1 0
        -1 0  0 0
        ```

        Returns
        - this
        """
        ...


    def mapnZXnY(self, dest: "Matrix4x3d") -> "Matrix4x3d":
        ...


    def mapnZYX(self) -> "Matrix4x3d":
        """
        Multiply `this` by the matrix
        ```
         0 0 1 0
         0 1 0 0
        -1 0 0 0
        ```

        Returns
        - this
        """
        ...


    def mapnZYX(self, dest: "Matrix4x3d") -> "Matrix4x3d":
        ...


    def mapnZYnX(self) -> "Matrix4x3d":
        """
        Multiply `this` by the matrix
        ```
         0 0 -1 0
         0 1  0 0
        -1 0  0 0
        ```

        Returns
        - this
        """
        ...


    def mapnZYnX(self, dest: "Matrix4x3d") -> "Matrix4x3d":
        ...


    def mapnZnXY(self) -> "Matrix4x3d":
        """
        Multiply `this` by the matrix
        ```
         0 -1 0 0
         0  0 1 0
        -1  0 0 0
        ```

        Returns
        - this
        """
        ...


    def mapnZnXY(self, dest: "Matrix4x3d") -> "Matrix4x3d":
        ...


    def mapnZnXnY(self) -> "Matrix4x3d":
        """
        Multiply `this` by the matrix
        ```
         0 -1  0 0
         0  0 -1 0
        -1  0  0 0
        ```

        Returns
        - this
        """
        ...


    def mapnZnXnY(self, dest: "Matrix4x3d") -> "Matrix4x3d":
        ...


    def mapnZnYX(self) -> "Matrix4x3d":
        """
        Multiply `this` by the matrix
        ```
         0  0 1 0
         0 -1 0 0
        -1  0 0 0
        ```

        Returns
        - this
        """
        ...


    def mapnZnYX(self, dest: "Matrix4x3d") -> "Matrix4x3d":
        ...


    def mapnZnYnX(self) -> "Matrix4x3d":
        """
        Multiply `this` by the matrix
        ```
         0  0 -1 0
         0 -1  0 0
        -1  0  0 0
        ```

        Returns
        - this
        """
        ...


    def mapnZnYnX(self, dest: "Matrix4x3d") -> "Matrix4x3d":
        ...


    def negateX(self) -> "Matrix4x3d":
        """
        Multiply `this` by the matrix
        ```
        -1 0 0 0
         0 1 0 0
         0 0 1 0
        ```

        Returns
        - this
        """
        ...


    def negateX(self, dest: "Matrix4x3d") -> "Matrix4x3d":
        ...


    def negateY(self) -> "Matrix4x3d":
        """
        Multiply `this` by the matrix
        ```
        1  0 0 0
        0 -1 0 0
        0  0 1 0
        ```

        Returns
        - this
        """
        ...


    def negateY(self, dest: "Matrix4x3d") -> "Matrix4x3d":
        ...


    def negateZ(self) -> "Matrix4x3d":
        """
        Multiply `this` by the matrix
        ```
        1 0  0 0
        0 1  0 0
        0 0 -1 0
        ```

        Returns
        - this
        """
        ...


    def negateZ(self, dest: "Matrix4x3d") -> "Matrix4x3d":
        ...


    def isFinite(self) -> bool:
        ...


    def clone(self) -> "Object":
        ...
