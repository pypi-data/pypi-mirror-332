"""
Python module generated from Java source file com.google.gson.annotations.JsonAdapter

Java source file obtained from artifact gson version 2.8.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.gson import TypeAdapter
from com.google.gson import TypeAdapterFactory
from com.google.gson.annotations import *
from typing import Any, Callable, Iterable, Tuple


class JsonAdapter:

    def value(self) -> type[Any]:
        """
        Either a TypeAdapter or TypeAdapterFactory.
        """
        ...


    def nullSafe(self) -> bool:
        """
        False, to be able to handle `null` values within the adapter, default value is True.
        """
        return True
