"""
Python module generated from Java source file java.io.Closeable

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.io import *
from java.io import IOException
from typing import Any, Callable, Iterable, Tuple


class Closeable(AutoCloseable):
    """
    A `Closeable` is a source or destination of data that can be closed.
    The close method is invoked to release resources that the object is
    holding (such as open files).

    Since
    - 1.5
    """

    def close(self) -> None:
        """
        Closes this stream and releases any system resources associated
        with it. If the stream is already closed then invoking this
        method has no effect.
        
         As noted in AutoCloseable.close(), cases where the
        close may fail require careful attention. It is strongly advised
        to relinquish the underlying resources and to internally
        *mark* the `Closeable` as closed, prior to throwing
        the `IOException`.

        Raises
        - IOException: if an I/O error occurs
        """
        ...
