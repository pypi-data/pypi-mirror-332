"""
Python module generated from Java source file java.lang.reflect.GenericArrayType

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.lang.reflect import *
from typing import Any, Callable, Iterable, Tuple


class GenericArrayType(Type):
    """
    `GenericArrayType` represents an array type whose component
    type is either a parameterized type or a type variable.

    Since
    - 1.5

    Unknown Tags
    - 10.1 Array Types
    """

    def getGenericComponentType(self) -> "Type":
        """
        Returns a `Type` object representing the component type
        of this array. This method creates the component type of the
        array.  See the declaration of java.lang.reflect.ParameterizedType ParameterizedType for the
        semantics of the creation process for parameterized types and
        see java.lang.reflect.TypeVariable TypeVariable for the
        creation process for type variables.

        Returns
        - a `Type` object representing the component type
            of this array

        Raises
        - TypeNotPresentException: if the underlying array type's component
            type refers to a non-existent class or interface declaration
        - MalformedParameterizedTypeException: if  the
            underlying array type's component type refers to a
            parameterized type that cannot be instantiated for any reason
        """
        ...
