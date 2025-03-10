"""
Python module generated from Java source file java.lang.reflect.Modifier

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.lang.reflect import *
from java.util import StringJoiner
from typing import Any, Callable, Iterable, Tuple


class Modifier:
    """
    The Modifier class provides `static` methods and
    constants to decode class and member access modifiers.  The sets of
    modifiers are represented as integers with distinct bit positions
    representing different modifiers.  The values for the constants
    representing the modifiers are taken from the tables in sections
    4.1, 4.4, 4.5, and 4.7 of
    <cite>The Java Virtual Machine Specification</cite>.

    Author(s)
    - Kenneth Russell

    See
    - Member.getModifiers()

    Since
    - 1.1
    """

    PUBLIC = 0x00000001
    """
    The `int` value representing the `public`
    modifier.
    """
    PRIVATE = 0x00000002
    """
    The `int` value representing the `private`
    modifier.
    """
    PROTECTED = 0x00000004
    """
    The `int` value representing the `protected`
    modifier.
    """
    STATIC = 0x00000008
    """
    The `int` value representing the `static`
    modifier.
    """
    FINAL = 0x00000010
    """
    The `int` value representing the `final`
    modifier.
    """
    SYNCHRONIZED = 0x00000020
    """
    The `int` value representing the `synchronized`
    modifier.
    """
    VOLATILE = 0x00000040
    """
    The `int` value representing the `volatile`
    modifier.
    """
    TRANSIENT = 0x00000080
    """
    The `int` value representing the `transient`
    modifier.
    """
    NATIVE = 0x00000100
    """
    The `int` value representing the `native`
    modifier.
    """
    INTERFACE = 0x00000200
    """
    The `int` value representing the `interface`
    modifier.
    """
    ABSTRACT = 0x00000400
    """
    The `int` value representing the `abstract`
    modifier.
    """
    STRICT = 0x00000800
    """
    The `int` value representing the `strictfp`
    modifier.
    """


    @staticmethod
    def isPublic(mod: int) -> bool:
        """
        Return `True` if the integer argument includes the
        `public` modifier, `False` otherwise.

        Arguments
        - mod: a set of modifiers

        Returns
        - `True` if `mod` includes the
        `public` modifier; `False` otherwise.
        """
        ...


    @staticmethod
    def isPrivate(mod: int) -> bool:
        """
        Return `True` if the integer argument includes the
        `private` modifier, `False` otherwise.

        Arguments
        - mod: a set of modifiers

        Returns
        - `True` if `mod` includes the
        `private` modifier; `False` otherwise.
        """
        ...


    @staticmethod
    def isProtected(mod: int) -> bool:
        """
        Return `True` if the integer argument includes the
        `protected` modifier, `False` otherwise.

        Arguments
        - mod: a set of modifiers

        Returns
        - `True` if `mod` includes the
        `protected` modifier; `False` otherwise.
        """
        ...


    @staticmethod
    def isStatic(mod: int) -> bool:
        """
        Return `True` if the integer argument includes the
        `static` modifier, `False` otherwise.

        Arguments
        - mod: a set of modifiers

        Returns
        - `True` if `mod` includes the
        `static` modifier; `False` otherwise.
        """
        ...


    @staticmethod
    def isFinal(mod: int) -> bool:
        """
        Return `True` if the integer argument includes the
        `final` modifier, `False` otherwise.

        Arguments
        - mod: a set of modifiers

        Returns
        - `True` if `mod` includes the
        `final` modifier; `False` otherwise.
        """
        ...


    @staticmethod
    def isSynchronized(mod: int) -> bool:
        """
        Return `True` if the integer argument includes the
        `synchronized` modifier, `False` otherwise.

        Arguments
        - mod: a set of modifiers

        Returns
        - `True` if `mod` includes the
        `synchronized` modifier; `False` otherwise.
        """
        ...


    @staticmethod
    def isVolatile(mod: int) -> bool:
        """
        Return `True` if the integer argument includes the
        `volatile` modifier, `False` otherwise.

        Arguments
        - mod: a set of modifiers

        Returns
        - `True` if `mod` includes the
        `volatile` modifier; `False` otherwise.
        """
        ...


    @staticmethod
    def isTransient(mod: int) -> bool:
        """
        Return `True` if the integer argument includes the
        `transient` modifier, `False` otherwise.

        Arguments
        - mod: a set of modifiers

        Returns
        - `True` if `mod` includes the
        `transient` modifier; `False` otherwise.
        """
        ...


    @staticmethod
    def isNative(mod: int) -> bool:
        """
        Return `True` if the integer argument includes the
        `native` modifier, `False` otherwise.

        Arguments
        - mod: a set of modifiers

        Returns
        - `True` if `mod` includes the
        `native` modifier; `False` otherwise.
        """
        ...


    @staticmethod
    def isInterface(mod: int) -> bool:
        """
        Return `True` if the integer argument includes the
        `interface` modifier, `False` otherwise.

        Arguments
        - mod: a set of modifiers

        Returns
        - `True` if `mod` includes the
        `interface` modifier; `False` otherwise.
        """
        ...


    @staticmethod
    def isAbstract(mod: int) -> bool:
        """
        Return `True` if the integer argument includes the
        `abstract` modifier, `False` otherwise.

        Arguments
        - mod: a set of modifiers

        Returns
        - `True` if `mod` includes the
        `abstract` modifier; `False` otherwise.
        """
        ...


    @staticmethod
    def isStrict(mod: int) -> bool:
        """
        Return `True` if the integer argument includes the
        `strictfp` modifier, `False` otherwise.

        Arguments
        - mod: a set of modifiers

        Returns
        - `True` if `mod` includes the
        `strictfp` modifier; `False` otherwise.
        """
        ...


    @staticmethod
    def toString(mod: int) -> str:
        """
        Return a string describing the access modifier flags in
        the specified modifier. For example:
        <blockquote>```
           public final synchronized strictfp
        ```</blockquote>
        The modifier names are returned in an order consistent with the
        suggested modifier orderings given in sections 8.1.1, 8.3.1, 8.4.3, 8.8.3, and 9.1.1 of
        <cite>The Java Language Specification</cite>.
        The full modifier ordering used by this method is:
        <blockquote> `public protected private abstract static final transient
        volatile synchronized native strictfp
        interface` </blockquote>
        The `interface` modifier discussed in this class is
        not a True modifier in the Java language and it appears after
        all other modifiers listed by this method.  This method may
        return a string of modifiers that are not valid modifiers of a
        Java entity; in other words, no checking is done on the
        possible validity of the combination of modifiers represented
        by the input.
        
        Note that to perform such checking for a known kind of entity,
        such as a constructor or method, first AND the argument of
        `toString` with the appropriate mask from a method like
        .constructorModifiers or .methodModifiers.

        Arguments
        - mod: a set of modifiers

        Returns
        - a string representation of the set of modifiers
        represented by `mod`
        """
        ...


    @staticmethod
    def classModifiers() -> int:
        """
        Return an `int` value OR-ing together the source language
        modifiers that can be applied to a class.

        Returns
        - an `int` value OR-ing together the source language
        modifiers that can be applied to a class.

        Since
        - 1.7

        Unknown Tags
        - 8.1.1 Class Modifiers
        """
        ...


    @staticmethod
    def interfaceModifiers() -> int:
        """
        Return an `int` value OR-ing together the source language
        modifiers that can be applied to an interface.

        Returns
        - an `int` value OR-ing together the source language
        modifiers that can be applied to an interface.

        Since
        - 1.7

        Unknown Tags
        - 9.1.1 Interface Modifiers
        """
        ...


    @staticmethod
    def constructorModifiers() -> int:
        """
        Return an `int` value OR-ing together the source language
        modifiers that can be applied to a constructor.

        Returns
        - an `int` value OR-ing together the source language
        modifiers that can be applied to a constructor.

        Since
        - 1.7

        Unknown Tags
        - 8.8.3 Constructor Modifiers
        """
        ...


    @staticmethod
    def methodModifiers() -> int:
        """
        Return an `int` value OR-ing together the source language
        modifiers that can be applied to a method.

        Returns
        - an `int` value OR-ing together the source language
        modifiers that can be applied to a method.

        Since
        - 1.7

        Unknown Tags
        - 8.4.3 Method Modifiers
        """
        ...


    @staticmethod
    def fieldModifiers() -> int:
        """
        Return an `int` value OR-ing together the source language
        modifiers that can be applied to a field.

        Returns
        - an `int` value OR-ing together the source language
        modifiers that can be applied to a field.

        Since
        - 1.7

        Unknown Tags
        - 8.3.1 Field Modifiers
        """
        ...


    @staticmethod
    def parameterModifiers() -> int:
        """
        Return an `int` value OR-ing together the source language
        modifiers that can be applied to a parameter.

        Returns
        - an `int` value OR-ing together the source language
        modifiers that can be applied to a parameter.

        Since
        - 1.8

        Unknown Tags
        - 8.4.1 Formal Parameters
        """
        ...
