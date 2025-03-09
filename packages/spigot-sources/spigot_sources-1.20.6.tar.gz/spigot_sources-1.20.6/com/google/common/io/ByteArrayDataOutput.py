"""
Python module generated from Java source file com.google.common.io.ByteArrayDataOutput

Java source file obtained from artifact guava version 32.1.2-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtIncompatible
from com.google.common.annotations import J2ktIncompatible
from com.google.common.io import *
from java.io import DataOutput
from java.io import IOException
from typing import Any, Callable, Iterable, Tuple


class ByteArrayDataOutput(DataOutput):
    """
    An extension of `DataOutput` for writing to in-memory byte arrays; its methods offer
    identical functionality but do not throw IOException.

    Author(s)
    - Jayaprabhakar Kadarkarai

    Since
    - 1.0
    """

    def write(self, b: int) -> None:
        ...


    def write(self, b: list[int]) -> None:
        ...


    def write(self, b: list[int], off: int, len: int) -> None:
        ...


    def writeBoolean(self, v: bool) -> None:
        ...


    def writeByte(self, v: int) -> None:
        ...


    def writeShort(self, v: int) -> None:
        ...


    def writeChar(self, v: int) -> None:
        ...


    def writeInt(self, v: int) -> None:
        ...


    def writeLong(self, v: int) -> None:
        ...


    def writeFloat(self, v: float) -> None:
        ...


    def writeDouble(self, v: float) -> None:
        ...


    def writeChars(self, s: str) -> None:
        ...


    def writeUTF(self, s: str) -> None:
        ...


    def writeBytes(self, s: str) -> None:
        """
        Deprecated
        - This method is dangerous as it discards the high byte of every character. For
            UTF-8, use `write(s.getBytes(StandardCharsets.UTF_8))`.
        """
        ...


    def toByteArray(self) -> list[int]:
        """
        Returns the contents that have been written to this instance, as a byte array.
        """
        ...
