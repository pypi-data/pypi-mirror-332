"""
Python module generated from Java source file com.google.common.io.TempFileCreator

Java source file obtained from artifact guava version 33.3.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtIncompatible
from com.google.common.annotations import J2ktIncompatible
from com.google.common.annotations import VisibleForTesting
from com.google.common.collect import ImmutableList
from com.google.common.io import *
from com.google.j2objc.annotations import J2ObjCIncompatible
from java.io import File
from java.io import IOException
from java.lang.reflect import InvocationTargetException
from java.lang.reflect import Method
from java.nio.file import FileSystems
from java.nio.file import Paths
from java.nio.file.attribute import AclEntry
from java.nio.file.attribute import AclEntryPermission
from java.nio.file.attribute import FileAttribute
from java.nio.file.attribute import PosixFilePermissions
from java.nio.file.attribute import UserPrincipal
from java.util import EnumSet
from typing import Any, Callable, Iterable, Tuple


class TempFileCreator:
    """
    Creates temporary files and directories whose permissions are restricted to the current user or,
    in the case of Android, the current app. If that is not possible (as is the case under the very
    old Android Ice Cream Sandwich release), then this class throws an exception instead of creating
    a file or directory that would be more accessible.
    """


