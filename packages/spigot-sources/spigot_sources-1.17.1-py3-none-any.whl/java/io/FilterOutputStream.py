"""
Python module generated from Java source file java.io.FilterOutputStream

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.io import *
from typing import Any, Callable, Iterable, Tuple


class FilterOutputStream(OutputStream):
    """
    This class is the superclass of all classes that filter output
    streams. These streams sit on top of an already existing output
    stream (the *underlying* output stream) which it uses as its
    basic sink of data, but possibly transforming the data along the
    way or providing additional functionality.
    
    The class `FilterOutputStream` itself simply overrides
    all methods of `OutputStream` with versions that pass
    all requests to the underlying output stream. Subclasses of
    `FilterOutputStream` may further override some of these
    methods as well as provide additional methods and fields.

    Author(s)
    - Jonathan Payne

    Since
    - 1.0
    """

    def __init__(self, out: "OutputStream"):
        """
        Creates an output stream filter built on top of the specified
        underlying output stream.

        Arguments
        - out: the underlying output stream to be assigned to
                       the field `this.out` for later use, or
                       `null` if this instance is to be
                       created without an underlying stream.
        """
        ...


    def write(self, b: int) -> None:
        """
        Writes the specified `byte` to this output stream.
        
        The `write` method of `FilterOutputStream`
        calls the `write` method of its underlying output stream,
        that is, it performs `out.write(b)`.
        
        Implements the abstract `write` method of `OutputStream`.

        Arguments
        - b: the `byte`.

        Raises
        - IOException: if an I/O error occurs.
        """
        ...


    def write(self, b: list[int]) -> None:
        """
        Writes `b.length` bytes to this output stream.
        
        The `write` method of `FilterOutputStream`
        calls its `write` method of three arguments with the
        arguments `b`, `0`, and
        `b.length`.
        
        Note that this method does not call the one-argument
        `write` method of its underlying output stream with
        the single argument `b`.

        Arguments
        - b: the data to be written.

        Raises
        - IOException: if an I/O error occurs.

        See
        - java.io.FilterOutputStream.write(byte[], int, int)
        """
        ...


    def write(self, b: list[int], off: int, len: int) -> None:
        """
        Writes `len` bytes from the specified
        `byte` array starting at offset `off` to
        this output stream.
        
        The `write` method of `FilterOutputStream`
        calls the `write` method of one argument on each
        `byte` to output.
        
        Note that this method does not call the `write` method
        of its underlying output stream with the same arguments. Subclasses
        of `FilterOutputStream` should provide a more efficient
        implementation of this method.

        Arguments
        - b: the data.
        - off: the start offset in the data.
        - len: the number of bytes to write.

        Raises
        - IOException: if an I/O error occurs.

        See
        - java.io.FilterOutputStream.write(int)
        """
        ...


    def flush(self) -> None:
        """
        Flushes this output stream and forces any buffered output bytes
        to be written out to the stream.
        
        The `flush` method of `FilterOutputStream`
        calls the `flush` method of its underlying output stream.

        Raises
        - IOException: if an I/O error occurs.

        See
        - java.io.FilterOutputStream.out
        """
        ...


    def close(self) -> None:
        """
        Closes this output stream and releases any system resources
        associated with the stream.
        
        When not already closed, the `close` method of `FilterOutputStream` calls its `flush` method, and then
        calls the `close` method of its underlying output stream.

        Raises
        - IOException: if an I/O error occurs.

        See
        - java.io.FilterOutputStream.out
        """
        ...
