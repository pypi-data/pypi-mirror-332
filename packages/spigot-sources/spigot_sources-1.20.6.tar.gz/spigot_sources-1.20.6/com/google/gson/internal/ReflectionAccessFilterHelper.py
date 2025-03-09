"""
Python module generated from Java source file com.google.gson.internal.ReflectionAccessFilterHelper

Java source file obtained from artifact gson version 2.10.1

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.gson import ReflectionAccessFilter
from com.google.gson.ReflectionAccessFilter import FilterResult
from com.google.gson.internal import *
from java.lang.reflect import AccessibleObject
from java.lang.reflect import Method
from typing import Any, Callable, Iterable, Tuple


class ReflectionAccessFilterHelper:
    """
    Internal helper class for ReflectionAccessFilter.
    """

    @staticmethod
    def isJavaType(c: type[Any]) -> bool:
        ...


    @staticmethod
    def isAndroidType(c: type[Any]) -> bool:
        ...


    @staticmethod
    def isAnyPlatformType(c: type[Any]) -> bool:
        ...


    @staticmethod
    def getFilterResult(reflectionFilters: list["ReflectionAccessFilter"], c: type[Any]) -> "FilterResult":
        """
        Gets the result of applying all filters until the first one returns a result
        other than FilterResult.INDECISIVE, or FilterResult.ALLOW if
        the list of filters is empty or all returned `INDECISIVE`.
        """
        ...


    @staticmethod
    def canAccess(accessibleObject: "AccessibleObject", object: "Object") -> bool:
        """
        See AccessibleObject.canAccess(Object) (Java >= 9)
        """
        ...
