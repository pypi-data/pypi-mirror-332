"""
Python module generated from Java source file java.io.EOFException

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.io import *
from typing import Any, Callable, Iterable, Tuple


class EOFException(IOException):
    """
    Signals that an end of file or end of stream has been reached
    unexpectedly during input.
    
    This exception is mainly used by data input streams to signal end of
    stream. Note that many other input operations return a special value on
    end of stream rather than throwing an exception.

    Author(s)
    - Frank Yellin

    See
    - java.io.IOException

    Since
    - 1.0
    """

    def __init__(self):
        """
        Constructs an `EOFException` with `null`
        as its error detail message.
        """
        ...


    def __init__(self, s: str):
        """
        Constructs an `EOFException` with the specified detail
        message. The string `s` may later be retrieved by the
        java.lang.Throwable.getMessage method of class
        `java.lang.Throwable`.

        Arguments
        - s: the detail message.
        """
        ...
