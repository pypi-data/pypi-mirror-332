"""
Python module generated from Java source file org.joml.Matrix2fc

Java source file obtained from artifact joml version 1.10.5

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util import *
from org.joml import *
from typing import Any, Callable, Iterable, Tuple


class Matrix2fc:
    """
    Interface to a read-only view of a 2x2 matrix of single-precision floats.

    Author(s)
    - Joseph Burton
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


    def mul(self, right: "Matrix2fc", dest: "Matrix2f") -> "Matrix2f":
        """
        Multiply this matrix by the supplied `right` matrix and store the result in `dest`.
        
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


    def mulLocal(self, left: "Matrix2fc", dest: "Matrix2f") -> "Matrix2f":
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


    def invert(self, dest: "Matrix2f") -> "Matrix2f":
        """
        Invert the `this` matrix and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def transpose(self, dest: "Matrix2f") -> "Matrix2f":
        """
        Transpose `this` matrix and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def get(self, dest: "Matrix2f") -> "Matrix2f":
        """
        Get the current values of `this` matrix and store them into
        `dest`.

        Arguments
        - dest: the destination matrix

        Returns
        - the passed in destination
        """
        ...


    def get(self, dest: "Matrix3x2f") -> "Matrix3x2f":
        """
        Get the current values of `this` matrix and store them as
        the rotational component of `dest`. All other values of `dest` will
        be set to 0.

        Arguments
        - dest: the destination matrix

        Returns
        - the passed in destination

        See
        - Matrix3x2f.set(Matrix2fc)
        """
        ...


    def get(self, dest: "Matrix3f") -> "Matrix3f":
        """
        Get the current values of `this` matrix and store them as
        the rotational component of `dest`. All other values of `dest` will
        be set to identity.

        Arguments
        - dest: the destination matrix

        Returns
        - the passed in destination

        See
        - Matrix3f.set(Matrix2fc)
        """
        ...


    def getRotation(self) -> float:
        """
        Get the angle of the rotation component of `this` matrix.
        
        This method assumes that there is a valid rotation to be returned, i.e. that
        `atan2(-m10, m00) == atan2(m01, m11)`.

        Returns
        - the angle
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


    def getTransposed(self, buffer: "FloatBuffer") -> "FloatBuffer":
        """
        Store the transpose of this matrix in column-major order into the supplied FloatBuffer at the current
        buffer FloatBuffer.position() position.
        
        This method will not increment the position of the given FloatBuffer.
        
        In order to specify the offset into the FloatBuffer at which
        the matrix is stored, use .getTransposed(int, FloatBuffer), taking
        the absolute position as parameter.

        Arguments
        - buffer: will receive the values of this matrix in column-major order at its current position

        Returns
        - the passed in buffer

        See
        - .getTransposed(int, FloatBuffer)
        """
        ...


    def getTransposed(self, index: int, buffer: "FloatBuffer") -> "FloatBuffer":
        """
        Store the transpose of this matrix in column-major order into the supplied FloatBuffer starting at the specified
        absolute buffer position/index.
        
        This method will not increment the position of the given FloatBuffer.

        Arguments
        - index: the absolute position into the FloatBuffer
        - buffer: will receive the values of this matrix in column-major order

        Returns
        - the passed in buffer
        """
        ...


    def getTransposed(self, buffer: "ByteBuffer") -> "ByteBuffer":
        """
        Store the transpose of this matrix in column-major order into the supplied ByteBuffer at the current
        buffer ByteBuffer.position() position.
        
        This method will not increment the position of the given ByteBuffer.
        
        In order to specify the offset into the ByteBuffer at which
        the matrix is stored, use .getTransposed(int, ByteBuffer), taking
        the absolute position as parameter.

        Arguments
        - buffer: will receive the values of this matrix in column-major order at its current position

        Returns
        - the passed in buffer

        See
        - .getTransposed(int, ByteBuffer)
        """
        ...


    def getTransposed(self, index: int, buffer: "ByteBuffer") -> "ByteBuffer":
        """
        Store the transpose of this matrix in column-major order into the supplied ByteBuffer starting at the specified
        absolute buffer position/index.
        
        This method will not increment the position of the given ByteBuffer.

        Arguments
        - index: the absolute position into the ByteBuffer
        - buffer: will receive the values of this matrix in column-major order

        Returns
        - the passed in buffer
        """
        ...


    def getToAddress(self, address: int) -> "Matrix2fc":
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
        Store this matrix into the supplied float array in column-major order at the given offset.

        Arguments
        - arr: the array to write the matrix values into
        - offset: the offset into the array

        Returns
        - the passed in array
        """
        ...


    def get(self, arr: list[float]) -> list[float]:
        """
        Store this matrix into the supplied float array in column-major order.
        
        In order to specify an explicit offset into the array, use the method .get(float[], int).

        Arguments
        - arr: the array to write the matrix values into

        Returns
        - the passed in array

        See
        - .get(float[], int)
        """
        ...


    def scale(self, xy: "Vector2fc", dest: "Matrix2f") -> "Matrix2f":
        """
        Apply scaling to `this` matrix by scaling the base axes by the given `xy.x` and
        `xy.y` factors, respectively and store the result in `dest`.
        
        If `M` is `this` matrix and `S` the scaling matrix,
        then the new matrix will be `M * S`. So when transforming a
        vector `v` with the new matrix by using `M * S * v`
        , the scaling will be applied first!

        Arguments
        - xy: the factors of the x and y component, respectively
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def scale(self, x: float, y: float, dest: "Matrix2f") -> "Matrix2f":
        """
        Apply scaling to this matrix by scaling the base axes by the given x and
        y factors and store the result in `dest`.
        
        If `M` is `this` matrix and `S` the scaling matrix,
        then the new matrix will be `M * S`. So when transforming a
        vector `v` with the new matrix by using `M * S * v`
        , the scaling will be applied first!

        Arguments
        - x: the factor of the x component
        - y: the factor of the y component
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def scale(self, xy: float, dest: "Matrix2f") -> "Matrix2f":
        """
        Apply scaling to this matrix by uniformly scaling all base axes by the given `xy` factor
        and store the result in `dest`.
        
        If `M` is `this` matrix and `S` the scaling matrix,
        then the new matrix will be `M * S`. So when transforming a
        vector `v` with the new matrix by using `M * S * v`
        , the scaling will be applied first!

        Arguments
        - xy: the factor for all components
        - dest: will hold the result

        Returns
        - dest

        See
        - .scale(float, float, Matrix2f)
        """
        ...


    def scaleLocal(self, x: float, y: float, dest: "Matrix2f") -> "Matrix2f":
        """
        Pre-multiply scaling to `this` matrix by scaling the base axes by the given x and
        y factors and store the result in `dest`.
        
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


    def transform(self, v: "Vector2f") -> "Vector2f":
        """
        Transform the given vector by this matrix.

        Arguments
        - v: the vector to transform

        Returns
        - v
        """
        ...


    def transform(self, v: "Vector2fc", dest: "Vector2f") -> "Vector2f":
        """
        Transform the given vector by this matrix and store the result in `dest`.

        Arguments
        - v: the vector to transform
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def transform(self, x: float, y: float, dest: "Vector2f") -> "Vector2f":
        """
        Transform the vector `(x, y)` by this matrix and store the result in `dest`.

        Arguments
        - x: the x coordinate of the vector to transform
        - y: the y coordinate of the vector to transform
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def transformTranspose(self, v: "Vector2f") -> "Vector2f":
        """
        Transform the given vector by the transpose of this matrix.

        Arguments
        - v: the vector to transform

        Returns
        - v
        """
        ...


    def transformTranspose(self, v: "Vector2fc", dest: "Vector2f") -> "Vector2f":
        """
        Transform the given vector by the transpose of this matrix and store the result in `dest`.

        Arguments
        - v: the vector to transform
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def transformTranspose(self, x: float, y: float, dest: "Vector2f") -> "Vector2f":
        """
        Transform the vector `(x, y)` by the transpose of this matrix and store the result in `dest`.

        Arguments
        - x: the x coordinate of the vector to transform
        - y: the y coordinate of the vector to transform
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def rotate(self, ang: float, dest: "Matrix2f") -> "Matrix2f":
        """
        Apply rotation to this matrix by rotating the given amount of radians
        and store the result in `dest`.
        
        The produced rotation will rotate a vector counter-clockwise around the origin.
        
        If `M` is `this` matrix and `R` the rotation matrix,
        then the new matrix will be `M * R`. So when transforming a
        vector `v` with the new matrix by using `M * R * v`
        , the rotation will be applied first!
        
        Reference: <a href="https://en.wikipedia.org/wiki/Rotation_matrix#In_two_dimensions">http://en.wikipedia.org</a>

        Arguments
        - ang: the angle in radians
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def rotateLocal(self, ang: float, dest: "Matrix2f") -> "Matrix2f":
        """
        Pre-multiply a rotation to this matrix by rotating the given amount of radians
        and store the result in `dest`.
        
        The produced rotation will rotate a vector counter-clockwise around the origin.
        
        If `M` is `this` matrix and `R` the rotation matrix,
        then the new matrix will be `R * M`. So when transforming a
        vector `v` with the new matrix by using `R * M * v`, the
        rotation will be applied last!
        
        Reference: <a href="https://en.wikipedia.org/wiki/Rotation_matrix#In_two_dimensions">http://en.wikipedia.org</a>

        Arguments
        - ang: the angle in radians
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def getRow(self, row: int, dest: "Vector2f") -> "Vector2f":
        """
        Get the row at the given `row` index, starting with `0`.

        Arguments
        - row: the row index in `[0..1]`
        - dest: will hold the row components

        Returns
        - the passed in destination

        Raises
        - IndexOutOfBoundsException: if `row` is not in `[0..1]`
        """
        ...


    def getColumn(self, column: int, dest: "Vector2f") -> "Vector2f":
        """
        Get the column at the given `column` index, starting with `0`.

        Arguments
        - column: the column index in `[0..1]`
        - dest: will hold the column components

        Returns
        - the passed in destination

        Raises
        - IndexOutOfBoundsException: if `column` is not in `[0..1]`
        """
        ...


    def get(self, column: int, row: int) -> float:
        """
        Get the matrix element value at the given column and row.

        Arguments
        - column: the colum index in `[0..1]`
        - row: the row index in `[0..1]`

        Returns
        - the element value
        """
        ...


    def normal(self, dest: "Matrix2f") -> "Matrix2f":
        """
        Compute a normal matrix from `this` matrix and store it into `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def getScale(self, dest: "Vector2f") -> "Vector2f":
        """
        Get the scaling factors of `this` matrix for the three base axes.

        Arguments
        - dest: will hold the scaling factors for `x` and `y`

        Returns
        - dest
        """
        ...


    def positiveX(self, dest: "Vector2f") -> "Vector2f":
        """
        Obtain the direction of `+X` before the transformation represented by `this` matrix is applied.
        
        This method is equivalent to the following code:
        ```
        Matrix2f inv = new Matrix2f(this).invert();
        inv.transform(dir.set(1, 0)).normalize();
        ```
        If `this` is already an orthogonal matrix, then consider using .normalizedPositiveX(Vector2f) instead.

        Arguments
        - dest: will hold the direction of `+X`

        Returns
        - dest
        """
        ...


    def normalizedPositiveX(self, dest: "Vector2f") -> "Vector2f":
        """
        Obtain the direction of `+X` before the transformation represented by `this` *orthogonal* matrix is applied.
        This method only produces correct results if `this` is an *orthogonal* matrix.
        
        This method is equivalent to the following code:
        ```
        Matrix2f inv = new Matrix2f(this).transpose();
        inv.transform(dir.set(1, 0));
        ```

        Arguments
        - dest: will hold the direction of `+X`

        Returns
        - dest
        """
        ...


    def positiveY(self, dest: "Vector2f") -> "Vector2f":
        """
        Obtain the direction of `+Y` before the transformation represented by `this` matrix is applied.
        
        This method is equivalent to the following code:
        ```
        Matrix2f inv = new Matrix2f(this).invert();
        inv.transform(dir.set(0, 1)).normalize();
        ```
        If `this` is already an orthogonal matrix, then consider using .normalizedPositiveY(Vector2f) instead.

        Arguments
        - dest: will hold the direction of `+Y`

        Returns
        - dest
        """
        ...


    def normalizedPositiveY(self, dest: "Vector2f") -> "Vector2f":
        """
        Obtain the direction of `+Y` before the transformation represented by `this` *orthogonal* matrix is applied.
        This method only produces correct results if `this` is an *orthogonal* matrix.
        
        This method is equivalent to the following code:
        ```
        Matrix2f inv = new Matrix2f(this).transpose();
        inv.transform(dir.set(0, 1));
        ```

        Arguments
        - dest: will hold the direction of `+Y`

        Returns
        - dest
        """
        ...


    def add(self, other: "Matrix2fc", dest: "Matrix2f") -> "Matrix2f":
        """
        Component-wise add `this` and `other` and store the result in `dest`.

        Arguments
        - other: the other addend
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def sub(self, subtrahend: "Matrix2fc", dest: "Matrix2f") -> "Matrix2f":
        """
        Component-wise subtract `subtrahend` from `this` and store the result in `dest`.

        Arguments
        - subtrahend: the subtrahend
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mulComponentWise(self, other: "Matrix2fc", dest: "Matrix2f") -> "Matrix2f":
        """
        Component-wise multiply `this` by `other` and store the result in `dest`.

        Arguments
        - other: the other matrix
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def lerp(self, other: "Matrix2fc", t: float, dest: "Matrix2f") -> "Matrix2f":
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


    def equals(self, m: "Matrix2fc", delta: float) -> bool:
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
        is, they are not Float.isNaN() NaN and not
        Float.isInfinite() infinity.

        Returns
        - `True` if all components are finite floating-point values;
                `False` otherwise
        """
        ...
