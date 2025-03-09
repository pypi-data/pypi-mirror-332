"""
Python module generated from Java source file com.google.common.escape.CharEscaperBuilder

Java source file obtained from artifact guava version 32.1.2-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.escape import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from javax.annotation import CheckForNull
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class CharEscaperBuilder:
    """
    Simple helper class to build a "sparse" array of objects based on the indexes that were added to
    it. The array will be from 0 to the maximum index given. All non-set indexes will contain null
    (so it's not really a sparse array, just a pseudo sparse array). The builder can also return a
    CharEscaper based on the generated array.

    Author(s)
    - Sven Mawson

    Since
    - 15.0
    """

    def __init__(self):
        """
        Construct a new sparse array builder.
        """
        ...


    def addEscape(self, c: str, r: str) -> "CharEscaperBuilder":
        """
        Add a new mapping from an index to an object to the escaping.
        """
        ...


    def addEscapes(self, cs: list[str], r: str) -> "CharEscaperBuilder":
        """
        Add multiple mappings at once for a particular index.
        """
        ...


    def toArray(self) -> list[list[str]]:
        """
        Convert this builder into an array of char[]s where the maximum index is the value of the
        highest character that has been seen. The array will be sparse in the sense that any unseen
        index will default to null.

        Returns
        - a "sparse" array that holds the replacement mappings.
        """
        ...


    def toEscaper(self) -> "Escaper":
        """
        Convert this builder into a char escaper which is just a decorator around the underlying array
        of replacement char[]s.

        Returns
        - an escaper that escapes based on the underlying array.
        """
        ...
