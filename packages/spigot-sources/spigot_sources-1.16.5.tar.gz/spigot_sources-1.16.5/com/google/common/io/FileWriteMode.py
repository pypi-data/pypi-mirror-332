"""
Python module generated from Java source file com.google.common.io.FileWriteMode

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtIncompatible
from com.google.common.io import *
from enum import Enum
from typing import Any, Callable, Iterable, Tuple


class FileWriteMode(Enum):
    """
    Modes for opening a file for writing. The default when mode when none is specified is to truncate
    the file before writing.

    Author(s)
    - Colin Decker
    """

    APPEND = 0
    """
    Specifies that writes to the opened file should append to the end of the file.
    """
