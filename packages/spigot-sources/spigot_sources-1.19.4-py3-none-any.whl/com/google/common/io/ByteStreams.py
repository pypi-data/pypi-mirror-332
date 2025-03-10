"""
Python module generated from Java source file com.google.common.io.ByteStreams

Java source file obtained from artifact guava version 31.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.annotations import GwtIncompatible
from com.google.common.io import *
from com.google.common.math import IntMath
from com.google.errorprone.annotations import CanIgnoreReturnValue
from java.io import ByteArrayInputStream
from java.io import ByteArrayOutputStream
from java.io import DataInput
from java.io import DataInputStream
from java.io import DataOutput
from java.io import DataOutputStream
from java.io import EOFException
from java.io import FilterInputStream
from java.io import IOException
from java.io import InputStream
from java.io import OutputStream
from java.util import ArrayDeque
from java.util import Arrays
from java.util import Queue
from javax.annotation import CheckForNull
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class ByteStreams:
    """
    Provides utility methods for working with byte arrays and I/O streams.

    Author(s)
    - Colin Decker

    Since
    - 1.0
    """

    @staticmethod
    def copy(from: "InputStream", to: "OutputStream") -> int:
        """
        Copies all bytes from the input stream to the output stream. Does not close or flush either
        stream.

        Arguments
        - from: the input stream to read from
        - to: the output stream to write to

        Returns
        - the number of bytes copied

        Raises
        - IOException: if an I/O error occurs
        """
        ...


    @staticmethod
    def copy(from: "ReadableByteChannel", to: "WritableByteChannel") -> int:
        """
        Copies all bytes from the readable channel to the writable channel. Does not close or flush
        either channel.

        Arguments
        - from: the readable channel to read from
        - to: the writable channel to write to

        Returns
        - the number of bytes copied

        Raises
        - IOException: if an I/O error occurs
        """
        ...


    @staticmethod
    def toByteArray(in: "InputStream") -> list[int]:
        """
        Reads all bytes from an input stream into a byte array. Does not close the stream.

        Arguments
        - in: the input stream to read from

        Returns
        - a byte array containing all the bytes from the stream

        Raises
        - IOException: if an I/O error occurs
        """
        ...


    @staticmethod
    def exhaust(in: "InputStream") -> int:
        """
        Reads and discards data from the given `InputStream` until the end of the stream is
        reached. Returns the total number of bytes read. Does not close the stream.

        Since
        - 20.0
        """
        ...


    @staticmethod
    def newDataInput(bytes: list[int]) -> "ByteArrayDataInput":
        """
        Returns a new ByteArrayDataInput instance to read from the `bytes` array from the
        beginning.
        """
        ...


    @staticmethod
    def newDataInput(bytes: list[int], start: int) -> "ByteArrayDataInput":
        """
        Returns a new ByteArrayDataInput instance to read from the `bytes` array,
        starting at the given position.

        Raises
        - IndexOutOfBoundsException: if `start` is negative or greater than the length of
            the array
        """
        ...


    @staticmethod
    def newDataInput(byteArrayInputStream: "ByteArrayInputStream") -> "ByteArrayDataInput":
        """
        Returns a new ByteArrayDataInput instance to read from the given `ByteArrayInputStream`. The given input stream is not reset before being read from by the
        returned `ByteArrayDataInput`.

        Since
        - 17.0
        """
        ...


    @staticmethod
    def newDataOutput() -> "ByteArrayDataOutput":
        """
        Returns a new ByteArrayDataOutput instance with a default size.
        """
        ...


    @staticmethod
    def newDataOutput(size: int) -> "ByteArrayDataOutput":
        """
        Returns a new ByteArrayDataOutput instance sized to hold `size` bytes before
        resizing.

        Raises
        - IllegalArgumentException: if `size` is negative
        """
        ...


    @staticmethod
    def newDataOutput(byteArrayOutputStream: "ByteArrayOutputStream") -> "ByteArrayDataOutput":
        """
        Returns a new ByteArrayDataOutput instance which writes to the given `ByteArrayOutputStream`. The given output stream is not reset before being written to by the
        returned `ByteArrayDataOutput` and new data will be appended to any existing content.
        
        Note that if the given output stream was not empty or is modified after the `ByteArrayDataOutput` is created, the contract for ByteArrayDataOutput.toByteArray will
        not be honored (the bytes returned in the byte array may not be exactly what was written via
        calls to `ByteArrayDataOutput`).

        Since
        - 17.0
        """
        ...


    @staticmethod
    def nullOutputStream() -> "OutputStream":
        """
        Returns an OutputStream that simply discards written bytes.

        Since
        - 14.0 (since 1.0 as com.google.common.io.NullOutputStream)
        """
        ...


    @staticmethod
    def limit(in: "InputStream", limit: int) -> "InputStream":
        """
        Wraps a InputStream, limiting the number of bytes which can be read.

        Arguments
        - in: the input stream to be wrapped
        - limit: the maximum number of bytes to be read

        Returns
        - a length-limited InputStream

        Since
        - 14.0 (since 1.0 as com.google.common.io.LimitInputStream)
        """
        ...


    @staticmethod
    def readFully(in: "InputStream", b: list[int]) -> None:
        """
        Attempts to read enough bytes from the stream to fill the given byte array, with the same
        behavior as DataInput.readFully(byte[]). Does not close the stream.

        Arguments
        - in: the input stream to read from.
        - b: the buffer into which the data is read.

        Raises
        - EOFException: if this stream reaches the end before reading all the bytes.
        - IOException: if an I/O error occurs.
        """
        ...


    @staticmethod
    def readFully(in: "InputStream", b: list[int], off: int, len: int) -> None:
        """
        Attempts to read `len` bytes from the stream into the given array starting at `off`, with the same behavior as DataInput.readFully(byte[], int, int). Does not close
        the stream.

        Arguments
        - in: the input stream to read from.
        - b: the buffer into which the data is read.
        - off: an int specifying the offset into the data.
        - len: an int specifying the number of bytes to read.

        Raises
        - EOFException: if this stream reaches the end before reading all the bytes.
        - IOException: if an I/O error occurs.
        """
        ...


    @staticmethod
    def skipFully(in: "InputStream", n: int) -> None:
        """
        Discards `n` bytes of data from the input stream. This method will block until the full
        amount has been skipped. Does not close the stream.

        Arguments
        - in: the input stream to read from
        - n: the number of bytes to skip

        Raises
        - EOFException: if this stream reaches the end before skipping all the bytes
        - IOException: if an I/O error occurs, or the stream does not support skipping
        """
        ...


    @staticmethod
    def readBytes(input: "InputStream", processor: "ByteProcessor"["T"]) -> "T":
        """
        Process the bytes of the given input stream using the given processor.

        Arguments
        - input: the input stream to process
        - processor: the object to which to pass the bytes of the stream

        Returns
        - the result of the byte processor

        Raises
        - IOException: if an I/O error occurs

        Since
        - 14.0
        """
        ...


    @staticmethod
    def read(in: "InputStream", b: list[int], off: int, len: int) -> int:
        """
        Reads some bytes from an input stream and stores them into the buffer array `b`. This
        method blocks until `len` bytes of input data have been read into the array, or end of
        file is detected. The number of bytes read is returned, possibly zero. Does not close the
        stream.
        
        A caller can detect EOF if the number of bytes read is less than `len`. All subsequent
        calls on the same stream will return zero.
        
        If `b` is null, a `NullPointerException` is thrown. If `off` is negative,
        or `len` is negative, or `off+len` is greater than the length of the array `b`, then an `IndexOutOfBoundsException` is thrown. If `len` is zero, then no bytes
        are read. Otherwise, the first byte read is stored into element `b[off]`, the next one
        into `b[off+1]`, and so on. The number of bytes read is, at most, equal to `len`.

        Arguments
        - in: the input stream to read from
        - b: the buffer into which the data is read
        - off: an int specifying the offset into the data
        - len: an int specifying the number of bytes to read

        Returns
        - the number of bytes read

        Raises
        - IOException: if an I/O error occurs
        - IndexOutOfBoundsException: if `off` is negative, if `len` is negative, or if
            `off + len` is greater than `b.length`
        """
        ...
