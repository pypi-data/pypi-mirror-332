"""
Python module generated from Java source file com.google.gson.internal.reflect.UnsafeReflectionAccessor

Java source file obtained from artifact gson version 2.8.9

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.gson import JsonIOException
from com.google.gson.internal.reflect import *
from java.lang.reflect import AccessibleObject
from java.lang.reflect import Field
from java.lang.reflect import Method
from typing import Any, Callable, Iterable, Tuple


class UnsafeReflectionAccessor(ReflectionAccessor):
    """
    An implementation of ReflectionAccessor based on Unsafe.
    
    NOTE: This implementation is designed for Java 9. Although it should work with earlier Java releases, it is better to
    use PreJava9ReflectionAccessor for them.
    """

    def makeAccessible(self, ao: "AccessibleObject") -> None:
        """

        """
        ...
