"""
Python module generated from Java source file com.google.gson.internal.UnsafeAllocator

Java source file obtained from artifact gson version 2.10.1

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.gson.internal import *
from java.io import ObjectInputStream
from java.io import ObjectStreamClass
from java.lang.reflect import Field
from java.lang.reflect import Method
from typing import Any, Callable, Iterable, Tuple


class UnsafeAllocator:
    """
    Do sneaky things to allocate objects without invoking their constructors.

    Author(s)
    - Jesse Wilson
    """

    INSTANCE = create()


    def newInstance(self, c: type["T"]) -> "T":
        ...
