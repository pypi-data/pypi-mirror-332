"""
Python module generated from Java source file java.nio.file.FileSystemException

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.io import IOException
from java.nio.file import *
from typing import Any, Callable, Iterable, Tuple


class FileSystemException(IOException):

    def __init__(self, file: str):
        """
        Constructs an instance of this class. This constructor should be used
        when an operation involving one file fails and there isn't any additional
        information to explain the reason.

        Arguments
        - file: a string identifying the file or `null` if not known.
        """
        ...


    def __init__(self, file: str, other: str, reason: str):
        """
        Constructs an instance of this class. This constructor should be used
        when an operation involving two files fails, or there is additional
        information to explain the reason.

        Arguments
        - file: a string identifying the file or `null` if not known.
        - other: a string identifying the other file or `null` if there
                 isn't another file or if not known
        - reason: a reason message with additional information or `null`
        """
        ...


    def getFile(self) -> str:
        """
        Returns the file used to create this exception.

        Returns
        - the file (can be `null`)
        """
        ...


    def getOtherFile(self) -> str:
        """
        Returns the other file used to create this exception.

        Returns
        - the other file (can be `null`)
        """
        ...


    def getReason(self) -> str:
        """
        Returns the string explaining why the file system operation failed.

        Returns
        - the string explaining why the file system operation failed
        """
        ...


    def getMessage(self) -> str:
        """
        Returns the detail message string.
        """
        ...
