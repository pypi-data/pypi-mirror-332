"""
Python module generated from Java source file com.google.common.io.FileBackedOutputStream

Java source file obtained from artifact guava version 32.1.2-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.annotations import GwtIncompatible
from com.google.common.annotations import J2ktIncompatible
from com.google.common.annotations import VisibleForTesting
from com.google.common.io import *
from com.google.errorprone.annotations.concurrent import GuardedBy
from com.google.j2objc.annotations import J2ObjCIncompatible
from java.io import ByteArrayInputStream
from java.io import ByteArrayOutputStream
from java.io import File
from java.io import FileInputStream
from java.io import FileOutputStream
from java.io import IOException
from java.io import InputStream
from java.io import OutputStream
from javax.annotation import CheckForNull
from typing import Any, Callable, Iterable, Tuple


class FileBackedOutputStream(OutputStream):
    """
    An OutputStream that starts buffering to a byte array, but switches to file buffering
    once the data reaches a configurable size.
    
    When this stream creates a temporary file, it restricts the file's permissions to the current
    user or, in the case of Android, the current app. If that is not possible (as is the case under
    the very old Android Ice Cream Sandwich release), then this stream throws an exception instead of
    creating a file that would be more accessible. (This behavior is new in Guava 32.0.0. Previous
    versions would create a file that is more accessible, as discussed in <a
    href="https://github.com/google/guava/issues/2575">Guava issue 2575</a>. TODO: b/283778848 - Fill
    in CVE number once it's available.)
    
    Temporary files created by this stream may live in the local filesystem until either:
    
    
      - .reset is called (removing the data in this stream and deleting the file), or...
      - this stream (or, more precisely, its .asByteSource view) is finalized during
          garbage collection, <strong>AND</strong> this stream was not constructed with .FileBackedOutputStream(int) the 1-arg constructor or the .FileBackedOutputStream(int, boolean) 2-arg constructor passing `False` in the
          second parameter.
    
    
    This class is thread-safe.

    Author(s)
    - Chris Nokleberg

    Since
    - 1.0
    """

    def __init__(self, fileThreshold: int):
        """
        Creates a new instance that uses the given file threshold, and does not reset the data when the
        ByteSource returned by .asByteSource is finalized.

        Arguments
        - fileThreshold: the number of bytes before the stream should switch to buffering to a file

        Raises
        - IllegalArgumentException: if `fileThreshold` is negative
        """
        ...


    def __init__(self, fileThreshold: int, resetOnFinalize: bool):
        """
        Creates a new instance that uses the given file threshold, and optionally resets the data when
        the ByteSource returned by .asByteSource is finalized.

        Arguments
        - fileThreshold: the number of bytes before the stream should switch to buffering to a file
        - resetOnFinalize: if True, the .reset method will be called when the ByteSource returned by .asByteSource is finalized.

        Raises
        - IllegalArgumentException: if `fileThreshold` is negative
        """
        ...


    def asByteSource(self) -> "ByteSource":
        """
        Returns a readable ByteSource view of the data that has been written to this stream.

        Since
        - 15.0
        """
        ...


    def reset(self) -> None:
        """
        Calls .close if not already closed, and then resets this object back to its initial
        state, for reuse. If data was buffered to a file, it will be deleted.

        Raises
        - IOException: if an I/O error occurred while deleting the file buffer
        """
        ...


    def write(self, b: int) -> None:
        ...


    def write(self, b: list[int]) -> None:
        ...


    def write(self, b: list[int], off: int, len: int) -> None:
        ...


    def close(self) -> None:
        ...


    def flush(self) -> None:
        ...
