"""
Python module generated from Java source file java.io.BufferedInputStream

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.io import *
from jdk.internal.misc import Unsafe
from jdk.internal.util import ArraysSupport
from typing import Any, Callable, Iterable, Tuple


class BufferedInputStream(FilterInputStream):
    """
    A `BufferedInputStream` adds
    functionality to another input stream-namely,
    the ability to buffer the input and to
    support the `mark` and `reset`
    methods. When  the `BufferedInputStream`
    is created, an internal buffer array is
    created. As bytes  from the stream are read
    or skipped, the internal buffer is refilled
    as necessary  from the contained input stream,
    many bytes at a time. The `mark`
    operation  remembers a point in the input
    stream and the `reset` operation
    causes all the  bytes read since the most
    recent `mark` operation to be
    reread before new bytes are  taken from
    the contained input stream.

    Author(s)
    - Arthur van Hoff

    Since
    - 1.0
    """

    def __init__(self, in: "InputStream"):
        """
        Creates a `BufferedInputStream`
        and saves its  argument, the input stream
        `in`, for later use. An internal
        buffer array is created and  stored in `buf`.

        Arguments
        - in: the underlying input stream.
        """
        ...


    def __init__(self, in: "InputStream", size: int):
        """
        Creates a `BufferedInputStream`
        with the specified buffer size,
        and saves its  argument, the input stream
        `in`, for later use.  An internal
        buffer array of length  `size`
        is created and stored in `buf`.

        Arguments
        - in: the underlying input stream.
        - size: the buffer size.

        Raises
        - IllegalArgumentException: if `size <= 0`.
        """
        ...


    def read(self) -> int:
        """
        See
        the general contract of the `read`
        method of `InputStream`.

        Returns
        - the next byte of data, or `-1` if the end of the
                    stream is reached.

        Raises
        - IOException: if this input stream has been closed by
                                 invoking its .close() method,
                                 or an I/O error occurs.

        See
        - java.io.FilterInputStream.in
        """
        ...


    def read(self, b: list[int], off: int, len: int) -> int:
        """
        Reads bytes from this byte-input stream into the specified byte array,
        starting at the given offset.
        
         This method implements the general contract of the corresponding
        InputStream.read(byte[], int, int) read method of
        the InputStream class.  As an additional
        convenience, it attempts to read as many bytes as possible by repeatedly
        invoking the `read` method of the underlying stream.  This
        iterated `read` continues until one of the following
        conditions becomes True: 
        
          -  The specified number of bytes have been read,
        
          -  The `read` method of the underlying stream returns
          `-1`, indicating end-of-file, or
        
          -  The `available` method of the underlying stream
          returns zero, indicating that further input requests would block.
        
         If the first `read` on the underlying stream returns
        `-1` to indicate end-of-file then this method returns
        `-1`.  Otherwise this method returns the number of bytes
        actually read.
        
         Subclasses of this class are encouraged, but not required, to
        attempt to read as many bytes as possible in the same fashion.

        Arguments
        - b: destination buffer.
        - off: offset at which to start storing bytes.
        - len: maximum number of bytes to read.

        Returns
        - the number of bytes read, or `-1` if the end of
                    the stream has been reached.

        Raises
        - IOException: if this input stream has been closed by
                                 invoking its .close() method,
                                 or an I/O error occurs.
        """
        ...


    def skip(self, n: int) -> int:
        """
        See the general contract of the `skip`
        method of `InputStream`.

        Raises
        - IOException: if this input stream has been closed by
                             invoking its .close() method,
                             `in.skip(n)` throws an IOException,
                             or an I/O error occurs.
        """
        ...


    def available(self) -> int:
        """
        Returns an estimate of the number of bytes that can be read (or
        skipped over) from this input stream without blocking by the next
        invocation of a method for this input stream. The next invocation might be
        the same thread or another thread.  A single read or skip of this
        many bytes will not block, but may read or skip fewer bytes.
        
        This method returns the sum of the number of bytes remaining to be read in
        the buffer (`count - pos`) and the result of calling the
        java.io.FilterInputStream.in in`.available()`.

        Returns
        - an estimate of the number of bytes that can be read (or skipped
                    over) from this input stream without blocking.

        Raises
        - IOException: if this input stream has been closed by
                                 invoking its .close() method,
                                 or an I/O error occurs.
        """
        ...


    def mark(self, readlimit: int) -> None:
        """
        See the general contract of the `mark`
        method of `InputStream`.

        Arguments
        - readlimit: the maximum limit of bytes that can be read before
                             the mark position becomes invalid.

        See
        - java.io.BufferedInputStream.reset()
        """
        ...


    def reset(self) -> None:
        """
        See the general contract of the `reset`
        method of `InputStream`.
        
        If `markpos` is `-1`
        (no mark has been set or the mark has been
        invalidated), an `IOException`
        is thrown. Otherwise, `pos` is
        set equal to `markpos`.

        Raises
        - IOException: if this stream has not been marked or,
                         if the mark has been invalidated, or the stream
                         has been closed by invoking its .close()
                         method, or an I/O error occurs.

        See
        - java.io.BufferedInputStream.mark(int)
        """
        ...


    def markSupported(self) -> bool:
        """
        Tests if this input stream supports the `mark`
        and `reset` methods. The `markSupported`
        method of `BufferedInputStream` returns
        `True`.

        Returns
        - a `boolean` indicating if this stream type supports
                 the `mark` and `reset` methods.

        See
        - java.io.InputStream.reset()
        """
        ...


    def close(self) -> None:
        """
        Closes this input stream and releases any system resources
        associated with the stream.
        Once the stream has been closed, further read(), available(), reset(),
        or skip() invocations will throw an IOException.
        Closing a previously closed stream has no effect.

        Raises
        - IOException: if an I/O error occurs.
        """
        ...
