"""
Python module generated from Java source file java.nio.file.Paths

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.net import URI
from java.nio.file import *
from java.nio.file.spi import FileSystemProvider
from typing import Any, Callable, Iterable, Tuple


class Paths:

    @staticmethod
    def get(first: str, *more: Tuple[str, ...]) -> "Path":
        """
        Converts a path string, or a sequence of strings that when joined form
        a path string, to a `Path`.

        Arguments
        - first: the path string or initial part of the path string
        - more: additional strings to be joined to form the path string

        Returns
        - the resulting `Path`

        Raises
        - InvalidPathException: if the path string cannot be converted to a `Path`

        See
        - Path.of(String,String...)

        Unknown Tags
        - This method simply invokes Path.of(String,String...)
        Path.of(String, String...) with the given parameters.
        """
        ...


    @staticmethod
    def get(uri: "URI") -> "Path":
        """
        Converts the given URI to a Path object.

        Arguments
        - uri: the URI to convert

        Returns
        - the resulting `Path`

        Raises
        - IllegalArgumentException: if preconditions on the `uri` parameter do not hold. The
                 format of the URI is provider specific.
        - FileSystemNotFoundException: The file system, identified by the URI, does not exist and
                 cannot be created automatically, or the provider identified by
                 the URI's scheme component is not installed
        - SecurityException: if a security manager is installed and it denies an unspecified
                 permission to access the file system

        See
        - Path.of(URI)

        Unknown Tags
        - This method simply invokes Path.of(URI) Path.of(URI) with the
        given parameter.
        """
        ...
