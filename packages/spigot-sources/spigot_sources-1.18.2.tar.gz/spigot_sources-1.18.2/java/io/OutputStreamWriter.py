"""
Python module generated from Java source file java.io.OutputStreamWriter

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.io import *
from java.nio.charset import Charset
from java.nio.charset import CharsetEncoder
from sun.nio.cs import StreamEncoder
from typing import Any, Callable, Iterable, Tuple


class OutputStreamWriter(Writer):

    def __init__(self, out: "OutputStream", charsetName: str):
        """
        Creates an OutputStreamWriter that uses the named charset.

        Arguments
        - out: An OutputStream
        - charsetName: The name of a supported
                java.nio.charset.Charset charset

        Raises
        - UnsupportedEncodingException: If the named encoding is not supported
        """
        ...


    def __init__(self, out: "OutputStream"):
        """
        Creates an OutputStreamWriter that uses the default character encoding.

        Arguments
        - out: An OutputStream
        """
        ...


    def __init__(self, out: "OutputStream", cs: "Charset"):
        """
        Creates an OutputStreamWriter that uses the given charset.

        Arguments
        - out: An OutputStream
        - cs: A charset

        Since
        - 1.4
        """
        ...


    def __init__(self, out: "OutputStream", enc: "CharsetEncoder"):
        """
        Creates an OutputStreamWriter that uses the given charset encoder.

        Arguments
        - out: An OutputStream
        - enc: A charset encoder

        Since
        - 1.4
        """
        ...


    def getEncoding(self) -> str:
        """
        Returns the name of the character encoding being used by this stream.
        
         If the encoding has an historical name then that name is returned;
        otherwise the encoding's canonical name is returned.
        
         If this instance was created with the .OutputStreamWriter(OutputStream, String) constructor then the returned
        name, being unique for the encoding, may differ from the name passed to
        the constructor.  This method may return `null` if the stream has
        been closed. 

        Returns
        - The historical name of this encoding, or possibly
                `null` if the stream has been closed

        See
        - java.nio.charset.Charset

        Unknown Tags
        - 1.4
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

        Arguments
        - cbuf: Buffer of characters
        - off: Offset from which to start writing characters
        - len: Number of characters to write

        Raises
        - IndexOutOfBoundsException: If `off` is negative, or `len` is negative,
                 or `off + len` is negative or greater than the length
                 of the given array
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
        - IndexOutOfBoundsException: If `off` is negative, or `len` is negative,
                 or `off + len` is negative or greater than the length
                 of the given string
        - IOException: If an I/O error occurs
        """
        ...


    def append(self, csq: "CharSequence", start: int, end: int) -> "Writer":
        ...


    def append(self, csq: "CharSequence") -> "Writer":
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
