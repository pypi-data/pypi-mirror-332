"""
Python module generated from Java source file com.google.common.base.JdkPattern

Java source file obtained from artifact guava version 31.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtIncompatible
from com.google.common.base import *
from java.io import Serializable
from java.util.regex import Matcher
from java.util.regex import Pattern
from typing import Any, Callable, Iterable, Tuple


class JdkPattern(CommonPattern, Serializable):
    """
    A regex pattern implementation which is backed by the Pattern.
    """

    def matcher(self, t: "CharSequence") -> "CommonMatcher":
        ...


    def pattern(self) -> str:
        ...


    def flags(self) -> int:
        ...


    def toString(self) -> str:
        ...
