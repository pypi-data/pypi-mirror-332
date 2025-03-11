"""
Python module generated from Java source file java.nio.file.NotDirectoryException

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.nio.file import *
from typing import Any, Callable, Iterable, Tuple


class NotDirectoryException(FileSystemException):

    def __init__(self, file: str):
        """
        Constructs an instance of this class.

        Arguments
        - file: a string identifying the file or `null` if not known
        """
        ...
