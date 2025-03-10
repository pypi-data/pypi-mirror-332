"""
Python module generated from Java source file java.lang.reflect.TypeVariable

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.lang.reflect import *
from typing import Any, Callable, Iterable, Tuple


class TypeVariable(Type, AnnotatedElement):
    """
    TypeVariable is the common superinterface for type variables of kinds.
    A type variable is created the first time it is needed by a reflective
    method, as specified in this package.  If a type variable t is referenced
    by a type (i.e, class, interface or annotation type) T, and T is declared
    by the nth enclosing class of T (see JLS 8.1.2), then the creation of t
    requires the resolution (see JVMS 5) of the ith enclosing class of T,
    for i = 0 to n, inclusive. Creating a type variable must not cause the
    creation of its bounds. Repeated creation of a type variable has no effect.
    
    Multiple objects may be instantiated at run-time to
    represent a given type variable. Even though a type variable is
    created only once, this does not imply any requirement to cache
    instances representing the type variable. However, all instances
    representing a type variable must be equal() to each other.
    As a consequence, users of type variables must not rely on the identity
    of instances of classes implementing this interface.
    
    Type `<D>`: the type of generic declaration that declared the
    underlying type variable.

    Since
    - 1.5

    Unknown Tags
    - 4.4 Type Variables
    """

    def getBounds(self) -> list["Type"]:
        """
        Returns an array of `Type` objects representing the
        upper bound(s) of this type variable.  If no upper bound is
        explicitly declared, the upper bound is `Object`.
        
        For each upper bound B:  - if B is a parameterized
        type or a type variable, it is created, (see java.lang.reflect.ParameterizedType ParameterizedType for the
        details of the creation process for parameterized types).
        - Otherwise, B is resolved.  

        Returns
        - an array of `Type`s representing the upper
            bound(s) of this type variable

        Raises
        - TypeNotPresentException: if any of the
            bounds refers to a non-existent type declaration
        - MalformedParameterizedTypeException: if any of the
            bounds refer to a parameterized type that cannot be instantiated
            for any reason
        """
        ...


    def getGenericDeclaration(self) -> "D":
        """
        Returns the `GenericDeclaration` object representing the
        generic declaration declared for this type variable.

        Returns
        - the generic declaration declared for this type variable.

        Since
        - 1.5
        """
        ...


    def getName(self) -> str:
        """
        Returns the name of this type variable, as it occurs in the source code.

        Returns
        - the name of this type variable, as it appears in the source code
        """
        ...


    def getAnnotatedBounds(self) -> list["AnnotatedType"]:
        """
        Returns an array of AnnotatedType objects that represent the use of
        types to denote the upper bounds of the type parameter represented by
        this TypeVariable. The order of the objects in the array corresponds to
        the order of the bounds in the declaration of the type parameter. Note that
        if no upper bound is explicitly declared, the upper bound is unannotated
        `Object`.

        Returns
        - an array of objects representing the upper bound(s) of the type variable

        Since
        - 1.8
        """
        ...
