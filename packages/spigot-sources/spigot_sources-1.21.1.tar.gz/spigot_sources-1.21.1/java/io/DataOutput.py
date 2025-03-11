"""
Python module generated from Java source file java.io.DataOutput

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.io import *
from typing import Any, Callable, Iterable, Tuple


class DataOutput:
    """
    The `DataOutput` interface provides
    for converting data from any of the Java
    primitive types to a series of bytes and
    writing these bytes to a binary stream.
    There is  also a facility for converting
    a `String` into
    <a href="DataInput.html#modified-utf-8">modified UTF-8</a>
    format and writing the resulting series
    of bytes.
    
    For all the methods in this interface that
    write bytes, it is generally True that if
    a byte cannot be written for any reason,
    an `IOException` is thrown.

    Author(s)
    - Frank Yellin

    See
    - java.io.DataOutputStream

    Since
    - 1.0
    """

    def write(self, b: int) -> None:
        """
        Writes to the output stream the eight
        low-order bits of the argument `b`.
        The 24 high-order  bits of `b`
        are ignored.

        Arguments
        - b: the byte to be written.

        Raises
        - IOException: if an I/O error occurs.
        """
        ...


    def write(self, b: list[int]) -> None:
        """
        Writes to the output stream all the bytes in array `b`.
        If `b` is `null`,
        a `NullPointerException` is thrown.
        If `b.length` is zero, then
        no bytes are written. Otherwise, the byte
        `b[0]` is written first, then
        `b[1]`, and so on; the last byte
        written is `b[b.length-1]`.

        Arguments
        - b: the data.

        Raises
        - IOException: if an I/O error occurs.
        """
        ...


    def write(self, b: list[int], off: int, len: int) -> None:
        """
        Writes `len` bytes from array
        `b`, in order,  to
        the output stream.  If `b`
        is `null`, a `NullPointerException`
        is thrown.  If `off` is negative,
        or `len` is negative, or `off+len`
        is greater than the length of the array
        `b`, then an `IndexOutOfBoundsException`
        is thrown.  If `len` is zero,
        then no bytes are written. Otherwise, the
        byte `b[off]` is written first,
        then `b[off+1]`, and so on; the
        last byte written is `b[off+len-1]`.

        Arguments
        - b: the data.
        - off: the start offset in the data.
        - len: the number of bytes to write.

        Raises
        - IOException: if an I/O error occurs.
        """
        ...


    def writeBoolean(self, v: bool) -> None:
        """
        Writes a `boolean` value to this output stream.
        If the argument `v`
        is `True`, the value `(byte)1`
        is written; if `v` is `False`,
        the  value `(byte)0` is written.
        The byte written by this method may
        be read by the `readBoolean`
        method of interface `DataInput`,
        which will then return a `boolean`
        equal to `v`.

        Arguments
        - v: the boolean to be written.

        Raises
        - IOException: if an I/O error occurs.
        """
        ...


    def writeByte(self, v: int) -> None:
        """
        Writes to the output stream the eight low-order
        bits of the argument `v`.
        The 24 high-order bits of `v`
        are ignored. (This means  that `writeByte`
        does exactly the same thing as `write`
        for an integer argument.) The byte written
        by this method may be read by the `readByte`
        method of interface `DataInput`,
        which will then return a `byte`
        equal to `(byte)v`.

        Arguments
        - v: the byte value to be written.

        Raises
        - IOException: if an I/O error occurs.
        """
        ...


    def writeShort(self, v: int) -> None:
        """
        Writes two bytes to the output
        stream to represent the value of the argument.
        The byte values to be written, in the  order
        shown, are:
        ````(byte)(0xff & (v >> 8))
        (byte)(0xff & v)```` 
        The bytes written by this method may be
        read by the `readShort` method
        of interface `DataInput`, which
        will then return a `short` equal
        to `(short)v`.

        Arguments
        - v: the `short` value to be written.

        Raises
        - IOException: if an I/O error occurs.
        """
        ...


    def writeChar(self, v: int) -> None:
        """
        Writes a `char` value, which
        is comprised of two bytes, to the
        output stream.
        The byte values to be written, in the  order
        shown, are:
        ````(byte)(0xff & (v >> 8))
        (byte)(0xff & v)````
        The bytes written by this method may be
        read by the `readChar` method
        of interface `DataInput`, which
        will then return a `char` equal
        to `(char)v`.

        Arguments
        - v: the `char` value to be written.

        Raises
        - IOException: if an I/O error occurs.
        """
        ...


    def writeInt(self, v: int) -> None:
        """
        Writes an `int` value, which is
        comprised of four bytes, to the output stream.
        The byte values to be written, in the  order
        shown, are:
        ````(byte)(0xff & (v >> 24))
        (byte)(0xff & (v >> 16))
        (byte)(0xff & (v >>  8))
        (byte)(0xff & v)````
        The bytes written by this method may be read
        by the `readInt` method of interface
        `DataInput`, which will then
        return an `int` equal to `v`.

        Arguments
        - v: the `int` value to be written.

        Raises
        - IOException: if an I/O error occurs.
        """
        ...


    def writeLong(self, v: int) -> None:
        """
        Writes a `long` value, which is
        comprised of eight bytes, to the output stream.
        The byte values to be written, in the  order
        shown, are:
        ````(byte)(0xff & (v >> 56))
        (byte)(0xff & (v >> 48))
        (byte)(0xff & (v >> 40))
        (byte)(0xff & (v >> 32))
        (byte)(0xff & (v >> 24))
        (byte)(0xff & (v >> 16))
        (byte)(0xff & (v >>  8))
        (byte)(0xff & v)````
        The bytes written by this method may be
        read by the `readLong` method
        of interface `DataInput`, which
        will then return a `long` equal
        to `v`.

        Arguments
        - v: the `long` value to be written.

        Raises
        - IOException: if an I/O error occurs.
        """
        ...


    def writeFloat(self, v: float) -> None:
        """
        Writes a `float` value,
        which is comprised of four bytes, to the output stream.
        It does this as if it first converts this
        `float` value to an `int`
        in exactly the manner of the `Float.floatToIntBits`
        method  and then writes the `int`
        value in exactly the manner of the  `writeInt`
        method.  The bytes written by this method
        may be read by the `readFloat`
        method of interface `DataInput`,
        which will then return a `float`
        equal to `v`.

        Arguments
        - v: the `float` value to be written.

        Raises
        - IOException: if an I/O error occurs.
        """
        ...


    def writeDouble(self, v: float) -> None:
        """
        Writes a `double` value,
        which is comprised of eight bytes, to the output stream.
        It does this as if it first converts this
        `double` value to a `long`
        in exactly the manner of the `Double.doubleToLongBits`
        method  and then writes the `long`
        value in exactly the manner of the  `writeLong`
        method. The bytes written by this method
        may be read by the `readDouble`
        method of interface `DataInput`,
        which will then return a `double`
        equal to `v`.

        Arguments
        - v: the `double` value to be written.

        Raises
        - IOException: if an I/O error occurs.
        """
        ...


    def writeBytes(self, s: str) -> None:
        """
        Writes a string to the output stream.
        For every character in the string
        `s`,  taken in order, one byte
        is written to the output stream.  If
        `s` is `null`, a `NullPointerException`
        is thrown.  If `s.length`
        is zero, then no bytes are written. Otherwise,
        the character `s[0]` is written
        first, then `s[1]`, and so on;
        the last character written is `s[s.length-1]`.
        For each character, one byte is written,
        the low-order byte, in exactly the manner
        of the `writeByte` method . The
        high-order eight bits of each character
        in the string are ignored.

        Arguments
        - s: the string of bytes to be written.

        Raises
        - IOException: if an I/O error occurs.
        """
        ...


    def writeChars(self, s: str) -> None:
        """
        Writes every character in the string `s`,
        to the output stream, in order,
        two bytes per character. If `s`
        is `null`, a `NullPointerException`
        is thrown.  If `s.length`
        is zero, then no characters are written.
        Otherwise, the character `s[0]`
        is written first, then `s[1]`,
        and so on; the last character written is
        `s[s.length-1]`. For each character,
        two bytes are actually written, high-order
        byte first, in exactly the manner of the
        `writeChar` method.

        Arguments
        - s: the string value to be written.

        Raises
        - IOException: if an I/O error occurs.
        """
        ...


    def writeUTF(self, s: str) -> None:
        """
        Writes two bytes of length information
        to the output stream, followed
        by the
        <a href="DataInput.html#modified-utf-8">modified UTF-8</a>
        representation
        of  every character in the string `s`.
        If `s` is `null`,
        a `NullPointerException` is thrown.
        Each character in the string `s`
        is converted to a group of one, two, or
        three bytes, depending on the value of the
        character.
        If a character `c`
        is in the range `&#92;u0001` through
        `&#92;u007f`, it is represented
        by one byte:
        ```(byte)c ```  
        If a character `c` is `&#92;u0000`
        or is in the range `&#92;u0080`
        through `&#92;u07ff`, then it is
        represented by two bytes, to be written
        in the order shown: ````(byte)(0xc0 | (0x1f & (c >> 6)))
        (byte)(0x80 | (0x3f & c))````  If a character
        `c` is in the range `&#92;u0800`
        through `uffff`, then it is
        represented by three bytes, to be written
        in the order shown: ````(byte)(0xe0 | (0x0f & (c >> 12)))
        (byte)(0x80 | (0x3f & (c >>  6)))
        (byte)(0x80 | (0x3f & c))````   First,
        the total number of bytes needed to represent
        all the characters of `s` is
        calculated. If this number is larger than
        `65535`, then a `UTFDataFormatException`
        is thrown. Otherwise, this length is written
        to the output stream in exactly the manner
        of the `writeShort` method;
        after this, the one-, two-, or three-byte
        representation of each character in the
        string `s` is written.  The
        bytes written by this method may be read
        by the `readUTF` method of interface
        `DataInput`, which will then
        return a `String` equal to `s`.

        Arguments
        - s: the string value to be written.

        Raises
        - IOException: if an I/O error occurs.
        """
        ...
