"""
Python module generated from Java source file java.io.StringReader

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.io import *
from java.util import Objects
from typing import Any, Callable, Iterable, Tuple


class StringReader(Reader):

    def __init__(self, s: str):
        """
        Creates a new string reader.

        Arguments
        - s: String providing the character stream.
        """
        ...


    def read(self) -> int:
        """
        Reads a single character.

        Returns
        - The character read, or -1 if the end of the stream has been
                    reached

        Raises
        - IOException: If an I/O error occurs
        """
        ...


    def read(self, cbuf: list[str], off: int, len: int) -> int:
        """
        Reads characters into a portion of an array.
        
         If `len` is zero, then no characters are read and `0` is
        returned; otherwise, there is an attempt to read at least one character.
        If no character is available because the stream is at its end, the value
        `-1` is returned; otherwise, at least one character is read and
        stored into `cbuf`.

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


    def skip(self, n: int) -> int:
        """
        Skips characters. If the stream is already at its end before this method
        is invoked, then no characters are skipped and zero is returned.
        
        The `n` parameter may be negative, even though the
        `skip` method of the Reader superclass throws
        an exception in this case. Negative values of `n` cause the
        stream to skip backwards. Negative return values indicate a skip
        backwards. It is not possible to skip backwards past the beginning of
        the string.
        
        If the entire string has been read or skipped, then this method has
        no effect and always returns `0`.

        Arguments
        - n: 

        Returns
        - 

        Raises
        - IOException: 
        """
        ...


    def ready(self) -> bool:
        """
        Tells whether this stream is ready to be read.

        Returns
        - True if the next read() is guaranteed not to block for input

        Raises
        - IOException: If the stream is closed
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
        will reposition the stream to this point.

        Arguments
        - readAheadLimit: Limit on the number of characters that may be
                                read while still preserving the mark.  Because
                                the stream's input comes from a string, there
                                is no actual limit, so this argument must not
                                be negative, but is otherwise ignored.

        Raises
        - IllegalArgumentException: If `readAheadLimit < 0`
        - IOException: If an I/O error occurs
        """
        ...


    def reset(self) -> None:
        """
        Resets the stream to the most recent mark, or to the beginning of the
        string if it has never been marked.

        Raises
        - IOException: If an I/O error occurs
        """
        ...


    def close(self) -> None:
        """
        Closes the stream and releases any system resources associated with
        it. Once the stream has been closed, further read(),
        ready(), mark(), or reset() invocations will throw an IOException.
        Closing a previously closed stream has no effect. This method will block
        while there is another thread blocking on the reader.
        """
        ...
