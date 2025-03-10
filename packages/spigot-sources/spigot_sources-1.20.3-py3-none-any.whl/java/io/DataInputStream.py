"""
Python module generated from Java source file java.io.DataInputStream

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.io import *
from java.util import Objects
from typing import Any, Callable, Iterable, Tuple


class DataInputStream(FilterInputStream, DataInput):
    """
    A data input stream lets an application read primitive Java data
    types from an underlying input stream in a machine-independent
    way. An application uses a data output stream to write data that
    can later be read by a data input stream.
    
    A DataInputStream is not safe for use by multiple concurrent
    threads. If a DataInputStream is to be used by more than one
    thread then access to the data input stream should be controlled
    by appropriate synchronization.

    Author(s)
    - Arthur van Hoff

    See
    - java.io.DataOutputStream

    Since
    - 1.0
    """

    def __init__(self, in: "InputStream"):
        """
        Creates a DataInputStream that uses the specified
        underlying InputStream.

        Arguments
        - in: the specified input stream
        """
        ...


    def read(self, b: list[int]) -> int:
        """
        Reads some number of bytes from the contained input stream and
        stores them into the buffer array `b`. The number of
        bytes actually read is returned as an integer. This method blocks
        until input data is available, end of file is detected, or an
        exception is thrown.
        
        If `b` is null, a `NullPointerException` is
        thrown. If the length of `b` is zero, then no bytes are
        read and `0` is returned; otherwise, there is an attempt
        to read at least one byte. If no byte is available because the
        stream is at end of file, the value `-1` is returned;
        otherwise, at least one byte is read and stored into `b`.
        
        The first byte read is stored into element `b[0]`, the
        next one into `b[1]`, and so on. The number of bytes read
        is, at most, equal to the length of `b`. Let `k`
        be the number of bytes actually read; these bytes will be stored in
        elements `b[0]` through `b[k-1]`, leaving
        elements `b[k]` through `b[b.length-1]`
        unaffected.
        
        The `read(b)` method has the same effect as:
        <blockquote>```
        read(b, 0, b.length)
        ```</blockquote>

        Arguments
        - b: the buffer into which the data is read.

        Returns
        - the total number of bytes read into the buffer, or
                    `-1` if there is no more data because the end
                    of the stream has been reached.

        Raises
        - IOException: if the first byte cannot be read for any reason
                    other than end of file, the stream has been closed and the underlying
                    input stream does not support reading after close, or another I/O
                    error occurs.

        See
        - java.io.InputStream.read(byte[], int, int)
        """
        ...


    def read(self, b: list[int], off: int, len: int) -> int:
        """
        Reads up to `len` bytes of data from the contained
        input stream into an array of bytes.  An attempt is made to read
        as many as `len` bytes, but a smaller number may be read,
        possibly zero. The number of bytes actually read is returned as an
        integer.
        
         This method blocks until input data is available, end of file is
        detected, or an exception is thrown.
        
         If `len` is zero, then no bytes are read and
        `0` is returned; otherwise, there is an attempt to read at
        least one byte. If no byte is available because the stream is at end of
        file, the value `-1` is returned; otherwise, at least one
        byte is read and stored into `b`.
        
         The first byte read is stored into element `b[off]`, the
        next one into `b[off+1]`, and so on. The number of bytes read
        is, at most, equal to `len`. Let *k* be the number of
        bytes actually read; these bytes will be stored in elements
        `b[off]` through `b[off+`*k*`-1]`,
        leaving elements `b[off+`*k*`]` through
        `b[off+len-1]` unaffected.
        
         In every case, elements `b[0]` through
        `b[off]` and elements `b[off+len]` through
        `b[b.length-1]` are unaffected.

        Arguments
        - b: the buffer into which the data is read.
        - off: the start offset in the destination array `b`
        - len: the maximum number of bytes read.

        Returns
        - the total number of bytes read into the buffer, or
                    `-1` if there is no more data because the end
                    of the stream has been reached.

        Raises
        - NullPointerException: If `b` is `null`.
        - IndexOutOfBoundsException: If `off` is negative,
                    `len` is negative, or `len` is greater than
                    `b.length - off`
        - IOException: if the first byte cannot be read for any reason
                    other than end of file, the stream has been closed and the underlying
                    input stream does not support reading after close, or another I/O
                    error occurs.

        See
        - java.io.InputStream.read(byte[], int, int)
        """
        ...


    def readFully(self, b: list[int]) -> None:
        """
        See the general contract of the `readFully`
        method of `DataInput`.
        
        Bytes
        for this operation are read from the contained
        input stream.

        Arguments
        - b: the buffer into which the data is read.

        Raises
        - NullPointerException: if `b` is `null`.
        - EOFException: if this input stream reaches the end before
                 reading all the bytes.
        - IOException: the stream has been closed and the contained
                 input stream does not support reading after close, or
                 another I/O error occurs.

        See
        - java.io.FilterInputStream.in
        """
        ...


    def readFully(self, b: list[int], off: int, len: int) -> None:
        """
        See the general contract of the `readFully`
        method of `DataInput`.
        
        Bytes
        for this operation are read from the contained
        input stream.

        Arguments
        - b: the buffer into which the data is read.
        - off: the start offset in the data array `b`.
        - len: the number of bytes to read.

        Raises
        - NullPointerException: if `b` is `null`.
        - IndexOutOfBoundsException: if `off` is negative,
                    `len` is negative, or `len` is greater than
                    `b.length - off`.
        - EOFException: if this input stream reaches the end before
                    reading all the bytes.
        - IOException: the stream has been closed and the contained
                    input stream does not support reading after close, or
                    another I/O error occurs.

        See
        - java.io.FilterInputStream.in
        """
        ...


    def skipBytes(self, n: int) -> int:
        """
        See the general contract of the `skipBytes`
        method of `DataInput`.
        
        Bytes for this operation are read from the contained
        input stream.

        Arguments
        - n: the number of bytes to be skipped.

        Returns
        - the actual number of bytes skipped.

        Raises
        - IOException: if the contained input stream does not support
                    seek, or the stream has been closed and
                    the contained input stream does not support
                    reading after close, or another I/O error occurs.
        """
        ...


    def readBoolean(self) -> bool:
        """
        See the general contract of the `readBoolean`
        method of `DataInput`.
        
        Bytes for this operation are read from the contained
        input stream.

        Returns
        - the `boolean` value read.

        Raises
        - EOFException: if this input stream has reached the end.
        - IOException: the stream has been closed and the contained
                    input stream does not support reading after close, or
                    another I/O error occurs.

        See
        - java.io.FilterInputStream.in
        """
        ...


    def readByte(self) -> int:
        """
        See the general contract of the `readByte`
        method of `DataInput`.
        
        Bytes
        for this operation are read from the contained
        input stream.

        Returns
        - the next byte of this input stream as a signed 8-bit
                    `byte`.

        Raises
        - EOFException: if this input stream has reached the end.
        - IOException: the stream has been closed and the contained
                    input stream does not support reading after close, or
                    another I/O error occurs.

        See
        - java.io.FilterInputStream.in
        """
        ...


    def readUnsignedByte(self) -> int:
        """
        See the general contract of the `readUnsignedByte`
        method of `DataInput`.
        
        Bytes
        for this operation are read from the contained
        input stream.

        Returns
        - the next byte of this input stream, interpreted as an
                    unsigned 8-bit number.

        Raises
        - EOFException: if this input stream has reached the end.
        - IOException: the stream has been closed and the contained
                    input stream does not support reading after close, or
                    another I/O error occurs.

        See
        - java.io.FilterInputStream.in
        """
        ...


    def readShort(self) -> int:
        """
        See the general contract of the `readShort`
        method of `DataInput`.
        
        Bytes
        for this operation are read from the contained
        input stream.

        Returns
        - the next two bytes of this input stream, interpreted as a
                    signed 16-bit number.

        Raises
        - EOFException: if this input stream reaches the end before
                      reading two bytes.
        - IOException: the stream has been closed and the contained
                    input stream does not support reading after close, or
                    another I/O error occurs.

        See
        - java.io.FilterInputStream.in
        """
        ...


    def readUnsignedShort(self) -> int:
        """
        See the general contract of the `readUnsignedShort`
        method of `DataInput`.
        
        Bytes
        for this operation are read from the contained
        input stream.

        Returns
        - the next two bytes of this input stream, interpreted as an
                    unsigned 16-bit integer.

        Raises
        - EOFException: if this input stream reaches the end before
                    reading two bytes.
        - IOException: the stream has been closed and the contained
                    input stream does not support reading after close, or
                    another I/O error occurs.

        See
        - java.io.FilterInputStream.in
        """
        ...


    def readChar(self) -> str:
        """
        See the general contract of the `readChar`
        method of `DataInput`.
        
        Bytes
        for this operation are read from the contained
        input stream.

        Returns
        - the next two bytes of this input stream, interpreted as a
                    `char`.

        Raises
        - EOFException: if this input stream reaches the end before
                      reading two bytes.
        - IOException: the stream has been closed and the contained
                    input stream does not support reading after close, or
                    another I/O error occurs.

        See
        - java.io.FilterInputStream.in
        """
        ...


    def readInt(self) -> int:
        """
        See the general contract of the `readInt`
        method of `DataInput`.
        
        Bytes
        for this operation are read from the contained
        input stream.

        Returns
        - the next four bytes of this input stream, interpreted as an
                    `int`.

        Raises
        - EOFException: if this input stream reaches the end before
                      reading four bytes.
        - IOException: the stream has been closed and the contained
                    input stream does not support reading after close, or
                    another I/O error occurs.

        See
        - java.io.FilterInputStream.in
        """
        ...


    def readLong(self) -> int:
        """
        See the general contract of the `readLong`
        method of `DataInput`.
        
        Bytes
        for this operation are read from the contained
        input stream.

        Returns
        - the next eight bytes of this input stream, interpreted as a
                    `long`.

        Raises
        - EOFException: if this input stream reaches the end before
                      reading eight bytes.
        - IOException: the stream has been closed and the contained
                    input stream does not support reading after close, or
                    another I/O error occurs.

        See
        - java.io.FilterInputStream.in
        """
        ...


    def readFloat(self) -> float:
        """
        See the general contract of the `readFloat`
        method of `DataInput`.
        
        Bytes
        for this operation are read from the contained
        input stream.

        Returns
        - the next four bytes of this input stream, interpreted as a
                    `float`.

        Raises
        - EOFException: if this input stream reaches the end before
                      reading four bytes.
        - IOException: the stream has been closed and the contained
                    input stream does not support reading after close, or
                    another I/O error occurs.

        See
        - java.lang.Float.intBitsToFloat(int)
        """
        ...


    def readDouble(self) -> float:
        """
        See the general contract of the `readDouble`
        method of `DataInput`.
        
        Bytes
        for this operation are read from the contained
        input stream.

        Returns
        - the next eight bytes of this input stream, interpreted as a
                    `double`.

        Raises
        - EOFException: if this input stream reaches the end before
                      reading eight bytes.
        - IOException: the stream has been closed and the contained
                    input stream does not support reading after close, or
                    another I/O error occurs.

        See
        - java.lang.Double.longBitsToDouble(long)
        """
        ...


    def readLine(self) -> str:
        """
        See the general contract of the `readLine`
        method of `DataInput`.
        
        Bytes
        for this operation are read from the contained
        input stream.

        Returns
        - the next line of text from this input stream.

        Raises
        - IOException: if an I/O error occurs.

        See
        - java.io.FilterInputStream.in

        Deprecated
        - This method does not properly convert bytes to characters.
        As of JDK&nbsp;1.1, the preferred way to read lines of text is via the
        `BufferedReader.readLine()` method.  Programs that use the
        `DataInputStream` class to read lines can be converted to use
        the `BufferedReader` class by replacing code of the form:
        <blockquote>```
            DataInputStream d =&nbsp;new&nbsp;DataInputStream(in);
        ```</blockquote>
        with:
        <blockquote>```
            BufferedReader d
                 =&nbsp;new&nbsp;BufferedReader(new&nbsp;InputStreamReader(in));
        ```</blockquote>
        """
        ...


    def readUTF(self) -> str:
        """
        See the general contract of the `readUTF`
        method of `DataInput`.
        
        Bytes
        for this operation are read from the contained
        input stream.

        Returns
        - a Unicode string.

        Raises
        - EOFException: if this input stream reaches the end before
                      reading all the bytes.
        - IOException: the stream has been closed and the contained
                    input stream does not support reading after close, or
                    another I/O error occurs.
        - UTFDataFormatException: if the bytes do not represent a valid
                    modified UTF-8 encoding of a string.

        See
        - java.io.DataInputStream.readUTF(java.io.DataInput)
        """
        ...


    @staticmethod
    def readUTF(in: "DataInput") -> str:
        """
        Reads from the
        stream `in` a representation
        of a Unicode  character string encoded in
        <a href="DataInput.html#modified-utf-8">modified UTF-8</a> format;
        this string of characters is then returned as a `String`.
        The details of the modified UTF-8 representation
        are  exactly the same as for the `readUTF`
        method of `DataInput`.

        Arguments
        - in: a data input stream.

        Returns
        - a Unicode string.

        Raises
        - EOFException: if the input stream reaches the end
                      before all the bytes.
        - IOException: the stream has been closed and the contained
                    input stream does not support reading after close, or
                    another I/O error occurs.
        - UTFDataFormatException: if the bytes do not represent a
                      valid modified UTF-8 encoding of a Unicode string.

        See
        - java.io.DataInputStream.readUnsignedShort()
        """
        ...
