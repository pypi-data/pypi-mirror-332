"""
Python module generated from Java source file org.joml.Matrix4x3dc

Java source file obtained from artifact joml version 1.10.5

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util import *
from org.joml import *
from typing import Any, Callable, Iterable, Tuple


class Matrix4x3dc:
    """
    Interface to a read-only view of a 4x3 matrix of double-precision floats.

    Author(s)
    - Kai Burjack
    """

    PLANE_NX = 0
    """
    Argument to the first parameter of .frustumPlane(int, Vector4d)
    identifying the plane with equation `x=-1` when using the identity matrix.
    """
    PLANE_PX = 1
    """
    Argument to the first parameter of .frustumPlane(int, Vector4d)
    identifying the plane with equation `x=1` when using the identity matrix.
    """
    PLANE_NY = 2
    """
    Argument to the first parameter of .frustumPlane(int, Vector4d)
    identifying the plane with equation `y=-1` when using the identity matrix.
    """
    PLANE_PY = 3
    """
    Argument to the first parameter of .frustumPlane(int, Vector4d)
    identifying the plane with equation `y=1` when using the identity matrix.
    """
    PLANE_NZ = 4
    """
    Argument to the first parameter of .frustumPlane(int, Vector4d)
    identifying the plane with equation `z=-1` when using the identity matrix.
    """
    PLANE_PZ = 5
    """
    Argument to the first parameter of .frustumPlane(int, Vector4d)
    identifying the plane with equation `z=1` when using the identity matrix.
    """
    PROPERTY_IDENTITY = 1 << 2
    """
    Bit returned by .properties() to indicate that the matrix represents the identity transformation.
    """
    PROPERTY_TRANSLATION = 1 << 3
    """
    Bit returned by .properties() to indicate that the matrix represents a pure translation transformation.
    """
    PROPERTY_ORTHONORMAL = 1 << 4
    """
    Bit returned by .properties() to indicate that the left 3x3 submatrix represents an orthogonal
    matrix (i.e. orthonormal basis).
    """


    def properties(self) -> int:
        """
        Returns
        - the properties of the matrix
        """
        ...


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


    def m02(self) -> float:
        """
        Return the value of the matrix element at column 0 and row 2.

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


    def m12(self) -> float:
        """
        Return the value of the matrix element at column 1 and row 2.

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


    def m22(self) -> float:
        """
        Return the value of the matrix element at column 2 and row 2.

        Returns
        - the value of the matrix element
        """
        ...


    def m30(self) -> float:
        """
        Return the value of the matrix element at column 3 and row 0.

        Returns
        - the value of the matrix element
        """
        ...


    def m31(self) -> float:
        """
        Return the value of the matrix element at column 3 and row 1.

        Returns
        - the value of the matrix element
        """
        ...


    def m32(self) -> float:
        """
        Return the value of the matrix element at column 3 and row 2.

        Returns
        - the value of the matrix element
        """
        ...


    def get(self, dest: "Matrix4d") -> "Matrix4d":
        """
        Get the current values of `this` matrix and store them into the upper 4x3 submatrix of `dest`.
        
        The other elements of `dest` will not be modified.

        Arguments
        - dest: the destination matrix

        Returns
        - dest

        See
        - Matrix4d.set4x3(Matrix4x3dc)
        """
        ...


    def mul(self, right: "Matrix4x3dc", dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Multiply this matrix by the supplied `right` matrix and store the result in `dest`.
        
        If `M` is `this` matrix and `R` the `right` matrix,
        then the new matrix will be `M * R`. So when transforming a
        vector `v` with the new matrix by using `M * R * v`, the
        transformation of the right matrix will be applied first!

        Arguments
        - right: the right operand of the multiplication
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mul(self, right: "Matrix4x3fc", dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Multiply this matrix by the supplied `right` matrix and store the result in `dest`.
        
        If `M` is `this` matrix and `R` the `right` matrix,
        then the new matrix will be `M * R`. So when transforming a
        vector `v` with the new matrix by using `M * R * v`, the
        transformation of the right matrix will be applied first!

        Arguments
        - right: the right operand of the multiplication
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mulTranslation(self, right: "Matrix4x3dc", dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Multiply this matrix, which is assumed to only contain a translation, by the supplied `right` matrix and store the result in `dest`.
        
        This method assumes that `this` matrix only contains a translation.
        
        This method will not modify either the last row of `this` or the last row of `right`.
        
        If `M` is `this` matrix and `R` the `right` matrix,
        then the new matrix will be `M * R`. So when transforming a
        vector `v` with the new matrix by using `M * R * v`, the
        transformation of the right matrix will be applied first!

        Arguments
        - right: the right operand of the matrix multiplication
        - dest: the destination matrix, which will hold the result

        Returns
        - dest
        """
        ...


    def mulTranslation(self, right: "Matrix4x3fc", dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Multiply this matrix, which is assumed to only contain a translation, by the supplied `right` matrix and store the result in `dest`.
        
        This method assumes that `this` matrix only contains a translation.
        
        This method will not modify either the last row of `this` or the last row of `right`.
        
        If `M` is `this` matrix and `R` the `right` matrix,
        then the new matrix will be `M * R`. So when transforming a
        vector `v` with the new matrix by using `M * R * v`, the
        transformation of the right matrix will be applied first!

        Arguments
        - right: the right operand of the matrix multiplication
        - dest: the destination matrix, which will hold the result

        Returns
        - dest
        """
        ...


    def mulOrtho(self, view: "Matrix4x3dc", dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Multiply `this` orthographic projection matrix by the supplied `view` matrix
        and store the result in `dest`.
        
        If `M` is `this` matrix and `V` the `view` matrix,
        then the new matrix will be `M * V`. So when transforming a
        vector `v` with the new matrix by using `M * V * v`, the
        transformation of the `view` matrix will be applied first!

        Arguments
        - view: the matrix which to multiply `this` with
        - dest: the destination matrix, which will hold the result

        Returns
        - dest
        """
        ...


    def mul3x3(self, rm00: float, rm01: float, rm02: float, rm10: float, rm11: float, rm12: float, rm20: float, rm21: float, rm22: float, dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Multiply `this` by the 4x3 matrix with the column vectors `(rm00, rm01, rm02)`,
        `(rm10, rm11, rm12)`, `(rm20, rm21, rm22)` and `(0, 0, 0)`
        and store the result in `dest`.
        
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
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def fma(self, other: "Matrix4x3dc", otherFactor: float, dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Component-wise add `this` and `other`
        by first multiplying each component of `other` by `otherFactor`,
        adding that to `this` and storing the final result in `dest`.
        
        The other components of `dest` will be set to the ones of `this`.
        
        The matrices `this` and `other` will not be changed.

        Arguments
        - other: the other matrix
        - otherFactor: the factor to multiply each of the other matrix's components
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def fma(self, other: "Matrix4x3fc", otherFactor: float, dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Component-wise add `this` and `other`
        by first multiplying each component of `other` by `otherFactor`,
        adding that to `this` and storing the final result in `dest`.
        
        The other components of `dest` will be set to the ones of `this`.
        
        The matrices `this` and `other` will not be changed.

        Arguments
        - other: the other matrix
        - otherFactor: the factor to multiply each of the other matrix's components
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def add(self, other: "Matrix4x3dc", dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Component-wise add `this` and `other` and store the result in `dest`.

        Arguments
        - other: the other addend
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def add(self, other: "Matrix4x3fc", dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Component-wise add `this` and `other` and store the result in `dest`.

        Arguments
        - other: the other addend
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def sub(self, subtrahend: "Matrix4x3dc", dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Component-wise subtract `subtrahend` from `this` and store the result in `dest`.

        Arguments
        - subtrahend: the subtrahend
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def sub(self, subtrahend: "Matrix4x3fc", dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Component-wise subtract `subtrahend` from `this` and store the result in `dest`.

        Arguments
        - subtrahend: the subtrahend
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mulComponentWise(self, other: "Matrix4x3dc", dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Component-wise multiply `this` by `other` and store the result in `dest`.

        Arguments
        - other: the other matrix
        - dest: will hold the result

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


    def invert(self, dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Invert `this` matrix and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def invertOrtho(self, dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Invert `this` orthographic projection matrix and store the result into the given `dest`.
        
        This method can be used to quickly obtain the inverse of an orthographic projection matrix.

        Arguments
        - dest: will hold the inverse of `this`

        Returns
        - dest
        """
        ...


    def transpose3x3(self, dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Transpose only the left 3x3 submatrix of this matrix and store the result in `dest`.
        
        All other matrix elements are left unchanged.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def transpose3x3(self, dest: "Matrix3d") -> "Matrix3d":
        """
        Transpose only the left 3x3 submatrix of this matrix and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def getTranslation(self, dest: "Vector3d") -> "Vector3d":
        """
        Get only the translation components `(m30, m31, m32)` of this matrix and store them in the given vector `xyz`.

        Arguments
        - dest: will hold the translation components of this matrix

        Returns
        - dest
        """
        ...


    def getScale(self, dest: "Vector3d") -> "Vector3d":
        """
        Get the scaling factors of `this` matrix for the three base axes.

        Arguments
        - dest: will hold the scaling factors for `x`, `y` and `z`

        Returns
        - dest
        """
        ...


    def get(self, dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Get the current values of `this` matrix and store them into
        `dest`.

        Arguments
        - dest: the destination matrix

        Returns
        - the passed in destination
        """
        ...


    def getUnnormalizedRotation(self, dest: "Quaternionf") -> "Quaternionf":
        """
        Get the current values of `this` matrix and store the represented rotation
        into the given Quaternionf.
        
        This method assumes that the first three column vectors of the left 3x3 submatrix are not normalized and
        thus allows to ignore any additional scaling factor that is applied to the matrix.

        Arguments
        - dest: the destination Quaternionf

        Returns
        - the passed in destination

        See
        - Quaternionf.setFromUnnormalized(Matrix4x3dc)
        """
        ...


    def getNormalizedRotation(self, dest: "Quaternionf") -> "Quaternionf":
        """
        Get the current values of `this` matrix and store the represented rotation
        into the given Quaternionf.
        
        This method assumes that the first three column vectors of the left 3x3 submatrix are normalized.

        Arguments
        - dest: the destination Quaternionf

        Returns
        - the passed in destination

        See
        - Quaternionf.setFromNormalized(Matrix4x3dc)
        """
        ...


    def getUnnormalizedRotation(self, dest: "Quaterniond") -> "Quaterniond":
        """
        Get the current values of `this` matrix and store the represented rotation
        into the given Quaterniond.
        
        This method assumes that the first three column vectors of the left 3x3 submatrix are not normalized and
        thus allows to ignore any additional scaling factor that is applied to the matrix.

        Arguments
        - dest: the destination Quaterniond

        Returns
        - the passed in destination

        See
        - Quaterniond.setFromUnnormalized(Matrix4x3dc)
        """
        ...


    def getNormalizedRotation(self, dest: "Quaterniond") -> "Quaterniond":
        """
        Get the current values of `this` matrix and store the represented rotation
        into the given Quaterniond.
        
        This method assumes that the first three column vectors of the left 3x3 submatrix are normalized.

        Arguments
        - dest: the destination Quaterniond

        Returns
        - the passed in destination

        See
        - Quaterniond.setFromNormalized(Matrix4x3dc)
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


    def get(self, buffer: "FloatBuffer") -> "FloatBuffer":
        """
        Store this matrix in column-major order into the supplied FloatBuffer at the current
        buffer FloatBuffer.position() position.
        
        This method will not increment the position of the given
        FloatBuffer.
        
        In order to specify the offset into the FloatBuffer at which
        the matrix is stored, use .get(int, FloatBuffer), taking
        the absolute position as parameter.
        
        Please note that due to this matrix storing double values those values will potentially
        lose precision when they are converted to float values before being put into the given FloatBuffer.

        Arguments
        - buffer: will receive the values of this matrix in column-major order at its current position

        Returns
        - the passed in buffer

        See
        - .get(int, FloatBuffer)
        """
        ...


    def get(self, index: int, buffer: "FloatBuffer") -> "FloatBuffer":
        """
        Store this matrix in column-major order into the supplied FloatBuffer starting at the specified
        absolute buffer position/index.
        
        This method will not increment the position of the given FloatBuffer.
        
        Please note that due to this matrix storing double values those values will potentially
        lose precision when they are converted to float values before being put into the given FloatBuffer.

        Arguments
        - index: the absolute position into the FloatBuffer
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


    def getFloats(self, buffer: "ByteBuffer") -> "ByteBuffer":
        """
        Store the elements of this matrix as float values in column-major order into the supplied ByteBuffer at the current
        buffer ByteBuffer.position() position.
        
        This method will not increment the position of the given ByteBuffer.
        
        Please note that due to this matrix storing double values those values will potentially
        lose precision when they are converted to float values before being put into the given ByteBuffer.
        
        In order to specify the offset into the ByteBuffer at which
        the matrix is stored, use .getFloats(int, ByteBuffer), taking
        the absolute position as parameter.

        Arguments
        - buffer: will receive the elements of this matrix as float values in column-major order at its current position

        Returns
        - the passed in buffer

        See
        - .getFloats(int, ByteBuffer)
        """
        ...


    def getFloats(self, index: int, buffer: "ByteBuffer") -> "ByteBuffer":
        """
        Store the elements of this matrix as float values in column-major order into the supplied ByteBuffer
        starting at the specified absolute buffer position/index.
        
        This method will not increment the position of the given ByteBuffer.
        
        Please note that due to this matrix storing double values those values will potentially
        lose precision when they are converted to float values before being put into the given ByteBuffer.

        Arguments
        - index: the absolute position into the ByteBuffer
        - buffer: will receive the elements of this matrix as float values in column-major order

        Returns
        - the passed in buffer
        """
        ...


    def getToAddress(self, address: int) -> "Matrix4x3dc":
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


    def get(self, arr: list[float], offset: int) -> list[float]:
        """
        Store the elements of this matrix as float values in column-major order into the supplied float array at the given offset.
        
        Please note that due to this matrix storing double values those values will potentially
        lose precision when they are converted to float values before being put into the given float array.

        Arguments
        - arr: the array to write the matrix values into
        - offset: the offset into the array

        Returns
        - the passed in array
        """
        ...


    def get(self, arr: list[float]) -> list[float]:
        """
        Store the elements of this matrix as float values in column-major order into the supplied float array.
        
        Please note that due to this matrix storing double values those values will potentially
        lose precision when they are converted to float values before being put into the given float array.
        
        In order to specify an explicit offset into the array, use the method .get(float[], int).

        Arguments
        - arr: the array to write the matrix values into

        Returns
        - the passed in array

        See
        - .get(float[], int)
        """
        ...


    def get4x4(self, arr: list[float], offset: int) -> list[float]:
        """
        Store a 4x4 matrix in column-major order into the supplied array at the given offset,
        where the upper 4x3 submatrix is `this` and the last row is `(0, 0, 0, 1)`.

        Arguments
        - arr: the array to write the matrix values into
        - offset: the offset into the array

        Returns
        - the passed in array
        """
        ...


    def get4x4(self, arr: list[float]) -> list[float]:
        """
        Store a 4x4 matrix in column-major order into the supplied array,
        where the upper 4x3 submatrix is `this` and the last row is `(0, 0, 0, 1)`.
        
        In order to specify an explicit offset into the array, use the method .get4x4(double[], int).

        Arguments
        - arr: the array to write the matrix values into

        Returns
        - the passed in array

        See
        - .get4x4(double[], int)
        """
        ...


    def get4x4(self, arr: list[float], offset: int) -> list[float]:
        """
        Store a 4x4 matrix in column-major order into the supplied array at the given offset,
        where the upper 4x3 submatrix is `this` and the last row is `(0, 0, 0, 1)`.
        
        Please note that due to this matrix storing double values those values will potentially
        lose precision when they are converted to float values before being put into the given float array.

        Arguments
        - arr: the array to write the matrix values into
        - offset: the offset into the array

        Returns
        - the passed in array
        """
        ...


    def get4x4(self, arr: list[float]) -> list[float]:
        """
        Store a 4x4 matrix in column-major order into the supplied array,
        where the upper 4x3 submatrix is `this` and the last row is `(0, 0, 0, 1)`.
        
        Please note that due to this matrix storing double values those values will potentially
        lose precision when they are converted to float values before being put into the given float array.
        
        In order to specify an explicit offset into the array, use the method .get4x4(float[], int).

        Arguments
        - arr: the array to write the matrix values into

        Returns
        - the passed in array

        See
        - .get4x4(float[], int)
        """
        ...


    def get4x4(self, buffer: "DoubleBuffer") -> "DoubleBuffer":
        """
        Store a 4x4 matrix in column-major order into the supplied DoubleBuffer at the current
        buffer DoubleBuffer.position() position, where the upper 4x3 submatrix is `this` and the last row is `(0, 0, 0, 1)`.
        
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
        Store a 4x4 matrix in column-major order into the supplied DoubleBuffer starting at the specified
        absolute buffer position/index, where the upper 4x3 submatrix is `this` and the last row is `(0, 0, 0, 1)`.
        
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
        Store a 4x4 matrix in column-major order into the supplied ByteBuffer at the current
        buffer ByteBuffer.position() position, where the upper 4x3 submatrix is `this` and the last row is `(0, 0, 0, 1)`.
        
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
        Store a 4x4 matrix in column-major order into the supplied ByteBuffer starting at the specified
        absolute buffer position/index, where the upper 4x3 submatrix is `this` and the last row is `(0, 0, 0, 1)`.
        
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


    def getTransposed(self, arr: list[float], offset: int) -> list[float]:
        """
        Store this matrix into the supplied float array in row-major order at the given offset.

        Arguments
        - arr: the array to write the matrix values into
        - offset: the offset into the array

        Returns
        - the passed in array
        """
        ...


    def getTransposed(self, arr: list[float]) -> list[float]:
        """
        Store this matrix into the supplied float array in row-major order.
        
        In order to specify an explicit offset into the array, use the method .getTransposed(double[], int).

        Arguments
        - arr: the array to write the matrix values into

        Returns
        - the passed in array

        See
        - .getTransposed(double[], int)
        """
        ...


    def transform(self, v: "Vector4d") -> "Vector4d":
        """
        Transform/multiply the given vector by this matrix and store the result in that vector.

        Arguments
        - v: the vector to transform and to hold the final result

        Returns
        - v

        See
        - Vector4d.mul(Matrix4x3dc)
        """
        ...


    def transform(self, v: "Vector4dc", dest: "Vector4d") -> "Vector4d":
        """
        Transform/multiply the given vector by this matrix and store the result in `dest`.

        Arguments
        - v: the vector to transform
        - dest: will contain the result

        Returns
        - dest

        See
        - Vector4d.mul(Matrix4x3dc, Vector4d)
        """
        ...


    def transformPosition(self, v: "Vector3d") -> "Vector3d":
        """
        Transform/multiply the given 3D-vector, as if it was a 4D-vector with w=1, by
        this matrix and store the result in that vector.
        
        The given 3D-vector is treated as a 4D-vector with its w-component being 1.0, so it
        will represent a position/location in 3D-space rather than a direction.
        
        In order to store the result in another vector, use .transformPosition(Vector3dc, Vector3d).

        Arguments
        - v: the vector to transform and to hold the final result

        Returns
        - v

        See
        - .transform(Vector4d)
        """
        ...


    def transformPosition(self, v: "Vector3dc", dest: "Vector3d") -> "Vector3d":
        """
        Transform/multiply the given 3D-vector, as if it was a 4D-vector with w=1, by
        this matrix and store the result in `dest`.
        
        The given 3D-vector is treated as a 4D-vector with its w-component being 1.0, so it
        will represent a position/location in 3D-space rather than a direction.
        
        In order to store the result in the same vector, use .transformPosition(Vector3d).

        Arguments
        - v: the vector to transform
        - dest: will hold the result

        Returns
        - dest

        See
        - .transform(Vector4dc, Vector4d)
        """
        ...


    def transformDirection(self, v: "Vector3d") -> "Vector3d":
        """
        Transform/multiply the given 3D-vector, as if it was a 4D-vector with w=0, by
        this matrix and store the result in that vector.
        
        The given 3D-vector is treated as a 4D-vector with its w-component being `0.0`, so it
        will represent a direction in 3D-space rather than a position. This method will therefore
        not take the translation part of the matrix into account.
        
        In order to store the result in another vector, use .transformDirection(Vector3dc, Vector3d).

        Arguments
        - v: the vector to transform and to hold the final result

        Returns
        - v
        """
        ...


    def transformDirection(self, v: "Vector3dc", dest: "Vector3d") -> "Vector3d":
        """
        Transform/multiply the given 3D-vector, as if it was a 4D-vector with w=0, by
        this matrix and store the result in `dest`.
        
        The given 3D-vector is treated as a 4D-vector with its w-component being `0.0`, so it
        will represent a direction in 3D-space rather than a position. This method will therefore
        not take the translation part of the matrix into account.
        
        In order to store the result in the same vector, use .transformDirection(Vector3d).

        Arguments
        - v: the vector to transform and to hold the final result
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def scale(self, xyz: "Vector3dc", dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Apply scaling to `this` matrix by scaling the base axes by the given `xyz.x`,
        `xyz.y` and `xyz.z` factors, respectively and store the result in `dest`.
        
        If `M` is `this` matrix and `S` the scaling matrix,
        then the new matrix will be `M * S`. So when transforming a
        vector `v` with the new matrix by using `M * S * v`
        , the scaling will be applied first!

        Arguments
        - xyz: the factors of the x, y and z component, respectively
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def scale(self, x: float, y: float, z: float, dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Apply scaling to `this` matrix by scaling the base axes by the given x,
        y and z factors and store the result in `dest`.
        
        If `M` is `this` matrix and `S` the scaling matrix,
        then the new matrix will be `M * S`. So when transforming a
        vector `v` with the new matrix by using `M * S * v`
        , the scaling will be applied first!

        Arguments
        - x: the factor of the x component
        - y: the factor of the y component
        - z: the factor of the z component
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def scale(self, xyz: float, dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Apply scaling to this matrix by uniformly scaling all base axes by the given xyz factor
        and store the result in `dest`.
        
        If `M` is `this` matrix and `S` the scaling matrix,
        then the new matrix will be `M * S`. So when transforming a
        vector `v` with the new matrix by using `M * S * v`
        , the scaling will be applied first!

        Arguments
        - xyz: the factor for all components
        - dest: will hold the result

        Returns
        - dest

        See
        - .scale(double, double, double, Matrix4x3d)
        """
        ...


    def scaleXY(self, x: float, y: float, dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Apply scaling to this matrix by by scaling the X axis by `x` and the Y axis by `y`
        and store the result in `dest`.
        
        If `M` is `this` matrix and `S` the scaling matrix,
        then the new matrix will be `M * S`. So when transforming a
        vector `v` with the new matrix by using `M * S * v`, the
        scaling will be applied first!

        Arguments
        - x: the factor of the x component
        - y: the factor of the y component
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def scaleAround(self, sx: float, sy: float, sz: float, ox: float, oy: float, oz: float, dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Apply scaling to `this` matrix by scaling the base axes by the given sx,
        sy and sz factors while using `(ox, oy, oz)` as the scaling origin,
        and store the result in `dest`.
        
        If `M` is `this` matrix and `S` the scaling matrix,
        then the new matrix will be `M * S`. So when transforming a
        vector `v` with the new matrix by using `M * S * v`
        , the scaling will be applied first!
        
        This method is equivalent to calling: `translate(ox, oy, oz, dest).scale(sx, sy, sz).translate(-ox, -oy, -oz)`

        Arguments
        - sx: the scaling factor of the x component
        - sy: the scaling factor of the y component
        - sz: the scaling factor of the z component
        - ox: the x coordinate of the scaling origin
        - oy: the y coordinate of the scaling origin
        - oz: the z coordinate of the scaling origin
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def scaleAround(self, factor: float, ox: float, oy: float, oz: float, dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Apply scaling to this matrix by scaling all three base axes by the given `factor`
        while using `(ox, oy, oz)` as the scaling origin,
        and store the result in `dest`.
        
        If `M` is `this` matrix and `S` the scaling matrix,
        then the new matrix will be `M * S`. So when transforming a
        vector `v` with the new matrix by using `M * S * v`, the
        scaling will be applied first!
        
        This method is equivalent to calling: `translate(ox, oy, oz, dest).scale(factor).translate(-ox, -oy, -oz)`

        Arguments
        - factor: the scaling factor for all three axes
        - ox: the x coordinate of the scaling origin
        - oy: the y coordinate of the scaling origin
        - oz: the z coordinate of the scaling origin
        - dest: will hold the result

        Returns
        - this
        """
        ...


    def scaleLocal(self, x: float, y: float, z: float, dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Pre-multiply scaling to `this` matrix by scaling the base axes by the given x,
        y and z factors and store the result in `dest`.
        
        If `M` is `this` matrix and `S` the scaling matrix,
        then the new matrix will be `S * M`. So when transforming a
        vector `v` with the new matrix by using `S * M * v`
        , the scaling will be applied last!

        Arguments
        - x: the factor of the x component
        - y: the factor of the y component
        - z: the factor of the z component
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def rotate(self, ang: float, x: float, y: float, z: float, dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Apply rotation to this matrix by rotating the given amount of radians
        about the given axis specified as x, y and z components and store the result in `dest`.
        
        When used with a right-handed coordinate system, the produced rotation will rotate a vector 
        counter-clockwise around the rotation axis, when viewing along the negative axis direction towards the origin.
        When used with a left-handed coordinate system, the rotation is clockwise.
        
        If `M` is `this` matrix and `R` the rotation matrix,
        then the new matrix will be `M * R`. So when transforming a
        vector `v` with the new matrix by using `M * R * v`
        , the rotation will be applied first!

        Arguments
        - ang: the angle is in radians
        - x: the x component of the axis
        - y: the y component of the axis
        - z: the z component of the axis
        - dest: will hold the result

        Returns
        - dest
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
        
        Reference: <a href="http://en.wikipedia.org/wiki/Rotation_matrix#Rotation_matrix_from_axis_and_angle">http://en.wikipedia.org</a>

        Arguments
        - ang: the angle in radians
        - x: the x component of the axis
        - y: the y component of the axis
        - z: the z component of the axis
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def rotateAround(self, quat: "Quaterniondc", ox: float, oy: float, oz: float, dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Apply the rotation - and possibly scaling - transformation of the given Quaterniondc to this matrix while using `(ox, oy, oz)` as the rotation origin,
        and store the result in `dest`.
        
        When used with a right-handed coordinate system, the produced rotation will rotate a vector 
        counter-clockwise around the rotation axis, when viewing along the negative axis direction towards the origin.
        When used with a left-handed coordinate system, the rotation is clockwise.
        
        If `M` is `this` matrix and `Q` the rotation matrix obtained from the given quaternion,
        then the new matrix will be `M * Q`. So when transforming a
        vector `v` with the new matrix by using `M * Q * v`,
        the quaternion rotation will be applied first!
        
        This method is equivalent to calling: `translate(ox, oy, oz, dest).rotate(quat).translate(-ox, -oy, -oz)`
        
        Reference: <a href="http://en.wikipedia.org/wiki/Rotation_matrix#Quaternion">http://en.wikipedia.org</a>

        Arguments
        - quat: the Quaterniondc
        - ox: the x coordinate of the rotation origin
        - oy: the y coordinate of the rotation origin
        - oz: the z coordinate of the rotation origin
        - dest: will hold the result

        Returns
        - dest
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
        
        Reference: <a href="http://en.wikipedia.org/wiki/Rotation_matrix#Rotation_matrix_from_axis_and_angle">http://en.wikipedia.org</a>

        Arguments
        - ang: the angle in radians
        - x: the x component of the axis
        - y: the y component of the axis
        - z: the z component of the axis
        - dest: will hold the result

        Returns
        - dest
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

        Arguments
        - offset: the number of units in x, y and z by which to translate
        - dest: will hold the result

        Returns
        - dest
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

        Arguments
        - offset: the number of units in x, y and z by which to translate
        - dest: will hold the result

        Returns
        - dest
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

        Arguments
        - x: the offset to translate in x
        - y: the offset to translate in y
        - z: the offset to translate in z
        - dest: will hold the result

        Returns
        - dest
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

        Arguments
        - offset: the number of units in x, y and z by which to translate
        - dest: will hold the result

        Returns
        - dest
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

        Arguments
        - offset: the number of units in x, y and z by which to translate
        - dest: will hold the result

        Returns
        - dest
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

        Arguments
        - x: the offset to translate in x
        - y: the offset to translate in y
        - z: the offset to translate in z
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def rotateX(self, ang: float, dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Apply rotation about the X axis to this matrix by rotating the given amount of radians 
        and store the result in `dest`.
        
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
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def rotateY(self, ang: float, dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Apply rotation about the Y axis to this matrix by rotating the given amount of radians 
        and store the result in `dest`.
        
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
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def rotateZ(self, ang: float, dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Apply rotation about the Z axis to this matrix by rotating the given amount of radians 
        and store the result in `dest`.
        
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
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def rotateXYZ(self, angleX: float, angleY: float, angleZ: float, dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Apply rotation of `angleX` radians about the X axis, followed by a rotation of `angleY` radians about the Y axis and
        followed by a rotation of `angleZ` radians about the Z axis and store the result in `dest`.
        
        When used with a right-handed coordinate system, the produced rotation will rotate a vector 
        counter-clockwise around the rotation axis, when viewing along the negative axis direction towards the origin.
        When used with a left-handed coordinate system, the rotation is clockwise.
        
        If `M` is `this` matrix and `R` the rotation matrix,
        then the new matrix will be `M * R`. So when transforming a
        vector `v` with the new matrix by using `M * R * v`, the
        rotation will be applied first!
        
        This method is equivalent to calling: `rotateX(angleX, dest).rotateY(angleY).rotateZ(angleZ)`

        Arguments
        - angleX: the angle to rotate about X
        - angleY: the angle to rotate about Y
        - angleZ: the angle to rotate about Z
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def rotateZYX(self, angleZ: float, angleY: float, angleX: float, dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Apply rotation of `angleZ` radians about the Z axis, followed by a rotation of `angleY` radians about the Y axis and
        followed by a rotation of `angleX` radians about the X axis and store the result in `dest`.
        
        When used with a right-handed coordinate system, the produced rotation will rotate a vector 
        counter-clockwise around the rotation axis, when viewing along the negative axis direction towards the origin.
        When used with a left-handed coordinate system, the rotation is clockwise.
        
        If `M` is `this` matrix and `R` the rotation matrix,
        then the new matrix will be `M * R`. So when transforming a
        vector `v` with the new matrix by using `M * R * v`, the
        rotation will be applied first!
        
        This method is equivalent to calling: `rotateZ(angleZ, dest).rotateY(angleY).rotateX(angleX)`

        Arguments
        - angleZ: the angle to rotate about Z
        - angleY: the angle to rotate about Y
        - angleX: the angle to rotate about X
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def rotateYXZ(self, angleY: float, angleX: float, angleZ: float, dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Apply rotation of `angleY` radians about the Y axis, followed by a rotation of `angleX` radians about the X axis and
        followed by a rotation of `angleZ` radians about the Z axis and store the result in `dest`.
        
        When used with a right-handed coordinate system, the produced rotation will rotate a vector 
        counter-clockwise around the rotation axis, when viewing along the negative axis direction towards the origin.
        When used with a left-handed coordinate system, the rotation is clockwise.
        
        If `M` is `this` matrix and `R` the rotation matrix,
        then the new matrix will be `M * R`. So when transforming a
        vector `v` with the new matrix by using `M * R * v`, the
        rotation will be applied first!
        
        This method is equivalent to calling: `rotateY(angleY, dest).rotateX(angleX).rotateZ(angleZ)`

        Arguments
        - angleY: the angle to rotate about Y
        - angleX: the angle to rotate about X
        - angleZ: the angle to rotate about Z
        - dest: will hold the result

        Returns
        - dest
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
        
        Reference: <a href="http://en.wikipedia.org/wiki/Rotation_matrix#Quaternion">http://en.wikipedia.org</a>

        Arguments
        - quat: the Quaterniondc
        - dest: will hold the result

        Returns
        - dest
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
        
        Reference: <a href="http://en.wikipedia.org/wiki/Rotation_matrix#Quaternion">http://en.wikipedia.org</a>

        Arguments
        - quat: the Quaternionfc
        - dest: will hold the result

        Returns
        - dest
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
        
        Reference: <a href="http://en.wikipedia.org/wiki/Rotation_matrix#Quaternion">http://en.wikipedia.org</a>

        Arguments
        - quat: the Quaterniondc
        - dest: will hold the result

        Returns
        - dest
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
        
        Reference: <a href="http://en.wikipedia.org/wiki/Rotation_matrix#Quaternion">http://en.wikipedia.org</a>

        Arguments
        - quat: the Quaternionfc
        - dest: will hold the result

        Returns
        - dest
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
        
        Reference: <a href="http://en.wikipedia.org/wiki/Rotation_matrix#Quaternion">http://en.wikipedia.org</a>

        Arguments
        - quat: the Quaterniondc
        - dest: will hold the result

        Returns
        - dest
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
        
        Reference: <a href="http://en.wikipedia.org/wiki/Rotation_matrix#Quaternion">http://en.wikipedia.org</a>

        Arguments
        - quat: the Quaternionfc
        - dest: will hold the result

        Returns
        - dest
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
        
        Reference: <a href="http://en.wikipedia.org/wiki/Rotation_matrix#Axis_and_angle">http://en.wikipedia.org</a>

        Arguments
        - axisAngle: the AxisAngle4f (needs to be AxisAngle4f.normalize() normalized)
        - dest: will hold the result

        Returns
        - dest

        See
        - .rotate(double, double, double, double, Matrix4x3d)
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
        
        Reference: <a href="http://en.wikipedia.org/wiki/Rotation_matrix#Axis_and_angle">http://en.wikipedia.org</a>

        Arguments
        - axisAngle: the AxisAngle4d (needs to be AxisAngle4d.normalize() normalized)
        - dest: will hold the result

        Returns
        - dest

        See
        - .rotate(double, double, double, double, Matrix4x3d)
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
        
        Reference: <a href="http://en.wikipedia.org/wiki/Rotation_matrix#Axis_and_angle">http://en.wikipedia.org</a>

        Arguments
        - angle: the angle in radians
        - axis: the rotation axis (needs to be Vector3d.normalize() normalized)
        - dest: will hold the result

        Returns
        - dest

        See
        - .rotate(double, double, double, double, Matrix4x3d)
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
        
        Reference: <a href="http://en.wikipedia.org/wiki/Rotation_matrix#Axis_and_angle">http://en.wikipedia.org</a>

        Arguments
        - angle: the angle in radians
        - axis: the rotation axis (needs to be Vector3f.normalize() normalized)
        - dest: will hold the result

        Returns
        - dest

        See
        - .rotate(double, double, double, double, Matrix4x3d)
        """
        ...


    def getRow(self, row: int, dest: "Vector4d") -> "Vector4d":
        """
        Get the row at the given `row` index, starting with `0`.

        Arguments
        - row: the row index in `[0..2]`
        - dest: will hold the row components

        Returns
        - the passed in destination

        Raises
        - IndexOutOfBoundsException: if `row` is not in `[0..2]`
        """
        ...


    def getColumn(self, column: int, dest: "Vector3d") -> "Vector3d":
        """
        Get the column at the given `column` index, starting with `0`.

        Arguments
        - column: the column index in `[0..3]`
        - dest: will hold the column components

        Returns
        - the passed in destination

        Raises
        - IndexOutOfBoundsException: if `column` is not in `[0..3]`
        """
        ...


    def normal(self, dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Compute a normal matrix from the left 3x3 submatrix of `this`
        and store it into the left 3x3 submatrix of `dest`.
        All other values of `dest` will be set to identity.
        
        The normal matrix of `m` is the transpose of the inverse of `m`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def normal(self, dest: "Matrix3d") -> "Matrix3d":
        """
        Compute a normal matrix from the left 3x3 submatrix of `this`
        and store it into `dest`.
        
        The normal matrix of `m` is the transpose of the inverse of `m`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
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
        All other values of `dest` will be set to identity.
        
        The cofactor matrix can be used instead of .normal(Matrix4x3d) to transform normals
        when the orientation of the normals with respect to the surface should be preserved.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def normalize3x3(self, dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Normalize the left 3x3 submatrix of this matrix and store the result in `dest`.
        
        The resulting matrix will map unit vectors to unit vectors, though a pair of orthogonal input unit
        vectors need not be mapped to a pair of orthogonal output vectors if the original matrix was not orthogonal itself
        (i.e. had *skewing*).

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def normalize3x3(self, dest: "Matrix3d") -> "Matrix3d":
        """
        Normalize the left 3x3 submatrix of this matrix and store the result in `dest`.
        
        The resulting matrix will map unit vectors to unit vectors, though a pair of orthogonal input unit
        vectors need not be mapped to a pair of orthogonal output vectors if the original matrix was not orthogonal itself
        (i.e. had *skewing*).

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def reflect(self, a: float, b: float, c: float, d: float, dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Apply a mirror/reflection transformation to this matrix that reflects about the given plane
        specified via the equation `x*a + y*b + z*c + d = 0` and store the result in `dest`.
        
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
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def reflect(self, nx: float, ny: float, nz: float, px: float, py: float, pz: float, dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Apply a mirror/reflection transformation to this matrix that reflects about the given plane
        specified via the plane normal and a point on the plane, and store the result in `dest`.
        
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
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def reflect(self, orientation: "Quaterniondc", point: "Vector3dc", dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Apply a mirror/reflection transformation to this matrix that reflects about a plane
        specified via the plane orientation and a point on the plane, and store the result in `dest`.
        
        This method can be used to build a reflection transformation based on the orientation of a mirror object in the scene.
        It is assumed that the default mirror plane's normal is `(0, 0, 1)`. So, if the given Quaterniondc is
        the identity (does not apply any additional rotation), the reflection plane will be `z=0`, offset by the given `point`.
        
        If `M` is `this` matrix and `R` the reflection matrix,
        then the new matrix will be `M * R`. So when transforming a
        vector `v` with the new matrix by using `M * R * v`, the
        reflection will be applied first!

        Arguments
        - orientation: the plane orientation
        - point: a point on the plane
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def reflect(self, normal: "Vector3dc", point: "Vector3dc", dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Apply a mirror/reflection transformation to this matrix that reflects about the given plane
        specified via the plane normal and a point on the plane, and store the result in `dest`.
        
        If `M` is `this` matrix and `R` the reflection matrix,
        then the new matrix will be `M * R`. So when transforming a
        vector `v` with the new matrix by using `M * R * v`, the
        reflection will be applied first!

        Arguments
        - normal: the plane normal
        - point: a point on the plane
        - dest: will hold the result

        Returns
        - dest
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
        
        Reference: <a href="http://www.songho.ca/opengl/gl_projectionmatrix.html#ortho">http://www.songho.ca</a>

        Arguments
        - width: the distance between the right and left frustum edges
        - height: the distance between the top and bottom frustum edges
        - zNear: near clipping plane distance
        - zFar: far clipping plane distance
        - dest: will hold the result

        Returns
        - dest
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
        
        Reference: <a href="http://www.songho.ca/opengl/gl_projectionmatrix.html#ortho">http://www.songho.ca</a>

        Arguments
        - width: the distance between the right and left frustum edges
        - height: the distance between the top and bottom frustum edges
        - zNear: near clipping plane distance
        - zFar: far clipping plane distance
        - dest: will hold the result

        Returns
        - dest
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
        - .ortho(double, double, double, double, double, double, Matrix4x3d)
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
        - .orthoLH(double, double, double, double, double, double, Matrix4x3d)
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
        .lookAt(Vector3dc, Vector3dc, Vector3dc, Matrix4x3d) lookAt
        with `eye = (0, 0, 0)` and `center = dir`.

        Arguments
        - dir: the direction in space to look along
        - up: the direction of 'up'
        - dest: will hold the result

        Returns
        - dest

        See
        - .lookAt(Vector3dc, Vector3dc, Vector3dc, Matrix4x3d)
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
        .lookAt(double, double, double, double, double, double, double, double, double, Matrix4x3d) lookAt()
        with `eye = (0, 0, 0)` and `center = dir`.

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
        - .lookAt(double, double, double, double, double, double, double, double, double, Matrix4x3d)
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

        Arguments
        - eye: the position of the camera
        - center: the point in space to look at
        - up: the direction of 'up'
        - dest: will hold the result

        Returns
        - dest

        See
        - .lookAt(double, double, double, double, double, double, double, double, double, Matrix4x3d)
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
        - .lookAt(Vector3dc, Vector3dc, Vector3dc, Matrix4x3d)
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

        Arguments
        - eye: the position of the camera
        - center: the point in space to look at
        - up: the direction of 'up'
        - dest: will hold the result

        Returns
        - dest

        See
        - .lookAtLH(double, double, double, double, double, double, double, double, double, Matrix4x3d)
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
        - .lookAtLH(Vector3dc, Vector3dc, Vector3dc, Matrix4x3d)
        """
        ...


    def frustumPlane(self, which: int, dest: "Vector4d") -> "Vector4d":
        """
        Calculate a frustum plane of `this` matrix, which
        can be a projection matrix or a combined modelview-projection matrix, and store the result
        in the given `dest`.
        
        Generally, this method computes the frustum plane in the local frame of
        any coordinate system that existed before `this`
        transformation was applied to it in order to yield homogeneous clipping space.
        
        The plane normal, which is `(a, b, c)`, is directed "inwards" of the frustum.
        Any plane/point test using `a*x + b*y + c*z + d` therefore will yield a result greater than zero
        if the point is within the frustum (i.e. at the *positive* side of the frustum plane).
        
        Reference: <a href="http://gamedevs.org/uploads/fast-extraction-viewing-frustum-planes-from-world-view-projection-matrix.pdf">
        Fast Extraction of Viewing Frustum Planes from the World-View-Projection Matrix</a>

        Arguments
        - which: one of the six possible planes, given as numeric constants
                 .PLANE_NX, .PLANE_PX,
                 .PLANE_NY, .PLANE_PY, 
                 .PLANE_NZ and .PLANE_PZ
        - dest: will hold the computed plane equation.
                 The plane equation will be normalized, meaning that `(a, b, c)` will be a unit vector

        Returns
        - dest
        """
        ...


    def positiveZ(self, dir: "Vector3d") -> "Vector3d":
        """
        Obtain the direction of `+Z` before the transformation represented by `this` matrix is applied.
        
        This method uses the rotation component of the left 3x3 submatrix to obtain the direction 
        that is transformed to `+Z` by `this` matrix.
        
        This method is equivalent to the following code:
        ```
        Matrix4x3d inv = new Matrix4x3d(this).invert();
        inv.transformDirection(dir.set(0, 0, 1)).normalize();
        ```
        If `this` is already an orthogonal matrix, then consider using .normalizedPositiveZ(Vector3d) instead.
        
        Reference: <a href="http://www.euclideanspace.com/maths/algebra/matrix/functions/inverse/threeD/">http://www.euclideanspace.com</a>

        Arguments
        - dir: will hold the direction of `+Z`

        Returns
        - dir
        """
        ...


    def normalizedPositiveZ(self, dir: "Vector3d") -> "Vector3d":
        """
        Obtain the direction of `+Z` before the transformation represented by `this` *orthogonal* matrix is applied.
        This method only produces correct results if `this` is an *orthogonal* matrix.
        
        This method uses the rotation component of the left 3x3 submatrix to obtain the direction 
        that is transformed to `+Z` by `this` matrix.
        
        This method is equivalent to the following code:
        ```
        Matrix4x3d inv = new Matrix4x3d(this).transpose();
        inv.transformDirection(dir.set(0, 0, 1)).normalize();
        ```
        
        Reference: <a href="http://www.euclideanspace.com/maths/algebra/matrix/functions/inverse/threeD/">http://www.euclideanspace.com</a>

        Arguments
        - dir: will hold the direction of `+Z`

        Returns
        - dir
        """
        ...


    def positiveX(self, dir: "Vector3d") -> "Vector3d":
        """
        Obtain the direction of `+X` before the transformation represented by `this` matrix is applied.
        
        This method uses the rotation component of the left 3x3 submatrix to obtain the direction 
        that is transformed to `+X` by `this` matrix.
        
        This method is equivalent to the following code:
        ```
        Matrix4x3d inv = new Matrix4x3d(this).invert();
        inv.transformDirection(dir.set(1, 0, 0)).normalize();
        ```
        If `this` is already an orthogonal matrix, then consider using .normalizedPositiveX(Vector3d) instead.
        
        Reference: <a href="http://www.euclideanspace.com/maths/algebra/matrix/functions/inverse/threeD/">http://www.euclideanspace.com</a>

        Arguments
        - dir: will hold the direction of `+X`

        Returns
        - dir
        """
        ...


    def normalizedPositiveX(self, dir: "Vector3d") -> "Vector3d":
        """
        Obtain the direction of `+X` before the transformation represented by `this` *orthogonal* matrix is applied.
        This method only produces correct results if `this` is an *orthogonal* matrix.
        
        This method uses the rotation component of the left 3x3 submatrix to obtain the direction 
        that is transformed to `+X` by `this` matrix.
        
        This method is equivalent to the following code:
        ```
        Matrix4x3d inv = new Matrix4x3d(this).transpose();
        inv.transformDirection(dir.set(1, 0, 0)).normalize();
        ```
        
        Reference: <a href="http://www.euclideanspace.com/maths/algebra/matrix/functions/inverse/threeD/">http://www.euclideanspace.com</a>

        Arguments
        - dir: will hold the direction of `+X`

        Returns
        - dir
        """
        ...


    def positiveY(self, dir: "Vector3d") -> "Vector3d":
        """
        Obtain the direction of `+Y` before the transformation represented by `this` matrix is applied.
        
        This method uses the rotation component of the left 3x3 submatrix to obtain the direction 
        that is transformed to `+Y` by `this` matrix.
        
        This method is equivalent to the following code:
        ```
        Matrix4x3d inv = new Matrix4x3d(this).invert();
        inv.transformDirection(dir.set(0, 1, 0)).normalize();
        ```
        If `this` is already an orthogonal matrix, then consider using .normalizedPositiveY(Vector3d) instead.
        
        Reference: <a href="http://www.euclideanspace.com/maths/algebra/matrix/functions/inverse/threeD/">http://www.euclideanspace.com</a>

        Arguments
        - dir: will hold the direction of `+Y`

        Returns
        - dir
        """
        ...


    def normalizedPositiveY(self, dir: "Vector3d") -> "Vector3d":
        """
        Obtain the direction of `+Y` before the transformation represented by `this` *orthogonal* matrix is applied.
        This method only produces correct results if `this` is an *orthogonal* matrix.
        
        This method uses the rotation component of the left 3x3 submatrix to obtain the direction 
        that is transformed to `+Y` by `this` matrix.
        
        This method is equivalent to the following code:
        ```
        Matrix4x3d inv = new Matrix4x3d(this).transpose();
        inv.transformDirection(dir.set(0, 1, 0)).normalize();
        ```
        
        Reference: <a href="http://www.euclideanspace.com/maths/algebra/matrix/functions/inverse/threeD/">http://www.euclideanspace.com</a>

        Arguments
        - dir: will hold the direction of `+Y`

        Returns
        - dir
        """
        ...


    def origin(self, origin: "Vector3d") -> "Vector3d":
        """
        Obtain the position that gets transformed to the origin by `this` matrix.
        This can be used to get the position of the "camera" from a given *view* transformation matrix.
        
        This method is equivalent to the following code:
        ```
        Matrix4x3f inv = new Matrix4x3f(this).invert();
        inv.transformPosition(origin.set(0, 0, 0));
        ```

        Arguments
        - origin: will hold the position transformed to the origin

        Returns
        - origin
        """
        ...


    def shadow(self, light: "Vector4dc", a: float, b: float, c: float, d: float, dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Apply a projection transformation to this matrix that projects onto the plane specified via the general plane equation
        `x*a + y*b + z*c + d = 0` as if casting a shadow from a given light position/direction `light`
        and store the result in `dest`.
        
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
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def shadow(self, lightX: float, lightY: float, lightZ: float, lightW: float, a: float, b: float, c: float, d: float, dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Apply a projection transformation to this matrix that projects onto the plane specified via the general plane equation
        `x*a + y*b + z*c + d = 0` as if casting a shadow from a given light position/direction `(lightX, lightY, lightZ, lightW)`
        and store the result in `dest`.
        
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
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def shadow(self, light: "Vector4dc", planeTransform: "Matrix4x3dc", dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Apply a projection transformation to this matrix that projects onto the plane with the general plane equation
        `y = 0` as if casting a shadow from a given light position/direction `light`
        and store the result in `dest`.
        
        Before the shadow projection is applied, the plane is transformed via the specified `planeTransformation`.
        
        If `light.w` is `0.0` the light is being treated as a directional light; if it is `1.0` it is a point light.
        
        If `M` is `this` matrix and `S` the shadow matrix,
        then the new matrix will be `M * S`. So when transforming a
        vector `v` with the new matrix by using `M * S * v`, the
        shadow projection will be applied first!

        Arguments
        - light: the light's vector
        - planeTransform: the transformation to transform the implied plane `y = 0` before applying the projection
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def shadow(self, lightX: float, lightY: float, lightZ: float, lightW: float, planeTransform: "Matrix4x3dc", dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Apply a projection transformation to this matrix that projects onto the plane with the general plane equation
        `y = 0` as if casting a shadow from a given light position/direction `(lightX, lightY, lightZ, lightW)`
        and store the result in `dest`.
        
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
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def pick(self, x: float, y: float, width: float, height: float, viewport: list[int], dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Apply a picking transformation to this matrix using the given window coordinates `(x, y)` as the pick center
        and the given `(width, height)` as the size of the picking region in window coordinates, and store the result
        in `dest`.

        Arguments
        - x: the x coordinate of the picking region center in window coordinates
        - y: the y coordinate of the picking region center in window coordinates
        - width: the width of the picking region in window coordinates
        - height: the height of the picking region in window coordinates
        - viewport: the viewport described by `[x, y, width, height]`
        - dest: the destination matrix, which will hold the result

        Returns
        - dest
        """
        ...


    def arcball(self, radius: float, centerX: float, centerY: float, centerZ: float, angleX: float, angleY: float, dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Apply an arcball view transformation to this matrix with the given `radius` and center `(centerX, centerY, centerZ)`
        position of the arcball and the specified X and Y rotation angles, and store the result in `dest`.
        
        This method is equivalent to calling: `translate(0, 0, -radius, dest).rotateX(angleX).rotateY(angleY).translate(-centerX, -centerY, -centerZ)`

        Arguments
        - radius: the arcball radius
        - centerX: the x coordinate of the center position of the arcball
        - centerY: the y coordinate of the center position of the arcball
        - centerZ: the z coordinate of the center position of the arcball
        - angleX: the rotation angle around the X axis in radians
        - angleY: the rotation angle around the Y axis in radians
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def arcball(self, radius: float, center: "Vector3dc", angleX: float, angleY: float, dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Apply an arcball view transformation to this matrix with the given `radius` and `center`
        position of the arcball and the specified X and Y rotation angles, and store the result in `dest`.
        
        This method is equivalent to calling: `translate(0, 0, -radius).rotateX(angleX).rotateY(angleY).translate(-center.x, -center.y, -center.z)`

        Arguments
        - radius: the arcball radius
        - center: the center position of the arcball
        - angleX: the rotation angle around the X axis in radians
        - angleY: the rotation angle around the Y axis in radians
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def transformAab(self, minX: float, minY: float, minZ: float, maxX: float, maxY: float, maxZ: float, outMin: "Vector3d", outMax: "Vector3d") -> "Matrix4x3d":
        """
        Transform the axis-aligned box given as the minimum corner `(minX, minY, minZ)` and maximum corner `(maxX, maxY, maxZ)`
        by `this` matrix and compute the axis-aligned box of the result whose minimum corner is stored in `outMin`
        and maximum corner stored in `outMax`.
        
        Reference: <a href="http://dev.theomader.com/transform-bounding-boxes/">http://dev.theomader.com</a>

        Arguments
        - minX: the x coordinate of the minimum corner of the axis-aligned box
        - minY: the y coordinate of the minimum corner of the axis-aligned box
        - minZ: the z coordinate of the minimum corner of the axis-aligned box
        - maxX: the x coordinate of the maximum corner of the axis-aligned box
        - maxY: the y coordinate of the maximum corner of the axis-aligned box
        - maxZ: the y coordinate of the maximum corner of the axis-aligned box
        - outMin: will hold the minimum corner of the resulting axis-aligned box
        - outMax: will hold the maximum corner of the resulting axis-aligned box

        Returns
        - this
        """
        ...


    def transformAab(self, min: "Vector3dc", max: "Vector3dc", outMin: "Vector3d", outMax: "Vector3d") -> "Matrix4x3d":
        """
        Transform the axis-aligned box given as the minimum corner `min` and maximum corner `max`
        by `this` matrix and compute the axis-aligned box of the result whose minimum corner is stored in `outMin`
        and maximum corner stored in `outMax`.

        Arguments
        - min: the minimum corner of the axis-aligned box
        - max: the maximum corner of the axis-aligned box
        - outMin: will hold the minimum corner of the resulting axis-aligned box
        - outMax: will hold the maximum corner of the resulting axis-aligned box

        Returns
        - this
        """
        ...


    def lerp(self, other: "Matrix4x3dc", t: float, dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Linearly interpolate `this` and `other` using the given interpolation factor `t`
        and store the result in `dest`.
        
        If `t` is `0.0` then the result is `this`. If the interpolation factor is `1.0`
        then the result is `other`.

        Arguments
        - other: the other matrix
        - t: the interpolation factor between 0.0 and 1.0
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def rotateTowards(self, dir: "Vector3dc", up: "Vector3dc", dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Apply a model transformation to this matrix for a right-handed coordinate system, 
        that aligns the `-z` axis with `dir`
        and store the result in `dest`.
        
        If `M` is `this` matrix and `L` the lookat matrix,
        then the new matrix will be `M * L`. So when transforming a
        vector `v` with the new matrix by using `M * L * v`,
        the lookat transformation will be applied first!
        
        This method is equivalent to calling: `mul(new Matrix4x3d().lookAt(new Vector3d(), new Vector3d(dir).negate(), up).invert(), dest)`

        Arguments
        - dir: the direction to rotate towards
        - up: the up vector
        - dest: will hold the result

        Returns
        - dest

        See
        - .rotateTowards(double, double, double, double, double, double, Matrix4x3d)
        """
        ...


    def rotateTowards(self, dirX: float, dirY: float, dirZ: float, upX: float, upY: float, upZ: float, dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Apply a model transformation to this matrix for a right-handed coordinate system, 
        that aligns the `-z` axis with `(dirX, dirY, dirZ)`
        and store the result in `dest`.
        
        If `M` is `this` matrix and `L` the lookat matrix,
        then the new matrix will be `M * L`. So when transforming a
        vector `v` with the new matrix by using `M * L * v`,
        the lookat transformation will be applied first!
        
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
        - .rotateTowards(Vector3dc, Vector3dc, Matrix4x3d)
        """
        ...


    def getEulerAnglesXYZ(self, dest: "Vector3d") -> "Vector3d":
        """
        Extract the Euler angles from the rotation represented by the left 3x3 submatrix of `this`
        and store the extracted Euler angles in `dest`.
        
        This method assumes that the left 3x3 submatrix of `this` only represents a rotation without scaling.
        
        The Euler angles are always returned as the angle around X in the Vector3d.x field, the angle around Y in the Vector3d.y
        field and the angle around Z in the Vector3d.z field of the supplied Vector3d instance.
        
        Note that the returned Euler angles must be applied in the order `X * Y * Z` to obtain the identical matrix.
        This means that calling Matrix4x3d.rotateXYZ(double, double, double) using the obtained Euler angles will yield
        the same rotation as the original matrix from which the Euler angles were obtained, so in the below code the matrix
        `m2` should be identical to `m` (disregarding possible floating-point inaccuracies).
        ```
        Matrix4x3d m = ...; // &lt;- matrix only representing rotation
        Matrix4x3d n = new Matrix4x3d();
        n.rotateXYZ(m.getEulerAnglesXYZ(new Vector3d()));
        ```
        
        Reference: <a href="https://en.wikipedia.org/wiki/Euler_angles#Rotation_matrix">http://en.wikipedia.org/</a>

        Arguments
        - dest: will hold the extracted Euler angles

        Returns
        - dest
        """
        ...


    def getEulerAnglesZYX(self, dest: "Vector3d") -> "Vector3d":
        """
        Extract the Euler angles from the rotation represented by the left 3x3 submatrix of `this`
        and store the extracted Euler angles in `dest`.
        
        This method assumes that the left 3x3 submatrix of `this` only represents a rotation without scaling.
        
        The Euler angles are always returned as the angle around X in the Vector3d.x field, the angle around Y in the Vector3d.y
        field and the angle around Z in the Vector3d.z field of the supplied Vector3d instance.
        
        Note that the returned Euler angles must be applied in the order `Z * Y * X` to obtain the identical matrix.
        This means that calling Matrix4x3d.rotateZYX(double, double, double) using the obtained Euler angles will yield
        the same rotation as the original matrix from which the Euler angles were obtained, so in the below code the matrix
        `m2` should be identical to `m` (disregarding possible floating-point inaccuracies).
        ```
        Matrix4x3d m = ...; // &lt;- matrix only representing rotation
        Matrix4x3d n = new Matrix4x3d();
        n.rotateZYX(m.getEulerAnglesZYX(new Vector3d()));
        ```
        
        Reference: <a href="https://en.wikipedia.org/wiki/Euler_angles#Rotation_matrix">http://en.wikipedia.org/</a>

        Arguments
        - dest: will hold the extracted Euler angles

        Returns
        - dest
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


    def mapXZY(self, dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Multiply `this` by the matrix
        ```
        1 0 0 0
        0 0 1 0
        0 1 0 0
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapXZnY(self, dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Multiply `this` by the matrix
        ```
        1 0  0 0
        0 0 -1 0
        0 1  0 0
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapXnYnZ(self, dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Multiply `this` by the matrix
        ```
        1  0  0 0
        0 -1  0 0
        0  0 -1 0
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapXnZY(self, dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Multiply `this` by the matrix
        ```
        1  0 0 0
        0  0 1 0
        0 -1 0 0
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapXnZnY(self, dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Multiply `this` by the matrix
        ```
        1  0  0 0
        0  0 -1 0
        0 -1  0 0
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapYXZ(self, dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Multiply `this` by the matrix
        ```
        0 1 0 0
        1 0 0 0
        0 0 1 0
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapYXnZ(self, dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Multiply `this` by the matrix
        ```
        0 1  0 0
        1 0  0 0
        0 0 -1 0
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapYZX(self, dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Multiply `this` by the matrix
        ```
        0 0 1 0
        1 0 0 0
        0 1 0 0
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapYZnX(self, dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Multiply `this` by the matrix
        ```
        0 0 -1 0
        1 0  0 0
        0 1  0 0
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapYnXZ(self, dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Multiply `this` by the matrix
        ```
        0 -1 0 0
        1  0 0 0
        0  0 1 0
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapYnXnZ(self, dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Multiply `this` by the matrix
        ```
        0 -1  0 0
        1  0  0 0
        0  0 -1 0
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapYnZX(self, dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Multiply `this` by the matrix
        ```
        0  0 1 0
        1  0 0 0
        0 -1 0 0
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapYnZnX(self, dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Multiply `this` by the matrix
        ```
        0  0 -1 0
        1  0  0 0
        0 -1  0 0
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapZXY(self, dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Multiply `this` by the matrix
        ```
        0 1 0 0
        0 0 1 0
        1 0 0 0
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapZXnY(self, dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Multiply `this` by the matrix
        ```
        0 1  0 0
        0 0 -1 0
        1 0  0 0
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapZYX(self, dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Multiply `this` by the matrix
        ```
        0 0 1 0
        0 1 0 0
        1 0 0 0
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapZYnX(self, dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Multiply `this` by the matrix
        ```
        0 0 -1 0
        0 1  0 0
        1 0  0 0
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapZnXY(self, dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Multiply `this` by the matrix
        ```
        0 -1 0 0
        0  0 1 0
        1  0 0 0
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapZnXnY(self, dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Multiply `this` by the matrix
        ```
        0 -1  0 0
        0  0 -1 0
        1  0  0 0
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapZnYX(self, dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Multiply `this` by the matrix
        ```
        0  0 1 0
        0 -1 0 0
        1  0 0 0
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapZnYnX(self, dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Multiply `this` by the matrix
        ```
        0  0 -1 0
        0 -1  0 0
        1  0  0 0
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapnXYnZ(self, dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Multiply `this` by the matrix
        ```
        -1 0  0 0
         0 1  0 0
         0 0 -1 0
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapnXZY(self, dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Multiply `this` by the matrix
        ```
        -1 0 0 0
         0 0 1 0
         0 1 0 0
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapnXZnY(self, dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Multiply `this` by the matrix
        ```
        -1 0  0 0
         0 0 -1 0
         0 1  0 0
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapnXnYZ(self, dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Multiply `this` by the matrix
        ```
        -1  0 0 0
         0 -1 0 0
         0  0 1 0
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapnXnYnZ(self, dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Multiply `this` by the matrix
        ```
        -1  0  0 0
         0 -1  0 0
         0  0 -1 0
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapnXnZY(self, dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Multiply `this` by the matrix
        ```
        -1  0 0 0
         0  0 1 0
         0 -1 0 0
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapnXnZnY(self, dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Multiply `this` by the matrix
        ```
        -1  0  0 0
         0  0 -1 0
         0 -1  0 0
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapnYXZ(self, dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Multiply `this` by the matrix
        ```
         0 1 0 0
        -1 0 0 0
         0 0 1 0
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapnYXnZ(self, dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Multiply `this` by the matrix
        ```
         0 1  0 0
        -1 0  0 0
         0 0 -1 0
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapnYZX(self, dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Multiply `this` by the matrix
        ```
         0 0 1 0
        -1 0 0 0
         0 1 0 0
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapnYZnX(self, dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Multiply `this` by the matrix
        ```
         0 0 -1 0
        -1 0  0 0
         0 1  0 0
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapnYnXZ(self, dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Multiply `this` by the matrix
        ```
         0 -1 0 0
        -1  0 0 0
         0  0 1 0
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapnYnXnZ(self, dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Multiply `this` by the matrix
        ```
         0 -1  0 0
        -1  0  0 0
         0  0 -1 0
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapnYnZX(self, dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Multiply `this` by the matrix
        ```
         0  0 1 0
        -1  0 0 0
         0 -1 0 0
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapnYnZnX(self, dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Multiply `this` by the matrix
        ```
         0  0 -1 0
        -1  0  0 0
         0 -1  0 0
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapnZXY(self, dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Multiply `this` by the matrix
        ```
         0 1 0 0
         0 0 1 0
        -1 0 0 0
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapnZXnY(self, dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Multiply `this` by the matrix
        ```
         0 1  0 0
         0 0 -1 0
        -1 0  0 0
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapnZYX(self, dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Multiply `this` by the matrix
        ```
         0 0 1 0
         0 1 0 0
        -1 0 0 0
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapnZYnX(self, dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Multiply `this` by the matrix
        ```
         0 0 -1 0
         0 1  0 0
        -1 0  0 0
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapnZnXY(self, dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Multiply `this` by the matrix
        ```
         0 -1 0 0
         0  0 1 0
        -1  0 0 0
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapnZnXnY(self, dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Multiply `this` by the matrix
        ```
         0 -1  0 0
         0  0 -1 0
        -1  0  0 0
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapnZnYX(self, dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Multiply `this` by the matrix
        ```
         0  0 1 0
         0 -1 0 0
        -1  0 0 0
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapnZnYnX(self, dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Multiply `this` by the matrix
        ```
         0  0 -1 0
         0 -1  0 0
        -1  0  0 0
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def negateX(self, dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Multiply `this` by the matrix
        ```
        -1 0 0 0
         0 1 0 0
         0 0 1 0
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def negateY(self, dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Multiply `this` by the matrix
        ```
        1  0 0 0
        0 -1 0 0
        0  0 1 0
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def negateZ(self, dest: "Matrix4x3d") -> "Matrix4x3d":
        """
        Multiply `this` by the matrix
        ```
        1 0  0 0
        0 1  0 0
        0 0 -1 0
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def equals(self, m: "Matrix4x3dc", delta: float) -> bool:
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
