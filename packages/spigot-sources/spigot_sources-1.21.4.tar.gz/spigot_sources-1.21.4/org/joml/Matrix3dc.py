"""
Python module generated from Java source file org.joml.Matrix3dc

Java source file obtained from artifact joml version 1.10.8

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util import *
from org.joml import *
from typing import Any, Callable, Iterable, Tuple


class Matrix3dc:
    """
    Interface to a read-only view of a 3x3 matrix of double-precision floats.

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


    def mul(self, right: "Matrix3dc", dest: "Matrix3d") -> "Matrix3d":
        """
        Multiply this matrix by the supplied matrix and store the result in `dest`.
        This matrix will be the left one.
        
        If `M` is `this` matrix and `R` the `right` matrix,
        then the new matrix will be `M * R`. So when transforming a
        vector `v` with the new matrix by using `M * R * v`, the
        transformation of the right matrix will be applied first!

        Arguments
        - right: the right operand
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mulLocal(self, left: "Matrix3dc", dest: "Matrix3d") -> "Matrix3d":
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


    def mul(self, right: "Matrix3fc", dest: "Matrix3d") -> "Matrix3d":
        """
        Multiply this matrix by the supplied matrix and store the result in `dest`.
        This matrix will be the left one.
        
        If `M` is `this` matrix and `R` the `right` matrix,
        then the new matrix will be `M * R`. So when transforming a
        vector `v` with the new matrix by using `M * R * v`, the
        transformation of the right matrix will be applied first!

        Arguments
        - right: the right operand
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


    def invert(self, dest: "Matrix3d") -> "Matrix3d":
        """
        Invert `this` matrix and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def transpose(self, dest: "Matrix3d") -> "Matrix3d":
        """
        Transpose `this` matrix and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def get(self, dest: "Matrix3d") -> "Matrix3d":
        """
        Get the current values of `this` matrix and store them into
        `dest`.

        Arguments
        - dest: the destination matrix

        Returns
        - the passed in destination
        """
        ...


    def getRotation(self, dest: "AxisAngle4f") -> "AxisAngle4f":
        """
        Get the current values of `this` matrix and store the represented rotation
        into the given AxisAngle4f.

        Arguments
        - dest: the destination AxisAngle4f

        Returns
        - the passed in destination

        See
        - AxisAngle4f.set(Matrix3dc)
        """
        ...


    def getUnnormalizedRotation(self, dest: "Quaternionf") -> "Quaternionf":
        """
        Get the current values of `this` matrix and store the represented rotation
        into the given Quaternionf.
        
        This method assumes that the three column vectors of this matrix are not normalized and
        thus allows to ignore any additional scaling factor that is applied to the matrix.

        Arguments
        - dest: the destination Quaternionf

        Returns
        - the passed in destination

        See
        - Quaternionf.setFromUnnormalized(Matrix3dc)
        """
        ...


    def getNormalizedRotation(self, dest: "Quaternionf") -> "Quaternionf":
        """
        Get the current values of `this` matrix and store the represented rotation
        into the given Quaternionf.
        
        This method assumes that the three column vectors of this matrix are normalized.

        Arguments
        - dest: the destination Quaternionf

        Returns
        - the passed in destination

        See
        - Quaternionf.setFromNormalized(Matrix3dc)
        """
        ...


    def getUnnormalizedRotation(self, dest: "Quaterniond") -> "Quaterniond":
        """
        Get the current values of `this` matrix and store the represented rotation
        into the given Quaterniond.
        
        This method assumes that the three column vectors of this matrix are not normalized and
        thus allows to ignore any additional scaling factor that is applied to the matrix.

        Arguments
        - dest: the destination Quaterniond

        Returns
        - the passed in destination

        See
        - Quaterniond.setFromUnnormalized(Matrix3dc)
        """
        ...


    def getNormalizedRotation(self, dest: "Quaterniond") -> "Quaterniond":
        """
        Get the current values of `this` matrix and store the represented rotation
        into the given Quaterniond.
        
        This method assumes that the three column vectors of this matrix are normalized.

        Arguments
        - dest: the destination Quaterniond

        Returns
        - the passed in destination

        See
        - Quaterniond.setFromNormalized(Matrix3dc)
        """
        ...


    def get(self, buffer: "DoubleBuffer") -> "DoubleBuffer":
        """
        Store this matrix into the supplied DoubleBuffer at the current
        buffer DoubleBuffer.position() position using column-major order.
        
        This method will not increment the position of the given DoubleBuffer.
        
        In order to specify the offset into the DoubleBuffer} at which
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
        Store this matrix into the supplied DoubleBuffer starting at the specified
        absolute buffer position/index using column-major order.
        
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
        
        This method will not increment the position of the given FloatBuffer.
        
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


    def getToAddress(self, address: int) -> "Matrix3dc":
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


    def getTransposedToAddress(self, address: int) -> "Matrix3dc":
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


    def scale(self, xyz: "Vector3dc", dest: "Matrix3d") -> "Matrix3d":
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


    def scale(self, x: float, y: float, z: float, dest: "Matrix3d") -> "Matrix3d":
        """
        Apply scaling to this matrix by scaling the base axes by the given x,
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


    def scale(self, xyz: float, dest: "Matrix3d") -> "Matrix3d":
        """
        Apply scaling to this matrix by uniformly scaling all base axes by the given `xyz` factor
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
        - .scale(double, double, double, Matrix3d)
        """
        ...


    def scaleLocal(self, x: float, y: float, z: float, dest: "Matrix3d") -> "Matrix3d":
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


    def transform(self, v: "Vector3d") -> "Vector3d":
        """
        Transform the given vector by this matrix.

        Arguments
        - v: the vector to transform

        Returns
        - v
        """
        ...


    def transform(self, v: "Vector3dc", dest: "Vector3d") -> "Vector3d":
        """
        Transform the given vector by this matrix and store the result in `dest`.

        Arguments
        - v: the vector to transform
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def transform(self, v: "Vector3f") -> "Vector3f":
        """
        Transform the given vector by this matrix.

        Arguments
        - v: the vector to transform

        Returns
        - v
        """
        ...


    def transform(self, v: "Vector3fc", dest: "Vector3f") -> "Vector3f":
        """
        Transform the given vector by this matrix and store the result in `dest`.

        Arguments
        - v: the vector to transform
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def transform(self, x: float, y: float, z: float, dest: "Vector3d") -> "Vector3d":
        """
        Transform the vector `(x, y, z)` by this matrix and store the result in `dest`.

        Arguments
        - x: the x coordinate of the vector to transform
        - y: the y coordinate of the vector to transform
        - z: the z coordinate of the vector to transform
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def transformTranspose(self, v: "Vector3d") -> "Vector3d":
        """
        Transform the given vector by the transpose of this matrix.

        Arguments
        - v: the vector to transform

        Returns
        - v
        """
        ...


    def transformTranspose(self, v: "Vector3dc", dest: "Vector3d") -> "Vector3d":
        """
        Transform the given vector by the transpose of this matrix and store the result in `dest`.

        Arguments
        - v: the vector to transform
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def transformTranspose(self, x: float, y: float, z: float, dest: "Vector3d") -> "Vector3d":
        """
        Transform the vector `(x, y, z)` by the transpose of this matrix and store the result in `dest`.

        Arguments
        - x: the x coordinate of the vector to transform
        - y: the y coordinate of the vector to transform
        - z: the z coordinate of the vector to transform
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def rotateX(self, ang: float, dest: "Matrix3d") -> "Matrix3d":
        """
        Apply rotation about the X axis to this matrix by rotating the given amount of radians
        and store the result in `dest`.
        
        When used with a right-handed coordinate system, the produced rotation will rotate a vector 
        counter-clockwise around the rotation axis, when viewing along the negative axis direction towards the origin.
        When used with a left-handed coordinate system, the rotation is clockwise.
        
        If `M` is `this` matrix and `R` the rotation matrix,
        then the new matrix will be `M * R`. So when transforming a
        vector `v` with the new matrix by using `M * R * v`
        , the rotation will be applied first!
        
        Reference: <a href="http://en.wikipedia.org/wiki/Rotation_matrix#Basic_rotations">http://en.wikipedia.org</a>

        Arguments
        - ang: the angle in radians
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def rotateY(self, ang: float, dest: "Matrix3d") -> "Matrix3d":
        """
        Apply rotation about the Y axis to this matrix by rotating the given amount of radians
        and store the result in `dest`.
        
        When used with a right-handed coordinate system, the produced rotation will rotate a vector 
        counter-clockwise around the rotation axis, when viewing along the negative axis direction towards the origin.
        When used with a left-handed coordinate system, the rotation is clockwise.
        
        If `M` is `this` matrix and `R` the rotation matrix,
        then the new matrix will be `M * R`. So when transforming a
        vector `v` with the new matrix by using `M * R * v`
        , the rotation will be applied first!
        
        Reference: <a href="http://en.wikipedia.org/wiki/Rotation_matrix#Basic_rotations">http://en.wikipedia.org</a>

        Arguments
        - ang: the angle in radians
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def rotateZ(self, ang: float, dest: "Matrix3d") -> "Matrix3d":
        """
        Apply rotation about the Z axis to this matrix by rotating the given amount of radians
        and store the result in `dest`.
        
        When used with a right-handed coordinate system, the produced rotation will rotate a vector 
        counter-clockwise around the rotation axis, when viewing along the negative axis direction towards the origin.
        When used with a left-handed coordinate system, the rotation is clockwise.
        
        If `M` is `this` matrix and `R` the rotation matrix,
        then the new matrix will be `M * R`. So when transforming a
        vector `v` with the new matrix by using `M * R * v`
        , the rotation will be applied first!
        
        Reference: <a href="http://en.wikipedia.org/wiki/Rotation_matrix#Basic_rotations">http://en.wikipedia.org</a>

        Arguments
        - ang: the angle in radians
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def rotateXYZ(self, angleX: float, angleY: float, angleZ: float, dest: "Matrix3d") -> "Matrix3d":
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


    def rotateZYX(self, angleZ: float, angleY: float, angleX: float, dest: "Matrix3d") -> "Matrix3d":
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


    def rotateYXZ(self, angleY: float, angleX: float, angleZ: float, dest: "Matrix3d") -> "Matrix3d":
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


    def rotate(self, ang: float, x: float, y: float, z: float, dest: "Matrix3d") -> "Matrix3d":
        """
        Apply rotation to this matrix by rotating the given amount of radians
        about the given axis specified as x, y and z components, and store the result in `dest`.
        
        The axis described by the three components needs to be a unit vector.
        
        When used with a right-handed coordinate system, the produced rotation will rotate a vector 
        counter-clockwise around the rotation axis, when viewing along the negative axis direction towards the origin.
        When used with a left-handed coordinate system, the rotation is clockwise.
        
        If `M` is `this` matrix and `R` the rotation matrix,
        then the new matrix will be `M * R`. So when transforming a
        vector `v` with the new matrix by using `M * R * v`
        , the rotation will be applied first!
        
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


    def rotateLocal(self, ang: float, x: float, y: float, z: float, dest: "Matrix3d") -> "Matrix3d":
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


    def rotateLocalX(self, ang: float, dest: "Matrix3d") -> "Matrix3d":
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
        
        Reference: <a href="http://en.wikipedia.org/wiki/Rotation_matrix#Rotation_matrix_from_axis_and_angle">http://en.wikipedia.org</a>

        Arguments
        - ang: the angle in radians to rotate about the X axis
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def rotateLocalY(self, ang: float, dest: "Matrix3d") -> "Matrix3d":
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
        
        Reference: <a href="http://en.wikipedia.org/wiki/Rotation_matrix#Rotation_matrix_from_axis_and_angle">http://en.wikipedia.org</a>

        Arguments
        - ang: the angle in radians to rotate about the Y axis
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def rotateLocalZ(self, ang: float, dest: "Matrix3d") -> "Matrix3d":
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
        
        Reference: <a href="http://en.wikipedia.org/wiki/Rotation_matrix#Rotation_matrix_from_axis_and_angle">http://en.wikipedia.org</a>

        Arguments
        - ang: the angle in radians to rotate about the Z axis
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def rotateLocal(self, quat: "Quaterniondc", dest: "Matrix3d") -> "Matrix3d":
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


    def rotateLocal(self, quat: "Quaternionfc", dest: "Matrix3d") -> "Matrix3d":
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


    def rotate(self, quat: "Quaterniondc", dest: "Matrix3d") -> "Matrix3d":
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


    def rotate(self, quat: "Quaternionfc", dest: "Matrix3d") -> "Matrix3d":
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


    def rotate(self, axisAngle: "AxisAngle4f", dest: "Matrix3d") -> "Matrix3d":
        """
        Apply a rotation transformation, rotating about the given AxisAngle4f and store the result in `dest`.
        
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
        - .rotate(double, double, double, double, Matrix3d)
        """
        ...


    def rotate(self, axisAngle: "AxisAngle4d", dest: "Matrix3d") -> "Matrix3d":
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
        - .rotate(double, double, double, double, Matrix3d)
        """
        ...


    def rotate(self, angle: float, axis: "Vector3dc", dest: "Matrix3d") -> "Matrix3d":
        """
        Apply a rotation transformation, rotating the given radians about the specified axis and store the result in `dest`.
        
        The axis described by the `axis` vector needs to be a unit vector.
        
        When used with a right-handed coordinate system, the produced rotation will rotate a vector 
        counter-clockwise around the rotation axis, when viewing along the negative axis direction towards the origin.
        When used with a left-handed coordinate system, the rotation is clockwise.
        
        If `M` is `this` matrix and `A` the rotation matrix obtained from the given axis and angle,
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
        - .rotate(double, double, double, double, Matrix3d)
        """
        ...


    def rotate(self, angle: float, axis: "Vector3fc", dest: "Matrix3d") -> "Matrix3d":
        """
        Apply a rotation transformation, rotating the given radians about the specified axis and store the result in `dest`.
        
        The axis described by the `axis` vector needs to be a unit vector.
        
        When used with a right-handed coordinate system, the produced rotation will rotate a vector 
        counter-clockwise around the rotation axis, when viewing along the negative axis direction towards the origin.
        When used with a left-handed coordinate system, the rotation is clockwise.
        
        If `M` is `this` matrix and `A` the rotation matrix obtained from the given axis and angle,
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
        - .rotate(double, double, double, double, Matrix3d)
        """
        ...


    def getRow(self, row: int, dest: "Vector3d") -> "Vector3d":
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
        - column: the column index in `[0..2]`
        - dest: will hold the column components

        Returns
        - the passed in destination

        Raises
        - IndexOutOfBoundsException: if `column` is not in `[0..2]`
        """
        ...


    def get(self, column: int, row: int) -> float:
        """
        Get the matrix element value at the given column and row.

        Arguments
        - column: the colum index in `[0..2]`
        - row: the row index in `[0..2]`

        Returns
        - the element value
        """
        ...


    def getRowColumn(self, row: int, column: int) -> float:
        """
        Get the matrix element value at the given row and column.

        Arguments
        - row: the row index in `[0..2]`
        - column: the colum index in `[0..2]`

        Returns
        - the element value
        """
        ...


    def normal(self, dest: "Matrix3d") -> "Matrix3d":
        """
        Compute a normal matrix from `this` matrix and store it into `dest`.
        
        The normal matrix of `m` is the transpose of the inverse of `m`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def cofactor(self, dest: "Matrix3d") -> "Matrix3d":
        """
        Compute the cofactor matrix of `this` and store it into `dest`.
        
        The cofactor matrix can be used instead of .normal(Matrix3d) to transform normals
        when the orientation of the normals with respect to the surface should be preserved.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def lookAlong(self, dir: "Vector3dc", up: "Vector3dc", dest: "Matrix3d") -> "Matrix3d":
        """
        Apply a rotation transformation to this matrix to make `-z` point along `dir`
        and store the result in `dest`. 
        
        If `M` is `this` matrix and `L` the lookalong rotation matrix,
        then the new matrix will be `M * L`. So when transforming a
        vector `v` with the new matrix by using `M * L * v`, the
        lookalong rotation transformation will be applied first!

        Arguments
        - dir: the direction in space to look along
        - up: the direction of 'up'
        - dest: will hold the result

        Returns
        - dest

        See
        - .lookAlong(double, double, double, double, double, double, Matrix3d)
        """
        ...


    def lookAlong(self, dirX: float, dirY: float, dirZ: float, upX: float, upY: float, upZ: float, dest: "Matrix3d") -> "Matrix3d":
        """
        Apply a rotation transformation to this matrix to make `-z` point along `dir`
        and store the result in `dest`. 
        
        If `M` is `this` matrix and `L` the lookalong rotation matrix,
        then the new matrix will be `M * L`. So when transforming a
        vector `v` with the new matrix by using `M * L * v`, the
        lookalong rotation transformation will be applied first!

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


    def positiveZ(self, dir: "Vector3d") -> "Vector3d":
        """
        Obtain the direction of `+Z` before the transformation represented by `this` matrix is applied.
        
        This method is equivalent to the following code:
        ```
        Matrix3d inv = new Matrix3d(this).invert();
        inv.transform(dir.set(0, 0, 1)).normalize();
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
        
        This method is equivalent to the following code:
        ```
        Matrix3d inv = new Matrix3d(this).transpose();
        inv.transform(dir.set(0, 0, 1));
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
        
        This method is equivalent to the following code:
        ```
        Matrix3d inv = new Matrix3d(this).invert();
        inv.transform(dir.set(1, 0, 0)).normalize();
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
        
        This method is equivalent to the following code:
        ```
        Matrix3d inv = new Matrix3d(this).transpose();
        inv.transform(dir.set(1, 0, 0));
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
        
        This method is equivalent to the following code:
        ```
        Matrix3d inv = new Matrix3d(this).invert();
        inv.transform(dir.set(0, 1, 0)).normalize();
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
        
        This method is equivalent to the following code:
        ```
        Matrix3d inv = new Matrix3d(this).transpose();
        inv.transform(dir.set(0, 1, 0));
        ```
        
        Reference: <a href="http://www.euclideanspace.com/maths/algebra/matrix/functions/inverse/threeD/">http://www.euclideanspace.com</a>

        Arguments
        - dir: will hold the direction of `+Y`

        Returns
        - dir
        """
        ...


    def add(self, other: "Matrix3dc", dest: "Matrix3d") -> "Matrix3d":
        """
        Component-wise add `this` and `other` and store the result in `dest`.

        Arguments
        - other: the other addend
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def sub(self, subtrahend: "Matrix3dc", dest: "Matrix3d") -> "Matrix3d":
        """
        Component-wise subtract `subtrahend` from `this` and store the result in `dest`.

        Arguments
        - subtrahend: the subtrahend
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mulComponentWise(self, other: "Matrix3dc", dest: "Matrix3d") -> "Matrix3d":
        """
        Component-wise multiply `this` by `other` and store the result in `dest`.

        Arguments
        - other: the other matrix
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def lerp(self, other: "Matrix3dc", t: float, dest: "Matrix3d") -> "Matrix3d":
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


    def rotateTowards(self, direction: "Vector3dc", up: "Vector3dc", dest: "Matrix3d") -> "Matrix3d":
        """
        Apply a model transformation to this matrix for a right-handed coordinate system, 
        that aligns the local `+Z` axis with `direction`
        and store the result in `dest`.
        
        If `M` is `this` matrix and `L` the lookat matrix,
        then the new matrix will be `M * L`. So when transforming a
        vector `v` with the new matrix by using `M * L * v`,
        the lookat transformation will be applied first!
        
        This method is equivalent to calling: `mul(new Matrix3d().lookAlong(new Vector3d(dir).negate(), up).invert(), dest)`

        Arguments
        - direction: the direction to rotate towards
        - up: the model's up vector
        - dest: will hold the result

        Returns
        - dest

        See
        - .rotateTowards(double, double, double, double, double, double, Matrix3d)
        """
        ...


    def rotateTowards(self, dirX: float, dirY: float, dirZ: float, upX: float, upY: float, upZ: float, dest: "Matrix3d") -> "Matrix3d":
        """
        Apply a model transformation to this matrix for a right-handed coordinate system, 
        that aligns the local `+Z` axis with `dir`
        and store the result in `dest`.
        
        If `M` is `this` matrix and `L` the lookat matrix,
        then the new matrix will be `M * L`. So when transforming a
        vector `v` with the new matrix by using `M * L * v`,
        the lookat transformation will be applied first!
        
        This method is equivalent to calling: `mul(new Matrix3d().lookAlong(-dirX, -dirY, -dirZ, upX, upY, upZ).invert(), dest)`

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
        - .rotateTowards(Vector3dc, Vector3dc, Matrix3d)
        """
        ...


    def getEulerAnglesXYZ(self, dest: "Vector3d") -> "Vector3d":
        """
        Extract the Euler angles from the rotation represented by `this` matrix and store the extracted Euler angles in `dest`.
        
        This method assumes that `this` matrix only represents a rotation without scaling.
        
        The Euler angles are always returned as the angle around X in the Vector3d.x field, the angle around Y in the Vector3d.y
        field and the angle around Z in the Vector3d.z field of the supplied vector.
        
        Note that the returned Euler angles must be applied in the order `X * Y * Z` to obtain the identical matrix.
        This means that calling Matrix3dc.rotateXYZ(double, double, double, Matrix3d) using the obtained Euler angles will yield
        the same rotation as the original matrix from which the Euler angles were obtained, so in the below code the matrix
        `m2` should be identical to `m` (disregarding possible floating-point inaccuracies).
        ```
        Matrix3d m = ...; // &lt;- matrix only representing rotation
        Matrix3d n = new Matrix3d();
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
        Extract the Euler angles from the rotation represented by `this` matrix and store the extracted Euler angles in `dest`.
        
        This method assumes that `this` matrix only represents a rotation without scaling.
        
        The Euler angles are always returned as the angle around X in the Vector3d.x field, the angle around Y in the Vector3d.y
        field and the angle around Z in the Vector3d.z field of the supplied vector.
        
        Note that the returned Euler angles must be applied in the order `Z * Y * X` to obtain the identical matrix.
        This means that calling Matrix3dc.rotateZYX(double, double, double, Matrix3d) using the obtained Euler angles will yield
        the same rotation as the original matrix from which the Euler angles were obtained, so in the below code the matrix
        `m2` should be identical to `m` (disregarding possible floating-point inaccuracies).
        ```
        Matrix3d m = ...; // &lt;- matrix only representing rotation
        Matrix3d n = new Matrix3d();
        n.rotateZYX(m.getEulerAnglesZYX(new Vector3d()));
        ```
        
        Reference: <a href="https://en.wikipedia.org/wiki/Euler_angles#Rotation_matrix">http://en.wikipedia.org/</a>

        Arguments
        - dest: will hold the extracted Euler angles

        Returns
        - dest
        """
        ...


    def getEulerAnglesYXZ(self, dest: "Vector3d") -> "Vector3d":
        """
        Extract the Euler angles from the rotation represented by `this` matrix and store the extracted Euler angles in `dest`.
        
        This method assumes that `this` matrix only represents a rotation without scaling.
        
        The Euler angles are always returned as the angle around X in the Vector3d.x field, the angle around Y in the Vector3d.y
        field and the angle around Z in the Vector3d.z field of the supplied vector.
        
        Note that the returned Euler angles must be applied in the order `Y * X * Z` to obtain the identical matrix.
        This means that calling Matrix3dc.rotateYXZ(double, double, double, Matrix3d) using the obtained Euler angles will yield
        the same rotation as the original matrix from which the Euler angles were obtained, so in the below code the matrix
        `m2` should be identical to `m` (disregarding possible floating-point inaccuracies).
        ```
        Matrix3d m = ...; // &lt;- matrix only representing rotation
        Matrix3d n = new Matrix3d();
        n.rotateYXZ(m.getEulerAnglesYXZ(new Vector3d()));
        ```
        
        Reference: <a href="https://en.wikipedia.org/wiki/Euler_angles#Rotation_matrix">http://en.wikipedia.org/</a>

        Arguments
        - dest: will hold the extracted Euler angles

        Returns
        - dest
        """
        ...


    def obliqueZ(self, a: float, b: float, dest: "Matrix3d") -> "Matrix3d":
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
        1 0 a
        0 1 b
        0 0 1
        ```

        Arguments
        - a: the value for the z factor that applies to x
        - b: the value for the z factor that applies to y
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def equals(self, m: "Matrix3dc", delta: float) -> bool:
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


    def reflect(self, nx: float, ny: float, nz: float, dest: "Matrix3d") -> "Matrix3d":
        """
        Apply a mirror/reflection transformation to this matrix that reflects through the given plane
        specified via the plane normal `(nx, ny, nz)`, and store the result in `dest`.
        
        If `M` is `this` matrix and `R` the reflection matrix,
        then the new matrix will be `M * R`. So when transforming a
        vector `v` with the new matrix by using `M * R * v`, the
        reflection will be applied first!

        Arguments
        - nx: the x-coordinate of the plane normal
        - ny: the y-coordinate of the plane normal
        - nz: the z-coordinate of the plane normal
        - dest: will hold the result

        Returns
        - this
        """
        ...


    def reflect(self, orientation: "Quaterniondc", dest: "Matrix3d") -> "Matrix3d":
        """
        Apply a mirror/reflection transformation to this matrix that reflects through a plane
        specified via the plane orientation, and store the result in `dest`.
        
        This method can be used to build a reflection transformation based on the orientation of a mirror object in the scene.
        It is assumed that the default mirror plane's normal is `(0, 0, 1)`. So, if the given Quaterniondc is
        the identity (does not apply any additional rotation), the reflection plane will be `z=0`.
        
        If `M` is `this` matrix and `R` the reflection matrix,
        then the new matrix will be `M * R`. So when transforming a
        vector `v` with the new matrix by using `M * R * v`, the
        reflection will be applied first!

        Arguments
        - orientation: the plane orientation
        - dest: will hold the result

        Returns
        - this
        """
        ...


    def reflect(self, normal: "Vector3dc", dest: "Matrix3d") -> "Matrix3d":
        """
        Apply a mirror/reflection transformation to this matrix that reflects through the given plane
        specified via the plane normal, and store the result in `dest`.
        
        If `M` is `this` matrix and `R` the reflection matrix,
        then the new matrix will be `M * R`. So when transforming a
        vector `v` with the new matrix by using `M * R * v`, the
        reflection will be applied first!

        Arguments
        - normal: the plane normal
        - dest: will hold the result

        Returns
        - this
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


    def quadraticFormProduct(self, x: float, y: float, z: float) -> float:
        """
        Compute `(x, y, z)^T * this * (x, y, z)`.

        Arguments
        - x: the x coordinate of the vector to multiply
        - y: the y coordinate of the vector to multiply
        - z: the z coordinate of the vector to multiply

        Returns
        - the result
        """
        ...


    def quadraticFormProduct(self, v: "Vector3dc") -> float:
        """
        Compute `v^T * this * v`.

        Arguments
        - v: the vector to multiply

        Returns
        - the result
        """
        ...


    def quadraticFormProduct(self, v: "Vector3fc") -> float:
        """
        Compute `v^T * this * v`.

        Arguments
        - v: the vector to multiply

        Returns
        - the result
        """
        ...


    def mapXZY(self, dest: "Matrix3d") -> "Matrix3d":
        """
        Multiply `this` by the matrix
        ```
        1 0 0
        0 0 1
        0 1 0
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapXZnY(self, dest: "Matrix3d") -> "Matrix3d":
        """
        Multiply `this` by the matrix
        ```
        1 0  0
        0 0 -1
        0 1  0
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapXnYnZ(self, dest: "Matrix3d") -> "Matrix3d":
        """
        Multiply `this` by the matrix
        ```
        1  0  0
        0 -1  0
        0  0 -1
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapXnZY(self, dest: "Matrix3d") -> "Matrix3d":
        """
        Multiply `this` by the matrix
        ```
        1  0 0
        0  0 1
        0 -1 0
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapXnZnY(self, dest: "Matrix3d") -> "Matrix3d":
        """
        Multiply `this` by the matrix
        ```
        1  0  0
        0  0 -1
        0 -1  0
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapYXZ(self, dest: "Matrix3d") -> "Matrix3d":
        """
        Multiply `this` by the matrix
        ```
        0 1 0
        1 0 0
        0 0 1
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapYXnZ(self, dest: "Matrix3d") -> "Matrix3d":
        """
        Multiply `this` by the matrix
        ```
        0 1  0
        1 0  0
        0 0 -1
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapYZX(self, dest: "Matrix3d") -> "Matrix3d":
        """
        Multiply `this` by the matrix
        ```
        0 0 1
        1 0 0
        0 1 0
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapYZnX(self, dest: "Matrix3d") -> "Matrix3d":
        """
        Multiply `this` by the matrix
        ```
        0 0 -1
        1 0  0
        0 1  0
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapYnXZ(self, dest: "Matrix3d") -> "Matrix3d":
        """
        Multiply `this` by the matrix
        ```
        0 -1 0
        1  0 0
        0  0 1
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapYnXnZ(self, dest: "Matrix3d") -> "Matrix3d":
        """
        Multiply `this` by the matrix
        ```
        0 -1  0
        1  0  0
        0  0 -1
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapYnZX(self, dest: "Matrix3d") -> "Matrix3d":
        """
        Multiply `this` by the matrix
        ```
        0  0 1
        1  0 0
        0 -1 0
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapYnZnX(self, dest: "Matrix3d") -> "Matrix3d":
        """
        Multiply `this` by the matrix
        ```
        0  0 -1
        1  0  0
        0 -1  0
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapZXY(self, dest: "Matrix3d") -> "Matrix3d":
        """
        Multiply `this` by the matrix
        ```
        0 1 0
        0 0 1
        1 0 0
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapZXnY(self, dest: "Matrix3d") -> "Matrix3d":
        """
        Multiply `this` by the matrix
        ```
        0 1  0
        0 0 -1
        1 0  0
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapZYX(self, dest: "Matrix3d") -> "Matrix3d":
        """
        Multiply `this` by the matrix
        ```
        0 0 1
        0 1 0
        1 0 0
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapZYnX(self, dest: "Matrix3d") -> "Matrix3d":
        """
        Multiply `this` by the matrix
        ```
        0 0 -1
        0 1  0
        1 0  0
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapZnXY(self, dest: "Matrix3d") -> "Matrix3d":
        """
        Multiply `this` by the matrix
        ```
        0 -1 0
        0  0 1
        1  0 0
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapZnXnY(self, dest: "Matrix3d") -> "Matrix3d":
        """
        Multiply `this` by the matrix
        ```
        0 -1  0
        0  0 -1
        1  0  0
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapZnYX(self, dest: "Matrix3d") -> "Matrix3d":
        """
        Multiply `this` by the matrix
        ```
        0  0 1
        0 -1 0
        1  0 0
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapZnYnX(self, dest: "Matrix3d") -> "Matrix3d":
        """
        Multiply `this` by the matrix
        ```
        0  0 -1
        0 -1  0
        1  0  0
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapnXYnZ(self, dest: "Matrix3d") -> "Matrix3d":
        """
        Multiply `this` by the matrix
        ```
        -1 0  0
         0 1  0
         0 0 -1
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapnXZY(self, dest: "Matrix3d") -> "Matrix3d":
        """
        Multiply `this` by the matrix
        ```
        -1 0 0
         0 0 1
         0 1 0
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapnXZnY(self, dest: "Matrix3d") -> "Matrix3d":
        """
        Multiply `this` by the matrix
        ```
        -1 0  0
         0 0 -1
         0 1  0
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapnXnYZ(self, dest: "Matrix3d") -> "Matrix3d":
        """
        Multiply `this` by the matrix
        ```
        -1  0 0
         0 -1 0
         0  0 1
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapnXnYnZ(self, dest: "Matrix3d") -> "Matrix3d":
        """
        Multiply `this` by the matrix
        ```
        -1  0  0
         0 -1  0
         0  0 -1
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapnXnZY(self, dest: "Matrix3d") -> "Matrix3d":
        """
        Multiply `this` by the matrix
        ```
        -1  0 0
         0  0 1
         0 -1 0
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapnXnZnY(self, dest: "Matrix3d") -> "Matrix3d":
        """
        Multiply `this` by the matrix
        ```
        -1  0  0
         0  0 -1
         0 -1  0
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapnYXZ(self, dest: "Matrix3d") -> "Matrix3d":
        """
        Multiply `this` by the matrix
        ```
         0 1 0
        -1 0 0
         0 0 1
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapnYXnZ(self, dest: "Matrix3d") -> "Matrix3d":
        """
        Multiply `this` by the matrix
        ```
         0 1  0
        -1 0  0
         0 0 -1
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapnYZX(self, dest: "Matrix3d") -> "Matrix3d":
        """
        Multiply `this` by the matrix
        ```
         0 0 1
        -1 0 0
         0 1 0
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapnYZnX(self, dest: "Matrix3d") -> "Matrix3d":
        """
        Multiply `this` by the matrix
        ```
         0 0 -1
        -1 0  0
         0 1  0
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapnYnXZ(self, dest: "Matrix3d") -> "Matrix3d":
        """
        Multiply `this` by the matrix
        ```
         0 -1 0
        -1  0 0
         0  0 1
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapnYnXnZ(self, dest: "Matrix3d") -> "Matrix3d":
        """
        Multiply `this` by the matrix
        ```
         0 -1  0
        -1  0  0
         0  0 -1
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapnYnZX(self, dest: "Matrix3d") -> "Matrix3d":
        """
        Multiply `this` by the matrix
        ```
         0  0 1
        -1  0 0
         0 -1 0
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapnYnZnX(self, dest: "Matrix3d") -> "Matrix3d":
        """
        Multiply `this` by the matrix
        ```
         0  0 -1
        -1  0  0
         0 -1  0
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapnZXY(self, dest: "Matrix3d") -> "Matrix3d":
        """
        Multiply `this` by the matrix
        ```
         0 1 0
         0 0 1
        -1 0 0
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapnZXnY(self, dest: "Matrix3d") -> "Matrix3d":
        """
        Multiply `this` by the matrix
        ```
         0 1  0
         0 0 -1
        -1 0  0
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapnZYX(self, dest: "Matrix3d") -> "Matrix3d":
        """
        Multiply `this` by the matrix
        ```
         0 0 1
         0 1 0
        -1 0 0
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapnZYnX(self, dest: "Matrix3d") -> "Matrix3d":
        """
        Multiply `this` by the matrix
        ```
         0 0 -1
         0 1  0
        -1 0  0
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapnZnXY(self, dest: "Matrix3d") -> "Matrix3d":
        """
        Multiply `this` by the matrix
        ```
         0 -1 0
         0  0 1
        -1  0 0
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapnZnXnY(self, dest: "Matrix3d") -> "Matrix3d":
        """
        Multiply `this` by the matrix
        ```
         0 -1  0
         0  0 -1
        -1  0  0
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapnZnYX(self, dest: "Matrix3d") -> "Matrix3d":
        """
        Multiply `this` by the matrix
        ```
         0  0 1
         0 -1 0
        -1  0 0
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mapnZnYnX(self, dest: "Matrix3d") -> "Matrix3d":
        """
        Multiply `this` by the matrix
        ```
         0  0 -1
         0 -1  0
        -1  0  0
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def negateX(self, dest: "Matrix3d") -> "Matrix3d":
        """
        Multiply `this` by the matrix
        ```
        -1 0 0
         0 1 0
         0 0 1
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def negateY(self, dest: "Matrix3d") -> "Matrix3d":
        """
        Multiply `this` by the matrix
        ```
        1  0 0
        0 -1 0
        0  0 1
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def negateZ(self, dest: "Matrix3d") -> "Matrix3d":
        """
        Multiply `this` by the matrix
        ```
        1 0  0
        0 1  0
        0 0 -1
        ```
        and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...
