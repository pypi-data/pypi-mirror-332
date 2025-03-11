"""
Python module generated from Java source file com.google.common.io.RecursiveDeleteOption

Java source file obtained from artifact guava version 32.1.2-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtIncompatible
from com.google.common.annotations import J2ktIncompatible
from com.google.common.io import *
from com.google.j2objc.annotations import J2ObjCIncompatible
from enum import Enum
from java.nio.file import SecureDirectoryStream
from typing import Any, Callable, Iterable, Tuple


class RecursiveDeleteOption(Enum):
    """
    Options for use with recursive delete methods (MoreFiles.deleteRecursively and MoreFiles.deleteDirectoryContents).

    Author(s)
    - Colin Decker

    Since
    - 21.0
    """

    ALLOW_INSECURE = 0
    """
    Specifies that the recursive delete should not throw an exception when it can't be guaranteed
    that it can be done securely, without vulnerability to race conditions (i.e. when the file
    system does not support SecureDirectoryStream).
    
    **Warning:** On a file system that supports symbolic links, it is possible for an
    insecure recursive delete to delete files and directories that are *outside* the directory
    being deleted. This can happen if, after checking that a file is a directory (and not a
    symbolic link), that directory is deleted and replaced by a symbolic link to an outside
    directory before the call that opens the directory to read its entries. File systems that
    support `SecureDirectoryStream` do not have this vulnerability.
    """
