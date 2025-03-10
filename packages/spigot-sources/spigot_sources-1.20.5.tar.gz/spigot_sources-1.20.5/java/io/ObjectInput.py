"""
Python module generated from Java source file java.io.ObjectInput

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.io import *
from typing import Any, Callable, Iterable, Tuple


class ObjectInput(DataInput, AutoCloseable):
    """
    ObjectInput extends the DataInput interface to include the reading of
    objects. DataInput includes methods for the input of primitive types,
    ObjectInput extends that interface to include objects, arrays, and Strings.

    See
    - java.io.ObjectInputStream

    Since
    - 1.1
    """

    def readObject(self) -> "Object":
        """
        Read and return an object. The class that implements this interface
        defines where the object is "read" from.

        Returns
        - the object read from the stream

        Raises
        - java.lang.ClassNotFoundException: If the class of a serialized
                   object cannot be found.
        - IOException: If any of the usual Input/Output
                   related exceptions occur.
        """
        ...


    def read(self) -> int:
        """
        Reads a byte of data. This method will block if no input is
        available.

        Returns
        - the byte read, or -1 if the end of the
                 stream is reached.

        Raises
        - IOException: If an I/O error has occurred.
        """
        ...


    def read(self, b: list[int]) -> int:
        """
        Reads into an array of bytes.  This method will
        block until some input is available.

        Arguments
        - b: the buffer into which the data is read

        Returns
        - the actual number of bytes read, -1 is
                 returned when the end of the stream is reached.

        Raises
        - IOException: If an I/O error has occurred.
        """
        ...


    def read(self, b: list[int], off: int, len: int) -> int:
        """
        Reads into an array of bytes.  This method will
        block until some input is available.

        Arguments
        - b: the buffer into which the data is read
        - off: the start offset of the data
        - len: the maximum number of bytes read

        Returns
        - the actual number of bytes read, -1 is
                 returned when the end of the stream is reached.

        Raises
        - IOException: If an I/O error has occurred.
        """
        ...


    def skip(self, n: int) -> int:
        """
        Skips n bytes of input.

        Arguments
        - n: the number of bytes to be skipped

        Returns
        - the actual number of bytes skipped.

        Raises
        - IOException: If an I/O error has occurred.
        """
        ...


    def available(self) -> int:
        """
        Returns the number of bytes that can be read
        without blocking.

        Returns
        - the number of available bytes.

        Raises
        - IOException: If an I/O error has occurred.
        """
        ...


    def close(self) -> None:
        """
        Closes the input stream. Must be called
        to release any resources associated with
        the stream.

        Raises
        - IOException: If an I/O error has occurred.
        """
        ...
