"""
Python module generated from Java source file com.google.common.base.PatternCompiler

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtIncompatible
from com.google.common.base import *
from typing import Any, Callable, Iterable, Tuple


class PatternCompiler:
    """
    Pluggable interface for compiling a regex pattern. By default this package uses the
    `java.util.regex` library, but an alternate implementation can be supplied
    using the java.util.ServiceLoader mechanism.
    """

    def compile(self, pattern: str) -> "CommonPattern":
        """
        Compiles the given pattern.

        Raises
        - IllegalArgumentException: if the pattern is invalid
        """
        ...
