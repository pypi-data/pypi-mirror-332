"""
Python module generated from Java source file com.google.common.io.Resources

Java source file obtained from artifact guava version 31.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtIncompatible
from com.google.common.base import Charsets
from com.google.common.base import MoreObjects
from com.google.common.collect import Lists
from com.google.common.io import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from java.io import IOException
from java.io import InputStream
from java.io import OutputStream
from java.net import URL
from java.nio.charset import Charset
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class Resources:
    """
    Provides utility methods for working with resources in the classpath. Note that even though these
    methods use URL parameters, they are usually not appropriate for HTTP or other
    non-classpath resources.

    Author(s)
    - Colin Decker

    Since
    - 1.0
    """

    @staticmethod
    def asByteSource(url: "URL") -> "ByteSource":
        """
        Returns a ByteSource that reads from the given URL.

        Since
        - 14.0
        """
        ...


    @staticmethod
    def asCharSource(url: "URL", charset: "Charset") -> "CharSource":
        """
        Returns a CharSource that reads from the given URL using the given character set.

        Since
        - 14.0
        """
        ...


    @staticmethod
    def toByteArray(url: "URL") -> list[int]:
        """
        Reads all bytes from a URL into a byte array.

        Arguments
        - url: the URL to read from

        Returns
        - a byte array containing all the bytes from the URL

        Raises
        - IOException: if an I/O error occurs
        """
        ...


    @staticmethod
    def toString(url: "URL", charset: "Charset") -> str:
        """
        Reads all characters from a URL into a String, using the given character set.

        Arguments
        - url: the URL to read from
        - charset: the charset used to decode the input stream; see Charsets for helpful
            predefined constants

        Returns
        - a string containing all the characters from the URL

        Raises
        - IOException: if an I/O error occurs.
        """
        ...


    @staticmethod
    def readLines(url: "URL", charset: "Charset", callback: "LineProcessor"["T"]) -> "T":
        """
        Streams lines from a URL, stopping when our callback returns False, or we have read all of the
        lines.

        Arguments
        - url: the URL to read from
        - charset: the charset used to decode the input stream; see Charsets for helpful
            predefined constants
        - callback: the LineProcessor to use to handle the lines

        Returns
        - the output of processing the lines

        Raises
        - IOException: if an I/O error occurs
        """
        ...


    @staticmethod
    def readLines(url: "URL", charset: "Charset") -> list[str]:
        """
        Reads all of the lines from a URL. The lines do not include line-termination characters, but do
        include other leading and trailing whitespace.
        
        This method returns a mutable `List`. For an `ImmutableList`, use `Resources.asCharSource(url, charset).readLines()`.

        Arguments
        - url: the URL to read from
        - charset: the charset used to decode the input stream; see Charsets for helpful
            predefined constants

        Returns
        - a mutable List containing all the lines

        Raises
        - IOException: if an I/O error occurs
        """
        ...


    @staticmethod
    def copy(from: "URL", to: "OutputStream") -> None:
        """
        Copies all bytes from a URL to an output stream.

        Arguments
        - from: the URL to read from
        - to: the output stream

        Raises
        - IOException: if an I/O error occurs
        """
        ...


    @staticmethod
    def getResource(resourceName: str) -> "URL":
        """
        Returns a `URL` pointing to `resourceName` if the resource is found using the
        Thread.getContextClassLoader() context class loader. In simple environments, the
        context class loader will find resources from the class path. In environments where different
        threads can have different class loaders, for example app servers, the context class loader
        will typically have been set to an appropriate loader for the current thread.
        
        In the unusual case where the context class loader is null, the class loader that loaded
        this class (`Resources`) will be used instead.

        Raises
        - IllegalArgumentException: if the resource is not found
        """
        ...


    @staticmethod
    def getResource(contextClass: type[Any], resourceName: str) -> "URL":
        """
        Given a `resourceName` that is relative to `contextClass`, returns a `URL`
        pointing to the named resource.

        Raises
        - IllegalArgumentException: if the resource is not found
        """
        ...
