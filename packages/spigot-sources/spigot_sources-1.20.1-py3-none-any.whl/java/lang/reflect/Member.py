"""
Python module generated from Java source file java.lang.reflect.Member

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.lang.reflect import *
from typing import Any, Callable, Iterable, Tuple


class Member:
    """
    Member is an interface that reflects identifying information about
    a single member (a field or a method) or a constructor.

    Author(s)
    - Nakul Saraiya

    See
    - Constructor

    Since
    - 1.1
    """

    PUBLIC = 0
    """
    Identifies the set of all public members of a class or interface,
    including inherited members.
    """
    DECLARED = 1
    """
    Identifies the set of declared members of a class or interface.
    Inherited members are not included.
    """


    def getDeclaringClass(self) -> type[Any]:
        """
        Returns the Class object representing the class or interface
        that declares the member or constructor represented by this Member.

        Returns
        - an object representing the declaring class of the
        underlying member
        """
        ...


    def getName(self) -> str:
        """
        Returns the simple name of the underlying member or constructor
        represented by this Member.

        Returns
        - the simple name of the underlying member
        """
        ...


    def getModifiers(self) -> int:
        """
        Returns the Java language modifiers for the member or
        constructor represented by this Member, as an integer.  The
        Modifier class should be used to decode the modifiers in
        the integer.

        Returns
        - the Java language modifiers for the underlying member

        See
        - Modifier
        """
        ...


    def isSynthetic(self) -> bool:
        """
        Returns `True` if this member was introduced by
        the compiler; returns `False` otherwise.

        Returns
        - True if and only if this member was introduced by
        the compiler.

        Since
        - 1.5

        Unknown Tags
        - 13.1 The Form of a Binary
        """
        ...
