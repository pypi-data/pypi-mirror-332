"""
Python module generated from Java source file org.yaml.snakeyaml.introspector.PropertyUtils

Java source file obtained from artifact snakeyaml version 2.2

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.lang.reflect import Field
from java.lang.reflect import Method
from java.lang.reflect import Modifier
from org.yaml.snakeyaml.error import YAMLException
from org.yaml.snakeyaml.introspector import *
from org.yaml.snakeyaml.util import PlatformFeatureDetector
from typing import Any, Callable, Iterable, Tuple


class PropertyUtils:

    def __init__(self):
        ...


    def getProperties(self, type: type["Object"]) -> set["Property"]:
        ...


    def getProperties(self, type: type["Object"], bAccess: "BeanAccess") -> set["Property"]:
        ...


    def getProperty(self, type: type["Object"], name: str) -> "Property":
        ...


    def getProperty(self, type: type["Object"], name: str, bAccess: "BeanAccess") -> "Property":
        ...


    def setBeanAccess(self, beanAccess: "BeanAccess") -> None:
        ...


    def setAllowReadOnlyProperties(self, allowReadOnlyProperties: bool) -> None:
        ...


    def isAllowReadOnlyProperties(self) -> bool:
        ...


    def setSkipMissingProperties(self, skipMissingProperties: bool) -> None:
        """
        Skip properties that are missing during deserialization of YAML to a Java object. The default
        is False.

        Arguments
        - skipMissingProperties: True if missing properties should be skipped, False otherwise.
        """
        ...


    def isSkipMissingProperties(self) -> bool:
        ...
