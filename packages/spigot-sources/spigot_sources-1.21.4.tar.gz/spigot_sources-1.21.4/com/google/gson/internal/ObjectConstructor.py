"""
Python module generated from Java source file com.google.gson.internal.ObjectConstructor

Java source file obtained from artifact gson version 2.11.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.gson.internal import *
from typing import Any, Callable, Iterable, Tuple


class ObjectConstructor:
    """
    Defines a generic object construction factory. The purpose of this class is to construct a
    default instance of a class that can be used for object navigation while deserialization from its
    JSON representation.

    Author(s)
    - Joel Leitch
    """

    def construct(self) -> "T":
        """
        Returns a new instance.
        """
        ...
