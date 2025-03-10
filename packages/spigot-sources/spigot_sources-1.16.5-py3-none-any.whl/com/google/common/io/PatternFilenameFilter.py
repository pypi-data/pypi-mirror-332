"""
Python module generated from Java source file com.google.common.io.PatternFilenameFilter

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.annotations import GwtIncompatible
from com.google.common.base import Preconditions
from com.google.common.io import *
from java.io import File
from java.io import FilenameFilter
from java.util.regex import Pattern
from java.util.regex import PatternSyntaxException
from javax.annotation import Nullable
from typing import Any, Callable, Iterable, Tuple


class PatternFilenameFilter(FilenameFilter):
    """
    File name filter that only accepts files matching a regular expression. This class is thread-safe
    and immutable.

    Author(s)
    - Apple Chow

    Since
    - 1.0
    """

    def __init__(self, patternStr: str):
        """
        Constructs a pattern file name filter object.

        Arguments
        - patternStr: the pattern string on which to filter file names

        Raises
        - PatternSyntaxException: if pattern compilation fails (runtime)
        """
        ...


    def __init__(self, pattern: "Pattern"):
        """
        Constructs a pattern file name filter object.

        Arguments
        - pattern: the pattern on which to filter file names
        """
        ...


    def accept(self, dir: "File", fileName: str) -> bool:
        ...
