"""
Python module generated from Java source file org.joml.Matrix3f

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


class Matrix3f(Externalizable, Cloneable, Matrix3fc):
    """
    Contains the definition of a 3x3 matrix of floats, and associated functions to transform
    it. The matrix is column-major to match OpenGL's interpretation, and it looks like this:
    
         m00  m10  m20
         m01  m11  m21
         m02  m12  m22

    Author(s)
    - Kai Burjack
    """

    def __init__(self):
        """
        Create a new Matrix3f and set it to .identity() identity.
        """
        ...


    def __init__(self, mat: "Matrix2fc"):
        """
        Create a new Matrix3f by setting its uppper left 2x2 submatrix to the values of the given Matrix2fc
        and the rest to identity.

        Arguments
        - mat: the Matrix2fc
        """
        ...


    def __init__(self, mat: "Matrix3fc"):
        """
        Create a new Matrix3f and make it a copy of the given matrix.

        Arguments
        - mat: the Matrix3fc to copy the values from
        """
        ...


    def __init__(self, mat: "Matrix4fc"):
        """
        Create a new Matrix3f and make it a copy of the upper left 3x3 of the given Matrix4fc.

        Arguments
        - mat: the Matrix4fc to copy the values from
        """
        ...


    def __init__(self, m00: float, m01: float, m02: float, m10: float, m11: float, m12: float, m20: float, m21: float, m22: float):
        """
        Create a new 3x3 matrix using the supplied float values. The order of the parameter is column-major, 
        so the first three parameters specify the three elements of the first column.

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
        """
        ...


    def __init__(self, buffer: "FloatBuffer"):
        """
        Create a new Matrix3f by reading its 9 float components from the given FloatBuffer
        at the buffer's current position.
        
        That FloatBuffer is expected to hold the values in column-major order.
        
        The buffer's position will not be changed by this method.

        Arguments
        - buffer: the FloatBuffer to read the matrix values from
        """
        ...


    def __init__(self, col0: "Vector3fc", col1: "Vector3fc", col2: "Vector3fc"):
        """
        Create a new Matrix3f and initialize its three columns using the supplied vectors.

        Arguments
        - col0: the first column
        - col1: the second column
        - col2: the third column
        """
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


    def m00(self, m00: float) -> "Matrix3f":
        """
        Set the value of the matrix element at column 0 and row 0.

        Arguments
        - m00: the new value

        Returns
        - this
        """
        ...


    def m01(self, m01: float) -> "Matrix3f":
        """
        Set the value of the matrix element at column 0 and row 1.

        Arguments
        - m01: the new value

        Returns
        - this
        """
        ...


    def m02(self, m02: float) -> "Matrix3f":
        """
        Set the value of the matrix element at column 0 and row 2.

        Arguments
        - m02: the new value

        Returns
        - this
        """
        ...


    def m10(self, m10: float) -> "Matrix3f":
        """
        Set the value of the matrix element at column 1 and row 0.

        Arguments
        - m10: the new value

        Returns
        - this
        """
        ...


    def m11(self, m11: float) -> "Matrix3f":
        """
        Set the value of the matrix element at column 1 and row 1.

        Arguments
        - m11: the new value

        Returns
        - this
        """
        ...


    def m12(self, m12: float) -> "Matrix3f":
        """
        Set the value of the matrix element at column 1 and row 2.

        Arguments
        - m12: the new value

        Returns
        - this
        """
        ...


    def m20(self, m20: float) -> "Matrix3f":
        """
        Set the value of the matrix element at column 2 and row 0.

        Arguments
        - m20: the new value

        Returns
        - this
        """
        ...


    def m21(self, m21: float) -> "Matrix3f":
        """
        Set the value of the matrix element at column 2 and row 1.

        Arguments
        - m21: the new value

        Returns
        - this
        """
        ...


    def m22(self, m22: float) -> "Matrix3f":
        """
        Set the value of the matrix element at column 2 and row 2.

        Arguments
        - m22: the new value

        Returns
        - this
        """
        ...


    def set(self, m: "Matrix3fc") -> "Matrix3f":
        """
        Set the elements of this matrix to the ones in `m`.

        Arguments
        - m: the matrix to copy the elements from

        Returns
        - this
        """
        ...


    def setTransposed(self, m: "Matrix3fc") -> "Matrix3f":
        """
        Store the values of the transpose of the given matrix `m` into `this` matrix.

        Arguments
        - m: the matrix to copy the transposed values from

        Returns
        - this
        """
        ...


    def set(self, m: "Matrix4x3fc") -> "Matrix3f":
        """
        Set the elements of this matrix to the left 3x3 submatrix of `m`.

        Arguments
        - m: the matrix to copy the elements from

        Returns
        - this
        """
        ...


    def set(self, mat: "Matrix4fc") -> "Matrix3f":
        """
        Set the elements of this matrix to the upper left 3x3 of the given Matrix4fc.

        Arguments
        - mat: the Matrix4fc to copy the values from

        Returns
        - this
        """
        ...


    def set(self, mat: "Matrix2fc") -> "Matrix3f":
        """
        Set the upper left 2x2 submatrix of this Matrix3f to the given Matrix2fc
        and the rest to identity.

        Arguments
        - mat: the Matrix2fc

        Returns
        - this

        See
        - .Matrix3f(Matrix2fc)
        """
        ...


    def set(self, axisAngle: "AxisAngle4f") -> "Matrix3f":
        """
        Set this matrix to be equivalent to the rotation specified by the given AxisAngle4f.

        Arguments
        - axisAngle: the AxisAngle4f

        Returns
        - this
        """
        ...


    def set(self, axisAngle: "AxisAngle4d") -> "Matrix3f":
        """
        Set this matrix to be equivalent to the rotation specified by the given AxisAngle4d.

        Arguments
        - axisAngle: the AxisAngle4d

        Returns
        - this
        """
        ...


    def set(self, q: "Quaternionfc") -> "Matrix3f":
        """
        Set this matrix to be equivalent to the rotation - and possibly scaling - specified by the given Quaternionfc.
        
        This method is equivalent to calling: `rotation(q)`
        
        Reference: <a href="http://www.euclideanspace.com/maths/geometry/rotations/conversions/quaternionToMatrix/">http://www.euclideanspace.com/</a>

        Arguments
        - q: the Quaternionfc

        Returns
        - this

        See
        - .rotation(Quaternionfc)
        """
        ...


    def set(self, q: "Quaterniondc") -> "Matrix3f":
        """
        Set this matrix to a rotation - and possibly scaling - equivalent to the given quaternion.
        
        Reference: <a href="http://www.euclideanspace.com/maths/geometry/rotations/conversions/quaternionToMatrix/">http://www.euclideanspace.com/</a>

        Arguments
        - q: the quaternion

        Returns
        - this
        """
        ...


    def mul(self, right: "Matrix3fc") -> "Matrix3f":
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


    def mul(self, right: "Matrix3fc", dest: "Matrix3f") -> "Matrix3f":
        ...


    def mulLocal(self, left: "Matrix3fc") -> "Matrix3f":
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


    def mulLocal(self, left: "Matrix3fc", dest: "Matrix3f") -> "Matrix3f":
        ...


    def set(self, m00: float, m01: float, m02: float, m10: float, m11: float, m12: float, m20: float, m21: float, m22: float) -> "Matrix3f":
        """
        Set the values within this matrix to the supplied float values. The result looks like this:
        
        m00, m10, m20
        m01, m11, m21
        m02, m12, m22

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

        Returns
        - this
        """
        ...


    def set(self, m: list[float]) -> "Matrix3f":
        """
        Set the values in this matrix based on the supplied float array. The result looks like this:
        
        0, 3, 6
        1, 4, 7
        2, 5, 8
        
        This method only uses the first 9 values, all others are ignored.

        Arguments
        - m: the array to read the matrix values from

        Returns
        - this
        """
        ...


    def set(self, col0: "Vector3fc", col1: "Vector3fc", col2: "Vector3fc") -> "Matrix3f":
        """
        Set the three columns of this matrix to the supplied vectors, respectively.

        Arguments
        - col0: the first column
        - col1: the second column
        - col2: the third column

        Returns
        - this
        """
        ...


    def determinant(self) -> float:
        ...


    def invert(self) -> "Matrix3f":
        """
        Invert this matrix.

        Returns
        - this
        """
        ...


    def invert(self, dest: "Matrix3f") -> "Matrix3f":
        ...


    def transpose(self) -> "Matrix3f":
        """
        Transpose this matrix.

        Returns
        - this
        """
        ...


    def transpose(self, dest: "Matrix3f") -> "Matrix3f":
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


    def get(self, dest: "Matrix3f") -> "Matrix3f":
        """
        Get the current values of `this` matrix and store them into
        `dest`.
        
        This is the reverse method of .set(Matrix3fc) and allows to obtain
        intermediate calculation results when chaining multiple transformations.

        Arguments
        - dest: the destination matrix

        Returns
        - the passed in destination

        See
        - .set(Matrix3fc)
        """
        ...


    def get(self, dest: "Matrix4f") -> "Matrix4f":
        ...


    def getRotation(self, dest: "AxisAngle4f") -> "AxisAngle4f":
        ...


    def getUnnormalizedRotation(self, dest: "Quaternionf") -> "Quaternionf":
        ...


    def getNormalizedRotation(self, dest: "Quaternionf") -> "Quaternionf":
        ...


    def getUnnormalizedRotation(self, dest: "Quaterniond") -> "Quaterniond":
        ...


    def getNormalizedRotation(self, dest: "Quaterniond") -> "Quaterniond":
        ...


    def get(self, buffer: "FloatBuffer") -> "FloatBuffer":
        ...


    def get(self, index: int, buffer: "FloatBuffer") -> "FloatBuffer":
        ...


    def get(self, buffer: "ByteBuffer") -> "ByteBuffer":
        ...


    def get(self, index: int, buffer: "ByteBuffer") -> "ByteBuffer":
        ...


    def get3x4(self, buffer: "FloatBuffer") -> "FloatBuffer":
        ...


    def get3x4(self, index: int, buffer: "FloatBuffer") -> "FloatBuffer":
        ...


    def get3x4(self, buffer: "ByteBuffer") -> "ByteBuffer":
        ...


    def get3x4(self, index: int, buffer: "ByteBuffer") -> "ByteBuffer":
        ...


    def getTransposed(self, buffer: "FloatBuffer") -> "FloatBuffer":
        ...


    def getTransposed(self, index: int, buffer: "FloatBuffer") -> "FloatBuffer":
        ...


    def getTransposed(self, buffer: "ByteBuffer") -> "ByteBuffer":
        ...


    def getTransposed(self, index: int, buffer: "ByteBuffer") -> "ByteBuffer":
        ...


    def getToAddress(self, address: int) -> "Matrix3fc":
        ...


    def get(self, arr: list[float], offset: int) -> list[float]:
        ...


    def get(self, arr: list[float]) -> list[float]:
        ...


    def set(self, buffer: "FloatBuffer") -> "Matrix3f":
        """
        Set the values of this matrix by reading 9 float values from the given FloatBuffer in column-major order,
        starting at its current position.
        
        The FloatBuffer is expected to contain the values in column-major order.
        
        The position of the FloatBuffer will not be changed by this method.

        Arguments
        - buffer: the FloatBuffer to read the matrix values from in column-major order

        Returns
        - this
        """
        ...


    def set(self, buffer: "ByteBuffer") -> "Matrix3f":
        """
        Set the values of this matrix by reading 9 float values from the given ByteBuffer in column-major order,
        starting at its current position.
        
        The ByteBuffer is expected to contain the values in column-major order.
        
        The position of the ByteBuffer will not be changed by this method.

        Arguments
        - buffer: the ByteBuffer to read the matrix values from in column-major order

        Returns
        - this
        """
        ...


    def set(self, index: int, buffer: "FloatBuffer") -> "Matrix3f":
        """
        Set the values of this matrix by reading 9 float values from the given FloatBuffer in column-major order,
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


    def set(self, index: int, buffer: "ByteBuffer") -> "Matrix3f":
        """
        Set the values of this matrix by reading 9 float values from the given ByteBuffer in column-major order,
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


    def setFromAddress(self, address: int) -> "Matrix3f":
        """
        Set the values of this matrix by reading 9 float values from off-heap memory in column-major order,
        starting at the given address.
        
        This method will throw an UnsupportedOperationException when JOML is used with `-Djoml.nounsafe`.
        
        *This method is unsafe as it can result in a crash of the JVM process when the specified address range does not belong to this process.*

        Arguments
        - address: the off-heap memory address to read the matrix values from in column-major order

        Returns
        - this
        """
        ...


    def zero(self) -> "Matrix3f":
        """
        Set all values within this matrix to zero.

        Returns
        - this
        """
        ...


    def identity(self) -> "Matrix3f":
        """
        Set this matrix to the identity.

        Returns
        - this
        """
        ...


    def scale(self, xyz: "Vector3fc", dest: "Matrix3f") -> "Matrix3f":
        ...


    def scale(self, xyz: "Vector3fc") -> "Matrix3f":
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


    def scale(self, x: float, y: float, z: float, dest: "Matrix3f") -> "Matrix3f":
        ...


    def scale(self, x: float, y: float, z: float) -> "Matrix3f":
        """
        Apply scaling to this matrix by scaling the base axes by the given x,
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


    def scale(self, xyz: float, dest: "Matrix3f") -> "Matrix3f":
        ...


    def scale(self, xyz: float) -> "Matrix3f":
        """
        Apply scaling to this matrix by uniformly scaling all base axes by the given `xyz` factor.
        
        If `M` is `this` matrix and `S` the scaling matrix,
        then the new matrix will be `M * S`. So when transforming a
        vector `v` with the new matrix by using `M * S * v`
        , the scaling will be applied first!

        Arguments
        - xyz: the factor for all components

        Returns
        - this

        See
        - .scale(float, float, float)
        """
        ...


    def scaleLocal(self, x: float, y: float, z: float, dest: "Matrix3f") -> "Matrix3f":
        ...


    def scaleLocal(self, x: float, y: float, z: float) -> "Matrix3f":
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


    def scaling(self, factor: float) -> "Matrix3f":
        """
        Set this matrix to be a simple scale matrix, which scales all axes uniformly by the given factor.
        
        The resulting matrix can be multiplied against another transformation
        matrix to obtain an additional scaling.
        
        In order to post-multiply a scaling transformation directly to a
        matrix, use .scale(float) scale() instead.

        Arguments
        - factor: the scale factor in x, y and z

        Returns
        - this

        See
        - .scale(float)
        """
        ...


    def scaling(self, x: float, y: float, z: float) -> "Matrix3f":
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


    def scaling(self, xyz: "Vector3fc") -> "Matrix3f":
        """
        Set this matrix to be a simple scale matrix which scales the base axes by `xyz.x`, `xyz.y` and `xyz.z` respectively.
        
        The resulting matrix can be multiplied against another transformation
        matrix to obtain an additional scaling.
        
        In order to post-multiply a scaling transformation directly to a
        matrix use .scale(Vector3fc) scale() instead.

        Arguments
        - xyz: the scale in x, y and z respectively

        Returns
        - this

        See
        - .scale(Vector3fc)
        """
        ...


    def rotation(self, angle: float, axis: "Vector3fc") -> "Matrix3f":
        """
        Set this matrix to a rotation matrix which rotates the given radians about a given axis.
        
        The axis described by the `axis` vector needs to be a unit vector.
        
        When used with a right-handed coordinate system, the produced rotation will rotate a vector 
        counter-clockwise around the rotation axis, when viewing along the negative axis direction towards the origin.
        When used with a left-handed coordinate system, the rotation is clockwise.
        
        The resulting matrix can be multiplied against another transformation
        matrix to obtain an additional rotation.
        
        In order to post-multiply a rotation transformation directly to a
        matrix, use .rotate(float, Vector3fc) rotate() instead.

        Arguments
        - angle: the angle in radians
        - axis: the axis to rotate about (needs to be Vector3f.normalize() normalized)

        Returns
        - this

        See
        - .rotate(float, Vector3fc)
        """
        ...


    def rotation(self, axisAngle: "AxisAngle4f") -> "Matrix3f":
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
        - axisAngle: the AxisAngle4f (needs to be AxisAngle4f.normalize() normalized)

        Returns
        - this

        See
        - .rotate(AxisAngle4f)
        """
        ...


    def rotation(self, angle: float, x: float, y: float, z: float) -> "Matrix3f":
        """
        Set this matrix to a rotation matrix which rotates the given radians about a given axis.
        
        The axis described by the three components needs to be a unit vector.
        
        When used with a right-handed coordinate system, the produced rotation will rotate a vector 
        counter-clockwise around the rotation axis, when viewing along the negative axis direction towards the origin.
        When used with a left-handed coordinate system, the rotation is clockwise.
        
        The resulting matrix can be multiplied against another transformation
        matrix to obtain an additional rotation.
        
        In order to apply the rotation transformation to an existing transformation,
        use .rotate(float, float, float, float) rotate() instead.
        
        Reference: <a href="http://en.wikipedia.org/wiki/Rotation_matrix#Rotation_matrix_from_axis_and_angle">http://en.wikipedia.org</a>

        Arguments
        - angle: the angle in radians
        - x: the x-component of the rotation axis
        - y: the y-component of the rotation axis
        - z: the z-component of the rotation axis

        Returns
        - this

        See
        - .rotate(float, float, float, float)
        """
        ...


    def rotationX(self, ang: float) -> "Matrix3f":
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


    def rotationY(self, ang: float) -> "Matrix3f":
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


    def rotationZ(self, ang: float) -> "Matrix3f":
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


    def rotationXYZ(self, angleX: float, angleY: float, angleZ: float) -> "Matrix3f":
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


    def rotationZYX(self, angleZ: float, angleY: float, angleX: float) -> "Matrix3f":
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


    def rotationYXZ(self, angleY: float, angleX: float, angleZ: float) -> "Matrix3f":
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


    def rotation(self, quat: "Quaternionfc") -> "Matrix3f":
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


    def transform(self, v: "Vector3f") -> "Vector3f":
        ...


    def transform(self, v: "Vector3fc", dest: "Vector3f") -> "Vector3f":
        ...


    def transform(self, x: float, y: float, z: float, dest: "Vector3f") -> "Vector3f":
        ...


    def transformTranspose(self, v: "Vector3f") -> "Vector3f":
        ...


    def transformTranspose(self, v: "Vector3fc", dest: "Vector3f") -> "Vector3f":
        ...


    def transformTranspose(self, x: float, y: float, z: float, dest: "Vector3f") -> "Vector3f":
        ...


    def writeExternal(self, out: "ObjectOutput") -> None:
        ...


    def readExternal(self, in: "ObjectInput") -> None:
        ...


    def rotateX(self, ang: float, dest: "Matrix3f") -> "Matrix3f":
        ...


    def rotateX(self, ang: float) -> "Matrix3f":
        """
        Apply rotation about the X axis to this matrix by rotating the given amount of radians.
        
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

        Returns
        - this
        """
        ...


    def rotateY(self, ang: float, dest: "Matrix3f") -> "Matrix3f":
        ...


    def rotateY(self, ang: float) -> "Matrix3f":
        """
        Apply rotation about the Y axis to this matrix by rotating the given amount of radians.
        
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

        Returns
        - this
        """
        ...


    def rotateZ(self, ang: float, dest: "Matrix3f") -> "Matrix3f":
        ...


    def rotateZ(self, ang: float) -> "Matrix3f":
        """
        Apply rotation about the Z axis to this matrix by rotating the given amount of radians.
        
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

        Returns
        - this
        """
        ...


    def rotateXYZ(self, angles: "Vector3f") -> "Matrix3f":
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


    def rotateXYZ(self, angleX: float, angleY: float, angleZ: float) -> "Matrix3f":
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


    def rotateXYZ(self, angleX: float, angleY: float, angleZ: float, dest: "Matrix3f") -> "Matrix3f":
        ...


    def rotateZYX(self, angles: "Vector3f") -> "Matrix3f":
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


    def rotateZYX(self, angleZ: float, angleY: float, angleX: float) -> "Matrix3f":
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


    def rotateZYX(self, angleZ: float, angleY: float, angleX: float, dest: "Matrix3f") -> "Matrix3f":
        ...


    def rotateYXZ(self, angles: "Vector3f") -> "Matrix3f":
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


    def rotateYXZ(self, angleY: float, angleX: float, angleZ: float) -> "Matrix3f":
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


    def rotateYXZ(self, angleY: float, angleX: float, angleZ: float, dest: "Matrix3f") -> "Matrix3f":
        ...


    def rotate(self, ang: float, x: float, y: float, z: float) -> "Matrix3f":
        """
        Apply rotation to this matrix by rotating the given amount of radians
        about the given axis specified as x, y and z components.
        
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

        Returns
        - this
        """
        ...


    def rotate(self, ang: float, x: float, y: float, z: float, dest: "Matrix3f") -> "Matrix3f":
        ...


    def rotateLocal(self, ang: float, x: float, y: float, z: float, dest: "Matrix3f") -> "Matrix3f":
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
        transformation, use .rotation(float, float, float, float) rotation().
        
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
        - .rotation(float, float, float, float)
        """
        ...


    def rotateLocal(self, ang: float, x: float, y: float, z: float) -> "Matrix3f":
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
        transformation, use .rotation(float, float, float, float) rotation().
        
        Reference: <a href="http://en.wikipedia.org/wiki/Rotation_matrix#Rotation_matrix_from_axis_and_angle">http://en.wikipedia.org</a>

        Arguments
        - ang: the angle in radians
        - x: the x component of the axis
        - y: the y component of the axis
        - z: the z component of the axis

        Returns
        - this

        See
        - .rotation(float, float, float, float)
        """
        ...


    def rotateLocalX(self, ang: float, dest: "Matrix3f") -> "Matrix3f":
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
        transformation, use .rotationX(float) rotationX().
        
        Reference: <a href="http://en.wikipedia.org/wiki/Rotation_matrix#Rotation_matrix_from_axis_and_angle">http://en.wikipedia.org</a>

        Arguments
        - ang: the angle in radians to rotate about the X axis
        - dest: will hold the result

        Returns
        - dest

        See
        - .rotationX(float)
        """
        ...


    def rotateLocalX(self, ang: float) -> "Matrix3f":
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
        transformation, use .rotationX(float) rotationX().
        
        Reference: <a href="http://en.wikipedia.org/wiki/Rotation_matrix#Rotation_matrix_from_axis_and_angle">http://en.wikipedia.org</a>

        Arguments
        - ang: the angle in radians to rotate about the X axis

        Returns
        - this

        See
        - .rotationX(float)
        """
        ...


    def rotateLocalY(self, ang: float, dest: "Matrix3f") -> "Matrix3f":
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
        transformation, use .rotationY(float) rotationY().
        
        Reference: <a href="http://en.wikipedia.org/wiki/Rotation_matrix#Rotation_matrix_from_axis_and_angle">http://en.wikipedia.org</a>

        Arguments
        - ang: the angle in radians to rotate about the Y axis
        - dest: will hold the result

        Returns
        - dest

        See
        - .rotationY(float)
        """
        ...


    def rotateLocalY(self, ang: float) -> "Matrix3f":
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
        transformation, use .rotationY(float) rotationY().
        
        Reference: <a href="http://en.wikipedia.org/wiki/Rotation_matrix#Rotation_matrix_from_axis_and_angle">http://en.wikipedia.org</a>

        Arguments
        - ang: the angle in radians to rotate about the Y axis

        Returns
        - this

        See
        - .rotationY(float)
        """
        ...


    def rotateLocalZ(self, ang: float, dest: "Matrix3f") -> "Matrix3f":
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
        transformation, use .rotationZ(float) rotationZ().
        
        Reference: <a href="http://en.wikipedia.org/wiki/Rotation_matrix#Rotation_matrix_from_axis_and_angle">http://en.wikipedia.org</a>

        Arguments
        - ang: the angle in radians to rotate about the Z axis
        - dest: will hold the result

        Returns
        - dest

        See
        - .rotationZ(float)
        """
        ...


    def rotateLocalZ(self, ang: float) -> "Matrix3f":
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
        transformation, use .rotationZ(float) rotationY().
        
        Reference: <a href="http://en.wikipedia.org/wiki/Rotation_matrix#Rotation_matrix_from_axis_and_angle">http://en.wikipedia.org</a>

        Arguments
        - ang: the angle in radians to rotate about the Z axis

        Returns
        - this

        See
        - .rotationY(float)
        """
        ...


    def rotate(self, quat: "Quaternionfc") -> "Matrix3f":
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


    def rotate(self, quat: "Quaternionfc", dest: "Matrix3f") -> "Matrix3f":
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


    def rotateLocal(self, quat: "Quaternionfc", dest: "Matrix3f") -> "Matrix3f":
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


    def rotateLocal(self, quat: "Quaternionfc") -> "Matrix3f":
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


    def rotate(self, axisAngle: "AxisAngle4f") -> "Matrix3f":
        """
        Apply a rotation transformation, rotating about the given AxisAngle4f, to this matrix.
        
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


    def rotate(self, axisAngle: "AxisAngle4f", dest: "Matrix3f") -> "Matrix3f":
        """
        Apply a rotation transformation, rotating about the given AxisAngle4f and store the result in `dest`.
        
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


    def rotate(self, angle: float, axis: "Vector3fc") -> "Matrix3f":
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
        use .rotation(float, Vector3fc).
        
        Reference: <a href="http://en.wikipedia.org/wiki/Rotation_matrix#Axis_and_angle">http://en.wikipedia.org</a>

        Arguments
        - angle: the angle in radians
        - axis: the rotation axis (needs to be Vector3f.normalize() normalized)

        Returns
        - this

        See
        - .rotation(float, Vector3fc)
        """
        ...


    def rotate(self, angle: float, axis: "Vector3fc", dest: "Matrix3f") -> "Matrix3f":
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
        use .rotation(float, Vector3fc).
        
        Reference: <a href="http://en.wikipedia.org/wiki/Rotation_matrix#Axis_and_angle">http://en.wikipedia.org</a>

        Arguments
        - angle: the angle in radians
        - axis: the rotation axis (needs to be Vector3f.normalize() normalized)
        - dest: will hold the result

        Returns
        - dest

        See
        - .rotation(float, Vector3fc)
        """
        ...


    def lookAlong(self, dir: "Vector3fc", up: "Vector3fc") -> "Matrix3f":
        """
        Apply a rotation transformation to this matrix to make `-z` point along `dir`. 
        
        If `M` is `this` matrix and `L` the lookalong rotation matrix,
        then the new matrix will be `M * L`. So when transforming a
        vector `v` with the new matrix by using `M * L * v`, the
        lookalong rotation transformation will be applied first!
        
        In order to set the matrix to a lookalong transformation without post-multiplying it,
        use .setLookAlong(Vector3fc, Vector3fc) setLookAlong().

        Arguments
        - dir: the direction in space to look along
        - up: the direction of 'up'

        Returns
        - this

        See
        - .setLookAlong(Vector3fc, Vector3fc)
        """
        ...


    def lookAlong(self, dir: "Vector3fc", up: "Vector3fc", dest: "Matrix3f") -> "Matrix3f":
        """
        Apply a rotation transformation to this matrix to make `-z` point along `dir`
        and store the result in `dest`. 
        
        If `M` is `this` matrix and `L` the lookalong rotation matrix,
        then the new matrix will be `M * L`. So when transforming a
        vector `v` with the new matrix by using `M * L * v`, the
        lookalong rotation transformation will be applied first!
        
        In order to set the matrix to a lookalong transformation without post-multiplying it,
        use .setLookAlong(Vector3fc, Vector3fc) setLookAlong().

        Arguments
        - dir: the direction in space to look along
        - up: the direction of 'up'
        - dest: will hold the result

        Returns
        - dest

        See
        - .setLookAlong(Vector3fc, Vector3fc)
        """
        ...


    def lookAlong(self, dirX: float, dirY: float, dirZ: float, upX: float, upY: float, upZ: float, dest: "Matrix3f") -> "Matrix3f":
        """
        Apply a rotation transformation to this matrix to make `-z` point along `dir`
        and store the result in `dest`. 
        
        If `M` is `this` matrix and `L` the lookalong rotation matrix,
        then the new matrix will be `M * L`. So when transforming a
        vector `v` with the new matrix by using `M * L * v`, the
        lookalong rotation transformation will be applied first!
        
        In order to set the matrix to a lookalong transformation without post-multiplying it,
        use .setLookAlong(float, float, float, float, float, float) setLookAlong()

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
        - .setLookAlong(float, float, float, float, float, float)
        """
        ...


    def lookAlong(self, dirX: float, dirY: float, dirZ: float, upX: float, upY: float, upZ: float) -> "Matrix3f":
        """
        Apply a rotation transformation to this matrix to make `-z` point along `dir`. 
        
        If `M` is `this` matrix and `L` the lookalong rotation matrix,
        then the new matrix will be `M * L`. So when transforming a
        vector `v` with the new matrix by using `M * L * v`, the
        lookalong rotation transformation will be applied first!
        
        In order to set the matrix to a lookalong transformation without post-multiplying it,
        use .setLookAlong(float, float, float, float, float, float) setLookAlong()

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
        - .setLookAlong(float, float, float, float, float, float)
        """
        ...


    def setLookAlong(self, dir: "Vector3fc", up: "Vector3fc") -> "Matrix3f":
        """
        Set this matrix to a rotation transformation to make `-z`
        point along `dir`.
        
        In order to apply the lookalong transformation to any previous existing transformation,
        use .lookAlong(Vector3fc, Vector3fc).

        Arguments
        - dir: the direction in space to look along
        - up: the direction of 'up'

        Returns
        - this

        See
        - .lookAlong(Vector3fc, Vector3fc)
        """
        ...


    def setLookAlong(self, dirX: float, dirY: float, dirZ: float, upX: float, upY: float, upZ: float) -> "Matrix3f":
        """
        Set this matrix to a rotation transformation to make `-z`
        point along `dir`.
        
        In order to apply the lookalong transformation to any previous existing transformation,
        use .lookAlong(float, float, float, float, float, float) lookAlong()

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
        - .lookAlong(float, float, float, float, float, float)
        """
        ...


    def getRow(self, row: int, dest: "Vector3f") -> "Vector3f":
        ...


    def setRow(self, row: int, src: "Vector3fc") -> "Matrix3f":
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


    def setRow(self, row: int, x: float, y: float, z: float) -> "Matrix3f":
        """
        Set the row at the given `row` index, starting with `0`.

        Arguments
        - row: the row index in `[0..2]`
        - x: the first element in the row
        - y: the second element in the row
        - z: the third element in the row

        Returns
        - this

        Raises
        - IndexOutOfBoundsException: if `row` is not in `[0..2]`
        """
        ...


    def getColumn(self, column: int, dest: "Vector3f") -> "Vector3f":
        ...


    def setColumn(self, column: int, src: "Vector3fc") -> "Matrix3f":
        """
        Set the column at the given `column` index, starting with `0`.

        Arguments
        - column: the column index in `[0..2]`
        - src: the column components to set

        Returns
        - this

        Raises
        - IndexOutOfBoundsException: if `column` is not in `[0..2]`
        """
        ...


    def setColumn(self, column: int, x: float, y: float, z: float) -> "Matrix3f":
        """
        Set the column at the given `column` index, starting with `0`.

        Arguments
        - column: the column index in `[0..2]`
        - x: the first element in the column
        - y: the second element in the column
        - z: the third element in the column

        Returns
        - this

        Raises
        - IndexOutOfBoundsException: if `column` is not in `[0..2]`
        """
        ...


    def get(self, column: int, row: int) -> float:
        ...


    def set(self, column: int, row: int, value: float) -> "Matrix3f":
        """
        Set the matrix element at the given column and row to the specified value.

        Arguments
        - column: the colum index in `[0..2]`
        - row: the row index in `[0..2]`
        - value: the value

        Returns
        - this
        """
        ...


    def getRowColumn(self, row: int, column: int) -> float:
        ...


    def setRowColumn(self, row: int, column: int, value: float) -> "Matrix3f":
        """
        Set the matrix element at the given row and column to the specified value.

        Arguments
        - row: the row index in `[0..2]`
        - column: the colum index in `[0..2]`
        - value: the value

        Returns
        - this
        """
        ...


    def normal(self) -> "Matrix3f":
        """
        Set `this` matrix to its own normal matrix.
        
        The normal matrix of `m` is the transpose of the inverse of `m`.
        
        Please note that, if `this` is an orthogonal matrix or a matrix whose columns are orthogonal vectors, 
        then this method *need not* be invoked, since in that case `this` itself is its normal matrix.
        In this case, use .set(Matrix3fc) to set a given Matrix3f to this matrix.

        Returns
        - this

        See
        - .set(Matrix3fc)
        """
        ...


    def normal(self, dest: "Matrix3f") -> "Matrix3f":
        """
        Compute a normal matrix from `this` matrix and store it into `dest`.
        
        The normal matrix of `m` is the transpose of the inverse of `m`.
        
        Please note that, if `this` is an orthogonal matrix or a matrix whose columns are orthogonal vectors, 
        then this method *need not* be invoked, since in that case `this` itself is its normal matrix.
        In this case, use .set(Matrix3fc) to set a given Matrix3f to this matrix.

        Arguments
        - dest: will hold the result

        Returns
        - dest

        See
        - .set(Matrix3fc)
        """
        ...


    def cofactor(self) -> "Matrix3f":
        """
        Compute the cofactor matrix of `this`.
        
        The cofactor matrix can be used instead of .normal() to transform normals
        when the orientation of the normals with respect to the surface should be preserved.

        Returns
        - this
        """
        ...


    def cofactor(self, dest: "Matrix3f") -> "Matrix3f":
        """
        Compute the cofactor matrix of `this` and store it into `dest`.
        
        The cofactor matrix can be used instead of .normal(Matrix3f) to transform normals
        when the orientation of the normals with respect to the surface should be preserved.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def getScale(self, dest: "Vector3f") -> "Vector3f":
        ...


    def positiveZ(self, dir: "Vector3f") -> "Vector3f":
        ...


    def normalizedPositiveZ(self, dir: "Vector3f") -> "Vector3f":
        ...


    def positiveX(self, dir: "Vector3f") -> "Vector3f":
        ...


    def normalizedPositiveX(self, dir: "Vector3f") -> "Vector3f":
        ...


    def positiveY(self, dir: "Vector3f") -> "Vector3f":
        ...


    def normalizedPositiveY(self, dir: "Vector3f") -> "Vector3f":
        ...


    def hashCode(self) -> int:
        ...


    def equals(self, obj: "Object") -> bool:
        ...


    def equals(self, m: "Matrix3fc", delta: float) -> bool:
        ...


    def swap(self, other: "Matrix3f") -> "Matrix3f":
        """
        Exchange the values of `this` matrix with the given `other` matrix.

        Arguments
        - other: the other matrix to exchange the values with

        Returns
        - this
        """
        ...


    def add(self, other: "Matrix3fc") -> "Matrix3f":
        """
        Component-wise add `this` and `other`.

        Arguments
        - other: the other addend

        Returns
        - this
        """
        ...


    def add(self, other: "Matrix3fc", dest: "Matrix3f") -> "Matrix3f":
        ...


    def sub(self, subtrahend: "Matrix3fc") -> "Matrix3f":
        """
        Component-wise subtract `subtrahend` from `this`.

        Arguments
        - subtrahend: the subtrahend

        Returns
        - this
        """
        ...


    def sub(self, subtrahend: "Matrix3fc", dest: "Matrix3f") -> "Matrix3f":
        ...


    def mulComponentWise(self, other: "Matrix3fc") -> "Matrix3f":
        """
        Component-wise multiply `this` by `other`.

        Arguments
        - other: the other matrix

        Returns
        - this
        """
        ...


    def mulComponentWise(self, other: "Matrix3fc", dest: "Matrix3f") -> "Matrix3f":
        ...


    def setSkewSymmetric(self, a: float, b: float, c: float) -> "Matrix3f":
        """
        Set this matrix to a skew-symmetric matrix using the following layout:
        ```
         0,  a, -b
        -a,  0,  c
         b, -c,  0
        ```
        
        Reference: <a href="https://en.wikipedia.org/wiki/Skew-symmetric_matrix">https://en.wikipedia.org</a>

        Arguments
        - a: the value used for the matrix elements m01 and m10
        - b: the value used for the matrix elements m02 and m20
        - c: the value used for the matrix elements m12 and m21

        Returns
        - this
        """
        ...


    def lerp(self, other: "Matrix3fc", t: float) -> "Matrix3f":
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


    def lerp(self, other: "Matrix3fc", t: float, dest: "Matrix3f") -> "Matrix3f":
        ...


    def rotateTowards(self, direction: "Vector3fc", up: "Vector3fc", dest: "Matrix3f") -> "Matrix3f":
        """
        Apply a model transformation to this matrix for a right-handed coordinate system, 
        that aligns the local `+Z` axis with `direction`
        and store the result in `dest`.
        
        If `M` is `this` matrix and `L` the lookat matrix,
        then the new matrix will be `M * L`. So when transforming a
        vector `v` with the new matrix by using `M * L * v`,
        the lookat transformation will be applied first!
        
        In order to set the matrix to a rotation transformation without post-multiplying it,
        use .rotationTowards(Vector3fc, Vector3fc) rotationTowards().
        
        This method is equivalent to calling: `mul(new Matrix3f().lookAlong(new Vector3f(dir).negate(), up).invert(), dest)`

        Arguments
        - direction: the direction to rotate towards
        - up: the model's up vector
        - dest: will hold the result

        Returns
        - dest

        See
        - .rotationTowards(Vector3fc, Vector3fc)
        """
        ...


    def rotateTowards(self, direction: "Vector3fc", up: "Vector3fc") -> "Matrix3f":
        """
        Apply a model transformation to this matrix for a right-handed coordinate system, 
        that aligns the local `+Z` axis with `direction`.
        
        If `M` is `this` matrix and `L` the lookat matrix,
        then the new matrix will be `M * L`. So when transforming a
        vector `v` with the new matrix by using `M * L * v`,
        the lookat transformation will be applied first!
        
        In order to set the matrix to a rotation transformation without post-multiplying it,
        use .rotationTowards(Vector3fc, Vector3fc) rotationTowards().
        
        This method is equivalent to calling: `mul(new Matrix3f().lookAlong(new Vector3f(dir).negate(), up).invert())`

        Arguments
        - direction: the direction to orient towards
        - up: the up vector

        Returns
        - this

        See
        - .rotationTowards(Vector3fc, Vector3fc)
        """
        ...


    def rotateTowards(self, dirX: float, dirY: float, dirZ: float, upX: float, upY: float, upZ: float) -> "Matrix3f":
        """
        Apply a model transformation to this matrix for a right-handed coordinate system, 
        that aligns the local `+Z` axis with `direction`.
        
        If `M` is `this` matrix and `L` the lookat matrix,
        then the new matrix will be `M * L`. So when transforming a
        vector `v` with the new matrix by using `M * L * v`,
        the lookat transformation will be applied first!
        
        In order to set the matrix to a rotation transformation without post-multiplying it,
        use .rotationTowards(float, float, float, float, float, float) rotationTowards().
        
        This method is equivalent to calling: `mul(new Matrix3f().lookAlong(-dirX, -dirY, -dirZ, upX, upY, upZ).invert())`

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
        - .rotationTowards(float, float, float, float, float, float)
        """
        ...


    def rotateTowards(self, dirX: float, dirY: float, dirZ: float, upX: float, upY: float, upZ: float, dest: "Matrix3f") -> "Matrix3f":
        """
        Apply a model transformation to this matrix for a right-handed coordinate system, 
        that aligns the local `+Z` axis with `dir`
        and store the result in `dest`.
        
        If `M` is `this` matrix and `L` the lookat matrix,
        then the new matrix will be `M * L`. So when transforming a
        vector `v` with the new matrix by using `M * L * v`,
        the lookat transformation will be applied first!
        
        In order to set the matrix to a rotation transformation without post-multiplying it,
        use .rotationTowards(float, float, float, float, float, float) rotationTowards().
        
        This method is equivalent to calling: `mul(new Matrix3f().lookAlong(-dirX, -dirY, -dirZ, upX, upY, upZ).invert(), dest)`

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
        - .rotationTowards(float, float, float, float, float, float)
        """
        ...


    def rotationTowards(self, dir: "Vector3fc", up: "Vector3fc") -> "Matrix3f":
        """
        Set this matrix to a model transformation for a right-handed coordinate system, 
        that aligns the local `-z` axis with `center - eye`.
        
        In order to apply the rotation transformation to a previous existing transformation,
        use .rotateTowards(float, float, float, float, float, float) rotateTowards.
        
        This method is equivalent to calling: `setLookAlong(new Vector3f(dir).negate(), up).invert()`

        Arguments
        - dir: the direction to orient the local -z axis towards
        - up: the up vector

        Returns
        - this

        See
        - .rotateTowards(float, float, float, float, float, float)
        """
        ...


    def rotationTowards(self, dirX: float, dirY: float, dirZ: float, upX: float, upY: float, upZ: float) -> "Matrix3f":
        """
        Set this matrix to a model transformation for a right-handed coordinate system, 
        that aligns the local `-z` axis with `center - eye`.
        
        In order to apply the rotation transformation to a previous existing transformation,
        use .rotateTowards(float, float, float, float, float, float) rotateTowards.
        
        This method is equivalent to calling: `setLookAlong(-dirX, -dirY, -dirZ, upX, upY, upZ).invert()`

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
        - .rotationTowards(float, float, float, float, float, float)
        """
        ...


    def getEulerAnglesZYX(self, dest: "Vector3f") -> "Vector3f":
        ...


    def getEulerAnglesXYZ(self, dest: "Vector3f") -> "Vector3f":
        ...


    def obliqueZ(self, a: float, b: float) -> "Matrix3f":
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
        1 0 a
        0 1 b
        0 0 1
        ```

        Arguments
        - a: the value for the z factor that applies to x
        - b: the value for the z factor that applies to y

        Returns
        - this
        """
        ...


    def obliqueZ(self, a: float, b: float, dest: "Matrix3f") -> "Matrix3f":
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


    def reflect(self, nx: float, ny: float, nz: float, dest: "Matrix3f") -> "Matrix3f":
        ...


    def reflect(self, nx: float, ny: float, nz: float) -> "Matrix3f":
        """
        Apply a mirror/reflection transformation to this matrix that reflects through the given plane
        specified via the plane normal.
        
        If `M` is `this` matrix and `R` the reflection matrix,
        then the new matrix will be `M * R`. So when transforming a
        vector `v` with the new matrix by using `M * R * v`, the
        reflection will be applied first!

        Arguments
        - nx: the x-coordinate of the plane normal
        - ny: the y-coordinate of the plane normal
        - nz: the z-coordinate of the plane normal

        Returns
        - this
        """
        ...


    def reflect(self, normal: "Vector3fc") -> "Matrix3f":
        """
        Apply a mirror/reflection transformation to this matrix that reflects through the given plane
        specified via the plane normal.
        
        If `M` is `this` matrix and `R` the reflection matrix,
        then the new matrix will be `M * R`. So when transforming a
        vector `v` with the new matrix by using `M * R * v`, the
        reflection will be applied first!

        Arguments
        - normal: the plane normal

        Returns
        - this
        """
        ...


    def reflect(self, orientation: "Quaternionfc") -> "Matrix3f":
        """
        Apply a mirror/reflection transformation to this matrix that reflects about a plane
        specified via the plane orientation.
        
        This method can be used to build a reflection transformation based on the orientation of a mirror object in the scene.
        It is assumed that the default mirror plane's normal is `(0, 0, 1)`. So, if the given Quaternionfc is
        the identity (does not apply any additional rotation), the reflection plane will be `z=0`.
        
        If `M` is `this` matrix and `R` the reflection matrix,
        then the new matrix will be `M * R`. So when transforming a
        vector `v` with the new matrix by using `M * R * v`, the
        reflection will be applied first!

        Arguments
        - orientation: the plane orientation

        Returns
        - this
        """
        ...


    def reflect(self, orientation: "Quaternionfc", dest: "Matrix3f") -> "Matrix3f":
        ...


    def reflect(self, normal: "Vector3fc", dest: "Matrix3f") -> "Matrix3f":
        ...


    def reflection(self, nx: float, ny: float, nz: float) -> "Matrix3f":
        """
        Set this matrix to a mirror/reflection transformation that reflects through the given plane
        specified via the plane normal.

        Arguments
        - nx: the x-coordinate of the plane normal
        - ny: the y-coordinate of the plane normal
        - nz: the z-coordinate of the plane normal

        Returns
        - this
        """
        ...


    def reflection(self, normal: "Vector3fc") -> "Matrix3f":
        """
        Set this matrix to a mirror/reflection transformation that reflects through the given plane
        specified via the plane normal.

        Arguments
        - normal: the plane normal

        Returns
        - this
        """
        ...


    def reflection(self, orientation: "Quaternionfc") -> "Matrix3f":
        """
        Set this matrix to a mirror/reflection transformation that reflects through a plane
        specified via the plane orientation.
        
        This method can be used to build a reflection transformation based on the orientation of a mirror object in the scene.
        It is assumed that the default mirror plane's normal is `(0, 0, 1)`. So, if the given Quaternionfc is
        the identity (does not apply any additional rotation), the reflection plane will be `z=0`, offset by the given `point`.

        Arguments
        - orientation: the plane orientation

        Returns
        - this
        """
        ...


    def isFinite(self) -> bool:
        ...


    def quadraticFormProduct(self, x: float, y: float, z: float) -> float:
        ...


    def quadraticFormProduct(self, v: "Vector3fc") -> float:
        ...


    def mapXZY(self) -> "Matrix3f":
        """
        Multiply `this` by the matrix
        ```
        1 0 0
        0 0 1
        0 1 0
        ```

        Returns
        - this
        """
        ...


    def mapXZY(self, dest: "Matrix3f") -> "Matrix3f":
        ...


    def mapXZnY(self) -> "Matrix3f":
        """
        Multiply `this` by the matrix
        ```
        1 0  0
        0 0 -1
        0 1  0
        ```

        Returns
        - this
        """
        ...


    def mapXZnY(self, dest: "Matrix3f") -> "Matrix3f":
        ...


    def mapXnYnZ(self) -> "Matrix3f":
        """
        Multiply `this` by the matrix
        ```
        1  0  0
        0 -1  0
        0  0 -1
        ```

        Returns
        - this
        """
        ...


    def mapXnYnZ(self, dest: "Matrix3f") -> "Matrix3f":
        ...


    def mapXnZY(self) -> "Matrix3f":
        """
        Multiply `this` by the matrix
        ```
        1  0 0
        0  0 1
        0 -1 0
        ```

        Returns
        - this
        """
        ...


    def mapXnZY(self, dest: "Matrix3f") -> "Matrix3f":
        ...


    def mapXnZnY(self) -> "Matrix3f":
        """
        Multiply `this` by the matrix
        ```
        1  0  0
        0  0 -1
        0 -1  0
        ```

        Returns
        - this
        """
        ...


    def mapXnZnY(self, dest: "Matrix3f") -> "Matrix3f":
        ...


    def mapYXZ(self) -> "Matrix3f":
        """
        Multiply `this` by the matrix
        ```
        0 1 0
        1 0 0
        0 0 1
        ```

        Returns
        - this
        """
        ...


    def mapYXZ(self, dest: "Matrix3f") -> "Matrix3f":
        ...


    def mapYXnZ(self) -> "Matrix3f":
        """
        Multiply `this` by the matrix
        ```
        0 1  0
        1 0  0
        0 0 -1
        ```

        Returns
        - this
        """
        ...


    def mapYXnZ(self, dest: "Matrix3f") -> "Matrix3f":
        ...


    def mapYZX(self) -> "Matrix3f":
        """
        Multiply `this` by the matrix
        ```
        0 0 1
        1 0 0
        0 1 0
        ```

        Returns
        - this
        """
        ...


    def mapYZX(self, dest: "Matrix3f") -> "Matrix3f":
        ...


    def mapYZnX(self) -> "Matrix3f":
        """
        Multiply `this` by the matrix
        ```
        0 0 -1
        1 0  0
        0 1  0
        ```

        Returns
        - this
        """
        ...


    def mapYZnX(self, dest: "Matrix3f") -> "Matrix3f":
        ...


    def mapYnXZ(self) -> "Matrix3f":
        """
        Multiply `this` by the matrix
        ```
        0 -1 0
        1  0 0
        0  0 1
        ```

        Returns
        - this
        """
        ...


    def mapYnXZ(self, dest: "Matrix3f") -> "Matrix3f":
        ...


    def mapYnXnZ(self) -> "Matrix3f":
        """
        Multiply `this` by the matrix
        ```
        0 -1  0
        1  0  0
        0  0 -1
        ```

        Returns
        - this
        """
        ...


    def mapYnXnZ(self, dest: "Matrix3f") -> "Matrix3f":
        ...


    def mapYnZX(self) -> "Matrix3f":
        """
        Multiply `this` by the matrix
        ```
        0  0 1
        1  0 0
        0 -1 0
        ```

        Returns
        - this
        """
        ...


    def mapYnZX(self, dest: "Matrix3f") -> "Matrix3f":
        ...


    def mapYnZnX(self) -> "Matrix3f":
        """
        Multiply `this` by the matrix
        ```
        0  0 -1
        1  0  0
        0 -1  0
        ```

        Returns
        - this
        """
        ...


    def mapYnZnX(self, dest: "Matrix3f") -> "Matrix3f":
        ...


    def mapZXY(self) -> "Matrix3f":
        """
        Multiply `this` by the matrix
        ```
        0 1 0
        0 0 1
        1 0 0
        ```

        Returns
        - this
        """
        ...


    def mapZXY(self, dest: "Matrix3f") -> "Matrix3f":
        ...


    def mapZXnY(self) -> "Matrix3f":
        """
        Multiply `this` by the matrix
        ```
        0 1  0
        0 0 -1
        1 0  0
        ```

        Returns
        - this
        """
        ...


    def mapZXnY(self, dest: "Matrix3f") -> "Matrix3f":
        ...


    def mapZYX(self) -> "Matrix3f":
        """
        Multiply `this` by the matrix
        ```
        0 0 1
        0 1 0
        1 0 0
        ```

        Returns
        - this
        """
        ...


    def mapZYX(self, dest: "Matrix3f") -> "Matrix3f":
        ...


    def mapZYnX(self) -> "Matrix3f":
        """
        Multiply `this` by the matrix
        ```
        0 0 -1
        0 1  0
        1 0  0
        ```

        Returns
        - this
        """
        ...


    def mapZYnX(self, dest: "Matrix3f") -> "Matrix3f":
        ...


    def mapZnXY(self) -> "Matrix3f":
        """
        Multiply `this` by the matrix
        ```
        0 -1 0
        0  0 1
        1  0 0
        ```

        Returns
        - this
        """
        ...


    def mapZnXY(self, dest: "Matrix3f") -> "Matrix3f":
        ...


    def mapZnXnY(self) -> "Matrix3f":
        """
        Multiply `this` by the matrix
        ```
        0 -1  0
        0  0 -1
        1  0  0
        ```

        Returns
        - this
        """
        ...


    def mapZnXnY(self, dest: "Matrix3f") -> "Matrix3f":
        ...


    def mapZnYX(self) -> "Matrix3f":
        """
        Multiply `this` by the matrix
        ```
        0  0 1
        0 -1 0
        1  0 0
        ```

        Returns
        - this
        """
        ...


    def mapZnYX(self, dest: "Matrix3f") -> "Matrix3f":
        ...


    def mapZnYnX(self) -> "Matrix3f":
        """
        Multiply `this` by the matrix
        ```
        0  0 -1
        0 -1  0
        1  0  0
        ```

        Returns
        - this
        """
        ...


    def mapZnYnX(self, dest: "Matrix3f") -> "Matrix3f":
        ...


    def mapnXYnZ(self) -> "Matrix3f":
        """
        Multiply `this` by the matrix
        ```
        -1 0  0
         0 1  0
         0 0 -1
        ```

        Returns
        - this
        """
        ...


    def mapnXYnZ(self, dest: "Matrix3f") -> "Matrix3f":
        ...


    def mapnXZY(self) -> "Matrix3f":
        """
        Multiply `this` by the matrix
        ```
        -1 0 0
         0 0 1
         0 1 0
        ```

        Returns
        - this
        """
        ...


    def mapnXZY(self, dest: "Matrix3f") -> "Matrix3f":
        ...


    def mapnXZnY(self) -> "Matrix3f":
        """
        Multiply `this` by the matrix
        ```
        -1 0  0
         0 0 -1
         0 1  0
        ```

        Returns
        - this
        """
        ...


    def mapnXZnY(self, dest: "Matrix3f") -> "Matrix3f":
        ...


    def mapnXnYZ(self) -> "Matrix3f":
        """
        Multiply `this` by the matrix
        ```
        -1  0 0
         0 -1 0
         0  0 1
        ```

        Returns
        - this
        """
        ...


    def mapnXnYZ(self, dest: "Matrix3f") -> "Matrix3f":
        ...


    def mapnXnYnZ(self) -> "Matrix3f":
        """
        Multiply `this` by the matrix
        ```
        -1  0  0
         0 -1  0
         0  0 -1
        ```

        Returns
        - this
        """
        ...


    def mapnXnYnZ(self, dest: "Matrix3f") -> "Matrix3f":
        ...


    def mapnXnZY(self) -> "Matrix3f":
        """
        Multiply `this` by the matrix
        ```
        -1  0 0
         0  0 1
         0 -1 0
        ```

        Returns
        - this
        """
        ...


    def mapnXnZY(self, dest: "Matrix3f") -> "Matrix3f":
        ...


    def mapnXnZnY(self) -> "Matrix3f":
        """
        Multiply `this` by the matrix
        ```
        -1  0  0
         0  0 -1
         0 -1  0
        ```

        Returns
        - this
        """
        ...


    def mapnXnZnY(self, dest: "Matrix3f") -> "Matrix3f":
        ...


    def mapnYXZ(self) -> "Matrix3f":
        """
        Multiply `this` by the matrix
        ```
         0 1 0
        -1 0 0
         0 0 1
        ```

        Returns
        - this
        """
        ...


    def mapnYXZ(self, dest: "Matrix3f") -> "Matrix3f":
        ...


    def mapnYXnZ(self) -> "Matrix3f":
        """
        Multiply `this` by the matrix
        ```
         0 1  0
        -1 0  0
         0 0 -1
        ```

        Returns
        - this
        """
        ...


    def mapnYXnZ(self, dest: "Matrix3f") -> "Matrix3f":
        ...


    def mapnYZX(self) -> "Matrix3f":
        """
        Multiply `this` by the matrix
        ```
         0 0 1
        -1 0 0
         0 1 0
        ```

        Returns
        - this
        """
        ...


    def mapnYZX(self, dest: "Matrix3f") -> "Matrix3f":
        ...


    def mapnYZnX(self) -> "Matrix3f":
        """
        Multiply `this` by the matrix
        ```
         0 0 -1
        -1 0  0
         0 1  0
        ```

        Returns
        - this
        """
        ...


    def mapnYZnX(self, dest: "Matrix3f") -> "Matrix3f":
        ...


    def mapnYnXZ(self) -> "Matrix3f":
        """
        Multiply `this` by the matrix
        ```
         0 -1 0
        -1  0 0
         0  0 1
        ```

        Returns
        - this
        """
        ...


    def mapnYnXZ(self, dest: "Matrix3f") -> "Matrix3f":
        ...


    def mapnYnXnZ(self) -> "Matrix3f":
        """
        Multiply `this` by the matrix
        ```
         0 -1  0
        -1  0  0
         0  0 -1
        ```

        Returns
        - this
        """
        ...


    def mapnYnXnZ(self, dest: "Matrix3f") -> "Matrix3f":
        ...


    def mapnYnZX(self) -> "Matrix3f":
        """
        Multiply `this` by the matrix
        ```
         0  0 1
        -1  0 0
         0 -1 0
        ```

        Returns
        - this
        """
        ...


    def mapnYnZX(self, dest: "Matrix3f") -> "Matrix3f":
        ...


    def mapnYnZnX(self) -> "Matrix3f":
        """
        Multiply `this` by the matrix
        ```
         0  0 -1
        -1  0  0
         0 -1  0
        ```

        Returns
        - this
        """
        ...


    def mapnYnZnX(self, dest: "Matrix3f") -> "Matrix3f":
        ...


    def mapnZXY(self) -> "Matrix3f":
        """
        Multiply `this` by the matrix
        ```
         0 1 0
         0 0 1
        -1 0 0
        ```

        Returns
        - this
        """
        ...


    def mapnZXY(self, dest: "Matrix3f") -> "Matrix3f":
        ...


    def mapnZXnY(self) -> "Matrix3f":
        """
        Multiply `this` by the matrix
        ```
         0 1  0
         0 0 -1
        -1 0  0
        ```

        Returns
        - this
        """
        ...


    def mapnZXnY(self, dest: "Matrix3f") -> "Matrix3f":
        ...


    def mapnZYX(self) -> "Matrix3f":
        """
        Multiply `this` by the matrix
        ```
         0 0 1
         0 1 0
        -1 0 0
        ```

        Returns
        - this
        """
        ...


    def mapnZYX(self, dest: "Matrix3f") -> "Matrix3f":
        ...


    def mapnZYnX(self) -> "Matrix3f":
        """
        Multiply `this` by the matrix
        ```
         0 0 -1
         0 1  0
        -1 0  0
        ```

        Returns
        - this
        """
        ...


    def mapnZYnX(self, dest: "Matrix3f") -> "Matrix3f":
        ...


    def mapnZnXY(self) -> "Matrix3f":
        """
        Multiply `this` by the matrix
        ```
         0 -1 0
         0  0 1
        -1  0 0
        ```

        Returns
        - this
        """
        ...


    def mapnZnXY(self, dest: "Matrix3f") -> "Matrix3f":
        ...


    def mapnZnXnY(self) -> "Matrix3f":
        """
        Multiply `this` by the matrix
        ```
         0 -1  0
         0  0 -1
        -1  0  0
        ```

        Returns
        - this
        """
        ...


    def mapnZnXnY(self, dest: "Matrix3f") -> "Matrix3f":
        ...


    def mapnZnYX(self) -> "Matrix3f":
        """
        Multiply `this` by the matrix
        ```
         0  0 1
         0 -1 0
        -1  0 0
        ```

        Returns
        - this
        """
        ...


    def mapnZnYX(self, dest: "Matrix3f") -> "Matrix3f":
        ...


    def mapnZnYnX(self) -> "Matrix3f":
        """
        Multiply `this` by the matrix
        ```
         0  0 -1
         0 -1  0
        -1  0  0
        ```

        Returns
        - this
        """
        ...


    def mapnZnYnX(self, dest: "Matrix3f") -> "Matrix3f":
        ...


    def negateX(self) -> "Matrix3f":
        """
        Multiply `this` by the matrix
        ```
        -1 0 0
         0 1 0
         0 0 1
        ```

        Returns
        - this
        """
        ...


    def negateX(self, dest: "Matrix3f") -> "Matrix3f":
        ...


    def negateY(self) -> "Matrix3f":
        """
        Multiply `this` by the matrix
        ```
        1  0 0
        0 -1 0
        0  0 1
        ```

        Returns
        - this
        """
        ...


    def negateY(self, dest: "Matrix3f") -> "Matrix3f":
        ...


    def negateZ(self) -> "Matrix3f":
        """
        Multiply `this` by the matrix
        ```
        1 0  0
        0 1  0
        0 0 -1
        ```

        Returns
        - this
        """
        ...


    def negateZ(self, dest: "Matrix3f") -> "Matrix3f":
        ...


    def clone(self) -> "Object":
        ...
