"""
Python module generated from Java source file org.joml.Matrix2f

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


class Matrix2f(Externalizable, Cloneable, Matrix2fc):
    """
    Contains the definition of a 2x2 matrix of floats, and associated functions to transform
    it. The matrix is column-major to match OpenGL's interpretation, and it looks like this:
    
         m00  m10
         m01  m11

    Author(s)
    - Joseph Burton
    """

    def __init__(self):
        """
        Create a new Matrix2f and set it to .identity() identity.
        """
        ...


    def __init__(self, mat: "Matrix2fc"):
        """
        Create a new Matrix2f and make it a copy of the given matrix.

        Arguments
        - mat: the Matrix2fc to copy the values from
        """
        ...


    def __init__(self, mat: "Matrix3fc"):
        """
        Create a new Matrix2f and make it a copy of the upper left 2x2 of the given Matrix3fc.

        Arguments
        - mat: the Matrix3fc to copy the values from
        """
        ...


    def __init__(self, m00: float, m01: float, m10: float, m11: float):
        """
        Create a new 2x2 matrix using the supplied float values. The order of the parameter is column-major,
        so the first two parameters specify the two elements of the first column.

        Arguments
        - m00: the value of m00
        - m01: the value of m01
        - m10: the value of m10
        - m11: the value of m11
        """
        ...


    def __init__(self, buffer: "FloatBuffer"):
        """
        Create a new Matrix2f by reading its 4 float components from the given FloatBuffer
        at the buffer's current position.
        
        That FloatBuffer is expected to hold the values in column-major order.
        
        The buffer's position will not be changed by this method.

        Arguments
        - buffer: the FloatBuffer to read the matrix values from
        """
        ...


    def __init__(self, col0: "Vector2fc", col1: "Vector2fc"):
        """
        Create a new Matrix2f and initialize its two columns using the supplied vectors.

        Arguments
        - col0: the first column
        - col1: the second column
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


    def m00(self, m00: float) -> "Matrix2f":
        """
        Set the value of the matrix element at column 0 and row 0.

        Arguments
        - m00: the new value

        Returns
        - this
        """
        ...


    def m01(self, m01: float) -> "Matrix2f":
        """
        Set the value of the matrix element at column 0 and row 1.

        Arguments
        - m01: the new value

        Returns
        - this
        """
        ...


    def m10(self, m10: float) -> "Matrix2f":
        """
        Set the value of the matrix element at column 1 and row 0.

        Arguments
        - m10: the new value

        Returns
        - this
        """
        ...


    def m11(self, m11: float) -> "Matrix2f":
        """
        Set the value of the matrix element at column 1 and row 1.

        Arguments
        - m11: the new value

        Returns
        - this
        """
        ...


    def set(self, m: "Matrix2fc") -> "Matrix2f":
        """
        Set the elements of this matrix to the ones in `m`.

        Arguments
        - m: the matrix to copy the elements from

        Returns
        - this
        """
        ...


    def set(self, m: "Matrix3x2fc") -> "Matrix2f":
        """
        Set the elements of this matrix to the left 2x2 submatrix of `m`.

        Arguments
        - m: the matrix to copy the elements from

        Returns
        - this
        """
        ...


    def set(self, m: "Matrix3fc") -> "Matrix2f":
        """
        Set the elements of this matrix to the upper left 2x2 of the given Matrix3fc.

        Arguments
        - m: the Matrix3fc to copy the values from

        Returns
        - this
        """
        ...


    def mul(self, right: "Matrix2fc") -> "Matrix2f":
        """
        Multiply this matrix by the supplied `right` matrix.
        
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


    def mul(self, right: "Matrix2fc", dest: "Matrix2f") -> "Matrix2f":
        ...


    def mulLocal(self, left: "Matrix2fc") -> "Matrix2f":
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


    def mulLocal(self, left: "Matrix2fc", dest: "Matrix2f") -> "Matrix2f":
        ...


    def set(self, m00: float, m01: float, m10: float, m11: float) -> "Matrix2f":
        """
        Set the values within this matrix to the supplied float values. The result looks like this:
        
        m00, m10
        m01, m11

        Arguments
        - m00: the new value of m00
        - m01: the new value of m01
        - m10: the new value of m10
        - m11: the new value of m11

        Returns
        - this
        """
        ...


    def set(self, m: list[float]) -> "Matrix2f":
        """
        Set the values in this matrix based on the supplied double array. The result looks like this:
        
        0, 2
        1, 3
        
        This method only uses the first 4 values, all others are ignored.

        Arguments
        - m: the array to read the matrix values from

        Returns
        - this
        """
        ...


    def set(self, m: list[float], off: int) -> "Matrix2f":
        """
        Set the values in this matrix based on the supplied array in column-major order. The result looks like this:
        
        0, 2
        1, 3
        
        This method only uses the 4 values starting at the given offset.

        Arguments
        - m: the array to read the matrix values from
        - off: the offset into the array

        Returns
        - this
        """
        ...


    def set(self, col0: "Vector2fc", col1: "Vector2fc") -> "Matrix2f":
        """
        Set the two columns of this matrix to the supplied vectors, respectively.

        Arguments
        - col0: the first column
        - col1: the second column

        Returns
        - this
        """
        ...


    def determinant(self) -> float:
        ...


    def invert(self) -> "Matrix2f":
        """
        Invert this matrix.

        Returns
        - this
        """
        ...


    def invert(self, dest: "Matrix2f") -> "Matrix2f":
        ...


    def transpose(self) -> "Matrix2f":
        """
        Transpose this matrix.

        Returns
        - this
        """
        ...


    def transpose(self, dest: "Matrix2f") -> "Matrix2f":
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


    def get(self, dest: "Matrix2f") -> "Matrix2f":
        """
        Get the current values of `this` matrix and store them into
        `dest`.
        
        This is the reverse method of .set(Matrix2fc) and allows to obtain
        intermediate calculation results when chaining multiple transformations.

        Arguments
        - dest: the destination matrix

        Returns
        - the passed in destination

        See
        - .set(Matrix2fc)
        """
        ...


    def get(self, dest: "Matrix3x2f") -> "Matrix3x2f":
        ...


    def get(self, dest: "Matrix3f") -> "Matrix3f":
        ...


    def getRotation(self) -> float:
        ...


    def get(self, buffer: "FloatBuffer") -> "FloatBuffer":
        ...


    def get(self, index: int, buffer: "FloatBuffer") -> "FloatBuffer":
        ...


    def get(self, buffer: "ByteBuffer") -> "ByteBuffer":
        ...


    def get(self, index: int, buffer: "ByteBuffer") -> "ByteBuffer":
        ...


    def getTransposed(self, buffer: "FloatBuffer") -> "FloatBuffer":
        ...


    def getTransposed(self, index: int, buffer: "FloatBuffer") -> "FloatBuffer":
        ...


    def getTransposed(self, buffer: "ByteBuffer") -> "ByteBuffer":
        ...


    def getTransposed(self, index: int, buffer: "ByteBuffer") -> "ByteBuffer":
        ...


    def getToAddress(self, address: int) -> "Matrix2fc":
        ...


    def getTransposedToAddress(self, address: int) -> "Matrix2fc":
        ...


    def get(self, arr: list[float], offset: int) -> list[float]:
        ...


    def get(self, arr: list[float]) -> list[float]:
        ...


    def set(self, buffer: "FloatBuffer") -> "Matrix2f":
        """
        Set the values of this matrix by reading 4 float values from the given FloatBuffer in column-major order,
        starting at its current position.
        
        The FloatBuffer is expected to contain the values in column-major order.
        
        The position of the FloatBuffer will not be changed by this method.

        Arguments
        - buffer: the FloatBuffer to read the matrix values from in column-major order

        Returns
        - this
        """
        ...


    def set(self, buffer: "ByteBuffer") -> "Matrix2f":
        """
        Set the values of this matrix by reading 4 float values from the given ByteBuffer in column-major order,
        starting at its current position.
        
        The ByteBuffer is expected to contain the values in column-major order.
        
        The position of the ByteBuffer will not be changed by this method.

        Arguments
        - buffer: the ByteBuffer to read the matrix values from in column-major order

        Returns
        - this
        """
        ...


    def set(self, index: int, buffer: "FloatBuffer") -> "Matrix2f":
        """
        Set the values of this matrix by reading 4 float values from the given FloatBuffer in column-major order,
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


    def set(self, index: int, buffer: "ByteBuffer") -> "Matrix2f":
        """
        Set the values of this matrix by reading 4 float values from the given ByteBuffer in column-major order,
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


    def setFromAddress(self, address: int) -> "Matrix2f":
        """
        Set the values of this matrix by reading 4 float values from off-heap memory in column-major order,
        starting at the given address.
        
        This method will throw an UnsupportedOperationException when JOML is used with `-Djoml.nounsafe`.
        
        *This method is unsafe as it can result in a crash of the JVM process when the specified address range does not belong to this process.*

        Arguments
        - address: the off-heap memory address to read the matrix values from in column-major order

        Returns
        - this
        """
        ...


    def setTransposedFromAddress(self, address: int) -> "Matrix2f":
        """
        Set the values of this matrix by reading 4 float values from off-heap memory in row-major order,
        starting at the given address.
        
        This method will throw an UnsupportedOperationException when JOML is used with `-Djoml.nounsafe`.
        
        *This method is unsafe as it can result in a crash of the JVM process when the specified address range does not belong to this process.*

        Arguments
        - address: the off-heap memory address to read the matrix values from in row-major order

        Returns
        - this
        """
        ...


    def zero(self) -> "Matrix2f":
        """
        Set all values within this matrix to zero.

        Returns
        - this
        """
        ...


    def identity(self) -> "Matrix2f":
        """
        Set this matrix to the identity.

        Returns
        - this
        """
        ...


    def scale(self, xy: "Vector2fc", dest: "Matrix2f") -> "Matrix2f":
        ...


    def scale(self, xy: "Vector2fc") -> "Matrix2f":
        """
        Apply scaling to this matrix by scaling the base axes by the given `xy.x` and
        `xy.y` factors, respectively.
        
        If `M` is `this` matrix and `S` the scaling matrix,
        then the new matrix will be `M * S`. So when transforming a
        vector `v` with the new matrix by using `M * S * v`, the
        scaling will be applied first!

        Arguments
        - xy: the factors of the x and y component, respectively

        Returns
        - this
        """
        ...


    def scale(self, x: float, y: float, dest: "Matrix2f") -> "Matrix2f":
        ...


    def scale(self, x: float, y: float) -> "Matrix2f":
        """
        Apply scaling to this matrix by scaling the base axes by the given x and
        y factors.
        
        If `M` is `this` matrix and `S` the scaling matrix,
        then the new matrix will be `M * S`. So when transforming a
        vector `v` with the new matrix by using `M * S * v`
        , the scaling will be applied first!

        Arguments
        - x: the factor of the x component
        - y: the factor of the y component

        Returns
        - this
        """
        ...


    def scale(self, xy: float, dest: "Matrix2f") -> "Matrix2f":
        ...


    def scale(self, xy: float) -> "Matrix2f":
        """
        Apply scaling to this matrix by uniformly scaling all base axes by the given `xy` factor.
        
        If `M` is `this` matrix and `S` the scaling matrix,
        then the new matrix will be `M * S`. So when transforming a
        vector `v` with the new matrix by using `M * S * v`
        , the scaling will be applied first!

        Arguments
        - xy: the factor for all components

        Returns
        - this

        See
        - .scale(float, float)
        """
        ...


    def scaleLocal(self, x: float, y: float, dest: "Matrix2f") -> "Matrix2f":
        ...


    def scaleLocal(self, x: float, y: float) -> "Matrix2f":
        """
        Pre-multiply scaling to this matrix by scaling the base axes by the given x and
        y factors.
        
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


    def scaling(self, factor: float) -> "Matrix2f":
        """
        Set this matrix to be a simple scale matrix, which scales all axes uniformly by the given factor.
        
        The resulting matrix can be multiplied against another transformation
        matrix to obtain an additional scaling.
        
        In order to post-multiply a scaling transformation directly to a
        matrix, use .scale(float) scale() instead.

        Arguments
        - factor: the scale factor in x and y

        Returns
        - this

        See
        - .scale(float)
        """
        ...


    def scaling(self, x: float, y: float) -> "Matrix2f":
        """
        Set this matrix to be a simple scale matrix.

        Arguments
        - x: the scale in x
        - y: the scale in y

        Returns
        - this
        """
        ...


    def scaling(self, xy: "Vector2fc") -> "Matrix2f":
        """
        Set this matrix to be a simple scale matrix which scales the base axes by `xy.x` and `xy.y` respectively.
        
        The resulting matrix can be multiplied against another transformation
        matrix to obtain an additional scaling.
        
        In order to post-multiply a scaling transformation directly to a
        matrix use .scale(Vector2fc) scale() instead.

        Arguments
        - xy: the scale in x and y respectively

        Returns
        - this

        See
        - .scale(Vector2fc)
        """
        ...


    def rotation(self, angle: float) -> "Matrix2f":
        """
        Set this matrix to a rotation matrix which rotates the given radians about the origin.
        
        The produced rotation will rotate a vector counter-clockwise around the origin.
        
        The resulting matrix can be multiplied against another transformation
        matrix to obtain an additional rotation.
        
        In order to post-multiply a rotation transformation directly to a
        matrix, use .rotate(float) rotate() instead.

        Arguments
        - angle: the angle in radians

        Returns
        - this

        See
        - .rotate(float)
        """
        ...


    def transform(self, v: "Vector2f") -> "Vector2f":
        ...


    def transform(self, v: "Vector2fc", dest: "Vector2f") -> "Vector2f":
        ...


    def transform(self, x: float, y: float, dest: "Vector2f") -> "Vector2f":
        ...


    def transformTranspose(self, v: "Vector2f") -> "Vector2f":
        ...


    def transformTranspose(self, v: "Vector2fc", dest: "Vector2f") -> "Vector2f":
        ...


    def transformTranspose(self, x: float, y: float, dest: "Vector2f") -> "Vector2f":
        ...


    def writeExternal(self, out: "ObjectOutput") -> None:
        ...


    def readExternal(self, in: "ObjectInput") -> None:
        ...


    def rotate(self, angle: float) -> "Matrix2f":
        """
        Apply rotation about the origin to this matrix by rotating the given amount of radians.
        
        The produced rotation will rotate a vector counter-clockwise around the origin.
        
        If `M` is `this` matrix and `R` the rotation matrix,
        then the new matrix will be `M * R`. So when transforming a
        vector `v` with the new matrix by using `M * R * v`
        , the rotation will be applied first!
        
        Reference: <a href="https://en.wikipedia.org/wiki/Rotation_matrix#In_two_dimensions">http://en.wikipedia.org</a>

        Arguments
        - angle: the angle in radians

        Returns
        - this
        """
        ...


    def rotate(self, angle: float, dest: "Matrix2f") -> "Matrix2f":
        ...


    def rotateLocal(self, angle: float) -> "Matrix2f":
        """
        Pre-multiply a rotation to this matrix by rotating the given amount of radians about the origin.
        
        The produced rotation will rotate a vector counter-clockwise around the origin.
        
        If `M` is `this` matrix and `R` the rotation matrix,
        then the new matrix will be `R * M`. So when transforming a
        vector `v` with the new matrix by using `R * M * v`, the
        rotation will be applied last!
        
        In order to set the matrix to a rotation matrix without pre-multiplying the rotation
        transformation, use .rotation(float) rotation().
        
        Reference: <a href="https://en.wikipedia.org/wiki/Rotation_matrix#In_two_dimensions">http://en.wikipedia.org</a>

        Arguments
        - angle: the angle in radians to rotate about the X axis

        Returns
        - this

        See
        - .rotation(float)
        """
        ...


    def rotateLocal(self, angle: float, dest: "Matrix2f") -> "Matrix2f":
        ...


    def getRow(self, row: int, dest: "Vector2f") -> "Vector2f":
        ...


    def setRow(self, row: int, src: "Vector2fc") -> "Matrix2f":
        """
        Set the row at the given `row` index, starting with `0`.

        Arguments
        - row: the row index in `[0..1]`
        - src: the row components to set

        Returns
        - this

        Raises
        - IndexOutOfBoundsException: if `row` is not in `[0..1]`
        """
        ...


    def setRow(self, row: int, x: float, y: float) -> "Matrix2f":
        """
        Set the row at the given `row` index, starting with `0`.

        Arguments
        - row: the row index in `[0..1]`
        - x: the first element in the row
        - y: the second element in the row

        Returns
        - this

        Raises
        - IndexOutOfBoundsException: if `row` is not in `[0..1]`
        """
        ...


    def getColumn(self, column: int, dest: "Vector2f") -> "Vector2f":
        ...


    def setColumn(self, column: int, src: "Vector2fc") -> "Matrix2f":
        """
        Set the column at the given `column` index, starting with `0`.

        Arguments
        - column: the column index in `[0..1]`
        - src: the column components to set

        Returns
        - this

        Raises
        - IndexOutOfBoundsException: if `column` is not in `[0..1]`
        """
        ...


    def setColumn(self, column: int, x: float, y: float) -> "Matrix2f":
        """
        Set the column at the given `column` index, starting with `0`.

        Arguments
        - column: the column index in `[0..1]`
        - x: the first element in the column
        - y: the second element in the column

        Returns
        - this

        Raises
        - IndexOutOfBoundsException: if `column` is not in `[0..1]`
        """
        ...


    def get(self, column: int, row: int) -> float:
        ...


    def set(self, column: int, row: int, value: float) -> "Matrix2f":
        """
        Set the matrix element at the given column and row to the specified value.

        Arguments
        - column: the colum index in `[0..1]`
        - row: the row index in `[0..1]`
        - value: the value

        Returns
        - this
        """
        ...


    def normal(self) -> "Matrix2f":
        """
        Set `this` matrix to its own normal matrix.
        
        Please note that, if `this` is an orthogonal matrix or a matrix whose columns are orthogonal vectors,
        then this method *need not* be invoked, since in that case `this` itself is its normal matrix.
        In this case, use .set(Matrix2fc) to set a given Matrix2f to this matrix.

        Returns
        - this

        See
        - .set(Matrix2fc)
        """
        ...


    def normal(self, dest: "Matrix2f") -> "Matrix2f":
        """
        Compute a normal matrix from `this` matrix and store it into `dest`.
        
        Please note that, if `this` is an orthogonal matrix or a matrix whose columns are orthogonal vectors,
        then this method *need not* be invoked, since in that case `this` itself is its normal matrix.
        In this case, use .set(Matrix2fc) to set a given Matrix2f to this matrix.

        Arguments
        - dest: will hold the result

        Returns
        - dest

        See
        - .set(Matrix2fc)
        """
        ...


    def getScale(self, dest: "Vector2f") -> "Vector2f":
        ...


    def positiveX(self, dir: "Vector2f") -> "Vector2f":
        ...


    def normalizedPositiveX(self, dir: "Vector2f") -> "Vector2f":
        ...


    def positiveY(self, dir: "Vector2f") -> "Vector2f":
        ...


    def normalizedPositiveY(self, dir: "Vector2f") -> "Vector2f":
        ...


    def hashCode(self) -> int:
        ...


    def equals(self, obj: "Object") -> bool:
        ...


    def equals(self, m: "Matrix2fc", delta: float) -> bool:
        ...


    def swap(self, other: "Matrix2f") -> "Matrix2f":
        """
        Exchange the values of `this` matrix with the given `other` matrix.

        Arguments
        - other: the other matrix to exchange the values with

        Returns
        - this
        """
        ...


    def add(self, other: "Matrix2fc") -> "Matrix2f":
        """
        Component-wise add `this` and `other`.

        Arguments
        - other: the other addend

        Returns
        - this
        """
        ...


    def add(self, other: "Matrix2fc", dest: "Matrix2f") -> "Matrix2f":
        ...


    def sub(self, subtrahend: "Matrix2fc") -> "Matrix2f":
        """
        Component-wise subtract `subtrahend` from `this`.

        Arguments
        - subtrahend: the subtrahend

        Returns
        - this
        """
        ...


    def sub(self, other: "Matrix2fc", dest: "Matrix2f") -> "Matrix2f":
        ...


    def mulComponentWise(self, other: "Matrix2fc") -> "Matrix2f":
        """
        Component-wise multiply `this` by `other`.

        Arguments
        - other: the other matrix

        Returns
        - this
        """
        ...


    def mulComponentWise(self, other: "Matrix2fc", dest: "Matrix2f") -> "Matrix2f":
        ...


    def lerp(self, other: "Matrix2fc", t: float) -> "Matrix2f":
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


    def lerp(self, other: "Matrix2fc", t: float, dest: "Matrix2f") -> "Matrix2f":
        ...


    def isFinite(self) -> bool:
        ...


    def clone(self) -> "Object":
        ...
