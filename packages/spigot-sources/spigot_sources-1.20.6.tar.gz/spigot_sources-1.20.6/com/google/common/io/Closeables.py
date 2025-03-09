"""
Python module generated from Java source file com.google.common.io.Closeables

Java source file obtained from artifact guava version 32.1.2-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtIncompatible
from com.google.common.annotations import J2ktIncompatible
from com.google.common.annotations import VisibleForTesting
from com.google.common.io import *
from java.io import Closeable
from java.io import IOException
from java.io import InputStream
from java.io import Reader
from javax.annotation import CheckForNull
from typing import Any, Callable, Iterable, Tuple


class Closeables:
    """
    Utility methods for working with Closeable objects.

    Author(s)
    - Michael Lancaster

    Since
    - 1.0
    """

    @staticmethod
    def close(closeable: "Closeable", swallowIOException: bool) -> None:
        """
        Closes a Closeable, with control over whether an `IOException` may be thrown.
        This is primarily useful in a finally block, where a thrown exception needs to be logged but
        not propagated (otherwise the original exception will be lost).
        
        If `swallowIOException` is True then we never throw `IOException` but merely log
        it.
        
        Example:
        
        ````public void useStreamNicely() throws IOException {
          SomeStream stream = new SomeStream("foo");
          boolean threw = True;
          try {
            // ... code which does something with the stream ...
            threw = False;` finally {
            // If an exception occurs, rethrow it only if threw==False:
            Closeables.close(stream, threw);
          }
        }
        }```

        Arguments
        - closeable: the `Closeable` object to be closed, or null, in which case this method
            does nothing
        - swallowIOException: if True, don't propagate IO exceptions thrown by the `close`
            methods

        Raises
        - IOException: if `swallowIOException` is False and `close` throws an `IOException`.
        """
        ...


    @staticmethod
    def closeQuietly(inputStream: "InputStream") -> None:
        """
        Closes the given InputStream, logging any `IOException` that's thrown rather than
        propagating it.
        
        While it's not safe in the general case to ignore exceptions that are thrown when closing an
        I/O resource, it should generally be safe in the case of a resource that's being used only for
        reading, such as an `InputStream`. Unlike with writable resources, there's no chance that
        a failure that occurs when closing the stream indicates a meaningful problem such as a failure
        to flush all bytes to the underlying resource.

        Arguments
        - inputStream: the input stream to be closed, or `null` in which case this method
            does nothing

        Since
        - 17.0
        """
        ...


    @staticmethod
    def closeQuietly(reader: "Reader") -> None:
        """
        Closes the given Reader, logging any `IOException` that's thrown rather than
        propagating it.
        
        While it's not safe in the general case to ignore exceptions that are thrown when closing an
        I/O resource, it should generally be safe in the case of a resource that's being used only for
        reading, such as a `Reader`. Unlike with writable resources, there's no chance that a
        failure that occurs when closing the reader indicates a meaningful problem such as a failure to
        flush all bytes to the underlying resource.

        Arguments
        - reader: the reader to be closed, or `null` in which case this method does nothing

        Since
        - 17.0
        """
        ...
