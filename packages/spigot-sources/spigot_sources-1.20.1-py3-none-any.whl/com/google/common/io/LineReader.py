"""
Python module generated from Java source file com.google.common.io.LineReader

Java source file obtained from artifact guava version 31.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.annotations import GwtIncompatible
from com.google.common.io import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from java.io import IOException
from java.io import Reader
from java.util import ArrayDeque
from java.util import Queue
from javax.annotation import CheckForNull
from typing import Any, Callable, Iterable, Tuple


class LineReader:
    """
    A class for reading lines of text. Provides the same functionality as java.io.BufferedReader.readLine() but for all Readable objects, not just instances of
    Reader.

    Author(s)
    - Chris Nokleberg

    Since
    - 1.0
    """

    def __init__(self, readable: "Readable"):
        """
        Creates a new instance that will read lines from the given `Readable` object.
        """
        ...


    def readLine(self) -> str:
        """
        Reads a line of text. A line is considered to be terminated by any one of a line feed (`'\n'`), a carriage return (`'\r'`), or a carriage return followed immediately by a
        linefeed (`"\r\n"`).

        Returns
        - a `String` containing the contents of the line, not including any
            line-termination characters, or `null` if the end of the stream has been reached.

        Raises
        - IOException: if an I/O error occurs
        """
        ...
