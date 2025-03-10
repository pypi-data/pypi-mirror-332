"""
Python module generated from Java source file org.bukkit.configuration.file.YamlConfiguration

Java source file obtained from artifact spigot-api version 1.17.1-R0.1-20211121.234319-104

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.io import File
from java.io import FileNotFoundException
from java.io import IOException
from java.io import Reader
from org.apache.commons.lang import Validate
from org.bukkit import Bukkit
from org.bukkit.configuration import Configuration
from org.bukkit.configuration import ConfigurationSection
from org.bukkit.configuration import InvalidConfigurationException
from org.bukkit.configuration.file import *
from org.yaml.snakeyaml import DumperOptions
from org.yaml.snakeyaml import LoaderOptions
from org.yaml.snakeyaml import Yaml
from org.yaml.snakeyaml.error import YAMLException
from org.yaml.snakeyaml.representer import Representer
from typing import Any, Callable, Iterable, Tuple


class YamlConfiguration(FileConfiguration):
    """
    An implementation of Configuration which saves all files in Yaml.
    Note that this implementation is not synchronized.
    """

    def saveToString(self) -> str:
        ...


    def loadFromString(self, contents: str) -> None:
        ...


    def options(self) -> "YamlConfigurationOptions":
        ...


    @staticmethod
    def loadConfiguration(file: "File") -> "YamlConfiguration":
        """
        Creates a new YamlConfiguration, loading from the given file.
        
        Any errors loading the Configuration will be logged and then ignored.
        If the specified input is not a valid config, a blank config will be
        returned.
        
        The encoding used may follow the system dependent default.

        Arguments
        - file: Input file

        Returns
        - Resulting configuration

        Raises
        - IllegalArgumentException: Thrown if file is null
        """
        ...


    @staticmethod
    def loadConfiguration(reader: "Reader") -> "YamlConfiguration":
        """
        Creates a new YamlConfiguration, loading from the given reader.
        
        Any errors loading the Configuration will be logged and then ignored.
        If the specified input is not a valid config, a blank config will be
        returned.

        Arguments
        - reader: input

        Returns
        - resulting configuration

        Raises
        - IllegalArgumentException: Thrown if stream is null
        """
        ...
