"""
Python module generated from Java source file java.nio.file.SecureDirectoryStream

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.io import IOException
from java.nio.file import *
from java.nio.file.attribute import *
from typing import Any, Callable, Iterable, Tuple


class SecureDirectoryStream(DirectoryStream):

    def newDirectoryStream(self, path: "T", *options: Tuple["LinkOption", ...]) -> "SecureDirectoryStream"["T"]:
        """
        Opens the directory identified by the given path, returning a `SecureDirectoryStream` to iterate over the entries in the directory.
        
         This method works in exactly the manner specified by the Files.newDirectoryStream(Path) newDirectoryStream method for the case that
        the `path` parameter is an Path.isAbsolute absolute path.
        When the parameter is a relative path then the directory to open is
        relative to this open directory. The LinkOption.NOFOLLOW_LINKS NOFOLLOW_LINKS option may be used to
        ensure that this method fails if the file is a symbolic link.
        
         The new directory stream, once created, is not dependent upon the
        directory stream used to create it. Closing this directory stream has no
        effect upon newly created directory stream.

        Arguments
        - path: the path to the directory to open
        - options: options indicating how symbolic links are handled

        Returns
        - a new and open `SecureDirectoryStream` object

        Raises
        - ClosedDirectoryStreamException: if the directory stream is closed
        - NotDirectoryException: if the file could not otherwise be opened because it is not
                 a directory *(optional specific exception)*
        - IOException: if an I/O error occurs
        - SecurityException: In the case of the default provider, and a security manager is
                 installed, the SecurityManager.checkRead(String) checkRead
                 method is invoked to check read access to the directory.
        """
        ...


    def newByteChannel(self, path: "T", options: set["OpenOption"], *attrs: Tuple["FileAttribute"[Any], ...]) -> "SeekableByteChannel":
        """
        Opens or creates a file in this directory, returning a seekable byte
        channel to access the file.
        
         This method works in exactly the manner specified by the Files.newByteChannel Files.newByteChannel method for the
        case that the `path` parameter is an Path.isAbsolute absolute
        path. When the parameter is a relative path then the file to open or
        create is relative to this open directory. In addition to the options
        defined by the `Files.newByteChannel` method, the LinkOption.NOFOLLOW_LINKS NOFOLLOW_LINKS option may be used to
        ensure that this method fails if the file is a symbolic link.
        
         The channel, once created, is not dependent upon the directory stream
        used to create it. Closing this directory stream has no effect upon the
        channel.

        Arguments
        - path: the path of the file to open or create
        - options: options specifying how the file is opened
        - attrs: an optional list of attributes to set atomically when creating
                 the file

        Returns
        - the seekable byte channel

        Raises
        - ClosedDirectoryStreamException: if the directory stream is closed
        - IllegalArgumentException: if the set contains an invalid combination of options
        - UnsupportedOperationException: if an unsupported open option is specified or the array contains
                 attributes that cannot be set atomically when creating the file
        - FileAlreadyExistsException: if a file of that name already exists and the StandardOpenOption.CREATE_NEW CREATE_NEW option is specified
                 *(optional specific exception)*
        - IOException: if an I/O error occurs
        - SecurityException: In the case of the default provider, and a security manager is
                 installed, the SecurityManager.checkRead(String) checkRead
                 method is invoked to check read access to the path if the file
                 is opened for reading. The SecurityManager.checkWrite(String)
                 checkWrite method is invoked to check write access to the path
                 if the file is opened for writing.
        """
        ...


    def deleteFile(self, path: "T") -> None:
        """
        Deletes a file.
        
         Unlike the Files.delete delete() method, this method does
        not first examine the file to determine if the file is a directory.
        Whether a directory is deleted by this method is system dependent and
        therefore not specified. If the file is a symbolic link, then the link
        itself, not the final target of the link, is deleted. When the
        parameter is a relative path then the file to delete is relative to
        this open directory.

        Arguments
        - path: the path of the file to delete

        Raises
        - ClosedDirectoryStreamException: if the directory stream is closed
        - NoSuchFileException: if the file does not exist *(optional specific exception)*
        - IOException: if an I/O error occurs
        - SecurityException: In the case of the default provider, and a security manager is
                 installed, the SecurityManager.checkDelete(String) checkDelete
                 method is invoked to check delete access to the file
        """
        ...


    def deleteDirectory(self, path: "T") -> None:
        """
        Deletes a directory.
        
         Unlike the Files.delete delete() method, this method
        does not first examine the file to determine if the file is a directory.
        Whether non-directories are deleted by this method is system dependent and
        therefore not specified. When the parameter is a relative path then the
        directory to delete is relative to this open directory.

        Arguments
        - path: the path of the directory to delete

        Raises
        - ClosedDirectoryStreamException: if the directory stream is closed
        - NoSuchFileException: if the directory does not exist *(optional specific exception)*
        - DirectoryNotEmptyException: if the directory could not otherwise be deleted because it is
                 not empty *(optional specific exception)*
        - IOException: if an I/O error occurs
        - SecurityException: In the case of the default provider, and a security manager is
                 installed, the SecurityManager.checkDelete(String) checkDelete
                 method is invoked to check delete access to the directory
        """
        ...


    def move(self, srcpath: "T", targetdir: "SecureDirectoryStream"["T"], targetpath: "T") -> None:
        """
        Move a file from this directory to another directory.
        
         This method works in a similar manner to Files.move move
        method when the StandardCopyOption.ATOMIC_MOVE ATOMIC_MOVE option
        is specified. That is, this method moves a file as an atomic file system
        operation. If the `srcpath` parameter is an Path.isAbsolute
        absolute path then it locates the source file. If the parameter is a
        relative path then it is located relative to this open directory. If
        the `targetpath` parameter is absolute then it locates the target
        file (the `targetdir` parameter is ignored). If the parameter is
        a relative path it is located relative to the open directory identified
        by the `targetdir` parameter. In all cases, if the target file
        exists then it is implementation specific if it is replaced or this
        method fails.

        Arguments
        - srcpath: the name of the file to move
        - targetdir: the destination directory
        - targetpath: the name to give the file in the destination directory

        Raises
        - ClosedDirectoryStreamException: if this or the target directory stream is closed
        - FileAlreadyExistsException: if the file already exists in the target directory and cannot
                 be replaced *(optional specific exception)*
        - AtomicMoveNotSupportedException: if the file cannot be moved as an atomic file system operation
        - IOException: if an I/O error occurs
        - SecurityException: In the case of the default provider, and a security manager is
                 installed, the SecurityManager.checkWrite(String) checkWrite
                 method is invoked to check write access to both the source and
                 target file.
        """
        ...


    def getFileAttributeView(self, type: type["V"]) -> "V":
        """
        Returns a new file attribute view to access the file attributes of this
        directory.
        
         The resulting file attribute view can be used to read or update the
        attributes of this (open) directory. The `type` parameter specifies
        the type of the attribute view and the method returns an instance of that
        type if supported. Invoking this method to obtain a BasicFileAttributeView always returns an instance of that class that is
        bound to this open directory.
        
         The state of resulting file attribute view is intimately connected
        to this directory stream. Once the directory stream is .close closed,
        then all methods to read or update attributes will throw ClosedDirectoryStreamException ClosedDirectoryStreamException.
        
        Type `<V>`: The `FileAttributeView` type

        Arguments
        - type: the `Class` object corresponding to the file attribute view

        Returns
        - a new file attribute view of the specified type bound to
                 this directory stream, or `null` if the attribute view
                 type is not available
        """
        ...


    def getFileAttributeView(self, path: "T", type: type["V"], *options: Tuple["LinkOption", ...]) -> "V":
        """
        Returns a new file attribute view to access the file attributes of a file
        in this directory.
        
         The resulting file attribute view can be used to read or update the
        attributes of file in this directory. The `type` parameter specifies
        the type of the attribute view and the method returns an instance of that
        type if supported. Invoking this method to obtain a BasicFileAttributeView always returns an instance of that class that is
        bound to the file in the directory.
        
         The state of resulting file attribute view is intimately connected
        to this directory stream. Once the directory stream .close closed,
        then all methods to read or update attributes will throw ClosedDirectoryStreamException ClosedDirectoryStreamException. The
        file is not required to exist at the time that the file attribute view
        is created but methods to read or update attributes of the file will
        fail when invoked and the file does not exist.
        
        Type `<V>`: The `FileAttributeView` type

        Arguments
        - path: the path of the file
        - type: the `Class` object corresponding to the file attribute view
        - options: options indicating how symbolic links are handled

        Returns
        - a new file attribute view of the specified type bound to a
                 this directory stream, or `null` if the attribute view
                 type is not available
        """
        ...
