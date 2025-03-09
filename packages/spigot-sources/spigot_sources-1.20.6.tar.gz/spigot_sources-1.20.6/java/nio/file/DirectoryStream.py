"""
Python module generated from Java source file java.nio.file.DirectoryStream

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.io import Closeable
from java.io import IOException
from java.nio.file import *
from java.util import Iterator
from typing import Any, Callable, Iterable, Tuple


class DirectoryStream(Closeable, Iterable):

    def iterator(self) -> Iterator["T"]:
        """
        Returns the iterator associated with this `DirectoryStream`.

        Returns
        - the iterator associated with this `DirectoryStream`

        Raises
        - IllegalStateException: if this directory stream is closed or the iterator has already
                 been returned
        """
        ...


    class Filter:
        """
        An interface that is implemented by objects that decide if a directory
        entry should be accepted or filtered. A `Filter` is passed as the
        parameter to the Files.newDirectoryStream(Path,DirectoryStream.Filter)
        method when opening a directory to iterate over the entries in the
        directory.
        
        Type `<T>`: the type of the directory entry

        Since
        - 1.7
        """

        def accept(self, entry: "T") -> bool:
            """
            Decides if the given directory entry should be accepted or filtered.

            Arguments
            - entry: the directory entry to be tested

            Returns
            - `True` if the directory entry should be accepted

            Raises
            - IOException: If an I/O error occurs
            """
            ...
