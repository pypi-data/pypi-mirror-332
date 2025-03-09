"""
Python module generated from Java source file java.nio.file.attribute.PosixFilePermissions

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.nio.file.attribute import *
from java.util import *
from typing import Any, Callable, Iterable, Tuple


class PosixFilePermissions:

    @staticmethod
    def toString(perms: set["PosixFilePermission"]) -> str:
        """
        Returns the `String` representation of a set of permissions. It
        is guaranteed that the returned `String` can be parsed by the
        .fromString method.
        
         If the set contains `null` or elements that are not of type
        `PosixFilePermission` then these elements are ignored.

        Arguments
        - perms: the set of permissions

        Returns
        - the string representation of the permission set
        """
        ...


    @staticmethod
    def fromString(perms: str) -> set["PosixFilePermission"]:
        """
        Returns the set of permissions corresponding to a given `String`
        representation.
        
         The `perms` parameter is a `String` representing the
        permissions. It has 9 characters that are interpreted as three sets of
        three. The first set refers to the owner's permissions; the next to the
        group permissions and the last to others. Within each set, the first
        character is `'r'` to indicate permission to read, the second
        character is `'w'` to indicate permission to write, and the third
        character is `'x'` for execute permission. Where a permission is
        not set then the corresponding character is set to `'-'`.
        
         **Usage Example:**
        Suppose we require the set of permissions that indicate the owner has read,
        write, and execute permissions, the group has read and execute permissions
        and others have none.
        ```
          Set&lt;PosixFilePermission&gt; perms = PosixFilePermissions.fromString("rwxr-x---");
        ```

        Arguments
        - perms: string representing a set of permissions

        Returns
        - the resulting set of permissions

        Raises
        - IllegalArgumentException: if the string cannot be converted to a set of permissions

        See
        - .toString(Set)
        """
        ...


    @staticmethod
    def asFileAttribute(perms: set["PosixFilePermission"]) -> "FileAttribute"[set["PosixFilePermission"]]:
        """
        Creates a FileAttribute, encapsulating a copy of the given file
        permissions, suitable for passing to the java.nio.file.Files.createFile
        createFile or java.nio.file.Files.createDirectory createDirectory
        methods.

        Arguments
        - perms: the set of permissions

        Returns
        - an attribute encapsulating the given file permissions with
                 FileAttribute.name name `"posix:permissions"`

        Raises
        - ClassCastException: if the set contains elements that are not of type `PosixFilePermission`
        """
        ...
