"""
Python module generated from Java source file java.io.Flushable

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.io import *
from java.io import IOException
from typing import Any, Callable, Iterable, Tuple


class Flushable:
    """
    A `Flushable` is a destination of data that can be flushed.  The
    flush method is invoked to write any buffered output to the underlying
    stream.

    Since
    - 1.5
    """

    def flush(self) -> None:
        """
        Flushes this stream by writing any buffered output to the underlying
        stream.

        Raises
        - IOException: If an I/O error occurs
        """
        ...
