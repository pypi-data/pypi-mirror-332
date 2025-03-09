"""
Python module generated from Java source file java.net.MalformedURLException

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.io import IOException
from java.net import *
from typing import Any, Callable, Iterable, Tuple


class MalformedURLException(IOException):
    """
    Thrown to indicate that a malformed URL has occurred. Either no
    legal protocol could be found in a specification string or the
    string could not be parsed.

    Author(s)
    - Arthur van Hoff

    Since
    - 1.0
    """

    def __init__(self):
        """
        Constructs a `MalformedURLException` with no detail message.
        """
        ...


    def __init__(self, msg: str):
        """
        Constructs a `MalformedURLException` with the
        specified detail message.

        Arguments
        - msg: the detail message.
        """
        ...
