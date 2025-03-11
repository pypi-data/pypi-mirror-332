"""
Python module generated from Java source file java.net.SocketException

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.io import IOException
from java.net import *
from typing import Any, Callable, Iterable, Tuple


class SocketException(IOException):
    """
    Thrown to indicate that there is an error creating or accessing a Socket.

    Author(s)
    - Jonathan Payne

    Since
    - 1.0
    """

    def __init__(self, msg: str):
        """
        Constructs a new `SocketException` with the
        specified detail message.

        Arguments
        - msg: the detail message.
        """
        ...


    def __init__(self):
        """
        Constructs a new `SocketException` with no detail message.
        """
        ...
