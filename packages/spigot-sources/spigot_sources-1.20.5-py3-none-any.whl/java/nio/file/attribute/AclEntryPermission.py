"""
Python module generated from Java source file java.nio.file.attribute.AclEntryPermission

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from java.nio.file.attribute import *
from typing import Any, Callable, Iterable, Tuple


class AclEntryPermission(Enum):

# Static fields
    LIST_DIRECTORY = READ_DATA
    """
    Permission to list the entries of a directory (equal to .READ_DATA)
    """
    ADD_FILE = WRITE_DATA
    """
    Permission to add a new file to a directory (equal to .WRITE_DATA)
    """
    ADD_SUBDIRECTORY = APPEND_DATA
    """
    Permission to create a subdirectory to a directory (equal to .APPEND_DATA)
    """


    READ_DATA = 0
    """
    Permission to read the data of the file.
    """
    WRITE_DATA = 1
    """
    Permission to modify the file's data.
    """
    APPEND_DATA = 2
    """
    Permission to append data to a file.
    """
    READ_NAMED_ATTRS = 3
    """
    Permission to read the named attributes of a file.
    
     <a href="http://www.ietf.org/rfc/rfc3530.txt">RFC&nbsp;3530: Network
    File System (NFS) version 4 Protocol</a> defines *named attributes*
    as opaque files associated with a file in the file system.
    """
    WRITE_NAMED_ATTRS = 4
    """
    Permission to write the named attributes of a file.
    
     <a href="http://www.ietf.org/rfc/rfc3530.txt">RFC&nbsp;3530: Network
    File System (NFS) version 4 Protocol</a> defines *named attributes*
    as opaque files associated with a file in the file system.
    """
    EXECUTE = 5
    """
    Permission to execute a file.
    """
    DELETE_CHILD = 6
    """
    Permission to delete a file or directory within a directory.
    """
    READ_ATTRIBUTES = 7
    """
    The ability to read (non-acl) file attributes.
    """
    WRITE_ATTRIBUTES = 8
    """
    The ability to write (non-acl) file attributes.
    """
    DELETE = 9
    """
    Permission to delete the file.
    """
    READ_ACL = 10
    """
    Permission to read the ACL attribute.
    """
    WRITE_ACL = 11
    """
    Permission to write the ACL attribute.
    """
    WRITE_OWNER = 12
    """
    Permission to change the owner.
    """
    SYNCHRONIZE = 13
    """
    Permission to access file locally at the server with synchronous reads
    and writes.
    """
