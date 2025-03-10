"""
Python module generated from Java source file org.joml.ConfigurationException

Java source file obtained from artifact joml version 1.10.5

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.joml import *
from typing import Any, Callable, Iterable, Tuple


class ConfigurationException(RuntimeException):
    """
    Exception thrown when using an invalid JOML runtime configuration.

    Author(s)
    - Kai Burjack
    """

    def __init__(self, message: str, cause: "Throwable"):
        ...
