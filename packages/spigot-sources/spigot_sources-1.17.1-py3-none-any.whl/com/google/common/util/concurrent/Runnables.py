"""
Python module generated from Java source file com.google.common.util.concurrent.Runnables

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.annotations import GwtCompatible
from com.google.common.util.concurrent import *
from typing import Any, Callable, Iterable, Tuple


class Runnables:
    """
    Static utility methods pertaining to the Runnable interface.

    Since
    - 16.0
    """

    @staticmethod
    def doNothing() -> "Runnable":
        """
        Returns a Runnable instance that does nothing when run.
        """
        ...
