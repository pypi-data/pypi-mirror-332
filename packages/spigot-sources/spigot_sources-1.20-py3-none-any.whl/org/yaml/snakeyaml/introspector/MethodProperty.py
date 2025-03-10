"""
Python module generated from Java source file org.yaml.snakeyaml.introspector.MethodProperty

Java source file obtained from artifact snakeyaml version 2.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.lang.reflect import Method
from java.lang.reflect import Type
from org.yaml.snakeyaml.error import YAMLException
from org.yaml.snakeyaml.introspector import *
from org.yaml.snakeyaml.util import ArrayUtils
from typing import Any, Callable, Iterable, Tuple


class MethodProperty(GenericProperty):
    """
    
    A `MethodProperty` is a `Property` which is accessed through accessor
    methods (setX, getX). It is possible to have a `MethodProperty` which has only setter,
    only getter, or both. It is not possible to have a `MethodProperty` which has neither
    setter nor getter.
    """

    def __init__(self, property: "PropertyDescriptor"):
        ...


    def set(self, object: "Object", value: "Object") -> None:
        ...


    def get(self, object: "Object") -> "Object":
        ...


    def getAnnotations(self) -> list["Annotation"]:
        """
        Returns the annotations that are present on read and write methods of this property or empty
        `List` if there're no annotations.

        Returns
        - the annotations that are present on this property or empty `List` if there're no
                annotations
        """
        ...


    def getAnnotation(self, annotationType: type["A"]) -> "A":
        """
        Returns property's annotation for the given type or `null` if it's not present. If the
        annotation is present on both read and write methods, the annotation on read method takes
        precedence.

        Arguments
        - annotationType: the type of the annotation to be returned

        Returns
        - property's annotation for the given type or `null` if it's not present
        """
        ...


    def isWritable(self) -> bool:
        ...


    def isReadable(self) -> bool:
        ...
