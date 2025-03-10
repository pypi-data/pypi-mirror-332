"""
Python module generated from Java source file org.yaml.snakeyaml.introspector.GenericProperty

Java source file obtained from artifact snakeyaml version 1.28

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.lang.reflect import Array
from java.lang.reflect import GenericArrayType
from java.lang.reflect import ParameterizedType
from java.lang.reflect import Type
from org.yaml.snakeyaml.introspector import *
from typing import Any, Callable, Iterable, Tuple


class GenericProperty(Property):

    def __init__(self, name: str, aClass: type[Any], aType: "Type"):
        ...


    def getActualTypeArguments(self) -> list[type[Any]]:
        ...
