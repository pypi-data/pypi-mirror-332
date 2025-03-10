"""
Python module generated from Java source file org.yaml.snakeyaml.error.MissingEnvironmentVariableException

Java source file obtained from artifact snakeyaml version 1.28

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.yaml.snakeyaml.error import *
from typing import Any, Callable, Iterable, Tuple


class MissingEnvironmentVariableException(YAMLException):
    """
    Indicate missing mandatory environment variable in the template
    Used by EnvScalarConstructor
    """

    def __init__(self, message: str):
        ...
