"""
Python module generated from Java source file com.google.common.reflect.Parameter

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.collect import FluentIterable
from com.google.common.collect import ImmutableList
from com.google.common.reflect import *
from java.lang.reflect import AnnotatedElement
from javax.annotation import Nullable
from typing import Any, Callable, Iterable, Tuple


class Parameter(AnnotatedElement):
    """
    Represents a method or constructor parameter.

    Author(s)
    - Ben Yu

    Since
    - 14.0
    """

    def getType(self) -> "TypeToken"[Any]:
        """
        Returns the type of the parameter.
        """
        ...


    def getDeclaringInvokable(self) -> "Invokable"[Any, Any]:
        """
        Returns the Invokable that declares this parameter.
        """
        ...


    def isAnnotationPresent(self, annotationType: type["Annotation"]) -> bool:
        ...


    def getAnnotation(self, annotationType: type["A"]) -> "A":
        ...


    def getAnnotations(self) -> list["Annotation"]:
        ...


    def getAnnotationsByType(self, annotationType: type["A"]) -> list["A"]:
        ...


    def getDeclaredAnnotations(self) -> list["Annotation"]:
        ...


    def getDeclaredAnnotation(self, annotationType: type["A"]) -> "A":
        ...


    def getDeclaredAnnotationsByType(self, annotationType: type["A"]) -> list["A"]:
        ...


    def equals(self, obj: "Object") -> bool:
        ...


    def hashCode(self) -> int:
        ...


    def toString(self) -> str:
        ...
