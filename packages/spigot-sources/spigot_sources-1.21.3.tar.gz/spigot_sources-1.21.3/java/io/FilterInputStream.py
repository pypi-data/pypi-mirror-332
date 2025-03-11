"""
Python module generated from Java source file java.io.FilterInputStream

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.io import *
from typing import Any, Callable, Iterable, Tuple


class FilterInputStream(InputStream):
    """
    A `FilterInputStream` contains
    some other input stream, which it uses as
    its  basic source of data, possibly transforming
    the data along the way or providing  additional
    functionality. The class `FilterInputStream`
    itself simply overrides all  methods of
    `InputStream` with versions that
    pass all requests to the contained  input
    stream. Subclasses of `FilterInputStream`
    may further override some of  these methods
    and may also provide additional methods
    and fields.

    Author(s)
    - Jonathan Payne

    Since
    - 1.0
    """

    def read(self) -> int:
        """
        Reads the next byte of data from this input stream. The value
        byte is returned as an `int` in the range
        `0` to `255`. If no byte is available
        because the end of the stream has been reached, the value
        `-1` is returned. This method blocks until input data
        is available, the end of the stream is detected, or an exception
        is thrown.
        
        This method
        simply performs `in.read()` and returns the result.

        Returns
        - the next byte of data, or `-1` if the end of the
                    stream is reached.

        Raises
        - IOException: if an I/O error occurs.

        See
        - java.io.FilterInputStream.in
        """
        ...


    def read(self, b: list[int]) -> int:
        """
        Reads up to `b.length` bytes of data from this
        input stream into an array of bytes. This method blocks until some
        input is available.
        
        This method simply performs the call
        `read(b, 0, b.length)` and returns
        the  result. It is important that it does
        *not* do `in.read(b)` instead;
        certain subclasses of  `FilterInputStream`
        depend on the implementation strategy actually
        used.

        Arguments
        - b: the buffer into which the data is read.

        Returns
        - the total number of bytes read into the buffer, or
                    `-1` if there is no more data because the end of
                    the stream has been reached.

        Raises
        - IOException: if an I/O error occurs.

        See
        - java.io.FilterInputStream.read(byte[], int, int)
        """
        ...


    def read(self, b: list[int], off: int, len: int) -> int:
        """
        Reads up to `len` bytes of data from this input stream
        into an array of bytes. If `len` is not zero, the method
        blocks until some input is available; otherwise, no
        bytes are read and `0` is returned.
        
        This method simply performs `in.read(b, off, len)`
        and returns the result.

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
        - IOException: if an I/O error occurs.

        See
        - java.io.FilterInputStream.in
        """
        ...


    def skip(self, n: int) -> int:
        """
        Skips over and discards `n` bytes of data from the
        input stream. The `skip` method may, for a variety of
        reasons, end up skipping over some smaller number of bytes,
        possibly `0`. The actual number of bytes skipped is
        returned.
        
        This method simply performs `in.skip(n)`.

        Arguments
        - n: the number of bytes to be skipped.

        Returns
        - the actual number of bytes skipped.

        Raises
        - IOException: if `in.skip(n)` throws an IOException.
        """
        ...


    def available(self) -> int:
        """
        Returns an estimate of the number of bytes that can be read (or
        skipped over) from this input stream without blocking by the next
        caller of a method for this input stream. The next caller might be
        the same thread or another thread.  A single read or skip of this
        many bytes will not block, but may read or skip fewer bytes.
        
        This method returns the result of .in in.available().

        Returns
        - an estimate of the number of bytes that can be read (or skipped
                    over) from this input stream without blocking.

        Raises
        - IOException: if an I/O error occurs.
        """
        ...


    def close(self) -> None:
        """
        Closes this input stream and releases any system resources
        associated with the stream.
        This
        method simply performs `in.close()`.

        Raises
        - IOException: if an I/O error occurs.

        See
        - java.io.FilterInputStream.in
        """
        ...


    def mark(self, readlimit: int) -> None:
        """
        Marks the current position in this input stream. A subsequent
        call to the `reset` method repositions this stream at
        the last marked position so that subsequent reads re-read the same bytes.
        
        The `readlimit` argument tells this input stream to
        allow that many bytes to be read before the mark position gets
        invalidated.
        
        This method simply performs `in.mark(readlimit)`.

        Arguments
        - readlimit: the maximum limit of bytes that can be read before
                             the mark position becomes invalid.

        See
        - java.io.FilterInputStream.reset()
        """
        ...


    def reset(self) -> None:
        """
        Repositions this stream to the position at the time the
        `mark` method was last called on this input stream.
        
        This method
        simply performs `in.reset()`.
        
        Stream marks are intended to be used in
        situations where you need to read ahead a little to see what's in
        the stream. Often this is most easily done by invoking some
        general parser. If the stream is of the type handled by the
        parse, it just chugs along happily. If the stream is not of
        that type, the parser should toss an exception when it fails.
        If this happens within readlimit bytes, it allows the outer
        code to reset the stream and try another parser.

        Raises
        - IOException: if the stream has not been marked or if the
                      mark has been invalidated.

        See
        - java.io.FilterInputStream.mark(int)
        """
        ...


    def markSupported(self) -> bool:
        """
        Tests if this input stream supports the `mark`
        and `reset` methods.
        This method
        simply performs `in.markSupported()`.

        Returns
        - `True` if this stream type supports the
                 `mark` and `reset` method;
                 `False` otherwise.

        See
        - java.io.InputStream.reset()
        """
        ...
