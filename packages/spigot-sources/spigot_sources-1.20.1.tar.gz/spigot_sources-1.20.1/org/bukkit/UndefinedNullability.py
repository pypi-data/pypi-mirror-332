"""
Python module generated from Java source file org.bukkit.UndefinedNullability

Java source file obtained from artifact spigot-api version 1.20.1-R0.1-20230921.163938-66

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import *
from typing import Any, Callable, Iterable, Tuple


class UndefinedNullability:
    """
    Annotation for types, whose nullability is not well defined, so
    org.jetbrains.annotations.NotNull nor
    org.jetbrains.annotations.Nullable is applicable. For example when
    interface defines a method, whose nullability depends on the implementation.

    Deprecated
    - This should generally not be used in any new API code as it
    suggests a bad API design.
    """

    def value(self) -> str:
        """
        Human readable description of the circumstances, in which the type is
        nullable.

        Returns
        - description
        """
        return ""
