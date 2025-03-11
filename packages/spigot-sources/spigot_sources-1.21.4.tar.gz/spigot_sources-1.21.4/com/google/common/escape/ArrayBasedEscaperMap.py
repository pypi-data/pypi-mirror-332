"""
Python module generated from Java source file com.google.common.escape.ArrayBasedEscaperMap

Java source file obtained from artifact guava version 33.3.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.annotations import VisibleForTesting
from com.google.common.escape import *
from java.util import Collections
from typing import Any, Callable, Iterable, Tuple


class ArrayBasedEscaperMap:
    """
    An implementation-specific parameter class suitable for initializing ArrayBasedCharEscaper or ArrayBasedUnicodeEscaper instances. This class should be used
    when more than one escaper is created using the same character replacement mapping to allow the
    underlying (implementation specific) data structures to be shared.
    
    The size of the data structure used by ArrayBasedCharEscaper and ArrayBasedUnicodeEscaper is
    proportional to the highest valued character that has a replacement. For example a replacement
    map containing the single character '\u1000' will require approximately 16K of memory.
    As such sharing this data structure between escaper instances is the primary goal of this class.

    Author(s)
    - David Beaumont

    Since
    - 15.0
    """

    @staticmethod
    def create(replacements: dict["Character", str]) -> "ArrayBasedEscaperMap":
        """
        Returns a new ArrayBasedEscaperMap for creating ArrayBasedCharEscaper or
        ArrayBasedUnicodeEscaper instances.

        Arguments
        - replacements: a map of characters to their escaped representations
        """
        ...
