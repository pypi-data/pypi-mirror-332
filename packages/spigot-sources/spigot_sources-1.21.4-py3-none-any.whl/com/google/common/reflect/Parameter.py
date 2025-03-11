"""
Python module generated from Java source file com.google.common.reflect.Parameter

Java source file obtained from artifact guava version 33.3.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.collect import FluentIterable
from com.google.common.collect import ImmutableList
from com.google.common.reflect import *
from java.lang.reflect import AnnotatedElement
from java.lang.reflect import AnnotatedType
from javax.annotation import CheckForNull
from org.checkerframework.checker.nullness.qual import Nullable
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
        """
        Since
        - 18.0
        """
        ...


    def getDeclaredAnnotations(self) -> list["Annotation"]:
        """
        Since
        - 18.0
        """
        ...


    def getDeclaredAnnotation(self, annotationType: type["A"]) -> "A":
        """
        Since
        - 18.0
        """
        ...


    def getDeclaredAnnotationsByType(self, annotationType: type["A"]) -> list["A"]:
        """
        Since
        - 18.0
        """
        ...


    def getAnnotatedType(self) -> "AnnotatedType":
        """
        Returns the AnnotatedType of the parameter.

        Since
        - 25.1 for guava-jre
        """
        ...


    def equals(self, obj: "Object") -> bool:
        ...


    def hashCode(self) -> int:
        ...


    def toString(self) -> str:
        ...
