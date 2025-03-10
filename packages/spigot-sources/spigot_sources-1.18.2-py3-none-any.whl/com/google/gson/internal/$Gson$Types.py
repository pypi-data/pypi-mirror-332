"""
Python module generated from Java source file com.google.gson.internal.$Gson$Types

Java source file obtained from artifact gson version 2.8.9

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.gson.internal import *
from java.io import Serializable
from java.lang.reflect import Array
from java.lang.reflect import GenericArrayType
from java.lang.reflect import GenericDeclaration
from java.lang.reflect import Modifier
from java.lang.reflect import ParameterizedType
from java.lang.reflect import Type
from java.lang.reflect import TypeVariable
from java.lang.reflect import WildcardType
from java.util import Arrays
from java.util import NoSuchElementException
from java.util import Properties
from typing import Any, Callable, Iterable, Tuple


class $Gson$Types:
    """
    Static methods for working with types.

    Author(s)
    - Jesse Wilson
    """

    @staticmethod
    def newParameterizedTypeWithOwner(ownerType: "Type", rawType: "Type", *typeArguments: Tuple["Type", ...]) -> "ParameterizedType":
        """
        Returns a new parameterized type, applying `typeArguments` to
        `rawType` and enclosed by `ownerType`.

        Returns
        - a java.io.Serializable serializable parameterized type.
        """
        ...


    @staticmethod
    def arrayOf(componentType: "Type") -> "GenericArrayType":
        """
        Returns an array type whose elements are all instances of
        `componentType`.

        Returns
        - a java.io.Serializable serializable generic array type.
        """
        ...


    @staticmethod
    def subtypeOf(bound: "Type") -> "WildcardType":
        """
        Returns a type that represents an unknown type that extends `bound`.
        For example, if `bound` is `CharSequence.class`, this returns
        `? extends CharSequence`. If `bound` is `Object.class`,
        this returns `?`, which is shorthand for `? extends Object`.
        """
        ...


    @staticmethod
    def supertypeOf(bound: "Type") -> "WildcardType":
        """
        Returns a type that represents an unknown supertype of `bound`. For
        example, if `bound` is `String.class`, this returns `?
        super String`.
        """
        ...


    @staticmethod
    def canonicalize(type: "Type") -> "Type":
        """
        Returns a type that is functionally equal but not necessarily equal
        according to Object.equals(Object) Object.equals(). The returned
        type is java.io.Serializable.
        """
        ...


    @staticmethod
    def getRawType(type: "Type") -> type[Any]:
        ...


    @staticmethod
    def equals(a: "Type", b: "Type") -> bool:
        """
        Returns True if `a` and `b` are equal.
        """
        ...


    @staticmethod
    def typeToString(type: "Type") -> str:
        ...


    @staticmethod
    def getArrayComponentType(array: "Type") -> "Type":
        """
        Returns the component type of this array type.

        Raises
        - ClassCastException: if this type is not an array.
        """
        ...


    @staticmethod
    def getCollectionElementType(context: "Type", contextRawType: type[Any]) -> "Type":
        """
        Returns the element type of this collection type.

        Raises
        - IllegalArgumentException: if this type is not a collection.
        """
        ...


    @staticmethod
    def getMapKeyAndValueTypes(context: "Type", contextRawType: type[Any]) -> list["Type"]:
        """
        Returns a two element array containing this map's key and value types in
        positions 0 and 1 respectively.
        """
        ...


    @staticmethod
    def resolve(context: "Type", contextRawType: type[Any], toResolve: "Type") -> "Type":
        ...
