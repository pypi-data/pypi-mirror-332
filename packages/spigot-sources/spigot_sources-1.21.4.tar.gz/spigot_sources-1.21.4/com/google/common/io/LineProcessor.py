"""
Python module generated from Java source file com.google.common.io.LineProcessor

Java source file obtained from artifact guava version 33.3.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtIncompatible
from com.google.common.annotations import J2ktIncompatible
from com.google.common.io import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from java.io import IOException
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class LineProcessor:
    """
    A callback to be used with the streaming `readLines` methods.
    
    .processLine will be called for each line that is read, and should return `False` when you want to stop processing.

    Author(s)
    - Miles Barr

    Since
    - 1.0
    """

    def processLine(self, line: str) -> bool:
        """
        This method will be called once for each line.

        Arguments
        - line: the line read from the input, without delimiter

        Returns
        - True to continue processing, False to stop
        """
        ...


    def getResult(self) -> "T":
        """
        Return the result of processing all the lines.
        """
        ...
