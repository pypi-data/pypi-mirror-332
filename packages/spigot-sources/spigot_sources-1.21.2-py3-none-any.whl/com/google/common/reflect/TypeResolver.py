"""
Python module generated from Java source file com.google.common.reflect.TypeResolver

Java source file obtained from artifact guava version 32.1.2-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.base import Joiner
from com.google.common.base import Objects
from com.google.common.collect import ImmutableMap
from com.google.common.collect import Maps
from com.google.common.reflect import *
from java.lang.reflect import GenericArrayType
from java.lang.reflect import ParameterizedType
from java.lang.reflect import Type
from java.lang.reflect import TypeVariable
from java.lang.reflect import WildcardType
from java.util import Arrays
from java.util import LinkedHashSet
from java.util.concurrent.atomic import AtomicInteger
from javax.annotation import CheckForNull
from typing import Any, Callable, Iterable, Tuple


class TypeResolver:
    """
    An object of this class encapsulates type mappings from type variables. Mappings are established
    with .where and types are resolved using .resolveType.
    
    Note that usually type mappings are already implied by the static type hierarchy (for example,
    the `E` type variable declared by class `List` naturally maps to `String` in
    the context of `class MyStringList implements List<String>`). In such case, prefer to use
    TypeToken.resolveType since it's simpler and more type safe. This class should only be
    used when the type mapping isn't implied by the static type hierarchy, but provided through other
    means such as an annotation or external configuration file.

    Author(s)
    - Ben Yu

    Since
    - 15.0
    """

    def __init__(self):
        ...


    def where(self, formal: "Type", actual: "Type") -> "TypeResolver":
        """
        Returns a new `TypeResolver` with type variables in `formal` mapping to types in
        `actual`.
        
        For example, if `formal` is a `TypeVariable T`, and `actual` is `String.class`, then `new TypeResolver().where(formal, actual)` will .resolveType resolve `ParameterizedType List<T>` to `List<String>`, and resolve
        `Map<T, Something>` to `Map<String, Something>` etc. Similarly, `formal` and
        `actual` can be `Map<K, V>` and `Map<String, Integer>` respectively, or they
        can be `E[]` and `String[]` respectively, or even any arbitrary combination
        thereof.

        Arguments
        - formal: The type whose type variables or itself is mapped to other type(s). It's almost
            always a bug if `formal` isn't a type variable and contains no type variable. Make
            sure you are passing the two parameters in the right order.
        - actual: The type that the formal type variable(s) are mapped to. It can be or contain yet
            other type variables, in which case these type variables will be further resolved if
            corresponding mappings exist in the current `TypeResolver` instance.
        """
        ...


    def resolveType(self, type: "Type") -> "Type":
        """
        Resolves all type variables in `type` and all downstream types and returns a
        corresponding type with type variables resolved.
        """
        ...
