"""
Python module generated from Java source file com.google.common.io.MultiReader

Java source file obtained from artifact guava version 31.0.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtIncompatible
from com.google.common.base import Preconditions
from com.google.common.io import *
from java.io import IOException
from java.io import Reader
from java.util import Iterator
from javax.annotation import CheckForNull
from typing import Any, Callable, Iterable, Tuple


class MultiReader(Reader):
    """
    A Reader that concatenates multiple readers.

    Author(s)
    - Bin Zhu

    Since
    - 1.0
    """

    def read(self, cbuf: list[str], off: int, len: int) -> int:
        ...


    def skip(self, n: int) -> int:
        ...


    def ready(self) -> bool:
        ...


    def close(self) -> None:
        ...
