"""
Python module generated from Java source file com.google.gson.reflect.TypeToken

Java source file obtained from artifact gson version 2.10.1

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.gson.internal import $Gson$Types
from com.google.gson.reflect import *
from java.lang.reflect import GenericArrayType
from java.lang.reflect import ParameterizedType
from java.lang.reflect import Type
from java.lang.reflect import TypeVariable
from java.util import Objects
from typing import Any, Callable, Iterable, Tuple


class TypeToken:
    """
    Represents a generic type `T`. Java doesn't yet provide a way to
    represent generic types, so this class does. Forces clients to create a
    subclass of this class which enables retrieval the type information even at
    runtime.
    
    For example, to create a type literal for `List<String>`, you can
    create an empty anonymous class:
    
    
    `TypeToken<List<String>> list = new TypeToken<List<String>>() {`;}
    
    Capturing a type variable as type argument of a `TypeToken` should
    be avoided. Due to type erasure the runtime type of a type variable is not
    available to Gson and therefore it cannot provide the functionality one
    might expect, which gives a False sense of type-safety at compilation time
    and can lead to an unexpected `ClassCastException` at runtime.
    
    If the type arguments of the parameterized type are only available at
    runtime, for example when you want to create a `List<E>` based on
    a `Class<E>` representing the element type, the method
    .getParameterized(Type, Type...) can be used.

    Author(s)
    - Jesse Wilson
    """

    def getRawType(self) -> type["T"]:
        """
        Returns the raw (non-generic) type for this type.
        """
        ...


    def getType(self) -> "Type":
        """
        Gets underlying `Type` instance.
        """
        ...


    def isAssignableFrom(self, cls: type[Any]) -> bool:
        """
        Check if this type is assignable from the given class object.

        Deprecated
        - this implementation may be inconsistent with javac for types
            with wildcards.
        """
        ...


    def isAssignableFrom(self, from: "Type") -> bool:
        """
        Check if this type is assignable from the given Type.

        Deprecated
        - this implementation may be inconsistent with javac for types
            with wildcards.
        """
        ...


    def isAssignableFrom(self, token: "TypeToken"[Any]) -> bool:
        """
        Check if this type is assignable from the given type token.

        Deprecated
        - this implementation may be inconsistent with javac for types
            with wildcards.
        """
        ...


    def hashCode(self) -> int:
        ...


    def equals(self, o: "Object") -> bool:
        ...


    def toString(self) -> str:
        ...


    @staticmethod
    def get(type: "Type") -> "TypeToken"[Any]:
        """
        Gets type literal for the given `Type` instance.
        """
        ...


    @staticmethod
    def get(type: type["T"]) -> "TypeToken"["T"]:
        """
        Gets type literal for the given `Class` instance.
        """
        ...


    @staticmethod
    def getParameterized(rawType: "Type", *typeArguments: Tuple["Type", ...]) -> "TypeToken"[Any]:
        """
        Gets a type literal for the parameterized type represented by applying `typeArguments` to
        `rawType`. This is mainly intended for situations where the type arguments are not
        available at compile time. The following example shows how a type token for `Map<K, V>`
        can be created:
        ````Class<K> keyClass = ...;
        Class<V> valueClass = ...;
        TypeToken<?> mapTypeToken = TypeToken.getParameterized(Map.class, keyClass, valueClass);````
        As seen here the result is a `TypeToken<?>`; this method cannot provide any type safety,
        and care must be taken to pass in the correct number of type arguments.

        Raises
        - IllegalArgumentException: If `rawType` is not of type `Class`, or if the type arguments are invalid for
          the raw type
        """
        ...


    @staticmethod
    def getArray(componentType: "Type") -> "TypeToken"[Any]:
        """
        Gets type literal for the array type whose elements are all instances of `componentType`.
        """
        ...
