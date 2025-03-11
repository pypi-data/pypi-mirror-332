"""
Python module generated from Java source file java.net.UnknownHostException

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.io import IOException
from java.net import *
from typing import Any, Callable, Iterable, Tuple


class UnknownHostException(IOException):
    """
    Thrown to indicate that the IP address of a host could not be determined.

    Author(s)
    - Jonathan Payne

    Since
    - 1.0
    """

    def __init__(self, message: str):
        """
        Constructs a new `UnknownHostException` with the
        specified detail message.

        Arguments
        - message: the detail message.
        """
        ...


    def __init__(self):
        """
        Constructs a new `UnknownHostException` with no detail
        message.
        """
        ...
