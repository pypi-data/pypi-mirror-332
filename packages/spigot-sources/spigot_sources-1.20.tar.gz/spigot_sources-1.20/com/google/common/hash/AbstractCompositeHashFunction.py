"""
Python module generated from Java source file com.google.common.hash.AbstractCompositeHashFunction

Java source file obtained from artifact guava version 31.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.hash import *
from com.google.errorprone.annotations import Immutable
from java.nio.charset import Charset
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class AbstractCompositeHashFunction(AbstractHashFunction):
    """
    An abstract composition of multiple hash functions. .newHasher() delegates to the
    `Hasher` objects of the delegate hash functions, and in the end, they are used by
    .makeHash(Hasher[]) that constructs the final `HashCode`.

    Author(s)
    - Dimitris Andreou
    """

    def newHasher(self) -> "Hasher":
        ...


    def newHasher(self, expectedInputSize: int) -> "Hasher":
        ...
