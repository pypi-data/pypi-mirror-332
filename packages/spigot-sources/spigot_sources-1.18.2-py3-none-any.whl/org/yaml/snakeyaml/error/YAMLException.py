"""
Python module generated from Java source file org.yaml.snakeyaml.error.YAMLException

Java source file obtained from artifact snakeyaml version 1.30

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.yaml.snakeyaml.error import *
from typing import Any, Callable, Iterable, Tuple


class YAMLException(RuntimeException):

    def __init__(self, message: str):
        ...


    def __init__(self, cause: "Throwable"):
        ...


    def __init__(self, message: str, cause: "Throwable"):
        ...
