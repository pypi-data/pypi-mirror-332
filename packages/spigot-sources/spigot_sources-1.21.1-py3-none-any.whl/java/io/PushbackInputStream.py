"""
Python module generated from Java source file java.io.PushbackInputStream

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.io import *
from typing import Any, Callable, Iterable, Tuple


class PushbackInputStream(FilterInputStream):
    """
    A `PushbackInputStream` adds
    functionality to another input stream, namely
    the  ability to "push back" or "unread" bytes,
    by storing pushed-back bytes in an internal buffer.
    This is useful in situations where
    it is convenient for a fragment of code
    to read an indefinite number of data bytes
    that  are delimited by a particular byte
    value; after reading the terminating byte,
    the  code fragment can "unread" it, so that
    the next read operation on the input stream
    will reread the byte that was pushed back.
    For example, bytes representing the  characters
    constituting an identifier might be terminated
    by a byte representing an  operator character;
    a method whose job is to read just an identifier
    can read until it  sees the operator and
    then push the operator back to be re-read.

    Author(s)
    - Jonathan Payne

    Since
    - 1.0
    """

    def __init__(self, in: "InputStream", size: int):
        """
        Creates a `PushbackInputStream`
        with a pushback buffer of the specified `size`,
        and saves its argument, the input stream
        `in`, for later use. Initially,
        the pushback buffer is empty.

        Arguments
        - in: the input stream from which bytes will be read.
        - size: the size of the pushback buffer.

        Raises
        - IllegalArgumentException: if `size <= 0`

        Since
        - 1.1
        """
        ...


    def __init__(self, in: "InputStream"):
        """
        Creates a `PushbackInputStream`
        with a 1-byte pushback buffer, and saves its argument, the input stream
        `in`, for later use. Initially,
        the pushback buffer is empty.

        Arguments
        - in: the input stream from which bytes will be read.
        """
        ...


    def read(self) -> int:
        """
        Reads the next byte of data from this input stream. The value
        byte is returned as an `int` in the range
        `0` to `255`. If no byte is available
        because the end of the stream has been reached, the value
        `-1` is returned. This method blocks until input data
        is available, the end of the stream is detected, or an exception
        is thrown.
        
         This method returns the most recently pushed-back byte, if there is
        one, and otherwise calls the `read` method of its underlying
        input stream and returns whatever value that method returns.

        Returns
        - the next byte of data, or `-1` if the end of the
                    stream has been reached.

        Raises
        - IOException: if this input stream has been closed by
                    invoking its .close() method,
                    or an I/O error occurs.

        See
        - java.io.InputStream.read()
        """
        ...


    def read(self, b: list[int], off: int, len: int) -> int:
        """
        Reads up to `len` bytes of data from this input stream into
        an array of bytes.  This method first reads any pushed-back bytes; after
        that, if fewer than `len` bytes have been read then it
        reads from the underlying input stream. If `len` is not zero, the method
        blocks until at least 1 byte of input is available; otherwise, no
        bytes are read and `0` is returned.

        Arguments
        - b: the buffer into which the data is read.
        - off: the start offset in the destination array `b`
        - len: the maximum number of bytes read.

        Returns
        - the total number of bytes read into the buffer, or
                    `-1` if there is no more data because the end of
                    the stream has been reached.

        Raises
        - NullPointerException: If `b` is `null`.
        - IndexOutOfBoundsException: If `off` is negative,
                    `len` is negative, or `len` is greater than
                    `b.length - off`
        - IOException: if this input stream has been closed by
                    invoking its .close() method,
                    or an I/O error occurs.

        See
        - java.io.InputStream.read(byte[], int, int)
        """
        ...


    def unread(self, b: int) -> None:
        """
        Pushes back a byte by copying it to the front of the pushback buffer.
        After this method returns, the next byte to be read will have the value
        `(byte)b`.

        Arguments
        - b: the `int` value whose low-order
                         byte is to be pushed back.

        Raises
        - IOException: If there is not enough room in the pushback
                   buffer for the byte, or this input stream has been closed by
                   invoking its .close() method.
        """
        ...


    def unread(self, b: list[int], off: int, len: int) -> None:
        """
        Pushes back a portion of an array of bytes by copying it to the front
        of the pushback buffer.  After this method returns, the next byte to be
        read will have the value `b[off]`, the byte after that will
        have the value `b[off+1]`, and so forth.

        Arguments
        - b: the byte array to push back.
        - off: the start offset of the data.
        - len: the number of bytes to push back.

        Raises
        - NullPointerException: If `b` is `null`.
        - IOException: If there is not enough room in the pushback
                   buffer for the specified number of bytes,
                   or this input stream has been closed by
                   invoking its .close() method.

        Since
        - 1.1
        """
        ...


    def unread(self, b: list[int]) -> None:
        """
        Pushes back an array of bytes by copying it to the front of the
        pushback buffer.  After this method returns, the next byte to be read
        will have the value `b[0]`, the byte after that will have the
        value `b[1]`, and so forth.

        Arguments
        - b: the byte array to push back

        Raises
        - NullPointerException: If `b` is `null`.
        - IOException: If there is not enough room in the pushback
                   buffer for the specified number of bytes,
                   or this input stream has been closed by
                   invoking its .close() method.

        Since
        - 1.1
        """
        ...


    def available(self) -> int:
        """
        Returns an estimate of the number of bytes that can be read (or
        skipped over) from this input stream without blocking by the next
        invocation of a method for this input stream. The next invocation might be
        the same thread or another thread.  A single read or skip of this
        many bytes will not block, but may read or skip fewer bytes.
        
         The method returns the sum of the number of bytes that have been
        pushed back and the value returned by java.io.FilterInputStream.available available.

        Returns
        - the number of bytes that can be read (or skipped over) from
                    the input stream without blocking.

        Raises
        - IOException: if this input stream has been closed by
                    invoking its .close() method,
                    or an I/O error occurs.

        See
        - java.io.InputStream.available()
        """
        ...


    def skip(self, n: int) -> int:
        """
        Skips over and discards `n` bytes of data from this
        input stream. The `skip` method may, for a variety of
        reasons, end up skipping over some smaller number of bytes,
        possibly zero.  If `n` is negative, no bytes are skipped.
        
         The `skip` method of `PushbackInputStream`
        first skips over the bytes in the pushback buffer, if any.  It then
        calls the `skip` method of the underlying input stream if
        more bytes need to be skipped.  The actual number of bytes skipped
        is returned.

        Arguments
        - n: 

        Returns
        - 

        Raises
        - IOException: if the stream has been closed by
                    invoking its .close() method,
                    `in.skip(n)` throws an IOException,
                    or an I/O error occurs.

        See
        - java.io.InputStream.skip(long n)

        Since
        - 1.2
        """
        ...


    def markSupported(self) -> bool:
        """
        Tests if this input stream supports the `mark` and
        `reset` methods, which it does not.

        Returns
        - `False`, since this class does not support the
                  `mark` and `reset` methods.

        See
        - java.io.InputStream.reset()
        """
        ...


    def mark(self, readlimit: int) -> None:
        """
        Marks the current position in this input stream.
        
         The `mark` method of `PushbackInputStream`
        does nothing.

        Arguments
        - readlimit: the maximum limit of bytes that can be read before
                             the mark position becomes invalid.

        See
        - java.io.InputStream.reset()
        """
        ...


    def reset(self) -> None:
        """
        Repositions this stream to the position at the time the
        `mark` method was last called on this input stream.
        
         The method `reset` for class
        `PushbackInputStream` does nothing except throw an
        `IOException`.

        Raises
        - IOException: if this method is invoked.

        See
        - java.io.IOException
        """
        ...


    def close(self) -> None:
        """
        Closes this input stream and releases any system resources
        associated with the stream.
        Once the stream has been closed, further read(), unread(),
        available(), reset(), or skip() invocations will throw an IOException.
        Closing a previously closed stream has no effect.

        Raises
        - IOException: if an I/O error occurs.
        """
        ...
