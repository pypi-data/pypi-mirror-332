"""
Python module generated from Java source file com.google.common.io.MoreFiles

Java source file obtained from artifact guava version 32.1.2-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtIncompatible
from com.google.common.annotations import J2ktIncompatible
from com.google.common.base import Optional
from com.google.common.base import Predicate
from com.google.common.collect import ImmutableList
from com.google.common.graph import Traverser
from com.google.common.io import *
from com.google.j2objc.annotations import J2ObjCIncompatible
from java.io import IOException
from java.io import InputStream
from java.io import OutputStream
from java.nio.charset import Charset
from java.nio.file import DirectoryIteratorException
from java.nio.file import DirectoryStream
from java.nio.file import FileAlreadyExistsException
from java.nio.file import FileSystemException
from java.nio.file import Files
from java.nio.file import LinkOption
from java.nio.file import NoSuchFileException
from java.nio.file import NotDirectoryException
from java.nio.file import OpenOption
from java.nio.file import Path
from java.nio.file import SecureDirectoryStream
from java.nio.file import StandardOpenOption
from java.nio.file.attribute import BasicFileAttributeView
from java.nio.file.attribute import BasicFileAttributes
from java.nio.file.attribute import FileAttribute
from java.nio.file.attribute import FileTime
from java.util import Arrays
from java.util.stream import Stream
from javax.annotation import CheckForNull
from typing import Any, Callable, Iterable, Tuple


class MoreFiles:
    """
    Static utilities for use with Path instances, intended to complement Files.
    
    Many methods provided by Guava's `Files` class for java.io.File instances are
    now available via the JDK's java.nio.file.Files class for `Path` - check the JDK's
    class if a sibling method from `Files` appears to be missing from this class.

    Author(s)
    - Colin Decker

    Since
    - 21.0
    """

    @staticmethod
    def asByteSource(path: "Path", *options: Tuple["OpenOption", ...]) -> "ByteSource":
        """
        Returns a view of the given `path` as a ByteSource.
        
        Any OpenOption open options provided are used when opening streams to the file
        and may affect the behavior of the returned source and the streams it provides. See StandardOpenOption for the standard options that may be provided. Providing no options is
        equivalent to providing the StandardOpenOption.READ READ option.
        """
        ...


    @staticmethod
    def asByteSink(path: "Path", *options: Tuple["OpenOption", ...]) -> "ByteSink":
        """
        Returns a view of the given `path` as a ByteSink.
        
        Any OpenOption open options provided are used when opening streams to the file
        and may affect the behavior of the returned sink and the streams it provides. See StandardOpenOption for the standard options that may be provided. Providing no options is
        equivalent to providing the StandardOpenOption.CREATE CREATE, StandardOpenOption.TRUNCATE_EXISTING TRUNCATE_EXISTING and StandardOpenOption.WRITE
        WRITE options.
        """
        ...


    @staticmethod
    def asCharSource(path: "Path", charset: "Charset", *options: Tuple["OpenOption", ...]) -> "CharSource":
        """
        Returns a view of the given `path` as a CharSource using the given `charset`.
        
        Any OpenOption open options provided are used when opening streams to the file
        and may affect the behavior of the returned source and the streams it provides. See StandardOpenOption for the standard options that may be provided. Providing no options is
        equivalent to providing the StandardOpenOption.READ READ option.
        """
        ...


    @staticmethod
    def asCharSink(path: "Path", charset: "Charset", *options: Tuple["OpenOption", ...]) -> "CharSink":
        """
        Returns a view of the given `path` as a CharSink using the given `charset`.
        
        Any OpenOption open options provided are used when opening streams to the file
        and may affect the behavior of the returned sink and the streams it provides. See StandardOpenOption for the standard options that may be provided. Providing no options is
        equivalent to providing the StandardOpenOption.CREATE CREATE, StandardOpenOption.TRUNCATE_EXISTING TRUNCATE_EXISTING and StandardOpenOption.WRITE
        WRITE options.
        """
        ...


    @staticmethod
    def listFiles(dir: "Path") -> "ImmutableList"["Path"]:
        """
        Returns an immutable list of paths to the files contained in the given directory.

        Raises
        - NoSuchFileException: if the file does not exist *(optional specific exception)*
        - NotDirectoryException: if the file could not be opened because it is not a directory
            *(optional specific exception)*
        - IOException: if an I/O error occurs
        """
        ...


    @staticmethod
    def fileTraverser() -> "Traverser"["Path"]:
        """
        Returns a Traverser instance for the file and directory tree. The returned traverser
        starts from a Path and will return all files and directories it encounters.
        
        The returned traverser attempts to avoid following symbolic links to directories. However,
        the traverser cannot guarantee that it will not follow symbolic links to directories as it is
        possible for a directory to be replaced with a symbolic link between checking if the file is a
        directory and actually reading the contents of that directory.
        
        If the Path passed to one of the traversal methods does not exist or is not a
        directory, no exception will be thrown and the returned Iterable will contain a single
        element: that path.
        
        DirectoryIteratorException may be thrown when iterating Iterable instances
        created by this traverser if an IOException is thrown by a call to .listFiles(Path).
        
        Example: `MoreFiles.fileTraverser().depthFirstPreOrder(Paths.get("/"))` may return the
        following paths: `["/", "/etc", "/etc/config.txt", "/etc/fonts", "/home", "/home/alice",
        ...]`

        Since
        - 23.5
        """
        ...


    @staticmethod
    def isDirectory(*options: Tuple["LinkOption", ...]) -> "Predicate"["Path"]:
        """
        Returns a predicate that returns the result of java.nio.file.Files.isDirectory(Path,
        LinkOption...) on input paths with the given link options.
        """
        ...


    @staticmethod
    def isRegularFile(*options: Tuple["LinkOption", ...]) -> "Predicate"["Path"]:
        """
        Returns a predicate that returns the result of java.nio.file.Files.isRegularFile(Path,
        LinkOption...) on input paths with the given link options.
        """
        ...


    @staticmethod
    def equal(path1: "Path", path2: "Path") -> bool:
        """
        Returns True if the files located by the given paths exist, are not directories, and contain
        the same bytes.

        Raises
        - IOException: if an I/O error occurs

        Since
        - 22.0
        """
        ...


    @staticmethod
    def touch(path: "Path") -> None:
        """
        Like the unix command of the same name, creates an empty file or updates the last modified
        timestamp of the existing file at the given path to the current system time.
        """
        ...


    @staticmethod
    def createParentDirectories(path: "Path", *attrs: Tuple["FileAttribute"[Any], ...]) -> None:
        """
        Creates any necessary but nonexistent parent directories of the specified path. Note that if
        this operation fails, it may have succeeded in creating some (but not all) of the necessary
        parent directories. The parent directory is created with the given `attrs`.

        Raises
        - IOException: if an I/O error occurs, or if any necessary but nonexistent parent
            directories of the specified file could not be created.
        """
        ...


    @staticmethod
    def getFileExtension(path: "Path") -> str:
        """
        Returns the <a href="http://en.wikipedia.org/wiki/Filename_extension">file extension</a> for
        the file at the given path, or the empty string if the file has no extension. The result does
        not include the '`.`'.
        
        **Note:** This method simply returns everything after the last '`.`' in the file's
        name as determined by Path.getFileName. It does not account for any filesystem-specific
        behavior that the Path API does not already account for. For example, on NTFS it will
        report `"txt"` as the extension for the filename `"foo.exe:.txt"` even though NTFS
        will drop the `":.txt"` part of the name when the file is actually created on the
        filesystem due to NTFS's <a href="https://goo.gl/vTpJi4">Alternate Data Streams</a>.
        """
        ...


    @staticmethod
    def getNameWithoutExtension(path: "Path") -> str:
        """
        Returns the file name without its <a
        href="http://en.wikipedia.org/wiki/Filename_extension">file extension</a> or path. This is
        similar to the `basename` unix command. The result does not include the '`.`'.
        """
        ...


    @staticmethod
    def deleteRecursively(path: "Path", *options: Tuple["RecursiveDeleteOption", ...]) -> None:
        """
        Deletes the file or directory at the given `path` recursively. Deletes symbolic links,
        not their targets (subject to the caveat below).
        
        If an I/O exception occurs attempting to read, open or delete any file under the given
        directory, this method skips that file and continues. All such exceptions are collected and,
        after attempting to delete all files, an `IOException` is thrown containing those
        exceptions as Throwable.getSuppressed() suppressed exceptions.
        
        <h2>Warning: Security of recursive deletes</h2>
        
        On a file system that supports symbolic links and does *not* support SecureDirectoryStream, it is possible for a recursive delete to delete files and directories
        that are *outside* the directory being deleted. This can happen if, after checking that a
        file is a directory (and not a symbolic link), that directory is replaced by a symbolic link to
        an outside directory before the call that opens the directory to read its entries.
        
        By default, this method throws InsecureRecursiveDeleteException if it can't
        guarantee the security of recursive deletes. If you wish to allow the recursive deletes anyway,
        pass RecursiveDeleteOption.ALLOW_INSECURE to this method to override that behavior.

        Raises
        - NoSuchFileException: if `path` does not exist *(optional specific exception)*
        - InsecureRecursiveDeleteException: if the security of recursive deletes can't be
            guaranteed for the file system and RecursiveDeleteOption.ALLOW_INSECURE was not
            specified
        - IOException: if `path` or any file in the subtree rooted at it can't be deleted
            for any reason
        """
        ...


    @staticmethod
    def deleteDirectoryContents(path: "Path", *options: Tuple["RecursiveDeleteOption", ...]) -> None:
        """
        Deletes all files within the directory at the given `path` .deleteRecursively
        recursively. Does not delete the directory itself. Deletes symbolic links, not their targets
        (subject to the caveat below). If `path` itself is a symbolic link to a directory, that
        link is followed and the contents of the directory it targets are deleted.
        
        If an I/O exception occurs attempting to read, open or delete any file under the given
        directory, this method skips that file and continues. All such exceptions are collected and,
        after attempting to delete all files, an `IOException` is thrown containing those
        exceptions as Throwable.getSuppressed() suppressed exceptions.
        
        <h2>Warning: Security of recursive deletes</h2>
        
        On a file system that supports symbolic links and does *not* support SecureDirectoryStream, it is possible for a recursive delete to delete files and directories
        that are *outside* the directory being deleted. This can happen if, after checking that a
        file is a directory (and not a symbolic link), that directory is replaced by a symbolic link to
        an outside directory before the call that opens the directory to read its entries.
        
        By default, this method throws InsecureRecursiveDeleteException if it can't
        guarantee the security of recursive deletes. If you wish to allow the recursive deletes anyway,
        pass RecursiveDeleteOption.ALLOW_INSECURE to this method to override that behavior.

        Raises
        - NoSuchFileException: if `path` does not exist *(optional specific exception)*
        - NotDirectoryException: if the file at `path` is not a directory *(optional
            specific exception)*
        - InsecureRecursiveDeleteException: if the security of recursive deletes can't be
            guaranteed for the file system and RecursiveDeleteOption.ALLOW_INSECURE was not
            specified
        - IOException: if one or more files can't be deleted for any reason
        """
        ...
