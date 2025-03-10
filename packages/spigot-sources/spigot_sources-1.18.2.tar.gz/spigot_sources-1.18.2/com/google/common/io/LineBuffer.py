"""
Python module generated from Java source file com.google.common.io.LineBuffer

Java source file obtained from artifact guava version 31.0.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtIncompatible
from com.google.common.io import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from java.io import IOException
from typing import Any, Callable, Iterable, Tuple


class LineBuffer:
    """
    Package-protected abstract class that implements the line reading algorithm used by LineReader. Line separators are per java.io.BufferedReader: line feed, carriage return,
    or carriage return followed immediately by a linefeed.
    
    Subclasses must implement .handleLine, call .add to pass character data, and
    call .finish at the end of stream.

    Author(s)
    - Chris Nokleberg

    Since
    - 1.0
    """


