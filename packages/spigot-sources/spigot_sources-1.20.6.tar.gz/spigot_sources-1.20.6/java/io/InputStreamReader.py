"""
Python module generated from Java source file java.io.InputStreamReader

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.io import *
from java.nio.charset import Charset
from java.nio.charset import CharsetDecoder
from sun.nio.cs import StreamDecoder
from typing import Any, Callable, Iterable, Tuple


class InputStreamReader(Reader):

    def __init__(self, in: "InputStream"):
        """
        Creates an InputStreamReader that uses the
        Charset.defaultCharset() default charset.

        Arguments
        - in: An InputStream

        See
        - Charset.defaultCharset()
        """
        ...


    def __init__(self, in: "InputStream", charsetName: str):
        """
        Creates an InputStreamReader that uses the named charset.

        Arguments
        - in: An InputStream
        - charsetName: The name of a supported
                java.nio.charset.Charset charset

        Raises
        - UnsupportedEncodingException: If the named charset is not supported
        """
        ...


    def __init__(self, in: "InputStream", cs: "Charset"):
        """
        Creates an InputStreamReader that uses the given charset.

        Arguments
        - in: An InputStream
        - cs: A charset

        Since
        - 1.4
        """
        ...


    def __init__(self, in: "InputStream", dec: "CharsetDecoder"):
        """
        Creates an InputStreamReader that uses the given charset decoder.

        Arguments
        - in: An InputStream
        - dec: A charset decoder

        Since
        - 1.4
        """
        ...


    def getEncoding(self) -> str:
        """
        Returns the name of the character encoding being used by this stream.
        
         If the encoding has an historical name then that name is returned;
        otherwise the encoding's canonical name is returned.
        
         If this instance was created with the .InputStreamReader(InputStream, String) constructor then the returned
        name, being unique for the encoding, may differ from the name passed to
        the constructor. This method will return `null` if the
        stream has been closed.

        Returns
        - The historical name of this encoding, or
                `null` if the stream has been closed

        See
        - java.nio.charset.Charset

        Unknown Tags
        - 1.4
        """
        ...


    def read(self, target: "CharBuffer") -> int:
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
        Raises
        - IndexOutOfBoundsException: 
        """
        ...


    def ready(self) -> bool:
        """
        Tells whether this stream is ready to be read.  An InputStreamReader is
        ready if its input buffer is not empty, or if bytes are available to be
        read from the underlying byte stream.

        Raises
        - IOException: If an I/O error occurs
        """
        ...


    def close(self) -> None:
        ...
