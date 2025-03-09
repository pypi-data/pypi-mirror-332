"""
Python module generated from Java source file org.joml.Quaterniondc

Java source file obtained from artifact joml version 1.10.5

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util import *
from org.joml import *
from typing import Any, Callable, Iterable, Tuple


class Quaterniondc:
    """
    Interface to a read-only view of a quaternion of double-precision floats.

    Author(s)
    - Kai Burjack
    """

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


    def normalize(self, dest: "Quaterniond") -> "Quaterniond":
        """
        Normalize this quaternion and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def add(self, x: float, y: float, z: float, w: float, dest: "Quaterniond") -> "Quaterniond":
        """
        Add the quaternion `(x, y, z, w)` to this quaternion and store the result in `dest`.

        Arguments
        - x: the x component of the vector part
        - y: the y component of the vector part
        - z: the z component of the vector part
        - w: the real/scalar component
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def add(self, q2: "Quaterniondc", dest: "Quaterniond") -> "Quaterniond":
        """
        Add `q2` to this quaternion and store the result in `dest`.

        Arguments
        - q2: the quaternion to add to this
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def dot(self, otherQuat: "Quaterniondc") -> float:
        """
        Return the dot product of this Quaterniond and `otherQuat`.

        Arguments
        - otherQuat: the other quaternion

        Returns
        - the dot product
        """
        ...


    def angle(self) -> float:
        """
        Return the angle in radians represented by this normalized quaternion rotation.
        
        This quaternion must be .normalize(Quaterniond) normalized.

        Returns
        - the angle in radians
        """
        ...


    def get(self, dest: "Matrix3d") -> "Matrix3d":
        """
        Set the given destination matrix to the rotation represented by `this`.

        Arguments
        - dest: the matrix to write the rotation into

        Returns
        - the passed in destination

        See
        - Matrix3d.set(Quaterniondc)
        """
        ...


    def get(self, dest: "Matrix3f") -> "Matrix3f":
        """
        Set the given destination matrix to the rotation represented by `this`.

        Arguments
        - dest: the matrix to write the rotation into

        Returns
        - the passed in destination

        See
        - Matrix3f.set(Quaterniondc)
        """
        ...


    def get(self, dest: "Matrix4d") -> "Matrix4d":
        """
        Set the given destination matrix to the rotation represented by `this`.

        Arguments
        - dest: the matrix to write the rotation into

        Returns
        - the passed in destination

        See
        - Matrix4d.set(Quaterniondc)
        """
        ...


    def get(self, dest: "Matrix4f") -> "Matrix4f":
        """
        Set the given destination matrix to the rotation represented by `this`.

        Arguments
        - dest: the matrix to write the rotation into

        Returns
        - the passed in destination

        See
        - Matrix4f.set(Quaterniondc)
        """
        ...


    def get(self, dest: "AxisAngle4f") -> "AxisAngle4f":
        """
        Set the given AxisAngle4f to represent the rotation of
        `this` quaternion.

        Arguments
        - dest: the AxisAngle4f to set

        Returns
        - the passed in destination
        """
        ...


    def get(self, dest: "AxisAngle4d") -> "AxisAngle4d":
        """
        Set the given AxisAngle4d to represent the rotation of
        `this` quaternion.

        Arguments
        - dest: the AxisAngle4d to set

        Returns
        - the passed in destination
        """
        ...


    def get(self, dest: "Quaterniond") -> "Quaterniond":
        """
        Set the given Quaterniond to the values of `this`.

        Arguments
        - dest: the Quaterniond to set

        Returns
        - the passed in destination
        """
        ...


    def get(self, dest: "Quaternionf") -> "Quaternionf":
        """
        Set the given Quaternionf to the values of `this`.

        Arguments
        - dest: the Quaternionf to set

        Returns
        - the passed in destination
        """
        ...


    def mul(self, q: "Quaterniondc", dest: "Quaterniond") -> "Quaterniond":
        """
        Multiply this quaternion by `q` and store the result in `dest`.
        
        If `T` is `this` and `Q` is the given
        quaternion, then the resulting quaternion `R` is:
        
        `R = T * Q`
        
        So, this method uses post-multiplication like the matrix classes, resulting in a
        vector to be transformed by `Q` first, and then by `T`.

        Arguments
        - q: the quaternion to multiply `this` by
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mul(self, qx: float, qy: float, qz: float, qw: float, dest: "Quaterniond") -> "Quaterniond":
        """
        Multiply this quaternion by the quaternion represented via `(qx, qy, qz, qw)` and store the result in `dest`.
        
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
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def mul(self, f: float, dest: "Quaterniond") -> "Quaterniond":
        """
        Multiply this quaternion by the given scalar and store the result in `dest`.
        
        This method multiplies all of the four components by the specified scalar.

        Arguments
        - f: the factor to multiply all components by
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def premul(self, q: "Quaterniondc", dest: "Quaterniond") -> "Quaterniond":
        """
        Pre-multiply this quaternion by `q` and store the result in `dest`.
        
        If `T` is `this` and `Q` is the given quaternion, then the resulting quaternion `R` is:
        
        `R = Q * T`
        
        So, this method uses pre-multiplication, resulting in a vector to be transformed by `T` first, and then by `Q`.

        Arguments
        - q: the quaternion to pre-multiply `this` by
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def premul(self, qx: float, qy: float, qz: float, qw: float, dest: "Quaterniond") -> "Quaterniond":
        """
        Pre-multiply this quaternion by the quaternion represented via `(qx, qy, qz, qw)` and store the result in `dest`.
        
        If `T` is `this` and `Q` is the given quaternion, then the resulting quaternion `R` is:
        
        `R = Q * T`
        
        So, this method uses pre-multiplication, resulting in a vector to be transformed by `T` first, and then by `Q`.

        Arguments
        - qx: the x component of the quaternion to multiply `this` by
        - qy: the y component of the quaternion to multiply `this` by
        - qz: the z component of the quaternion to multiply `this` by
        - qw: the w component of the quaternion to multiply `this` by
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def transform(self, vec: "Vector3d") -> "Vector3d":
        """
        Transform the given vector by this quaternion.
        
        This will apply the rotation described by this quaternion to the given vector.

        Arguments
        - vec: the vector to transform

        Returns
        - vec
        """
        ...


    def transformInverse(self, vec: "Vector3d") -> "Vector3d":
        """
        Transform the given vector by the inverse of this quaternion.
        
        This will apply the rotation described by this quaternion to the given vector.

        Arguments
        - vec: the vector to transform

        Returns
        - vec
        """
        ...


    def transformUnit(self, vec: "Vector3d") -> "Vector3d":
        """
        Transform the given vector by this unit quaternion.
        
        This will apply the rotation described by this quaternion to the given vector.
        
        This method is only applicable when `this` is a unit quaternion.

        Arguments
        - vec: the vector to transform

        Returns
        - vec
        """
        ...


    def transformInverseUnit(self, vec: "Vector3d") -> "Vector3d":
        """
        Transform the given vector by the inverse of this unit quaternion.
        
        This will apply the rotation described by this quaternion to the given vector.
        
        This method is only applicable when `this` is a unit quaternion.

        Arguments
        - vec: the vector to transform

        Returns
        - vec
        """
        ...


    def transformPositiveX(self, dest: "Vector3d") -> "Vector3d":
        """
        Transform the vector `(1, 0, 0)` by this quaternion.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def transformPositiveX(self, dest: "Vector4d") -> "Vector4d":
        """
        Transform the vector `(1, 0, 0)` by this quaternion.
        
        Only the first three components of the given 4D vector are modified.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def transformUnitPositiveX(self, dest: "Vector3d") -> "Vector3d":
        """
        Transform the vector `(1, 0, 0)` by this unit quaternion.
        
        This method is only applicable when `this` is a unit quaternion.
        
        Reference: <a href="https://de.mathworks.com/help/aerotbx/ug/quatrotate.html?requestedDomain=True">https://de.mathworks.com/</a>

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def transformUnitPositiveX(self, dest: "Vector4d") -> "Vector4d":
        """
        Transform the vector `(1, 0, 0)` by this unit quaternion.
        
        Only the first three components of the given 4D vector are modified.
        
        This method is only applicable when `this` is a unit quaternion.
        
        Reference: <a href="https://de.mathworks.com/help/aerotbx/ug/quatrotate.html?requestedDomain=True">https://de.mathworks.com/</a>

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def transformPositiveY(self, dest: "Vector3d") -> "Vector3d":
        """
        Transform the vector `(0, 1, 0)` by this quaternion.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def transformPositiveY(self, dest: "Vector4d") -> "Vector4d":
        """
        Transform the vector `(0, 1, 0)` by this quaternion.
        
        Only the first three components of the given 4D vector are modified.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def transformUnitPositiveY(self, dest: "Vector3d") -> "Vector3d":
        """
        Transform the vector `(0, 1, 0)` by this unit quaternion.
        
        This method is only applicable when `this` is a unit quaternion.
        
        Reference: <a href="https://de.mathworks.com/help/aerotbx/ug/quatrotate.html?requestedDomain=True">https://de.mathworks.com/</a>

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def transformUnitPositiveY(self, dest: "Vector4d") -> "Vector4d":
        """
        Transform the vector `(0, 1, 0)` by this unit quaternion.
        
        Only the first three components of the given 4D vector are modified.
        
        This method is only applicable when `this` is a unit quaternion.
        
        Reference: <a href="https://de.mathworks.com/help/aerotbx/ug/quatrotate.html?requestedDomain=True">https://de.mathworks.com/</a>

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def transformPositiveZ(self, dest: "Vector3d") -> "Vector3d":
        """
        Transform the vector `(0, 0, 1)` by this quaternion.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def transformPositiveZ(self, dest: "Vector4d") -> "Vector4d":
        """
        Transform the vector `(0, 0, 1)` by this quaternion.
        
        Only the first three components of the given 4D vector are modified.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def transformUnitPositiveZ(self, dest: "Vector3d") -> "Vector3d":
        """
        Transform the vector `(0, 0, 1)` by this unit quaternion.
        
        This method is only applicable when `this` is a unit quaternion.
        
        Reference: <a href="https://de.mathworks.com/help/aerotbx/ug/quatrotate.html?requestedDomain=True">https://de.mathworks.com/</a>

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def transformUnitPositiveZ(self, dest: "Vector4d") -> "Vector4d":
        """
        Transform the vector `(0, 0, 1)` by this unit quaternion.
        
        Only the first three components of the given 4D vector are modified.
        
        This method is only applicable when `this` is a unit quaternion.
        
        Reference: <a href="https://de.mathworks.com/help/aerotbx/ug/quatrotate.html?requestedDomain=True">https://de.mathworks.com/</a>

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def transform(self, vec: "Vector4d") -> "Vector4d":
        """
        Transform the given vector by this quaternion.
        
        This will apply the rotation described by this quaternion to the given vector.
        
        Only the first three components of the given 4D vector are being used and modified.

        Arguments
        - vec: the vector to transform

        Returns
        - vec
        """
        ...


    def transformInverse(self, vec: "Vector4d") -> "Vector4d":
        """
        Transform the given vector by the inverse of this quaternion.
        
        This will apply the rotation described by this quaternion to the given vector.
        
        Only the first three components of the given 4D vector are being used and modified.

        Arguments
        - vec: the vector to transform

        Returns
        - vec
        """
        ...


    def transform(self, vec: "Vector3dc", dest: "Vector3d") -> "Vector3d":
        """
        Transform the given vector by this quaternion and store the result in `dest`.
        
        This will apply the rotation described by this quaternion to the given vector.

        Arguments
        - vec: the vector to transform
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def transformInverse(self, vec: "Vector3dc", dest: "Vector3d") -> "Vector3d":
        """
        Transform the given vector by the inverse of this quaternion and store the result in `dest`.
        
        This will apply the rotation described by this quaternion to the given vector.

        Arguments
        - vec: the vector to transform
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def transform(self, x: float, y: float, z: float, dest: "Vector3d") -> "Vector3d":
        """
        Transform the given vector `(x, y, z)` by this quaternion and store the result in `dest`.
        
        This will apply the rotation described by this quaternion to the given vector.

        Arguments
        - x: the x coordinate of the vector to transform
        - y: the y coordinate of the vector to transform
        - z: the z coordinate of the vector to transform
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def transformInverse(self, x: float, y: float, z: float, dest: "Vector3d") -> "Vector3d":
        """
        Transform the given vector `(x, y, z)` by the inverse of
        this quaternion and store the result in `dest`.
        
        This will apply the rotation described by this quaternion to the given vector.

        Arguments
        - x: the x coordinate of the vector to transform
        - y: the y coordinate of the vector to transform
        - z: the z coordinate of the vector to transform
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def transform(self, vec: "Vector4dc", dest: "Vector4d") -> "Vector4d":
        """
        Transform the given vector by this quaternion and store the result in `dest`.
        
        This will apply the rotation described by this quaternion to the given vector.
        
        Only the first three components of the given 4D vector are being used and set on the destination.

        Arguments
        - vec: the vector to transform
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def transformInverse(self, vec: "Vector4dc", dest: "Vector4d") -> "Vector4d":
        """
        Transform the given vector by the inverse of this quaternion and store the result in `dest`.
        
        This will apply the rotation described by this quaternion to the given vector.
        
        Only the first three components of the given 4D vector are being used and set on the destination.

        Arguments
        - vec: the vector to transform
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def transform(self, x: float, y: float, z: float, dest: "Vector4d") -> "Vector4d":
        """
        Transform the given vector `(x, y, z)` by this quaternion and store the result in `dest`.
        
        This will apply the rotation described by this quaternion to the given vector.

        Arguments
        - x: the x coordinate of the vector to transform
        - y: the y coordinate of the vector to transform
        - z: the z coordinate of the vector to transform
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def transformInverse(self, x: float, y: float, z: float, dest: "Vector4d") -> "Vector4d":
        """
        Transform the given vector `(x, y, z)` by the inverse of
        this quaternion and store the result in `dest`.
        
        This will apply the rotation described by this quaternion to the given vector.

        Arguments
        - x: the x coordinate of the vector to transform
        - y: the y coordinate of the vector to transform
        - z: the z coordinate of the vector to transform
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def transform(self, vec: "Vector3f") -> "Vector3f":
        """
        Transform the given vector by this quaternion.
        
        This will apply the rotation described by this quaternion to the given vector.

        Arguments
        - vec: the vector to transform

        Returns
        - vec
        """
        ...


    def transformInverse(self, vec: "Vector3f") -> "Vector3f":
        """
        Transform the given vector by the inverse of this quaternion.
        
        This will apply the rotation described by this quaternion to the given vector.

        Arguments
        - vec: the vector to transform

        Returns
        - vec
        """
        ...


    def transformUnit(self, vec: "Vector4d") -> "Vector4d":
        """
        Transform the given vector by this unit quaternion.
        
        This will apply the rotation described by this quaternion to the given vector.
        
        Only the first three components of the given 4D vector are being used and modified.
        
        This method is only applicable when `this` is a unit quaternion.

        Arguments
        - vec: the vector to transform

        Returns
        - vec
        """
        ...


    def transformInverseUnit(self, vec: "Vector4d") -> "Vector4d":
        """
        Transform the given vector by the inverse of this unit quaternion.
        
        This will apply the rotation described by this quaternion to the given vector.
        
        Only the first three components of the given 4D vector are being used and modified.
        
        This method is only applicable when `this` is a unit quaternion.

        Arguments
        - vec: the vector to transform

        Returns
        - vec
        """
        ...


    def transformUnit(self, vec: "Vector3dc", dest: "Vector3d") -> "Vector3d":
        """
        Transform the given vector by this unit quaternion and store the result in `dest`.
        
        This will apply the rotation described by this quaternion to the given vector.
        
        This method is only applicable when `this` is a unit quaternion.

        Arguments
        - vec: the vector to transform
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def transformInverseUnit(self, vec: "Vector3dc", dest: "Vector3d") -> "Vector3d":
        """
        Transform the given vector by the inverse of this unit quaternion and store the result in `dest`.
        
        This will apply the rotation described by this quaternion to the given vector.
        
        This method is only applicable when `this` is a unit quaternion.

        Arguments
        - vec: the vector to transform
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def transformUnit(self, x: float, y: float, z: float, dest: "Vector3d") -> "Vector3d":
        """
        Transform the given vector `(x, y, z)` by this unit quaternion and store the result in `dest`.
        
        This will apply the rotation described by this quaternion to the given vector.
        
        This method is only applicable when `this` is a unit quaternion.

        Arguments
        - x: the x coordinate of the vector to transform
        - y: the y coordinate of the vector to transform
        - z: the z coordinate of the vector to transform
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def transformInverseUnit(self, x: float, y: float, z: float, dest: "Vector3d") -> "Vector3d":
        """
        Transform the given vector `(x, y, z)` by the inverse of
        this unit quaternion and store the result in `dest`.
        
        This will apply the rotation described by this quaternion to the given vector.
        
        This method is only applicable when `this` is a unit quaternion.

        Arguments
        - x: the x coordinate of the vector to transform
        - y: the y coordinate of the vector to transform
        - z: the z coordinate of the vector to transform
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def transformUnit(self, vec: "Vector4dc", dest: "Vector4d") -> "Vector4d":
        """
        Transform the given vector by this unit quaternion and store the result in `dest`.
        
        This will apply the rotation described by this quaternion to the given vector.
        
        Only the first three components of the given 4D vector are being used and set on the destination.
        
        This method is only applicable when `this` is a unit quaternion.

        Arguments
        - vec: the vector to transform
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def transformInverseUnit(self, vec: "Vector4dc", dest: "Vector4d") -> "Vector4d":
        """
        Transform the given vector by the inverse of this unit quaternion and store the result in `dest`.
        
        This will apply the rotation described by this quaternion to the given vector.
        
        Only the first three components of the given 4D vector are being used and set on the destination.
        
        This method is only applicable when `this` is a unit quaternion.

        Arguments
        - vec: the vector to transform
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def transformUnit(self, x: float, y: float, z: float, dest: "Vector4d") -> "Vector4d":
        """
        Transform the given vector `(x, y, z)` by this unit quaternion and store the result in `dest`.
        
        This will apply the rotation described by this quaternion to the given vector.
        
        This method is only applicable when `this` is a unit quaternion.

        Arguments
        - x: the x coordinate of the vector to transform
        - y: the y coordinate of the vector to transform
        - z: the z coordinate of the vector to transform
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def transformInverseUnit(self, x: float, y: float, z: float, dest: "Vector4d") -> "Vector4d":
        """
        Transform the given vector `(x, y, z)` by the inverse of
        this unit quaternion and store the result in `dest`.
        
        This will apply the rotation described by this quaternion to the given vector.
        
        This method is only applicable when `this` is a unit quaternion.

        Arguments
        - x: the x coordinate of the vector to transform
        - y: the y coordinate of the vector to transform
        - z: the z coordinate of the vector to transform
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def transformUnit(self, vec: "Vector3f") -> "Vector3f":
        """
        Transform the given vector by this unit quaternion.
        
        This will apply the rotation described by this quaternion to the given vector.
        
        This method is only applicable when `this` is a unit quaternion.

        Arguments
        - vec: the vector to transform

        Returns
        - vec
        """
        ...


    def transformInverseUnit(self, vec: "Vector3f") -> "Vector3f":
        """
        Transform the given vector by the inverse of this unit quaternion.
        
        This will apply the rotation described by this quaternion to the given vector.
        
        This method is only applicable when `this` is a unit quaternion.

        Arguments
        - vec: the vector to transform

        Returns
        - vec
        """
        ...


    def transformPositiveX(self, dest: "Vector3f") -> "Vector3f":
        """
        Transform the vector `(1, 0, 0)` by this quaternion.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def transformPositiveX(self, dest: "Vector4f") -> "Vector4f":
        """
        Transform the vector `(1, 0, 0)` by this quaternion.
        
        Only the first three components of the given 4D vector are modified.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def transformUnitPositiveX(self, dest: "Vector3f") -> "Vector3f":
        """
        Transform the vector `(1, 0, 0)` by this unit quaternion.
        
        This method is only applicable when `this` is a unit quaternion.
        
        Reference: <a href="https://de.mathworks.com/help/aerotbx/ug/quatrotate.html?requestedDomain=True">https://de.mathworks.com/</a>

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def transformUnitPositiveX(self, dest: "Vector4f") -> "Vector4f":
        """
        Transform the vector `(1, 0, 0)` by this unit quaternion.
        
        Only the first three components of the given 4D vector are modified.
        
        This method is only applicable when `this` is a unit quaternion.
        
        Reference: <a href="https://de.mathworks.com/help/aerotbx/ug/quatrotate.html?requestedDomain=True">https://de.mathworks.com/</a>

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def transformPositiveY(self, dest: "Vector3f") -> "Vector3f":
        """
        Transform the vector `(0, 1, 0)` by this quaternion.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def transformPositiveY(self, dest: "Vector4f") -> "Vector4f":
        """
        Transform the vector `(0, 1, 0)` by this quaternion.
        
        Only the first three components of the given 4D vector are modified.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def transformUnitPositiveY(self, dest: "Vector3f") -> "Vector3f":
        """
        Transform the vector `(0, 1, 0)` by this unit quaternion.
        
        This method is only applicable when `this` is a unit quaternion.
        
        Reference: <a href="https://de.mathworks.com/help/aerotbx/ug/quatrotate.html?requestedDomain=True">https://de.mathworks.com/</a>

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def transformUnitPositiveY(self, dest: "Vector4f") -> "Vector4f":
        """
        Transform the vector `(0, 1, 0)` by this unit quaternion.
        
        Only the first three components of the given 4D vector are modified.
        
        This method is only applicable when `this` is a unit quaternion.
        
        Reference: <a href="https://de.mathworks.com/help/aerotbx/ug/quatrotate.html?requestedDomain=True">https://de.mathworks.com/</a>

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def transformPositiveZ(self, dest: "Vector3f") -> "Vector3f":
        """
        Transform the vector `(0, 0, 1)` by this quaternion.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def transformPositiveZ(self, dest: "Vector4f") -> "Vector4f":
        """
        Transform the vector `(0, 0, 1)` by this quaternion.
        
        Only the first three components of the given 4D vector are modified.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def transformUnitPositiveZ(self, dest: "Vector3f") -> "Vector3f":
        """
        Transform the vector `(0, 0, 1)` by this unit quaternion.
        
        This method is only applicable when `this` is a unit quaternion.
        
        Reference: <a href="https://de.mathworks.com/help/aerotbx/ug/quatrotate.html?requestedDomain=True">https://de.mathworks.com/</a>

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def transformUnitPositiveZ(self, dest: "Vector4f") -> "Vector4f":
        """
        Transform the vector `(0, 0, 1)` by this unit quaternion.
        
        Only the first three components of the given 4D vector are modified.
        
        This method is only applicable when `this` is a unit quaternion.
        
        Reference: <a href="https://de.mathworks.com/help/aerotbx/ug/quatrotate.html?requestedDomain=True">https://de.mathworks.com/</a>

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def transform(self, vec: "Vector4f") -> "Vector4f":
        """
        Transform the given vector by this quaternion.
        
        This will apply the rotation described by this quaternion to the given vector.
        
        Only the first three components of the given 4D vector are being used and modified.

        Arguments
        - vec: the vector to transform

        Returns
        - vec
        """
        ...


    def transformInverse(self, vec: "Vector4f") -> "Vector4f":
        """
        Transform the given vector by the inverse of this quaternion.
        
        This will apply the rotation described by this quaternion to the given vector.
        
        Only the first three components of the given 4D vector are being used and modified.

        Arguments
        - vec: the vector to transform

        Returns
        - vec
        """
        ...


    def transform(self, vec: "Vector3fc", dest: "Vector3f") -> "Vector3f":
        """
        Transform the given vector by this quaternion and store the result in `dest`.
        
        This will apply the rotation described by this quaternion to the given vector.

        Arguments
        - vec: the vector to transform
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def transformInverse(self, vec: "Vector3fc", dest: "Vector3f") -> "Vector3f":
        """
        Transform the given vector by the inverse of this quaternion and store the result in `dest`.
        
        This will apply the rotation described by this quaternion to the given vector.

        Arguments
        - vec: the vector to transform
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def transform(self, x: float, y: float, z: float, dest: "Vector3f") -> "Vector3f":
        """
        Transform the given vector `(x, y, z)` by this quaternion and store the result in `dest`.
        
        This will apply the rotation described by this quaternion to the given vector.

        Arguments
        - x: the x coordinate of the vector to transform
        - y: the y coordinate of the vector to transform
        - z: the z coordinate of the vector to transform
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def transformInverse(self, x: float, y: float, z: float, dest: "Vector3f") -> "Vector3f":
        """
        Transform the given vector `(x, y, z)` by the inverse of
        this quaternion and store the result in `dest`.
        
        This will apply the rotation described by this quaternion to the given vector.

        Arguments
        - x: the x coordinate of the vector to transform
        - y: the y coordinate of the vector to transform
        - z: the z coordinate of the vector to transform
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def transform(self, vec: "Vector4fc", dest: "Vector4f") -> "Vector4f":
        """
        Transform the given vector by this quaternion and store the result in `dest`.
        
        This will apply the rotation described by this quaternion to the given vector.
        
        Only the first three components of the given 4D vector are being used and set on the destination.

        Arguments
        - vec: the vector to transform
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def transformInverse(self, vec: "Vector4fc", dest: "Vector4f") -> "Vector4f":
        """
        Transform the given vector by the inverse of this quaternion and store the result in `dest`.
        
        This will apply the rotation described by this quaternion to the given vector.
        
        Only the first three components of the given 4D vector are being used and set on the destination.

        Arguments
        - vec: the vector to transform
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def transform(self, x: float, y: float, z: float, dest: "Vector4f") -> "Vector4f":
        """
        Transform the given vector `(x, y, z)` by this quaternion and store the result in `dest`.
        
        This will apply the rotation described by this quaternion to the given vector.

        Arguments
        - x: the x coordinate of the vector to transform
        - y: the y coordinate of the vector to transform
        - z: the z coordinate of the vector to transform
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def transformInverse(self, x: float, y: float, z: float, dest: "Vector4f") -> "Vector4f":
        """
        Transform the given vector `(x, y, z)` by the inverse of
        this quaternion and store the result in `dest`.
        
        This will apply the rotation described by this quaternion to the given vector.

        Arguments
        - x: the x coordinate of the vector to transform
        - y: the y coordinate of the vector to transform
        - z: the z coordinate of the vector to transform
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def transformUnit(self, vec: "Vector4f") -> "Vector4f":
        """
        Transform the given vector by this unit quaternion.
        
        This will apply the rotation described by this quaternion to the given vector.
        
        Only the first three components of the given 4D vector are being used and modified.
        
        This method is only applicable when `this` is a unit quaternion.

        Arguments
        - vec: the vector to transform

        Returns
        - vec
        """
        ...


    def transformInverseUnit(self, vec: "Vector4f") -> "Vector4f":
        """
        Transform the given vector by the inverse of this unit quaternion.
        
        This will apply the rotation described by this quaternion to the given vector.
        
        Only the first three components of the given 4D vector are being used and modified.
        
        This method is only applicable when `this` is a unit quaternion.

        Arguments
        - vec: the vector to transform

        Returns
        - vec
        """
        ...


    def transformUnit(self, vec: "Vector3fc", dest: "Vector3f") -> "Vector3f":
        """
        Transform the given vector by this unit quaternion and store the result in `dest`.
        
        This will apply the rotation described by this quaternion to the given vector.
        
        This method is only applicable when `this` is a unit quaternion.

        Arguments
        - vec: the vector to transform
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def transformInverseUnit(self, vec: "Vector3fc", dest: "Vector3f") -> "Vector3f":
        """
        Transform the given vector by the inverse of this unit quaternion and store the result in `dest`.
        
        This will apply the rotation described by this quaternion to the given vector.
        
        This method is only applicable when `this` is a unit quaternion.

        Arguments
        - vec: the vector to transform
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def transformUnit(self, x: float, y: float, z: float, dest: "Vector3f") -> "Vector3f":
        """
        Transform the given vector `(x, y, z)` by this unit quaternion and store the result in `dest`.
        
        This will apply the rotation described by this quaternion to the given vector.
        
        This method is only applicable when `this` is a unit quaternion.

        Arguments
        - x: the x coordinate of the vector to transform
        - y: the y coordinate of the vector to transform
        - z: the z coordinate of the vector to transform
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def transformInverseUnit(self, x: float, y: float, z: float, dest: "Vector3f") -> "Vector3f":
        """
        Transform the given vector `(x, y, z)` by the inverse of
        this unit quaternion and store the result in `dest`.
        
        This will apply the rotation described by this quaternion to the given vector.
        
        This method is only applicable when `this` is a unit quaternion.

        Arguments
        - x: the x coordinate of the vector to transform
        - y: the y coordinate of the vector to transform
        - z: the z coordinate of the vector to transform
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def transformUnit(self, vec: "Vector4fc", dest: "Vector4f") -> "Vector4f":
        """
        Transform the given vector by this unit quaternion and store the result in `dest`.
        
        This will apply the rotation described by this quaternion to the given vector.
        
        Only the first three components of the given 4D vector are being used and set on the destination.
        
        This method is only applicable when `this` is a unit quaternion.

        Arguments
        - vec: the vector to transform
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def transformInverseUnit(self, vec: "Vector4fc", dest: "Vector4f") -> "Vector4f":
        """
        Transform the given vector by the inverse of this unit quaternion and store the result in `dest`.
        
        This will apply the rotation described by this quaternion to the given vector.
        
        Only the first three components of the given 4D vector are being used and set on the destination.
        
        This method is only applicable when `this` is a unit quaternion.

        Arguments
        - vec: the vector to transform
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def transformUnit(self, x: float, y: float, z: float, dest: "Vector4f") -> "Vector4f":
        """
        Transform the given vector `(x, y, z)` by this unit quaternion and store the result in `dest`.
        
        This will apply the rotation described by this quaternion to the given vector.
        
        This method is only applicable when `this` is a unit quaternion.

        Arguments
        - x: the x coordinate of the vector to transform
        - y: the y coordinate of the vector to transform
        - z: the z coordinate of the vector to transform
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def transformInverseUnit(self, x: float, y: float, z: float, dest: "Vector4f") -> "Vector4f":
        """
        Transform the given vector `(x, y, z)` by the inverse of
        this unit quaternion and store the result in `dest`.
        
        This will apply the rotation described by this quaternion to the given vector.
        
        This method is only applicable when `this` is a unit quaternion.

        Arguments
        - x: the x coordinate of the vector to transform
        - y: the y coordinate of the vector to transform
        - z: the z coordinate of the vector to transform
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def invert(self, dest: "Quaterniond") -> "Quaterniond":
        """
        Invert this quaternion and store the .normalize(Quaterniond) normalized result in `dest`.
        
        If this quaternion is already normalized, then .conjugate(Quaterniond) should be used instead.

        Arguments
        - dest: will hold the result

        Returns
        - dest

        See
        - .conjugate(Quaterniond)
        """
        ...


    def div(self, b: "Quaterniondc", dest: "Quaterniond") -> "Quaterniond":
        """
        Divide `this` quaternion by `b` and store the result in `dest`.
        
        The division expressed using the inverse is performed in the following way:
        
        `dest = this * b^-1`, where `b^-1` is the inverse of `b`.

        Arguments
        - b: the Quaterniondc to divide this by
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def conjugate(self, dest: "Quaterniond") -> "Quaterniond":
        """
        Conjugate this quaternion and store the result in `dest`.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def lengthSquared(self) -> float:
        """
        Return the square of the length of this quaternion.

        Returns
        - the length
        """
        ...


    def slerp(self, target: "Quaterniondc", alpha: float, dest: "Quaterniond") -> "Quaterniond":
        """
        Interpolate between `this` .normalize(Quaterniond) unit quaternion and the specified
        `target` .normalize(Quaterniond) unit quaternion using spherical linear interpolation using the specified interpolation factor `alpha`,
        and store the result in `dest`.
        
        This method resorts to non-spherical linear interpolation when the absolute dot product between `this` and `target` is
        below `1E-6`.
        
        Reference: <a href="http://fabiensanglard.net/doom3_documentation/37725-293747_293747.pdf">http://fabiensanglard.net</a>

        Arguments
        - target: the target of the interpolation, which should be reached with `alpha = 1.0`
        - alpha: the interpolation factor, within `[0..1]`
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def scale(self, factor: float, dest: "Quaterniond") -> "Quaterniond":
        """
        Apply scaling to this quaternion, which results in any vector transformed by the quaternion to change
        its length by the given `factor`, and store the result in `dest`.

        Arguments
        - factor: the scaling factor
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def integrate(self, dt: float, vx: float, vy: float, vz: float, dest: "Quaterniond") -> "Quaterniond":
        """
        Integrate the rotation given by the angular velocity `(vx, vy, vz)` around the x, y and z axis, respectively,
        with respect to the given elapsed time delta `dt` and add the differentiate rotation to the rotation represented by this quaternion
        and store the result into `dest`.
        
        This method pre-multiplies the rotation given by `dt` and `(vx, vy, vz)` by `this`, so
        the angular velocities are always relative to the local coordinate system of the rotation represented by `this` quaternion.
        
        This method is equivalent to calling: `rotateLocal(dt * vx, dt * vy, dt * vz, dest)`
        
        Reference: <a href="http://physicsforgames.blogspot.de/2010/02/quaternions.html">http://physicsforgames.blogspot.de/</a>

        Arguments
        - dt: the delta time
        - vx: the angular velocity around the x axis
        - vy: the angular velocity around the y axis
        - vz: the angular velocity around the z axis
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def nlerp(self, q: "Quaterniondc", factor: float, dest: "Quaterniond") -> "Quaterniond":
        """
        Compute a linear (non-spherical) interpolation of `this` and the given quaternion `q`
        and store the result in `dest`.
        
        Reference: <a href="http://fabiensanglard.net/doom3_documentation/37725-293747_293747.pdf">http://fabiensanglard.net</a>

        Arguments
        - q: the other quaternion
        - factor: the interpolation factor. It is between 0.0 and 1.0
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def nlerpIterative(self, q: "Quaterniondc", alpha: float, dotThreshold: float, dest: "Quaterniond") -> "Quaterniond":
        """
        Compute linear (non-spherical) interpolations of `this` and the given quaternion `q`
        iteratively and store the result in `dest`.
        
        This method performs a series of small-step nlerp interpolations to avoid doing a costly spherical linear interpolation, like
        .slerp(Quaterniondc, double, Quaterniond) slerp,
        by subdividing the rotation arc between `this` and `q` via non-spherical linear interpolations as long as
        the absolute dot product of `this` and `q` is greater than the given `dotThreshold` parameter.
        
        Thanks to `@theagentd` at <a href="http://www.java-gaming.org/">http://www.java-gaming.org/</a> for providing the code.

        Arguments
        - q: the other quaternion
        - alpha: the interpolation factor, between 0.0 and 1.0
        - dotThreshold: the threshold for the dot product of `this` and `q` above which this method performs another iteration
                 of a small-step linear interpolation
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def lookAlong(self, dir: "Vector3dc", up: "Vector3dc", dest: "Quaterniond") -> "Quaterniond":
        """
        Apply a rotation to this quaternion that maps the given direction to the positive Z axis, and store the result in `dest`.
        
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
        - dest: will hold the result

        Returns
        - dest

        See
        - .lookAlong(double, double, double, double, double, double, Quaterniond)
        """
        ...


    def lookAlong(self, dirX: float, dirY: float, dirZ: float, upX: float, upY: float, upZ: float, dest: "Quaterniond") -> "Quaterniond":
        """
        Apply a rotation to this quaternion that maps the given direction to the positive Z axis, and store the result in `dest`.
        
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
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def difference(self, other: "Quaterniondc", dest: "Quaterniond") -> "Quaterniond":
        """
        Compute the difference between `this` and the `other` quaternion
        and store the result in `dest`.
        
        The difference is the rotation that has to be applied to get from
        `this` rotation to `other`. If `T` is `this`, `Q`
        is `other` and `D` is the computed difference, then the following equation holds:
        
        `T * D = Q`
        
        It is defined as: `D = T^-1 * Q`, where `T^-1` denotes the .invert(Quaterniond) inverse of `T`.

        Arguments
        - other: the other quaternion
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def rotateTo(self, fromDirX: float, fromDirY: float, fromDirZ: float, toDirX: float, toDirY: float, toDirZ: float, dest: "Quaterniond") -> "Quaterniond":
        """
        Apply a rotation to `this` that rotates the `fromDir` vector to point along `toDir` and
        store the result in `dest`.
        
        Since there can be multiple possible rotations, this method chooses the one with the shortest arc.
        
        If `Q` is `this` quaternion and `R` the quaternion representing the 
        specified rotation, then the new quaternion will be `Q * R`. So when transforming a
        vector `v` with the new quaternion by using `Q * R * v`, the
        rotation added by this method will be applied first!
        
        Reference: <a href="http://stackoverflow.com/questions/1171849/finding-quaternion-representing-the-rotation-from-one-vector-to-another#answer-1171995">stackoverflow.com</a>

        Arguments
        - fromDirX: the x-coordinate of the direction to rotate into the destination direction
        - fromDirY: the y-coordinate of the direction to rotate into the destination direction
        - fromDirZ: the z-coordinate of the direction to rotate into the destination direction
        - toDirX: the x-coordinate of the direction to rotate to
        - toDirY: the y-coordinate of the direction to rotate to
        - toDirZ: the z-coordinate of the direction to rotate to
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def rotateTo(self, fromDir: "Vector3dc", toDir: "Vector3dc", dest: "Quaterniond") -> "Quaterniond":
        """
        Apply a rotation to `this` that rotates the `fromDir` vector to point along `toDir` and
        store the result in `dest`.
        
        Because there can be multiple possible rotations, this method chooses the one with the shortest arc.
        
        If `Q` is `this` quaternion and `R` the quaternion representing the 
        specified rotation, then the new quaternion will be `Q * R`. So when transforming a
        vector `v` with the new quaternion by using `Q * R * v`, the
        rotation added by this method will be applied first!

        Arguments
        - fromDir: the starting direction
        - toDir: the destination direction
        - dest: will hold the result

        Returns
        - dest

        See
        - .rotateTo(double, double, double, double, double, double, Quaterniond)
        """
        ...


    def rotateX(self, angle: float, dest: "Quaterniond") -> "Quaterniond":
        """
        Apply a rotation to `this` quaternion rotating the given radians about the x axis
        and store the result in `dest`.
        
        If `Q` is `this` quaternion and `R` the quaternion representing the 
        specified rotation, then the new quaternion will be `Q * R`. So when transforming a
        vector `v` with the new quaternion by using `Q * R * v`, the
        rotation added by this method will be applied first!

        Arguments
        - angle: the angle in radians to rotate about the x axis
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def rotateY(self, angle: float, dest: "Quaterniond") -> "Quaterniond":
        """
        Apply a rotation to `this` quaternion rotating the given radians about the y axis
        and store the result in `dest`.
        
        If `Q` is `this` quaternion and `R` the quaternion representing the 
        specified rotation, then the new quaternion will be `Q * R`. So when transforming a
        vector `v` with the new quaternion by using `Q * R * v`, the
        rotation added by this method will be applied first!

        Arguments
        - angle: the angle in radians to rotate about the y axis
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def rotateZ(self, angle: float, dest: "Quaterniond") -> "Quaterniond":
        """
        Apply a rotation to `this` quaternion rotating the given radians about the z axis
        and store the result in `dest`.
        
        If `Q` is `this` quaternion and `R` the quaternion representing the 
        specified rotation, then the new quaternion will be `Q * R`. So when transforming a
        vector `v` with the new quaternion by using `Q * R * v`, the
        rotation added by this method will be applied first!

        Arguments
        - angle: the angle in radians to rotate about the z axis
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def rotateLocalX(self, angle: float, dest: "Quaterniond") -> "Quaterniond":
        """
        Apply a rotation to `this` quaternion rotating the given radians about the local x axis
        and store the result in `dest`.
        
        If `Q` is `this` quaternion and `R` the quaternion representing the 
        specified rotation, then the new quaternion will be `R * Q`. So when transforming a
        vector `v` with the new quaternion by using `R * Q * v`, the
        rotation represented by `this` will be applied first!

        Arguments
        - angle: the angle in radians to rotate about the local x axis
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def rotateLocalY(self, angle: float, dest: "Quaterniond") -> "Quaterniond":
        """
        Apply a rotation to `this` quaternion rotating the given radians about the local y axis
        and store the result in `dest`.
        
        If `Q` is `this` quaternion and `R` the quaternion representing the 
        specified rotation, then the new quaternion will be `R * Q`. So when transforming a
        vector `v` with the new quaternion by using `R * Q * v`, the
        rotation represented by `this` will be applied first!

        Arguments
        - angle: the angle in radians to rotate about the local y axis
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def rotateLocalZ(self, angle: float, dest: "Quaterniond") -> "Quaterniond":
        """
        Apply a rotation to `this` quaternion rotating the given radians about the local z axis
        and store the result in `dest`.
        
        If `Q` is `this` quaternion and `R` the quaternion representing the 
        specified rotation, then the new quaternion will be `R * Q`. So when transforming a
        vector `v` with the new quaternion by using `R * Q * v`, the
        rotation represented by `this` will be applied first!

        Arguments
        - angle: the angle in radians to rotate about the local z axis
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def rotateXYZ(self, angleX: float, angleY: float, angleZ: float, dest: "Quaterniond") -> "Quaterniond":
        """
        Apply a rotation to `this` quaternion rotating the given radians about the cartesian base unit axes,
        called the euler angles using rotation sequence `XYZ` and store the result in `dest`.
        
        This method is equivalent to calling: `rotateX(angleX, dest).rotateY(angleY).rotateZ(angleZ)`
        
        If `Q` is `this` quaternion and `R` the quaternion representing the 
        specified rotation, then the new quaternion will be `Q * R`. So when transforming a
        vector `v` with the new quaternion by using `Q * R * v`, the
        rotation added by this method will be applied first!

        Arguments
        - angleX: the angle in radians to rotate about the x axis
        - angleY: the angle in radians to rotate about the y axis
        - angleZ: the angle in radians to rotate about the z axis
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def rotateZYX(self, angleZ: float, angleY: float, angleX: float, dest: "Quaterniond") -> "Quaterniond":
        """
        Apply a rotation to `this` quaternion rotating the given radians about the cartesian base unit axes,
        called the euler angles, using the rotation sequence `ZYX` and store the result in `dest`.
        
        This method is equivalent to calling: `rotateZ(angleZ, dest).rotateY(angleY).rotateX(angleX)`
        
        If `Q` is `this` quaternion and `R` the quaternion representing the 
        specified rotation, then the new quaternion will be `Q * R`. So when transforming a
        vector `v` with the new quaternion by using `Q * R * v`, the
        rotation added by this method will be applied first!

        Arguments
        - angleZ: the angle in radians to rotate about the z axis
        - angleY: the angle in radians to rotate about the y axis
        - angleX: the angle in radians to rotate about the x axis
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def rotateYXZ(self, angleY: float, angleX: float, angleZ: float, dest: "Quaterniond") -> "Quaterniond":
        """
        Apply a rotation to `this` quaternion rotating the given radians about the cartesian base unit axes,
        called the euler angles, using the rotation sequence `YXZ` and store the result in `dest`.
        
        This method is equivalent to calling: `rotateY(angleY, dest).rotateX(angleX).rotateZ(angleZ)`
        
        If `Q` is `this` quaternion and `R` the quaternion representing the 
        specified rotation, then the new quaternion will be `Q * R`. So when transforming a
        vector `v` with the new quaternion by using `Q * R * v`, the
        rotation added by this method will be applied first!

        Arguments
        - angleY: the angle in radians to rotate about the y axis
        - angleX: the angle in radians to rotate about the x axis
        - angleZ: the angle in radians to rotate about the z axis
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def getEulerAnglesXYZ(self, eulerAngles: "Vector3d") -> "Vector3d":
        """
        Get the euler angles in radians in rotation sequence `XYZ` of this quaternion and store them in the 
        provided parameter `eulerAngles`.
        
        The Euler angles are always returned as the angle around X in the Vector3d.x field, the angle around Y in the Vector3d.y
        field and the angle around Z in the Vector3d.z field of the supplied Vector3d instance.

        Arguments
        - eulerAngles: will hold the euler angles in radians

        Returns
        - the passed in vector
        """
        ...


    def getEulerAnglesZYX(self, eulerAngles: "Vector3d") -> "Vector3d":
        """
        Get the euler angles in radians in rotation sequence `ZYX` of this quaternion and store them in the 
        provided parameter `eulerAngles`.
        
        The Euler angles are always returned as the angle around X in the Vector3d.x field, the angle around Y in the Vector3d.y
        field and the angle around Z in the Vector3d.z field of the supplied Vector3d instance.

        Arguments
        - eulerAngles: will hold the euler angles in radians

        Returns
        - the passed in vector
        """
        ...


    def getEulerAnglesZXY(self, eulerAngles: "Vector3d") -> "Vector3d":
        """
        Get the euler angles in radians in rotation sequence `ZXY` of this quaternion and store them in the 
        provided parameter `eulerAngles`.
        
        The Euler angles are always returned as the angle around X in the Vector3d.x field, the angle around Y in the Vector3d.y
        field and the angle around Z in the Vector3d.z field of the supplied Vector3d instance.

        Arguments
        - eulerAngles: will hold the euler angles in radians

        Returns
        - the passed in vector
        """
        ...


    def getEulerAnglesYXZ(self, eulerAngles: "Vector3d") -> "Vector3d":
        """
        Get the euler angles in radians in rotation sequence `YXZ` of this quaternion and store them in the 
        provided parameter `eulerAngles`.
        
        The Euler angles are always returned as the angle around X in the Vector3d.x field, the angle around Y in the Vector3d.y
        field and the angle around Z in the Vector3d.z field of the supplied Vector3d instance.

        Arguments
        - eulerAngles: will hold the euler angles in radians

        Returns
        - the passed in vector
        """
        ...


    def rotateAxis(self, angle: float, axisX: float, axisY: float, axisZ: float, dest: "Quaterniond") -> "Quaterniond":
        """
        Apply a rotation to `this` quaternion rotating the given radians about the specified axis
        and store the result in `dest`.
        
        If `Q` is `this` quaternion and `R` the quaternion representing the 
        specified rotation, then the new quaternion will be `Q * R`. So when transforming a
        vector `v` with the new quaternion by using `Q * R * v`, the
        rotation added by this method will be applied first!

        Arguments
        - angle: the angle in radians to rotate about the specified axis
        - axisX: the x coordinate of the rotation axis
        - axisY: the y coordinate of the rotation axis
        - axisZ: the z coordinate of the rotation axis
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def rotateAxis(self, angle: float, axis: "Vector3dc", dest: "Quaterniond") -> "Quaterniond":
        """
        Apply a rotation to `this` quaternion rotating the given radians about the specified axis
        and store the result in `dest`.
        
        If `Q` is `this` quaternion and `R` the quaternion representing the 
        specified rotation, then the new quaternion will be `Q * R`. So when transforming a
        vector `v` with the new quaternion by using `Q * R * v`, the
        rotation added by this method will be applied first!

        Arguments
        - angle: the angle in radians to rotate about the specified axis
        - axis: the rotation axis
        - dest: will hold the result

        Returns
        - dest

        See
        - .rotateAxis(double, double, double, double, Quaterniond)
        """
        ...


    def positiveX(self, dir: "Vector3d") -> "Vector3d":
        """
        Obtain the direction of `+X` before the rotation transformation represented by `this` quaternion is applied.
        
        This method is equivalent to the following code:
        ```
        Quaterniond inv = new Quaterniond(this).invert();
        inv.transform(dir.set(1, 0, 0));
        ```

        Arguments
        - dir: will hold the direction of `+X`

        Returns
        - dir
        """
        ...


    def normalizedPositiveX(self, dir: "Vector3d") -> "Vector3d":
        """
        Obtain the direction of `+X` before the rotation transformation represented by `this` *normalized* quaternion is applied.
        The quaternion *must* be .normalize(Quaterniond) normalized for this method to work.
        
        This method is equivalent to the following code:
        ```
        Quaterniond inv = new Quaterniond(this).conjugate();
        inv.transform(dir.set(1, 0, 0));
        ```

        Arguments
        - dir: will hold the direction of `+X`

        Returns
        - dir
        """
        ...


    def positiveY(self, dir: "Vector3d") -> "Vector3d":
        """
        Obtain the direction of `+Y` before the rotation transformation represented by `this` quaternion is applied.
        
        This method is equivalent to the following code:
        ```
        Quaterniond inv = new Quaterniond(this).invert();
        inv.transform(dir.set(0, 1, 0));
        ```

        Arguments
        - dir: will hold the direction of `+Y`

        Returns
        - dir
        """
        ...


    def normalizedPositiveY(self, dir: "Vector3d") -> "Vector3d":
        """
        Obtain the direction of `+Y` before the rotation transformation represented by `this` *normalized* quaternion is applied.
        The quaternion *must* be .normalize(Quaterniond) normalized for this method to work.
        
        This method is equivalent to the following code:
        ```
        Quaterniond inv = new Quaterniond(this).conjugate();
        inv.transform(dir.set(0, 1, 0));
        ```

        Arguments
        - dir: will hold the direction of `+Y`

        Returns
        - dir
        """
        ...


    def positiveZ(self, dir: "Vector3d") -> "Vector3d":
        """
        Obtain the direction of `+Z` before the rotation transformation represented by `this` quaternion is applied.
        
        This method is equivalent to the following code:
        ```
        Quaterniond inv = new Quaterniond(this).invert();
        inv.transform(dir.set(0, 0, 1));
        ```

        Arguments
        - dir: will hold the direction of `+Z`

        Returns
        - dir
        """
        ...


    def normalizedPositiveZ(self, dir: "Vector3d") -> "Vector3d":
        """
        Obtain the direction of `+Z` before the rotation transformation represented by `this` *normalized* quaternion is applied.
        The quaternion *must* be .normalize(Quaterniond) normalized for this method to work.
        
        This method is equivalent to the following code:
        ```
        Quaterniond inv = new Quaterniond(this).conjugate();
        inv.transform(dir.set(0, 0, 1));
        ```

        Arguments
        - dir: will hold the direction of `+Z`

        Returns
        - dir
        """
        ...


    def conjugateBy(self, q: "Quaterniondc", dest: "Quaterniond") -> "Quaterniond":
        """
        Conjugate `this` by the given quaternion `q` by computing `q * this * q^-1`
        and store the result into `dest`.

        Arguments
        - q: the Quaterniondc to conjugate `this` by
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def isFinite(self) -> bool:
        """
        Determine whether all components are finite floating-point values, that
        is, they are not Double.isNaN() NaN and not
        Double.isInfinite() infinity.

        Returns
        - `True` if all components are finite floating-point values;
                `False` otherwise
        """
        ...


    def equals(self, q: "Quaterniondc", delta: float) -> bool:
        """
             Compare the quaternion components of `this` quaternion with the given quaternion using the given `delta`
        and return whether all of them are equal within a maximum difference of `delta`.
        
        Please note that this method is not used by any data structure such as ArrayList HashSet or HashMap
        and their operations, such as ArrayList.contains(Object) or HashSet.remove(Object), since those
        data structures only use the Object.equals(Object) and Object.hashCode() methods.

        Arguments
        - q: the other quaternion
        - delta: the allowed maximum difference

        Returns
        - `True` whether all of the quaternion components are equal; `False` otherwise
        """
        ...


    def equals(self, x: float, y: float, z: float, w: float) -> bool:
        """
        Arguments
        - x: the x component to compare to
        - y: the y component to compare to
        - z: the z component to compare to
        - w: the w component to compare to

        Returns
        - `True` if all the quaternion components are equal
        """
        ...
