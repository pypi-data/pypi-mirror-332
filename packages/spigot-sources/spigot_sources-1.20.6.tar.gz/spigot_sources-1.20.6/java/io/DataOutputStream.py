"""
Python module generated from Java source file java.io.DataOutputStream

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.io import *
from typing import Any, Callable, Iterable, Tuple


class DataOutputStream(FilterOutputStream, DataOutput):
    """
    A data output stream lets an application write primitive Java data
    types to an output stream in a portable way. An application can
    then use a data input stream to read the data back in.
    
    A DataOutputStream is not safe for use by multiple concurrent
    threads. If a DataOutputStream is to be used by more than one
    thread then access to the data output stream should be controlled
    by appropriate synchronization.

    See
    - java.io.DataInputStream

    Since
    - 1.0
    """

    def __init__(self, out: "OutputStream"):
        """
        Creates a new data output stream to write data to the specified
        underlying output stream. The counter `written` is
        set to zero.

        Arguments
        - out: the underlying output stream, to be saved for later
                       use.

        See
        - java.io.FilterOutputStream.out
        """
        ...


    def write(self, b: int) -> None:
        """
        Writes the specified byte (the low eight bits of the argument
        `b`) to the underlying output stream. If no exception
        is thrown, the counter `written` is incremented by
        `1`.
        
        Implements the `write` method of `OutputStream`.

        Arguments
        - b: the `byte` to be written.

        Raises
        - IOException: if an I/O error occurs.

        See
        - java.io.FilterOutputStream.out
        """
        ...


    def write(self, b: list[int], off: int, len: int) -> None:
        """
        Writes `len` bytes from the specified byte array
        starting at offset `off` to the underlying output stream.
        If no exception is thrown, the counter `written` is
        incremented by `len`.

        Arguments
        - b: the data.
        - off: the start offset in the data.
        - len: the number of bytes to write.

        Raises
        - IOException: if an I/O error occurs.

        See
        - java.io.FilterOutputStream.out
        """
        ...


    def flush(self) -> None:
        """
        Flushes this data output stream. This forces any buffered output
        bytes to be written out to the stream.
        
        The `flush` method of `DataOutputStream`
        calls the `flush` method of its underlying output stream.

        Raises
        - IOException: if an I/O error occurs.

        See
        - java.io.OutputStream.flush()
        """
        ...


    def writeBoolean(self, v: bool) -> None:
        """
        Writes a `boolean` to the underlying output stream as
        a 1-byte value. The value `True` is written out as the
        value `(byte)1`; the value `False` is
        written out as the value `(byte)0`. If no exception is
        thrown, the counter `written` is incremented by
        `1`.

        Arguments
        - v: a `boolean` value to be written.

        Raises
        - IOException: if an I/O error occurs.

        See
        - java.io.FilterOutputStream.out
        """
        ...


    def writeByte(self, v: int) -> None:
        """
        Writes out a `byte` to the underlying output stream as
        a 1-byte value. If no exception is thrown, the counter
        `written` is incremented by `1`.

        Arguments
        - v: a `byte` value to be written.

        Raises
        - IOException: if an I/O error occurs.

        See
        - java.io.FilterOutputStream.out
        """
        ...


    def writeShort(self, v: int) -> None:
        """
        Writes a `short` to the underlying output stream as two
        bytes, high byte first. If no exception is thrown, the counter
        `written` is incremented by `2`.

        Arguments
        - v: a `short` to be written.

        Raises
        - IOException: if an I/O error occurs.

        See
        - java.io.FilterOutputStream.out
        """
        ...


    def writeChar(self, v: int) -> None:
        """
        Writes a `char` to the underlying output stream as a
        2-byte value, high byte first. If no exception is thrown, the
        counter `written` is incremented by `2`.

        Arguments
        - v: a `char` value to be written.

        Raises
        - IOException: if an I/O error occurs.

        See
        - java.io.FilterOutputStream.out
        """
        ...


    def writeInt(self, v: int) -> None:
        """
        Writes an `int` to the underlying output stream as four
        bytes, high byte first. If no exception is thrown, the counter
        `written` is incremented by `4`.

        Arguments
        - v: an `int` to be written.

        Raises
        - IOException: if an I/O error occurs.

        See
        - java.io.FilterOutputStream.out
        """
        ...


    def writeLong(self, v: int) -> None:
        """
        Writes a `long` to the underlying output stream as eight
        bytes, high byte first. In no exception is thrown, the counter
        `written` is incremented by `8`.

        Arguments
        - v: a `long` to be written.

        Raises
        - IOException: if an I/O error occurs.

        See
        - java.io.FilterOutputStream.out
        """
        ...


    def writeFloat(self, v: float) -> None:
        """
        Converts the float argument to an `int` using the
        `floatToIntBits` method in class `Float`,
        and then writes that `int` value to the underlying
        output stream as a 4-byte quantity, high byte first. If no
        exception is thrown, the counter `written` is
        incremented by `4`.

        Arguments
        - v: a `float` value to be written.

        Raises
        - IOException: if an I/O error occurs.

        See
        - java.lang.Float.floatToIntBits(float)
        """
        ...


    def writeDouble(self, v: float) -> None:
        """
        Converts the double argument to a `long` using the
        `doubleToLongBits` method in class `Double`,
        and then writes that `long` value to the underlying
        output stream as an 8-byte quantity, high byte first. If no
        exception is thrown, the counter `written` is
        incremented by `8`.

        Arguments
        - v: a `double` value to be written.

        Raises
        - IOException: if an I/O error occurs.

        See
        - java.lang.Double.doubleToLongBits(double)
        """
        ...


    def writeBytes(self, s: str) -> None:
        """
        Writes out the string to the underlying output stream as a
        sequence of bytes. Each character in the string is written out, in
        sequence, by discarding its high eight bits. If no exception is
        thrown, the counter `written` is incremented by the
        length of `s`.

        Arguments
        - s: a string of bytes to be written.

        Raises
        - IOException: if an I/O error occurs.

        See
        - java.io.FilterOutputStream.out
        """
        ...


    def writeChars(self, s: str) -> None:
        """
        Writes a string to the underlying output stream as a sequence of
        characters. Each character is written to the data output stream as
        if by the `writeChar` method. If no exception is
        thrown, the counter `written` is incremented by twice
        the length of `s`.

        Arguments
        - s: a `String` value to be written.

        Raises
        - IOException: if an I/O error occurs.

        See
        - java.io.FilterOutputStream.out
        """
        ...


    def writeUTF(self, str: str) -> None:
        """
        Writes a string to the underlying output stream using
        <a href="DataInput.html#modified-utf-8">modified UTF-8</a>
        encoding in a machine-independent manner.
        
        First, two bytes are written to the output stream as if by the
        `writeShort` method giving the number of bytes to
        follow. This value is the number of bytes actually written out,
        not the length of the string. Following the length, each character
        of the string is output, in sequence, using the modified UTF-8 encoding
        for the character. If no exception is thrown, the counter
        `written` is incremented by the total number of
        bytes written to the output stream. This will be at least two
        plus the length of `str`, and at most two plus
        thrice the length of `str`.

        Arguments
        - str: a string to be written.

        Raises
        - UTFDataFormatException: if the modified UTF-8 encoding of
                    `str` would exceed 65535 bytes in length
        - IOException: if some other I/O error occurs.

        See
        - .writeChars(String)
        """
        ...


    def size(self) -> int:
        """
        Returns the current value of the counter `written`,
        the number of bytes written to this data output stream so far.
        If the counter overflows, it will be wrapped to Integer.MAX_VALUE.

        Returns
        - the value of the `written` field.

        See
        - java.io.DataOutputStream.written
        """
        ...
