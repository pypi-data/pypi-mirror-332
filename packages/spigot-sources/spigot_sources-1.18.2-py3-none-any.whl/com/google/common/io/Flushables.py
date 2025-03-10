"""
Python module generated from Java source file com.google.common.io.Flushables

Java source file obtained from artifact guava version 31.0.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.annotations import GwtIncompatible
from com.google.common.io import *
from java.io import Flushable
from java.io import IOException
from typing import Any, Callable, Iterable, Tuple


class Flushables:
    """
    Utility methods for working with Flushable objects.

    Author(s)
    - Michael Lancaster

    Since
    - 1.0
    """

    @staticmethod
    def flush(flushable: "Flushable", swallowIOException: bool) -> None:
        """
        Flush a Flushable, with control over whether an `IOException` may be thrown.
        
        If `swallowIOException` is True, then we don't rethrow `IOException`, but merely
        log it.

        Arguments
        - flushable: the `Flushable` object to be flushed.
        - swallowIOException: if True, don't propagate IO exceptions thrown by the `flush`
            method

        Raises
        - IOException: if `swallowIOException` is False and Flushable.flush throws
            an `IOException`.

        See
        - Closeables.close
        """
        ...


    @staticmethod
    def flushQuietly(flushable: "Flushable") -> None:
        """
        Equivalent to calling `flush(flushable, True)`, but with no `IOException` in the
        signature.

        Arguments
        - flushable: the `Flushable` object to be flushed.
        """
        ...
