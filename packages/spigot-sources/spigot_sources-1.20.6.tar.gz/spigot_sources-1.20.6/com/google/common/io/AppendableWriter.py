"""
Python module generated from Java source file com.google.common.io.AppendableWriter

Java source file obtained from artifact guava version 32.1.2-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtIncompatible
from com.google.common.annotations import J2ktIncompatible
from com.google.common.io import *
from java.io import Closeable
from java.io import Flushable
from java.io import IOException
from java.io import Writer
from javax.annotation import CheckForNull
from typing import Any, Callable, Iterable, Tuple


class AppendableWriter(Writer):
    """
    Writer that places all output on an Appendable target. If the target is Flushable
    or Closeable, flush()es and close()s will also be delegated to the target.

    Author(s)
    - Sebastian Kanthak

    Since
    - 1.0
    """

    def write(self, cbuf: list[str], off: int, len: int) -> None:
        ...


    def write(self, c: int) -> None:
        ...


    def write(self, str: str) -> None:
        ...


    def write(self, str: str, off: int, len: int) -> None:
        ...


    def flush(self) -> None:
        ...


    def close(self) -> None:
        ...


    def append(self, c: str) -> "Writer":
        ...


    def append(self, charSeq: "CharSequence") -> "Writer":
        ...


    def append(self, charSeq: "CharSequence", start: int, end: int) -> "Writer":
        ...
