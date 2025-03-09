"""
Python module generated from Java source file java.io.BufferedReader

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.io import *
from java.util import Iterator
from java.util import NoSuchElementException
from java.util import Objects
from java.util import Spliterator
from java.util.stream import Stream
from java.util.stream import StreamSupport
from typing import Any, Callable, Iterable, Tuple


class BufferedReader(Reader):

    def __init__(self, in: "Reader", sz: int):
        """
        Creates a buffering character-input stream that uses an input buffer of
        the specified size.

        Arguments
        - in: A Reader
        - sz: Input-buffer size

        Raises
        - IllegalArgumentException: If `sz <= 0`
        """
        ...


    def __init__(self, in: "Reader"):
        """
        Creates a buffering character-input stream that uses a default-sized
        input buffer.

        Arguments
        - in: A Reader
        """
        ...


    def read(self) -> int:
        """
        Reads a single character.

        Returns
        - The character read, as an integer in the range
                0 to 65535 (`0x00-0xffff`), or -1 if the
                end of the stream has been reached

        Raises
        - IOException: If an I/O error occurs
        """
        ...


    def read(self, cbuf: list[str], off: int, len: int) -> int:
        """
        Reads characters into a portion of an array.
        
         This method implements the general contract of the corresponding
        Reader.read(char[], int, int) read method of the
        Reader class.  As an additional convenience, it
        attempts to read as many characters as possible by repeatedly invoking
        the `read` method of the underlying stream.  This iterated
        `read` continues until one of the following conditions becomes
        True:
        
        
          -  The specified number of characters have been read,
        
          -  The `read` method of the underlying stream returns
          `-1`, indicating end-of-file, or
        
          -  The `ready` method of the underlying stream
          returns `False`, indicating that further input requests
          would block.
        
        
        If the first `read` on the underlying stream returns
        `-1` to indicate end-of-file then this method returns
        `-1`.  Otherwise this method returns the number of characters
        actually read.
        
         Subclasses of this class are encouraged, but not required, to
        attempt to read as many characters as possible in the same fashion.
        
         Ordinarily this method takes characters from this stream's character
        buffer, filling it from the underlying stream as necessary.  If,
        however, the buffer is empty, the mark is not valid, and the requested
        length is at least as large as the buffer, then this method will read
        characters directly from the underlying stream into the given array.
        Thus redundant `BufferedReader`s will not copy data
        unnecessarily.

        Arguments
        - cbuf: 
        - off: 
        - len: 

        Returns
        - 

        Raises
        - IndexOutOfBoundsException: 
        - IOException: 
        """
        ...


    def readLine(self) -> str:
        """
        Reads a line of text.  A line is considered to be terminated by any one
        of a line feed ('\n'), a carriage return ('\r'), a carriage return
        followed immediately by a line feed, or by reaching the end-of-file
        (EOF).

        Returns
        - A String containing the contents of the line, not including
                    any line-termination characters, or null if the end of the
                    stream has been reached without reading any characters

        Raises
        - IOException: If an I/O error occurs

        See
        - java.nio.file.Files.readAllLines
        """
        ...


    def skip(self, n: int) -> int:
        """

        """
        ...


    def ready(self) -> bool:
        """
        Tells whether this stream is ready to be read.  A buffered character
        stream is ready if the buffer is not empty, or if the underlying
        character stream is ready.

        Raises
        - IOException: If an I/O error occurs
        """
        ...


    def markSupported(self) -> bool:
        """
        Tells whether this stream supports the mark() operation, which it does.
        """
        ...


    def mark(self, readAheadLimit: int) -> None:
        """
        Marks the present position in the stream.  Subsequent calls to reset()
        will attempt to reposition the stream to this point.

        Arguments
        - readAheadLimit: Limit on the number of characters that may be
                                read while still preserving the mark. An attempt
                                to reset the stream after reading characters
                                up to this limit or beyond may fail.
                                A limit value larger than the size of the input
                                buffer will cause a new buffer to be allocated
                                whose size is no smaller than limit.
                                Therefore large values should be used with care.

        Raises
        - IllegalArgumentException: If `readAheadLimit < 0`
        - IOException: If an I/O error occurs
        """
        ...


    def reset(self) -> None:
        """
        Resets the stream to the most recent mark.

        Raises
        - IOException: If the stream has never been marked,
                                 or if the mark has been invalidated
        """
        ...


    def close(self) -> None:
        ...


    def lines(self) -> "Stream"[str]:
        """
        Returns a `Stream`, the elements of which are lines read from
        this `BufferedReader`.  The Stream is lazily populated,
        i.e., read only occurs during the
        <a href="../util/stream/package-summary.html#StreamOps">terminal
        stream operation</a>.
        
         The reader must not be operated on during the execution of the
        terminal stream operation. Otherwise, the result of the terminal stream
        operation is undefined.
        
         After execution of the terminal stream operation there are no
        guarantees that the reader will be at a specific position from which to
        read the next character or line.
        
         If an IOException is thrown when accessing the underlying
        `BufferedReader`, it is wrapped in an UncheckedIOException which will be thrown from the `Stream`
        method that caused the read to take place. This method will return a
        Stream if invoked on a BufferedReader that is closed. Any operation on
        that stream that requires reading from the BufferedReader after it is
        closed, will cause an UncheckedIOException to be thrown.

        Returns
        - a `Stream<String>` providing the lines of text
                described by this `BufferedReader`

        Since
        - 1.8
        """
        ...
