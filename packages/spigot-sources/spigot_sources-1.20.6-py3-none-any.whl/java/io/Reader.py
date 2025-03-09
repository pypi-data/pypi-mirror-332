"""
Python module generated from Java source file java.io.Reader

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.io import *
from java.util import Objects
from typing import Any, Callable, Iterable, Tuple


class Reader(Readable, Closeable):

    @staticmethod
    def nullReader() -> "Reader":
        """
        Returns a new `Reader` that reads no characters. The returned
        stream is initially open.  The stream is closed by calling the
        `close()` method.  Subsequent calls to `close()` have no
        effect.
        
         While the stream is open, the `read()`, `read(char[])`,
        `read(char[], int, int)`, `read(CharBuffer)`, `ready()`, `skip(long)`, and `transferTo()` methods all
        behave as if end of stream has been reached. After the stream has been
        closed, these methods all throw `IOException`.
        
         The `markSupported()` method returns `False`.  The
        `mark()` and `reset()` methods throw an `IOException`.
        
         The .lock object used to synchronize operations on the
        returned `Reader` is not specified.

        Returns
        - a `Reader` which reads no characters

        Since
        - 11
        """
        ...


    def read(self, target: "CharBuffer") -> int:
        """
        Attempts to read characters into the specified character buffer.
        The buffer is used as a repository of characters as-is: the only
        changes made are the results of a put operation. No flipping or
        rewinding of the buffer is performed.

        Arguments
        - target: the buffer to read characters into

        Returns
        - The number of characters added to the buffer, or
                -1 if this source of characters is at its end

        Raises
        - IOException: if an I/O error occurs
        - NullPointerException: if target is null
        - java.nio.ReadOnlyBufferException: if target is a read only buffer

        Since
        - 1.5
        """
        ...


    def read(self) -> int:
        """
        Reads a single character.  This method will block until a character is
        available, an I/O error occurs, or the end of the stream is reached.
        
         Subclasses that intend to support efficient single-character input
        should override this method.

        Returns
        - The character read, as an integer in the range 0 to 65535
                    (`0x00-0xffff`), or -1 if the end of the stream has
                    been reached

        Raises
        - IOException: If an I/O error occurs
        """
        ...


    def read(self, cbuf: list[str]) -> int:
        """
        Reads characters into an array.  This method will block until some input
        is available, an I/O error occurs, or the end of the stream is reached.
        
         If the length of `cbuf` is zero, then no characters are read
        and `0` is returned; otherwise, there is an attempt to read at
        least one character.  If no character is available because the stream is
        at its end, the value `-1` is returned; otherwise, at least one
        character is read and stored into `cbuf`.

        Arguments
        - cbuf: Destination buffer

        Returns
        - The number of characters read, or -1
                     if the end of the stream
                     has been reached

        Raises
        - IOException: If an I/O error occurs
        """
        ...


    def read(self, cbuf: list[str], off: int, len: int) -> int:
        """
        Reads characters into a portion of an array.  This method will block
        until some input is available, an I/O error occurs, or the end of the
        stream is reached.
        
         If `len` is zero, then no characters are read and `0` is
        returned; otherwise, there is an attempt to read at least one character.
        If no character is available because the stream is at its end, the value
        `-1` is returned; otherwise, at least one character is read and
        stored into `cbuf`.

        Arguments
        - cbuf: Destination buffer
        - off: Offset at which to start storing characters
        - len: Maximum number of characters to read

        Returns
        - The number of characters read, or -1 if the end of the
                    stream has been reached

        Raises
        - IndexOutOfBoundsException: If `off` is negative, or `len` is negative,
                    or `len` is greater than `cbuf.length - off`
        - IOException: If an I/O error occurs
        """
        ...


    def skip(self, n: int) -> int:
        """
        Skips characters.  This method will block until some characters are
        available, an I/O error occurs, or the end of the stream is reached.
        If the stream is already at its end before this method is invoked,
        then no characters are skipped and zero is returned.

        Arguments
        - n: The number of characters to skip

        Returns
        - The number of characters actually skipped

        Raises
        - IllegalArgumentException: If `n` is negative.
        - IOException: If an I/O error occurs
        """
        ...


    def ready(self) -> bool:
        """
        Tells whether this stream is ready to be read.

        Returns
        - True if the next read() is guaranteed not to block for input,
        False otherwise.  Note that returning False does not guarantee that the
        next read will block.

        Raises
        - IOException: If an I/O error occurs
        """
        ...


    def markSupported(self) -> bool:
        """
        Tells whether this stream supports the mark() operation. The default
        implementation always returns False. Subclasses should override this
        method.

        Returns
        - True if and only if this stream supports the mark operation.
        """
        ...


    def mark(self, readAheadLimit: int) -> None:
        """
        Marks the present position in the stream.  Subsequent calls to reset()
        will attempt to reposition the stream to this point.  Not all
        character-input streams support the mark() operation.

        Arguments
        - readAheadLimit: Limit on the number of characters that may be
                                read while still preserving the mark.  After
                                reading this many characters, attempting to
                                reset the stream may fail.

        Raises
        - IOException: If the stream does not support mark(),
                                 or if some other I/O error occurs
        """
        ...


    def reset(self) -> None:
        """
        Resets the stream.  If the stream has been marked, then attempt to
        reposition it at the mark.  If the stream has not been marked, then
        attempt to reset it in some way appropriate to the particular stream,
        for example by repositioning it to its starting point.  Not all
        character-input streams support the reset() operation, and some support
        reset() without supporting mark().

        Raises
        - IOException: If the stream has not been marked,
                                 or if the mark has been invalidated,
                                 or if the stream does not support reset(),
                                 or if some other I/O error occurs
        """
        ...


    def close(self) -> None:
        """
        Closes the stream and releases any system resources associated with
        it.  Once the stream has been closed, further read(), ready(),
        mark(), reset(), or skip() invocations will throw an IOException.
        Closing a previously closed stream has no effect.

        Raises
        - IOException: If an I/O error occurs
        """
        ...


    def transferTo(self, out: "Writer") -> int:
        """
        Reads all characters from this reader and writes the characters to the
        given writer in the order that they are read. On return, this reader
        will be at end of the stream. This method does not close either reader
        or writer.
        
        This method may block indefinitely reading from the reader, or
        writing to the writer. The behavior for the case where the reader
        and/or writer is *asynchronously closed*, or the thread
        interrupted during the transfer, is highly reader and writer
        specific, and therefore not specified.
        
        If an I/O error occurs reading from the reader or writing to the
        writer, then it may do so after some characters have been read or
        written. Consequently the reader may not be at end of the stream and
        one, or both, streams may be in an inconsistent state. It is strongly
        recommended that both streams be promptly closed if an I/O error occurs.

        Arguments
        - out: the writer, non-null

        Returns
        - the number of characters transferred

        Raises
        - IOException: if an I/O error occurs when reading or writing
        - NullPointerException: if `out` is `null`

        Since
        - 10
        """
        ...
