"""
Python module generated from Java source file org.joml.AxisAngle4d

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


class AxisAngle4d(Externalizable, Cloneable):
    """
    Represents a 3D rotation of a given radians about an axis represented as an
    unit 3D vector.
    
    This class uses double-precision components.

    Author(s)
    - Kai Burjack
    """

    def __init__(self):
        """
        Create a new AxisAngle4d with zero rotation about `(0, 0, 1)`.
        """
        ...


    def __init__(self, a: "AxisAngle4d"):
        """
        Create a new AxisAngle4d with the same values of `a`.

        Arguments
        - a: the AngleAxis4d to copy the values from
        """
        ...


    def __init__(self, a: "AxisAngle4f"):
        """
        Create a new AxisAngle4d with the same values of `a`.

        Arguments
        - a: the AngleAxis4f to copy the values from
        """
        ...


    def __init__(self, q: "Quaternionfc"):
        """
        Create a new AxisAngle4d from the given Quaternionfc.
        
        Reference: <a href=
        "http://www.euclideanspace.com/maths/geometry/rotations/conversions/quaternionToAngle/"
        >http://www.euclideanspace.com</a>

        Arguments
        - q: the quaternion from which to create the new AngleAxis4f
        """
        ...


    def __init__(self, q: "Quaterniondc"):
        """
        Create a new AxisAngle4d from the given Quaterniondc.
        
        Reference: <a href=
        "http://www.euclideanspace.com/maths/geometry/rotations/conversions/quaternionToAngle/"
        >http://www.euclideanspace.com</a>

        Arguments
        - q: the quaternion from which to create the new AngleAxis4d
        """
        ...


    def __init__(self, angle: float, x: float, y: float, z: float):
        """
        Create a new AxisAngle4d with the given values.

        Arguments
        - angle: the angle in radians
        - x: the x-coordinate of the rotation axis
        - y: the y-coordinate of the rotation axis
        - z: the z-coordinate of the rotation axis
        """
        ...


    def __init__(self, angle: float, v: "Vector3dc"):
        """
        Create a new AxisAngle4d with the given values.

        Arguments
        - angle: the angle in radians
        - v: the rotation axis as a Vector3dc
        """
        ...


    def __init__(self, angle: float, v: "Vector3f"):
        """
        Create a new AxisAngle4d with the given values.

        Arguments
        - angle: the angle in radians
        - v: the rotation axis as a Vector3f
        """
        ...


    def set(self, a: "AxisAngle4d") -> "AxisAngle4d":
        """
        Set this AxisAngle4d to the values of `a`.

        Arguments
        - a: the AngleAxis4f to copy the values from

        Returns
        - this
        """
        ...


    def set(self, a: "AxisAngle4f") -> "AxisAngle4d":
        """
        Set this AxisAngle4d to the values of `a`.

        Arguments
        - a: the AngleAxis4f to copy the values from

        Returns
        - this
        """
        ...


    def set(self, angle: float, x: float, y: float, z: float) -> "AxisAngle4d":
        """
        Set this AxisAngle4d to the given values.

        Arguments
        - angle: the angle in radians
        - x: the x-coordinate of the rotation axis
        - y: the y-coordinate of the rotation axis
        - z: the z-coordinate of the rotation axis

        Returns
        - this
        """
        ...


    def set(self, angle: float, v: "Vector3dc") -> "AxisAngle4d":
        """
        Set this AxisAngle4d to the given values.

        Arguments
        - angle: the angle in radians
        - v: the rotation axis as a Vector3dc

        Returns
        - this
        """
        ...


    def set(self, angle: float, v: "Vector3f") -> "AxisAngle4d":
        """
        Set this AxisAngle4d to the given values.

        Arguments
        - angle: the angle in radians
        - v: the rotation axis as a Vector3f

        Returns
        - this
        """
        ...


    def set(self, q: "Quaternionfc") -> "AxisAngle4d":
        """
        Set this AxisAngle4d to be equivalent to the given
        Quaternionfc.

        Arguments
        - q: the quaternion to set this AngleAxis4d from

        Returns
        - this
        """
        ...


    def set(self, q: "Quaterniondc") -> "AxisAngle4d":
        """
        Set this AxisAngle4d to be equivalent to the given
        Quaterniondc.

        Arguments
        - q: the quaternion to set this AngleAxis4d from

        Returns
        - this
        """
        ...


    def set(self, m: "Matrix3fc") -> "AxisAngle4d":
        """
        Set this AxisAngle4d to be equivalent to the rotation 
        of the given Matrix3fc.
        
        Reference: <a href="http://www.euclideanspace.com/maths/geometry/rotations/conversions/matrixToAngle/">http://www.euclideanspace.com</a>

        Arguments
        - m: the Matrix3fc to set this AngleAxis4d from

        Returns
        - this
        """
        ...


    def set(self, m: "Matrix3dc") -> "AxisAngle4d":
        """
        Set this AxisAngle4d to be equivalent to the rotation 
        of the given Matrix3dc.
        
        Reference: <a href="http://www.euclideanspace.com/maths/geometry/rotations/conversions/matrixToAngle/">http://www.euclideanspace.com</a>

        Arguments
        - m: the Matrix3dc to set this AngleAxis4d from

        Returns
        - this
        """
        ...


    def set(self, m: "Matrix4fc") -> "AxisAngle4d":
        """
        Set this AxisAngle4d to be equivalent to the rotational component 
        of the given Matrix4fc.
        
        Reference: <a href="http://www.euclideanspace.com/maths/geometry/rotations/conversions/matrixToAngle/">http://www.euclideanspace.com</a>

        Arguments
        - m: the Matrix4fc to set this AngleAxis4d from

        Returns
        - this
        """
        ...


    def set(self, m: "Matrix4x3fc") -> "AxisAngle4d":
        """
        Set this AxisAngle4d to be equivalent to the rotational component 
        of the given Matrix4x3fc.
        
        Reference: <a href="http://www.euclideanspace.com/maths/geometry/rotations/conversions/matrixToAngle/">http://www.euclideanspace.com</a>

        Arguments
        - m: the Matrix4x3fc to set this AngleAxis4d from

        Returns
        - this
        """
        ...


    def set(self, m: "Matrix4dc") -> "AxisAngle4d":
        """
        Set this AxisAngle4d to be equivalent to the rotational component 
        of the given Matrix4dc.
        
        Reference: <a href="http://www.euclideanspace.com/maths/geometry/rotations/conversions/matrixToAngle/">http://www.euclideanspace.com</a>

        Arguments
        - m: the Matrix4dc to set this AngleAxis4d from

        Returns
        - this
        """
        ...


    def get(self, q: "Quaternionf") -> "Quaternionf":
        """
        Set the given Quaternionf to be equivalent to this AxisAngle4d rotation.

        Arguments
        - q: the quaternion to set

        Returns
        - q

        See
        - Quaternionf.set(AxisAngle4d)
        """
        ...


    def get(self, q: "Quaterniond") -> "Quaterniond":
        """
        Set the given Quaterniond to be equivalent to this AxisAngle4d rotation.

        Arguments
        - q: the quaternion to set

        Returns
        - q

        See
        - Quaterniond.set(AxisAngle4d)
        """
        ...


    def get(self, m: "Matrix4f") -> "Matrix4f":
        """
        Set the given Matrix4f to a rotation transformation equivalent to this AxisAngle4d.

        Arguments
        - m: the matrix to set

        Returns
        - m

        See
        - Matrix4f.set(AxisAngle4d)
        """
        ...


    def get(self, m: "Matrix3f") -> "Matrix3f":
        """
        Set the given Matrix3f to a rotation transformation equivalent to this AxisAngle4d.

        Arguments
        - m: the matrix to set

        Returns
        - m

        See
        - Matrix3f.set(AxisAngle4d)
        """
        ...


    def get(self, m: "Matrix4d") -> "Matrix4d":
        """
        Set the given Matrix4d to a rotation transformation equivalent to this AxisAngle4d.

        Arguments
        - m: the matrix to set

        Returns
        - m

        See
        - Matrix4f.set(AxisAngle4d)
        """
        ...


    def get(self, m: "Matrix3d") -> "Matrix3d":
        """
        Set the given Matrix3d to a rotation transformation equivalent to this AxisAngle4d.

        Arguments
        - m: the matrix to set

        Returns
        - m

        See
        - Matrix3f.set(AxisAngle4d)
        """
        ...


    def get(self, dest: "AxisAngle4d") -> "AxisAngle4d":
        """
        Set the given AxisAngle4d to this AxisAngle4d.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def get(self, dest: "AxisAngle4f") -> "AxisAngle4f":
        """
        Set the given AxisAngle4f to this AxisAngle4d.

        Arguments
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def writeExternal(self, out: "ObjectOutput") -> None:
        ...


    def readExternal(self, in: "ObjectInput") -> None:
        ...


    def normalize(self) -> "AxisAngle4d":
        """
        Normalize the axis vector.

        Returns
        - this
        """
        ...


    def rotate(self, ang: float) -> "AxisAngle4d":
        """
        Increase the rotation angle by the given amount.
        
        This method also takes care of wrapping around.

        Arguments
        - ang: the angle increase

        Returns
        - this
        """
        ...


    def transform(self, v: "Vector3d") -> "Vector3d":
        """
        Transform the given vector by the rotation transformation described by this AxisAngle4d.

        Arguments
        - v: the vector to transform

        Returns
        - v
        """
        ...


    def transform(self, v: "Vector3dc", dest: "Vector3d") -> "Vector3d":
        """
        Transform the given vector by the rotation transformation described by this AxisAngle4d
        and store the result in `dest`.

        Arguments
        - v: the vector to transform
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def transform(self, v: "Vector3f") -> "Vector3f":
        """
        Transform the given vector by the rotation transformation described by this AxisAngle4d.

        Arguments
        - v: the vector to transform

        Returns
        - v
        """
        ...


    def transform(self, v: "Vector3fc", dest: "Vector3f") -> "Vector3f":
        """
        Transform the given vector by the rotation transformation described by this AxisAngle4d
        and store the result in `dest`.

        Arguments
        - v: the vector to transform
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def transform(self, v: "Vector4d") -> "Vector4d":
        """
        Transform the given vector by the rotation transformation described by this AxisAngle4d.

        Arguments
        - v: the vector to transform

        Returns
        - v
        """
        ...


    def transform(self, v: "Vector4dc", dest: "Vector4d") -> "Vector4d":
        """
        Transform the given vector by the rotation transformation described by this AxisAngle4d
        and store the result in `dest`.

        Arguments
        - v: the vector to transform
        - dest: will hold the result

        Returns
        - dest
        """
        ...


    def toString(self) -> str:
        """
        Return a string representation of this AxisAngle4d.
        
        This method creates a new DecimalFormat on every invocation with the format string "` 0.000E0;-`".

        Returns
        - the string representation
        """
        ...


    def toString(self, formatter: "NumberFormat") -> str:
        """
        Return a string representation of this AxisAngle4d by formatting the components with the given NumberFormat.

        Arguments
        - formatter: the NumberFormat used to format the vector components with

        Returns
        - the string representation
        """
        ...


    def hashCode(self) -> int:
        ...


    def equals(self, obj: "Object") -> bool:
        ...


    def clone(self) -> "Object":
        ...
