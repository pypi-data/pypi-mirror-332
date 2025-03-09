"""
Python module generated from Java source file java.lang.reflect.GenericDeclaration

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.lang.reflect import *
from typing import Any, Callable, Iterable, Tuple


class GenericDeclaration(AnnotatedElement):
    """
    A common interface for all entities that declare type variables.

    Since
    - 1.5
    """

    def getTypeParameters(self) -> list["TypeVariable"[Any]]:
        """
        Returns an array of `TypeVariable` objects that
        represent the type variables declared by the generic
        declaration represented by this `GenericDeclaration`
        object, in declaration order.  Returns an array of length 0 if
        the underlying generic declaration declares no type variables.

        Returns
        - an array of `TypeVariable` objects that represent
            the type variables declared by this generic declaration

        Raises
        - GenericSignatureFormatError: if the generic
            signature of this generic declaration does not conform to
            the format specified in
            <cite>The Java Virtual Machine Specification</cite>
        """
        ...
