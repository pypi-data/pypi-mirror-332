"""
Python module generated from Java source file com.google.common.base.CaseFormat

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.base import *
from enum import Enum
from java.io import Serializable
from javax.annotation import Nullable
from typing import Any, Callable, Iterable, Tuple


class CaseFormat(Enum):
    """
    Utility class for converting between various ASCII case formats. Behavior is undefined for
    non-ASCII input.

    Author(s)
    - Mike Bostock

    Since
    - 1.0
    """

    LOWER_HYPHEN = (CharMatcher.is('-'), "-")
    """
    Hyphenated variable naming convention, e.g., "lower-hyphen".
    """
    LOWER_UNDERSCORE = (CharMatcher.is('_'), "_")
    """
    C++ variable naming convention, e.g., "lower_underscore".
    """
    LOWER_CAMEL = (CharMatcher.inRange('A', 'Z'), "")
    """
    Java variable naming convention, e.g., "lowerCamel".
    """
    UPPER_CAMEL = (CharMatcher.inRange('A', 'Z'), "")
    """
    Java and C++ class naming convention, e.g., "UpperCamel".
    """
    UPPER_UNDERSCORE = (CharMatcher.is('_'), "_")
    """
    Java and C++ constant naming convention, e.g., "UPPER_UNDERSCORE".
    """


    def to(self, format: "CaseFormat", str: str) -> str:
        """
        Converts the specified `String str` from this format to the specified `format`. A
        "best effort" approach is taken; if `str` does not conform to the assumed format, then
        the behavior of this method is undefined but we make a reasonable effort at converting anyway.
        """
        ...


    def converterTo(self, targetFormat: "CaseFormat") -> "Converter"[str, str]:
        """
        Returns a `Converter` that converts strings from this format to `targetFormat`.

        Since
        - 16.0
        """
        ...
