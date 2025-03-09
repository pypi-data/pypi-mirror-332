"""
Python module generated from Java source file java.io.RandomAccessFile

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.io import *
from jdk.internal.access import JavaIORandomAccessFileAccess
from jdk.internal.access import SharedSecrets
from sun.nio.ch import FileChannelImpl
from typing import Any, Callable, Iterable, Tuple


class RandomAccessFile(DataOutput, DataInput, Closeable):

    def __init__(self, name: str, mode: str):
        """
        Creates a random access file stream to read from, and optionally
        to write to, a file with the specified name. A new
        FileDescriptor object is created to represent the
        connection to the file.
        
         The `mode` argument specifies the access mode with which the
        file is to be opened.  The permitted values and their meanings are as
        specified for the <a
        href="#mode">`RandomAccessFile(File,String)`</a> constructor.
        
        
        If there is a security manager, its `checkRead` method
        is called with the `name` argument
        as its argument to see if read access to the file is allowed.
        If the mode allows writing, the security manager's
        `checkWrite` method
        is also called with the `name` argument
        as its argument to see if write access to the file is allowed.

        Arguments
        - name: the system-dependent filename
        - mode: the access <a href="#mode">mode</a>

        Raises
        - IllegalArgumentException: if the mode argument is not equal
                    to one of `"r"`, `"rw"`, `"rws"`, or
                    `"rwd"`
        - FileNotFoundException: if the mode is `"r"` but the given string does not
                    denote an existing regular file, or if the mode begins with
                    `"rw"` but the given string does not denote an
                    existing, writable regular file and a new regular file of
                    that name cannot be created, or if some other error occurs
                    while opening or creating the file
        - SecurityException: if a security manager exists and its
                    `checkRead` method denies read access to the file
                    or the mode is `"rw"` and the security manager's
                    `checkWrite` method denies write access to the file

        See
        - java.lang.SecurityManager.checkWrite(java.lang.String)

        Unknown Tags
        - 1.4
        """
        ...


    def __init__(self, file: "File", mode: str):
        """
        Creates a random access file stream to read from, and optionally to
        write to, the file specified by the File argument.  A new FileDescriptor object is created to represent this file connection.
        
        The <a id="mode">`mode`</a> argument specifies the access mode
        in which the file is to be opened.  The permitted values and their
        meanings are:
        
        <table class="striped">
        <caption style="display:none">Access mode permitted values and meanings</caption>
        <thead>
        <tr><th scope="col" style="text-align:left">Value</th><th scope="col" style="text-align:left">Meaning</th></tr>
        </thead>
        <tbody>
        <tr><th scope="row" style="vertical-align:top">`"r"`</th>
            <td> Open for reading only. Invoking any of the `write`
            methods of the resulting object will cause an
            java.io.IOException to be thrown.</td></tr>
        <tr><th scope="row" style="vertical-align:top">`"rw"`</th>
            <td> Open for reading and writing.  If the file does not already
            exist then an attempt will be made to create it.</td></tr>
        <tr><th scope="row" style="vertical-align:top">`"rws"`</th>
            <td> Open for reading and writing, as with `"rw"`, and also
            require that every update to the file's content or metadata be
            written synchronously to the underlying storage device.</td></tr>
        <tr><th scope="row" style="vertical-align:top">`"rwd"`</th>
            <td> Open for reading and writing, as with `"rw"`, and also
            require that every update to the file's content be written
            synchronously to the underlying storage device.</td></tr>
        </tbody>
        </table>
        
        The `"rws"` and `"rwd"` modes work much like the java.nio.channels.FileChannel.force(boolean) force(boolean) method of
        the java.nio.channels.FileChannel class, passing arguments of
        `True` and `False`, respectively, except that they always
        apply to every I/O operation and are therefore often more efficient.  If
        the file resides on a local storage device then when an invocation of a
        method of this class returns it is guaranteed that all changes made to
        the file by that invocation will have been written to that device.  This
        is useful for ensuring that critical information is not lost in the
        event of a system crash.  If the file does not reside on a local device
        then no such guarantee is made.
        
        The `"rwd"` mode can be used to reduce the number of I/O
        operations performed.  Using `"rwd"` only requires updates to the
        file's content to be written to storage; using `"rws"` requires
        updates to both the file's content and its metadata to be written, which
        generally requires at least one more low-level I/O operation.
        
        If there is a security manager, its `checkRead` method is
        called with the pathname of the `file` argument as its
        argument to see if read access to the file is allowed.  If the mode
        allows writing, the security manager's `checkWrite` method is
        also called with the path argument to see if write access to the file is
        allowed.

        Arguments
        - file: the file object
        - mode: the access mode, as described
                           <a href="#mode">above</a>

        Raises
        - IllegalArgumentException: if the mode argument is not equal
                    to one of `"r"`, `"rw"`, `"rws"`, or
                    `"rwd"`
        - FileNotFoundException: if the mode is `"r"` but the given file object does
                    not denote an existing regular file, or if the mode begins
                    with `"rw"` but the given file object does not denote
                    an existing, writable regular file and a new regular file of
                    that name cannot be created, or if some other error occurs
                    while opening or creating the file
        - SecurityException: if a security manager exists and its
                    `checkRead` method denies read access to the file
                    or the mode is `"rw"` and the security manager's
                    `checkWrite` method denies write access to the file

        See
        - java.nio.channels.FileChannel.force(boolean)

        Unknown Tags
        - 1.4
        """
        ...


    def getFD(self) -> "FileDescriptor":
        """
        Returns the opaque file descriptor object associated with this
        stream.

        Returns
        - the file descriptor object associated with this stream.

        Raises
        - IOException: if an I/O error occurs.

        See
        - java.io.FileDescriptor
        """
        ...


    def getChannel(self) -> "FileChannel":
        """
        Returns the unique java.nio.channels.FileChannel FileChannel
        object associated with this file.
        
         The java.nio.channels.FileChannel.position()
        position of the returned channel will always be equal to
        this object's file-pointer offset as returned by the .getFilePointer getFilePointer method.  Changing this object's
        file-pointer offset, whether explicitly or by reading or writing bytes,
        will change the position of the channel, and vice versa.  Changing the
        file's length via this object will change the length seen via the file
        channel, and vice versa.

        Returns
        - the file channel associated with this file

        Since
        - 1.4
        """
        ...


    def read(self) -> int:
        """
        Reads a byte of data from this file. The byte is returned as an
        integer in the range 0 to 255 (`0x00-0x0ff`). This
        method blocks if no input is yet available.
        
        Although `RandomAccessFile` is not a subclass of
        `InputStream`, this method behaves in exactly the same
        way as the InputStream.read() method of
        `InputStream`.

        Returns
        - the next byte of data, or `-1` if the end of the
                    file has been reached.

        Raises
        - IOException: if an I/O error occurs. Not thrown if
                                 end-of-file has been reached.
        """
        ...


    def read(self, b: list[int], off: int, len: int) -> int:
        """
        Reads up to `len` bytes of data from this file into an
        array of bytes. This method blocks until at least one byte of input
        is available.
        
        Although `RandomAccessFile` is not a subclass of
        `InputStream`, this method behaves in exactly the
        same way as the InputStream.read(byte[], int, int) method of
        `InputStream`.

        Arguments
        - b: the buffer into which the data is read.
        - off: the start offset in array `b`
                          at which the data is written.
        - len: the maximum number of bytes read.

        Returns
        - the total number of bytes read into the buffer, or
                    `-1` if there is no more data because the end of
                    the file has been reached.

        Raises
        - IOException: If the first byte cannot be read for any reason
                    other than end of file, or if the random access file has been closed,
                    or if some other I/O error occurs.
        - NullPointerException: If `b` is `null`.
        - IndexOutOfBoundsException: If `off` is negative,
                    `len` is negative, or `len` is greater than
                    `b.length - off`
        """
        ...


    def read(self, b: list[int]) -> int:
        """
        Reads up to `b.length` bytes of data from this file
        into an array of bytes. This method blocks until at least one byte
        of input is available.
        
        Although `RandomAccessFile` is not a subclass of
        `InputStream`, this method behaves in exactly the
        same way as the InputStream.read(byte[]) method of
        `InputStream`.

        Arguments
        - b: the buffer into which the data is read.

        Returns
        - the total number of bytes read into the buffer, or
                    `-1` if there is no more data because the end of
                    this file has been reached.

        Raises
        - IOException: If the first byte cannot be read for any reason
                    other than end of file, or if the random access file has been closed,
                    or if some other I/O error occurs.
        - NullPointerException: If `b` is `null`.
        """
        ...


    def readFully(self, b: list[int]) -> None:
        """
        Reads `b.length` bytes from this file into the byte
        array, starting at the current file pointer. This method reads
        repeatedly from the file until the requested number of bytes are
        read. This method blocks until the requested number of bytes are
        read, the end of the stream is detected, or an exception is thrown.

        Arguments
        - b: the buffer into which the data is read.

        Raises
        - NullPointerException: if `b` is `null`.
        - EOFException: if this file reaches the end before reading
                     all the bytes.
        - IOException: if an I/O error occurs.
        """
        ...


    def readFully(self, b: list[int], off: int, len: int) -> None:
        """
        Reads exactly `len` bytes from this file into the byte
        array, starting at the current file pointer. This method reads
        repeatedly from the file until the requested number of bytes are
        read. This method blocks until the requested number of bytes are
        read, the end of the stream is detected, or an exception is thrown.

        Arguments
        - b: the buffer into which the data is read.
        - off: the start offset into the data array `b`.
        - len: the number of bytes to read.

        Raises
        - NullPointerException: if `b` is `null`.
        - IndexOutOfBoundsException: if `off` is negative,
                       `len` is negative, or `len` is greater than
                       `b.length - off`.
        - EOFException: if this file reaches the end before reading
                       all the bytes.
        - IOException: if an I/O error occurs.
        """
        ...


    def skipBytes(self, n: int) -> int:
        """
        Attempts to skip over `n` bytes of input discarding the
        skipped bytes.
        
        
        This method may skip over some smaller number of bytes, possibly zero.
        This may result from any of a number of conditions; reaching end of
        file before `n` bytes have been skipped is only one
        possibility. This method never throws an `EOFException`.
        The actual number of bytes skipped is returned.  If `n`
        is negative, no bytes are skipped.

        Arguments
        - n: the number of bytes to be skipped.

        Returns
        - the actual number of bytes skipped.

        Raises
        - IOException: if an I/O error occurs.
        """
        ...


    def write(self, b: int) -> None:
        """
        Writes the specified byte to this file. The write starts at
        the current file pointer.

        Arguments
        - b: the `byte` to be written.

        Raises
        - IOException: if an I/O error occurs.
        """
        ...


    def write(self, b: list[int]) -> None:
        """
        Writes `b.length` bytes from the specified byte array
        to this file, starting at the current file pointer.

        Arguments
        - b: the data.

        Raises
        - IOException: if an I/O error occurs.
        """
        ...


    def write(self, b: list[int], off: int, len: int) -> None:
        """
        Writes `len` bytes from the specified byte array
        starting at offset `off` to this file.

        Arguments
        - b: the data.
        - off: the start offset in the data.
        - len: the number of bytes to write.

        Raises
        - IOException: if an I/O error occurs.
        """
        ...


    def getFilePointer(self) -> int:
        """
        Returns the current offset in this file.

        Returns
        - the offset from the beginning of the file, in bytes,
                    at which the next read or write occurs.

        Raises
        - IOException: if an I/O error occurs.
        """
        ...


    def seek(self, pos: int) -> None:
        """
        Sets the file-pointer offset, measured from the beginning of this
        file, at which the next read or write occurs.  The offset may be
        set beyond the end of the file. Setting the offset beyond the end
        of the file does not change the file length.  The file length will
        change only by writing after the offset has been set beyond the end
        of the file.

        Arguments
        - pos: the offset position, measured in bytes from the
                          beginning of the file, at which to set the file
                          pointer.

        Raises
        - IOException: if `pos` is less than
                                 `0` or if an I/O error occurs.
        """
        ...


    def length(self) -> int:
        """
        Returns the length of this file.

        Returns
        - the length of this file, measured in bytes.

        Raises
        - IOException: if an I/O error occurs.
        """
        ...


    def setLength(self, newLength: int) -> None:
        """
        Sets the length of this file.
        
         If the present length of the file as returned by the
        `length` method is greater than the `newLength`
        argument then the file will be truncated.  In this case, if the file
        offset as returned by the `getFilePointer` method is greater
        than `newLength` then after this method returns the offset
        will be equal to `newLength`.
        
         If the present length of the file as returned by the
        `length` method is smaller than the `newLength`
        argument then the file will be extended.  In this case, the contents of
        the extended portion of the file are not defined.

        Arguments
        - newLength: The desired length of the file

        Raises
        - IOException: If an I/O error occurs

        Since
        - 1.2
        """
        ...


    def close(self) -> None:
        """
        Closes this random access file stream and releases any system
        resources associated with the stream. A closed random access
        file cannot perform input or output operations and cannot be
        reopened.
        
         If this file has an associated channel then the channel is closed
        as well.

        Raises
        - IOException: if an I/O error occurs.

        Unknown Tags
        - 1.4
        """
        ...


    def readBoolean(self) -> bool:
        """
        Reads a `boolean` from this file. This method reads a
        single byte from the file, starting at the current file pointer.
        A value of `0` represents
        `False`. Any other value represents `True`.
        This method blocks until the byte is read, the end of the stream
        is detected, or an exception is thrown.

        Returns
        - the `boolean` value read.

        Raises
        - EOFException: if this file has reached the end.
        - IOException: if an I/O error occurs.
        """
        ...


    def readByte(self) -> int:
        """
        Reads a signed eight-bit value from this file. This method reads a
        byte from the file, starting from the current file pointer.
        If the byte read is `b`, where
        `0 <= b <= 255`,
        then the result is:
        <blockquote>```
            (byte)(b)
        ```</blockquote>
        
        This method blocks until the byte is read, the end of the stream
        is detected, or an exception is thrown.

        Returns
        - the next byte of this file as a signed eight-bit
                    `byte`.

        Raises
        - EOFException: if this file has reached the end.
        - IOException: if an I/O error occurs.
        """
        ...


    def readUnsignedByte(self) -> int:
        """
        Reads an unsigned eight-bit number from this file. This method reads
        a byte from this file, starting at the current file pointer,
        and returns that byte.
        
        This method blocks until the byte is read, the end of the stream
        is detected, or an exception is thrown.

        Returns
        - the next byte of this file, interpreted as an unsigned
                    eight-bit number.

        Raises
        - EOFException: if this file has reached the end.
        - IOException: if an I/O error occurs.
        """
        ...


    def readShort(self) -> int:
        """
        Reads a signed 16-bit number from this file. The method reads two
        bytes from this file, starting at the current file pointer.
        If the two bytes read, in order, are
        `b1` and `b2`, where each of the two values is
        between `0` and `255`, inclusive, then the
        result is equal to:
        <blockquote>```
            (short)((b1 &lt;&lt; 8) | b2)
        ```</blockquote>
        
        This method blocks until the two bytes are read, the end of the
        stream is detected, or an exception is thrown.

        Returns
        - the next two bytes of this file, interpreted as a signed
                    16-bit number.

        Raises
        - EOFException: if this file reaches the end before reading
                      two bytes.
        - IOException: if an I/O error occurs.
        """
        ...


    def readUnsignedShort(self) -> int:
        """
        Reads an unsigned 16-bit number from this file. This method reads
        two bytes from the file, starting at the current file pointer.
        If the bytes read, in order, are
        `b1` and `b2`, where
        `0 <= b1, b2 <= 255`,
        then the result is equal to:
        <blockquote>```
            (b1 &lt;&lt; 8) | b2
        ```</blockquote>
        
        This method blocks until the two bytes are read, the end of the
        stream is detected, or an exception is thrown.

        Returns
        - the next two bytes of this file, interpreted as an unsigned
                    16-bit integer.

        Raises
        - EOFException: if this file reaches the end before reading
                      two bytes.
        - IOException: if an I/O error occurs.
        """
        ...


    def readChar(self) -> str:
        """
        Reads a character from this file. This method reads two
        bytes from the file, starting at the current file pointer.
        If the bytes read, in order, are
        `b1` and `b2`, where
        `0 <= b1, b2 <= 255`,
        then the result is equal to:
        <blockquote>```
            (char)((b1 &lt;&lt; 8) | b2)
        ```</blockquote>
        
        This method blocks until the two bytes are read, the end of the
        stream is detected, or an exception is thrown.

        Returns
        - the next two bytes of this file, interpreted as a
                         `char`.

        Raises
        - EOFException: if this file reaches the end before reading
                      two bytes.
        - IOException: if an I/O error occurs.
        """
        ...


    def readInt(self) -> int:
        """
        Reads a signed 32-bit integer from this file. This method reads 4
        bytes from the file, starting at the current file pointer.
        If the bytes read, in order, are `b1`,
        `b2`, `b3`, and `b4`, where
        `0 <= b1, b2, b3, b4 <= 255`,
        then the result is equal to:
        <blockquote>```
            (b1 &lt;&lt; 24) | (b2 &lt;&lt; 16) + (b3 &lt;&lt; 8) + b4
        ```</blockquote>
        
        This method blocks until the four bytes are read, the end of the
        stream is detected, or an exception is thrown.

        Returns
        - the next four bytes of this file, interpreted as an
                    `int`.

        Raises
        - EOFException: if this file reaches the end before reading
                      four bytes.
        - IOException: if an I/O error occurs.
        """
        ...


    def readLong(self) -> int:
        """
        Reads a signed 64-bit integer from this file. This method reads eight
        bytes from the file, starting at the current file pointer.
        If the bytes read, in order, are
        `b1`, `b2`, `b3`,
        `b4`, `b5`, `b6`,
        `b7`, and `b8,` where:
        <blockquote>```
            0 &lt;= b1, b2, b3, b4, b5, b6, b7, b8 &lt;=255,
        ```</blockquote>
        
        then the result is equal to:
        <blockquote>```
            ((long)b1 &lt;&lt; 56) + ((long)b2 &lt;&lt; 48)
            + ((long)b3 &lt;&lt; 40) + ((long)b4 &lt;&lt; 32)
            + ((long)b5 &lt;&lt; 24) + ((long)b6 &lt;&lt; 16)
            + ((long)b7 &lt;&lt; 8) + b8
        ```</blockquote>
        
        This method blocks until the eight bytes are read, the end of the
        stream is detected, or an exception is thrown.

        Returns
        - the next eight bytes of this file, interpreted as a
                    `long`.

        Raises
        - EOFException: if this file reaches the end before reading
                      eight bytes.
        - IOException: if an I/O error occurs.
        """
        ...


    def readFloat(self) -> float:
        """
        Reads a `float` from this file. This method reads an
        `int` value, starting at the current file pointer,
        as if by the `readInt` method
        and then converts that `int` to a `float`
        using the `intBitsToFloat` method in class
        `Float`.
        
        This method blocks until the four bytes are read, the end of the
        stream is detected, or an exception is thrown.

        Returns
        - the next four bytes of this file, interpreted as a
                    `float`.

        Raises
        - EOFException: if this file reaches the end before reading
                    four bytes.
        - IOException: if an I/O error occurs.

        See
        - java.lang.Float.intBitsToFloat(int)
        """
        ...


    def readDouble(self) -> float:
        """
        Reads a `double` from this file. This method reads a
        `long` value, starting at the current file pointer,
        as if by the `readLong` method
        and then converts that `long` to a `double`
        using the `longBitsToDouble` method in
        class `Double`.
        
        This method blocks until the eight bytes are read, the end of the
        stream is detected, or an exception is thrown.

        Returns
        - the next eight bytes of this file, interpreted as a
                    `double`.

        Raises
        - EOFException: if this file reaches the end before reading
                    eight bytes.
        - IOException: if an I/O error occurs.

        See
        - java.lang.Double.longBitsToDouble(long)
        """
        ...


    def readLine(self) -> str:
        ...


    def readUTF(self) -> str:
        """
        Reads in a string from this file. The string has been encoded
        using a
        <a href="DataInput.html#modified-utf-8">modified UTF-8</a>
        format.
        
        The first two bytes are read, starting from the current file
        pointer, as if by
        `readUnsignedShort`. This value gives the number of
        following bytes that are in the encoded string, not
        the length of the resulting string. The following bytes are then
        interpreted as bytes encoding characters in the modified UTF-8 format
        and are converted into characters.
        
        This method blocks until all the bytes are read, the end of the
        stream is detected, or an exception is thrown.

        Returns
        - a Unicode string.

        Raises
        - EOFException: if this file reaches the end before
                      reading all the bytes.
        - IOException: if an I/O error occurs.
        - UTFDataFormatException: if the bytes do not represent
                      valid modified UTF-8 encoding of a Unicode string.

        See
        - java.io.RandomAccessFile.readUnsignedShort()
        """
        ...


    def writeBoolean(self, v: bool) -> None:
        """
        Writes a `boolean` to the file as a one-byte value. The
        value `True` is written out as the value
        `(byte)1`; the value `False` is written out
        as the value `(byte)0`. The write starts at
        the current position of the file pointer.

        Arguments
        - v: a `boolean` value to be written.

        Raises
        - IOException: if an I/O error occurs.
        """
        ...


    def writeByte(self, v: int) -> None:
        """
        Writes a `byte` to the file as a one-byte value. The
        write starts at the current position of the file pointer.

        Arguments
        - v: a `byte` value to be written.

        Raises
        - IOException: if an I/O error occurs.
        """
        ...


    def writeShort(self, v: int) -> None:
        """
        Writes a `short` to the file as two bytes, high byte first.
        The write starts at the current position of the file pointer.

        Arguments
        - v: a `short` to be written.

        Raises
        - IOException: if an I/O error occurs.
        """
        ...


    def writeChar(self, v: int) -> None:
        """
        Writes a `char` to the file as a two-byte value, high
        byte first. The write starts at the current position of the
        file pointer.

        Arguments
        - v: a `char` value to be written.

        Raises
        - IOException: if an I/O error occurs.
        """
        ...


    def writeInt(self, v: int) -> None:
        """
        Writes an `int` to the file as four bytes, high byte first.
        The write starts at the current position of the file pointer.

        Arguments
        - v: an `int` to be written.

        Raises
        - IOException: if an I/O error occurs.
        """
        ...


    def writeLong(self, v: int) -> None:
        """
        Writes a `long` to the file as eight bytes, high byte first.
        The write starts at the current position of the file pointer.

        Arguments
        - v: a `long` to be written.

        Raises
        - IOException: if an I/O error occurs.
        """
        ...


    def writeFloat(self, v: float) -> None:
        """
        Converts the float argument to an `int` using the
        `floatToIntBits` method in class `Float`,
        and then writes that `int` value to the file as a
        four-byte quantity, high byte first. The write starts at the
        current position of the file pointer.

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
        and then writes that `long` value to the file as an
        eight-byte quantity, high byte first. The write starts at the current
        position of the file pointer.

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
        Writes the string to the file as a sequence of bytes. Each
        character in the string is written out, in sequence, by discarding
        its high eight bits. The write starts at the current position of
        the file pointer.

        Arguments
        - s: a string of bytes to be written.

        Raises
        - IOException: if an I/O error occurs.
        """
        ...


    def writeChars(self, s: str) -> None:
        """
        Writes a string to the file as a sequence of characters. Each
        character is written to the data output stream as if by the
        `writeChar` method. The write starts at the current
        position of the file pointer.

        Arguments
        - s: a `String` value to be written.

        Raises
        - IOException: if an I/O error occurs.

        See
        - java.io.RandomAccessFile.writeChar(int)
        """
        ...


    def writeUTF(self, str: str) -> None:
        """
        Writes a string to the file using
        <a href="DataInput.html#modified-utf-8">modified UTF-8</a>
        encoding in a machine-independent manner.
        
        First, two bytes are written to the file, starting at the
        current file pointer, as if by the
        `writeShort` method giving the number of bytes to
        follow. This value is the number of bytes actually written out,
        not the length of the string. Following the length, each character
        of the string is output, in sequence, using the modified UTF-8 encoding
        for each character.

        Arguments
        - str: a string to be written.

        Raises
        - IOException: if an I/O error occurs.
        """
        ...
