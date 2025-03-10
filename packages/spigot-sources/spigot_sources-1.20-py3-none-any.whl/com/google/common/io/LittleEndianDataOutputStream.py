"""
Python module generated from Java source file com.google.common.io.LittleEndianDataOutputStream

Java source file obtained from artifact guava version 31.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.annotations import GwtIncompatible
from com.google.common.base import Preconditions
from com.google.common.io import *
from com.google.common.primitives import Longs
from java.io import DataOutput
from java.io import DataOutputStream
from java.io import FilterOutputStream
from java.io import IOException
from java.io import OutputStream
from typing import Any, Callable, Iterable, Tuple


class LittleEndianDataOutputStream(FilterOutputStream, DataOutput):
    """
    An implementation of DataOutput that uses little-endian byte ordering for writing `char`, `short`, `int`, `float`, `double`, and `long` values.
    
    **Note:** This class intentionally violates the specification of its supertype `DataOutput`, which explicitly requires big-endian byte order.

    Author(s)
    - Keith Bottner

    Since
    - 8.0
    """

    def __init__(self, out: "OutputStream"):
        """
        Creates a `LittleEndianDataOutputStream` that wraps the given stream.

        Arguments
        - out: the stream to delegate to
        """
        ...


    def write(self, b: list[int], off: int, len: int) -> None:
        ...


    def writeBoolean(self, v: bool) -> None:
        ...


    def writeByte(self, v: int) -> None:
        ...


    def writeBytes(self, s: str) -> None:
        """
        Deprecated
        - The semantics of `writeBytes(String s)` are considered dangerous. Please use
            .writeUTF(String s), .writeChars(String s) or another write method instead.
        """
        ...


    def writeChar(self, v: int) -> None:
        """
        Writes a char as specified by DataOutputStream.writeChar(int), except using
        little-endian byte order.

        Raises
        - IOException: if an I/O error occurs
        """
        ...


    def writeChars(self, s: str) -> None:
        """
        Writes a `String` as specified by DataOutputStream.writeChars(String), except
        each character is written using little-endian byte order.

        Raises
        - IOException: if an I/O error occurs
        """
        ...


    def writeDouble(self, v: float) -> None:
        """
        Writes a `double` as specified by DataOutputStream.writeDouble(double), except
        using little-endian byte order.

        Raises
        - IOException: if an I/O error occurs
        """
        ...


    def writeFloat(self, v: float) -> None:
        """
        Writes a `float` as specified by DataOutputStream.writeFloat(float), except using
        little-endian byte order.

        Raises
        - IOException: if an I/O error occurs
        """
        ...


    def writeInt(self, v: int) -> None:
        """
        Writes an `int` as specified by DataOutputStream.writeInt(int), except using
        little-endian byte order.

        Raises
        - IOException: if an I/O error occurs
        """
        ...


    def writeLong(self, v: int) -> None:
        """
        Writes a `long` as specified by DataOutputStream.writeLong(long), except using
        little-endian byte order.

        Raises
        - IOException: if an I/O error occurs
        """
        ...


    def writeShort(self, v: int) -> None:
        """
        Writes a `short` as specified by DataOutputStream.writeShort(int), except using
        little-endian byte order.

        Raises
        - IOException: if an I/O error occurs
        """
        ...


    def writeUTF(self, str: str) -> None:
        ...


    def close(self) -> None:
        ...
