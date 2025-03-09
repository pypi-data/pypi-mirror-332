"""
Python module generated from Java source file java.lang.reflect.AnnotatedType

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.lang.reflect import *
from typing import Any, Callable, Iterable, Tuple


class AnnotatedType(AnnotatedElement):
    """
    `AnnotatedType` represents the potentially annotated use of a type in
    the program currently running in this VM. The use may be of any type in the
    Java programming language, including an array type, a parameterized type, a
    type variable, or a wildcard type.
    
    Note that any annotations returned by methods on this interface are
    *type annotations* (JLS 9.7.4) as the entity being
    potentially annotated is a type.

    Since
    - 1.8

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

    def getAnnotatedOwnerType(self) -> "AnnotatedType":
        """
        Returns the potentially annotated type that this type is a member of, if
        this type represents a nested type. For example, if this type is
        `@TA O<T>.I<S>`, return a representation of `@TA O<T>`.
        
        Returns `null` if this `AnnotatedType` represents a
            top-level class or interface, or a local or anonymous class, or
            a primitive type, or void.
        
        Returns `null` if this `AnnotatedType` is an instance of
            `AnnotatedArrayType`, `AnnotatedTypeVariable`, or
            `AnnotatedWildcardType`.

        Returns
        - an `AnnotatedType` object representing the potentially
            annotated type that this type is a member of, or `null`

        Raises
        - TypeNotPresentException: if the owner type
            refers to a non-existent class or interface declaration
        - MalformedParameterizedTypeException: if the owner type
            refers to a parameterized type that cannot be instantiated
            for any reason

        Since
        - 9

        Unknown Tags
        - This default implementation returns `null` and performs no other
        action.
        """
        ...


    def getType(self) -> "Type":
        """
        Returns the underlying type that this annotated type represents.

        Returns
        - the type this annotated type represents
        """
        ...


    def getAnnotation(self, annotationClass: type["T"]) -> "T":
        """
        
        Note that any annotation returned by this method is a type
        annotation.

        Raises
        - NullPointerException: 
        """
        ...


    def getAnnotations(self) -> list["Annotation"]:
        """
        
        Note that any annotations returned by this method are type
        annotations.
        """
        ...


    def getDeclaredAnnotations(self) -> list["Annotation"]:
        """
        
        Note that any annotations returned by this method are type
        annotations.
        """
        ...
