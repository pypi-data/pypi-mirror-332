"""
Python module generated from Java source file com.google.common.io.ByteSink

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtIncompatible
from com.google.common.io import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from java.io import BufferedOutputStream
from java.io import IOException
from java.io import InputStream
from java.io import OutputStream
from java.io import OutputStreamWriter
from java.io import Writer
from java.nio.charset import Charset
from typing import Any, Callable, Iterable, Tuple


class ByteSink:
    """
    A destination to which bytes can be written, such as a file. Unlike an OutputStream, a
    `ByteSink` is not an open, stateful stream that can be written to and closed. Instead, it
    is an immutable *supplier* of `OutputStream` instances.
    
    `ByteSink` provides two kinds of methods:
    
    - **Methods that return a stream:** These methods should return a *new*, independent
        instance each time they are called. The caller is responsible for ensuring that the returned
        stream is closed.
    - **Convenience methods:** These are implementations of common operations that are typically
        implemented by opening a stream using one of the methods in the first category, doing
        something and finally closing the stream or channel that was opened.

    Author(s)
    - Colin Decker

    Since
    - 14.0
    """

    def asCharSink(self, charset: "Charset") -> "CharSink":
        """
        Returns a CharSink view of this `ByteSink` that writes characters to this sink as
        bytes encoded with the given Charset charset.
        """
        ...


    def openStream(self) -> "OutputStream":
        """
        Opens a new OutputStream for writing to this sink. This method should return a new,
        independent stream each time it is called.
        
        The caller is responsible for ensuring that the returned stream is closed.

        Raises
        - IOException: if an I/O error occurs in the process of opening the stream
        """
        ...


    def openBufferedStream(self) -> "OutputStream":
        """
        Opens a new buffered OutputStream for writing to this sink. The returned stream is not
        required to be a BufferedOutputStream in order to allow implementations to simply
        delegate to .openStream() when the stream returned by that method does not benefit from
        additional buffering (for example, a `ByteArrayOutputStream`). This method should return
        a new, independent stream each time it is called.
        
        The caller is responsible for ensuring that the returned stream is closed.

        Raises
        - IOException: if an I/O error occurs in the process of opening the stream

        Since
        - 15.0 (in 14.0 with return type BufferedOutputStream)
        """
        ...


    def write(self, bytes: list[int]) -> None:
        """
        Writes all the given bytes to this sink.

        Raises
        - IOException: if an I/O occurs in the process of writing to this sink
        """
        ...


    def writeFrom(self, input: "InputStream") -> int:
        """
        Writes all the bytes from the given `InputStream` to this sink. Does not close
        `input`.

        Returns
        - the number of bytes written

        Raises
        - IOException: if an I/O occurs in the process of reading from `input` or writing to
            this sink
        """
        ...
