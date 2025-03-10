"""
Python module generated from Java source file org.bukkit.configuration.file.FileConfiguration

Java source file obtained from artifact spigot-api version 1.17.1-R0.1-20211121.234319-104

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.base import Charsets
from com.google.common.io import Files
from java.io import BufferedReader
from java.io import File
from java.io import FileInputStream
from java.io import FileNotFoundException
from java.io import FileOutputStream
from java.io import IOException
from java.io import InputStreamReader
from java.io import OutputStreamWriter
from java.io import Reader
from java.io import Writer
from org.apache.commons.lang import Validate
from org.bukkit.configuration import Configuration
from org.bukkit.configuration import InvalidConfigurationException
from org.bukkit.configuration import MemoryConfiguration
from org.bukkit.configuration.file import *
from typing import Any, Callable, Iterable, Tuple


class FileConfiguration(MemoryConfiguration):
    """
    This is a base class for all File based implementations of Configuration
    """

    def __init__(self):
        """
        Creates an empty FileConfiguration with no default values.
        """
        ...


    def __init__(self, defaults: "Configuration"):
        """
        Creates an empty FileConfiguration using the specified Configuration as a source for all default values.

        Arguments
        - defaults: Default value provider
        """
        ...


    def save(self, file: "File") -> None:
        """
        Saves this FileConfiguration to the specified location.
        
        If the file does not exist, it will be created. If already exists, it
        will be overwritten. If it cannot be overwritten or created, an
        exception will be thrown.
        
        This method will save using the system default encoding, or possibly
        using UTF8.

        Arguments
        - file: File to save to.

        Raises
        - IOException: Thrown when the given file cannot be written to for
            any reason.
        - IllegalArgumentException: Thrown when file is null.
        """
        ...


    def save(self, file: str) -> None:
        """
        Saves this FileConfiguration to the specified location.
        
        If the file does not exist, it will be created. If already exists, it
        will be overwritten. If it cannot be overwritten or created, an
        exception will be thrown.
        
        This method will save using the system default encoding, or possibly
        using UTF8.

        Arguments
        - file: File to save to.

        Raises
        - IOException: Thrown when the given file cannot be written to for
            any reason.
        - IllegalArgumentException: Thrown when file is null.
        """
        ...


    def saveToString(self) -> str:
        """
        Saves this FileConfiguration to a string, and returns it.

        Returns
        - String containing this configuration.
        """
        ...


    def load(self, file: "File") -> None:
        """
        Loads this FileConfiguration from the specified location.
        
        All the values contained within this configuration will be removed,
        leaving only settings and defaults, and the new values will be loaded
        from the given file.
        
        If the file cannot be loaded for any reason, an exception will be
        thrown.

        Arguments
        - file: File to load from.

        Raises
        - FileNotFoundException: Thrown when the given file cannot be
            opened.
        - IOException: Thrown when the given file cannot be read.
        - InvalidConfigurationException: Thrown when the given file is not
            a valid Configuration.
        - IllegalArgumentException: Thrown when file is null.
        """
        ...


    def load(self, reader: "Reader") -> None:
        """
        Loads this FileConfiguration from the specified reader.
        
        All the values contained within this configuration will be removed,
        leaving only settings and defaults, and the new values will be loaded
        from the given stream.

        Arguments
        - reader: the reader to load from

        Raises
        - IOException: thrown when underlying reader throws an IOException
        - InvalidConfigurationException: thrown when the reader does not
             represent a valid Configuration
        - IllegalArgumentException: thrown when reader is null
        """
        ...


    def load(self, file: str) -> None:
        """
        Loads this FileConfiguration from the specified location.
        
        All the values contained within this configuration will be removed,
        leaving only settings and defaults, and the new values will be loaded
        from the given file.
        
        If the file cannot be loaded for any reason, an exception will be
        thrown.

        Arguments
        - file: File to load from.

        Raises
        - FileNotFoundException: Thrown when the given file cannot be
            opened.
        - IOException: Thrown when the given file cannot be read.
        - InvalidConfigurationException: Thrown when the given file is not
            a valid Configuration.
        - IllegalArgumentException: Thrown when file is null.
        """
        ...


    def loadFromString(self, contents: str) -> None:
        """
        Loads this FileConfiguration from the specified string, as
        opposed to from file.
        
        All the values contained within this configuration will be removed,
        leaving only settings and defaults, and the new values will be loaded
        from the given string.
        
        If the string is invalid in any way, an exception will be thrown.

        Arguments
        - contents: Contents of a Configuration to load.

        Raises
        - InvalidConfigurationException: Thrown if the specified string is
            invalid.
        - IllegalArgumentException: Thrown if contents is null.
        """
        ...


    def options(self) -> "FileConfigurationOptions":
        ...
