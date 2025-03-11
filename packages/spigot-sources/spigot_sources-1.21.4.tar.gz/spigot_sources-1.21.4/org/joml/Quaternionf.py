"""
Python module generated from Java source file org.joml.Quaternionf

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


class Quaternionf(Externalizable, Cloneable, Quaternionfc):
    """
    Quaternion of 4 single-precision floats which can represent rotation and uniform scaling.

    Author(s)
    - Kai Burjack
    """

    def __init__(self):
        """
        Create a new Quaternionf and initialize it with `(x=0, y=0, z=0, w=1)`, 
        where `(x, y, z)` is the vector part of the quaternion and `w` is the real/scalar part.
        """
        ...


    def __init__(self, x: float, y: float, z: float, w: float):
        """
        Create a new Quaternionf and initialize its components to the given values.

        Arguments
        - x: the first component of the imaginary part
        - y: the second component of the imaginary part
        - z: the third component of the imaginary part
        - w: the real part
        """
        ...


    def __init__(self, x: float, y: float, z: float, w: float):
        """
        Create a new Quaternionf and initialize its components to the given values.

        Arguments
        - x: the first component of the imaginary part
        - y: the second component of the imaginary part
        - z: the third component of the imaginary part
        - w: the real part
        """
        ...


    def __init__(self, source: "Quaternionfc"):
        """
        Create a new Quaternionf and initialize its components to the same values as the given Quaternionfc.

        Arguments
        - source: the Quaternionfc to take the component values from
        """
        ...


    def __init__(self, source: "Quaterniondc"):
        """
        Create a new Quaternionf and initialize its components to the same values as the given Quaterniondc.

        Arguments
        - source: the Quaterniondc to take the component values from
        """
        ...


    def __init__(self, axisAngle: "AxisAngle4f"):
        """
        Create a new Quaternionf which represents the rotation of the given AxisAngle4f.

        Arguments
        - axisAngle: the AxisAngle4f
        """
        ...


    def __init__(self, axisAngle: "AxisAngle4d"):
        """
        Create a new Quaterniond which represents the rotation of the given AxisAngle4d.

        Arguments
        - axisAngle: the AxisAngle4d
        """
        ...


    def x(self) -> float:
        """
        Returns
        - the first component of the vector part
        """
        ...


    def y(self) -> float:
        """
        Returns
        - the second component of the vector part
        """
        ...


    def z(self) -> float:
        """
        Returns
        - the third component of the vector part
        """
        ...


    def w(self) -> float:
        """
        Returns
        - the real/scalar part of the quaternion
        """
        ...


    def normalize(self) -> "Quaternionf":
        """
        Normalize this quaternion.

        Returns
        - this
        """
        ...


    def normalize(self, dest: "Quaternionf") -> "Quaternionf":
        ...


    def add(self, x: float, y: float, z: float, w: float) -> "Quaternionf":
        """
        Add the quaternion `(x, y, z, w)` to this quaternion.

        Arguments
        - x: the x component of the vector part
        - y: the y component of the vector part
        - z: the z component of the vector part
        - w: the real/scalar component

        Returns
        - this
        """
        ...


    def add(self, x: float, y: float, z: float, w: float, dest: "Quaternionf") -> "Quaternionf":
        ...


    def add(self, q2: "Quaternionfc") -> "Quaternionf":
        """
        Add `q2` to this quaternion.

        Arguments
        - q2: the quaternion to add to this

        Returns
        - this
        """
        ...


    def add(self, q2: "Quaternionfc", dest: "Quaternionf") -> "Quaternionf":
        ...


    def sub(self, x: float, y: float, z: float, w: float) -> "Quaternionf":
        """
        Subtract the quaternion `(x, y, z, w)` from this quaternion.

        Arguments
        - x: the x component of the vector part
        - y: the y component of the vector part
        - z: the z component of the vector part
        - w: the real/scalar component

        Returns
        - this
        """
        ...


    def sub(self, x: float, y: float, z: float, w: float, dest: "Quaternionf") -> "Quaternionf":
        ...


    def sub(self, q2: "Quaternionfc") -> "Quaternionf":
        """
        Subtract `q2` from this quaternion.

        Arguments
        - q2: the quaternion to add to this

        Returns
        - this
        """
        ...


    def sub(self, q2: "Quaternionfc", dest: "Quaternionf") -> "Quaternionf":
        ...


    def dot(self, otherQuat: "Quaternionf") -> float:
        """
        Return the dot of this quaternion and `otherQuat`.

        Arguments
        - otherQuat: the other quaternion

        Returns
        - the dot product
        """
        ...


    def angle(self) -> float:
        ...


    def get(self, dest: "Matrix3f") -> "Matrix3f":
        ...


    def get(self, dest: "Matrix3d") -> "Matrix3d":
        ...


    def get(self, dest: "Matrix4f") -> "Matrix4f":
        ...


    def get(self, dest: "Matrix4d") -> "Matrix4d":
        ...


    def get(self, dest: "Matrix4x3f") -> "Matrix4x3f":
        ...


    def get(self, dest: "Matrix4x3d") -> "Matrix4x3d":
        ...


    def get(self, dest: "AxisAngle4f") -> "AxisAngle4f":
        ...


    def get(self, dest: "AxisAngle4d") -> "AxisAngle4d":
        ...


    def get(self, dest: "Quaterniond") -> "Quaterniond":
        ...


    def get(self, dest: "Quaternionf") -> "Quaternionf":
        """
        Set the given Quaternionf to the values of `this`.

        Arguments
        - dest: the Quaternionf to set

        Returns
        - the passed in destination

        See
        - .set(Quaternionfc)
        """
        ...


    def getAsMatrix3f(self, dest: "ByteBuffer") -> "ByteBuffer":
        ...


    def getAsMatrix3f(self, dest: "FloatBuffer") -> "FloatBuffer":
        ...


    def getAsMatrix4f(self, dest: "ByteBuffer") -> "ByteBuffer":
        ...


    def getAsMatrix4f(self, dest: "FloatBuffer") -> "FloatBuffer":
        ...


    def getAsMatrix4x3f(self, dest: "ByteBuffer") -> "ByteBuffer":
        ...


    def getAsMatrix4x3f(self, dest: "FloatBuffer") -> "FloatBuffer":
        ...


    def set(self, x: float, y: float, z: float, w: float) -> "Quaternionf":
        """
        Set this quaternion to the given values.

        Arguments
        - x: the new value of x
        - y: the new value of y
        - z: the new value of z
        - w: the new value of w

        Returns
        - this
        """
        ...


    def set(self, q: "Quaternionfc") -> "Quaternionf":
        """
        Set this quaternion to be a copy of `q`.

        Arguments
        - q: the Quaternionfc to copy

        Returns
        - this
        """
        ...


    def set(self, q: "Quaterniondc") -> "Quaternionf":
        """
        Set this quaternion to be a copy of `q`.

        Arguments
        - q: the Quaterniondc to copy

        Returns
        - this
        """
        ...


    def set(self, axisAngle: "AxisAngle4f") -> "Quaternionf":
        """
        Set this quaternion to a rotation equivalent to the given AxisAngle4f.

        Arguments
        - axisAngle: the AxisAngle4f

        Returns
        - this
        """
        ...


    def set(self, axisAngle: "AxisAngle4d") -> "Quaternionf":
        """
        Set this quaternion to a rotation equivalent to the given AxisAngle4d.

        Arguments
        - axisAngle: the AxisAngle4d

        Returns
        - this
        """
        ...


    def setAngleAxis(self, angle: float, x: float, y: float, z: float) -> "Quaternionf":
        """
        Set this quaternion to a rotation equivalent to the supplied axis and
        angle (in radians).
        
        This method assumes that the given rotation axis `(x, y, z)` is already normalized

        Arguments
        - angle: the angle in radians
        - x: the x-component of the normalized rotation axis
        - y: the y-component of the normalized rotation axis
        - z: the z-component of the normalized rotation axis

        Returns
        - this
        """
        ...


    def setAngleAxis(self, angle: float, x: float, y: float, z: float) -> "Quaternionf":
        """
        Set this quaternion to a rotation equivalent to the supplied axis and
        angle (in radians).
        
        This method assumes that the given rotation axis `(x, y, z)` is already normalized

        Arguments
        - angle: the angle in radians
        - x: the x-component of the normalized rotation axis
        - y: the y-component of the normalized rotation axis
        - z: the z-component of the normalized rotation axis

        Returns
        - this
        """
        ...


    def rotationAxis(self, axisAngle: "AxisAngle4f") -> "Quaternionf":
        """
        Set this Quaternionf to a rotation of the given angle in radians about the supplied
        axis, all of which are specified via the AxisAngle4f.

        Arguments
        - axisAngle: the AxisAngle4f giving the rotation angle in radians and the axis to rotate about

        Returns
        - this

        See
        - .rotationAxis(float, float, float, float)
        """
        ...


    def rotationAxis(self, angle: float, axisX: float, axisY: float, axisZ: float) -> "Quaternionf":
        """
        Set this quaternion to a rotation of the given angle in radians about the supplied axis.

        Arguments
        - angle: the rotation angle in radians
        - axisX: the x-coordinate of the rotation axis
        - axisY: the y-coordinate of the rotation axis
        - axisZ: the z-coordinate of the rotation axis

        Returns
        - this
        """
        ...


    def rotationAxis(self, angle: float, axis: "Vector3fc") -> "Quaternionf":
        """
        Set this quaternion to a rotation of the given angle in radians about the supplied axis.

        Arguments
        - angle: the rotation angle in radians
        - axis: the axis to rotate about

        Returns
        - this

        See
        - .rotationAxis(float, float, float, float)
        """
        ...


    def rotationX(self, angle: float) -> "Quaternionf":
        """
        Set this quaternion to represent a rotation of the given radians about the x axis.

        Arguments
        - angle: the angle in radians to rotate about the x axis

        Returns
        - this
        """
        ...


    def rotationY(self, angle: float) -> "Quaternionf":
        """
        Set this quaternion to represent a rotation of the given radians about the y axis.

        Arguments
        - angle: the angle in radians to rotate about the y axis

        Returns
        - this
        """
        ...


    def rotationZ(self, angle: float) -> "Quaternionf":
        """
        Set this quaternion to represent a rotation of the given radians about the z axis.

        Arguments
        - angle: the angle in radians to rotate about the z axis

        Returns
        - this
        """
        ...


    def setFromUnnormalized(self, mat: "Matrix4fc") -> "Quaternionf":
        """
        Set this quaternion to be a representation of the rotational component of the given matrix.
        
        This method assumes that the first three columns of the upper left 3x3 submatrix are no unit vectors.

        Arguments
        - mat: the matrix whose rotational component is used to set this quaternion

        Returns
        - this
        """
        ...


    def setFromUnnormalized(self, mat: "Matrix4x3fc") -> "Quaternionf":
        """
        Set this quaternion to be a representation of the rotational component of the given matrix.
        
        This method assumes that the first three columns of the upper left 3x3 submatrix are no unit vectors.

        Arguments
        - mat: the matrix whose rotational component is used to set this quaternion

        Returns
        - this
        """
        ...


    def setFromUnnormalized(self, mat: "Matrix4x3dc") -> "Quaternionf":
        """
        Set this quaternion to be a representation of the rotational component of the given matrix.
        
        This method assumes that the first three columns of the upper left 3x3 submatrix are no unit vectors.

        Arguments
        - mat: the matrix whose rotational component is used to set this quaternion

        Returns
        - this
        """
        ...


    def setFromNormalized(self, mat: "Matrix4fc") -> "Quaternionf":
        """
        Set this quaternion to be a representation of the rotational component of the given matrix.
        
        This method assumes that the first three columns of the upper left 3x3 submatrix are unit vectors.

        Arguments
        - mat: the matrix whose rotational component is used to set this quaternion

        Returns
        - this
        """
        ...


    def setFromNormalized(self, mat: "Matrix4x3fc") -> "Quaternionf":
        """
        Set this quaternion to be a representation of the rotational component of the given matrix.
        
        This method assumes that the first three columns of the upper left 3x3 submatrix are unit vectors.

        Arguments
        - mat: the matrix whose rotational component is used to set this quaternion

        Returns
        - this
        """
        ...


    def setFromNormalized(self, mat: "Matrix4x3dc") -> "Quaternionf":
        """
        Set this quaternion to be a representation of the rotational component of the given matrix.
        
        This method assumes that the first three columns of the upper left 3x3 submatrix are unit vectors.

        Arguments
        - mat: the matrix whose rotational component is used to set this quaternion

        Returns
        - this
        """
        ...


    def setFromUnnormalized(self, mat: "Matrix4dc") -> "Quaternionf":
        """
        Set this quaternion to be a representation of the rotational component of the given matrix.
        
        This method assumes that the first three columns of the upper left 3x3 submatrix are no unit vectors.

        Arguments
        - mat: the matrix whose rotational component is used to set this quaternion

        Returns
        - this
        """
        ...


    def setFromNormalized(self, mat: "Matrix4dc") -> "Quaternionf":
        """
        Set this quaternion to be a representation of the rotational component of the given matrix.
        
        This method assumes that the first three columns of the upper left 3x3 submatrix are unit vectors.

        Arguments
        - mat: the matrix whose rotational component is used to set this quaternion

        Returns
        - this
        """
        ...


    def setFromUnnormalized(self, mat: "Matrix3fc") -> "Quaternionf":
        """
        Set this quaternion to be a representation of the rotational component of the given matrix.
        
        This method assumes that the first three columns of the upper left 3x3 submatrix are no unit vectors.

        Arguments
        - mat: the matrix whose rotational component is used to set this quaternion

        Returns
        - this
        """
        ...


    def setFromNormalized(self, mat: "Matrix3fc") -> "Quaternionf":
        """
        Set this quaternion to be a representation of the rotational component of the given matrix.
        
        This method assumes that the first three columns of the upper left 3x3 submatrix are unit vectors.

        Arguments
        - mat: the matrix whose rotational component is used to set this quaternion

        Returns
        - this
        """
        ...


    def setFromUnnormalized(self, mat: "Matrix3dc") -> "Quaternionf":
        """
        Set this quaternion to be a representation of the rotational component of the given matrix.
        
        This method assumes that the first three columns of the upper left 3x3 submatrix are no unit vectors.

        Arguments
        - mat: the matrix whose rotational component is used to set this quaternion

        Returns
        - this
        """
        ...


    def setFromNormalized(self, mat: "Matrix3dc") -> "Quaternionf":
        """
        Set this quaternion to be a representation of the rotational component of the given matrix.

        Arguments
        - mat: the matrix whose rotational component is used to set this quaternion

        Returns
        - this
        """
        ...


    def fromAxisAngleRad(self, axis: "Vector3fc", angle: float) -> "Quaternionf":
        """
        Set this quaternion to be a representation of the supplied axis and
        angle (in radians).

        Arguments
        - axis: the rotation axis
        - angle: the angle in radians

        Returns
        - this
        """
        ...


    def fromAxisAngleRad(self, axisX: float, axisY: float, axisZ: float, angle: float) -> "Quaternionf":
        """
        Set this quaternion to be a representation of the supplied axis and
        angle (in radians).

        Arguments
        - axisX: the x component of the rotation axis
        - axisY: the y component of the rotation axis
        - axisZ: the z component of the rotation axis
        - angle: the angle in radians

        Returns
        - this
        """
        ...


    def fromAxisAngleDeg(self, axis: "Vector3fc", angle: float) -> "Quaternionf":
        """
        Set this quaternion to be a representation of the supplied axis and
        angle (in degrees).

        Arguments
        - axis: the rotation axis
        - angle: the angle in degrees

        Returns
        - this
        """
        ...


    def fromAxisAngleDeg(self, axisX: float, axisY: float, axisZ: float, angle: float) -> "Quaternionf":
        """
        Set this quaternion to be a representation of the supplied axis and
        angle (in degrees).

        Arguments
        - axisX: the x component of the rotation axis
        - axisY: the y component of the rotation axis
        - axisZ: the z component of the rotation axis
        - angle: the angle in degrees

        Returns
        - this
        """
        ...


    def mul(self, q: "Quaternionfc") -> "Quaternionf":
        """
        Multiply this quaternion by `q`.
        
        If `T` is `this` and `Q` is the given
        quaternion, then the resulting quaternion `R` is:
        
        `R = T * Q`
        
        So, this method uses post-multiplication like the matrix classes, resulting in a
        vector to be transformed by `Q` first, and then by `T`.

        Arguments
        - q: the quaternion to multiply `this` by

        Returns
        - this
        """
        ...


    def mul(self, q: "Quaternionfc", dest: "Quaternionf") -> "Quaternionf":
        ...


    def mul(self, qx: float, qy: float, qz: float, qw: float) -> "Quaternionf":
        """
        Multiply this quaternion by the quaternion represented via `(qx, qy, qz, qw)`.
        
        If `T` is `this` and `Q` is the given
        quaternion, then the resulting quaternion `R` is:
        
        `R = T * Q`
        
        So, this method uses post-multiplication like the matrix classes, resulting in a
        vector to be transformed by `Q` first, and then by `T`.

        Arguments
        - qx: the x component of the quaternion to multiply `this` by
        - qy: the y component of the quaternion to multiply `this` by
        - qz: the z component of the quaternion to multiply `this` by
        - qw: the w component of the quaternion to multiply `this` by

        Returns
        - this
        """
        ...


    def mul(self, qx: float, qy: float, qz: float, qw: float, dest: "Quaternionf") -> "Quaternionf":
        ...


    def mul(self, f: float) -> "Quaternionf":
        """
        Multiply this quaternion by the given scalar.
        
        This method multiplies all of the four components by the specified scalar.

        Arguments
        - f: the factor to multiply all components by

        Returns
        - this
        """
        ...


    def mul(self, f: float, dest: "Quaternionf") -> "Quaternionf":
        ...


    def premul(self, q: "Quaternionfc") -> "Quaternionf":
        """
        Pre-multiply this quaternion by `q`.
        
        If `T` is `this` and `Q` is the given quaternion, then the resulting quaternion `R` is:
        
        `R = Q * T`
        
        So, this method uses pre-multiplication, resulting in a vector to be transformed by `T` first, and then by `Q`.

        Arguments
        - q: the quaternion to pre-multiply `this` by

        Returns
        - this
        """
        ...


    def premul(self, q: "Quaternionfc", dest: "Quaternionf") -> "Quaternionf":
        ...


    def premul(self, qx: float, qy: float, qz: float, qw: float) -> "Quaternionf":
        """
        Pre-multiply this quaternion by the quaternion represented via `(qx, qy, qz, qw)`.
        
        If `T` is `this` and `Q` is the given quaternion, then the resulting quaternion `R` is:
        
        `R = Q * T`
        
        So, this method uses pre-multiplication, resulting in a vector to be transformed by `T` first, and then by `Q`.

        Arguments
        - qx: the x component of the quaternion to multiply `this` by
        - qy: the y component of the quaternion to multiply `this` by
        - qz: the z component of the quaternion to multiply `this` by
        - qw: the w component of the quaternion to multiply `this` by

        Returns
        - this
        """
        ...


    def premul(self, qx: float, qy: float, qz: float, qw: float, dest: "Quaternionf") -> "Quaternionf":
        ...


    def transform(self, vec: "Vector3f") -> "Vector3f":
        ...


    def transformInverse(self, vec: "Vector3f") -> "Vector3f":
        ...


    def transformPositiveX(self, dest: "Vector3f") -> "Vector3f":
        ...


    def transformPositiveX(self, dest: "Vector4f") -> "Vector4f":
        ...


    def transformUnitPositiveX(self, dest: "Vector3f") -> "Vector3f":
        ...


    def transformUnitPositiveX(self, dest: "Vector4f") -> "Vector4f":
        ...


    def transformPositiveY(self, dest: "Vector3f") -> "Vector3f":
        ...


    def transformPositiveY(self, dest: "Vector4f") -> "Vector4f":
        ...


    def transformUnitPositiveY(self, dest: "Vector4f") -> "Vector4f":
        ...


    def transformUnitPositiveY(self, dest: "Vector3f") -> "Vector3f":
        ...


    def transformPositiveZ(self, dest: "Vector3f") -> "Vector3f":
        ...


    def transformPositiveZ(self, dest: "Vector4f") -> "Vector4f":
        ...


    def transformUnitPositiveZ(self, dest: "Vector4f") -> "Vector4f":
        ...


    def transformUnitPositiveZ(self, dest: "Vector3f") -> "Vector3f":
        ...


    def transform(self, vec: "Vector4f") -> "Vector4f":
        ...


    def transformInverse(self, vec: "Vector4f") -> "Vector4f":
        ...


    def transform(self, vec: "Vector3fc", dest: "Vector3f") -> "Vector3f":
        ...


    def transformInverse(self, vec: "Vector3fc", dest: "Vector3f") -> "Vector3f":
        ...


    def transform(self, x: float, y: float, z: float, dest: "Vector3f") -> "Vector3f":
        ...


    def transformInverse(self, x: float, y: float, z: float, dest: "Vector3f") -> "Vector3f":
        ...


    def transformUnit(self, vec: "Vector3f") -> "Vector3f":
        ...


    def transformInverseUnit(self, vec: "Vector3f") -> "Vector3f":
        ...


    def transformUnit(self, vec: "Vector3fc", dest: "Vector3f") -> "Vector3f":
        ...


    def transformInverseUnit(self, vec: "Vector3fc", dest: "Vector3f") -> "Vector3f":
        ...


    def transformUnit(self, x: float, y: float, z: float, dest: "Vector3f") -> "Vector3f":
        ...


    def transformInverseUnit(self, x: float, y: float, z: float, dest: "Vector3f") -> "Vector3f":
        ...


    def transform(self, vec: "Vector4fc", dest: "Vector4f") -> "Vector4f":
        ...


    def transformInverse(self, vec: "Vector4fc", dest: "Vector4f") -> "Vector4f":
        ...


    def transform(self, x: float, y: float, z: float, dest: "Vector4f") -> "Vector4f":
        ...


    def transformInverse(self, x: float, y: float, z: float, dest: "Vector4f") -> "Vector4f":
        ...


    def transform(self, vec: "Vector3d") -> "Vector3d":
        ...


    def transformInverse(self, vec: "Vector3d") -> "Vector3d":
        ...


    def transformUnit(self, vec: "Vector4f") -> "Vector4f":
        ...


    def transformInverseUnit(self, vec: "Vector4f") -> "Vector4f":
        ...


    def transformUnit(self, vec: "Vector4fc", dest: "Vector4f") -> "Vector4f":
        ...


    def transformInverseUnit(self, vec: "Vector4fc", dest: "Vector4f") -> "Vector4f":
        ...


    def transformUnit(self, x: float, y: float, z: float, dest: "Vector4f") -> "Vector4f":
        ...


    def transformInverseUnit(self, x: float, y: float, z: float, dest: "Vector4f") -> "Vector4f":
        ...


    def transformPositiveX(self, dest: "Vector3d") -> "Vector3d":
        ...


    def transformPositiveX(self, dest: "Vector4d") -> "Vector4d":
        ...


    def transformUnitPositiveX(self, dest: "Vector3d") -> "Vector3d":
        ...


    def transformUnitPositiveX(self, dest: "Vector4d") -> "Vector4d":
        ...


    def transformPositiveY(self, dest: "Vector3d") -> "Vector3d":
        ...


    def transformPositiveY(self, dest: "Vector4d") -> "Vector4d":
        ...


    def transformUnitPositiveY(self, dest: "Vector4d") -> "Vector4d":
        ...


    def transformUnitPositiveY(self, dest: "Vector3d") -> "Vector3d":
        ...


    def transformPositiveZ(self, dest: "Vector3d") -> "Vector3d":
        ...


    def transformPositiveZ(self, dest: "Vector4d") -> "Vector4d":
        ...


    def transformUnitPositiveZ(self, dest: "Vector4d") -> "Vector4d":
        ...


    def transformUnitPositiveZ(self, dest: "Vector3d") -> "Vector3d":
        ...


    def transform(self, vec: "Vector4d") -> "Vector4d":
        ...


    def transformInverse(self, vec: "Vector4d") -> "Vector4d":
        ...


    def transform(self, vec: "Vector3dc", dest: "Vector3d") -> "Vector3d":
        ...


    def transformInverse(self, vec: "Vector3dc", dest: "Vector3d") -> "Vector3d":
        ...


    def transform(self, x: float, y: float, z: float, dest: "Vector3d") -> "Vector3d":
        ...


    def transformInverse(self, x: float, y: float, z: float, dest: "Vector3d") -> "Vector3d":
        ...


    def transform(self, x: float, y: float, z: float, dest: "Vector3d") -> "Vector3d":
        ...


    def transformInverse(self, x: float, y: float, z: float, dest: "Vector3d") -> "Vector3d":
        ...


    def transform(self, vec: "Vector4dc", dest: "Vector4d") -> "Vector4d":
        ...


    def transformInverse(self, vec: "Vector4dc", dest: "Vector4d") -> "Vector4d":
        ...


    def transform(self, x: float, y: float, z: float, dest: "Vector4d") -> "Vector4d":
        ...


    def transformInverse(self, x: float, y: float, z: float, dest: "Vector4d") -> "Vector4d":
        ...


    def transformUnit(self, vec: "Vector4d") -> "Vector4d":
        ...


    def transformInverseUnit(self, vec: "Vector4d") -> "Vector4d":
        ...


    def transformUnit(self, vec: "Vector3dc", dest: "Vector3d") -> "Vector3d":
        ...


    def transformInverseUnit(self, vec: "Vector3dc", dest: "Vector3d") -> "Vector3d":
        ...


    def transformUnit(self, x: float, y: float, z: float, dest: "Vector3d") -> "Vector3d":
        ...


    def transformInverseUnit(self, x: float, y: float, z: float, dest: "Vector3d") -> "Vector3d":
        ...


    def transformUnit(self, x: float, y: float, z: float, dest: "Vector3d") -> "Vector3d":
        ...


    def transformInverseUnit(self, x: float, y: float, z: float, dest: "Vector3d") -> "Vector3d":
        ...


    def transformUnit(self, vec: "Vector4dc", dest: "Vector4d") -> "Vector4d":
        ...


    def transformInverseUnit(self, vec: "Vector4dc", dest: "Vector4d") -> "Vector4d":
        ...


    def transformUnit(self, x: float, y: float, z: float, dest: "Vector4d") -> "Vector4d":
        ...


    def transformInverseUnit(self, x: float, y: float, z: float, dest: "Vector4d") -> "Vector4d":
        ...


    def invert(self, dest: "Quaternionf") -> "Quaternionf":
        ...


    def invert(self) -> "Quaternionf":
        """
        Invert this quaternion and .normalize() normalize it.
        
        If this quaternion is already normalized, then .conjugate() should be used instead.

        Returns
        - this

        See
        - .conjugate()
        """
        ...


    def div(self, b: "Quaternionfc", dest: "Quaternionf") -> "Quaternionf":
        ...


    def div(self, b: "Quaternionfc") -> "Quaternionf":
        """
        Divide `this` quaternion by `b`.
        
        The division expressed using the inverse is performed in the following way:
        
        `this = this * b^-1`, where `b^-1` is the inverse of `b`.

        Arguments
        - b: the Quaternionf to divide this by

        Returns
        - this
        """
        ...


    def div(self, f: float, dest: "Quaternionf") -> "Quaternionf":
        ...


    def div(self, f: float) -> "Quaternionf":
        """
        Divide this quaternion by the given scalar.
        
        This method divides all the four components by the specified scalar.

        Arguments
        - f: the factor to divide all components by

        Returns
        - this
        """
        ...


    def conjugate(self) -> "Quaternionf":
        """
        Conjugate this quaternion.

        Returns
        - this
        """
        ...


    def conjugate(self, dest: "Quaternionf") -> "Quaternionf":
        ...


    def identity(self) -> "Quaternionf":
        """
        Set this quaternion to the identity.

        Returns
        - this
        """
        ...


    def rotateXYZ(self, angleX: float, angleY: float, angleZ: float) -> "Quaternionf":
        """
        Apply a rotation to `this` quaternion rotating the given radians about the cartesian base unit axes,
        called the euler angles using rotation sequence `XYZ`.
        
        This method is equivalent to calling: `rotateX(angleX).rotateY(angleY).rotateZ(angleZ)`
        
        If `Q` is `this` quaternion and `R` the quaternion representing the 
        specified rotation, then the new quaternion will be `Q * R`. So when transforming a
        vector `v` with the new quaternion by using `Q * R * v`, the
        rotation added by this method will be applied first!

        Arguments
        - angleX: the angle in radians to rotate about the x axis
        - angleY: the angle in radians to rotate about the y axis
        - angleZ: the angle in radians to rotate about the z axis

        Returns
        - this
        """
        ...


    def rotateXYZ(self, angleX: float, angleY: float, angleZ: float, dest: "Quaternionf") -> "Quaternionf":
        ...


    def rotateZYX(self, angleZ: float, angleY: float, angleX: float) -> "Quaternionf":
        """
        Apply a rotation to `this` quaternion rotating the given radians about the cartesian base unit axes,
        called the euler angles, using the rotation sequence `ZYX`.
        
        This method is equivalent to calling: `rotateZ(angleZ).rotateY(angleY).rotateX(angleX)`
        
        If `Q` is `this` quaternion and `R` the quaternion representing the 
        specified rotation, then the new quaternion will be `Q * R`. So when transforming a
        vector `v` with the new quaternion by using `Q * R * v`, the
        rotation added by this method will be applied first!

        Arguments
        - angleZ: the angle in radians to rotate about the z axis
        - angleY: the angle in radians to rotate about the y axis
        - angleX: the angle in radians to rotate about the x axis

        Returns
        - this
        """
        ...


    def rotateZYX(self, angleZ: float, angleY: float, angleX: float, dest: "Quaternionf") -> "Quaternionf":
        ...


    def rotateYXZ(self, angleY: float, angleX: float, angleZ: float) -> "Quaternionf":
        """
        Apply a rotation to `this` quaternion rotating the given radians about the cartesian base unit axes,
        called the euler angles, using the rotation sequence `YXZ`.
        
        This method is equivalent to calling: `rotateY(angleY).rotateX(angleX).rotateZ(angleZ)`
        
        If `Q` is `this` quaternion and `R` the quaternion representing the 
        specified rotation, then the new quaternion will be `Q * R`. So when transforming a
        vector `v` with the new quaternion by using `Q * R * v`, the
        rotation added by this method will be applied first!

        Arguments
        - angleY: the angle in radians to rotate about the y axis
        - angleX: the angle in radians to rotate about the x axis
        - angleZ: the angle in radians to rotate about the z axis

        Returns
        - this
        """
        ...


    def rotateYXZ(self, angleY: float, angleX: float, angleZ: float, dest: "Quaternionf") -> "Quaternionf":
        ...


    def getEulerAnglesXYZ(self, eulerAngles: "Vector3f") -> "Vector3f":
        ...


    def getEulerAnglesZYX(self, eulerAngles: "Vector3f") -> "Vector3f":
        ...


    def getEulerAnglesZXY(self, eulerAngles: "Vector3f") -> "Vector3f":
        ...


    def getEulerAnglesYXZ(self, eulerAngles: "Vector3f") -> "Vector3f":
        ...


    def lengthSquared(self) -> float:
        ...


    def rotationXYZ(self, angleX: float, angleY: float, angleZ: float) -> "Quaternionf":
        """
        Set this quaternion from the supplied euler angles (in radians) with rotation order XYZ.
        
        This method is equivalent to calling: `rotationX(angleX).rotateY(angleY).rotateZ(angleZ)`
        
        Reference: <a href="http://gamedev.stackexchange.com/questions/13436/glm-euler-angles-to-quaternion#answer-13446">this stackexchange answer</a>

        Arguments
        - angleX: the angle in radians to rotate about x
        - angleY: the angle in radians to rotate about y
        - angleZ: the angle in radians to rotate about z

        Returns
        - this
        """
        ...


    def rotationZYX(self, angleZ: float, angleY: float, angleX: float) -> "Quaternionf":
        """
        Set this quaternion from the supplied euler angles (in radians) with rotation order ZYX.
        
        This method is equivalent to calling: `rotationZ(angleZ).rotateY(angleY).rotateX(angleX)`
        
        Reference: <a href="http://gamedev.stackexchange.com/questions/13436/glm-euler-angles-to-quaternion#answer-13446">this stackexchange answer</a>

        Arguments
        - angleX: the angle in radians to rotate about x
        - angleY: the angle in radians to rotate about y
        - angleZ: the angle in radians to rotate about z

        Returns
        - this
        """
        ...


    def rotationYXZ(self, angleY: float, angleX: float, angleZ: float) -> "Quaternionf":
        """
        Set this quaternion from the supplied euler angles (in radians) with rotation order YXZ.
        
        This method is equivalent to calling: `rotationY(angleY).rotateX(angleX).rotateZ(angleZ)`
        
        Reference: <a href="https://en.wikipedia.org/wiki/Conversion_between_quaternions_and_Euler_angles">https://en.wikipedia.org</a>

        Arguments
        - angleY: the angle in radians to rotate about y
        - angleX: the angle in radians to rotate about x
        - angleZ: the angle in radians to rotate about z

        Returns
        - this
        """
        ...


    def slerp(self, target: "Quaternionfc", alpha: float) -> "Quaternionf":
        """
        Interpolate between `this` .normalize() unit quaternion and the specified
        `target` .normalize() unit quaternion using spherical linear interpolation using the specified interpolation factor `alpha`.
        
        This method resorts to non-spherical linear interpolation when the absolute dot product of `this` and `target` is
        below `1E-6f`.

        Arguments
        - target: the target of the interpolation, which should be reached with `alpha = 1.0`
        - alpha: the interpolation factor, within `[0..1]`

        Returns
        - this
        """
        ...


    def slerp(self, target: "Quaternionfc", alpha: float, dest: "Quaternionf") -> "Quaternionf":
        ...


    @staticmethod
    def slerp(qs: list["Quaternionf"], weights: list[float], dest: "Quaternionf") -> "Quaternionfc":
        """
        Interpolate between all of the quaternions given in `qs` via spherical linear interpolation using the specified interpolation factors `weights`,
        and store the result in `dest`.
        
        This method will interpolate between each two successive quaternions via .slerp(Quaternionfc, float) using their relative interpolation weights.
        
        This method resorts to non-spherical linear interpolation when the absolute dot product of any two interpolated quaternions is below `1E-6f`.
        
        Reference: <a href="http://gamedev.stackexchange.com/questions/62354/method-for-interpolation-between-3-quaternions#answer-62356">http://gamedev.stackexchange.com/</a>

        Arguments
        - qs: the quaternions to interpolate over
        - weights: the weights of each individual quaternion in `qs`
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def scale(self, factor: float) -> "Quaternionf":
        """
        Apply scaling to this quaternion, which results in any vector transformed by this quaternion to change
        its length by the given `factor`.

        Arguments
        - factor: the scaling factor

        Returns
        - this
        """
        ...


    def scale(self, factor: float, dest: "Quaternionf") -> "Quaternionf":
        ...


    def scaling(self, factor: float) -> "Quaternionf":
        """
        Set this quaternion to represent scaling, which results in a transformed vector to change
        its length by the given `factor`.

        Arguments
        - factor: the scaling factor

        Returns
        - this
        """
        ...


    def integrate(self, dt: float, vx: float, vy: float, vz: float) -> "Quaternionf":
        """
        Integrate the rotation given by the angular velocity `(vx, vy, vz)` around the x, y and z axis, respectively,
        with respect to the given elapsed time delta `dt` and add the differentiate rotation to the rotation represented by this quaternion.
        
        This method pre-multiplies the rotation given by `dt` and `(vx, vy, vz)` by `this`, so
        the angular velocities are always relative to the local coordinate system of the rotation represented by `this` quaternion.
        
        This method is equivalent to calling: `rotateLocal(dt * vx, dt * vy, dt * vz)`
        
        Reference: <a href="http://physicsforgames.blogspot.de/2010/02/quaternions.html">http://physicsforgames.blogspot.de/</a>

        Arguments
        - dt: the delta time
        - vx: the angular velocity around the x axis
        - vy: the angular velocity around the y axis
        - vz: the angular velocity around the z axis

        Returns
        - this
        """
        ...


    def integrate(self, dt: float, vx: float, vy: float, vz: float, dest: "Quaternionf") -> "Quaternionf":
        ...


    def nlerp(self, q: "Quaternionfc", factor: float) -> "Quaternionf":
        """
        Compute a linear (non-spherical) interpolation of `this` and the given quaternion `q`
        and store the result in `this`.

        Arguments
        - q: the other quaternion
        - factor: the interpolation factor. It is between 0.0 and 1.0

        Returns
        - this
        """
        ...


    def nlerp(self, q: "Quaternionfc", factor: float, dest: "Quaternionf") -> "Quaternionf":
        ...


    @staticmethod
    def nlerp(qs: list["Quaternionfc"], weights: list[float], dest: "Quaternionf") -> "Quaternionfc":
        """
        Interpolate between all of the quaternions given in `qs` via non-spherical linear interpolation using the
        specified interpolation factors `weights`, and store the result in `dest`.
        
        This method will interpolate between each two successive quaternions via .nlerp(Quaternionfc, float)
        using their relative interpolation weights.
        
        Reference: <a href="http://gamedev.stackexchange.com/questions/62354/method-for-interpolation-between-3-quaternions#answer-62356">http://gamedev.stackexchange.com/</a>

        Arguments
        - qs: the quaternions to interpolate over
        - weights: the weights of each individual quaternion in `qs`
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def nlerpIterative(self, q: "Quaternionfc", alpha: float, dotThreshold: float, dest: "Quaternionf") -> "Quaternionf":
        ...


    def nlerpIterative(self, q: "Quaternionfc", alpha: float, dotThreshold: float) -> "Quaternionf":
        """
        Compute linear (non-spherical) interpolations of `this` and the given quaternion `q`
        iteratively and store the result in `this`.
        
        This method performs a series of small-step nlerp interpolations to avoid doing a costly spherical linear interpolation, like
        .slerp(Quaternionfc, float, Quaternionf) slerp,
        by subdividing the rotation arc between `this` and `q` via non-spherical linear interpolations as long as
        the absolute dot product of `this` and `q` is greater than the given `dotThreshold` parameter.
        
        Thanks to `@theagentd` at <a href="http://www.java-gaming.org/">http://www.java-gaming.org/</a> for providing the code.

        Arguments
        - q: the other quaternion
        - alpha: the interpolation factor, between 0.0 and 1.0
        - dotThreshold: the threshold for the dot product of `this` and `q` above which this method performs another iteration
                 of a small-step linear interpolation

        Returns
        - this
        """
        ...


    @staticmethod
    def nlerpIterative(qs: list["Quaternionf"], weights: list[float], dotThreshold: float, dest: "Quaternionf") -> "Quaternionfc":
        """
        Interpolate between all of the quaternions given in `qs` via iterative non-spherical linear interpolation using the
        specified interpolation factors `weights`, and store the result in `dest`.
        
        This method will interpolate between each two successive quaternions via .nlerpIterative(Quaternionfc, float, float)
        using their relative interpolation weights.
        
        Reference: <a href="http://gamedev.stackexchange.com/questions/62354/method-for-interpolation-between-3-quaternions#answer-62356">http://gamedev.stackexchange.com/</a>

        Arguments
        - qs: the quaternions to interpolate over
        - weights: the weights of each individual quaternion in `qs`
        - dotThreshold: the threshold for the dot product of each two interpolated quaternions above which .nlerpIterative(Quaternionfc, float, float) performs another iteration
                 of a small-step linear interpolation
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def lookAlong(self, dir: "Vector3fc", up: "Vector3fc") -> "Quaternionf":
        """
        Apply a rotation to this quaternion that maps the given direction to the positive Z axis.
        
        Because there are multiple possibilities for such a rotation, this method will choose the one that ensures the given up direction to remain
        parallel to the plane spanned by the `up` and `dir` vectors. 
        
        If `Q` is `this` quaternion and `R` the quaternion representing the 
        specified rotation, then the new quaternion will be `Q * R`. So when transforming a
        vector `v` with the new quaternion by using `Q * R * v`, the
        rotation added by this method will be applied first!
        
        Reference: <a href="http://answers.unity3d.com/questions/467614/what-is-the-source-code-of-quaternionlookrotation.html">http://answers.unity3d.com</a>

        Arguments
        - dir: the direction to map to the positive Z axis
        - up: the vector which will be mapped to a vector parallel to the plane
                     spanned by the given `dir` and `up`

        Returns
        - this

        See
        - .lookAlong(float, float, float, float, float, float, Quaternionf)
        """
        ...


    def lookAlong(self, dir: "Vector3fc", up: "Vector3fc", dest: "Quaternionf") -> "Quaternionf":
        ...


    def lookAlong(self, dirX: float, dirY: float, dirZ: float, upX: float, upY: float, upZ: float) -> "Quaternionf":
        """
        Apply a rotation to this quaternion that maps the given direction to the positive Z axis.
        
        Because there are multiple possibilities for such a rotation, this method will choose the one that ensures the given up direction to remain
        parallel to the plane spanned by the `up` and `dir` vectors. 
        
        If `Q` is `this` quaternion and `R` the quaternion representing the 
        specified rotation, then the new quaternion will be `Q * R`. So when transforming a
        vector `v` with the new quaternion by using `Q * R * v`, the
        rotation added by this method will be applied first!
        
        Reference: <a href="http://answers.unity3d.com/questions/467614/what-is-the-source-code-of-quaternionlookrotation.html">http://answers.unity3d.com</a>

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
        - .lookAlong(float, float, float, float, float, float, Quaternionf)
        """
        ...


    def lookAlong(self, dirX: float, dirY: float, dirZ: float, upX: float, upY: float, upZ: float, dest: "Quaternionf") -> "Quaternionf":
        ...


    def rotationTo(self, fromDirX: float, fromDirY: float, fromDirZ: float, toDirX: float, toDirY: float, toDirZ: float) -> "Quaternionf":
        """
        Set `this` quaternion to a rotation that rotates the `fromDir` vector to point along `toDir`.
        
        Since there can be multiple possible rotations, this method chooses the one with the shortest arc.
        
        Reference: <a href="http://stackoverflow.com/questions/1171849/finding-quaternion-representing-the-rotation-from-one-vector-to-another#answer-1171995">stackoverflow.com</a>

        Arguments
        - fromDirX: the x-coordinate of the direction to rotate into the destination direction
        - fromDirY: the y-coordinate of the direction to rotate into the destination direction
        - fromDirZ: the z-coordinate of the direction to rotate into the destination direction
        - toDirX: the x-coordinate of the direction to rotate to
        - toDirY: the y-coordinate of the direction to rotate to
        - toDirZ: the z-coordinate of the direction to rotate to

        Returns
        - this
        """
        ...


    def rotationTo(self, fromDir: "Vector3fc", toDir: "Vector3fc") -> "Quaternionf":
        """
        Set `this` quaternion to a rotation that rotates the `fromDir` vector to point along `toDir`.
        
        Because there can be multiple possible rotations, this method chooses the one with the shortest arc.

        Arguments
        - fromDir: the starting direction
        - toDir: the destination direction

        Returns
        - this

        See
        - .rotationTo(float, float, float, float, float, float)
        """
        ...


    def rotateTo(self, fromDirX: float, fromDirY: float, fromDirZ: float, toDirX: float, toDirY: float, toDirZ: float, dest: "Quaternionf") -> "Quaternionf":
        ...


    def rotateTo(self, fromDirX: float, fromDirY: float, fromDirZ: float, toDirX: float, toDirY: float, toDirZ: float) -> "Quaternionf":
        """
        Apply a rotation to `this` that rotates the `fromDir` vector to point along `toDir`.
        
        Since there can be multiple possible rotations, this method chooses the one with the shortest arc.
        
        If `Q` is `this` quaternion and `R` the quaternion representing the 
        specified rotation, then the new quaternion will be `Q * R`. So when transforming a
        vector `v` with the new quaternion by using `Q * R * v`, the
        rotation added by this method will be applied first!

        Arguments
        - fromDirX: the x-coordinate of the direction to rotate into the destination direction
        - fromDirY: the y-coordinate of the direction to rotate into the destination direction
        - fromDirZ: the z-coordinate of the direction to rotate into the destination direction
        - toDirX: the x-coordinate of the direction to rotate to
        - toDirY: the y-coordinate of the direction to rotate to
        - toDirZ: the z-coordinate of the direction to rotate to

        Returns
        - this

        See
        - .rotateTo(float, float, float, float, float, float, Quaternionf)
        """
        ...


    def rotateTo(self, fromDir: "Vector3fc", toDir: "Vector3fc", dest: "Quaternionf") -> "Quaternionf":
        ...


    def rotateTo(self, fromDir: "Vector3fc", toDir: "Vector3fc") -> "Quaternionf":
        """
        Apply a rotation to `this` that rotates the `fromDir` vector to point along `toDir`.
        
        Because there can be multiple possible rotations, this method chooses the one with the shortest arc.
        
        If `Q` is `this` quaternion and `R` the quaternion representing the 
        specified rotation, then the new quaternion will be `Q * R`. So when transforming a
        vector `v` with the new quaternion by using `Q * R * v`, the
        rotation added by this method will be applied first!

        Arguments
        - fromDir: the starting direction
        - toDir: the destination direction

        Returns
        - this

        See
        - .rotateTo(float, float, float, float, float, float, Quaternionf)
        """
        ...


    def rotateX(self, angle: float) -> "Quaternionf":
        """
        Apply a rotation to `this` quaternion rotating the given radians about the x axis.
        
        If `Q` is `this` quaternion and `R` the quaternion representing the 
        specified rotation, then the new quaternion will be `Q * R`. So when transforming a
        vector `v` with the new quaternion by using `Q * R * v`, the
        rotation added by this method will be applied first!

        Arguments
        - angle: the angle in radians to rotate about the x axis

        Returns
        - this
        """
        ...


    def rotateX(self, angle: float, dest: "Quaternionf") -> "Quaternionf":
        ...


    def rotateY(self, angle: float) -> "Quaternionf":
        """
        Apply a rotation to `this` quaternion rotating the given radians about the y axis.
        
        If `Q` is `this` quaternion and `R` the quaternion representing the 
        specified rotation, then the new quaternion will be `Q * R`. So when transforming a
        vector `v` with the new quaternion by using `Q * R * v`, the
        rotation added by this method will be applied first!

        Arguments
        - angle: the angle in radians to rotate about the y axis

        Returns
        - this
        """
        ...


    def rotateY(self, angle: float, dest: "Quaternionf") -> "Quaternionf":
        ...


    def rotateZ(self, angle: float) -> "Quaternionf":
        """
        Apply a rotation to `this` quaternion rotating the given radians about the z axis.
        
        If `Q` is `this` quaternion and `R` the quaternion representing the 
        specified rotation, then the new quaternion will be `Q * R`. So when transforming a
        vector `v` with the new quaternion by using `Q * R * v`, the
        rotation added by this method will be applied first!

        Arguments
        - angle: the angle in radians to rotate about the z axis

        Returns
        - this
        """
        ...


    def rotateZ(self, angle: float, dest: "Quaternionf") -> "Quaternionf":
        ...


    def rotateLocalX(self, angle: float) -> "Quaternionf":
        """
        Apply a rotation to `this` quaternion rotating the given radians about the local x axis.
        
        If `Q` is `this` quaternion and `R` the quaternion representing the 
        specified rotation, then the new quaternion will be `R * Q`. So when transforming a
        vector `v` with the new quaternion by using `R * Q * v`, the
        rotation represented by `this` will be applied first!

        Arguments
        - angle: the angle in radians to rotate about the local x axis

        Returns
        - this
        """
        ...


    def rotateLocalX(self, angle: float, dest: "Quaternionf") -> "Quaternionf":
        ...


    def rotateLocalY(self, angle: float) -> "Quaternionf":
        """
        Apply a rotation to `this` quaternion rotating the given radians about the local y axis.
        
        If `Q` is `this` quaternion and `R` the quaternion representing the 
        specified rotation, then the new quaternion will be `R * Q`. So when transforming a
        vector `v` with the new quaternion by using `R * Q * v`, the
        rotation represented by `this` will be applied first!

        Arguments
        - angle: the angle in radians to rotate about the local y axis

        Returns
        - this
        """
        ...


    def rotateLocalY(self, angle: float, dest: "Quaternionf") -> "Quaternionf":
        ...


    def rotateLocalZ(self, angle: float) -> "Quaternionf":
        """
        Apply a rotation to `this` quaternion rotating the given radians about the local z axis.
        
        If `Q` is `this` quaternion and `R` the quaternion representing the 
        specified rotation, then the new quaternion will be `R * Q`. So when transforming a
        vector `v` with the new quaternion by using `R * Q * v`, the
        rotation represented by `this` will be applied first!

        Arguments
        - angle: the angle in radians to rotate about the local z axis

        Returns
        - this
        """
        ...


    def rotateLocalZ(self, angle: float, dest: "Quaternionf") -> "Quaternionf":
        ...


    def rotateAxis(self, angle: float, axisX: float, axisY: float, axisZ: float, dest: "Quaternionf") -> "Quaternionf":
        ...


    def rotateAxis(self, angle: float, axis: "Vector3fc", dest: "Quaternionf") -> "Quaternionf":
        ...


    def rotateAxis(self, angle: float, axis: "Vector3fc") -> "Quaternionf":
        """
        Apply a rotation to `this` quaternion rotating the given radians about the specified axis.
        
        If `Q` is `this` quaternion and `R` the quaternion representing the 
        specified rotation, then the new quaternion will be `Q * R`. So when transforming a
        vector `v` with the new quaternion by using `Q * R * v`, the
        rotation added by this method will be applied first!

        Arguments
        - angle: the angle in radians to rotate about the specified axis
        - axis: the rotation axis

        Returns
        - this

        See
        - .rotateAxis(float, float, float, float, Quaternionf)
        """
        ...


    def rotateAxis(self, angle: float, axisX: float, axisY: float, axisZ: float) -> "Quaternionf":
        """
        Apply a rotation to `this` quaternion rotating the given radians about the specified axis.
        
        If `Q` is `this` quaternion and `R` the quaternion representing the 
        specified rotation, then the new quaternion will be `Q * R`. So when transforming a
        vector `v` with the new quaternion by using `Q * R * v`, the
        rotation added by this method will be applied first!

        Arguments
        - angle: the angle in radians to rotate about the specified axis
        - axisX: the x coordinate of the rotation axis
        - axisY: the y coordinate of the rotation axis
        - axisZ: the z coordinate of the rotation axis

        Returns
        - this

        See
        - .rotateAxis(float, float, float, float, Quaternionf)
        """
        ...


    def toString(self) -> str:
        """
        Return a string representation of this quaternion.
        
        This method creates a new DecimalFormat on every invocation with the format string "`0.000E0;-`".

        Returns
        - the string representation
        """
        ...


    def toString(self, formatter: "NumberFormat") -> str:
        """
        Return a string representation of this quaternion by formatting the components with the given NumberFormat.

        Arguments
        - formatter: the NumberFormat used to format the quaternion components with

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


    def difference(self, other: "Quaternionf") -> "Quaternionf":
        """
        Compute the difference between `this` and the `other` quaternion
        and store the result in `this`.
        
        The difference is the rotation that has to be applied to get from
        `this` rotation to `other`. If `T` is `this`, `Q`
        is `other` and `D` is the computed difference, then the following equation holds:
        
        `T * D = Q`
        
        It is defined as: `D = T^-1 * Q`, where `T^-1` denotes the .invert() inverse of `T`.

        Arguments
        - other: the other quaternion

        Returns
        - this
        """
        ...


    def difference(self, other: "Quaternionfc", dest: "Quaternionf") -> "Quaternionf":
        ...


    def positiveX(self, dir: "Vector3f") -> "Vector3f":
        ...


    def normalizedPositiveX(self, dir: "Vector3f") -> "Vector3f":
        ...


    def positiveY(self, dir: "Vector3f") -> "Vector3f":
        ...


    def normalizedPositiveY(self, dir: "Vector3f") -> "Vector3f":
        ...


    def positiveZ(self, dir: "Vector3f") -> "Vector3f":
        ...


    def normalizedPositiveZ(self, dir: "Vector3f") -> "Vector3f":
        ...


    def conjugateBy(self, q: "Quaternionfc") -> "Quaternionf":
        """
        Conjugate `this` by the given quaternion `q` by computing `q * this * q^-1`.

        Arguments
        - q: the Quaternionfc to conjugate `this` by

        Returns
        - this
        """
        ...


    def conjugateBy(self, q: "Quaternionfc", dest: "Quaternionf") -> "Quaternionf":
        """
        Conjugate `this` by the given quaternion `q` by computing `q * this * q^-1`
        and store the result into `dest`.

        Arguments
        - q: the Quaternionfc to conjugate `this` by
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def isFinite(self) -> bool:
        ...


    def equals(self, q: "Quaternionfc", delta: float) -> bool:
        ...


    def equals(self, x: float, y: float, z: float, w: float) -> bool:
        ...


    def clone(self) -> "Object":
        ...
