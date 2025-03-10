"""
Python module generated from Java source file java.lang.reflect.ParameterizedType

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.lang.reflect import *
from typing import Any, Callable, Iterable, Tuple


class ParameterizedType(Type):
    """
    ParameterizedType represents a parameterized type such as
    `Collection<String>`.
    
    A parameterized type is created the first time it is needed by a
    reflective method, as specified in this package. When a
    parameterized type p is created, the generic class or interface declaration
    that p instantiates is resolved, and all type arguments of p are created
    recursively. See java.lang.reflect.TypeVariable
    TypeVariable for details on the creation process for type
    variables. Repeated creation of a parameterized type has no effect.
    
    Instances of classes that implement this interface must implement
    an equals() method that equates any two instances that share the
    same generic class or interface declaration and have equal type parameters.

    Since
    - 1.5

    Unknown Tags
    - 4.5 Parameterized Types
    """

    def getActualTypeArguments(self) -> list["Type"]:
        """
        Returns an array of `Type` objects representing the actual type
        arguments to this type.
        
        Note that in some cases, the returned array be empty. This can occur
        if this type represents a non-parameterized type nested within
        a parameterized type.

        Returns
        - an array of `Type` objects representing the actual type
            arguments to this type

        Raises
        - TypeNotPresentException: if any of the actual type arguments
            refers to a non-existent class or interface declaration
        - MalformedParameterizedTypeException: if any of the
            actual type parameters refer to a parameterized type that cannot
            be instantiated for any reason

        Since
        - 1.5
        """
        ...


    def getRawType(self) -> "Type":
        """
        Returns the `Type` object representing the class or interface
        that declared this type.

        Returns
        - the `Type` object representing the class or interface
            that declared this type

        Since
        - 1.5
        """
        ...


    def getOwnerType(self) -> "Type":
        """
        Returns a `Type` object representing the type that this type
        is a member of.  For example, if this type is `O<T>.I<S>`,
        return a representation of `O<T>`.
        
        If this type is a top-level type, `null` is returned.

        Returns
        - a `Type` object representing the type that
            this type is a member of. If this type is a top-level type,
            `null` is returned

        Raises
        - TypeNotPresentException: if the owner type
            refers to a non-existent class or interface declaration
        - MalformedParameterizedTypeException: if the owner type
            refers to a parameterized type that cannot be instantiated
            for any reason

        Since
        - 1.5
        """
        ...
