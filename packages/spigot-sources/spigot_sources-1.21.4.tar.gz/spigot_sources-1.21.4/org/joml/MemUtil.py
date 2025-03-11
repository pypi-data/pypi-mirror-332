"""
Python module generated from Java source file org.joml.MemUtil

Java source file obtained from artifact joml version 1.10.8

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.lang.reflect import Field
from org.joml import *
from typing import Any, Callable, Iterable, Tuple


class MemUtil:
    """
    Helper class to do efficient memory operations on all JOML objects, NIO buffers and primitive arrays.
    This class is used internally throughout JOML, is undocumented and is subject to change.
    Use with extreme caution!

    Author(s)
    - Kai Burjack
    """

    INSTANCE = createInstance()


    def put(self, m: "Matrix4f", offset: int, dest: "FloatBuffer") -> None:
        ...


    def put(self, m: "Matrix4f", offset: int, dest: "ByteBuffer") -> None:
        ...


    def put(self, m: "Matrix4x3f", offset: int, dest: "FloatBuffer") -> None:
        ...


    def put(self, m: "Matrix4x3f", offset: int, dest: "ByteBuffer") -> None:
        ...


    def put4x4(self, m: "Matrix4x3f", offset: int, dest: "FloatBuffer") -> None:
        ...


    def put4x4(self, m: "Matrix4x3f", offset: int, dest: "ByteBuffer") -> None:
        ...


    def put4x4(self, m: "Matrix4x3d", offset: int, dest: "DoubleBuffer") -> None:
        ...


    def put4x4(self, m: "Matrix4x3d", offset: int, dest: "ByteBuffer") -> None:
        ...


    def put4x4(self, m: "Matrix3x2f", offset: int, dest: "FloatBuffer") -> None:
        ...


    def put4x4(self, m: "Matrix3x2f", offset: int, dest: "ByteBuffer") -> None:
        ...


    def put4x4(self, m: "Matrix3x2d", offset: int, dest: "DoubleBuffer") -> None:
        ...


    def put4x4(self, m: "Matrix3x2d", offset: int, dest: "ByteBuffer") -> None:
        ...


    def put3x3(self, m: "Matrix3x2f", offset: int, dest: "FloatBuffer") -> None:
        ...


    def put3x3(self, m: "Matrix3x2f", offset: int, dest: "ByteBuffer") -> None:
        ...


    def put3x3(self, m: "Matrix3x2d", offset: int, dest: "DoubleBuffer") -> None:
        ...


    def put3x3(self, m: "Matrix3x2d", offset: int, dest: "ByteBuffer") -> None:
        ...


    def put4x3(self, m: "Matrix4f", offset: int, dest: "FloatBuffer") -> None:
        ...


    def put4x3(self, m: "Matrix4f", offset: int, dest: "ByteBuffer") -> None:
        ...


    def put3x4(self, m: "Matrix4f", offset: int, dest: "FloatBuffer") -> None:
        ...


    def put3x4(self, m: "Matrix4f", offset: int, dest: "ByteBuffer") -> None:
        ...


    def put3x4(self, m: "Matrix4x3f", offset: int, dest: "FloatBuffer") -> None:
        ...


    def put3x4(self, m: "Matrix4x3f", offset: int, dest: "ByteBuffer") -> None:
        ...


    def put3x4(self, m: "Matrix3f", offset: int, dest: "FloatBuffer") -> None:
        ...


    def put3x4(self, m: "Matrix3f", offset: int, dest: "ByteBuffer") -> None:
        ...


    def putTransposed(self, m: "Matrix4f", offset: int, dest: "FloatBuffer") -> None:
        ...


    def putTransposed(self, m: "Matrix4f", offset: int, dest: "ByteBuffer") -> None:
        ...


    def put4x3Transposed(self, m: "Matrix4f", offset: int, dest: "FloatBuffer") -> None:
        ...


    def put4x3Transposed(self, m: "Matrix4f", offset: int, dest: "ByteBuffer") -> None:
        ...


    def putTransposed(self, m: "Matrix4x3f", offset: int, dest: "FloatBuffer") -> None:
        ...


    def putTransposed(self, m: "Matrix4x3f", offset: int, dest: "ByteBuffer") -> None:
        ...


    def putTransposed(self, m: "Matrix3x2f", offset: int, dest: "FloatBuffer") -> None:
        ...


    def putTransposed(self, m: "Matrix3f", offset: int, dest: "FloatBuffer") -> None:
        ...


    def putTransposed(self, m: "Matrix3f", offset: int, dest: "ByteBuffer") -> None:
        ...


    def putTransposed(self, m: "Matrix2f", offset: int, dest: "FloatBuffer") -> None:
        ...


    def putTransposed(self, m: "Matrix2f", offset: int, dest: "ByteBuffer") -> None:
        ...


    def put(self, m: "Matrix4d", offset: int, dest: "DoubleBuffer") -> None:
        ...


    def put(self, m: "Matrix4d", offset: int, dest: "ByteBuffer") -> None:
        ...


    def put(self, m: "Matrix4x3d", offset: int, dest: "DoubleBuffer") -> None:
        ...


    def put(self, m: "Matrix4x3d", offset: int, dest: "ByteBuffer") -> None:
        ...


    def putf(self, m: "Matrix4d", offset: int, dest: "FloatBuffer") -> None:
        ...


    def putf(self, m: "Matrix4d", offset: int, dest: "ByteBuffer") -> None:
        ...


    def putf(self, m: "Matrix4x3d", offset: int, dest: "FloatBuffer") -> None:
        ...


    def putf(self, m: "Matrix4x3d", offset: int, dest: "ByteBuffer") -> None:
        ...


    def put4x3Transposed(self, m: "Matrix4d", offset: int, dest: "DoubleBuffer") -> None:
        ...


    def put4x3Transposed(self, m: "Matrix4d", offset: int, dest: "ByteBuffer") -> None:
        ...


    def putTransposed(self, m: "Matrix4d", offset: int, dest: "DoubleBuffer") -> None:
        ...


    def putTransposed(self, m: "Matrix4d", offset: int, dest: "ByteBuffer") -> None:
        ...


    def putTransposed(self, m: "Matrix4x3d", offset: int, dest: "DoubleBuffer") -> None:
        ...


    def putTransposed(self, m: "Matrix4x3d", offset: int, dest: "ByteBuffer") -> None:
        ...


    def putTransposed(self, m: "Matrix3d", offset: int, dest: "DoubleBuffer") -> None:
        ...


    def putTransposed(self, m: "Matrix3d", offset: int, dest: "ByteBuffer") -> None:
        ...


    def putTransposed(self, m: "Matrix3x2d", offset: int, dest: "DoubleBuffer") -> None:
        ...


    def putTransposed(self, m: "Matrix3x2d", offset: int, dest: "ByteBuffer") -> None:
        ...


    def putTransposed(self, m: "Matrix2d", offset: int, dest: "DoubleBuffer") -> None:
        ...


    def putTransposed(self, m: "Matrix2d", offset: int, dest: "ByteBuffer") -> None:
        ...


    def putfTransposed(self, m: "Matrix4d", offset: int, dest: "FloatBuffer") -> None:
        ...


    def putfTransposed(self, m: "Matrix4d", offset: int, dest: "ByteBuffer") -> None:
        ...


    def putfTransposed(self, m: "Matrix4x3d", offset: int, dest: "FloatBuffer") -> None:
        ...


    def putfTransposed(self, m: "Matrix4x3d", offset: int, dest: "ByteBuffer") -> None:
        ...


    def putfTransposed(self, m: "Matrix3d", offset: int, dest: "FloatBuffer") -> None:
        ...


    def putfTransposed(self, m: "Matrix3d", offset: int, dest: "ByteBuffer") -> None:
        ...


    def putfTransposed(self, m: "Matrix3x2d", offset: int, dest: "FloatBuffer") -> None:
        ...


    def putfTransposed(self, m: "Matrix3x2d", offset: int, dest: "ByteBuffer") -> None:
        ...


    def putfTransposed(self, m: "Matrix2d", offset: int, dest: "FloatBuffer") -> None:
        ...


    def putfTransposed(self, m: "Matrix2d", offset: int, dest: "ByteBuffer") -> None:
        ...


    def put(self, m: "Matrix3f", offset: int, dest: "FloatBuffer") -> None:
        ...


    def put(self, m: "Matrix3f", offset: int, dest: "ByteBuffer") -> None:
        ...


    def put(self, m: "Matrix3d", offset: int, dest: "DoubleBuffer") -> None:
        ...


    def put(self, m: "Matrix3d", offset: int, dest: "ByteBuffer") -> None:
        ...


    def putf(self, m: "Matrix3d", offset: int, dest: "FloatBuffer") -> None:
        ...


    def putf(self, m: "Matrix3d", offset: int, dest: "ByteBuffer") -> None:
        ...


    def put(self, m: "Matrix3x2f", offset: int, dest: "FloatBuffer") -> None:
        ...


    def put(self, m: "Matrix3x2f", offset: int, dest: "ByteBuffer") -> None:
        ...


    def put(self, m: "Matrix3x2d", offset: int, dest: "DoubleBuffer") -> None:
        ...


    def put(self, m: "Matrix3x2d", offset: int, dest: "ByteBuffer") -> None:
        ...


    def put(self, m: "Matrix2f", offset: int, dest: "FloatBuffer") -> None:
        ...


    def put(self, m: "Matrix2f", offset: int, dest: "ByteBuffer") -> None:
        ...


    def put(self, m: "Matrix2d", offset: int, dest: "DoubleBuffer") -> None:
        ...


    def put(self, m: "Matrix2d", offset: int, dest: "ByteBuffer") -> None:
        ...


    def putf(self, m: "Matrix2d", offset: int, dest: "FloatBuffer") -> None:
        ...


    def putf(self, m: "Matrix2d", offset: int, dest: "ByteBuffer") -> None:
        ...


    def put(self, src: "Vector4d", offset: int, dest: "DoubleBuffer") -> None:
        ...


    def put(self, src: "Vector4d", offset: int, dest: "FloatBuffer") -> None:
        ...


    def put(self, src: "Vector4d", offset: int, dest: "ByteBuffer") -> None:
        ...


    def putf(self, src: "Vector4d", offset: int, dest: "ByteBuffer") -> None:
        ...


    def put(self, src: "Vector4f", offset: int, dest: "FloatBuffer") -> None:
        ...


    def put(self, src: "Vector4f", offset: int, dest: "ByteBuffer") -> None:
        ...


    def put(self, src: "Vector4i", offset: int, dest: "IntBuffer") -> None:
        ...


    def put(self, src: "Vector4i", offset: int, dest: "ByteBuffer") -> None:
        ...


    def put(self, src: "Vector4L", offset: int, dest: "LongBuffer") -> None:
        ...


    def put(self, src: "Vector4L", offset: int, dest: "ByteBuffer") -> None:
        ...


    def put(self, src: "Vector3f", offset: int, dest: "FloatBuffer") -> None:
        ...


    def put(self, src: "Vector3f", offset: int, dest: "ByteBuffer") -> None:
        ...


    def put(self, src: "Vector3d", offset: int, dest: "DoubleBuffer") -> None:
        ...


    def put(self, src: "Vector3d", offset: int, dest: "FloatBuffer") -> None:
        ...


    def put(self, src: "Vector3d", offset: int, dest: "ByteBuffer") -> None:
        ...


    def putf(self, src: "Vector3d", offset: int, dest: "ByteBuffer") -> None:
        ...


    def put(self, src: "Vector3i", offset: int, dest: "IntBuffer") -> None:
        ...


    def put(self, src: "Vector3i", offset: int, dest: "ByteBuffer") -> None:
        ...


    def put(self, src: "Vector3L", offset: int, dest: "LongBuffer") -> None:
        ...


    def put(self, src: "Vector3L", offset: int, dest: "ByteBuffer") -> None:
        ...


    def put(self, src: "Vector2f", offset: int, dest: "FloatBuffer") -> None:
        ...


    def put(self, src: "Vector2f", offset: int, dest: "ByteBuffer") -> None:
        ...


    def put(self, src: "Vector2d", offset: int, dest: "DoubleBuffer") -> None:
        ...


    def put(self, src: "Vector2d", offset: int, dest: "ByteBuffer") -> None:
        ...


    def put(self, src: "Vector2i", offset: int, dest: "IntBuffer") -> None:
        ...


    def put(self, src: "Vector2i", offset: int, dest: "ByteBuffer") -> None:
        ...


    def put(self, src: "Vector2L", offset: int, dest: "LongBuffer") -> None:
        ...


    def put(self, src: "Vector2L", offset: int, dest: "ByteBuffer") -> None:
        ...


    def get(self, m: "Matrix4f", offset: int, src: "FloatBuffer") -> None:
        ...


    def get(self, m: "Matrix4f", offset: int, src: "ByteBuffer") -> None:
        ...


    def getTransposed(self, m: "Matrix4f", offset: int, src: "FloatBuffer") -> None:
        ...


    def getTransposed(self, m: "Matrix4f", offset: int, src: "ByteBuffer") -> None:
        ...


    def get(self, m: "Matrix4x3f", offset: int, src: "FloatBuffer") -> None:
        ...


    def get(self, m: "Matrix4x3f", offset: int, src: "ByteBuffer") -> None:
        ...


    def get(self, m: "Matrix4d", offset: int, src: "DoubleBuffer") -> None:
        ...


    def get(self, m: "Matrix4d", offset: int, src: "ByteBuffer") -> None:
        ...


    def get(self, m: "Matrix4x3d", offset: int, src: "DoubleBuffer") -> None:
        ...


    def get(self, m: "Matrix4x3d", offset: int, src: "ByteBuffer") -> None:
        ...


    def getf(self, m: "Matrix4d", offset: int, src: "FloatBuffer") -> None:
        ...


    def getf(self, m: "Matrix4d", offset: int, src: "ByteBuffer") -> None:
        ...


    def getf(self, m: "Matrix4x3d", offset: int, src: "FloatBuffer") -> None:
        ...


    def getf(self, m: "Matrix4x3d", offset: int, src: "ByteBuffer") -> None:
        ...


    def get(self, m: "Matrix3f", offset: int, src: "FloatBuffer") -> None:
        ...


    def get(self, m: "Matrix3f", offset: int, src: "ByteBuffer") -> None:
        ...


    def get(self, m: "Matrix3d", offset: int, src: "DoubleBuffer") -> None:
        ...


    def get(self, m: "Matrix3d", offset: int, src: "ByteBuffer") -> None:
        ...


    def get(self, m: "Matrix3x2f", offset: int, src: "FloatBuffer") -> None:
        ...


    def get(self, m: "Matrix3x2f", offset: int, src: "ByteBuffer") -> None:
        ...


    def get(self, m: "Matrix3x2d", offset: int, src: "DoubleBuffer") -> None:
        ...


    def get(self, m: "Matrix3x2d", offset: int, src: "ByteBuffer") -> None:
        ...


    def getf(self, m: "Matrix3d", offset: int, src: "FloatBuffer") -> None:
        ...


    def getf(self, m: "Matrix3d", offset: int, src: "ByteBuffer") -> None:
        ...


    def get(self, m: "Matrix2f", offset: int, src: "FloatBuffer") -> None:
        ...


    def get(self, m: "Matrix2f", offset: int, src: "ByteBuffer") -> None:
        ...


    def get(self, m: "Matrix2d", offset: int, src: "DoubleBuffer") -> None:
        ...


    def get(self, m: "Matrix2d", offset: int, src: "ByteBuffer") -> None:
        ...


    def getf(self, m: "Matrix2d", offset: int, src: "FloatBuffer") -> None:
        ...


    def getf(self, m: "Matrix2d", offset: int, src: "ByteBuffer") -> None:
        ...


    def get(self, dst: "Vector4d", offset: int, src: "DoubleBuffer") -> None:
        ...


    def get(self, dst: "Vector4d", offset: int, src: "ByteBuffer") -> None:
        ...


    def get(self, dst: "Vector4f", offset: int, src: "FloatBuffer") -> None:
        ...


    def get(self, dst: "Vector4f", offset: int, src: "ByteBuffer") -> None:
        ...


    def get(self, dst: "Vector4i", offset: int, src: "IntBuffer") -> None:
        ...


    def get(self, dst: "Vector4i", offset: int, src: "ByteBuffer") -> None:
        ...


    def get(self, dst: "Vector4L", offset: int, src: "LongBuffer") -> None:
        ...


    def get(self, dst: "Vector4L", offset: int, src: "ByteBuffer") -> None:
        ...


    def get(self, dst: "Vector3f", offset: int, src: "FloatBuffer") -> None:
        ...


    def get(self, dst: "Vector3f", offset: int, src: "ByteBuffer") -> None:
        ...


    def get(self, dst: "Vector3d", offset: int, src: "DoubleBuffer") -> None:
        ...


    def get(self, dst: "Vector3d", offset: int, src: "ByteBuffer") -> None:
        ...


    def get(self, dst: "Vector3i", offset: int, src: "IntBuffer") -> None:
        ...


    def get(self, dst: "Vector3i", offset: int, src: "ByteBuffer") -> None:
        ...


    def get(self, dst: "Vector3L", offset: int, src: "LongBuffer") -> None:
        ...


    def get(self, dst: "Vector3L", offset: int, src: "ByteBuffer") -> None:
        ...


    def get(self, dst: "Vector2f", offset: int, src: "FloatBuffer") -> None:
        ...


    def get(self, dst: "Vector2f", offset: int, src: "ByteBuffer") -> None:
        ...


    def get(self, dst: "Vector2d", offset: int, src: "DoubleBuffer") -> None:
        ...


    def get(self, dst: "Vector2d", offset: int, src: "ByteBuffer") -> None:
        ...


    def get(self, dst: "Vector2i", offset: int, src: "IntBuffer") -> None:
        ...


    def get(self, dst: "Vector2i", offset: int, src: "ByteBuffer") -> None:
        ...


    def get(self, dst: "Vector2L", offset: int, src: "LongBuffer") -> None:
        ...


    def get(self, dst: "Vector2L", offset: int, src: "ByteBuffer") -> None:
        ...


    def putMatrix3f(self, q: "Quaternionf", position: int, dest: "ByteBuffer") -> None:
        ...


    def putMatrix3f(self, q: "Quaternionf", position: int, dest: "FloatBuffer") -> None:
        ...


    def putMatrix4f(self, q: "Quaternionf", position: int, dest: "ByteBuffer") -> None:
        ...


    def putMatrix4f(self, q: "Quaternionf", position: int, dest: "FloatBuffer") -> None:
        ...


    def putMatrix4x3f(self, q: "Quaternionf", position: int, dest: "ByteBuffer") -> None:
        ...


    def putMatrix4x3f(self, q: "Quaternionf", position: int, dest: "FloatBuffer") -> None:
        ...


    def get(self, m: "Matrix4f", column: int, row: int) -> float:
        ...


    def set(self, m: "Matrix4f", column: int, row: int, v: float) -> "Matrix4f":
        ...


    def get(self, m: "Matrix4d", column: int, row: int) -> float:
        ...


    def set(self, m: "Matrix4d", column: int, row: int, v: float) -> "Matrix4d":
        ...


    def get(self, m: "Matrix3f", column: int, row: int) -> float:
        ...


    def set(self, m: "Matrix3f", column: int, row: int, v: float) -> "Matrix3f":
        ...


    def get(self, m: "Matrix3d", column: int, row: int) -> float:
        ...


    def set(self, m: "Matrix3d", column: int, row: int, v: float) -> "Matrix3d":
        ...


    def getColumn(self, m: "Matrix4f", column: int, dest: "Vector4f") -> "Vector4f":
        ...


    def setColumn(self, v: "Vector4f", column: int, dest: "Matrix4f") -> "Matrix4f":
        ...


    def setColumn(self, v: "Vector4fc", column: int, dest: "Matrix4f") -> "Matrix4f":
        ...


    def copy(self, src: "Matrix4fc", dest: "Matrix4f") -> None:
        ...


    def copy(self, src: "Matrix4x3fc", dest: "Matrix4x3f") -> None:
        ...


    def copy(self, src: "Matrix4fc", dest: "Matrix4x3f") -> None:
        ...


    def copy(self, src: "Matrix4x3fc", dest: "Matrix4f") -> None:
        ...


    def copy(self, src: "Matrix3fc", dest: "Matrix3f") -> None:
        ...


    def copy(self, src: "Matrix3fc", dest: "Matrix4f") -> None:
        ...


    def copy(self, src: "Matrix4fc", dest: "Matrix3f") -> None:
        ...


    def copy(self, src: "Matrix3fc", dest: "Matrix4x3f") -> None:
        ...


    def copy(self, src: "Matrix3x2fc", dest: "Matrix3x2f") -> None:
        ...


    def copy(self, src: "Matrix3x2dc", dest: "Matrix3x2d") -> None:
        ...


    def copy(self, src: "Matrix2fc", dest: "Matrix2f") -> None:
        ...


    def copy(self, src: "Matrix2dc", dest: "Matrix2d") -> None:
        ...


    def copy(self, src: "Matrix2fc", dest: "Matrix3f") -> None:
        ...


    def copy(self, src: "Matrix3fc", dest: "Matrix2f") -> None:
        ...


    def copy(self, src: "Matrix2fc", dest: "Matrix3x2f") -> None:
        ...


    def copy(self, src: "Matrix3x2fc", dest: "Matrix2f") -> None:
        ...


    def copy(self, src: "Matrix2dc", dest: "Matrix3d") -> None:
        ...


    def copy(self, src: "Matrix3dc", dest: "Matrix2d") -> None:
        ...


    def copy(self, src: "Matrix2dc", dest: "Matrix3x2d") -> None:
        ...


    def copy(self, src: "Matrix3x2dc", dest: "Matrix2d") -> None:
        ...


    def copy3x3(self, src: "Matrix4fc", dest: "Matrix4f") -> None:
        ...


    def copy3x3(self, src: "Matrix4x3fc", dest: "Matrix4x3f") -> None:
        ...


    def copy3x3(self, src: "Matrix3fc", dest: "Matrix4x3f") -> None:
        ...


    def copy3x3(self, src: "Matrix3fc", dest: "Matrix4f") -> None:
        ...


    def copy4x3(self, src: "Matrix4fc", dest: "Matrix4f") -> None:
        ...


    def copy4x3(self, src: "Matrix4x3fc", dest: "Matrix4f") -> None:
        ...


    def copy(self, arr: list[float], off: int, dest: "Matrix4f") -> None:
        ...


    def copyTransposed(self, arr: list[float], off: int, dest: "Matrix4f") -> None:
        ...


    def copy(self, arr: list[float], off: int, dest: "Matrix3f") -> None:
        ...


    def copy(self, arr: list[float], off: int, dest: "Matrix4x3f") -> None:
        ...


    def copy(self, arr: list[float], off: int, dest: "Matrix3x2f") -> None:
        ...


    def copy(self, arr: list[float], off: int, dest: "Matrix3x2d") -> None:
        ...


    def copy(self, arr: list[float], off: int, dest: "Matrix3x2d") -> None:
        ...


    def copy(self, arr: list[float], off: int, dest: "Matrix2f") -> None:
        ...


    def copy(self, arr: list[float], off: int, dest: "Matrix2d") -> None:
        ...


    def copy(self, src: "Matrix4fc", dest: list[float], off: int) -> None:
        ...


    def copy(self, src: "Matrix3fc", dest: list[float], off: int) -> None:
        ...


    def copy(self, src: "Matrix4x3fc", dest: list[float], off: int) -> None:
        ...


    def copy(self, src: "Matrix3x2fc", dest: list[float], off: int) -> None:
        ...


    def copy(self, src: "Matrix3x2dc", dest: list[float], off: int) -> None:
        ...


    def copy(self, src: "Matrix2fc", dest: list[float], off: int) -> None:
        ...


    def copy(self, src: "Matrix2dc", dest: list[float], off: int) -> None:
        ...


    def copy4x4(self, src: "Matrix4x3fc", dest: list[float], off: int) -> None:
        ...


    def copy4x4(self, src: "Matrix4x3dc", dest: list[float], off: int) -> None:
        ...


    def copy4x4(self, src: "Matrix4x3dc", dest: list[float], off: int) -> None:
        ...


    def copy4x4(self, src: "Matrix3x2fc", dest: list[float], off: int) -> None:
        ...


    def copy4x4(self, src: "Matrix3x2dc", dest: list[float], off: int) -> None:
        ...


    def copy3x3(self, src: "Matrix3x2fc", dest: list[float], off: int) -> None:
        ...


    def copy3x3(self, src: "Matrix3x2dc", dest: list[float], off: int) -> None:
        ...


    def identity(self, dest: "Matrix4f") -> None:
        ...


    def identity(self, dest: "Matrix4x3f") -> None:
        ...


    def identity(self, dest: "Matrix3f") -> None:
        ...


    def identity(self, dest: "Matrix3x2f") -> None:
        ...


    def identity(self, dest: "Matrix3x2d") -> None:
        ...


    def identity(self, dest: "Matrix2f") -> None:
        ...


    def swap(self, m1: "Matrix4f", m2: "Matrix4f") -> None:
        ...


    def swap(self, m1: "Matrix4x3f", m2: "Matrix4x3f") -> None:
        ...


    def swap(self, m1: "Matrix3f", m2: "Matrix3f") -> None:
        ...


    def swap(self, m1: "Matrix2f", m2: "Matrix2f") -> None:
        ...


    def swap(self, m1: "Matrix2d", m2: "Matrix2d") -> None:
        ...


    def zero(self, dest: "Matrix4f") -> None:
        ...


    def zero(self, dest: "Matrix4x3f") -> None:
        ...


    def zero(self, dest: "Matrix3f") -> None:
        ...


    def zero(self, dest: "Matrix3x2f") -> None:
        ...


    def zero(self, dest: "Matrix3x2d") -> None:
        ...


    def zero(self, dest: "Matrix2f") -> None:
        ...


    def zero(self, dest: "Matrix2d") -> None:
        ...


    class MemUtilNIO(MemUtil):

        def put0(self, m: "Matrix4f", dest: "FloatBuffer") -> None:
            ...


        def putN(self, m: "Matrix4f", offset: int, dest: "FloatBuffer") -> None:
            ...


        def put(self, m: "Matrix4f", offset: int, dest: "FloatBuffer") -> None:
            ...


        def put0(self, m: "Matrix4f", dest: "ByteBuffer") -> None:
            ...


        def put(self, m: "Matrix4f", offset: int, dest: "ByteBuffer") -> None:
            ...


        def put4x3_0(self, m: "Matrix4f", dest: "FloatBuffer") -> None:
            ...


        def put4x3_N(self, m: "Matrix4f", offset: int, dest: "FloatBuffer") -> None:
            ...


        def put4x3(self, m: "Matrix4f", offset: int, dest: "FloatBuffer") -> None:
            ...


        def put4x3_0(self, m: "Matrix4f", dest: "ByteBuffer") -> None:
            ...


        def put4x3(self, m: "Matrix4f", offset: int, dest: "ByteBuffer") -> None:
            ...


        def put3x4_0(self, m: "Matrix4f", dest: "ByteBuffer") -> None:
            ...


        def put3x4(self, m: "Matrix4f", offset: int, dest: "ByteBuffer") -> None:
            ...


        def put3x4_0(self, m: "Matrix4f", dest: "FloatBuffer") -> None:
            ...


        def put3x4_N(self, m: "Matrix4f", offset: int, dest: "FloatBuffer") -> None:
            ...


        def put3x4(self, m: "Matrix4f", offset: int, dest: "FloatBuffer") -> None:
            ...


        def put3x4_0(self, m: "Matrix4x3f", dest: "ByteBuffer") -> None:
            ...


        def put3x4(self, m: "Matrix4x3f", offset: int, dest: "ByteBuffer") -> None:
            ...


        def put3x4_0(self, m: "Matrix4x3f", dest: "FloatBuffer") -> None:
            ...


        def put3x4_N(self, m: "Matrix4x3f", offset: int, dest: "FloatBuffer") -> None:
            ...


        def put3x4(self, m: "Matrix4x3f", offset: int, dest: "FloatBuffer") -> None:
            ...


        def put0(self, m: "Matrix4x3f", dest: "FloatBuffer") -> None:
            ...


        def putN(self, m: "Matrix4x3f", offset: int, dest: "FloatBuffer") -> None:
            ...


        def put(self, m: "Matrix4x3f", offset: int, dest: "FloatBuffer") -> None:
            ...


        def put0(self, m: "Matrix4x3f", dest: "ByteBuffer") -> None:
            ...


        def putN(self, m: "Matrix4x3f", offset: int, dest: "ByteBuffer") -> None:
            ...


        def put(self, m: "Matrix4x3f", offset: int, dest: "ByteBuffer") -> None:
            ...


        def put4x4(self, m: "Matrix4x3f", offset: int, dest: "FloatBuffer") -> None:
            ...


        def put4x4(self, m: "Matrix4x3f", offset: int, dest: "ByteBuffer") -> None:
            ...


        def put4x4(self, m: "Matrix4x3d", offset: int, dest: "DoubleBuffer") -> None:
            ...


        def put4x4(self, m: "Matrix4x3d", offset: int, dest: "ByteBuffer") -> None:
            ...


        def put4x4(self, m: "Matrix3x2f", offset: int, dest: "FloatBuffer") -> None:
            ...


        def put4x4(self, m: "Matrix3x2f", offset: int, dest: "ByteBuffer") -> None:
            ...


        def put4x4(self, m: "Matrix3x2d", offset: int, dest: "DoubleBuffer") -> None:
            ...


        def put4x4(self, m: "Matrix3x2d", offset: int, dest: "ByteBuffer") -> None:
            ...


        def put3x3(self, m: "Matrix3x2f", offset: int, dest: "FloatBuffer") -> None:
            ...


        def put3x3(self, m: "Matrix3x2f", offset: int, dest: "ByteBuffer") -> None:
            ...


        def put3x3(self, m: "Matrix3x2d", offset: int, dest: "DoubleBuffer") -> None:
            ...


        def put3x3(self, m: "Matrix3x2d", offset: int, dest: "ByteBuffer") -> None:
            ...


        def putTransposed(self, m: "Matrix4f", offset: int, dest: "FloatBuffer") -> None:
            ...


        def putTransposed(self, m: "Matrix4f", offset: int, dest: "ByteBuffer") -> None:
            ...


        def put4x3Transposed(self, m: "Matrix4f", offset: int, dest: "FloatBuffer") -> None:
            ...


        def put4x3Transposed(self, m: "Matrix4f", offset: int, dest: "ByteBuffer") -> None:
            ...


        def putTransposed(self, m: "Matrix4x3f", offset: int, dest: "FloatBuffer") -> None:
            ...


        def putTransposed(self, m: "Matrix4x3f", offset: int, dest: "ByteBuffer") -> None:
            ...


        def putTransposed(self, m: "Matrix3f", offset: int, dest: "FloatBuffer") -> None:
            ...


        def putTransposed(self, m: "Matrix3f", offset: int, dest: "ByteBuffer") -> None:
            ...


        def putTransposed(self, m: "Matrix2f", offset: int, dest: "FloatBuffer") -> None:
            ...


        def putTransposed(self, m: "Matrix3x2f", offset: int, dest: "FloatBuffer") -> None:
            ...


        def putTransposed(self, m: "Matrix2f", offset: int, dest: "ByteBuffer") -> None:
            ...


        def put(self, m: "Matrix4d", offset: int, dest: "DoubleBuffer") -> None:
            ...


        def put(self, m: "Matrix4d", offset: int, dest: "ByteBuffer") -> None:
            ...


        def put(self, m: "Matrix4x3d", offset: int, dest: "DoubleBuffer") -> None:
            ...


        def put(self, m: "Matrix4x3d", offset: int, dest: "ByteBuffer") -> None:
            ...


        def putf(self, m: "Matrix4d", offset: int, dest: "FloatBuffer") -> None:
            ...


        def putf(self, m: "Matrix4d", offset: int, dest: "ByteBuffer") -> None:
            ...


        def putf(self, m: "Matrix4x3d", offset: int, dest: "FloatBuffer") -> None:
            ...


        def putf(self, m: "Matrix4x3d", offset: int, dest: "ByteBuffer") -> None:
            ...


        def putTransposed(self, m: "Matrix4d", offset: int, dest: "DoubleBuffer") -> None:
            ...


        def putTransposed(self, m: "Matrix4d", offset: int, dest: "ByteBuffer") -> None:
            ...


        def put4x3Transposed(self, m: "Matrix4d", offset: int, dest: "DoubleBuffer") -> None:
            ...


        def put4x3Transposed(self, m: "Matrix4d", offset: int, dest: "ByteBuffer") -> None:
            ...


        def putTransposed(self, m: "Matrix4x3d", offset: int, dest: "DoubleBuffer") -> None:
            ...


        def putTransposed(self, m: "Matrix4x3d", offset: int, dest: "ByteBuffer") -> None:
            ...


        def putTransposed(self, m: "Matrix3d", offset: int, dest: "DoubleBuffer") -> None:
            ...


        def putTransposed(self, m: "Matrix3d", offset: int, dest: "ByteBuffer") -> None:
            ...


        def putTransposed(self, m: "Matrix3x2d", offset: int, dest: "ByteBuffer") -> None:
            ...


        def putTransposed(self, m: "Matrix3x2d", offset: int, dest: "DoubleBuffer") -> None:
            ...


        def putTransposed(self, m: "Matrix2d", offset: int, dest: "DoubleBuffer") -> None:
            ...


        def putTransposed(self, m: "Matrix2d", offset: int, dest: "ByteBuffer") -> None:
            ...


        def putfTransposed(self, m: "Matrix4x3d", offset: int, dest: "FloatBuffer") -> None:
            ...


        def putfTransposed(self, m: "Matrix4x3d", offset: int, dest: "ByteBuffer") -> None:
            ...


        def putfTransposed(self, m: "Matrix3d", offset: int, dest: "FloatBuffer") -> None:
            ...


        def putfTransposed(self, m: "Matrix3d", offset: int, dest: "ByteBuffer") -> None:
            ...


        def putfTransposed(self, m: "Matrix3x2d", offset: int, dest: "FloatBuffer") -> None:
            ...


        def putfTransposed(self, m: "Matrix3x2d", offset: int, dest: "ByteBuffer") -> None:
            ...


        def putfTransposed(self, m: "Matrix2d", offset: int, dest: "FloatBuffer") -> None:
            ...


        def putfTransposed(self, m: "Matrix2d", offset: int, dest: "ByteBuffer") -> None:
            ...


        def putfTransposed(self, m: "Matrix4d", offset: int, dest: "FloatBuffer") -> None:
            ...


        def putfTransposed(self, m: "Matrix4d", offset: int, dest: "ByteBuffer") -> None:
            ...


        def put0(self, m: "Matrix3f", dest: "FloatBuffer") -> None:
            ...


        def putN(self, m: "Matrix3f", offset: int, dest: "FloatBuffer") -> None:
            ...


        def put(self, m: "Matrix3f", offset: int, dest: "FloatBuffer") -> None:
            ...


        def put0(self, m: "Matrix3f", dest: "ByteBuffer") -> None:
            ...


        def putN(self, m: "Matrix3f", offset: int, dest: "ByteBuffer") -> None:
            ...


        def put(self, m: "Matrix3f", offset: int, dest: "ByteBuffer") -> None:
            ...


        def put3x4_0(self, m: "Matrix3f", dest: "ByteBuffer") -> None:
            ...


        def put3x4(self, m: "Matrix3f", offset: int, dest: "ByteBuffer") -> None:
            ...


        def put3x4_0(self, m: "Matrix3f", dest: "FloatBuffer") -> None:
            ...


        def put3x4_N(self, m: "Matrix3f", offset: int, dest: "FloatBuffer") -> None:
            ...


        def put3x4(self, m: "Matrix3f", offset: int, dest: "FloatBuffer") -> None:
            ...


        def put(self, m: "Matrix3d", offset: int, dest: "DoubleBuffer") -> None:
            ...


        def put(self, m: "Matrix3d", offset: int, dest: "ByteBuffer") -> None:
            ...


        def put(self, m: "Matrix3x2f", offset: int, dest: "FloatBuffer") -> None:
            ...


        def put(self, m: "Matrix3x2f", offset: int, dest: "ByteBuffer") -> None:
            ...


        def put(self, m: "Matrix3x2d", offset: int, dest: "DoubleBuffer") -> None:
            ...


        def put(self, m: "Matrix3x2d", offset: int, dest: "ByteBuffer") -> None:
            ...


        def putf(self, m: "Matrix3d", offset: int, dest: "FloatBuffer") -> None:
            ...


        def put(self, m: "Matrix2f", offset: int, dest: "FloatBuffer") -> None:
            ...


        def put(self, m: "Matrix2f", offset: int, dest: "ByteBuffer") -> None:
            ...


        def put(self, m: "Matrix2d", offset: int, dest: "DoubleBuffer") -> None:
            ...


        def put(self, m: "Matrix2d", offset: int, dest: "ByteBuffer") -> None:
            ...


        def putf(self, m: "Matrix2d", offset: int, dest: "FloatBuffer") -> None:
            ...


        def putf(self, m: "Matrix2d", offset: int, dest: "ByteBuffer") -> None:
            ...


        def putf(self, m: "Matrix3d", offset: int, dest: "ByteBuffer") -> None:
            ...


        def put(self, src: "Vector4d", offset: int, dest: "DoubleBuffer") -> None:
            ...


        def put(self, src: "Vector4d", offset: int, dest: "FloatBuffer") -> None:
            ...


        def put(self, src: "Vector4d", offset: int, dest: "ByteBuffer") -> None:
            ...


        def putf(self, src: "Vector4d", offset: int, dest: "ByteBuffer") -> None:
            ...


        def put(self, src: "Vector4f", offset: int, dest: "FloatBuffer") -> None:
            ...


        def put(self, src: "Vector4f", offset: int, dest: "ByteBuffer") -> None:
            ...


        def put(self, src: "Vector4L", offset: int, dest: "LongBuffer") -> None:
            ...


        def put(self, src: "Vector4L", offset: int, dest: "ByteBuffer") -> None:
            ...


        def put(self, src: "Vector4i", offset: int, dest: "IntBuffer") -> None:
            ...


        def put(self, src: "Vector4i", offset: int, dest: "ByteBuffer") -> None:
            ...


        def put(self, src: "Vector3f", offset: int, dest: "FloatBuffer") -> None:
            ...


        def put(self, src: "Vector3f", offset: int, dest: "ByteBuffer") -> None:
            ...


        def put(self, src: "Vector3d", offset: int, dest: "DoubleBuffer") -> None:
            ...


        def put(self, src: "Vector3d", offset: int, dest: "FloatBuffer") -> None:
            ...


        def put(self, src: "Vector3d", offset: int, dest: "ByteBuffer") -> None:
            ...


        def putf(self, src: "Vector3d", offset: int, dest: "ByteBuffer") -> None:
            ...


        def put(self, src: "Vector3i", offset: int, dest: "IntBuffer") -> None:
            ...


        def put(self, src: "Vector3i", offset: int, dest: "ByteBuffer") -> None:
            ...


        def put(self, src: "Vector3L", offset: int, dest: "LongBuffer") -> None:
            ...


        def put(self, src: "Vector3L", offset: int, dest: "ByteBuffer") -> None:
            ...


        def put(self, src: "Vector2f", offset: int, dest: "FloatBuffer") -> None:
            ...


        def put(self, src: "Vector2f", offset: int, dest: "ByteBuffer") -> None:
            ...


        def put(self, src: "Vector2d", offset: int, dest: "DoubleBuffer") -> None:
            ...


        def put(self, src: "Vector2d", offset: int, dest: "ByteBuffer") -> None:
            ...


        def put(self, src: "Vector2i", offset: int, dest: "IntBuffer") -> None:
            ...


        def put(self, src: "Vector2i", offset: int, dest: "ByteBuffer") -> None:
            ...


        def put(self, src: "Vector2i", offset: int, dest: "LongBuffer") -> None:
            ...


        def put(self, src: "Vector2L", offset: int, dest: "ByteBuffer") -> None:
            ...


        def put(self, src: "Vector2L", offset: int, dest: "LongBuffer") -> None:
            ...


        def get(self, m: "Matrix4f", offset: int, src: "FloatBuffer") -> None:
            ...


        def get(self, m: "Matrix4f", offset: int, src: "ByteBuffer") -> None:
            ...


        def getTransposed(self, m: "Matrix4f", offset: int, src: "FloatBuffer") -> None:
            ...


        def getTransposed(self, m: "Matrix4f", offset: int, src: "ByteBuffer") -> None:
            ...


        def get(self, m: "Matrix4x3f", offset: int, src: "FloatBuffer") -> None:
            ...


        def get(self, m: "Matrix4x3f", offset: int, src: "ByteBuffer") -> None:
            ...


        def get(self, m: "Matrix4d", offset: int, src: "DoubleBuffer") -> None:
            ...


        def get(self, m: "Matrix4d", offset: int, src: "ByteBuffer") -> None:
            ...


        def get(self, m: "Matrix4x3d", offset: int, src: "DoubleBuffer") -> None:
            ...


        def get(self, m: "Matrix4x3d", offset: int, src: "ByteBuffer") -> None:
            ...


        def getf(self, m: "Matrix4d", offset: int, src: "FloatBuffer") -> None:
            ...


        def getf(self, m: "Matrix4d", offset: int, src: "ByteBuffer") -> None:
            ...


        def getf(self, m: "Matrix4x3d", offset: int, src: "FloatBuffer") -> None:
            ...


        def getf(self, m: "Matrix4x3d", offset: int, src: "ByteBuffer") -> None:
            ...


        def get(self, m: "Matrix3f", offset: int, src: "FloatBuffer") -> None:
            ...


        def get(self, m: "Matrix3f", offset: int, src: "ByteBuffer") -> None:
            ...


        def get(self, m: "Matrix3d", offset: int, src: "DoubleBuffer") -> None:
            ...


        def get(self, m: "Matrix3d", offset: int, src: "ByteBuffer") -> None:
            ...


        def get(self, m: "Matrix3x2f", offset: int, src: "FloatBuffer") -> None:
            ...


        def get(self, m: "Matrix3x2f", offset: int, src: "ByteBuffer") -> None:
            ...


        def get(self, m: "Matrix3x2d", offset: int, src: "DoubleBuffer") -> None:
            ...


        def get(self, m: "Matrix3x2d", offset: int, src: "ByteBuffer") -> None:
            ...


        def getf(self, m: "Matrix3d", offset: int, src: "FloatBuffer") -> None:
            ...


        def getf(self, m: "Matrix3d", offset: int, src: "ByteBuffer") -> None:
            ...


        def get(self, m: "Matrix2f", offset: int, src: "FloatBuffer") -> None:
            ...


        def get(self, m: "Matrix2f", offset: int, src: "ByteBuffer") -> None:
            ...


        def get(self, m: "Matrix2d", offset: int, src: "DoubleBuffer") -> None:
            ...


        def get(self, m: "Matrix2d", offset: int, src: "ByteBuffer") -> None:
            ...


        def getf(self, m: "Matrix2d", offset: int, src: "FloatBuffer") -> None:
            ...


        def getf(self, m: "Matrix2d", offset: int, src: "ByteBuffer") -> None:
            ...


        def get(self, dst: "Vector4d", offset: int, src: "DoubleBuffer") -> None:
            ...


        def get(self, dst: "Vector4d", offset: int, src: "ByteBuffer") -> None:
            ...


        def get(self, dst: "Vector4f", offset: int, src: "FloatBuffer") -> None:
            ...


        def get(self, dst: "Vector4f", offset: int, src: "ByteBuffer") -> None:
            ...


        def get(self, dst: "Vector4L", offset: int, src: "LongBuffer") -> None:
            ...


        def get(self, dst: "Vector4L", offset: int, src: "ByteBuffer") -> None:
            ...


        def get(self, dst: "Vector4i", offset: int, src: "IntBuffer") -> None:
            ...


        def get(self, dst: "Vector4i", offset: int, src: "ByteBuffer") -> None:
            ...


        def get(self, dst: "Vector3f", offset: int, src: "FloatBuffer") -> None:
            ...


        def get(self, dst: "Vector3f", offset: int, src: "ByteBuffer") -> None:
            ...


        def get(self, dst: "Vector3d", offset: int, src: "DoubleBuffer") -> None:
            ...


        def get(self, dst: "Vector3d", offset: int, src: "ByteBuffer") -> None:
            ...


        def get(self, dst: "Vector3i", offset: int, src: "IntBuffer") -> None:
            ...


        def get(self, dst: "Vector3i", offset: int, src: "ByteBuffer") -> None:
            ...


        def get(self, dst: "Vector3L", offset: int, src: "LongBuffer") -> None:
            ...


        def get(self, dst: "Vector3L", offset: int, src: "ByteBuffer") -> None:
            ...


        def get(self, dst: "Vector2f", offset: int, src: "FloatBuffer") -> None:
            ...


        def get(self, dst: "Vector2f", offset: int, src: "ByteBuffer") -> None:
            ...


        def get(self, dst: "Vector2d", offset: int, src: "DoubleBuffer") -> None:
            ...


        def get(self, dst: "Vector2d", offset: int, src: "ByteBuffer") -> None:
            ...


        def get(self, dst: "Vector2i", offset: int, src: "IntBuffer") -> None:
            ...


        def get(self, dst: "Vector2L", offset: int, src: "LongBuffer") -> None:
            ...


        def get(self, dst: "Vector2i", offset: int, src: "ByteBuffer") -> None:
            ...


        def get(self, dst: "Vector2L", offset: int, src: "ByteBuffer") -> None:
            ...


        def get(self, m: "Matrix4f", column: int, row: int) -> float:
            ...


        def set(self, m: "Matrix4f", column: int, row: int, value: float) -> "Matrix4f":
            ...


        def get(self, m: "Matrix4d", column: int, row: int) -> float:
            ...


        def set(self, m: "Matrix4d", column: int, row: int, value: float) -> "Matrix4d":
            ...


        def get(self, m: "Matrix3f", column: int, row: int) -> float:
            ...


        def set(self, m: "Matrix3f", column: int, row: int, value: float) -> "Matrix3f":
            ...


        def get(self, m: "Matrix3d", column: int, row: int) -> float:
            ...


        def set(self, m: "Matrix3d", column: int, row: int, value: float) -> "Matrix3d":
            ...


        def getColumn(self, m: "Matrix4f", column: int, dest: "Vector4f") -> "Vector4f":
            ...


        def setColumn(self, v: "Vector4f", column: int, dest: "Matrix4f") -> "Matrix4f":
            ...


        def setColumn(self, v: "Vector4fc", column: int, dest: "Matrix4f") -> "Matrix4f":
            ...


        def copy(self, src: "Matrix4fc", dest: "Matrix4f") -> None:
            ...


        def copy(self, src: "Matrix3fc", dest: "Matrix4f") -> None:
            ...


        def copy(self, src: "Matrix4fc", dest: "Matrix3f") -> None:
            ...


        def copy(self, src: "Matrix3fc", dest: "Matrix4x3f") -> None:
            ...


        def copy(self, src: "Matrix3x2fc", dest: "Matrix3x2f") -> None:
            ...


        def copy(self, src: "Matrix3x2dc", dest: "Matrix3x2d") -> None:
            ...


        def copy(self, src: "Matrix2fc", dest: "Matrix2f") -> None:
            ...


        def copy(self, src: "Matrix2dc", dest: "Matrix2d") -> None:
            ...


        def copy(self, src: "Matrix2fc", dest: "Matrix3f") -> None:
            ...


        def copy(self, src: "Matrix3fc", dest: "Matrix2f") -> None:
            ...


        def copy(self, src: "Matrix2fc", dest: "Matrix3x2f") -> None:
            ...


        def copy(self, src: "Matrix3x2fc", dest: "Matrix2f") -> None:
            ...


        def copy(self, src: "Matrix2dc", dest: "Matrix3d") -> None:
            ...


        def copy(self, src: "Matrix3dc", dest: "Matrix2d") -> None:
            ...


        def copy(self, src: "Matrix2dc", dest: "Matrix3x2d") -> None:
            ...


        def copy(self, src: "Matrix3x2dc", dest: "Matrix2d") -> None:
            ...


        def copy3x3(self, src: "Matrix4fc", dest: "Matrix4f") -> None:
            ...


        def copy3x3(self, src: "Matrix4x3fc", dest: "Matrix4x3f") -> None:
            ...


        def copy3x3(self, src: "Matrix3fc", dest: "Matrix4x3f") -> None:
            ...


        def copy3x3(self, src: "Matrix3fc", dest: "Matrix4f") -> None:
            ...


        def copy4x3(self, src: "Matrix4x3fc", dest: "Matrix4f") -> None:
            ...


        def copy4x3(self, src: "Matrix4fc", dest: "Matrix4f") -> None:
            ...


        def copy(self, src: "Matrix4fc", dest: "Matrix4x3f") -> None:
            ...


        def copy(self, src: "Matrix4x3fc", dest: "Matrix4f") -> None:
            ...


        def copy(self, src: "Matrix4x3fc", dest: "Matrix4x3f") -> None:
            ...


        def copy(self, src: "Matrix3fc", dest: "Matrix3f") -> None:
            ...


        def copy(self, arr: list[float], off: int, dest: "Matrix4f") -> None:
            ...


        def copyTransposed(self, arr: list[float], off: int, dest: "Matrix4f") -> None:
            ...


        def copy(self, arr: list[float], off: int, dest: "Matrix3f") -> None:
            ...


        def copy(self, arr: list[float], off: int, dest: "Matrix4x3f") -> None:
            ...


        def copy(self, arr: list[float], off: int, dest: "Matrix3x2f") -> None:
            ...


        def copy(self, arr: list[float], off: int, dest: "Matrix3x2d") -> None:
            ...


        def copy(self, arr: list[float], off: int, dest: "Matrix3x2d") -> None:
            ...


        def copy(self, arr: list[float], off: int, dest: "Matrix2f") -> None:
            ...


        def copy(self, arr: list[float], off: int, dest: "Matrix2d") -> None:
            ...


        def copy(self, src: "Matrix4fc", dest: list[float], off: int) -> None:
            ...


        def copy(self, src: "Matrix3fc", dest: list[float], off: int) -> None:
            ...


        def copy(self, src: "Matrix4x3fc", dest: list[float], off: int) -> None:
            ...


        def copy(self, src: "Matrix3x2fc", dest: list[float], off: int) -> None:
            ...


        def copy(self, src: "Matrix3x2dc", dest: list[float], off: int) -> None:
            ...


        def copy(self, src: "Matrix2fc", dest: list[float], off: int) -> None:
            ...


        def copy(self, src: "Matrix2dc", dest: list[float], off: int) -> None:
            ...


        def copy4x4(self, src: "Matrix4x3fc", dest: list[float], off: int) -> None:
            ...


        def copy4x4(self, src: "Matrix4x3dc", dest: list[float], off: int) -> None:
            ...


        def copy4x4(self, src: "Matrix4x3dc", dest: list[float], off: int) -> None:
            ...


        def copy3x3(self, src: "Matrix3x2fc", dest: list[float], off: int) -> None:
            ...


        def copy3x3(self, src: "Matrix3x2dc", dest: list[float], off: int) -> None:
            ...


        def copy4x4(self, src: "Matrix3x2fc", dest: list[float], off: int) -> None:
            ...


        def copy4x4(self, src: "Matrix3x2dc", dest: list[float], off: int) -> None:
            ...


        def identity(self, dest: "Matrix4f") -> None:
            ...


        def identity(self, dest: "Matrix4x3f") -> None:
            ...


        def identity(self, dest: "Matrix3f") -> None:
            ...


        def identity(self, dest: "Matrix3x2f") -> None:
            ...


        def identity(self, dest: "Matrix3x2d") -> None:
            ...


        def identity(self, dest: "Matrix2f") -> None:
            ...


        def swap(self, m1: "Matrix4f", m2: "Matrix4f") -> None:
            ...


        def swap(self, m1: "Matrix4x3f", m2: "Matrix4x3f") -> None:
            ...


        def swap(self, m1: "Matrix3f", m2: "Matrix3f") -> None:
            ...


        def swap(self, m1: "Matrix2f", m2: "Matrix2f") -> None:
            ...


        def swap(self, m1: "Matrix2d", m2: "Matrix2d") -> None:
            ...


        def zero(self, dest: "Matrix4f") -> None:
            ...


        def zero(self, dest: "Matrix4x3f") -> None:
            ...


        def zero(self, dest: "Matrix3f") -> None:
            ...


        def zero(self, dest: "Matrix3x2f") -> None:
            ...


        def zero(self, dest: "Matrix3x2d") -> None:
            ...


        def zero(self, dest: "Matrix2f") -> None:
            ...


        def zero(self, dest: "Matrix2d") -> None:
            ...


        def putMatrix3f(self, q: "Quaternionf", position: int, dest: "ByteBuffer") -> None:
            ...


        def putMatrix3f(self, q: "Quaternionf", position: int, dest: "FloatBuffer") -> None:
            ...


        def putMatrix4f(self, q: "Quaternionf", position: int, dest: "ByteBuffer") -> None:
            ...


        def putMatrix4f(self, q: "Quaternionf", position: int, dest: "FloatBuffer") -> None:
            ...


        def putMatrix4x3f(self, q: "Quaternionf", position: int, dest: "ByteBuffer") -> None:
            ...


        def putMatrix4x3f(self, q: "Quaternionf", position: int, dest: "FloatBuffer") -> None:
            ...


    class MemUtilUnsafe(MemUtilNIO):

        UNSAFE = None
        ADDRESS = None
        Matrix2f_m00 = None
        Matrix3f_m00 = None
        Matrix3d_m00 = None
        Matrix4f_m00 = None
        Matrix4d_m00 = None
        Matrix4x3f_m00 = None
        Matrix3x2f_m00 = None
        Vector4f_x = None
        Vector4i_x = None
        Vector3f_x = None
        Vector3i_x = None
        Vector2f_x = None
        Vector2i_x = None
        floatArrayOffset = None


        @staticmethod
        def getUnsafeInstance() -> "sun.misc.Unsafe":
            ...


        @staticmethod
        def put(m: "Matrix4f", destAddr: int) -> None:
            ...


        @staticmethod
        def put4x3(m: "Matrix4f", destAddr: int) -> None:
            ...


        @staticmethod
        def put3x4(m: "Matrix4f", destAddr: int) -> None:
            ...


        @staticmethod
        def put(m: "Matrix4x3f", destAddr: int) -> None:
            ...


        @staticmethod
        def put4x4(m: "Matrix4x3f", destAddr: int) -> None:
            ...


        @staticmethod
        def put3x4(m: "Matrix4x3f", destAddr: int) -> None:
            ...


        @staticmethod
        def put4x4(m: "Matrix4x3d", destAddr: int) -> None:
            ...


        @staticmethod
        def put4x4(m: "Matrix3x2f", destAddr: int) -> None:
            ...


        @staticmethod
        def put4x4(m: "Matrix3x2d", destAddr: int) -> None:
            ...


        @staticmethod
        def put3x3(m: "Matrix3x2f", destAddr: int) -> None:
            ...


        @staticmethod
        def put3x3(m: "Matrix3x2d", destAddr: int) -> None:
            ...


        @staticmethod
        def putTransposed(m: "Matrix4f", destAddr: int) -> None:
            ...


        @staticmethod
        def put4x3Transposed(m: "Matrix4f", destAddr: int) -> None:
            ...


        @staticmethod
        def putTransposed(m: "Matrix4x3f", destAddr: int) -> None:
            ...


        @staticmethod
        def putTransposed(m: "Matrix3f", destAddr: int) -> None:
            ...


        @staticmethod
        def putTransposed(m: "Matrix3x2f", destAddr: int) -> None:
            ...


        @staticmethod
        def putTransposed(m: "Matrix2f", destAddr: int) -> None:
            ...


        @staticmethod
        def put(m: "Matrix4d", destAddr: int) -> None:
            ...


        @staticmethod
        def put(m: "Matrix4x3d", destAddr: int) -> None:
            ...


        @staticmethod
        def putTransposed(m: "Matrix4d", destAddr: int) -> None:
            ...


        @staticmethod
        def putfTransposed(m: "Matrix4d", destAddr: int) -> None:
            ...


        @staticmethod
        def put4x3Transposed(m: "Matrix4d", destAddr: int) -> None:
            ...


        @staticmethod
        def putTransposed(m: "Matrix4x3d", destAddr: int) -> None:
            ...


        @staticmethod
        def putTransposed(m: "Matrix3d", destAddr: int) -> None:
            ...


        @staticmethod
        def putTransposed(m: "Matrix3x2d", destAddr: int) -> None:
            ...


        @staticmethod
        def putTransposed(m: "Matrix2d", destAddr: int) -> None:
            ...


        @staticmethod
        def putfTransposed(m: "Matrix4x3d", destAddr: int) -> None:
            ...


        @staticmethod
        def putfTransposed(m: "Matrix3d", destAddr: int) -> None:
            ...


        @staticmethod
        def putfTransposed(m: "Matrix3x2d", destAddr: int) -> None:
            ...


        @staticmethod
        def putfTransposed(m: "Matrix2d", destAddr: int) -> None:
            ...


        @staticmethod
        def putf(m: "Matrix4d", destAddr: int) -> None:
            ...


        @staticmethod
        def putf(m: "Matrix4x3d", destAddr: int) -> None:
            ...


        @staticmethod
        def put(m: "Matrix3f", destAddr: int) -> None:
            ...


        @staticmethod
        def put3x4(m: "Matrix3f", destAddr: int) -> None:
            ...


        @staticmethod
        def put(m: "Matrix3d", destAddr: int) -> None:
            ...


        @staticmethod
        def put(m: "Matrix3x2f", destAddr: int) -> None:
            ...


        @staticmethod
        def put(m: "Matrix3x2d", destAddr: int) -> None:
            ...


        @staticmethod
        def putf(m: "Matrix3d", destAddr: int) -> None:
            ...


        @staticmethod
        def put(m: "Matrix2f", destAddr: int) -> None:
            ...


        @staticmethod
        def put(m: "Matrix2d", destAddr: int) -> None:
            ...


        @staticmethod
        def putf(m: "Matrix2d", destAddr: int) -> None:
            ...


        @staticmethod
        def put(src: "Vector4d", destAddr: int) -> None:
            ...


        @staticmethod
        def putf(src: "Vector4d", destAddr: int) -> None:
            ...


        @staticmethod
        def put(src: "Vector4f", destAddr: int) -> None:
            ...


        @staticmethod
        def put(src: "Vector4i", destAddr: int) -> None:
            ...


        @staticmethod
        def put(src: "Vector4L", destAddr: int) -> None:
            ...


        @staticmethod
        def put(src: "Vector3f", destAddr: int) -> None:
            ...


        @staticmethod
        def put(src: "Vector3d", destAddr: int) -> None:
            ...


        @staticmethod
        def putf(src: "Vector3d", destAddr: int) -> None:
            ...


        @staticmethod
        def put(src: "Vector3i", destAddr: int) -> None:
            ...


        @staticmethod
        def put(src: "Vector3L", destAddr: int) -> None:
            ...


        @staticmethod
        def put(src: "Vector2f", destAddr: int) -> None:
            ...


        @staticmethod
        def put(src: "Vector2d", destAddr: int) -> None:
            ...


        @staticmethod
        def put(src: "Vector2i", destAddr: int) -> None:
            ...


        @staticmethod
        def put(src: "Vector2L", destAddr: int) -> None:
            ...


        @staticmethod
        def get(m: "Matrix4f", srcAddr: int) -> None:
            ...


        @staticmethod
        def getTransposed(m: "Matrix4f", srcAddr: int) -> None:
            ...


        @staticmethod
        def getTransposed(m: "Matrix3f", srcAddr: int) -> None:
            ...


        @staticmethod
        def getTransposed(m: "Matrix4x3f", srcAddr: int) -> None:
            ...


        @staticmethod
        def getTransposed(m: "Matrix3x2f", srcAddr: int) -> None:
            ...


        @staticmethod
        def getTransposed(m: "Matrix2f", srcAddr: int) -> None:
            ...


        @staticmethod
        def getTransposed(m: "Matrix2d", srcAddr: int) -> None:
            ...


        @staticmethod
        def getTransposed(m: "Matrix4x3d", srcAddr: int) -> None:
            ...


        @staticmethod
        def getTransposed(m: "Matrix3x2d", srcAddr: int) -> None:
            ...


        @staticmethod
        def getTransposed(m: "Matrix3d", srcAddr: int) -> None:
            ...


        @staticmethod
        def getTransposed(m: "Matrix4d", srcAddr: int) -> None:
            ...


        @staticmethod
        def get(m: "Matrix4x3f", srcAddr: int) -> None:
            ...


        @staticmethod
        def get(m: "Matrix4d", srcAddr: int) -> None:
            ...


        @staticmethod
        def get(m: "Matrix4x3d", srcAddr: int) -> None:
            ...


        @staticmethod
        def getf(m: "Matrix4d", srcAddr: int) -> None:
            ...


        @staticmethod
        def getf(m: "Matrix4x3d", srcAddr: int) -> None:
            ...


        @staticmethod
        def get(m: "Matrix3f", srcAddr: int) -> None:
            ...


        @staticmethod
        def get(m: "Matrix3d", srcAddr: int) -> None:
            ...


        @staticmethod
        def get(m: "Matrix3x2f", srcAddr: int) -> None:
            ...


        @staticmethod
        def get(m: "Matrix3x2d", srcAddr: int) -> None:
            ...


        @staticmethod
        def getf(m: "Matrix3d", srcAddr: int) -> None:
            ...


        @staticmethod
        def get(m: "Matrix2f", srcAddr: int) -> None:
            ...


        @staticmethod
        def get(m: "Matrix2d", srcAddr: int) -> None:
            ...


        @staticmethod
        def getf(m: "Matrix2d", srcAddr: int) -> None:
            ...


        @staticmethod
        def get(dst: "Vector4d", srcAddr: int) -> None:
            ...


        @staticmethod
        def get(dst: "Vector4f", srcAddr: int) -> None:
            ...


        @staticmethod
        def get(dst: "Vector4i", srcAddr: int) -> None:
            ...


        @staticmethod
        def get(dst: "Vector4L", srcAddr: int) -> None:
            ...


        @staticmethod
        def get(dst: "Vector3f", srcAddr: int) -> None:
            ...


        @staticmethod
        def get(dst: "Vector3d", srcAddr: int) -> None:
            ...


        @staticmethod
        def get(dst: "Vector3i", srcAddr: int) -> None:
            ...


        @staticmethod
        def get(dst: "Vector3L", srcAddr: int) -> None:
            ...


        @staticmethod
        def get(dst: "Vector2f", srcAddr: int) -> None:
            ...


        @staticmethod
        def get(dst: "Vector2d", srcAddr: int) -> None:
            ...


        @staticmethod
        def get(dst: "Vector2i", srcAddr: int) -> None:
            ...


        @staticmethod
        def get(dst: "Vector2L", srcAddr: int) -> None:
            ...


        @staticmethod
        def putMatrix3f(q: "Quaternionf", addr: int) -> None:
            ...


        @staticmethod
        def putMatrix4f(q: "Quaternionf", addr: int) -> None:
            ...


        @staticmethod
        def putMatrix4x3f(q: "Quaternionf", addr: int) -> None:
            ...


        def putMatrix3f(self, q: "Quaternionf", offset: int, dest: "ByteBuffer") -> None:
            ...


        def putMatrix3f(self, q: "Quaternionf", offset: int, dest: "FloatBuffer") -> None:
            ...


        def putMatrix4f(self, q: "Quaternionf", offset: int, dest: "ByteBuffer") -> None:
            ...


        def putMatrix4f(self, q: "Quaternionf", offset: int, dest: "FloatBuffer") -> None:
            ...


        def putMatrix4x3f(self, q: "Quaternionf", offset: int, dest: "ByteBuffer") -> None:
            ...


        def putMatrix4x3f(self, q: "Quaternionf", offset: int, dest: "FloatBuffer") -> None:
            ...


        def put(self, m: "Matrix4f", offset: int, dest: "FloatBuffer") -> None:
            ...


        def put(self, m: "Matrix4f", offset: int, dest: "ByteBuffer") -> None:
            ...


        def put4x3(self, m: "Matrix4f", offset: int, dest: "FloatBuffer") -> None:
            ...


        def put4x3(self, m: "Matrix4f", offset: int, dest: "ByteBuffer") -> None:
            ...


        def put3x4(self, m: "Matrix4f", offset: int, dest: "FloatBuffer") -> None:
            ...


        def put3x4(self, m: "Matrix4f", offset: int, dest: "ByteBuffer") -> None:
            ...


        def put(self, m: "Matrix4x3f", offset: int, dest: "FloatBuffer") -> None:
            ...


        def put(self, m: "Matrix4x3f", offset: int, dest: "ByteBuffer") -> None:
            ...


        def put4x4(self, m: "Matrix4x3f", offset: int, dest: "FloatBuffer") -> None:
            ...


        def put4x4(self, m: "Matrix4x3f", offset: int, dest: "ByteBuffer") -> None:
            ...


        def put3x4(self, m: "Matrix4x3f", offset: int, dest: "FloatBuffer") -> None:
            ...


        def put3x4(self, m: "Matrix4x3f", offset: int, dest: "ByteBuffer") -> None:
            ...


        def put4x4(self, m: "Matrix4x3d", offset: int, dest: "DoubleBuffer") -> None:
            ...


        def put4x4(self, m: "Matrix4x3d", offset: int, dest: "ByteBuffer") -> None:
            ...


        def put4x4(self, m: "Matrix3x2f", offset: int, dest: "FloatBuffer") -> None:
            ...


        def put4x4(self, m: "Matrix3x2f", offset: int, dest: "ByteBuffer") -> None:
            ...


        def put4x4(self, m: "Matrix3x2d", offset: int, dest: "DoubleBuffer") -> None:
            ...


        def put4x4(self, m: "Matrix3x2d", offset: int, dest: "ByteBuffer") -> None:
            ...


        def put3x3(self, m: "Matrix3x2f", offset: int, dest: "FloatBuffer") -> None:
            ...


        def put3x3(self, m: "Matrix3x2f", offset: int, dest: "ByteBuffer") -> None:
            ...


        def put3x3(self, m: "Matrix3x2d", offset: int, dest: "DoubleBuffer") -> None:
            ...


        def put3x3(self, m: "Matrix3x2d", offset: int, dest: "ByteBuffer") -> None:
            ...


        def putTransposed(self, m: "Matrix4f", offset: int, dest: "FloatBuffer") -> None:
            ...


        def putTransposed(self, m: "Matrix4f", offset: int, dest: "ByteBuffer") -> None:
            ...


        def put4x3Transposed(self, m: "Matrix4f", offset: int, dest: "FloatBuffer") -> None:
            ...


        def put4x3Transposed(self, m: "Matrix4f", offset: int, dest: "ByteBuffer") -> None:
            ...


        def putTransposed(self, m: "Matrix4x3f", offset: int, dest: "FloatBuffer") -> None:
            ...


        def putTransposed(self, m: "Matrix4x3f", offset: int, dest: "ByteBuffer") -> None:
            ...


        def putTransposed(self, m: "Matrix3f", offset: int, dest: "FloatBuffer") -> None:
            ...


        def putTransposed(self, m: "Matrix3f", offset: int, dest: "ByteBuffer") -> None:
            ...


        def putTransposed(self, m: "Matrix3x2f", offset: int, dest: "FloatBuffer") -> None:
            ...


        def putTransposed(self, m: "Matrix2f", offset: int, dest: "FloatBuffer") -> None:
            ...


        def putTransposed(self, m: "Matrix2f", offset: int, dest: "ByteBuffer") -> None:
            ...


        def put(self, m: "Matrix4d", offset: int, dest: "DoubleBuffer") -> None:
            ...


        def put(self, m: "Matrix4d", offset: int, dest: "ByteBuffer") -> None:
            ...


        def put(self, m: "Matrix4x3d", offset: int, dest: "DoubleBuffer") -> None:
            ...


        def put(self, m: "Matrix4x3d", offset: int, dest: "ByteBuffer") -> None:
            ...


        def putf(self, m: "Matrix4d", offset: int, dest: "FloatBuffer") -> None:
            ...


        def putf(self, m: "Matrix4d", offset: int, dest: "ByteBuffer") -> None:
            ...


        def putf(self, m: "Matrix4x3d", offset: int, dest: "FloatBuffer") -> None:
            ...


        def putf(self, m: "Matrix4x3d", offset: int, dest: "ByteBuffer") -> None:
            ...


        def putTransposed(self, m: "Matrix4d", offset: int, dest: "DoubleBuffer") -> None:
            ...


        def putTransposed(self, m: "Matrix4d", offset: int, dest: "ByteBuffer") -> None:
            ...


        def put4x3Transposed(self, m: "Matrix4d", offset: int, dest: "DoubleBuffer") -> None:
            ...


        def put4x3Transposed(self, m: "Matrix4d", offset: int, dest: "ByteBuffer") -> None:
            ...


        def putTransposed(self, m: "Matrix4x3d", offset: int, dest: "DoubleBuffer") -> None:
            ...


        def putTransposed(self, m: "Matrix4x3d", offset: int, dest: "ByteBuffer") -> None:
            ...


        def putTransposed(self, m: "Matrix3d", offset: int, dest: "DoubleBuffer") -> None:
            ...


        def putTransposed(self, m: "Matrix3d", offset: int, dest: "ByteBuffer") -> None:
            ...


        def putTransposed(self, m: "Matrix3x2d", offset: int, dest: "DoubleBuffer") -> None:
            ...


        def putTransposed(self, m: "Matrix3x2d", offset: int, dest: "ByteBuffer") -> None:
            ...


        def putTransposed(self, m: "Matrix2d", offset: int, dest: "DoubleBuffer") -> None:
            ...


        def putTransposed(self, m: "Matrix2d", offset: int, dest: "ByteBuffer") -> None:
            ...


        def putfTransposed(self, m: "Matrix4d", offset: int, dest: "FloatBuffer") -> None:
            ...


        def putfTransposed(self, m: "Matrix4d", offset: int, dest: "ByteBuffer") -> None:
            ...


        def putfTransposed(self, m: "Matrix4x3d", offset: int, dest: "FloatBuffer") -> None:
            ...


        def putfTransposed(self, m: "Matrix4x3d", offset: int, dest: "ByteBuffer") -> None:
            ...


        def putfTransposed(self, m: "Matrix3d", offset: int, dest: "FloatBuffer") -> None:
            ...


        def putfTransposed(self, m: "Matrix3d", offset: int, dest: "ByteBuffer") -> None:
            ...


        def putfTransposed(self, m: "Matrix3x2d", offset: int, dest: "FloatBuffer") -> None:
            ...


        def putfTransposed(self, m: "Matrix3x2d", offset: int, dest: "ByteBuffer") -> None:
            ...


        def putfTransposed(self, m: "Matrix2d", offset: int, dest: "FloatBuffer") -> None:
            ...


        def putfTransposed(self, m: "Matrix2d", offset: int, dest: "ByteBuffer") -> None:
            ...


        def put(self, m: "Matrix3f", offset: int, dest: "FloatBuffer") -> None:
            ...


        def put(self, m: "Matrix3f", offset: int, dest: "ByteBuffer") -> None:
            ...


        def put3x4(self, m: "Matrix3f", offset: int, dest: "FloatBuffer") -> None:
            ...


        def put3x4(self, m: "Matrix3f", offset: int, dest: "ByteBuffer") -> None:
            ...


        def put(self, m: "Matrix3d", offset: int, dest: "DoubleBuffer") -> None:
            ...


        def put(self, m: "Matrix3d", offset: int, dest: "ByteBuffer") -> None:
            ...


        def put(self, m: "Matrix3x2f", offset: int, dest: "FloatBuffer") -> None:
            ...


        def put(self, m: "Matrix3x2f", offset: int, dest: "ByteBuffer") -> None:
            ...


        def put(self, m: "Matrix3x2d", offset: int, dest: "DoubleBuffer") -> None:
            ...


        def put(self, m: "Matrix3x2d", offset: int, dest: "ByteBuffer") -> None:
            ...


        def putf(self, m: "Matrix3d", offset: int, dest: "FloatBuffer") -> None:
            ...


        def putf(self, m: "Matrix3d", offset: int, dest: "ByteBuffer") -> None:
            ...


        def put(self, m: "Matrix2f", offset: int, dest: "FloatBuffer") -> None:
            ...


        def put(self, m: "Matrix2f", offset: int, dest: "ByteBuffer") -> None:
            ...


        def put(self, m: "Matrix2d", offset: int, dest: "DoubleBuffer") -> None:
            ...


        def put(self, m: "Matrix2d", offset: int, dest: "ByteBuffer") -> None:
            ...


        def putf(self, m: "Matrix2d", offset: int, dest: "FloatBuffer") -> None:
            ...


        def putf(self, m: "Matrix2d", offset: int, dest: "ByteBuffer") -> None:
            ...


        def put(self, src: "Vector4d", offset: int, dest: "DoubleBuffer") -> None:
            ...


        def put(self, src: "Vector4d", offset: int, dest: "FloatBuffer") -> None:
            ...


        def put(self, src: "Vector4d", offset: int, dest: "ByteBuffer") -> None:
            ...


        def putf(self, src: "Vector4d", offset: int, dest: "ByteBuffer") -> None:
            ...


        def put(self, src: "Vector4f", offset: int, dest: "FloatBuffer") -> None:
            ...


        def put(self, src: "Vector4f", offset: int, dest: "ByteBuffer") -> None:
            ...


        def put(self, src: "Vector4i", offset: int, dest: "IntBuffer") -> None:
            ...


        def put(self, src: "Vector4i", offset: int, dest: "ByteBuffer") -> None:
            ...


        def put(self, src: "Vector3f", offset: int, dest: "FloatBuffer") -> None:
            ...


        def put(self, src: "Vector3f", offset: int, dest: "ByteBuffer") -> None:
            ...


        def put(self, src: "Vector3d", offset: int, dest: "DoubleBuffer") -> None:
            ...


        def put(self, src: "Vector3d", offset: int, dest: "FloatBuffer") -> None:
            ...


        def put(self, src: "Vector3d", offset: int, dest: "ByteBuffer") -> None:
            ...


        def putf(self, src: "Vector3d", offset: int, dest: "ByteBuffer") -> None:
            ...


        def put(self, src: "Vector3i", offset: int, dest: "IntBuffer") -> None:
            ...


        def put(self, src: "Vector3i", offset: int, dest: "ByteBuffer") -> None:
            ...


        def put(self, src: "Vector2f", offset: int, dest: "FloatBuffer") -> None:
            ...


        def put(self, src: "Vector2f", offset: int, dest: "ByteBuffer") -> None:
            ...


        def put(self, src: "Vector2d", offset: int, dest: "DoubleBuffer") -> None:
            ...


        def put(self, src: "Vector2d", offset: int, dest: "ByteBuffer") -> None:
            ...


        def put(self, src: "Vector2i", offset: int, dest: "IntBuffer") -> None:
            ...


        def put(self, src: "Vector2i", offset: int, dest: "ByteBuffer") -> None:
            ...


        def put(self, src: "Vector2L", offset: int, dest: "LongBuffer") -> None:
            ...


        def put(self, src: "Vector2L", offset: int, dest: "ByteBuffer") -> None:
            ...


        def get(self, m: "Matrix4f", offset: int, src: "FloatBuffer") -> None:
            ...


        def get(self, m: "Matrix4f", offset: int, src: "ByteBuffer") -> None:
            ...


        def get(self, m: "Matrix4f", column: int, row: int) -> float:
            ...


        def set(self, m: "Matrix4f", column: int, row: int, value: float) -> "Matrix4f":
            ...


        def get(self, m: "Matrix4d", column: int, row: int) -> float:
            ...


        def set(self, m: "Matrix4d", column: int, row: int, value: float) -> "Matrix4d":
            ...


        def get(self, m: "Matrix3f", column: int, row: int) -> float:
            ...


        def set(self, m: "Matrix3f", column: int, row: int, value: float) -> "Matrix3f":
            ...


        def get(self, m: "Matrix3d", column: int, row: int) -> float:
            ...


        def set(self, m: "Matrix3d", column: int, row: int, value: float) -> "Matrix3d":
            ...


        def get(self, m: "Matrix4x3f", offset: int, src: "FloatBuffer") -> None:
            ...


        def get(self, m: "Matrix4x3f", offset: int, src: "ByteBuffer") -> None:
            ...


        def get(self, m: "Matrix4d", offset: int, src: "DoubleBuffer") -> None:
            ...


        def get(self, m: "Matrix4d", offset: int, src: "ByteBuffer") -> None:
            ...


        def get(self, m: "Matrix4x3d", offset: int, src: "DoubleBuffer") -> None:
            ...


        def get(self, m: "Matrix4x3d", offset: int, src: "ByteBuffer") -> None:
            ...


        def getf(self, m: "Matrix4d", offset: int, src: "FloatBuffer") -> None:
            ...


        def getf(self, m: "Matrix4d", offset: int, src: "ByteBuffer") -> None:
            ...


        def getf(self, m: "Matrix4x3d", offset: int, src: "FloatBuffer") -> None:
            ...


        def getf(self, m: "Matrix4x3d", offset: int, src: "ByteBuffer") -> None:
            ...


        def get(self, m: "Matrix3f", offset: int, src: "FloatBuffer") -> None:
            ...


        def get(self, m: "Matrix3f", offset: int, src: "ByteBuffer") -> None:
            ...


        def get(self, m: "Matrix3d", offset: int, src: "DoubleBuffer") -> None:
            ...


        def get(self, m: "Matrix3d", offset: int, src: "ByteBuffer") -> None:
            ...


        def get(self, m: "Matrix3x2f", offset: int, src: "FloatBuffer") -> None:
            ...


        def get(self, m: "Matrix3x2f", offset: int, src: "ByteBuffer") -> None:
            ...


        def get(self, m: "Matrix3x2d", offset: int, src: "DoubleBuffer") -> None:
            ...


        def get(self, m: "Matrix3x2d", offset: int, src: "ByteBuffer") -> None:
            ...


        def getf(self, m: "Matrix3d", offset: int, src: "FloatBuffer") -> None:
            ...


        def getf(self, m: "Matrix3d", offset: int, src: "ByteBuffer") -> None:
            ...


        def get(self, m: "Matrix2f", offset: int, src: "FloatBuffer") -> None:
            ...


        def get(self, m: "Matrix2f", offset: int, src: "ByteBuffer") -> None:
            ...


        def get(self, m: "Matrix2d", offset: int, src: "DoubleBuffer") -> None:
            ...


        def get(self, m: "Matrix2d", offset: int, src: "ByteBuffer") -> None:
            ...


        def getf(self, m: "Matrix2d", offset: int, src: "FloatBuffer") -> None:
            ...


        def getf(self, m: "Matrix2d", offset: int, src: "ByteBuffer") -> None:
            ...


        def get(self, dst: "Vector4d", offset: int, src: "DoubleBuffer") -> None:
            ...


        def get(self, dst: "Vector4d", offset: int, src: "ByteBuffer") -> None:
            ...


        def get(self, dst: "Vector4f", offset: int, src: "FloatBuffer") -> None:
            ...


        def get(self, dst: "Vector4f", offset: int, src: "ByteBuffer") -> None:
            ...


        def get(self, dst: "Vector4i", offset: int, src: "IntBuffer") -> None:
            ...


        def get(self, dst: "Vector4i", offset: int, src: "ByteBuffer") -> None:
            ...


        def get(self, dst: "Vector3f", offset: int, src: "FloatBuffer") -> None:
            ...


        def get(self, dst: "Vector3f", offset: int, src: "ByteBuffer") -> None:
            ...


        def get(self, dst: "Vector3d", offset: int, src: "DoubleBuffer") -> None:
            ...


        def get(self, dst: "Vector3d", offset: int, src: "ByteBuffer") -> None:
            ...


        def get(self, dst: "Vector3i", offset: int, src: "IntBuffer") -> None:
            ...


        def get(self, dst: "Vector3i", offset: int, src: "ByteBuffer") -> None:
            ...


        def get(self, dst: "Vector2f", offset: int, src: "FloatBuffer") -> None:
            ...


        def get(self, dst: "Vector2f", offset: int, src: "ByteBuffer") -> None:
            ...


        def get(self, dst: "Vector2d", offset: int, src: "DoubleBuffer") -> None:
            ...


        def get(self, dst: "Vector2d", offset: int, src: "ByteBuffer") -> None:
            ...


        def get(self, dst: "Vector2i", offset: int, src: "IntBuffer") -> None:
            ...


        def get(self, dst: "Vector2i", offset: int, src: "ByteBuffer") -> None:
            ...
