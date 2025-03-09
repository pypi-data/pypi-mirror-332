"""
Python module generated from Java source file org.bukkit.configuration.file.YamlConfigurationOptions

Java source file obtained from artifact spigot-api version 1.20.6-R0.1-20240613.150924-57

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.base import Preconditions
from org.bukkit.configuration.file import *
from typing import Any, Callable, Iterable, Tuple


class YamlConfigurationOptions(FileConfigurationOptions):
    """
    Various settings for controlling the input and output of a YamlConfiguration
    """

    def configuration(self) -> "YamlConfiguration":
        ...


    def copyDefaults(self, value: bool) -> "YamlConfigurationOptions":
        ...


    def pathSeparator(self, value: str) -> "YamlConfigurationOptions":
        ...


    def setHeader(self, value: list[str]) -> "YamlConfigurationOptions":
        ...


    def header(self, value: str) -> "YamlConfigurationOptions":
        ...


    def setFooter(self, value: list[str]) -> "YamlConfigurationOptions":
        ...


    def parseComments(self, value: bool) -> "YamlConfigurationOptions":
        ...


    def copyHeader(self, value: bool) -> "YamlConfigurationOptions":
        ...


    def indent(self) -> int:
        """
        Gets how much spaces should be used to indent each line.
        
        The minimum value this may be is 2, and the maximum is 9.

        Returns
        - How much to indent by
        """
        ...


    def indent(self, value: int) -> "YamlConfigurationOptions":
        """
        Sets how much spaces should be used to indent each line.
        
        The minimum value this may be is 2, and the maximum is 9.

        Arguments
        - value: New indent

        Returns
        - This object, for chaining
        """
        ...


    def width(self) -> int:
        """
        Gets how long a line can be, before it gets split.

        Returns
        - How the max line width
        """
        ...


    def width(self, value: int) -> "YamlConfigurationOptions":
        """
        Sets how long a line can be, before it gets split.

        Arguments
        - value: New width

        Returns
        - This object, for chaining
        """
        ...
