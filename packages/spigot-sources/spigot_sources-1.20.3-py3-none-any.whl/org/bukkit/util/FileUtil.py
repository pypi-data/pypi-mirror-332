"""
Python module generated from Java source file org.bukkit.util.FileUtil

Java source file obtained from artifact spigot-api version 1.20.3-R0.1-20231207.085553-9

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.io import File
from java.io import FileInputStream
from java.io import FileOutputStream
from java.io import IOException
from org.bukkit.util import *
from typing import Any, Callable, Iterable, Tuple


class FileUtil:
    """
    Class containing file utilities
    """

    @staticmethod
    def copy(inFile: "File", outFile: "File") -> bool:
        """
        This method copies one file to another location

        Arguments
        - inFile: the source filename
        - outFile: the target filename

        Returns
        - True on success
        """
        ...
