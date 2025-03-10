"""
Python module generated from Java source file java.io.OutputStream

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.io import *
from java.util import Objects
from typing import Any, Callable, Iterable, Tuple


class OutputStream(Closeable, Flushable):
    """
    This abstract class is the superclass of all classes representing
    an output stream of bytes. An output stream accepts output bytes
    and sends them to some sink.
    
    Applications that need to define a subclass of
    `OutputStream` must always provide at least a method
    that writes one byte of output.

    Author(s)
    - Arthur van Hoff

    See
    - java.io.OutputStream.write(int)

    Since
    - 1.0
    """

    def __init__(self):
        """
        Constructor for subclasses to call.
        """
        ...


    @staticmethod
    def nullOutputStream() -> "OutputStream":
        """
        Returns a new `OutputStream` which discards all bytes.  The
        returned stream is initially open.  The stream is closed by calling
        the `close()` method.  Subsequent calls to `close()` have
        no effect.
        
         While the stream is open, the `write(int)`, `write(byte[])`, and `write(byte[], int, int)` methods do nothing.
        After the stream has been closed, these methods all throw `IOException`.
        
         The `flush()` method does nothing.

        Returns
        - an `OutputStream` which discards all bytes

        Since
        - 11
        """
        ...


    def write(self, b: int) -> None:
        """
        Writes the specified byte to this output stream. The general
        contract for `write` is that one byte is written
        to the output stream. The byte to be written is the eight
        low-order bits of the argument `b`. The 24
        high-order bits of `b` are ignored.
        
        Subclasses of `OutputStream` must provide an
        implementation for this method.

        Arguments
        - b: the `byte`.

        Raises
        - IOException: if an I/O error occurs. In particular,
                    an `IOException` may be thrown if the
                    output stream has been closed.
        """
        ...


    def write(self, b: list[int]) -> None:
        """
        Writes `b.length` bytes from the specified byte array
        to this output stream. The general contract for `write(b)`
        is that it should have exactly the same effect as the call
        `write(b, 0, b.length)`.

        Arguments
        - b: the data.

        Raises
        - IOException: if an I/O error occurs.

        See
        - java.io.OutputStream.write(byte[], int, int)
        """
        ...


    def write(self, b: list[int], off: int, len: int) -> None:
        """
        Writes `len` bytes from the specified byte array
        starting at offset `off` to this output stream.
        The general contract for `write(b, off, len)` is that
        some of the bytes in the array `b` are written to the
        output stream in order; element `b[off]` is the first
        byte written and `b[off+len-1]` is the last byte written
        by this operation.
        
        The `write` method of `OutputStream` calls
        the write method of one argument on each of the bytes to be
        written out. Subclasses are encouraged to override this method and
        provide a more efficient implementation.
        
        If `b` is `null`, a
        `NullPointerException` is thrown.
        
        If `off` is negative, or `len` is negative, or
        `off+len` is greater than the length of the array
        `b`, then an `IndexOutOfBoundsException` is thrown.

        Arguments
        - b: the data.
        - off: the start offset in the data.
        - len: the number of bytes to write.

        Raises
        - IOException: if an I/O error occurs. In particular,
                    an `IOException` is thrown if the output
                    stream is closed.
        """
        ...


    def flush(self) -> None:
        """
        Flushes this output stream and forces any buffered output bytes
        to be written out. The general contract of `flush` is
        that calling it is an indication that, if any bytes previously
        written have been buffered by the implementation of the output
        stream, such bytes should immediately be written to their
        intended destination.
        
        If the intended destination of this stream is an abstraction provided by
        the underlying operating system, for example a file, then flushing the
        stream guarantees only that bytes previously written to the stream are
        passed to the operating system for writing; it does not guarantee that
        they are actually written to a physical device such as a disk drive.
        
        The `flush` method of `OutputStream` does nothing.

        Raises
        - IOException: if an I/O error occurs.
        """
        ...


    def close(self) -> None:
        """
        Closes this output stream and releases any system resources
        associated with this stream. The general contract of `close`
        is that it closes the output stream. A closed stream cannot perform
        output operations and cannot be reopened.
        
        The `close` method of `OutputStream` does nothing.

        Raises
        - IOException: if an I/O error occurs.
        """
        ...
