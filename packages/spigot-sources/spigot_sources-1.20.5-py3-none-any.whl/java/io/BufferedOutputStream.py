"""
Python module generated from Java source file java.io.BufferedOutputStream

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.io import *
from typing import Any, Callable, Iterable, Tuple


class BufferedOutputStream(FilterOutputStream):
    """
    The class implements a buffered output stream. By setting up such
    an output stream, an application can write bytes to the underlying
    output stream without necessarily causing a call to the underlying
    system for each byte written.

    Author(s)
    - Arthur van Hoff

    Since
    - 1.0
    """

    def __init__(self, out: "OutputStream"):
        """
        Creates a new buffered output stream to write data to the
        specified underlying output stream.

        Arguments
        - out: the underlying output stream.
        """
        ...


    def __init__(self, out: "OutputStream", size: int):
        """
        Creates a new buffered output stream to write data to the
        specified underlying output stream with the specified buffer
        size.

        Arguments
        - out: the underlying output stream.
        - size: the buffer size.

        Raises
        - IllegalArgumentException: if size &lt;= 0.
        """
        ...


    def write(self, b: int) -> None:
        """
        Writes the specified byte to this buffered output stream.

        Arguments
        - b: the byte to be written.

        Raises
        - IOException: if an I/O error occurs.
        """
        ...


    def write(self, b: list[int], off: int, len: int) -> None:
        """
        Writes `len` bytes from the specified byte array
        starting at offset `off` to this buffered output stream.
        
         Ordinarily this method stores bytes from the given array into this
        stream's buffer, flushing the buffer to the underlying output stream as
        needed.  If the requested length is at least as large as this stream's
        buffer, however, then this method will flush the buffer and write the
        bytes directly to the underlying output stream.  Thus redundant
        `BufferedOutputStream`s will not copy data unnecessarily.

        Arguments
        - b: the data.
        - off: the start offset in the data.
        - len: the number of bytes to write.

        Raises
        - IOException: if an I/O error occurs.
        """
        ...


    def flush(self) -> None:
        """
        Flushes this buffered output stream. This forces any buffered
        output bytes to be written out to the underlying output stream.

        Raises
        - IOException: if an I/O error occurs.

        See
        - java.io.FilterOutputStream.out
        """
        ...
