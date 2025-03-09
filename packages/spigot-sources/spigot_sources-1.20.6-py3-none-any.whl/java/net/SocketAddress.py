"""
Python module generated from Java source file java.net.SocketAddress

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.net import *
from typing import Any, Callable, Iterable, Tuple


class SocketAddress(Serializable):
    """
    This class represents a Socket Address with no protocol attachment.
    As an abstract class, it is meant to be subclassed with a specific,
    protocol dependent, implementation.
    
    It provides an immutable object used by sockets for binding, connecting, or
    as returned values.

    See
    - java.net.ServerSocket

    Since
    - 1.4
    """

    def __init__(self):
        """
        Constructor for subclasses to call.
        """
        ...
