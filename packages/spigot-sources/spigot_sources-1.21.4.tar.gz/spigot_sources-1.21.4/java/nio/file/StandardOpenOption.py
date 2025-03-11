"""
Python module generated from Java source file java.nio.file.StandardOpenOption

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from java.nio.file import *
from typing import Any, Callable, Iterable, Tuple


class StandardOpenOption(Enum):

    READ = 0
    """
    Open for read access.
    """
    WRITE = 1
    """
    Open for write access.
    """
    APPEND = 2
    """
    If the file is opened for .WRITE access then bytes will be written
    to the end of the file rather than the beginning.
    
     If the file is opened for write access by other programs, then it
    is file system specific if writing to the end of the file is atomic.
    """
    TRUNCATE_EXISTING = 3
    """
    If the file already exists and it is opened for .WRITE
    access, then its length is truncated to 0. This option is ignored
    if the file is opened only for .READ access.
    """
    CREATE = 4
    """
    Create a new file if it does not exist.
    This option is ignored if the .CREATE_NEW option is also set.
    The check for the existence of the file and the creation of the file
    if it does not exist is atomic with respect to other file system
    operations.
    """
    CREATE_NEW = 5
    """
    Create a new file, failing if the file already exists.
    The check for the existence of the file and the creation of the file
    if it does not exist is atomic with respect to other file system
    operations.
    """
    DELETE_ON_CLOSE = 6
    """
    Delete on close. When this option is present then the implementation
    makes a *best effort* attempt to delete the file when closed
    by the appropriate `close` method. If the `close` method is
    not invoked then a *best effort* attempt is made to delete the
    file when the Java virtual machine terminates (either normally, as
    defined by the Java Language Specification, or where possible, abnormally).
    This option is primarily intended for use with *work files* that
    are used solely by a single instance of the Java virtual machine. This
    option is not recommended for use when opening files that are open
    concurrently by other entities. Many of the details as to when and how
    the file is deleted are implementation specific and therefore not
    specified. In particular, an implementation may be unable to guarantee
    that it deletes the expected file when replaced by an attacker while the
    file is open. Consequently, security sensitive applications should take
    care when using this option.
    
     For security reasons, this option may imply the LinkOption.NOFOLLOW_LINKS option. In other words, if the option is present
    when opening an existing file that is a symbolic link then it may fail
    (by throwing java.io.IOException).
    """
    SPARSE = 7
    """
    Sparse file. When used with the .CREATE_NEW option then this
    option provides a *hint* that the new file will be sparse. The
    option is ignored when the file system does not support the creation of
    sparse files.
    """
    SYNC = 8
    """
    Requires that every update to the file's content or metadata be written
    synchronously to the underlying storage device.

    See
    - <a href="package-summary.html.integrity">Synchronized I/O file integrity</a>
    """
    DSYNC = 9
    """
    Requires that every update to the file's content be written
    synchronously to the underlying storage device.

    See
    - <a href="package-summary.html.integrity">Synchronized I/O file integrity</a>
    """
