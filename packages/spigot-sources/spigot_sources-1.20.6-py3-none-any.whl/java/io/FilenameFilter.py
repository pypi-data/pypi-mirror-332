"""
Python module generated from Java source file java.io.FilenameFilter

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.io import *
from typing import Any, Callable, Iterable, Tuple


class FilenameFilter:
    """
    Instances of classes that implement this interface are used to
    filter filenames. These instances are used to filter directory
    listings in the `list` method of class
    `File`, and by the Abstract Window Toolkit's file
    dialog component.

    Author(s)
    - Jonathan Payne

    See
    - java.io.File.list(java.io.FilenameFilter)

    Since
    - 1.0
    """

    def accept(self, dir: "File", name: str) -> bool:
        """
        Tests if a specified file should be included in a file list.

        Arguments
        - dir: the directory in which the file was found.
        - name: the name of the file.

        Returns
        - `True` if and only if the name should be
        included in the file list; `False` otherwise.
        """
        ...
