"""
Python module generated from Java source file java.io.StringWriter

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.io import *
from typing import Any, Callable, Iterable, Tuple


class StringWriter(Writer):

    def __init__(self):
        """
        Create a new string writer using the default initial string-buffer
        size.
        """
        ...


    def __init__(self, initialSize: int):
        """
        Create a new string writer using the specified initial string-buffer
        size.

        Arguments
        - initialSize: The number of `char` values that will fit into this buffer
               before it is automatically expanded

        Raises
        - IllegalArgumentException: If `initialSize` is negative
        """
        ...


    def write(self, c: int) -> None:
        """
        Write a single character.
        """
        ...


    def write(self, cbuf: list[str], off: int, len: int) -> None:
        """
        Write a portion of an array of characters.

        Arguments
        - cbuf: Array of characters
        - off: Offset from which to start writing characters
        - len: Number of characters to write

        Raises
        - IndexOutOfBoundsException: If `off` is negative, or `len` is negative,
                 or `off + len` is negative or greater than the length
                 of the given array
        """
        ...


    def write(self, str: str) -> None:
        """
        Write a string.
        """
        ...


    def write(self, str: str, off: int, len: int) -> None:
        """
        Write a portion of a string.

        Arguments
        - str: String to be written
        - off: Offset from which to start writing characters
        - len: Number of characters to write

        Raises
        - IndexOutOfBoundsException: If `off` is negative, or `len` is negative,
                 or `off + len` is negative or greater than the length
                 of the given string
        """
        ...


    def append(self, csq: "CharSequence") -> "StringWriter":
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

        Since
        - 1.5
        """
        ...


    def append(self, csq: "CharSequence", start: int, end: int) -> "StringWriter":
        """
        Appends a subsequence of the specified character sequence to this writer.
        
         An invocation of this method of the form
        `out.append(csq, start, end)` when `csq`
        is not `null`, behaves in
        exactly the same way as the invocation
        
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

        Since
        - 1.5
        """
        ...


    def append(self, c: str) -> "StringWriter":
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

        Since
        - 1.5
        """
        ...


    def toString(self) -> str:
        """
        Return the buffer's current value as a string.
        """
        ...


    def getBuffer(self) -> "StringBuffer":
        """
        Return the string buffer itself.

        Returns
        - StringBuffer holding the current buffer value.
        """
        ...


    def flush(self) -> None:
        """
        Flush the stream.
        
         The `flush` method of `StringWriter` does nothing.
        """
        ...


    def close(self) -> None:
        """
        Closing a `StringWriter` has no effect. The methods in this
        class can be called after the stream has been closed without generating
        an `IOException`.
        """
        ...
