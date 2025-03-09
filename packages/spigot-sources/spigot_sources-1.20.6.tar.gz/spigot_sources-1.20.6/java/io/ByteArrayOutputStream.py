"""
Python module generated from Java source file java.io.ByteArrayOutputStream

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.io import *
from java.nio.charset import Charset
from java.util import Arrays
from java.util import Objects
from jdk.internal.util import ArraysSupport
from typing import Any, Callable, Iterable, Tuple


class ByteArrayOutputStream(OutputStream):

    def __init__(self):
        """
        Creates a new `ByteArrayOutputStream`. The buffer capacity is
        initially 32 bytes, though its size increases if necessary.
        """
        ...


    def __init__(self, size: int):
        """
        Creates a new `ByteArrayOutputStream`, with a buffer capacity of
        the specified size, in bytes.

        Arguments
        - size: the initial size.

        Raises
        - IllegalArgumentException: if size is negative.
        """
        ...


    def write(self, b: int) -> None:
        """
        Writes the specified byte to this `ByteArrayOutputStream`.

        Arguments
        - b: the byte to be written.
        """
        ...


    def write(self, b: list[int], off: int, len: int) -> None:
        """
        Writes `len` bytes from the specified byte array
        starting at offset `off` to this `ByteArrayOutputStream`.

        Arguments
        - b: the data.
        - off: the start offset in the data.
        - len: the number of bytes to write.

        Raises
        - NullPointerException: if `b` is `null`.
        - IndexOutOfBoundsException: if `off` is negative,
        `len` is negative, or `len` is greater than
        `b.length - off`
        """
        ...


    def writeBytes(self, b: list[int]) -> None:
        """
        Writes the complete contents of the specified byte array
        to this `ByteArrayOutputStream`.

        Arguments
        - b: the data.

        Raises
        - NullPointerException: if `b` is `null`.

        Since
        - 11

        Unknown Tags
        - This method is equivalent to .write(byte[],int,int)
        write(b, 0, b.length).
        """
        ...


    def writeTo(self, out: "OutputStream") -> None:
        """
        Writes the complete contents of this `ByteArrayOutputStream` to
        the specified output stream argument, as if by calling the output
        stream's write method using `out.write(buf, 0, count)`.

        Arguments
        - out: the output stream to which to write the data.

        Raises
        - NullPointerException: if `out` is `null`.
        - IOException: if an I/O error occurs.
        """
        ...


    def reset(self) -> None:
        """
        Resets the `count` field of this `ByteArrayOutputStream`
        to zero, so that all currently accumulated output in the
        output stream is discarded. The output stream can be used again,
        reusing the already allocated buffer space.

        See
        - java.io.ByteArrayInputStream.count
        """
        ...


    def toByteArray(self) -> list[int]:
        """
        Creates a newly allocated byte array. Its size is the current
        size of this output stream and the valid contents of the buffer
        have been copied into it.

        Returns
        - the current contents of this output stream, as a byte array.

        See
        - java.io.ByteArrayOutputStream.size()
        """
        ...


    def size(self) -> int:
        """
        Returns the current size of the buffer.

        Returns
        - the value of the `count` field, which is the number
                 of valid bytes in this output stream.

        See
        - java.io.ByteArrayOutputStream.count
        """
        ...


    def toString(self) -> str:
        """
        Converts the buffer's contents into a string decoding bytes using the
        platform's default character set. The length of the new `String`
        is a function of the character set, and hence may not be equal to the
        size of the buffer.
        
         This method always replaces malformed-input and unmappable-character
        sequences with the default replacement string for the platform's
        default character set. The java.nio.charset.CharsetDecoder
        class should be used when more control over the decoding process is
        required.

        Returns
        - String decoded from the buffer's contents.

        Since
        - 1.1
        """
        ...


    def toString(self, charsetName: str) -> str:
        """
        Converts the buffer's contents into a string by decoding the bytes using
        the named java.nio.charset.Charset charset.
        
         This method is equivalent to `.toString(charset)` that takes a
        java.nio.charset.Charset charset.
        
         An invocation of this method of the form
        
        ``` `ByteArrayOutputStream b = ...
             b.toString("UTF-8")`
        ```
        
        behaves in exactly the same way as the expression
        
        ``` `ByteArrayOutputStream b = ...
             b.toString(StandardCharsets.UTF_8)`
        ```

        Arguments
        - charsetName: the name of a supported
                java.nio.charset.Charset charset

        Returns
        - String decoded from the buffer's contents.

        Raises
        - UnsupportedEncodingException: If the named charset is not supported

        Since
        - 1.1
        """
        ...


    def toString(self, charset: "Charset") -> str:
        """
        Converts the buffer's contents into a string by decoding the bytes using
        the specified java.nio.charset.Charset charset. The length of the new
        `String` is a function of the charset, and hence may not be equal
        to the length of the byte array.
        
         This method always replaces malformed-input and unmappable-character
        sequences with the charset's default replacement string. The java.nio.charset.CharsetDecoder class should be used when more control
        over the decoding process is required.

        Arguments
        - charset: the java.nio.charset.Charset charset
                    to be used to decode the `bytes`

        Returns
        - String decoded from the buffer's contents.

        Since
        - 10
        """
        ...


    def toString(self, hibyte: int) -> str:
        """
        Creates a newly allocated string. Its size is the current size of
        the output stream and the valid contents of the buffer have been
        copied into it. Each character *c* in the resulting string is
        constructed from the corresponding element *b* in the byte
        array such that:
        <blockquote>````c == (char)(((hibyte & 0xff) << 8) | (b & 0xff))````</blockquote>

        Arguments
        - hibyte: the high byte of each resulting Unicode character.

        Returns
        - the current contents of the output stream, as a string.

        See
        - java.io.ByteArrayOutputStream.toString()

        Deprecated
        - This method does not properly convert bytes into characters.
        As of JDK&nbsp;1.1, the preferred way to do this is via the
        .toString(String charsetName) or .toString(Charset charset)
        method, which takes an encoding-name or charset argument,
        or the `toString()` method, which uses the platform's default
        character encoding.
        """
        ...


    def close(self) -> None:
        """
        Closing a `ByteArrayOutputStream` has no effect. The methods in
        this class can be called after the stream has been closed without
        generating an `IOException`.
        """
        ...
