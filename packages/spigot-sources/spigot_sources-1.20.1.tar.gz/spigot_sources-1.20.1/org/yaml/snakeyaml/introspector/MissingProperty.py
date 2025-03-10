"""
Python module generated from Java source file org.yaml.snakeyaml.introspector.MissingProperty

Java source file obtained from artifact snakeyaml version 2.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util import Collections
from org.yaml.snakeyaml.introspector import *
from typing import Any, Callable, Iterable, Tuple


class MissingProperty(Property):
    """
    A property that does not map to a real property; this is used when
    PropertyUtils.setSkipMissingProperties(boolean) is set to True.
    """

    def __init__(self, name: str):
        ...


    def getActualTypeArguments(self) -> list[type[Any]]:
        ...


    def set(self, object: "Object", value: "Object") -> None:
        """
        Setter does nothing.
        """
        ...


    def get(self, object: "Object") -> "Object":
        ...


    def getAnnotations(self) -> list["Annotation"]:
        ...


    def getAnnotation(self, annotationType: type["A"]) -> "A":
        ...
