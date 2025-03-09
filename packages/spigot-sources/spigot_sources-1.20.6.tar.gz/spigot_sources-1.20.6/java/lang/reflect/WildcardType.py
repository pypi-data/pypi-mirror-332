"""
Python module generated from Java source file java.lang.reflect.WildcardType

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.lang.reflect import *
from typing import Any, Callable, Iterable, Tuple


class WildcardType(Type):
    """
    WildcardType represents a wildcard type expression, such as
    `?`, `? extends Number`, or `? super Integer`.

    Since
    - 1.5

    Unknown Tags
    - 4.5.1 Type Arguments of Parameterized Types
    """

    def getUpperBounds(self) -> list["Type"]:
        """
        Returns an array of `Type` objects representing the  upper
        bound(s) of this type variable.  If no upper bound is
        explicitly declared, the upper bound is `Object`.
        
        For each upper bound B :
        
         - if B is a parameterized type or a type variable, it is created,
         (see java.lang.reflect.ParameterizedType ParameterizedType
         for the details of the creation process for parameterized types).
         - Otherwise, B is resolved.

        Returns
        - an array of Types representing the upper bound(s) of this
            type variable

        Raises
        - TypeNotPresentException: if any of the
            bounds refers to a non-existent type declaration
        - MalformedParameterizedTypeException: if any of the
            bounds refer to a parameterized type that cannot be instantiated
            for any reason

        Unknown Tags
        - While to date a wildcard may have at most one upper
        bound, callers of this method should be written to accommodate
        multiple bounds.
        """
        ...


    def getLowerBounds(self) -> list["Type"]:
        """
        Returns an array of `Type` objects representing the
        lower bound(s) of this type variable.  If no lower bound is
        explicitly declared, the lower bound is the type of `null`.
        In this case, a zero length array is returned.
        
        For each lower bound B :
        
          - if B is a parameterized type or a type variable, it is created,
         (see java.lang.reflect.ParameterizedType ParameterizedType
         for the details of the creation process for parameterized types).
          - Otherwise, B is resolved.

        Returns
        - an array of Types representing the lower bound(s) of this
            type variable

        Raises
        - TypeNotPresentException: if any of the
            bounds refers to a non-existent type declaration
        - MalformedParameterizedTypeException: if any of the
            bounds refer to a parameterized type that cannot be instantiated
            for any reason

        Unknown Tags
        - While to date a wildcard may have at most one lower
        bound, callers of this method should be written to accommodate
        multiple bounds.
        """
        ...
