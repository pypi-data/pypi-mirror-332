"""
Python module generated from Java source file java.io.Writer

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.io import *
from java.util import Objects
from typing import Any, Callable, Iterable, Tuple


class Writer(Appendable, Closeable, Flushable):

    @staticmethod
    def nullWriter() -> "Writer":
        """
        Returns a new `Writer` which discards all characters.  The
        returned stream is initially open.  The stream is closed by calling
        the `close()` method.  Subsequent calls to `close()` have
        no effect.
        
         While the stream is open, the `append(char)`, `append(CharSequence)`, `append(CharSequence, int, int)`,
        `flush()`, `write(int)`, `write(char[])`, and
        `write(char[], int, int)` methods do nothing. After the stream
        has been closed, these methods all throw `IOException`.
        
         The .lock object used to synchronize operations on the
        returned `Writer` is not specified.

        Returns
        - a `Writer` which discards all characters

        Since
        - 11
        """
        ...


    def write(self, c: int) -> None:
        """
        Writes a single character.  The character to be written is contained in
        the 16 low-order bits of the given integer value; the 16 high-order bits
        are ignored.
        
         Subclasses that intend to support efficient single-character output
        should override this method.

        Arguments
        - c: int specifying a character to be written

        Raises
        - IOException: If an I/O error occurs
        """
        ...


    def write(self, cbuf: list[str]) -> None:
        """
        Writes an array of characters.

        Arguments
        - cbuf: Array of characters to be written

        Raises
        - IOException: If an I/O error occurs
        """
        ...


    def write(self, cbuf: list[str], off: int, len: int) -> None:
        """
        Writes a portion of an array of characters.

        Arguments
        - cbuf: Array of characters
        - off: Offset from which to start writing characters
        - len: Number of characters to write

        Raises
        - IndexOutOfBoundsException: Implementations should throw this exception
                 if `off` is negative, or `len` is negative,
                 or `off + len` is negative or greater than the length
                 of the given array
        - IOException: If an I/O error occurs
        """
        ...


    def write(self, str: str) -> None:
        """
        Writes a string.

        Arguments
        - str: String to be written

        Raises
        - IOException: If an I/O error occurs
        """
        ...


    def write(self, str: str, off: int, len: int) -> None:
        """
        Writes a portion of a string.

        Arguments
        - str: A String
        - off: Offset from which to start writing characters
        - len: Number of characters to write

        Raises
        - IndexOutOfBoundsException: Implementations should throw this exception
                 if `off` is negative, or `len` is negative,
                 or `off + len` is negative or greater than the length
                 of the given string
        - IOException: If an I/O error occurs

        Unknown Tags
        - The implementation in this class throws an
        `IndexOutOfBoundsException` for the indicated conditions;
        overriding methods may choose to do otherwise.
        """
        ...


    def append(self, csq: "CharSequence") -> "Writer":
        """
        Appends the specified character sequence to this writer.
        
         An invocation of this method of the form `out.append(csq)`
        behaves in exactly the same way as the invocation
        
        ```
            out.write(csq.toString()) ```
        
         Depending on the specification of `toString` for the
        character sequence `csq`, the entire sequence may not be
        appended. For instance, invoking the `toString` method of a
        character buffer will return a subsequence whose content depends upon
        the buffer's position and limit.

        Arguments
        - csq: The character sequence to append.  If `csq` is
                `null`, then the four characters `"null"` are
                appended to this writer.

        Returns
        - This writer

        Raises
        - IOException: If an I/O error occurs

        Since
        - 1.5
        """
        ...


    def append(self, csq: "CharSequence", start: int, end: int) -> "Writer":
        """
        Appends a subsequence of the specified character sequence to this writer.
        `Appendable`.
        
         An invocation of this method of the form
        `out.append(csq, start, end)` when `csq`
        is not `null` behaves in exactly the
        same way as the invocation
        
        ````out.write(csq.subSequence(start, end).toString())````

        Arguments
        - csq: The character sequence from which a subsequence will be
                appended.  If `csq` is `null`, then characters
                will be appended as if `csq` contained the four
                characters `"null"`.
        - start: The index of the first character in the subsequence
        - end: The index of the character following the last character in the
                subsequence

        Returns
        - This writer

        Raises
        - IndexOutOfBoundsException: If `start` or `end` are negative, `start`
                 is greater than `end`, or `end` is greater than
                 `csq.length()`
        - IOException: If an I/O error occurs

        Since
        - 1.5
        """
        ...


    def append(self, c: str) -> "Writer":
        """
        Appends the specified character to this writer.
        
         An invocation of this method of the form `out.append(c)`
        behaves in exactly the same way as the invocation
        
        ```
            out.write(c) ```

        Arguments
        - c: The 16-bit character to append

        Returns
        - This writer

        Raises
        - IOException: If an I/O error occurs

        Since
        - 1.5
        """
        ...


    def flush(self) -> None:
        """
        Flushes the stream.  If the stream has saved any characters from the
        various write() methods in a buffer, write them immediately to their
        intended destination.  Then, if that destination is another character or
        byte stream, flush it.  Thus one flush() invocation will flush all the
        buffers in a chain of Writers and OutputStreams.
        
         If the intended destination of this stream is an abstraction provided
        by the underlying operating system, for example a file, then flushing the
        stream guarantees only that bytes previously written to the stream are
        passed to the operating system for writing; it does not guarantee that
        they are actually written to a physical device such as a disk drive.

        Raises
        - IOException: If an I/O error occurs
        """
        ...


    def close(self) -> None:
        """
        Closes the stream, flushing it first. Once the stream has been closed,
        further write() or flush() invocations will cause an IOException to be
        thrown. Closing a previously closed stream has no effect.

        Raises
        - IOException: If an I/O error occurs
        """
        ...
