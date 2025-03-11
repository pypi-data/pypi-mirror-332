"""
Python module generated from Java source file org.joml.Matrix4x3dStack

Java source file obtained from artifact joml version 1.10.8

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.io import IOException
from java.io import ObjectInput
from java.io import ObjectOutput
from org.joml import *
from typing import Any, Callable, Iterable, Tuple


class Matrix4x3dStack(Matrix4x3d):
    """
    A stack of many Matrix4x3d instances. This resembles the matrix stack known from legacy OpenGL.
    
    This Matrix4x3dStack class inherits from Matrix4x3d, so the current/top matrix is always the
    Matrix4x3dStack/Matrix4x3d itself. This affects all operations in Matrix4x3d that take
    another Matrix4x3d as parameter. If a Matrix4x3dStack is used as argument to those methods, the
    effective argument will always be the *current* matrix of the matrix stack.

    Author(s)
    - Kai Burjack
    """

    def __init__(self, stackSize: int):
        """
        Create a new Matrix4x3dStack of the given size.
        
        Initially the stack pointer is at zero and the current matrix is set to identity.

        Arguments
        - stackSize: the size of the stack. This must be at least 1, in which case the Matrix4x3dStack simply only consists of `this`
                   Matrix4x3d
        """
        ...


    def __init__(self):
        """
        Do not invoke manually! Only meant for serialization.
        
        Invoking this constructor from client code will result in an inconsistent state of the 
        created Matrix4x3dStack instance.
        """
        ...


    def clear(self) -> "Matrix4x3dStack":
        """
        Set the stack pointer to zero and set the current/bottom matrix to .identity() identity.

        Returns
        - this
        """
        ...


    def pushMatrix(self) -> "Matrix4x3dStack":
        """
        Increment the stack pointer by one and set the values of the new current matrix to the one directly below it.

        Returns
        - this
        """
        ...


    def popMatrix(self) -> "Matrix4x3dStack":
        """
        Decrement the stack pointer by one.
        
        This will effectively dispose of the current matrix.

        Returns
        - this
        """
        ...


    def hashCode(self) -> int:
        ...


    def equals(self, obj: "Object") -> bool:
        ...


    def writeExternal(self, out: "ObjectOutput") -> None:
        ...


    def readExternal(self, in: "ObjectInput") -> None:
        ...


    def clone(self) -> "Object":
        ...
