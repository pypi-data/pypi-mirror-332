"""
Python module generated from Java source file com.google.common.hash.AbstractCompositeHashFunction

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.hash import *
from java.nio.charset import Charset
from typing import Any, Callable, Iterable, Tuple


class AbstractCompositeHashFunction(AbstractStreamingHashFunction):
    """
    An abstract composition of multiple hash functions. .newHasher() delegates to the
    `Hasher` objects of the delegate hash functions, and in the end, they are used by
    .makeHash(Hasher[]) that constructs the final `HashCode`.

    Author(s)
    - Dimitris Andreou
    """

    def newHasher(self) -> "Hasher":
        ...
