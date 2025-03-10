"""
Python module generated from Java source file com.google.common.io.CharSink

Java source file obtained from artifact guava version 31.0.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.annotations import GwtIncompatible
from com.google.common.io import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from java.io import BufferedWriter
from java.io import IOException
from java.io import Reader
from java.io import Writer
from java.nio.charset import Charset
from java.util import Iterator
from java.util.stream import Stream
from typing import Any, Callable, Iterable, Tuple


class CharSink:
    """
    A destination to which characters can be written, such as a text file. Unlike a Writer, a
    `CharSink` is not an open, stateful stream that can be written to and closed. Instead, it
    is an immutable *supplier* of `Writer` instances.
    
    `CharSink` provides two kinds of methods:
    
    
      - **Methods that return a writer:** These methods should return a *new*, independent
          instance each time they are called. The caller is responsible for ensuring that the
          returned writer is closed.
      - **Convenience methods:** These are implementations of common operations that are
          typically implemented by opening a writer using one of the methods in the first category,
          doing something and finally closing the writer that was opened.
    
    
    Any ByteSink may be viewed as a `CharSink` with a specific Charset
    character encoding using ByteSink.asCharSink(Charset). Characters written to the
    resulting `CharSink` will written to the `ByteSink` as encoded bytes.

    Author(s)
    - Colin Decker

    Since
    - 14.0
    """

    def openStream(self) -> "Writer":
        """
        Opens a new Writer for writing to this sink. This method returns a new, independent
        writer each time it is called.
        
        The caller is responsible for ensuring that the returned writer is closed.

        Raises
        - IOException: if an I/O error occurs while opening the writer
        """
        ...


    def openBufferedStream(self) -> "Writer":
        """
        Opens a new buffered Writer for writing to this sink. The returned stream is not
        required to be a BufferedWriter in order to allow implementations to simply delegate to
        .openStream() when the stream returned by that method does not benefit from additional
        buffering. This method returns a new, independent writer each time it is called.
        
        The caller is responsible for ensuring that the returned writer is closed.

        Raises
        - IOException: if an I/O error occurs while opening the writer

        Since
        - 15.0 (in 14.0 with return type BufferedWriter)
        """
        ...


    def write(self, charSequence: "CharSequence") -> None:
        """
        Writes the given character sequence to this sink.

        Raises
        - IOException: if an I/O error while writing to this sink
        """
        ...


    def writeLines(self, lines: Iterable["CharSequence"]) -> None:
        """
        Writes the given lines of text to this sink with each line (including the last) terminated with
        the operating system's default line separator. This method is equivalent to `writeLines(lines, System.getProperty("line.separator"))`.

        Raises
        - IOException: if an I/O error occurs while writing to this sink
        """
        ...


    def writeLines(self, lines: Iterable["CharSequence"], lineSeparator: str) -> None:
        """
        Writes the given lines of text to this sink with each line (including the last) terminated with
        the given line separator.

        Raises
        - IOException: if an I/O error occurs while writing to this sink
        """
        ...


    def writeLines(self, lines: "Stream"["CharSequence"]) -> None:
        """
        Writes the given lines of text to this sink with each line (including the last) terminated with
        the operating system's default line separator. This method is equivalent to `writeLines(lines, System.getProperty("line.separator"))`.

        Raises
        - IOException: if an I/O error occurs while writing to this sink

        Since
        - 22.0
        """
        ...


    def writeLines(self, lines: "Stream"["CharSequence"], lineSeparator: str) -> None:
        """
        Writes the given lines of text to this sink with each line (including the last) terminated with
        the given line separator.

        Raises
        - IOException: if an I/O error occurs while writing to this sink

        Since
        - 22.0
        """
        ...


    def writeFrom(self, readable: "Readable") -> int:
        """
        Writes all the text from the given Readable (such as a Reader) to this sink.
        Does not close `readable` if it is `Closeable`.

        Returns
        - the number of characters written

        Raises
        - IOException: if an I/O error occurs while reading from `readable` or writing to
            this sink
        """
        ...
