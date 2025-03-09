"""
Python module generated from Java source file org.joml.Matrix4x3fStack

Java source file obtained from artifact joml version 1.10.5

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.io import IOException
from java.io import ObjectInput
from java.io import ObjectOutput
from org.joml import *
from typing import Any, Callable, Iterable, Tuple


class Matrix4x3fStack(Matrix4x3f):
    """
    A stack of many Matrix4x3f instances. This resembles the matrix stack known from legacy OpenGL.
    
    This Matrix4x3fStack class inherits from Matrix4x3f, so the current/top matrix is always the
    Matrix4x3fStack/Matrix4x3f itself. This affects all operations in Matrix4x3f that take
    another Matrix4x3f as parameter. If a Matrix4x3fStack is used as argument to those methods, the
    effective argument will always be the *current* matrix of the matrix stack.

    Author(s)
    - Kai Burjack
    """

    def __init__(self, stackSize: int):
        """
        Create a new Matrix4x3fStack of the given size.
        
        Initially the stack pointer is at zero and the current matrix is set to identity.

        Arguments
        - stackSize: the size of the stack. This must be at least 1, in which case the Matrix4x3fStack simply only consists of `this`
                   Matrix4x3f
        """
        ...


    def __init__(self):
        """
        Do not invoke manually! Only meant for serialization.
        
        Invoking this constructor from client code will result in an inconsistent state of the 
        created Matrix4x3fStack instance.
        """
        ...


    def clear(self) -> "Matrix4x3fStack":
        """
        Set the stack pointer to zero and set the current/bottom matrix to .identity() identity.

        Returns
        - this
        """
        ...


    def pushMatrix(self) -> "Matrix4x3fStack":
        """
        Increment the stack pointer by one and set the values of the new current matrix to the one directly below it.

        Returns
        - this
        """
        ...


    def popMatrix(self) -> "Matrix4x3fStack":
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
