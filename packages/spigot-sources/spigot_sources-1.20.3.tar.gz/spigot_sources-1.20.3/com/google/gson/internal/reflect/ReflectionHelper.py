"""
Python module generated from Java source file com.google.gson.internal.reflect.ReflectionHelper

Java source file obtained from artifact gson version 2.10.1

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.gson import JsonIOException
from com.google.gson.internal import GsonBuildConfig
from com.google.gson.internal.reflect import *
from java.lang.reflect import AccessibleObject
from java.lang.reflect import Constructor
from java.lang.reflect import Field
from java.lang.reflect import Method
from typing import Any, Callable, Iterable, Tuple


class ReflectionHelper:

    @staticmethod
    def makeAccessible(object: "AccessibleObject") -> None:
        """
        Internal implementation of making an AccessibleObject accessible.

        Arguments
        - object: the object that AccessibleObject.setAccessible(boolean) should be called on.

        Raises
        - JsonIOException: if making the object accessible fails
        """
        ...


    @staticmethod
    def getAccessibleObjectDescription(object: "AccessibleObject", uppercaseFirstLetter: bool) -> str:
        """
        Returns a short string describing the AccessibleObject in a human-readable way.
        The result is normally shorter than AccessibleObject.toString() because it omits
        modifiers (e.g. `final`) and uses simple names for constructor and method parameter
        types.

        Arguments
        - object: object to describe
        - uppercaseFirstLetter: whether the first letter of the description should be uppercased
        """
        ...


    @staticmethod
    def fieldToString(field: "Field") -> str:
        """
        Creates a string representation for a field, omitting modifiers and
        the field type.
        """
        ...


    @staticmethod
    def constructorToString(constructor: "Constructor"[Any]) -> str:
        """
        Creates a string representation for a constructor.
        E.g.: `java.lang.String(char[], int, int)`
        """
        ...


    @staticmethod
    def tryMakeAccessible(constructor: "Constructor"[Any]) -> str:
        """
        Tries making the constructor accessible, returning an exception message
        if this fails.

        Arguments
        - constructor: constructor to make accessible

        Returns
        - exception message; `null` if successful, non-`null` if
           unsuccessful
        """
        ...


    @staticmethod
    def isRecord(raw: type[Any]) -> bool:
        """
        If records are supported on the JVM, this is equivalent to a call to Class.isRecord()
        """
        ...


    @staticmethod
    def getRecordComponentNames(raw: type[Any]) -> list[str]:
        ...


    @staticmethod
    def getAccessor(raw: type[Any], field: "Field") -> "Method":
        """
        Looks up the record accessor method that corresponds to the given record field
        """
        ...


    @staticmethod
    def getCanonicalRecordConstructor(raw: type["T"]) -> "Constructor"["T"]:
        ...


    @staticmethod
    def createExceptionForUnexpectedIllegalAccess(exception: "IllegalAccessException") -> "RuntimeException":
        ...
