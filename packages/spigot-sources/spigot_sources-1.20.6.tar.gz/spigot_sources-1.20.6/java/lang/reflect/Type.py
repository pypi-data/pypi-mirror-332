"""
Python module generated from Java source file java.lang.reflect.Type

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.lang.reflect import *
from typing import Any, Callable, Iterable, Tuple


class Type:
    """
    Type is the common superinterface for all types in the Java
    programming language. These include raw types, parameterized types,
    array types, type variables and primitive types.

    Since
    - 1.5

    Unknown Tags
    - 4.1 The Kinds of Types and Values
    - 4.2 Primitive Types and Values
    - 4.3 Reference Types and Values
    - 4.4 Type Variables
    - 4.5 Parameterized Types
    - 4.8 Raw Types
    - 4.9 Intersection Types
    - 10.1 Array Types
    """

    def getTypeName(self) -> str:
        """
        Returns a string describing this type, including information
        about any type parameters.

        Returns
        - a string describing this type

        Since
        - 1.8

        Unknown Tags
        - The default implementation calls `toString`.
        """
        ...
