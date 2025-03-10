"""
Python module generated from Java source file com.google.common.io.InsecureRecursiveDeleteException

Java source file obtained from artifact guava version 31.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.annotations import GwtIncompatible
from com.google.common.io import *
from com.google.j2objc.annotations import J2ObjCIncompatible
from java.nio.file import FileSystemException
from java.nio.file import SecureDirectoryStream
from javax.annotation import CheckForNull
from typing import Any, Callable, Iterable, Tuple


class InsecureRecursiveDeleteException(FileSystemException):
    """
    Exception indicating that a recursive delete can't be performed because the file system does not
    have the support necessary to guarantee that it is not vulnerable to race conditions that would
    allow it to delete files and directories outside of the directory being deleted (i.e., SecureDirectoryStream is not supported).
    
    RecursiveDeleteOption.ALLOW_INSECURE can be used to force the recursive delete method
    to proceed anyway.

    Author(s)
    - Colin Decker

    Since
    - 21.0
    """

    def __init__(self, file: str):
        ...
