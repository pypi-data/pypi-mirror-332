"""
Python module generated from Java source file org.joml.Matrix3x2dc

Java source file obtained from artifact joml version 1.10.8

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util import *
from org.joml import *
from typing import Any, Callable, Iterable, Tuple


class Matrix3x2dc:
    """
    Interface to a read-only view of a 3x2 matrix of double-precision floats.

    Author(s)
    - Kai Burjack
    """

    def m00(self) -> float:
        """
        Return the value of the matrix element at column 0 and row 0.

        Returns
        - the value of the matrix element
        """
        ...


    def m01(self) -> float:
        """
        Return the value of the matrix element at column 0 and row 1.

        Returns
        - the value of the matrix element
        """
        ...


    def m10(self) -> float:
        """
        Return the value of the matrix element at column 1 and row 0.

        Returns
        - the value of the matrix element
        """
        ...


    def m11(self) -> float:
        """
        Return the value of the matrix element at column 1 and row 1.

        Returns
        - the value of the matrix element
        """
        ...


    def m20(self) -> float:
        """
        Return the value of the matrix element at column 2 and row 0.

        Returns
        - the value of the matrix element
        """
        ...


    def m21(self) -> float:
        """
        Return the value of the matrix element at column 2 and row 1.

        Returns
        - the value of the matrix element
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


    def mulLocal(self, left: "Matrix3x2dc", dest: "Matrix3x2d") -> "Matrix3x2d":
        """
        Pre-multiply this matrix by the supplied `left` matrix and store the result in `dest`.
        
        If `M` is `this` matrix and `L` the `left` matrix,
        then the new matrix will be `L * M`. So when transforming a
        vector `v` with the new matrix by using `L * M * v`, the
        transformation of `this` matrix will be applied first!

        Arguments
        - left: the left operand of the matrix multiplication
        - dest: the destination matrix, which will hold the result

        Returns
        - dest
        """
        ...


    def determinant(self) -> float:
        """
        Return the determinant of this matrix.

        Returns
        - the determinant
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


    def translate(self, x: float, y: float, dest: "Matrix3x2d") -> "Matrix3x2d":
        """
        Apply a translation to this matrix by translating by the given number of units in x and y and store the result
        in `dest`.
        
        If `M` is `this` matrix and `T` the translation
        matrix, then the new matrix will be `M * T`. So when
        transforming a vector `v` with the new matrix by using
        `M * T * v`, the translation will be applied first!

        Arguments
        - x: the offset to translate in x
        - y: the offset to translate in y
        - dest: will hold the result

        Returns
        - dest
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

        Arguments
        - offset: the offset to translate
        - dest: will hold the result

        Returns
        - dest
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

        Arguments
        - offset: the number of units in x and y by which to translate
        - dest: will hold the result

        Returns
        - dest
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

        Arguments
        - x: the offset to translate in x
        - y: the offset to translate in y
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def get(self, dest: "Matrix3x2d") -> "Matrix3x2d":
        """
        Get the current values of `this` matrix and store them into
        `dest`.

        Arguments
        - dest: the destination matrix

        Returns
        - dest
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


    def getTransposed(self, buffer: "DoubleBuffer") -> "DoubleBuffer":
        """
        Store this matrix in row-major order into the supplied DoubleBuffer at the current
        buffer DoubleBuffer.position() position.
        
        This method will not increment the position of the given DoubleBuffer.
        
        In order to specify the offset into the DoubleBuffer at which
        the matrix is stored, use .getTransposed(int, DoubleBuffer), taking
        the absolute position as parameter.

        Arguments
        - buffer: will receive the values of this matrix in row-major order at its current position

        Returns
        - the passed in buffer

        See
        - .getTransposed(int, DoubleBuffer)
        """
        ...


    def getTransposed(self, index: int, buffer: "DoubleBuffer") -> "DoubleBuffer":
        """
        Store this matrix in row-major order into the supplied DoubleBuffer starting at the specified
        absolute buffer position/index.
        
        This method will not increment the position of the given DoubleBuffer.

        Arguments
        - index: the absolute position into the DoubleBuffer
        - buffer: will receive the values of this matrix in row-major order

        Returns
        - the passed in buffer
        """
        ...


    def getTransposed(self, buffer: "ByteBuffer") -> "ByteBuffer":
        """
        Store this matrix in row-major order into the supplied ByteBuffer at the current
        buffer ByteBuffer.position() position.
        
        This method will not increment the position of the given ByteBuffer.
        
        In order to specify the offset into the ByteBuffer at which
        the matrix is stored, use .getTransposed(int, ByteBuffer), taking
        the absolute position as parameter.

        Arguments
        - buffer: will receive the values of this matrix in row-major order at its current position

        Returns
        - the passed in buffer

        See
        - .getTransposed(int, ByteBuffer)
        """
        ...


    def getTransposed(self, index: int, buffer: "ByteBuffer") -> "ByteBuffer":
        """
        Store this matrix in row-major order into the supplied ByteBuffer starting at the specified
        absolute buffer position/index.
        
        This method will not increment the position of the given ByteBuffer.

        Arguments
        - index: the absolute position into the ByteBuffer
        - buffer: will receive the values of this matrix in row-major order

        Returns
        - the passed in buffer
        """
        ...


    def getTransposed(self, buffer: "FloatBuffer") -> "FloatBuffer":
        """
        Store this matrix in row-major order into the supplied FloatBuffer at the current
        buffer FloatBuffer.position() position.
        
        This method will not increment the position of the given FloatBuffer.
        
        Please note that due to this matrix storing double values those values will potentially
        lose precision when they are converted to float values before being put into the given FloatBuffer.
        
        In order to specify the offset into the FloatBuffer at which
        the matrix is stored, use .getTransposed(int, FloatBuffer), taking
        the absolute position as parameter.

        Arguments
        - buffer: will receive the values of this matrix in row-major order at its current position

        Returns
        - the passed in buffer

        See
        - .getTransposed(int, FloatBuffer)
        """
        ...


    def getTransposed(self, index: int, buffer: "FloatBuffer") -> "FloatBuffer":
        """
        Store this matrix in row-major order into the supplied FloatBuffer starting at the specified
        absolute buffer position/index.
        
        This method will not increment the position of the given FloatBuffer.
        
        Please note that due to this matrix storing double values those values will potentially
        lose precision when they are converted to float values before being put into the given FloatBuffer.

        Arguments
        - index: the absolute position into the FloatBuffer
        - buffer: will receive the values of this matrix in row-major order

        Returns
        - the passed in buffer
        """
        ...


    def getTransposedFloats(self, buffer: "ByteBuffer") -> "ByteBuffer":
        """
        Store this matrix as float values in row-major order into the supplied ByteBuffer at the current
        buffer ByteBuffer.position() position.
        
        This method will not increment the position of the given ByteBuffer.
        
        Please note that due to this matrix storing double values those values will potentially
        lose precision when they are converted to float values before being put into the given FloatBuffer.
        
        In order to specify the offset into the ByteBuffer at which
        the matrix is stored, use .getTransposedFloats(int, ByteBuffer), taking
        the absolute position as parameter.

        Arguments
        - buffer: will receive the values of this matrix as float values in row-major order at its current position

        Returns
        - the passed in buffer

        See
        - .getTransposedFloats(int, ByteBuffer)
        """
        ...


    def getTransposedFloats(self, index: int, buffer: "ByteBuffer") -> "ByteBuffer":
        """
        Store this matrix in row-major order into the supplied ByteBuffer starting at the specified
        absolute buffer position/index.
        
        This method will not increment the position of the given ByteBuffer.
        
        Please note that due to this matrix storing double values those values will potentially
        lose precision when they are converted to float values before being put into the given FloatBuffer.

        Arguments
        - index: the absolute position into the ByteBuffer
        - buffer: will receive the values of this matrix as float values in row-major order

        Returns
        - the passed in buffer
        """
        ...


    def get3x3(self, buffer: "DoubleBuffer") -> "DoubleBuffer":
        """
        Store this matrix as an equivalent 3x3 matrix in column-major order into the supplied DoubleBuffer at the current
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


    def getToAddress(self, address: int) -> "Matrix3x2dc":
        """
        Store this matrix in column-major order at the given off-heap address.
        
        This method will throw an UnsupportedOperationException when JOML is used with `-Djoml.nounsafe`.
        
        *This method is unsafe as it can result in a crash of the JVM process when the specified address range does not belong to this process.*

        Arguments
        - address: the off-heap address where to store this matrix

        Returns
        - this
        """
        ...


    def getTransposedToAddress(self, address: int) -> "Matrix3x2dc":
        """
        Store this matrix in row-major order at the given off-heap address.
        
        This method will throw an UnsupportedOperationException when JOML is used with `-Djoml.nounsafe`.
        
        *This method is unsafe as it can result in a crash of the JVM process when the specified address range does not belong to this process.*

        Arguments
        - address: the off-heap address where to store this matrix

        Returns
        - this
        """
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
        Store this matrix as an equivalent 3x3 matrix into the supplied double array in column-major order at the given offset.

        Arguments
        - arr: the array to write the matrix values into
        - offset: the offset into the array

        Returns
        - the passed in array
        """
        ...


    def get3x3(self, arr: list[float]) -> list[float]:
        """
        Store this matrix as an equivalent 3x3 matrix into the supplied double array in column-major order.
        
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
        Store this matrix as an equivalent 4x4 matrix into the supplied double array in column-major order at the given offset.

        Arguments
        - arr: the array to write the matrix values into
        - offset: the offset into the array

        Returns
        - the passed in array
        """
        ...


    def get4x4(self, arr: list[float]) -> list[float]:
        """
        Store this matrix as an equivalent 4x4 matrix into the supplied double array in column-major order.
        
        In order to specify an explicit offset into the array, use the method .get4x4(double[], int).

        Arguments
        - arr: the array to write the matrix values into

        Returns
        - the passed in array

        See
        - .get4x4(double[], int)
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


    def scaleLocal(self, xy: float, dest: "Matrix3x2d") -> "Matrix3x2d":
        """
        Pre-multiply scaling to `this` matrix by scaling the two base axes by the given `xy` factor,
        and store the result in `dest`.
        
        If `M` is `this` matrix and `S` the scaling matrix,
        then the new matrix will be `S * M`. So when transforming a
        vector `v` with the new matrix by using `S * M * v`
        , the scaling will be applied last!

        Arguments
        - xy: the factor to scale all two base axes by
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def scaleLocal(self, x: float, y: float, dest: "Matrix3x2d") -> "Matrix3x2d":
        """
        Pre-multiply scaling to `this` matrix by scaling the base axes by the given x and y
        factors and store the result in `dest`.
        
        If `M` is `this` matrix and `S` the scaling matrix,
        then the new matrix will be `S * M`. So when transforming a
        vector `v` with the new matrix by using `S * M * v`
        , the scaling will be applied last!

        Arguments
        - x: the factor of the x component
        - y: the factor of the y component
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def scaleAroundLocal(self, sx: float, sy: float, ox: float, oy: float, dest: "Matrix3x2d") -> "Matrix3x2d":
        """
        Pre-multiply scaling to `this` matrix by scaling the base axes by the given sx and
        sy factors while using the given `(ox, oy)` as the scaling origin,
        and store the result in `dest`.
        
        If `M` is `this` matrix and `S` the scaling matrix,
        then the new matrix will be `S * M`. So when transforming a
        vector `v` with the new matrix by using `S * M * v`
        , the scaling will be applied last!
        
        This method is equivalent to calling: `new Matrix3x2d().translate(ox, oy).scale(sx, sy).translate(-ox, -oy).mul(this, dest)`

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


    def scaleAroundLocal(self, factor: float, ox: float, oy: float, dest: "Matrix3x2d") -> "Matrix3x2d":
        """
        Pre-multiply scaling to this matrix by scaling the base axes by the given `factor`
        while using `(ox, oy)` as the scaling origin,
        and store the result in `dest`.
        
        If `M` is `this` matrix and `S` the scaling matrix,
        then the new matrix will be `S * M`. So when transforming a
        vector `v` with the new matrix by using `S * M * v`, the
        scaling will be applied last!
        
        This method is equivalent to calling: `new Matrix3x2d().translate(ox, oy).scale(factor).translate(-ox, -oy).mul(this, dest)`

        Arguments
        - factor: the scaling factor for all three axes
        - ox: the x coordinate of the scaling origin
        - oy: the y coordinate of the scaling origin
        - dest: will hold the result

        Returns
        - this
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
        Transform/multiply the given vector by this matrix and store the result in `dest`.

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
        
        Reference: <a href="http://en.wikipedia.org/wiki/Rotation_matrix#Rotation_matrix_from_axis_and_angle">http://en.wikipedia.org</a>

        Arguments
        - ang: the angle in radians
        - dest: will hold the result

        Returns
        - dest
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
        """
        ...


    def origin(self, origin: "Vector2d") -> "Vector2d":
        """
        Obtain the position that gets transformed to the origin by `this` matrix.
        This can be used to get the position of the "camera" from a given *view* transformation matrix.
        
        This method is equivalent to the following code:
        ```
        Matrix3x2d inv = new Matrix3x2d(this).invertAffine();
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
        """
        Obtain the direction of `+X` before the transformation represented by `this` matrix is applied.
        
        This method uses the rotation component of the left 2x2 submatrix to obtain the direction 
        that is transformed to `+X` by `this` matrix.
        
        This method is equivalent to the following code:
        ```
        Matrix3x2d inv = new Matrix3x2d(this).invert();
        inv.transformDirection(dir.set(1, 0)).normalize();
        ```
        If `this` is already an orthogonal matrix, then consider using .normalizedPositiveX(Vector2d) instead.
        
        Reference: <a href="http://www.euclideanspace.com/maths/algebra/matrix/functions/inverse/threeD/">http://www.euclideanspace.com</a>

        Arguments
        - dir: will hold the direction of `+X`

        Returns
        - dir
        """
        ...


    def normalizedPositiveX(self, dir: "Vector2d") -> "Vector2d":
        """
        Obtain the direction of `+X` before the transformation represented by `this` *orthogonal* matrix is applied.
        This method only produces correct results if `this` is an *orthogonal* matrix.
        
        This method uses the rotation component of the left 2x2 submatrix to obtain the direction 
        that is transformed to `+X` by `this` matrix.
        
        This method is equivalent to the following code:
        ```
        Matrix3x2d inv = new Matrix3x2d(this).transpose();
        inv.transformDirection(dir.set(1, 0));
        ```
        
        Reference: <a href="http://www.euclideanspace.com/maths/algebra/matrix/functions/inverse/threeD/">http://www.euclideanspace.com</a>

        Arguments
        - dir: will hold the direction of `+X`

        Returns
        - dir
        """
        ...


    def positiveY(self, dir: "Vector2d") -> "Vector2d":
        """
        Obtain the direction of `+Y` before the transformation represented by `this` matrix is applied.
        
        This method uses the rotation component of the left 2x2 submatrix to obtain the direction 
        that is transformed to `+Y` by `this` matrix.
        
        This method is equivalent to the following code:
        ```
        Matrix3x2d inv = new Matrix3x2d(this).invert();
        inv.transformDirection(dir.set(0, 1)).normalize();
        ```
        If `this` is already an orthogonal matrix, then consider using .normalizedPositiveY(Vector2d) instead.
        
        Reference: <a href="http://www.euclideanspace.com/maths/algebra/matrix/functions/inverse/threeD/">http://www.euclideanspace.com</a>

        Arguments
        - dir: will hold the direction of `+Y`

        Returns
        - dir
        """
        ...


    def normalizedPositiveY(self, dir: "Vector2d") -> "Vector2d":
        """
        Obtain the direction of `+Y` before the transformation represented by `this` *orthogonal* matrix is applied.
        This method only produces correct results if `this` is an *orthogonal* matrix.
        
        This method uses the rotation component of the left 2x2 submatrix to obtain the direction 
        that is transformed to `+Y` by `this` matrix.
        
        This method is equivalent to the following code:
        ```
        Matrix3x2d inv = new Matrix3x2d(this).transpose();
        inv.transformDirection(dir.set(0, 1));
        ```
        
        Reference: <a href="http://www.euclideanspace.com/maths/algebra/matrix/functions/inverse/threeD/">http://www.euclideanspace.com</a>

        Arguments
        - dir: will hold the direction of `+Y`

        Returns
        - dir
        """
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


    def testPoint(self, x: float, y: float) -> bool:
        """
        Test whether the given point `(x, y)` is within the frustum defined by `this` matrix.
        
        This method assumes `this` matrix to be a transformation from any arbitrary coordinate system/space `M`
        into standard OpenGL clip space and tests whether the given point with the coordinates `(x, y, z)` given
        in space `M` is within the clip space.
        
        Reference: <a href="http://gamedevs.org/uploads/fast-extraction-viewing-frustum-planes-from-world-view-projection-matrix.pdf">
        Fast Extraction of Viewing Frustum Planes from the World-View-Projection Matrix</a>

        Arguments
        - x: the x-coordinate of the point
        - y: the y-coordinate of the point

        Returns
        - `True` if the given point is inside the frustum; `False` otherwise
        """
        ...


    def testCircle(self, x: float, y: float, r: float) -> bool:
        """
        Test whether the given circle is partly or completely within or outside of the frustum defined by `this` matrix.
        
        This method assumes `this` matrix to be a transformation from any arbitrary coordinate system/space `M`
        into standard OpenGL clip space and tests whether the given sphere with the coordinates `(x, y, z)` given
        in space `M` is within the clip space.
        
        Reference: <a href="http://gamedevs.org/uploads/fast-extraction-viewing-frustum-planes-from-world-view-projection-matrix.pdf">
        Fast Extraction of Viewing Frustum Planes from the World-View-Projection Matrix</a>

        Arguments
        - x: the x-coordinate of the circle's center
        - y: the y-coordinate of the circle's center
        - r: the circle's radius

        Returns
        - `True` if the given circle is partly or completely inside the frustum; `False` otherwise
        """
        ...


    def testAar(self, minX: float, minY: float, maxX: float, maxY: float) -> bool:
        """
        Test whether the given axis-aligned rectangle is partly or completely within or outside of the frustum defined by `this` matrix.
        The rectangle is specified via its min and max corner coordinates.
        
        This method assumes `this` matrix to be a transformation from any arbitrary coordinate system/space `M`
        into standard OpenGL clip space and tests whether the given axis-aligned rectangle with its minimum corner coordinates `(minX, minY, minZ)`
        and maximum corner coordinates `(maxX, maxY, maxZ)` given in space `M` is within the clip space.
        
        Reference: <a href="http://old.cescg.org/CESCG-2002/DSykoraJJelinek/">Efficient View Frustum Culling</a>
        
        Reference: <a href="http://gamedevs.org/uploads/fast-extraction-viewing-frustum-planes-from-world-view-projection-matrix.pdf">
        Fast Extraction of Viewing Frustum Planes from the World-View-Projection Matrix</a>

        Arguments
        - minX: the x-coordinate of the minimum corner
        - minY: the y-coordinate of the minimum corner
        - maxX: the x-coordinate of the maximum corner
        - maxY: the y-coordinate of the maximum corner

        Returns
        - `True` if the axis-aligned box is completely or partly inside of the frustum; `False` otherwise
        """
        ...


    def equals(self, m: "Matrix3x2dc", delta: float) -> bool:
        """
        Compare the matrix elements of `this` matrix with the given matrix using the given `delta`
        and return whether all of them are equal within a maximum difference of `delta`.
        
        Please note that this method is not used by any data structure such as ArrayList HashSet or HashMap
        and their operations, such as ArrayList.contains(Object) or HashSet.remove(Object), since those
        data structures only use the Object.equals(Object) and Object.hashCode() methods.

        Arguments
        - m: the other matrix
        - delta: the allowed maximum difference

        Returns
        - `True` whether all of the matrix elements are equal; `False` otherwise
        """
        ...


    def isFinite(self) -> bool:
        """
        Determine whether all matrix elements are finite floating-point values, that
        is, they are not Double.isNaN() NaN and not
        Double.isInfinite() infinity.

        Returns
        - `True` if all components are finite floating-point values;
                `False` otherwise
        """
        ...
