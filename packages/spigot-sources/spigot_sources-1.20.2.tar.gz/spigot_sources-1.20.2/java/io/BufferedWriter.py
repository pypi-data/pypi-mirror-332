"""
Python module generated from Java source file java.io.BufferedWriter

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.io import *
from typing import Any, Callable, Iterable, Tuple


class BufferedWriter(Writer):

    def __init__(self, out: "Writer"):
        """
        Creates a buffered character-output stream that uses a default-sized
        output buffer.

        Arguments
        - out: A Writer
        """
        ...


    def __init__(self, out: "Writer", sz: int):
        """
        Creates a new buffered character-output stream that uses an output
        buffer of the given size.

        Arguments
        - out: A Writer
        - sz: Output-buffer size, a positive integer

        Raises
        - IllegalArgumentException: If `sz <= 0`
        """
        ...


    def write(self, c: int) -> None:
        """
        Writes a single character.

        Raises
        - IOException: If an I/O error occurs
        """
        ...


    def write(self, cbuf: list[str], off: int, len: int) -> None:
        """
        Writes a portion of an array of characters.
        
         Ordinarily this method stores characters from the given array into
        this stream's buffer, flushing the buffer to the underlying stream as
        needed.  If the requested length is at least as large as the buffer,
        however, then this method will flush the buffer and write the characters
        directly to the underlying stream.  Thus redundant
        `BufferedWriter`s will not copy data unnecessarily.

        Arguments
        - cbuf: A character array
        - off: Offset from which to start reading characters
        - len: Number of characters to write

        Raises
        - IndexOutOfBoundsException: If `off` is negative, or `len` is negative,
                 or `off + len` is negative or greater than the length
                 of the given array
        - IOException: If an I/O error occurs
        """
        ...


    def write(self, s: str, off: int, len: int) -> None:
        """
        Writes a portion of a String.

        Arguments
        - s: String to be written
        - off: Offset from which to start reading characters
        - len: Number of characters to be written

        Raises
        - IndexOutOfBoundsException: If `off` is negative,
                 or `off + len` is greater than the length
                 of the given string
        - IOException: If an I/O error occurs

        Unknown Tags
        - While the specification of this method in the
        java.io.Writer.write(java.lang.String,int,int) superclass
        recommends that an IndexOutOfBoundsException be thrown
        if `len` is negative or `off + len` is negative,
        the implementation in this class does not throw such an exception in
        these cases but instead simply writes no characters.
        """
        ...


    def newLine(self) -> None:
        """
        Writes a line separator.  The line separator string is defined by the
        system property `line.separator`, and is not necessarily a single
        newline ('\n') character.

        Raises
        - IOException: If an I/O error occurs
        """
        ...


    def flush(self) -> None:
        """
        Flushes the stream.

        Raises
        - IOException: If an I/O error occurs
        """
        ...


    def close(self) -> None:
        ...
