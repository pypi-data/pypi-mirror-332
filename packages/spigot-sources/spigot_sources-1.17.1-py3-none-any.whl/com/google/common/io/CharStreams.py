"""
Python module generated from Java source file com.google.common.io.CharStreams

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.annotations import GwtIncompatible
from com.google.common.io import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from java.io import Closeable
from java.io import EOFException
from java.io import IOException
from java.io import Reader
from java.io import Writer
from typing import Any, Callable, Iterable, Tuple


class CharStreams:
    """
    Provides utility methods for working with character streams.
    
    All method parameters must be non-null unless documented otherwise.
    
    Some of the methods in this class take arguments with a generic type of
    `Readable & Closeable`. A java.io.Reader implements both of those interfaces.
    Similarly for `Appendable & Closeable` and java.io.Writer.

    Author(s)
    - Colin Decker

    Since
    - 1.0
    """

    @staticmethod
    def copy(from: "Readable", to: "Appendable") -> int:
        """
        Copies all characters between the Readable and Appendable objects. Does not
        close or flush either object.

        Arguments
        - from: the object to read from
        - to: the object to write to

        Returns
        - the number of characters copied

        Raises
        - IOException: if an I/O error occurs
        """
        ...


    @staticmethod
    def toString(r: "Readable") -> str:
        """
        Reads all characters from a Readable object into a String. Does not close the
        `Readable`.

        Arguments
        - r: the object to read from

        Returns
        - a string containing all the characters

        Raises
        - IOException: if an I/O error occurs
        """
        ...


    @staticmethod
    def readLines(r: "Readable") -> list[str]:
        """
        Reads all of the lines from a Readable object. The lines do not include
        line-termination characters, but do include other leading and trailing whitespace.
        
        Does not close the `Readable`. If reading files or resources you should use the
        Files.readLines and Resources.readLines methods.

        Arguments
        - r: the object to read from

        Returns
        - a mutable List containing all the lines

        Raises
        - IOException: if an I/O error occurs
        """
        ...


    @staticmethod
    def readLines(readable: "Readable", processor: "LineProcessor"["T"]) -> "T":
        """
        Streams lines from a Readable object, stopping when the processor returns `False`
        or all lines have been read and returning the result produced by the processor. Does not close
        `readable`. Note that this method may not fully consume the contents of `readable`
        if the processor stops processing early.

        Raises
        - IOException: if an I/O error occurs

        Since
        - 14.0
        """
        ...


    @staticmethod
    def exhaust(readable: "Readable") -> int:
        """
        Reads and discards data from the given `Readable` until the end of the stream is
        reached. Returns the total number of chars read. Does not close the stream.

        Since
        - 20.0
        """
        ...


    @staticmethod
    def skipFully(reader: "Reader", n: int) -> None:
        """
        Discards `n` characters of data from the reader. This method will block until the full
        amount has been skipped. Does not close the reader.

        Arguments
        - reader: the reader to read from
        - n: the number of characters to skip

        Raises
        - EOFException: if this stream reaches the end before skipping all the characters
        - IOException: if an I/O error occurs
        """
        ...


    @staticmethod
    def nullWriter() -> "Writer":
        """
        Returns a Writer that simply discards written chars.

        Since
        - 15.0
        """
        ...


    @staticmethod
    def asWriter(target: "Appendable") -> "Writer":
        """
        Returns a Writer that sends all output to the given Appendable target. Closing the
        writer will close the target if it is Closeable, and flushing the writer will flush the
        target if it is java.io.Flushable.

        Arguments
        - target: the object to which output will be sent

        Returns
        - a new Writer object, unless target is a Writer, in which case the target is returned
        """
        ...
