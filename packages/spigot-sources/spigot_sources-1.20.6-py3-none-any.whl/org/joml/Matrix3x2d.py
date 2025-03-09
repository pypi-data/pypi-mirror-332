"""
Python module generated from Java source file org.joml.Matrix3x2d

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


class Matrix3x2d(Matrix3x2dc, Cloneable, Externalizable):
    """
    Contains the definition of a 3x2 matrix of doubles, and associated functions to transform
    it. The matrix is column-major to match OpenGL's interpretation, and it looks like this:
    
         m00  m10  m20
         m01  m11  m21

    Author(s)
    - Kai Burjack
    """

    def __init__(self):
        """
        Create a new Matrix3x2d and set it to .identity() identity.
        """
        ...


    def __init__(self, mat: "Matrix2dc"):
        """
        Create a new Matrix3x2d by setting its left 2x2 submatrix to the values of the given Matrix2dc
        and the rest to identity.

        Arguments
        - mat: the Matrix2dc
        """
        ...


    def __init__(self, mat: "Matrix2fc"):
        """
        Create a new Matrix3x2d by setting its left 2x2 submatrix to the values of the given Matrix2fc
        and the rest to identity.

        Arguments
        - mat: the Matrix2fc
        """
        ...


    def __init__(self, mat: "Matrix3x2dc"):
        """
        Create a new Matrix3x2d and make it a copy of the given matrix.

        Arguments
        - mat: the Matrix3x2dc to copy the values from
        """
        ...


    def __init__(self, m00: float, m01: float, m10: float, m11: float, m20: float, m21: float):
        """
        Create a new 3x2 matrix using the supplied double values. The order of the parameter is column-major, 
        so the first two parameters specify the two elements of the first column.

        Arguments
        - m00: the value of m00
        - m01: the value of m01
        - m10: the value of m10
        - m11: the value of m11
        - m20: the value of m20
        - m21: the value of m21
        """
        ...


    def __init__(self, buffer: "DoubleBuffer"):
        """
        Create a new Matrix3x2d by reading its 6 double components from the given DoubleBuffer
        at the buffer's current position.
        
        That DoubleBuffer is expected to hold the values in column-major order.
        
        The buffer's position will not be changed by this method.

        Arguments
        - buffer: the DoubleBuffer to read the matrix values from
        """
        ...


    def m00(self) -> float:
        ...


    def m01(self) -> float:
        ...


    def m10(self) -> float:
        ...


    def m11(self) -> float:
        ...


    def m20(self) -> float:
        ...


    def m21(self) -> float:
        ...


    def set(self, m: "Matrix3x2dc") -> "Matrix3x2d":
        """
        Set the elements of this matrix to the ones in `m`.

        Arguments
        - m: the matrix to copy the elements from

        Returns
        - this
        """
        ...


    def set(self, m: "Matrix2dc") -> "Matrix3x2d":
        """
        Set the left 2x2 submatrix of this Matrix3x2d to the given Matrix2dc and don't change the other elements.

        Arguments
        - m: the 2x2 matrix

        Returns
        - this
        """
        ...


    def set(self, m: "Matrix2fc") -> "Matrix3x2d":
        """
        Set the left 2x2 submatrix of this Matrix3x2d to the given Matrix2fc and don't change the other elements.

        Arguments
        - m: the 2x2 matrix

        Returns
        - this
        """
        ...


    def mul(self, right: "Matrix3x2dc") -> "Matrix3x2d":
        """
        Multiply this matrix by the supplied `right` matrix by assuming a third row in
        both matrices of `(0, 0, 1)`.
        
        If `M` is `this` matrix and `R` the `right` matrix,
        then the new matrix will be `M * R`. So when transforming a
        vector `v` with the new matrix by using `M * R * v`, the
        transformation of the right matrix will be applied first!

        Arguments
        - right: the right operand of the matrix multiplication

        Returns
        - this
        """
        ...


    def mul(self, right: "Matrix3x2dc", dest: "Matrix3x2d") -> "Matrix3x2d":
        """
        Multiply this matrix by the supplied `right` matrix by assuming a third row in
        both matrices of `(0, 0, 1)` and store the result in `dest`.
        
        If `M` is `this` matrix and `R` the `right` matrix,
        then the new matrix will be `M * R`. So when transforming a
        vector `v` with the new matrix by using `M * R * v`, the
        transformation of the right matrix will be applied first!

        Arguments
        - right: the right operand of the matrix multiplication
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mulLocal(self, left: "Matrix3x2dc") -> "Matrix3x2d":
        """
        Pre-multiply this matrix by the supplied `left` matrix and store the result in `this`.
        
        If `M` is `this` matrix and `L` the `left` matrix,
        then the new matrix will be `L * M`. So when transforming a
        vector `v` with the new matrix by using `L * M * v`, the
        transformation of `this` matrix will be applied first!

        Arguments
        - left: the left operand of the matrix multiplication

        Returns
        - this
        """
        ...


    def mulLocal(self, left: "Matrix3x2dc", dest: "Matrix3x2d") -> "Matrix3x2d":
        ...


    def set(self, m00: float, m01: float, m10: float, m11: float, m20: float, m21: float) -> "Matrix3x2d":
        """
        Set the values within this matrix to the supplied double values. The result looks like this:
        
        m00, m10, m20
        m01, m11, m21

        Arguments
        - m00: the new value of m00
        - m01: the new value of m01
        - m10: the new value of m10
        - m11: the new value of m11
        - m20: the new value of m20
        - m21: the new value of m21

        Returns
        - this
        """
        ...


    def set(self, m: list[float]) -> "Matrix3x2d":
        """
        Set the values in this matrix based on the supplied double array. The result looks like this:
        
        0, 2, 4
        1, 3, 5
        
        This method only uses the first 6 values, all others are ignored.

        Arguments
        - m: the array to read the matrix values from

        Returns
        - this
        """
        ...


    def determinant(self) -> float:
        """
        Return the determinant of this matrix.

        Returns
        - the determinant
        """
        ...


    def invert(self) -> "Matrix3x2d":
        """
        Invert this matrix by assuming a third row in this matrix of `(0, 0, 1)`.

        Returns
        - this
        """
        ...


    def invert(self, dest: "Matrix3x2d") -> "Matrix3x2d":
        """
        Invert the `this` matrix by assuming a third row in this matrix of `(0, 0, 1)`
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def translation(self, x: float, y: float) -> "Matrix3x2d":
        """
        Set this matrix to be a simple translation matrix in a two-dimensional coordinate system.
        
        The resulting matrix can be multiplied against another transformation
        matrix to obtain an additional translation.
        
        In order to apply a translation via to an already existing transformation
        matrix, use .translate(double, double) translate() instead.

        Arguments
        - x: the units to translate in x
        - y: the units to translate in y

        Returns
        - this

        See
        - .translate(double, double)
        """
        ...


    def translation(self, offset: "Vector2dc") -> "Matrix3x2d":
        """
        Set this matrix to be a simple translation matrix in a two-dimensional coordinate system.
        
        The resulting matrix can be multiplied against another transformation
        matrix to obtain an additional translation.
        
        In order to apply a translation via to an already existing transformation
        matrix, use .translate(Vector2dc) translate() instead.

        Arguments
        - offset: the translation

        Returns
        - this

        See
        - .translate(Vector2dc)
        """
        ...


    def setTranslation(self, x: float, y: float) -> "Matrix3x2d":
        """
        Set only the translation components of this matrix `(m20, m21)` to the given values `(x, y)`.
        
        To build a translation matrix instead, use .translation(double, double).
        To apply a translation to another matrix, use .translate(double, double).

        Arguments
        - x: the offset to translate in x
        - y: the offset to translate in y

        Returns
        - this

        See
        - .translate(double, double)
        """
        ...


    def setTranslation(self, offset: "Vector2dc") -> "Matrix3x2d":
        """
        Set only the translation components of this matrix `(m20, m21)` to the given values `(offset.x, offset.y)`.
        
        To build a translation matrix instead, use .translation(Vector2dc).
        To apply a translation to another matrix, use .translate(Vector2dc).

        Arguments
        - offset: the new translation to set

        Returns
        - this

        See
        - .translate(Vector2dc)
        """
        ...


    def translate(self, x: float, y: float, dest: "Matrix3x2d") -> "Matrix3x2d":
        """
        Apply a translation to this matrix by translating by the given number of units in x and y and store the result
        in `dest`.
        
        If `M` is `this` matrix and `T` the translation
        matrix, then the new matrix will be `M * T`. So when
        transforming a vector `v` with the new matrix by using
        `M * T * v`, the translation will be applied first!
        
        In order to set the matrix to a translation transformation without post-multiplying
        it, use .translation(double, double).

        Arguments
        - x: the offset to translate in x
        - y: the offset to translate in y
        - dest: will hold the result

        Returns
        - dest

        See
        - .translation(double, double)
        """
        ...


    def translate(self, x: float, y: float) -> "Matrix3x2d":
        """
        Apply a translation to this matrix by translating by the given number of units in x and y.
        
        If `M` is `this` matrix and `T` the translation
        matrix, then the new matrix will be `M * T`. So when
        transforming a vector `v` with the new matrix by using
        `M * T * v`, the translation will be applied first!
        
        In order to set the matrix to a translation transformation without post-multiplying
        it, use .translation(double, double).

        Arguments
        - x: the offset to translate in x
        - y: the offset to translate in y

        Returns
        - this

        See
        - .translation(double, double)
        """
        ...


    def translate(self, offset: "Vector2dc", dest: "Matrix3x2d") -> "Matrix3x2d":
        """
        Apply a translation to this matrix by translating by the given number of units in x and y, and
        store the result in `dest`.
        
        If `M` is `this` matrix and `T` the translation
        matrix, then the new matrix will be `M * T`. So when
        transforming a vector `v` with the new matrix by using
        `M * T * v`, the translation will be applied first!
        
        In order to set the matrix to a translation transformation without post-multiplying
        it, use .translation(Vector2dc).

        Arguments
        - offset: the offset to translate
        - dest: will hold the result

        Returns
        - dest

        See
        - .translation(Vector2dc)
        """
        ...


    def translate(self, offset: "Vector2dc") -> "Matrix3x2d":
        """
        Apply a translation to this matrix by translating by the given number of units in x and y.
        
        If `M` is `this` matrix and `T` the translation
        matrix, then the new matrix will be `M * T`. So when
        transforming a vector `v` with the new matrix by using
        `M * T * v`, the translation will be applied first!
        
        In order to set the matrix to a translation transformation without post-multiplying
        it, use .translation(Vector2dc).

        Arguments
        - offset: the offset to translate

        Returns
        - this

        See
        - .translation(Vector2dc)
        """
        ...


    def translateLocal(self, offset: "Vector2dc") -> "Matrix3x2d":
        """
        Pre-multiply a translation to this matrix by translating by the given number of
        units in x and y.
        
        If `M` is `this` matrix and `T` the translation
        matrix, then the new matrix will be `T * M`. So when
        transforming a vector `v` with the new matrix by using
        `T * M * v`, the translation will be applied last!
        
        In order to set the matrix to a translation transformation without pre-multiplying
        it, use .translation(Vector2dc).

        Arguments
        - offset: the number of units in x and y by which to translate

        Returns
        - this

        See
        - .translation(Vector2dc)
        """
        ...


    def translateLocal(self, offset: "Vector2dc", dest: "Matrix3x2d") -> "Matrix3x2d":
        """
        Pre-multiply a translation to this matrix by translating by the given number of
        units in x and y and store the result in `dest`.
        
        If `M` is `this` matrix and `T` the translation
        matrix, then the new matrix will be `T * M`. So when
        transforming a vector `v` with the new matrix by using
        `T * M * v`, the translation will be applied last!
        
        In order to set the matrix to a translation transformation without pre-multiplying
        it, use .translation(Vector2dc).

        Arguments
        - offset: the number of units in x and y by which to translate
        - dest: will hold the result

        Returns
        - dest

        See
        - .translation(Vector2dc)
        """
        ...


    def translateLocal(self, x: float, y: float, dest: "Matrix3x2d") -> "Matrix3x2d":
        """
        Pre-multiply a translation to this matrix by translating by the given number of
        units in x and y and store the result in `dest`.
        
        If `M` is `this` matrix and `T` the translation
        matrix, then the new matrix will be `T * M`. So when
        transforming a vector `v` with the new matrix by using
        `T * M * v`, the translation will be applied last!
        
        In order to set the matrix to a translation transformation without pre-multiplying
        it, use .translation(double, double).

        Arguments
        - x: the offset to translate in x
        - y: the offset to translate in y
        - dest: will hold the result

        Returns
        - dest

        See
        - .translation(double, double)
        """
        ...


    def translateLocal(self, x: float, y: float) -> "Matrix3x2d":
        """
        Pre-multiply a translation to this matrix by translating by the given number of
        units in x and y.
        
        If `M` is `this` matrix and `T` the translation
        matrix, then the new matrix will be `T * M`. So when
        transforming a vector `v` with the new matrix by using
        `T * M * v`, the translation will be applied last!
        
        In order to set the matrix to a translation transformation without pre-multiplying
        it, use .translation(double, double).

        Arguments
        - x: the offset to translate in x
        - y: the offset to translate in y

        Returns
        - this

        See
        - .translation(double, double)
        """
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


    def get(self, dest: "Matrix3x2d") -> "Matrix3x2d":
        """
        Get the current values of `this` matrix and store them into
        `dest`.
        
        This is the reverse method of .set(Matrix3x2dc) and allows to obtain
        intermediate calculation results when chaining multiple transformations.

        Arguments
        - dest: the destination matrix

        Returns
        - dest

        See
        - .set(Matrix3x2dc)
        """
        ...


    def get(self, buffer: "DoubleBuffer") -> "DoubleBuffer":
        """
        Store this matrix in column-major order into the supplied DoubleBuffer at the current
        buffer DoubleBuffer.position() position.
        
        This method will not increment the position of the given DoubleBuffer.
        
        In order to specify the offset into the DoubleBuffer at which
        the matrix is stored, use .get(int, DoubleBuffer), taking
        the absolute position as parameter.

        Arguments
        - buffer: will receive the values of this matrix in column-major order at its current position

        Returns
        - the passed in buffer

        See
        - .get(int, DoubleBuffer)
        """
        ...


    def get(self, index: int, buffer: "DoubleBuffer") -> "DoubleBuffer":
        """
        Store this matrix in column-major order into the supplied DoubleBuffer starting at the specified
        absolute buffer position/index.
        
        This method will not increment the position of the given DoubleBuffer.

        Arguments
        - index: the absolute position into the DoubleBuffer
        - buffer: will receive the values of this matrix in column-major order

        Returns
        - the passed in buffer
        """
        ...


    def get(self, buffer: "ByteBuffer") -> "ByteBuffer":
        """
        Store this matrix in column-major order into the supplied ByteBuffer at the current
        buffer ByteBuffer.position() position.
        
        This method will not increment the position of the given ByteBuffer.
        
        In order to specify the offset into the ByteBuffer at which
        the matrix is stored, use .get(int, ByteBuffer), taking
        the absolute position as parameter.

        Arguments
        - buffer: will receive the values of this matrix in column-major order at its current position

        Returns
        - the passed in buffer

        See
        - .get(int, ByteBuffer)
        """
        ...


    def get(self, index: int, buffer: "ByteBuffer") -> "ByteBuffer":
        """
        Store this matrix in column-major order into the supplied ByteBuffer starting at the specified
        absolute buffer position/index.
        
        This method will not increment the position of the given ByteBuffer.

        Arguments
        - index: the absolute position into the ByteBuffer
        - buffer: will receive the values of this matrix in column-major order

        Returns
        - the passed in buffer
        """
        ...


    def get3x3(self, buffer: "DoubleBuffer") -> "DoubleBuffer":
        """
        Store this matrix as an equivalent 4x4 matrix in column-major order into the supplied DoubleBuffer at the current
        buffer DoubleBuffer.position() position.
        
        This method will not increment the position of the given DoubleBuffer.
        
        In order to specify the offset into the DoubleBuffer at which
        the matrix is stored, use .get3x3(int, DoubleBuffer), taking
        the absolute position as parameter.

        Arguments
        - buffer: will receive the values of this matrix in column-major order at its current position

        Returns
        - the passed in buffer

        See
        - .get3x3(int, DoubleBuffer)
        """
        ...


    def get3x3(self, index: int, buffer: "DoubleBuffer") -> "DoubleBuffer":
        """
        Store this matrix as an equivalent 3x3 matrix in column-major order into the supplied DoubleBuffer starting at the specified
        absolute buffer position/index.
        
        This method will not increment the position of the given DoubleBuffer.

        Arguments
        - index: the absolute position into the DoubleBuffer
        - buffer: will receive the values of this matrix in column-major order

        Returns
        - the passed in buffer
        """
        ...


    def get3x3(self, buffer: "ByteBuffer") -> "ByteBuffer":
        """
        Store this matrix as an equivalent 3x3 matrix in column-major order into the supplied ByteBuffer at the current
        buffer ByteBuffer.position() position.
        
        This method will not increment the position of the given ByteBuffer.
        
        In order to specify the offset into the ByteBuffer at which
        the matrix is stored, use .get3x3(int, ByteBuffer), taking
        the absolute position as parameter.

        Arguments
        - buffer: will receive the values of this matrix in column-major order at its current position

        Returns
        - the passed in buffer

        See
        - .get3x3(int, ByteBuffer)
        """
        ...


    def get3x3(self, index: int, buffer: "ByteBuffer") -> "ByteBuffer":
        """
        Store this matrix as an equivalent 3x3 matrix in column-major order into the supplied ByteBuffer starting at the specified
        absolute buffer position/index.
        
        This method will not increment the position of the given ByteBuffer.

        Arguments
        - index: the absolute position into the ByteBuffer
        - buffer: will receive the values of this matrix in column-major order

        Returns
        - the passed in buffer
        """
        ...


    def get4x4(self, buffer: "DoubleBuffer") -> "DoubleBuffer":
        """
        Store this matrix as an equivalent 4x4 matrix in column-major order into the supplied DoubleBuffer at the current
        buffer DoubleBuffer.position() position.
        
        This method will not increment the position of the given DoubleBuffer.
        
        In order to specify the offset into the DoubleBuffer at which
        the matrix is stored, use .get4x4(int, DoubleBuffer), taking
        the absolute position as parameter.

        Arguments
        - buffer: will receive the values of this matrix in column-major order at its current position

        Returns
        - the passed in buffer

        See
        - .get4x4(int, DoubleBuffer)
        """
        ...


    def get4x4(self, index: int, buffer: "DoubleBuffer") -> "DoubleBuffer":
        """
        Store this matrix as an equivalent 4x4 matrix in column-major order into the supplied DoubleBuffer starting at the specified
        absolute buffer position/index.
        
        This method will not increment the position of the given DoubleBuffer.

        Arguments
        - index: the absolute position into the DoubleBuffer
        - buffer: will receive the values of this matrix in column-major order

        Returns
        - the passed in buffer
        """
        ...


    def get4x4(self, buffer: "ByteBuffer") -> "ByteBuffer":
        """
        Store this matrix as an equivalent 4x4 matrix in column-major order into the supplied ByteBuffer at the current
        buffer ByteBuffer.position() position.
        
        This method will not increment the position of the given ByteBuffer.
        
        In order to specify the offset into the ByteBuffer at which
        the matrix is stored, use .get4x4(int, ByteBuffer), taking
        the absolute position as parameter.

        Arguments
        - buffer: will receive the values of this matrix in column-major order at its current position

        Returns
        - the passed in buffer

        See
        - .get4x4(int, ByteBuffer)
        """
        ...


    def get4x4(self, index: int, buffer: "ByteBuffer") -> "ByteBuffer":
        """
        Store this matrix as an equivalent 4x4 matrix in column-major order into the supplied ByteBuffer starting at the specified
        absolute buffer position/index.
        
        This method will not increment the position of the given ByteBuffer.

        Arguments
        - index: the absolute position into the ByteBuffer
        - buffer: will receive the values of this matrix in column-major order

        Returns
        - the passed in buffer
        """
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


    def getToAddress(self, address: int) -> "Matrix3x2dc":
        ...


    def get(self, arr: list[float], offset: int) -> list[float]:
        """
        Store this matrix into the supplied double array in column-major order at the given offset.

        Arguments
        - arr: the array to write the matrix values into
        - offset: the offset into the array

        Returns
        - the passed in array
        """
        ...


    def get(self, arr: list[float]) -> list[float]:
        """
        Store this matrix into the supplied double array in column-major order.
        
        In order to specify an explicit offset into the array, use the method .get(double[], int).

        Arguments
        - arr: the array to write the matrix values into

        Returns
        - the passed in array

        See
        - .get(double[], int)
        """
        ...


    def get3x3(self, arr: list[float], offset: int) -> list[float]:
        """
        Store this matrix as an equivalent 3x3 matrix in column-major order into the supplied float array at the given offset.

        Arguments
        - arr: the array to write the matrix values into
        - offset: the offset into the array

        Returns
        - the passed in array
        """
        ...


    def get3x3(self, arr: list[float]) -> list[float]:
        """
        Store this matrix as an equivalent 3x3 matrix in column-major order into the supplied float array.
        
        In order to specify an explicit offset into the array, use the method .get3x3(double[], int).

        Arguments
        - arr: the array to write the matrix values into

        Returns
        - the passed in array

        See
        - .get3x3(double[], int)
        """
        ...


    def get4x4(self, arr: list[float], offset: int) -> list[float]:
        """
        Store this matrix as an equivalent 4x4 matrix in column-major order into the supplied float array at the given offset.

        Arguments
        - arr: the array to write the matrix values into
        - offset: the offset into the array

        Returns
        - the passed in array
        """
        ...


    def get4x4(self, arr: list[float]) -> list[float]:
        """
        Store this matrix as an equivalent 4x4 matrix in column-major order into the supplied float array.
        
        In order to specify an explicit offset into the array, use the method .get4x4(double[], int).

        Arguments
        - arr: the array to write the matrix values into

        Returns
        - the passed in array

        See
        - .get4x4(double[], int)
        """
        ...


    def set(self, buffer: "DoubleBuffer") -> "Matrix3x2d":
        """
        Set the values of this matrix by reading 6 double values from the given DoubleBuffer in column-major order,
        starting at its current position.
        
        The DoubleBuffer is expected to contain the values in column-major order.
        
        The position of the DoubleBuffer will not be changed by this method.

        Arguments
        - buffer: the DoubleBuffer to read the matrix values from in column-major order

        Returns
        - this
        """
        ...


    def set(self, buffer: "ByteBuffer") -> "Matrix3x2d":
        """
        Set the values of this matrix by reading 6 double values from the given ByteBuffer in column-major order,
        starting at its current position.
        
        The ByteBuffer is expected to contain the values in column-major order.
        
        The position of the ByteBuffer will not be changed by this method.

        Arguments
        - buffer: the ByteBuffer to read the matrix values from in column-major order

        Returns
        - this
        """
        ...


    def set(self, index: int, buffer: "DoubleBuffer") -> "Matrix3x2d":
        """
        Set the values of this matrix by reading 6 double values from the given DoubleBuffer in column-major order,
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


    def set(self, index: int, buffer: "ByteBuffer") -> "Matrix3x2d":
        """
        Set the values of this matrix by reading 6 double values from the given ByteBuffer in column-major order,
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


    def setFromAddress(self, address: int) -> "Matrix3x2d":
        """
        Set the values of this matrix by reading 6 double values from off-heap memory in column-major order,
        starting at the given address.
        
        This method will throw an UnsupportedOperationException when JOML is used with `-Djoml.nounsafe`.
        
        *This method is unsafe as it can result in a crash of the JVM process when the specified address range does not belong to this process.*

        Arguments
        - address: the off-heap memory address to read the matrix values from in column-major order

        Returns
        - this
        """
        ...


    def zero(self) -> "Matrix3x2d":
        """
        Set all values within this matrix to zero.

        Returns
        - this
        """
        ...


    def identity(self) -> "Matrix3x2d":
        """
        Set this matrix to the identity.

        Returns
        - this
        """
        ...


    def scale(self, x: float, y: float, dest: "Matrix3x2d") -> "Matrix3x2d":
        """
        Apply scaling to this matrix by scaling the unit axes by the given x and y and store the result in `dest`.
        
        If `M` is `this` matrix and `S` the scaling matrix,
        then the new matrix will be `M * S`. So when transforming a
        vector `v` with the new matrix by using `M * S * v`, the scaling will be applied first!

        Arguments
        - x: the factor of the x component
        - y: the factor of the y component
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def scale(self, x: float, y: float) -> "Matrix3x2d":
        """
        Apply scaling to this matrix by scaling the base axes by the given x and y factors.
        
        If `M` is `this` matrix and `S` the scaling matrix,
        then the new matrix will be `M * S`. So when transforming a
        vector `v` with the new matrix by using `M * S * v`, the scaling will be applied first!

        Arguments
        - x: the factor of the x component
        - y: the factor of the y component

        Returns
        - this
        """
        ...


    def scale(self, xy: "Vector2dc") -> "Matrix3x2d":
        """
        Apply scaling to this matrix by scaling the base axes by the given `xy` factors.
        
        If `M` is `this` matrix and `S` the scaling matrix,
        then the new matrix will be `M * S`. So when transforming a
        vector `v` with the new matrix by using `M * S * v`, the scaling will be applied first!

        Arguments
        - xy: the factors of the x and y component, respectively

        Returns
        - this
        """
        ...


    def scale(self, xy: "Vector2dc", dest: "Matrix3x2d") -> "Matrix3x2d":
        """
        Apply scaling to this matrix by scaling the base axes by the given `xy` factors
        and store the result in `dest`.
        
        If `M` is `this` matrix and `S` the scaling matrix,
        then the new matrix will be `M * S`. So when transforming a
        vector `v` with the new matrix by using `M * S * v`, the scaling will be applied first!

        Arguments
        - xy: the factors of the x and y component, respectively
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def scale(self, xy: "Vector2fc") -> "Matrix3x2d":
        """
        Apply scaling to this matrix by scaling the base axes by the given `xy` factors.
        
        If `M` is `this` matrix and `S` the scaling matrix,
        then the new matrix will be `M * S`. So when transforming a
        vector `v` with the new matrix by using `M * S * v`, the scaling will be applied first!

        Arguments
        - xy: the factors of the x and y component, respectively

        Returns
        - this
        """
        ...


    def scale(self, xy: "Vector2fc", dest: "Matrix3x2d") -> "Matrix3x2d":
        """
        Apply scaling to this matrix by scaling the base axes by the given `xy` factors
        and store the result in `dest`.
        
        If `M` is `this` matrix and `S` the scaling matrix,
        then the new matrix will be `M * S`. So when transforming a
        vector `v` with the new matrix by using `M * S * v`, the scaling will be applied first!

        Arguments
        - xy: the factors of the x and y component, respectively
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def scale(self, xy: float, dest: "Matrix3x2d") -> "Matrix3x2d":
        """
        Apply scaling to this matrix by uniformly scaling the two base axes by the given `xy` factor
        and store the result in `dest`.
        
        If `M` is `this` matrix and `S` the scaling matrix,
        then the new matrix will be `M * S`. So when transforming a
        vector `v` with the new matrix by using `M * S * v`, the scaling will be applied first!

        Arguments
        - xy: the factor for the two components
        - dest: will hold the result

        Returns
        - dest

        See
        - .scale(double, double, Matrix3x2d)
        """
        ...


    def scale(self, xy: float) -> "Matrix3x2d":
        """
        Apply scaling to this matrix by uniformly scaling the two base axes by the given `xyz` factor.
        
        If `M` is `this` matrix and `S` the scaling matrix,
        then the new matrix will be `M * S`. So when transforming a
        vector `v` with the new matrix by using `M * S * v`, the scaling will be applied first!

        Arguments
        - xy: the factor for the two components

        Returns
        - this

        See
        - .scale(double, double)
        """
        ...


    def scaleLocal(self, x: float, y: float, dest: "Matrix3x2d") -> "Matrix3x2d":
        ...


    def scaleLocal(self, x: float, y: float) -> "Matrix3x2d":
        """
        Pre-multiply scaling to this matrix by scaling the base axes by the given x and y factors.
        
        If `M` is `this` matrix and `S` the scaling matrix,
        then the new matrix will be `S * M`. So when transforming a
        vector `v` with the new matrix by using `S * M * v`, the
        scaling will be applied last!

        Arguments
        - x: the factor of the x component
        - y: the factor of the y component

        Returns
        - this
        """
        ...


    def scaleLocal(self, xy: float, dest: "Matrix3x2d") -> "Matrix3x2d":
        ...


    def scaleLocal(self, xy: float) -> "Matrix3x2d":
        """
        Pre-multiply scaling to this matrix by scaling the base axes by the given xy factor.
        
        If `M` is `this` matrix and `S` the scaling matrix,
        then the new matrix will be `S * M`. So when transforming a
        vector `v` with the new matrix by using `S * M * v`, the
        scaling will be applied last!

        Arguments
        - xy: the factor of the x and y component

        Returns
        - this
        """
        ...


    def scaleAround(self, sx: float, sy: float, ox: float, oy: float, dest: "Matrix3x2d") -> "Matrix3x2d":
        """
        Apply scaling to `this` matrix by scaling the base axes by the given sx and
        sy factors while using `(ox, oy)` as the scaling origin, and store the result in `dest`.
        
        If `M` is `this` matrix and `S` the scaling matrix,
        then the new matrix will be `M * S`. So when transforming a
        vector `v` with the new matrix by using `M * S * v`
        , the scaling will be applied first!
        
        This method is equivalent to calling: `translate(ox, oy, dest).scale(sx, sy).translate(-ox, -oy)`

        Arguments
        - sx: the scaling factor of the x component
        - sy: the scaling factor of the y component
        - ox: the x coordinate of the scaling origin
        - oy: the y coordinate of the scaling origin
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def scaleAround(self, sx: float, sy: float, ox: float, oy: float) -> "Matrix3x2d":
        """
        Apply scaling to this matrix by scaling the base axes by the given sx and
        sy factors while using `(ox, oy)` as the scaling origin.
        
        If `M` is `this` matrix and `S` the scaling matrix,
        then the new matrix will be `M * S`. So when transforming a
        vector `v` with the new matrix by using `M * S * v`, the
        scaling will be applied first!
        
        This method is equivalent to calling: `translate(ox, oy).scale(sx, sy).translate(-ox, -oy)`

        Arguments
        - sx: the scaling factor of the x component
        - sy: the scaling factor of the y component
        - ox: the x coordinate of the scaling origin
        - oy: the y coordinate of the scaling origin

        Returns
        - this
        """
        ...


    def scaleAround(self, factor: float, ox: float, oy: float, dest: "Matrix3x2d") -> "Matrix3x2d":
        """
        Apply scaling to this matrix by scaling the base axes by the given `factor`
        while using `(ox, oy)` as the scaling origin,
        and store the result in `dest`.
        
        If `M` is `this` matrix and `S` the scaling matrix,
        then the new matrix will be `M * S`. So when transforming a
        vector `v` with the new matrix by using `M * S * v`, the
        scaling will be applied first!
        
        This method is equivalent to calling: `translate(ox, oy, dest).scale(factor).translate(-ox, -oy)`

        Arguments
        - factor: the scaling factor for all three axes
        - ox: the x coordinate of the scaling origin
        - oy: the y coordinate of the scaling origin
        - dest: will hold the result

        Returns
        - this
        """
        ...


    def scaleAround(self, factor: float, ox: float, oy: float) -> "Matrix3x2d":
        """
        Apply scaling to this matrix by scaling the base axes by the given `factor`
        while using `(ox, oy)` as the scaling origin.
        
        If `M` is `this` matrix and `S` the scaling matrix,
        then the new matrix will be `M * S`. So when transforming a
        vector `v` with the new matrix by using `M * S * v`, the
        scaling will be applied first!
        
        This method is equivalent to calling: `translate(ox, oy).scale(factor).translate(-ox, -oy)`

        Arguments
        - factor: the scaling factor for all axes
        - ox: the x coordinate of the scaling origin
        - oy: the y coordinate of the scaling origin

        Returns
        - this
        """
        ...


    def scaleAroundLocal(self, sx: float, sy: float, ox: float, oy: float, dest: "Matrix3x2d") -> "Matrix3x2d":
        ...


    def scaleAroundLocal(self, factor: float, ox: float, oy: float, dest: "Matrix3x2d") -> "Matrix3x2d":
        ...


    def scaleAroundLocal(self, sx: float, sy: float, sz: float, ox: float, oy: float, oz: float) -> "Matrix3x2d":
        """
        Pre-multiply scaling to this matrix by scaling the base axes by the given sx and
        sy factors while using `(ox, oy)` as the scaling origin.
        
        If `M` is `this` matrix and `S` the scaling matrix,
        then the new matrix will be `S * M`. So when transforming a
        vector `v` with the new matrix by using `S * M * v`, the
        scaling will be applied last!
        
        This method is equivalent to calling: `new Matrix3x2d().translate(ox, oy).scale(sx, sy).translate(-ox, -oy).mul(this, this)`

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


    def scaleAroundLocal(self, factor: float, ox: float, oy: float) -> "Matrix3x2d":
        """
        Pre-multiply scaling to this matrix by scaling the base axes by the given `factor`
        while using `(ox, oy)` as the scaling origin.
        
        If `M` is `this` matrix and `S` the scaling matrix,
        then the new matrix will be `S * M`. So when transforming a
        vector `v` with the new matrix by using `S * M * v`, the
        scaling will be applied last!
        
        This method is equivalent to calling: `new Matrix3x2d().translate(ox, oy).scale(factor).translate(-ox, -oy).mul(this, this)`

        Arguments
        - factor: the scaling factor for all three axes
        - ox: the x coordinate of the scaling origin
        - oy: the y coordinate of the scaling origin

        Returns
        - this
        """
        ...


    def scaling(self, factor: float) -> "Matrix3x2d":
        """
        Set this matrix to be a simple scale matrix, which scales the two base axes uniformly by the given factor.
        
        The resulting matrix can be multiplied against another transformation
        matrix to obtain an additional scaling.
        
        In order to post-multiply a scaling transformation directly to a matrix, use .scale(double) scale() instead.

        Arguments
        - factor: the scale factor in x and y

        Returns
        - this

        See
        - .scale(double)
        """
        ...


    def scaling(self, x: float, y: float) -> "Matrix3x2d":
        """
        Set this matrix to be a simple scale matrix.

        Arguments
        - x: the scale in x
        - y: the scale in y

        Returns
        - this
        """
        ...


    def rotation(self, angle: float) -> "Matrix3x2d":
        """
        Set this matrix to a rotation matrix which rotates the given radians.
        
        The resulting matrix can be multiplied against another transformation
        matrix to obtain an additional rotation.
        
        In order to apply the rotation transformation to an existing transformation,
        use .rotate(double) rotate() instead.

        Arguments
        - angle: the angle in radians

        Returns
        - this

        See
        - .rotate(double)
        """
        ...


    def transform(self, v: "Vector3d") -> "Vector3d":
        """
        Transform/multiply the given vector by this matrix by assuming a third row in this matrix of `(0, 0, 1)`
        and store the result in that vector.

        Arguments
        - v: the vector to transform and to hold the final result

        Returns
        - v

        See
        - Vector3d.mul(Matrix3x2dc)
        """
        ...


    def transform(self, v: "Vector3dc", dest: "Vector3d") -> "Vector3d":
        """
        Transform/multiply the given vector by this matrix by assuming a third row in this matrix of `(0, 0, 1)`
        and store the result in `dest`.

        Arguments
        - v: the vector to transform
        - dest: will contain the result

        Returns
        - dest

        See
        - Vector3d.mul(Matrix3x2dc, Vector3d)
        """
        ...


    def transform(self, x: float, y: float, z: float, dest: "Vector3d") -> "Vector3d":
        """
        Transform/multiply the given vector `(x, y, z)` by this matrix and store the result in `dest`.

        Arguments
        - x: the x component of the vector to transform
        - y: the y component of the vector to transform
        - z: the z component of the vector to transform
        - dest: will contain the result

        Returns
        - dest
        """
        ...


    def transformPosition(self, v: "Vector2d") -> "Vector2d":
        """
        Transform/multiply the given 2D-vector, as if it was a 3D-vector with z=1, by
        this matrix and store the result in that vector.
        
        The given 2D-vector is treated as a 3D-vector with its z-component being 1.0, so it
        will represent a position/location in 2D-space rather than a direction.
        
        In order to store the result in another vector, use .transformPosition(Vector2dc, Vector2d).

        Arguments
        - v: the vector to transform and to hold the final result

        Returns
        - v

        See
        - .transform(Vector3d)
        """
        ...


    def transformPosition(self, v: "Vector2dc", dest: "Vector2d") -> "Vector2d":
        """
        Transform/multiply the given 2D-vector, as if it was a 3D-vector with z=1, by
        this matrix and store the result in `dest`.
        
        The given 2D-vector is treated as a 3D-vector with its z-component being 1.0, so it
        will represent a position/location in 2D-space rather than a direction.
        
        In order to store the result in the same vector, use .transformPosition(Vector2d).

        Arguments
        - v: the vector to transform
        - dest: will hold the result

        Returns
        - dest

        See
        - .transform(Vector3dc, Vector3d)
        """
        ...


    def transformPosition(self, x: float, y: float, dest: "Vector2d") -> "Vector2d":
        """
        Transform/multiply the given 2D-vector `(x, y)`, as if it was a 3D-vector with z=1, by
        this matrix and store the result in `dest`.
        
        The given 2D-vector is treated as a 3D-vector with its z-component being 1.0, so it
        will represent a position/location in 2D-space rather than a direction.
        
        In order to store the result in the same vector, use .transformPosition(Vector2d).

        Arguments
        - x: the x component of the vector to transform
        - y: the y component of the vector to transform
        - dest: will hold the result

        Returns
        - dest

        See
        - .transform(Vector3dc, Vector3d)
        """
        ...


    def transformDirection(self, v: "Vector2d") -> "Vector2d":
        """
        Transform/multiply the given 2D-vector, as if it was a 3D-vector with z=0, by
        this matrix and store the result in that vector.
        
        The given 2D-vector is treated as a 3D-vector with its z-component being `0.0`, so it
        will represent a direction in 2D-space rather than a position. This method will therefore
        not take the translation part of the matrix into account.
        
        In order to store the result in another vector, use .transformDirection(Vector2dc, Vector2d).

        Arguments
        - v: the vector to transform and to hold the final result

        Returns
        - v

        See
        - .transformDirection(Vector2dc, Vector2d)
        """
        ...


    def transformDirection(self, v: "Vector2dc", dest: "Vector2d") -> "Vector2d":
        """
        Transform/multiply the given 2D-vector, as if it was a 3D-vector with z=0, by
        this matrix and store the result in `dest`.
        
        The given 2D-vector is treated as a 3D-vector with its z-component being `0.0`, so it
        will represent a direction in 2D-space rather than a position. This method will therefore
        not take the translation part of the matrix into account.
        
        In order to store the result in the same vector, use .transformDirection(Vector2d).

        Arguments
        - v: the vector to transform and to hold the final result
        - dest: will hold the result

        Returns
        - dest

        See
        - .transformDirection(Vector2d)
        """
        ...


    def transformDirection(self, x: float, y: float, dest: "Vector2d") -> "Vector2d":
        """
        Transform/multiply the given 2D-vector `(x, y)`, as if it was a 3D-vector with z=0, by
        this matrix and store the result in `dest`.
        
        The given 2D-vector is treated as a 3D-vector with its z-component being `0.0`, so it
        will represent a direction in 2D-space rather than a position. This method will therefore
        not take the translation part of the matrix into account.
        
        In order to store the result in the same vector, use .transformDirection(Vector2d).

        Arguments
        - x: the x component of the vector to transform
        - y: the y component of the vector to transform
        - dest: will hold the result

        Returns
        - dest

        See
        - .transformDirection(Vector2d)
        """
        ...


    def writeExternal(self, out: "ObjectOutput") -> None:
        ...


    def readExternal(self, in: "ObjectInput") -> None:
        ...


    def rotate(self, ang: float) -> "Matrix3x2d":
        """
        Apply a rotation transformation to this matrix by rotating the given amount of radians.
        
        If `M` is `this` matrix and `R` the rotation matrix,
        then the new matrix will be `M * R`. So when transforming a
        vector `v` with the new matrix by using `M * R * v`
        , the rotation will be applied first!

        Arguments
        - ang: the angle in radians

        Returns
        - this
        """
        ...


    def rotate(self, ang: float, dest: "Matrix3x2d") -> "Matrix3x2d":
        """
        Apply a rotation transformation to this matrix by rotating the given amount of radians and store the result in `dest`.
        
        If `M` is `this` matrix and `R` the rotation matrix,
        then the new matrix will be `M * R`. So when transforming a
        vector `v` with the new matrix by using `M * R * v`, the rotation will be applied first!

        Arguments
        - ang: the angle in radians
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def rotateLocal(self, ang: float, dest: "Matrix3x2d") -> "Matrix3x2d":
        """
        Pre-multiply a rotation to this matrix by rotating the given amount of radians and store the result in `dest`.
        
        If `M` is `this` matrix and `R` the rotation matrix,
        then the new matrix will be `R * M`. So when transforming a
        vector `v` with the new matrix by using `R * M * v`, the
        rotation will be applied last!
        
        In order to set the matrix to a rotation matrix without pre-multiplying the rotation
        transformation, use .rotation(double) rotation().
        
        Reference: <a href="http://en.wikipedia.org/wiki/Rotation_matrix#Rotation_matrix_from_axis_and_angle">http://en.wikipedia.org</a>

        Arguments
        - ang: the angle in radians to rotate
        - dest: will hold the result

        Returns
        - dest

        See
        - .rotation(double)
        """
        ...


    def rotateLocal(self, ang: float) -> "Matrix3x2d":
        """
        Pre-multiply a rotation to this matrix by rotating the given amount of radians.
        
        If `M` is `this` matrix and `R` the rotation matrix,
        then the new matrix will be `R * M`. So when transforming a
        vector `v` with the new matrix by using `R * M * v`, the
        rotation will be applied last!
        
        In order to set the matrix to a rotation matrix without pre-multiplying the rotation
        transformation, use .rotation(double) rotation().
        
        Reference: <a href="http://en.wikipedia.org/wiki/Rotation_matrix#Rotation_matrix_from_axis_and_angle">http://en.wikipedia.org</a>

        Arguments
        - ang: the angle in radians to rotate

        Returns
        - this

        See
        - .rotation(double)
        """
        ...


    def rotateAbout(self, ang: float, x: float, y: float) -> "Matrix3x2d":
        """
        Apply a rotation transformation to this matrix by rotating the given amount of radians about
        the specified rotation center `(x, y)`.
        
        This method is equivalent to calling: `translate(x, y).rotate(ang).translate(-x, -y)`
        
        If `M` is `this` matrix and `R` the rotation matrix,
        then the new matrix will be `M * R`. So when transforming a
        vector `v` with the new matrix by using `M * R * v`, the rotation will be applied first!

        Arguments
        - ang: the angle in radians
        - x: the x component of the rotation center
        - y: the y component of the rotation center

        Returns
        - this

        See
        - .rotate(double)
        """
        ...


    def rotateAbout(self, ang: float, x: float, y: float, dest: "Matrix3x2d") -> "Matrix3x2d":
        """
        Apply a rotation transformation to this matrix by rotating the given amount of radians about
        the specified rotation center `(x, y)` and store the result in `dest`.
        
        This method is equivalent to calling: `translate(x, y, dest).rotate(ang).translate(-x, -y)`
        
        If `M` is `this` matrix and `R` the rotation matrix,
        then the new matrix will be `M * R`. So when transforming a
        vector `v` with the new matrix by using `M * R * v`, the rotation will be applied first!

        Arguments
        - ang: the angle in radians
        - x: the x component of the rotation center
        - y: the y component of the rotation center
        - dest: will hold the result

        Returns
        - dest

        See
        - .rotate(double, Matrix3x2d)
        """
        ...


    def rotateTo(self, fromDir: "Vector2dc", toDir: "Vector2dc", dest: "Matrix3x2d") -> "Matrix3x2d":
        """
        Apply a rotation transformation to this matrix that rotates the given normalized `fromDir` direction vector
        to point along the normalized `toDir`, and store the result in `dest`.
        
        If `M` is `this` matrix and `R` the rotation matrix,
        then the new matrix will be `M * R`. So when transforming a
        vector `v` with the new matrix by using `M * R * v`, the rotation will be applied first!

        Arguments
        - fromDir: the normalized direction which should be rotate to point along `toDir`
        - toDir: the normalized destination direction
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def rotateTo(self, fromDir: "Vector2dc", toDir: "Vector2dc") -> "Matrix3x2d":
        """
        Apply a rotation transformation to this matrix that rotates the given normalized `fromDir` direction vector
        to point along the normalized `toDir`.
        
        If `M` is `this` matrix and `R` the rotation matrix,
        then the new matrix will be `M * R`. So when transforming a
        vector `v` with the new matrix by using `M * R * v`, the rotation will be applied first!

        Arguments
        - fromDir: the normalized direction which should be rotate to point along `toDir`
        - toDir: the normalized destination direction

        Returns
        - this
        """
        ...


    def view(self, left: float, right: float, bottom: float, top: float, dest: "Matrix3x2d") -> "Matrix3x2d":
        """
        Apply a "view" transformation to this matrix that maps the given `(left, bottom)` and
        `(right, top)` corners to `(-1, -1)` and `(1, 1)` respectively and store the result in `dest`.
        
        If `M` is `this` matrix and `O` the orthographic projection matrix,
        then the new matrix will be `M * O`. So when transforming a
        vector `v` with the new matrix by using `M * O * v`, the
        orthographic projection transformation will be applied first!

        Arguments
        - left: the distance from the center to the left view edge
        - right: the distance from the center to the right view edge
        - bottom: the distance from the center to the bottom view edge
        - top: the distance from the center to the top view edge
        - dest: will hold the result

        Returns
        - dest

        See
        - .setView(double, double, double, double)
        """
        ...


    def view(self, left: float, right: float, bottom: float, top: float) -> "Matrix3x2d":
        """
        Apply a "view" transformation to this matrix that maps the given `(left, bottom)` and
        `(right, top)` corners to `(-1, -1)` and `(1, 1)` respectively.
        
        If `M` is `this` matrix and `O` the orthographic projection matrix,
        then the new matrix will be `M * O`. So when transforming a
        vector `v` with the new matrix by using `M * O * v`, the
        orthographic projection transformation will be applied first!

        Arguments
        - left: the distance from the center to the left view edge
        - right: the distance from the center to the right view edge
        - bottom: the distance from the center to the bottom view edge
        - top: the distance from the center to the top view edge

        Returns
        - this

        See
        - .setView(double, double, double, double)
        """
        ...


    def setView(self, left: float, right: float, bottom: float, top: float) -> "Matrix3x2d":
        """
        Set this matrix to define a "view" transformation that maps the given `(left, bottom)` and
        `(right, top)` corners to `(-1, -1)` and `(1, 1)` respectively.

        Arguments
        - left: the distance from the center to the left view edge
        - right: the distance from the center to the right view edge
        - bottom: the distance from the center to the bottom view edge
        - top: the distance from the center to the top view edge

        Returns
        - this

        See
        - .view(double, double, double, double)
        """
        ...


    def origin(self, origin: "Vector2d") -> "Vector2d":
        """
        Obtain the position that gets transformed to the origin by `this` matrix.
        This can be used to get the position of the "camera" from a given *view* transformation matrix.
        
        This method is equivalent to the following code:
        ```
        Matrix3x2d inv = new Matrix3x2d(this).invert();
        inv.transform(origin.set(0, 0));
        ```

        Arguments
        - origin: will hold the position transformed to the origin

        Returns
        - origin
        """
        ...


    def viewArea(self, area: list[float]) -> list[float]:
        """
        Obtain the extents of the view transformation of `this` matrix and store it in `area`.
        This can be used to determine which region of the screen (i.e. the NDC space) is covered by the view.

        Arguments
        - area: will hold the view area as `[minX, minY, maxX, maxY]`

        Returns
        - area
        """
        ...


    def positiveX(self, dir: "Vector2d") -> "Vector2d":
        ...


    def normalizedPositiveX(self, dir: "Vector2d") -> "Vector2d":
        ...


    def positiveY(self, dir: "Vector2d") -> "Vector2d":
        ...


    def normalizedPositiveY(self, dir: "Vector2d") -> "Vector2d":
        ...


    def unproject(self, winX: float, winY: float, viewport: list[int], dest: "Vector2d") -> "Vector2d":
        """
        Unproject the given window coordinates `(winX, winY)` by `this` matrix using the specified viewport.
        
        This method first converts the given window coordinates to normalized device coordinates in the range `[-1..1]`
        and then transforms those NDC coordinates by the inverse of `this` matrix.  
        
        As a necessary computation step for unprojecting, this method computes the inverse of `this` matrix.
        In order to avoid computing the matrix inverse with every invocation, the inverse of `this` matrix can be built
        once outside using .invert(Matrix3x2d) and then the method .unprojectInv(double, double, int[], Vector2d) unprojectInv() can be invoked on it.

        Arguments
        - winX: the x-coordinate in window coordinates (pixels)
        - winY: the y-coordinate in window coordinates (pixels)
        - viewport: the viewport described by `[x, y, width, height]`
        - dest: will hold the unprojected position

        Returns
        - dest

        See
        - .invert(Matrix3x2d)
        """
        ...


    def unprojectInv(self, winX: float, winY: float, viewport: list[int], dest: "Vector2d") -> "Vector2d":
        """
        Unproject the given window coordinates `(winX, winY)` by `this` matrix using the specified viewport.
        
        This method differs from .unproject(double, double, int[], Vector2d) unproject() 
        in that it assumes that `this` is already the inverse matrix of the original projection matrix.
        It exists to avoid recomputing the matrix inverse with every invocation.

        Arguments
        - winX: the x-coordinate in window coordinates (pixels)
        - winY: the y-coordinate in window coordinates (pixels)
        - viewport: the viewport described by `[x, y, width, height]`
        - dest: will hold the unprojected position

        Returns
        - dest

        See
        - .unproject(double, double, int[], Vector2d)
        """
        ...


    def span(self, corner: "Vector2d", xDir: "Vector2d", yDir: "Vector2d") -> "Matrix3x2d":
        """
        Compute the extents of the coordinate system before this transformation was applied and store the resulting
        corner coordinates in `corner` and the span vectors in `xDir` and `yDir`.
        
        That means, given the maximum extents of the coordinate system between `[-1..+1]` in all dimensions,
        this method returns one corner and the length and direction of the two base axis vectors in the coordinate
        system before this transformation is applied, which transforms into the corner coordinates `[-1, +1]`.

        Arguments
        - corner: will hold one corner of the span
        - xDir: will hold the direction and length of the span along the positive X axis
        - yDir: will hold the direction and length of the span along the positive Y axis

        Returns
        - this
        """
        ...


    def testPoint(self, x: float, y: float) -> bool:
        ...


    def testCircle(self, x: float, y: float, r: float) -> bool:
        ...


    def testAar(self, minX: float, minY: float, maxX: float, maxY: float) -> bool:
        ...


    def hashCode(self) -> int:
        ...


    def equals(self, obj: "Object") -> bool:
        ...


    def equals(self, m: "Matrix3x2dc", delta: float) -> bool:
        ...


    def isFinite(self) -> bool:
        ...


    def clone(self) -> "Object":
        ...
