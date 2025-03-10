"""
Python module generated from Java source file com.google.gson.internal.reflect.PreJava9ReflectionAccessor

Java source file obtained from artifact gson version 2.8.9

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.gson.internal.reflect import *
from java.lang.reflect import AccessibleObject
from typing import Any, Callable, Iterable, Tuple


class PreJava9ReflectionAccessor(ReflectionAccessor):
    """
    A basic implementation of ReflectionAccessor which is suitable for Java 8 and below.
    
    This implementation just calls AccessibleObject.setAccessible(boolean) setAccessible(True), which worked
    fine before Java 9.
    """

    def makeAccessible(self, ao: "AccessibleObject") -> None:
        """

        """
        ...
