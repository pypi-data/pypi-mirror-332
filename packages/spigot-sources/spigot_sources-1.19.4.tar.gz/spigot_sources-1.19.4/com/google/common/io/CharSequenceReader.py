"""
Python module generated from Java source file com.google.common.io.CharSequenceReader

Java source file obtained from artifact guava version 31.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtIncompatible
from com.google.common.io import *
from java.io import IOException
from java.io import Reader
from javax.annotation import CheckForNull
from typing import Any, Callable, Iterable, Tuple


class CharSequenceReader(Reader):

    def __init__(self, seq: "CharSequence"):
        """
        Creates a new reader wrapping the given character sequence.
        """
        ...


    def read(self, target: "CharBuffer") -> int:
        ...


    def read(self) -> int:
        ...


    def read(self, cbuf: list[str], off: int, len: int) -> int:
        ...


    def skip(self, n: int) -> int:
        ...


    def ready(self) -> bool:
        ...


    def markSupported(self) -> bool:
        ...


    def mark(self, readAheadLimit: int) -> None:
        ...


    def reset(self) -> None:
        ...


    def close(self) -> None:
        ...
