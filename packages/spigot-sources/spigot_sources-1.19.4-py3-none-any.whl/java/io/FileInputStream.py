"""
Python module generated from Java source file java.io.FileInputStream

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.io import *
from java.util import Arrays
from jdk.internal.util import ArraysSupport
from sun.nio.ch import FileChannelImpl
from typing import Any, Callable, Iterable, Tuple


class FileInputStream(InputStream):
    """
    A `FileInputStream` obtains input bytes
    from a file in a file system. What files
    are  available depends on the host environment.
    
    `FileInputStream` is meant for reading streams of raw bytes
    such as image data. For reading streams of characters, consider using
    `FileReader`.

    Author(s)
    - Arthur van Hoff

    See
    - java.nio.file.Files.newInputStream

    Since
    - 1.0

    Unknown Tags
    - To release resources used by this stream .close should be called
    directly or by try-with-resources. Subclasses are responsible for the cleanup
    of resources acquired by the subclass.
    Subclasses that override .finalize in order to perform cleanup
    should be modified to use alternative cleanup mechanisms such as
    java.lang.ref.Cleaner and remove the overriding `finalize` method.
    - If this FileInputStream has been subclassed and the .close
    method has been overridden, the .close method will be
    called when the FileInputStream is unreachable.
    Otherwise, it is implementation specific how the resource cleanup described in
    .close is performed.
    """

    def __init__(self, name: str):
        """
        Creates a `FileInputStream` by
        opening a connection to an actual file,
        the file named by the path name `name`
        in the file system.  A new `FileDescriptor`
        object is created to represent this file
        connection.
        
        First, if there is a security
        manager, its `checkRead` method
        is called with the `name` argument
        as its argument.
        
        If the named file does not exist, is a directory rather than a regular
        file, or for some other reason cannot be opened for reading then a
        `FileNotFoundException` is thrown.

        Arguments
        - name: the system-dependent file name.

        Raises
        - FileNotFoundException: if the file does not exist,
                    is a directory rather than a regular file,
                    or for some other reason cannot be opened for
                    reading.
        - SecurityException: if a security manager exists and its
                    `checkRead` method denies read access
                    to the file.

        See
        - java.lang.SecurityManager.checkRead(java.lang.String)
        """
        ...


    def __init__(self, file: "File"):
        """
        Creates a `FileInputStream` by
        opening a connection to an actual file,
        the file named by the `File`
        object `file` in the file system.
        A new `FileDescriptor` object
        is created to represent this file connection.
        
        First, if there is a security manager,
        its `checkRead` method  is called
        with the path represented by the `file`
        argument as its argument.
        
        If the named file does not exist, is a directory rather than a regular
        file, or for some other reason cannot be opened for reading then a
        `FileNotFoundException` is thrown.

        Arguments
        - file: the file to be opened for reading.

        Raises
        - FileNotFoundException: if the file does not exist,
                    is a directory rather than a regular file,
                    or for some other reason cannot be opened for
                    reading.
        - SecurityException: if a security manager exists and its
                    `checkRead` method denies read access to the file.

        See
        - java.lang.SecurityManager.checkRead(java.lang.String)
        """
        ...


    def __init__(self, fdObj: "FileDescriptor"):
        """
        Creates a `FileInputStream` by using the file descriptor
        `fdObj`, which represents an existing connection to an
        actual file in the file system.
        
        If there is a security manager, its `checkRead` method is
        called with the file descriptor `fdObj` as its argument to
        see if it's ok to read the file descriptor. If read access is denied
        to the file descriptor a `SecurityException` is thrown.
        
        If `fdObj` is null then a `NullPointerException`
        is thrown.
        
        This constructor does not throw an exception if `fdObj`
        is java.io.FileDescriptor.valid() invalid.
        However, if the methods are invoked on the resulting stream to attempt
        I/O on the stream, an `IOException` is thrown.

        Arguments
        - fdObj: the file descriptor to be opened for reading.

        Raises
        - SecurityException: if a security manager exists and its
                    `checkRead` method denies read access to the
                    file descriptor.

        See
        - SecurityManager.checkRead(java.io.FileDescriptor)
        """
        ...


    def read(self) -> int:
        """
        Reads a byte of data from this input stream. This method blocks
        if no input is yet available.

        Returns
        - the next byte of data, or `-1` if the end of the
                    file is reached.

        Raises
        - IOException: if an I/O error occurs.
        """
        ...


    def read(self, b: list[int]) -> int:
        """
        Reads up to `b.length` bytes of data from this input
        stream into an array of bytes. This method blocks until some input
        is available.

        Arguments
        - b: the buffer into which the data is read.

        Returns
        - the total number of bytes read into the buffer, or
                    `-1` if there is no more data because the end of
                    the file has been reached.

        Raises
        - IOException: if an I/O error occurs.
        """
        ...


    def read(self, b: list[int], off: int, len: int) -> int:
        """
        Reads up to `len` bytes of data from this input stream
        into an array of bytes. If `len` is not zero, the method
        blocks until some input is available; otherwise, no
        bytes are read and `0` is returned.

        Arguments
        - b: the buffer into which the data is read.
        - off: the start offset in the destination array `b`
        - len: the maximum number of bytes read.

        Returns
        - the total number of bytes read into the buffer, or
                    `-1` if there is no more data because the end of
                    the file has been reached.

        Raises
        - NullPointerException: If `b` is `null`.
        - IndexOutOfBoundsException: If `off` is negative,
                    `len` is negative, or `len` is greater than
                    `b.length - off`
        - IOException: if an I/O error occurs.
        """
        ...


    def readAllBytes(self) -> list[int]:
        ...


    def readNBytes(self, len: int) -> list[int]:
        ...


    def skip(self, n: int) -> int:
        """
        Skips over and discards `n` bytes of data from the
        input stream.
        
        The `skip` method may, for a variety of
        reasons, end up skipping over some smaller number of bytes,
        possibly `0`. If `n` is negative, the method
        will try to skip backwards. In case the backing file does not support
        backward skip at its current position, an `IOException` is
        thrown. The actual number of bytes skipped is returned. If it skips
        forwards, it returns a positive value. If it skips backwards, it
        returns a negative value.
        
        This method may skip more bytes than what are remaining in the
        backing file. This produces no exception and the number of bytes skipped
        may include some number of bytes that were beyond the EOF of the
        backing file. Attempting to read from the stream after skipping past
        the end will result in -1 indicating the end of the file.

        Arguments
        - n: the number of bytes to be skipped.

        Returns
        - the actual number of bytes skipped.

        Raises
        - IOException: if n is negative, if the stream does not
                    support seek, or if an I/O error occurs.
        """
        ...


    def available(self) -> int:
        """
        Returns an estimate of the number of remaining bytes that can be read (or
        skipped over) from this input stream without blocking by the next
        invocation of a method for this input stream. Returns 0 when the file
        position is beyond EOF. The next invocation might be the same thread
        or another thread. A single read or skip of this many bytes will not
        block, but may read or skip fewer bytes.
        
         In some cases, a non-blocking read (or skip) may appear to be
        blocked when it is merely slow, for example when reading large
        files over slow networks.

        Returns
        - an estimate of the number of remaining bytes that can be read
                    (or skipped over) from this input stream without blocking.

        Raises
        - IOException: if this file input stream has been closed by calling
                    `close` or an I/O error occurs.
        """
        ...


    def close(self) -> None:
        """
        Closes this file input stream and releases any system resources
        associated with the stream.
        
         If this stream has an associated channel then the channel is closed
        as well.

        Raises
        - IOException: if an I/O error occurs.

        Unknown Tags
        - Overriding .close to perform cleanup actions is reliable
        only when called directly or when called by try-with-resources.
        Do not depend on finalization to invoke `close`;
        finalization is not reliable and is deprecated.
        If cleanup of native resources is needed, other mechanisms such as
        java.lang.ref.Cleaner should be used.
        - 1.4
        """
        ...


    def getFD(self) -> "FileDescriptor":
        """
        Returns the `FileDescriptor`
        object  that represents the connection to
        the actual file in the file system being
        used by this `FileInputStream`.

        Returns
        - the file descriptor object associated with this stream.

        Raises
        - IOException: if an I/O error occurs.

        See
        - java.io.FileDescriptor
        """
        ...


    def getChannel(self) -> "FileChannel":
        """
        Returns the unique java.nio.channels.FileChannel FileChannel
        object associated with this file input stream.
        
         The initial java.nio.channels.FileChannel.position()
        position of the returned channel will be equal to the
        number of bytes read from the file so far.  Reading bytes from this
        stream will increment the channel's position.  Changing the channel's
        position, either explicitly or by reading, will change this stream's
        file position.

        Returns
        - the file channel associated with this file input stream

        Since
        - 1.4
        """
        ...
