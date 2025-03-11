"""
Python module generated from Java source file com.google.gson.JsonNull

Java source file obtained from artifact gson version 2.11.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.gson import *
from typing import Any, Callable, Iterable, Tuple


class JsonNull(JsonElement):
    """
    A class representing a JSON `null` value.

    Author(s)
    - Joel Leitch

    Since
    - 1.2
    """

    INSTANCE = JsonNull()
    """
    Singleton for `JsonNull`.

    Since
    - 1.8
    """


    def __init__(self):
        """
        Creates a new `JsonNull` object.

        Deprecated
        - Deprecated since Gson version 1.8, use .INSTANCE instead.
        """
        ...


    def deepCopy(self) -> "JsonNull":
        """
        Returns the same instance since it is an immutable value.

        Since
        - 2.8.2
        """
        ...


    def hashCode(self) -> int:
        """
        All instances of `JsonNull` have the same hash code since they are indistinguishable.
        """
        ...


    def equals(self, other: "Object") -> bool:
        """
        All instances of `JsonNull` are considered equal.
        """
        ...
