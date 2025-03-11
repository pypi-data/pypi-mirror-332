"""
Python module generated from Java source file org.bukkit.configuration.file.FileConfigurationOptions

Java source file obtained from artifact spigot-api version 1.21-R0.1-20240807.214924-87

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util import Arrays
from java.util import Collections
from org.bukkit.configuration import MemoryConfiguration
from org.bukkit.configuration import MemoryConfigurationOptions
from org.bukkit.configuration.file import *
from typing import Any, Callable, Iterable, Tuple


class FileConfigurationOptions(MemoryConfigurationOptions):
    """
    Various settings for controlling the input and output of a FileConfiguration
    """

    def configuration(self) -> "FileConfiguration":
        ...


    def copyDefaults(self, value: bool) -> "FileConfigurationOptions":
        ...


    def pathSeparator(self, value: str) -> "FileConfigurationOptions":
        ...


    def getHeader(self) -> list[str]:
        """
        Gets the header that will be applied to the top of the saved output.
        
        This header will be commented out and applied directly at the top of
        the generated output of the FileConfiguration. It is not
        required to include a newline at the end of the header as it will
        automatically be applied, but you may include one if you wish for extra
        spacing.
        
        If no comments exist, an empty list will be returned. A null entry
        represents an empty line and an empty String represents an empty comment
        line.

        Returns
        - Unmodifiable header, every entry represents one line.
        """
        ...


    def header(self) -> str:
        """
        Returns
        - The string header.

        Deprecated
        - use getHeader() instead.
        """
        ...


    def setHeader(self, value: list[str]) -> "FileConfigurationOptions":
        """
        Sets the header that will be applied to the top of the saved output.
        
        This header will be commented out and applied directly at the top of
        the generated output of the FileConfiguration. It is not
        required to include a newline at the end of the header as it will
        automatically be applied, but you may include one if you wish for extra
        spacing.
        
        If no comments exist, an empty list will be returned. A null entry
        represents an empty line and an empty String represents an empty comment
        line.

        Arguments
        - value: New header, every entry represents one line.

        Returns
        - This object, for chaining
        """
        ...


    def header(self, value: str) -> "FileConfigurationOptions":
        """
        Arguments
        - value: The string header.

        Returns
        - This object, for chaining.

        Deprecated
        - use setHeader() instead
        """
        ...


    def getFooter(self) -> list[str]:
        """
        Gets the footer that will be applied to the bottom of the saved output.
        
        This footer will be commented out and applied directly at the bottom of
        the generated output of the FileConfiguration. It is not required
        to include a newline at the beginning of the footer as it will
        automatically be applied, but you may include one if you wish for extra
        spacing.
        
        If no comments exist, an empty list will be returned. A null entry
        represents an empty line and an empty String represents an empty comment
        line.

        Returns
        - Unmodifiable footer, every entry represents one line.
        """
        ...


    def setFooter(self, value: list[str]) -> "FileConfigurationOptions":
        """
        Sets the footer that will be applied to the bottom of the saved output.
        
        This footer will be commented out and applied directly at the bottom of
        the generated output of the FileConfiguration. It is not required
        to include a newline at the beginning of the footer as it will
        automatically be applied, but you may include one if you wish for extra
        spacing.
        
        If no comments exist, an empty list will be returned. A null entry
        represents an empty line and an empty String represents an empty comment
        line.

        Arguments
        - value: New footer, every entry represents one line.

        Returns
        - This object, for chaining
        """
        ...


    def parseComments(self) -> bool:
        """
        Gets whether or not comments should be loaded and saved.
        
        Defaults to True.

        Returns
        - Whether or not comments are parsed.
        """
        ...


    def parseComments(self, value: bool) -> "MemoryConfigurationOptions":
        """
        Sets whether or not comments should be loaded and saved.
        
        Defaults to True.

        Arguments
        - value: Whether or not comments are parsed.

        Returns
        - This object, for chaining
        """
        ...


    def copyHeader(self) -> bool:
        """
        Returns
        - Whether or not comments are parsed.

        Deprecated
        - Call .parseComments() instead.
        """
        ...


    def copyHeader(self, value: bool) -> "FileConfigurationOptions":
        """
        Arguments
        - value: Should comments be parsed.

        Returns
        - This object, for chaining

        Deprecated
        - Call .parseComments(boolean) instead.
        """
        ...
