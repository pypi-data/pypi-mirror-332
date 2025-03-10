"""
Python module generated from Java source file com.google.common.base.CommonPattern

Java source file obtained from artifact guava version 31.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.base import *
from typing import Any, Callable, Iterable, Tuple


class CommonPattern:
    """
    The subset of the java.util.regex.Pattern API which is used by this package, and also
    shared with the `re2j` library. For internal use only. Please refer to the `Pattern`
    javadoc for details.
    """

    def matcher(self, t: "CharSequence") -> "CommonMatcher":
        ...


    def pattern(self) -> str:
        ...


    def flags(self) -> int:
        ...


    def toString(self) -> str:
        ...


    @staticmethod
    def compile(pattern: str) -> "CommonPattern":
        ...


    @staticmethod
    def isPcreLike() -> bool:
        ...
