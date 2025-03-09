"""
Python module generated from Java source file org.yaml.snakeyaml.introspector.PropertySubstitute

Java source file obtained from artifact snakeyaml version 2.2

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.lang.reflect import Array
from java.lang.reflect import Field
from java.lang.reflect import Method
from java.lang.reflect import Modifier
from java.util import Arrays
from org.yaml.snakeyaml.error import YAMLException
from org.yaml.snakeyaml.internal import Logger
from org.yaml.snakeyaml.internal.Logger import Level
from org.yaml.snakeyaml.introspector import *
from typing import Any, Callable, Iterable, Tuple


class PropertySubstitute(Property):

    def __init__(self, name: str, type: type[Any], readMethod: str, writeMethod: str, *params: Tuple[type[Any], ...]):
        ...


    def __init__(self, name: str, type: type[Any], *params: Tuple[type[Any], ...]):
        ...


    def getActualTypeArguments(self) -> list[type[Any]]:
        ...


    def setActualTypeArguments(self, *args: Tuple[type[Any], ...]) -> None:
        ...


    def set(self, object: "Object", value: "Object") -> None:
        ...


    def get(self, object: "Object") -> "Object":
        ...


    def getAnnotations(self) -> list["Annotation"]:
        ...


    def getAnnotation(self, annotationType: type["A"]) -> "A":
        ...


    def setTargetType(self, targetType: type[Any]) -> None:
        ...


    def getName(self) -> str:
        ...


    def getType(self) -> type[Any]:
        ...


    def isReadable(self) -> bool:
        ...


    def isWritable(self) -> bool:
        ...


    def setDelegate(self, delegate: "Property") -> None:
        ...
