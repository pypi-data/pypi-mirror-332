"""
Python module generated from Java source file com.google.gson.internal.reflect.ReflectionAccessor

Java source file obtained from artifact gson version 2.8.9

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.gson.internal import JavaVersion
from com.google.gson.internal.reflect import *
from java.lang.reflect import AccessibleObject
from typing import Any, Callable, Iterable, Tuple


class ReflectionAccessor:
    """
    Provides a replacement for AccessibleObject.setAccessible(boolean), which may be used to
    avoid reflective access issues appeared in Java 9, like java.lang.reflect.InaccessibleObjectException
    thrown or warnings like
    ```
      WARNING: An illegal reflective access operation has occurred
      WARNING: Illegal reflective access by ...
    ```
    <p/>
    Works both for Java 9 and earlier Java versions.
    """

    def makeAccessible(self, ao: "AccessibleObject") -> None:
        """
        Does the same as `ao.setAccessible(True)`, but never throws
        java.lang.reflect.InaccessibleObjectException
        """
        ...


    @staticmethod
    def getInstance() -> "ReflectionAccessor":
        """
        Obtains a ReflectionAccessor instance suitable for the current Java version.
        
        You may need one a reflective operation in your code throws java.lang.reflect.InaccessibleObjectException.
        In such a case, use ReflectionAccessor.makeAccessible(AccessibleObject) on a field, method or constructor
        (instead of basic AccessibleObject.setAccessible(boolean)).
        """
        ...
