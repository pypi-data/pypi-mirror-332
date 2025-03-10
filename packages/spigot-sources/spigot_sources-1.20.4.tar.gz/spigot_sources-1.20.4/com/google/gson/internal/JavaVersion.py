"""
Python module generated from Java source file com.google.gson.internal.JavaVersion

Java source file obtained from artifact gson version 2.10.1

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.gson.internal import *
from typing import Any, Callable, Iterable, Tuple


class JavaVersion:
    """
    Utility to check the major Java version of the current JVM.
    """

    @staticmethod
    def getMajorJavaVersion() -> int:
        """
        Returns
        - the major Java version, i.e. '8' for Java 1.8, '9' for Java 9 etc.
        """
        ...


    @staticmethod
    def isJava9OrLater() -> bool:
        """
        Returns
        - `True` if the application is running on Java 9 or later; and `False` otherwise.
        """
        ...
