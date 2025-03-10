"""
Python module generated from Java source file com.google.common.io.ByteArrayDataInput

Java source file obtained from artifact guava version 32.1.2-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtIncompatible
from com.google.common.annotations import J2ktIncompatible
from com.google.common.io import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from java.io import DataInput
from java.io import IOException
from javax.annotation import CheckForNull
from typing import Any, Callable, Iterable, Tuple


class ByteArrayDataInput(DataInput):
    """
    An extension of `DataInput` for reading from in-memory byte arrays; its methods offer
    identical functionality but do not throw IOException.
    
    **Warning:** The caller is responsible for not attempting to read past the end of the
    array. If any method encounters the end of the array prematurely, it throws IllegalStateException to signify *programmer error*. This behavior is a technical violation
    of the supertype's contract, which specifies a checked exception.

    Author(s)
    - Kevin Bourrillion

    Since
    - 1.0
    """

    def readFully(self, b: list[int]) -> None:
        ...


    def readFully(self, b: list[int], off: int, len: int) -> None:
        ...


    def skipBytes(self, n: int) -> int:
        ...


    def readBoolean(self) -> bool:
        ...


    def readByte(self) -> int:
        ...


    def readUnsignedByte(self) -> int:
        ...


    def readShort(self) -> int:
        ...


    def readUnsignedShort(self) -> int:
        ...


    def readChar(self) -> str:
        ...


    def readInt(self) -> int:
        ...


    def readLong(self) -> int:
        ...


    def readFloat(self) -> float:
        ...


    def readDouble(self) -> float:
        ...


    def readLine(self) -> str:
        ...


    def readUTF(self) -> str:
        ...
