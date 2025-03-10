"""
Python module generated from Java source file org.yaml.snakeyaml.introspector.FieldProperty

Java source file obtained from artifact snakeyaml version 1.30

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.lang.reflect import Field
from org.yaml.snakeyaml.error import YAMLException
from org.yaml.snakeyaml.introspector import *
from org.yaml.snakeyaml.util import ArrayUtils
from typing import Any, Callable, Iterable, Tuple


class FieldProperty(GenericProperty):
    """
    
    A `FieldProperty` is a `Property` which is accessed as
    a field, without going through accessor methods (setX, getX). The field may
    have any scope (public, package, protected, private).
    """

    def __init__(self, field: "Field"):
        ...


    def set(self, object: "Object", value: "Object") -> None:
        ...


    def get(self, object: "Object") -> "Object":
        ...


    def getAnnotations(self) -> list["Annotation"]:
        ...


    def getAnnotation(self, annotationType: type["A"]) -> "A":
        ...
