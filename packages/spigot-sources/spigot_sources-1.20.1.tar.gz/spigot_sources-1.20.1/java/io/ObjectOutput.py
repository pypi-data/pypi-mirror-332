"""
Python module generated from Java source file java.io.ObjectOutput

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.io import *
from typing import Any, Callable, Iterable, Tuple


class ObjectOutput(DataOutput, AutoCloseable):
    """
    ObjectOutput extends the DataOutput interface to include writing of objects.
    DataOutput includes methods for output of primitive types, ObjectOutput
    extends that interface to include objects, arrays, and Strings.

    See
    - java.io.ObjectInputStream

    Since
    - 1.1
    """

    def writeObject(self, obj: "Object") -> None:
        """
        Write an object to the underlying storage or stream.  The
        class that implements this interface defines how the object is
        written.

        Arguments
        - obj: the object to be written

        Raises
        - IOException: Any of the usual Input/Output related exceptions.
        """
        ...


    def write(self, b: int) -> None:
        """
        Writes a byte. This method will block until the byte is actually
        written.

        Arguments
        - b: the byte

        Raises
        - IOException: If an I/O error has occurred.
        """
        ...


    def write(self, b: list[int]) -> None:
        """
        Writes an array of bytes. This method will block until the bytes
        are actually written.

        Arguments
        - b: the data to be written

        Raises
        - IOException: If an I/O error has occurred.
        """
        ...


    def write(self, b: list[int], off: int, len: int) -> None:
        """
        Writes a sub array of bytes.

        Arguments
        - b: the data to be written
        - off: the start offset in the data
        - len: the number of bytes that are written

        Raises
        - IOException: If an I/O error has occurred.
        """
        ...


    def flush(self) -> None:
        """
        Flushes the stream. This will write any buffered
        output bytes.

        Raises
        - IOException: If an I/O error has occurred.
        """
        ...


    def close(self) -> None:
        """
        Closes the stream. This method must be called
        to release any resources associated with the
        stream.

        Raises
        - IOException: If an I/O error has occurred.
        """
        ...
