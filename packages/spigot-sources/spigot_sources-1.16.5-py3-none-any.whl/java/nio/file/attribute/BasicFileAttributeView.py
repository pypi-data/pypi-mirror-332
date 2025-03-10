"""
Python module generated from Java source file java.nio.file.attribute.BasicFileAttributeView

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.io import IOException
from java.nio.file.attribute import *
from typing import Any, Callable, Iterable, Tuple


class BasicFileAttributeView(FileAttributeView):

    def name(self) -> str:
        """
        Returns the name of the attribute view. Attribute views of this type
        have the name `"basic"`.
        """
        ...


    def readAttributes(self) -> "BasicFileAttributes":
        """
        Reads the basic file attributes as a bulk operation.
        
         It is implementation specific if all file attributes are read as an
        atomic operation with respect to other file system operations.

        Returns
        - the file attributes

        Raises
        - IOException: if an I/O error occurs
        - SecurityException: In the case of the default provider, a security manager is
                 installed, its SecurityManager.checkRead(String) checkRead
                 method is invoked to check read access to the file
        """
        ...


    def setTimes(self, lastModifiedTime: "FileTime", lastAccessTime: "FileTime", createTime: "FileTime") -> None:
        """
        Updates any or all of the file's last modified time, last access time,
        and create time attributes.
        
         This method updates the file's timestamp attributes. The values are
        converted to the epoch and precision supported by the file system.
        Converting from finer to coarser granularities result in precision loss.
        The behavior of this method when attempting to set a timestamp that is
        not supported or to a value that is outside the range supported by the
        underlying file store is not defined. It may or not fail by throwing an
        `IOException`.
        
         If any of the `lastModifiedTime`, `lastAccessTime`,
        or `createTime` parameters has the value `null` then the
        corresponding timestamp is not changed. An implementation may require to
        read the existing values of the file attributes when only some, but not
        all, of the timestamp attributes are updated. Consequently, this method
        may not be an atomic operation with respect to other file system
        operations. Reading and re-writing existing values may also result in
        precision loss. If all of the `lastModifiedTime`, `lastAccessTime` and `createTime` parameters are `null` then
        this method has no effect.
        
         **Usage Example:**
        Suppose we want to change a file's last access time.
        ```
           Path path = ...
           FileTime time = ...
           Files.getFileAttributeView(path, BasicFileAttributeView.class).setTimes(null, time, null);
        ```

        Arguments
        - lastModifiedTime: the new last modified time, or `null` to not change the
                 value
        - lastAccessTime: the last access time, or `null` to not change the value
        - createTime: the file's create time, or `null` to not change the value

        Raises
        - IOException: if an I/O error occurs
        - SecurityException: In the case of the default provider, a security manager is
                 installed, its  SecurityManager.checkWrite(String) checkWrite
                 method is invoked to check write access to the file

        See
        - java.nio.file.Files.setLastModifiedTime
        """
        ...
