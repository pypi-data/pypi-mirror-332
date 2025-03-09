"""
Python module generated from Java source file java.nio.file.attribute.BasicFileAttributes

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.nio.file.attribute import *
from typing import Any, Callable, Iterable, Tuple


class BasicFileAttributes:

    def lastModifiedTime(self) -> "FileTime":
        """
        Returns the time of last modification.
        
         If the file system implementation does not support a time stamp
        to indicate the time of last modification then this method returns an
        implementation specific default value, typically a `FileTime`
        representing the epoch (1970-01-01T00:00:00Z).

        Returns
        - a `FileTime` representing the time the file was last
                 modified
        """
        ...


    def lastAccessTime(self) -> "FileTime":
        """
        Returns the time of last access.
        
         If the file system implementation does not support a time stamp
        to indicate the time of last access then this method returns
        an implementation specific default value, typically the .lastModifiedTime() last-modified-time or a `FileTime`
        representing the epoch (1970-01-01T00:00:00Z).

        Returns
        - a `FileTime` representing the time of last access
        """
        ...


    def creationTime(self) -> "FileTime":
        """
        Returns the creation time. The creation time is the time that the file
        was created.
        
         If the file system implementation does not support a time stamp
        to indicate the time when the file was created then this method returns
        an implementation specific default value, typically the .lastModifiedTime() last-modified-time or a `FileTime`
        representing the epoch (1970-01-01T00:00:00Z).

        Returns
        - a `FileTime` representing the time the file was created
        """
        ...


    def isRegularFile(self) -> bool:
        """
        Tells whether the file is a regular file with opaque content.

        Returns
        - `True` if the file is a regular file with opaque content
        """
        ...


    def isDirectory(self) -> bool:
        """
        Tells whether the file is a directory.

        Returns
        - `True` if the file is a directory
        """
        ...


    def isSymbolicLink(self) -> bool:
        """
        Tells whether the file is a symbolic link.

        Returns
        - `True` if the file is a symbolic link
        """
        ...


    def isOther(self) -> bool:
        """
        Tells whether the file is something other than a regular file, directory,
        or symbolic link.

        Returns
        - `True` if the file something other than a regular file,
                directory or symbolic link
        """
        ...


    def size(self) -> int:
        """
        Returns the size of the file (in bytes). The size may differ from the
        actual size on the file system due to compression, support for sparse
        files, or other reasons. The size of files that are not .isRegularFile regular files is implementation specific and
        therefore unspecified.

        Returns
        - the file size, in bytes
        """
        ...


    def fileKey(self) -> "Object":
        """
        Returns an object that uniquely identifies the given file, or `null` if a file key is not available. On some platforms or file systems
        it is possible to use an identifier, or a combination of identifiers to
        uniquely identify a file. Such identifiers are important for operations
        such as file tree traversal in file systems that support <a
        href="../package-summary.html#links">symbolic links</a> or file systems
        that allow a file to be an entry in more than one directory. On UNIX file
        systems, for example, the *device ID* and *inode* are
        commonly used for such purposes.
        
         The file key returned by this method can only be guaranteed to be
        unique if the file system and files remain static. Whether a file system
        re-uses identifiers after a file is deleted is implementation dependent and
        therefore unspecified.
        
         File keys returned by this method can be compared for equality and are
        suitable for use in collections. If the file system and files remain static,
        and two files are the java.nio.file.Files.isSameFile same with
        non-`null` file keys, then their file keys are equal.

        Returns
        - an object that uniquely identifies the given file, or `null`

        See
        - java.nio.file.Files.walkFileTree
        """
        ...
