"""
Python module generated from Java source file com.google.common.base.Defaults

Java source file obtained from artifact guava version 33.3.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtIncompatible
from com.google.common.annotations import J2ktIncompatible
from com.google.common.base import *
from javax.annotation import CheckForNull
from typing import Any, Callable, Iterable, Tuple


class Defaults:
    """
    This class provides default values for all Java types, as defined by the JLS.

    Author(s)
    - Ben Yu

    Since
    - 1.0
    """

    @staticmethod
    def defaultValue(type: type["T"]) -> "T":
        """
        Returns the default value of `type` as defined by JLS --- `0` for numbers, `False` for `boolean` and `'\0'` for `char`. For non-primitive types and
        `void`, `null` is returned.
        """
        ...
