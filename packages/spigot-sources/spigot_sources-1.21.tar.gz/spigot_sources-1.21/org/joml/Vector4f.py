"""
Python module generated from Java source file org.joml.Vector4f

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


class Vector4f(Externalizable, Cloneable, Vector4fc):
    """
    Contains the definition of a Vector comprising 4 floats and associated
    transformations.

    Author(s)
    - F. Neurath
    """

    def __init__(self):
        """
        Create a new Vector4f of `(0, 0, 0, 1)`.
        """
        ...


    def __init__(self, v: "Vector4fc"):
        """
        Create a new Vector4f with the same values as `v`.

        Arguments
        - v: the Vector4fc to copy the values from
        """
        ...


    def __init__(self, v: "Vector4ic"):
        """
        Create a new Vector4f with the same values as `v`.

        Arguments
        - v: the Vector4ic to copy the values from
        """
        ...


    def __init__(self, v: "Vector3fc", w: float):
        """
        Create a new Vector4f with the first three components from the
        given `v` and the given `w`.

        Arguments
        - v: the Vector3fc
        - w: the w component
        """
        ...


    def __init__(self, v: "Vector3ic", w: float):
        """
        Create a new Vector4f with the first three components from the
        given `v` and the given `w`.

        Arguments
        - v: the Vector3ic
        - w: the w component
        """
        ...


    def __init__(self, v: "Vector2fc", z: float, w: float):
        """
        Create a new Vector4f with the first two components from the
        given `v` and the given `z`, and `w`.

        Arguments
        - v: the Vector2fc
        - z: the z component
        - w: the w component
        """
        ...


    def __init__(self, v: "Vector2ic", z: float, w: float):
        """
        Create a new Vector4f with the first two components from the
        given `v` and the given `z`, and `w`.

        Arguments
        - v: the Vector2ic
        - z: the z component
        - w: the w component
        """
        ...


    def __init__(self, d: float):
        """
        Create a new Vector4f and initialize all four components with the given value.

        Arguments
        - d: the value of all four components
        """
        ...


    def __init__(self, x: float, y: float, z: float, w: float):
        """
        Create a new Vector4f with the given component values.

        Arguments
        - x: the x component
        - y: the y component
        - z: the z component
        - w: the w component
        """
        ...


    def __init__(self, xyzw: list[float]):
        """
        Create a new Vector4f and initialize its four components from the first
        four elements of the given array.

        Arguments
        - xyzw: the array containing at least four elements
        """
        ...


    def __init__(self, buffer: "ByteBuffer"):
        """
        Create a new Vector4f and read this vector from the supplied ByteBuffer
        at the current buffer ByteBuffer.position() position.
        
        This method will not increment the position of the given ByteBuffer.
        
        In order to specify the offset into the ByteBuffer at which
        the vector is read, use .Vector4f(int, ByteBuffer), taking
        the absolute position as parameter.

        Arguments
        - buffer: values will be read in `x, y, z, w` order

        See
        - .Vector4f(int, ByteBuffer)
        """
        ...


    def __init__(self, index: int, buffer: "ByteBuffer"):
        """
        Create a new Vector4f and read this vector from the supplied ByteBuffer
        starting at the specified absolute buffer position/index.
        
        This method will not increment the position of the given ByteBuffer.

        Arguments
        - index: the absolute position into the ByteBuffer
        - buffer: values will be read in `x, y, z, w` order
        """
        ...


    def __init__(self, buffer: "FloatBuffer"):
        """
        Create a new Vector4f and read this vector from the supplied FloatBuffer
        at the current buffer FloatBuffer.position() position.
        
        This method will not increment the position of the given FloatBuffer.
        
        In order to specify the offset into the FloatBuffer at which
        the vector is read, use .Vector4f(int, FloatBuffer), taking
        the absolute position as parameter.

        Arguments
        - buffer: values will be read in `x, y, z, w` order

        See
        - .Vector4f(int, FloatBuffer)
        """
        ...


    def __init__(self, index: int, buffer: "FloatBuffer"):
        """
        Create a new Vector4f and read this vector from the supplied FloatBuffer
        starting at the specified absolute buffer position/index.
        
        This method will not increment the position of the given FloatBuffer.

        Arguments
        - index: the absolute position into the FloatBuffer
        - buffer: values will be read in `x, y, z, w` order
        """
        ...


    def x(self) -> float:
        ...


    def y(self) -> float:
        ...


    def z(self) -> float:
        ...


    def w(self) -> float:
        ...


    def set(self, v: "Vector4fc") -> "Vector4f":
        """
        Set this Vector4f to the values of the given `v`.

        Arguments
        - v: the vector whose values will be copied into this

        Returns
        - this
        """
        ...


    def set(self, v: "Vector4ic") -> "Vector4f":
        """
        Set this Vector4f to the values of the given `v`.

        Arguments
        - v: the vector whose values will be copied into this

        Returns
        - this
        """
        ...


    def set(self, v: "Vector4dc") -> "Vector4f":
        """
        Set this Vector4f to the values of the given `v`.
        
        Note that due to the given vector `v` storing the components in double-precision,
        there is the possibility to lose precision.

        Arguments
        - v: the vector whose values will be copied into this

        Returns
        - this
        """
        ...


    def set(self, v: "Vector3fc", w: float) -> "Vector4f":
        """
        Set the first three components of this to the components of
        `v` and the last component to `w`.

        Arguments
        - v: the Vector3fc to copy
        - w: the w component

        Returns
        - this
        """
        ...


    def set(self, v: "Vector3ic", w: float) -> "Vector4f":
        """
        Set the first three components of this to the components of
        `v` and the last component to `w`.

        Arguments
        - v: the Vector3ic to copy
        - w: the w component

        Returns
        - this
        """
        ...


    def set(self, v: "Vector2fc", z: float, w: float) -> "Vector4f":
        """
        Sets the first two components of this to the components of given `v`
        and last two components to the given `z`, and `w`.

        Arguments
        - v: the Vector2fc
        - z: the z component
        - w: the w component

        Returns
        - this
        """
        ...


    def set(self, v: "Vector2ic", z: float, w: float) -> "Vector4f":
        """
        Sets the first two components of this to the components of given `v`
        and last two components to the given `z`, and `w`.

        Arguments
        - v: the Vector2ic
        - z: the z component
        - w: the w component

        Returns
        - this
        """
        ...


    def set(self, d: float) -> "Vector4f":
        """
        Set the x, y, z, and w components to the supplied value.

        Arguments
        - d: the value of all four components

        Returns
        - this
        """
        ...


    def set(self, x: float, y: float, z: float, w: float) -> "Vector4f":
        """
        Set the x, y, z, and w components to the supplied values.

        Arguments
        - x: the x component
        - y: the y component
        - z: the z component
        - w: the w component

        Returns
        - this
        """
        ...


    def set(self, x: float, y: float, z: float) -> "Vector4f":
        """
        Set the x, y, z components to the supplied values.

        Arguments
        - x: the x component
        - y: the y component
        - z: the z component

        Returns
        - this
        """
        ...


    def set(self, d: float) -> "Vector4f":
        """
        Set the x, y, z, and w components to the supplied value.

        Arguments
        - d: the value of all four components

        Returns
        - this
        """
        ...


    def set(self, x: float, y: float, z: float, w: float) -> "Vector4f":
        """
        Set the x, y, z, and w components to the supplied values.

        Arguments
        - x: the x component
        - y: the y component
        - z: the z component
        - w: the w component

        Returns
        - this
        """
        ...


    def set(self, xyzw: list[float]) -> "Vector4f":
        """
        Set the four components of this vector to the first four elements of the given array.

        Arguments
        - xyzw: the array containing at least four elements

        Returns
        - this
        """
        ...


    def set(self, buffer: "ByteBuffer") -> "Vector4f":
        """
        Read this vector from the supplied ByteBuffer at the current
        buffer ByteBuffer.position() position.
        
        This method will not increment the position of the given ByteBuffer.
        
        In order to specify the offset into the ByteBuffer at which
        the vector is read, use .set(int, ByteBuffer), taking
        the absolute position as parameter.

        Arguments
        - buffer: values will be read in `x, y, z, w` order

        Returns
        - this

        See
        - .set(int, ByteBuffer)
        """
        ...


    def set(self, index: int, buffer: "ByteBuffer") -> "Vector4f":
        """
        Read this vector from the supplied ByteBuffer starting at the specified
        absolute buffer position/index.
        
        This method will not increment the position of the given ByteBuffer.

        Arguments
        - index: the absolute position into the ByteBuffer
        - buffer: values will be read in `x, y, z, w` order

        Returns
        - this
        """
        ...


    def set(self, buffer: "FloatBuffer") -> "Vector4f":
        """
        Read this vector from the supplied FloatBuffer at the current
        buffer FloatBuffer.position() position.
        
        This method will not increment the position of the given FloatBuffer.
        
        In order to specify the offset into the FloatBuffer at which
        the vector is read, use .set(int, FloatBuffer), taking
        the absolute position as parameter.

        Arguments
        - buffer: values will be read in `x, y, z, w` order

        Returns
        - this

        See
        - .set(int, FloatBuffer)
        """
        ...


    def set(self, index: int, buffer: "FloatBuffer") -> "Vector4f":
        """
        Read this vector from the supplied FloatBuffer starting at the specified
        absolute buffer position/index.
        
        This method will not increment the position of the given FloatBuffer.

        Arguments
        - index: the absolute position into the FloatBuffer
        - buffer: values will be read in `x, y, z, w` order

        Returns
        - this
        """
        ...


    def setFromAddress(self, address: int) -> "Vector4f":
        """
        Set the values of this vector by reading 4 float values from off-heap memory,
        starting at the given address.
        
        This method will throw an UnsupportedOperationException when JOML is used with `-Djoml.nounsafe`.
        
        *This method is unsafe as it can result in a crash of the JVM process when the specified address range does not belong to this process.*

        Arguments
        - address: the off-heap memory address to read the vector values from

        Returns
        - this
        """
        ...


    def setComponent(self, component: int, value: float) -> "Vector4f":
        """
        Set the value of the specified component of this vector.

        Arguments
        - component: the component whose value to set, within `[0..3]`
        - value: the value to set

        Returns
        - this

        Raises
        - IllegalArgumentException: if `component` is not within `[0..3]`
        """
        ...


    def get(self, buffer: "FloatBuffer") -> "FloatBuffer":
        ...


    def get(self, index: int, buffer: "FloatBuffer") -> "FloatBuffer":
        ...


    def get(self, buffer: "ByteBuffer") -> "ByteBuffer":
        ...


    def get(self, index: int, buffer: "ByteBuffer") -> "ByteBuffer":
        ...


    def getToAddress(self, address: int) -> "Vector4fc":
        ...


    def sub(self, v: "Vector4fc") -> "Vector4f":
        """
        Subtract the supplied vector from this one.

        Arguments
        - v: the vector to subtract

        Returns
        - this
        """
        ...


    def sub(self, x: float, y: float, z: float, w: float) -> "Vector4f":
        """
        Subtract `(x, y, z, w)` from this.

        Arguments
        - x: the x component to subtract
        - y: the y component to subtract
        - z: the z component to subtract
        - w: the w component to subtract

        Returns
        - this
        """
        ...


    def sub(self, v: "Vector4fc", dest: "Vector4f") -> "Vector4f":
        ...


    def sub(self, x: float, y: float, z: float, w: float, dest: "Vector4f") -> "Vector4f":
        ...


    def add(self, v: "Vector4fc") -> "Vector4f":
        """
        Add the supplied vector to this one.

        Arguments
        - v: the vector to add

        Returns
        - this
        """
        ...


    def add(self, v: "Vector4fc", dest: "Vector4f") -> "Vector4f":
        ...


    def add(self, x: float, y: float, z: float, w: float) -> "Vector4f":
        """
        Increment the components of this vector by the given values.

        Arguments
        - x: the x component to add
        - y: the y component to add
        - z: the z component to add
        - w: the w component to add

        Returns
        - this
        """
        ...


    def add(self, x: float, y: float, z: float, w: float, dest: "Vector4f") -> "Vector4f":
        ...


    def fma(self, a: "Vector4fc", b: "Vector4fc") -> "Vector4f":
        """
        Add the component-wise multiplication of `a * b` to this vector.

        Arguments
        - a: the first multiplicand
        - b: the second multiplicand

        Returns
        - this
        """
        ...


    def fma(self, a: float, b: "Vector4fc") -> "Vector4f":
        """
        Add the component-wise multiplication of `a * b` to this vector.

        Arguments
        - a: the first multiplicand
        - b: the second multiplicand

        Returns
        - this
        """
        ...


    def fma(self, a: "Vector4fc", b: "Vector4fc", dest: "Vector4f") -> "Vector4f":
        ...


    def fma(self, a: float, b: "Vector4fc", dest: "Vector4f") -> "Vector4f":
        ...


    def mulAdd(self, a: "Vector4fc", b: "Vector4fc") -> "Vector4f":
        """
        Add the component-wise multiplication of `this * a` to `b`
        and store the result in `this`.

        Arguments
        - a: the multiplicand
        - b: the addend

        Returns
        - this
        """
        ...


    def mulAdd(self, a: float, b: "Vector4fc") -> "Vector4f":
        """
        Add the component-wise multiplication of `this * a` to `b`
        and store the result in `this`.

        Arguments
        - a: the multiplicand
        - b: the addend

        Returns
        - this
        """
        ...


    def mulAdd(self, a: "Vector4fc", b: "Vector4fc", dest: "Vector4f") -> "Vector4f":
        ...


    def mulAdd(self, a: float, b: "Vector4fc", dest: "Vector4f") -> "Vector4f":
        ...


    def mul(self, v: "Vector4fc") -> "Vector4f":
        """
        Multiply this Vector4f component-wise by another Vector4f.

        Arguments
        - v: the other vector

        Returns
        - this
        """
        ...


    def mul(self, v: "Vector4fc", dest: "Vector4f") -> "Vector4f":
        ...


    def div(self, v: "Vector4fc") -> "Vector4f":
        """
        Divide this Vector4f component-wise by another Vector4f.

        Arguments
        - v: the vector to divide by

        Returns
        - this
        """
        ...


    def div(self, v: "Vector4fc", dest: "Vector4f") -> "Vector4f":
        ...


    def mul(self, mat: "Matrix4fc") -> "Vector4f":
        """
        Multiply the given matrix mat with this Vector4f and store the result in
        `this`.

        Arguments
        - mat: the matrix to multiply the vector with

        Returns
        - this
        """
        ...


    def mul(self, mat: "Matrix4fc", dest: "Vector4f") -> "Vector4f":
        ...


    def mulTranspose(self, mat: "Matrix4fc") -> "Vector4f":
        """
        Multiply the transpose of the given matrix `mat` with this Vector4f and store the result in
        `this`.

        Arguments
        - mat: the matrix whose transpose to multiply the vector with

        Returns
        - this
        """
        ...


    def mulTranspose(self, mat: "Matrix4fc", dest: "Vector4f") -> "Vector4f":
        ...


    def mulAffine(self, mat: "Matrix4fc", dest: "Vector4f") -> "Vector4f":
        ...


    def mulAffineTranspose(self, mat: "Matrix4fc", dest: "Vector4f") -> "Vector4f":
        ...


    def mul(self, mat: "Matrix4x3fc") -> "Vector4f":
        """
        Multiply the given matrix mat with this Vector4f and store the result in
        `this`.

        Arguments
        - mat: the matrix to multiply the vector with

        Returns
        - this
        """
        ...


    def mul(self, mat: "Matrix4x3fc", dest: "Vector4f") -> "Vector4f":
        ...


    def mulProject(self, mat: "Matrix4fc", dest: "Vector4f") -> "Vector4f":
        ...


    def mulProject(self, mat: "Matrix4fc") -> "Vector4f":
        """
        Multiply the given matrix `mat` with this Vector4f, perform perspective division.

        Arguments
        - mat: the matrix to multiply this vector by

        Returns
        - this
        """
        ...


    def mulProject(self, mat: "Matrix4fc", dest: "Vector3f") -> "Vector3f":
        ...


    def mul(self, scalar: float) -> "Vector4f":
        """
        Multiply all components of this Vector4f by the given scalar
        value.

        Arguments
        - scalar: the scalar to multiply by

        Returns
        - this
        """
        ...


    def mul(self, scalar: float, dest: "Vector4f") -> "Vector4f":
        ...


    def mul(self, x: float, y: float, z: float, w: float) -> "Vector4f":
        """
        Multiply the components of this Vector4f by the given scalar values and store the result in `this`.

        Arguments
        - x: the x component to multiply by
        - y: the y component to multiply by
        - z: the z component to multiply by
        - w: the w component to multiply by

        Returns
        - this
        """
        ...


    def mul(self, x: float, y: float, z: float, w: float, dest: "Vector4f") -> "Vector4f":
        ...


    def div(self, scalar: float) -> "Vector4f":
        """
        Divide all components of this Vector4f by the given scalar
        value.

        Arguments
        - scalar: the scalar to divide by

        Returns
        - this
        """
        ...


    def div(self, scalar: float, dest: "Vector4f") -> "Vector4f":
        ...


    def div(self, x: float, y: float, z: float, w: float) -> "Vector4f":
        """
        Divide the components of this Vector4f by the given scalar values and store the result in `this`.

        Arguments
        - x: the x component to divide by
        - y: the y component to divide by
        - z: the z component to divide by
        - w: the w component to divide by

        Returns
        - this
        """
        ...


    def div(self, x: float, y: float, z: float, w: float, dest: "Vector4f") -> "Vector4f":
        ...


    def rotate(self, quat: "Quaternionfc") -> "Vector4f":
        """
        Rotate this vector by the given quaternion `quat` and store the result in `this`.

        Arguments
        - quat: the quaternion to rotate this vector

        Returns
        - this

        See
        - Quaternionf.transform(Vector4f)
        """
        ...


    def rotate(self, quat: "Quaternionfc", dest: "Vector4f") -> "Vector4f":
        ...


    def rotateAbout(self, angle: float, x: float, y: float, z: float) -> "Vector4f":
        """
        Rotate this vector the specified radians around the given rotation axis.

        Arguments
        - angle: the angle in radians
        - x: the x component of the rotation axis
        - y: the y component of the rotation axis
        - z: the z component of the rotation axis

        Returns
        - this
        """
        ...


    def rotateAxis(self, angle: float, aX: float, aY: float, aZ: float, dest: "Vector4f") -> "Vector4f":
        ...


    def rotateX(self, angle: float) -> "Vector4f":
        """
        Rotate this vector the specified radians around the X axis.

        Arguments
        - angle: the angle in radians

        Returns
        - this
        """
        ...


    def rotateX(self, angle: float, dest: "Vector4f") -> "Vector4f":
        ...


    def rotateY(self, angle: float) -> "Vector4f":
        """
        Rotate this vector the specified radians around the Y axis.

        Arguments
        - angle: the angle in radians

        Returns
        - this
        """
        ...


    def rotateY(self, angle: float, dest: "Vector4f") -> "Vector4f":
        ...


    def rotateZ(self, angle: float) -> "Vector4f":
        """
        Rotate this vector the specified radians around the Z axis.

        Arguments
        - angle: the angle in radians

        Returns
        - this
        """
        ...


    def rotateZ(self, angle: float, dest: "Vector4f") -> "Vector4f":
        ...


    def lengthSquared(self) -> float:
        ...


    @staticmethod
    def lengthSquared(x: float, y: float, z: float, w: float) -> float:
        """
        Get the length squared of a 4-dimensional single-precision vector.

    Author(s)
        - F. Neurath

        Arguments
        - x: the vector's x component
        - y: the vector's y component
        - z: the vector's z component
        - w: the vector's w component

        Returns
        - the length squared of the given vector
        """
        ...


    @staticmethod
    def lengthSquared(x: int, y: int, z: int, w: int) -> float:
        """
        Get the length squared of a 4-dimensional int vector.

        Arguments
        - x: the vector's x component
        - y: the vector's y component
        - z: the vector's z component
        - w: the vector's w component

        Returns
        - the length squared of the given vector
        """
        ...


    def length(self) -> float:
        ...


    @staticmethod
    def length(x: float, y: float, z: float, w: float) -> float:
        """
        Get the length of a 4-dimensional single-precision vector.

    Author(s)
        - F. Neurath

        Arguments
        - x: The vector's x component
        - y: The vector's y component
        - z: The vector's z component
        - w: The vector's w component

        Returns
        - the length of the given vector
        """
        ...


    def normalize(self) -> "Vector4f":
        """
        Normalizes this vector.

        Returns
        - this
        """
        ...


    def normalize(self, dest: "Vector4f") -> "Vector4f":
        ...


    def normalize(self, length: float) -> "Vector4f":
        """
        Scale this vector to have the given length.

        Arguments
        - length: the desired length

        Returns
        - this
        """
        ...


    def normalize(self, length: float, dest: "Vector4f") -> "Vector4f":
        ...


    def normalize3(self) -> "Vector4f":
        """
        Normalize this vector by computing only the norm of `(x, y, z)`.

        Returns
        - this
        """
        ...


    def normalize3(self, dest: "Vector4f") -> "Vector4f":
        ...


    def distance(self, v: "Vector4fc") -> float:
        ...


    def distance(self, x: float, y: float, z: float, w: float) -> float:
        ...


    def distanceSquared(self, v: "Vector4fc") -> float:
        ...


    def distanceSquared(self, x: float, y: float, z: float, w: float) -> float:
        ...


    @staticmethod
    def distance(x1: float, y1: float, z1: float, w1: float, x2: float, y2: float, z2: float, w2: float) -> float:
        """
        Return the distance between `(x1, y1, z1, w1)` and `(x2, y2, z2, w2)`.

        Arguments
        - x1: the x component of the first vector
        - y1: the y component of the first vector
        - z1: the z component of the first vector
        - w1: the w component of the first vector
        - x2: the x component of the second vector
        - y2: the y component of the second vector
        - z2: the z component of the second vector
        - w2: the 2 component of the second vector

        Returns
        - the euclidean distance
        """
        ...


    @staticmethod
    def distanceSquared(x1: float, y1: float, z1: float, w1: float, x2: float, y2: float, z2: float, w2: float) -> float:
        """
        Return the squared distance between `(x1, y1, z1, w1)` and `(x2, y2, z2, w2)`.

        Arguments
        - x1: the x component of the first vector
        - y1: the y component of the first vector
        - z1: the z component of the first vector
        - w1: the w component of the first vector
        - x2: the x component of the second vector
        - y2: the y component of the second vector
        - z2: the z component of the second vector
        - w2: the w component of the second vector

        Returns
        - the euclidean distance squared
        """
        ...


    def dot(self, v: "Vector4fc") -> float:
        ...


    def dot(self, x: float, y: float, z: float, w: float) -> float:
        ...


    def angleCos(self, v: "Vector4fc") -> float:
        ...


    def angle(self, v: "Vector4fc") -> float:
        ...


    def zero(self) -> "Vector4f":
        """
        Set all components to zero.

        Returns
        - this
        """
        ...


    def negate(self) -> "Vector4f":
        """
        Negate this vector.

        Returns
        - this
        """
        ...


    def negate(self, dest: "Vector4f") -> "Vector4f":
        ...


    def toString(self) -> str:
        """
        Return a string representation of this vector.
        
        This method creates a new DecimalFormat on every invocation with the format string "`0.000E0;-`".

        Returns
        - the string representation
        """
        ...


    def toString(self, formatter: "NumberFormat") -> str:
        """
        Return a string representation of this vector by formatting the vector components with the given NumberFormat.

        Arguments
        - formatter: the NumberFormat used to format the vector components with

        Returns
        - the string representation
        """
        ...


    def writeExternal(self, out: "ObjectOutput") -> None:
        ...


    def readExternal(self, in: "ObjectInput") -> None:
        ...


    def min(self, v: "Vector4fc") -> "Vector4f":
        """
        Set the components of this vector to be the component-wise minimum of this and the other vector.

        Arguments
        - v: the other vector

        Returns
        - this
        """
        ...


    def min(self, v: "Vector4fc", dest: "Vector4f") -> "Vector4f":
        ...


    def max(self, v: "Vector4fc") -> "Vector4f":
        """
        Set the components of this vector to be the component-wise maximum of this and the other vector.

        Arguments
        - v: the other vector

        Returns
        - this
        """
        ...


    def max(self, v: "Vector4fc", dest: "Vector4f") -> "Vector4f":
        ...


    def hashCode(self) -> int:
        ...


    def equals(self, obj: "Object") -> bool:
        ...


    def equals(self, v: "Vector4fc", delta: float) -> bool:
        ...


    def equals(self, x: float, y: float, z: float, w: float) -> bool:
        ...


    def smoothStep(self, v: "Vector4fc", t: float, dest: "Vector4f") -> "Vector4f":
        ...


    def hermite(self, t0: "Vector4fc", v1: "Vector4fc", t1: "Vector4fc", t: float, dest: "Vector4f") -> "Vector4f":
        ...


    def lerp(self, other: "Vector4fc", t: float) -> "Vector4f":
        """
        Linearly interpolate `this` and `other` using the given interpolation factor `t`
        and store the result in `this`.
        
        If `t` is `0.0` then the result is `this`. If the interpolation factor is `1.0`
        then the result is `other`.

        Arguments
        - other: the other vector
        - t: the interpolation factor between 0.0 and 1.0

        Returns
        - this
        """
        ...


    def lerp(self, other: "Vector4fc", t: float, dest: "Vector4f") -> "Vector4f":
        ...


    def get(self, component: int) -> float:
        ...


    def get(self, mode: int, dest: "Vector4i") -> "Vector4i":
        ...


    def get(self, dest: "Vector4f") -> "Vector4f":
        ...


    def get(self, dest: "Vector4d") -> "Vector4d":
        ...


    def maxComponent(self) -> int:
        ...


    def minComponent(self) -> int:
        ...


    def floor(self) -> "Vector4f":
        """
        Set each component of this vector to the largest (closest to positive
        infinity) `float` value that is less than or equal to that
        component and is equal to a mathematical integer.

        Returns
        - this
        """
        ...


    def floor(self, dest: "Vector4f") -> "Vector4f":
        ...


    def ceil(self) -> "Vector4f":
        """
        Set each component of this vector to the smallest (closest to negative
        infinity) `float` value that is greater than or equal to that
        component and is equal to a mathematical integer.

        Returns
        - this
        """
        ...


    def ceil(self, dest: "Vector4f") -> "Vector4f":
        ...


    def round(self) -> "Vector4f":
        """
        Set each component of this vector to the closest float that is equal to
        a mathematical integer, with ties rounding to positive infinity.

        Returns
        - this
        """
        ...


    def round(self, dest: "Vector4f") -> "Vector4f":
        ...


    def isFinite(self) -> bool:
        ...


    def absolute(self) -> "Vector4f":
        """
        Compute the absolute of each of this vector's components.

        Returns
        - this
        """
        ...


    def absolute(self, dest: "Vector4f") -> "Vector4f":
        ...


    def clone(self) -> "Object":
        ...
