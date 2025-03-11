"""
Python module generated from Java source file com.google.common.io.ReaderInputStream

Java source file obtained from artifact guava version 33.3.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtIncompatible
from com.google.common.annotations import J2ktIncompatible
from com.google.common.io import *
from com.google.common.primitives import UnsignedBytes
from java.io import IOException
from java.io import InputStream
from java.io import Reader
from java.nio.charset import Charset
from java.nio.charset import CharsetEncoder
from java.nio.charset import CoderResult
from java.nio.charset import CodingErrorAction
from java.util import Arrays
from typing import Any, Callable, Iterable, Tuple


class ReaderInputStream(InputStream):
    """
    An InputStream that converts characters from a Reader into bytes using an
    arbitrary Charset.
    
    This is an alternative to copying the data to an `OutputStream` via a `Writer`,
    which is necessarily blocking. By implementing an `InputStream` it allows consumers to
    "pull" as much data as they can handle, which is more convenient when dealing with flow
    controlled, async APIs.

    Author(s)
    - Chris Nokleberg
    """

    def close(self) -> None:
        ...


    def read(self) -> int:
        ...


    def read(self, b: list[int], off: int, len: int) -> int:
        ...
