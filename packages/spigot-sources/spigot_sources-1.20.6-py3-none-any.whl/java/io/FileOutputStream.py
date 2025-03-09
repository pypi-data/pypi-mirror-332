"""
Python module generated from Java source file java.io.FileOutputStream

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.io import *
from jdk.internal.access import JavaIOFileDescriptorAccess
from jdk.internal.access import SharedSecrets
from sun.nio.ch import FileChannelImpl
from typing import Any, Callable, Iterable, Tuple


class FileOutputStream(OutputStream):
    """
    A file output stream is an output stream for writing data to a
    `File` or to a `FileDescriptor`. Whether or not
    a file is available or may be created depends upon the underlying
    platform.  Some platforms, in particular, allow a file to be opened
    for writing by only one `FileOutputStream` (or other
    file-writing object) at a time.  In such situations the constructors in
    this class will fail if the file involved is already open.
    
    `FileOutputStream` is meant for writing streams of raw bytes
    such as image data. For writing streams of characters, consider using
    `FileWriter`.

    Author(s)
    - Arthur van Hoff

    See
    - java.nio.file.Files.newOutputStream

    Since
    - 1.0

    Unknown Tags
    - To release resources used by this stream .close should be called
    directly or by try-with-resources. Subclasses are responsible for the cleanup
    of resources acquired by the subclass.
    Subclasses that override .finalize in order to perform cleanup
    should be modified to use alternative cleanup mechanisms such as
    java.lang.ref.Cleaner and remove the overriding `finalize` method.
    - If this FileOutputStream has been subclassed and the .close
    method has been overridden, the .close method will be
    called when the FileInputStream is unreachable.
    Otherwise, it is implementation specific how the resource cleanup described in
    .close is performed.
    """

    def __init__(self, name: str):
        """
        Creates a file output stream to write to the file with the
        specified name. A new `FileDescriptor` object is
        created to represent this file connection.
        
        First, if there is a security manager, its `checkWrite`
        method is called with `name` as its argument.
        
        If the file exists but is a directory rather than a regular file, does
        not exist but cannot be created, or cannot be opened for any other
        reason then a `FileNotFoundException` is thrown.

        Arguments
        - name: the system-dependent filename

        Raises
        - FileNotFoundException: if the file exists but is a directory
                          rather than a regular file, does not exist but cannot
                          be created, or cannot be opened for any other reason
        - SecurityException: if a security manager exists and its
                      `checkWrite` method denies write access
                      to the file.

        See
        - java.lang.SecurityManager.checkWrite(java.lang.String)

        Unknown Tags
        - Invoking this constructor with the parameter `name` is
        equivalent to invoking .FileOutputStream(String,boolean)
        new FileOutputStream(name, False).
        """
        ...


    def __init__(self, name: str, append: bool):
        """
        Creates a file output stream to write to the file with the specified
        name.  If the second argument is `True`, then
        bytes will be written to the end of the file rather than the beginning.
        A new `FileDescriptor` object is created to represent this
        file connection.
        
        First, if there is a security manager, its `checkWrite`
        method is called with `name` as its argument.
        
        If the file exists but is a directory rather than a regular file, does
        not exist but cannot be created, or cannot be opened for any other
        reason then a `FileNotFoundException` is thrown.

        Arguments
        - name: the system-dependent file name
        - append: if `True`, then bytes will be written
                          to the end of the file rather than the beginning

        Raises
        - FileNotFoundException: if the file exists but is a directory
                          rather than a regular file, does not exist but cannot
                          be created, or cannot be opened for any other reason.
        - SecurityException: if a security manager exists and its
                      `checkWrite` method denies write access
                      to the file.

        See
        - java.lang.SecurityManager.checkWrite(java.lang.String)

        Since
        - 1.1
        """
        ...


    def __init__(self, file: "File"):
        """
        Creates a file output stream to write to the file represented by
        the specified `File` object. A new
        `FileDescriptor` object is created to represent this
        file connection.
        
        First, if there is a security manager, its `checkWrite`
        method is called with the path represented by the `file`
        argument as its argument.
        
        If the file exists but is a directory rather than a regular file, does
        not exist but cannot be created, or cannot be opened for any other
        reason then a `FileNotFoundException` is thrown.

        Arguments
        - file: the file to be opened for writing.

        Raises
        - FileNotFoundException: if the file exists but is a directory
                          rather than a regular file, does not exist but cannot
                          be created, or cannot be opened for any other reason
        - SecurityException: if a security manager exists and its
                      `checkWrite` method denies write access
                      to the file.

        See
        - java.lang.SecurityManager.checkWrite(java.lang.String)
        """
        ...


    def __init__(self, file: "File", append: bool):
        """
        Creates a file output stream to write to the file represented by
        the specified `File` object. If the second argument is
        `True`, then bytes will be written to the end of the file
        rather than the beginning. A new `FileDescriptor` object is
        created to represent this file connection.
        
        First, if there is a security manager, its `checkWrite`
        method is called with the path represented by the `file`
        argument as its argument.
        
        If the file exists but is a directory rather than a regular file, does
        not exist but cannot be created, or cannot be opened for any other
        reason then a `FileNotFoundException` is thrown.

        Arguments
        - file: the file to be opened for writing.
        - append: if `True`, then bytes will be written
                          to the end of the file rather than the beginning

        Raises
        - FileNotFoundException: if the file exists but is a directory
                          rather than a regular file, does not exist but cannot
                          be created, or cannot be opened for any other reason
        - SecurityException: if a security manager exists and its
                      `checkWrite` method denies write access
                      to the file.

        See
        - java.lang.SecurityManager.checkWrite(java.lang.String)

        Since
        - 1.4
        """
        ...


    def __init__(self, fdObj: "FileDescriptor"):
        """
        Creates a file output stream to write to the specified file
        descriptor, which represents an existing connection to an actual
        file in the file system.
        
        First, if there is a security manager, its `checkWrite`
        method is called with the file descriptor `fdObj`
        argument as its argument.
        
        If `fdObj` is null then a `NullPointerException`
        is thrown.
        
        This constructor does not throw an exception if `fdObj`
        is java.io.FileDescriptor.valid() invalid.
        However, if the methods are invoked on the resulting stream to attempt
        I/O on the stream, an `IOException` is thrown.

        Arguments
        - fdObj: the file descriptor to be opened for writing

        Raises
        - SecurityException: if a security manager exists and its
                      `checkWrite` method denies
                      write access to the file descriptor

        See
        - java.lang.SecurityManager.checkWrite(java.io.FileDescriptor)
        """
        ...


    def write(self, b: int) -> None:
        """
        Writes the specified byte to this file output stream. Implements
        the `write` method of `OutputStream`.

        Arguments
        - b: the byte to be written.

        Raises
        - IOException: if an I/O error occurs.
        """
        ...


    def write(self, b: list[int]) -> None:
        """
        Writes `b.length` bytes from the specified byte array
        to this file output stream.

        Arguments
        - b: the data.

        Raises
        - IOException: if an I/O error occurs.
        """
        ...


    def write(self, b: list[int], off: int, len: int) -> None:
        """
        Writes `len` bytes from the specified byte array
        starting at offset `off` to this file output stream.

        Arguments
        - b: the data.
        - off: the start offset in the data.
        - len: the number of bytes to write.

        Raises
        - IOException: if an I/O error occurs.
        """
        ...


    def close(self) -> None:
        """
        Closes this file output stream and releases any system resources
        associated with this stream. This file output stream may no longer
        be used for writing bytes.
        
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
        Returns the file descriptor associated with this stream.

        Returns
        - the `FileDescriptor` object that represents
                 the connection to the file in the file system being used
                 by this `FileOutputStream` object.

        Raises
        - IOException: if an I/O error occurs.

        See
        - java.io.FileDescriptor
        """
        ...


    def getChannel(self) -> "FileChannel":
        """
        Returns the unique java.nio.channels.FileChannel FileChannel
        object associated with this file output stream.
        
         The initial java.nio.channels.FileChannel.position()
        position of the returned channel will be equal to the
        number of bytes written to the file so far unless this stream is in
        append mode, in which case it will be equal to the size of the file.
        Writing bytes to this stream will increment the channel's position
        accordingly.  Changing the channel's position, either explicitly or by
        writing, will change this stream's file position.

        Returns
        - the file channel associated with this file output stream

        Since
        - 1.4
        """
        ...
