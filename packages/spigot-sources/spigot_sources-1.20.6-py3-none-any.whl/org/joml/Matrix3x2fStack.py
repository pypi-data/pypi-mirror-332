"""
Python module generated from Java source file org.joml.Matrix3x2fStack

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


class Matrix3x2fStack(Matrix3x2f):
    """
    A stack of many Matrix3x2f instances. This resembles the matrix stack known from legacy OpenGL.
    
    This Matrix3x2fStack class inherits from Matrix3x2f, so the current/top matrix is always the
    Matrix3x2fStack/Matrix3x2f itself. This affects all operations in Matrix3x2f that take
    another Matrix3x2f as parameter. If a Matrix3x2fStack is used as argument to those methods, the
    effective argument will always be the *current* matrix of the matrix stack.

    Author(s)
    - Kai Burjack
    """

    def __init__(self, stackSize: int):
        """
        Create a new Matrix3x2fStack of the given size.
        
        Initially the stack pointer is at zero and the current matrix is set to identity.

        Arguments
        - stackSize: the size of the stack. This must be at least 1, in which case the Matrix3x2fStack simply only consists of `this`
                   Matrix3x2f
        """
        ...


    def __init__(self):
        """
        Do not invoke manually! Only meant for serialization.
        
        Invoking this constructor from client code will result in an inconsistent state of the 
        created Matrix3x2fStack instance.
        """
        ...


    def clear(self) -> "Matrix3x2fStack":
        """
        Set the stack pointer to zero and set the current/bottom matrix to .identity() identity.

        Returns
        - this
        """
        ...


    def pushMatrix(self) -> "Matrix3x2fStack":
        """
        Increment the stack pointer by one and set the values of the new current matrix to the one directly below it.

        Returns
        - this
        """
        ...


    def popMatrix(self) -> "Matrix3x2fStack":
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
