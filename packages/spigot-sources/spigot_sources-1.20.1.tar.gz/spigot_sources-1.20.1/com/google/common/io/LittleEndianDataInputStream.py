"""
Python module generated from Java source file com.google.common.io.LittleEndianDataInputStream

Java source file obtained from artifact guava version 31.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.annotations import GwtIncompatible
from com.google.common.base import Preconditions
from com.google.common.io import *
from com.google.common.primitives import Ints
from com.google.common.primitives import Longs
from com.google.errorprone.annotations import CanIgnoreReturnValue
from com.google.errorprone.annotations import DoNotCall
from java.io import DataInput
from java.io import DataInputStream
from java.io import EOFException
from java.io import FilterInputStream
from java.io import IOException
from java.io import InputStream
from typing import Any, Callable, Iterable, Tuple


class LittleEndianDataInputStream(FilterInputStream, DataInput):
    """
    An implementation of DataInput that uses little-endian byte ordering for reading `short`, `int`, `float`, `double`, and `long` values.
    
    **Note:** This class intentionally violates the specification of its supertype `DataInput`, which explicitly requires big-endian byte order.

    Author(s)
    - Keith Bottner

    Since
    - 8.0
    """

    def __init__(self, in: "InputStream"):
        """
        Creates a `LittleEndianDataInputStream` that wraps the given stream.

        Arguments
        - in: the stream to delegate to
        """
        ...


    def readLine(self) -> str:
        """
        This method will throw an UnsupportedOperationException.
        """
        ...


    def readFully(self, b: list[int]) -> None:
        ...


    def readFully(self, b: list[int], off: int, len: int) -> None:
        ...


    def skipBytes(self, n: int) -> int:
        ...


    def readUnsignedByte(self) -> int:
        ...


    def readUnsignedShort(self) -> int:
        """
        Reads an unsigned `short` as specified by DataInputStream.readUnsignedShort(),
        except using little-endian byte order.

        Returns
        - the next two bytes of the input stream, interpreted as an unsigned 16-bit integer in
            little-endian byte order

        Raises
        - IOException: if an I/O error occurs
        """
        ...


    def readInt(self) -> int:
        """
        Reads an integer as specified by DataInputStream.readInt(), except using little-endian
        byte order.

        Returns
        - the next four bytes of the input stream, interpreted as an `int` in little-endian
            byte order

        Raises
        - IOException: if an I/O error occurs
        """
        ...


    def readLong(self) -> int:
        """
        Reads a `long` as specified by DataInputStream.readLong(), except using
        little-endian byte order.

        Returns
        - the next eight bytes of the input stream, interpreted as a `long` in
            little-endian byte order

        Raises
        - IOException: if an I/O error occurs
        """
        ...


    def readFloat(self) -> float:
        """
        Reads a `float` as specified by DataInputStream.readFloat(), except using
        little-endian byte order.

        Returns
        - the next four bytes of the input stream, interpreted as a `float` in
            little-endian byte order

        Raises
        - IOException: if an I/O error occurs
        """
        ...


    def readDouble(self) -> float:
        """
        Reads a `double` as specified by DataInputStream.readDouble(), except using
        little-endian byte order.

        Returns
        - the next eight bytes of the input stream, interpreted as a `double` in
            little-endian byte order

        Raises
        - IOException: if an I/O error occurs
        """
        ...


    def readUTF(self) -> str:
        ...


    def readShort(self) -> int:
        """
        Reads a `short` as specified by DataInputStream.readShort(), except using
        little-endian byte order.

        Returns
        - the next two bytes of the input stream, interpreted as a `short` in little-endian
            byte order.

        Raises
        - IOException: if an I/O error occurs.
        """
        ...


    def readChar(self) -> str:
        """
        Reads a char as specified by DataInputStream.readChar(), except using little-endian
        byte order.

        Returns
        - the next two bytes of the input stream, interpreted as a `char` in little-endian
            byte order

        Raises
        - IOException: if an I/O error occurs
        """
        ...


    def readByte(self) -> int:
        ...


    def readBoolean(self) -> bool:
        ...
