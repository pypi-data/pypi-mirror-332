"""
Python module generated from Java source file org.bukkit.configuration.file.YamlConfiguration

Java source file obtained from artifact spigot-api version 1.21.3-R0.1-20241203.162251-46

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.base import Preconditions
from java.io import ByteArrayInputStream
from java.io import File
from java.io import FileNotFoundException
from java.io import IOException
from java.io import Reader
from java.io import StringWriter
from java.nio.charset import StandardCharsets
from org.bukkit import Bukkit
from org.bukkit.configuration import Configuration
from org.bukkit.configuration import ConfigurationSection
from org.bukkit.configuration import InvalidConfigurationException
from org.bukkit.configuration.file import *
from org.bukkit.configuration.serialization import ConfigurationSerialization
from org.yaml.snakeyaml import DumperOptions
from org.yaml.snakeyaml import LoaderOptions
from org.yaml.snakeyaml import Yaml
from org.yaml.snakeyaml.comments import CommentLine
from org.yaml.snakeyaml.comments import CommentType
from org.yaml.snakeyaml.error import YAMLException
from org.yaml.snakeyaml.nodes import AnchorNode
from org.yaml.snakeyaml.nodes import MappingNode
from org.yaml.snakeyaml.nodes import Node
from org.yaml.snakeyaml.nodes import NodeTuple
from org.yaml.snakeyaml.nodes import ScalarNode
from org.yaml.snakeyaml.nodes import SequenceNode
from org.yaml.snakeyaml.nodes import Tag
from org.yaml.snakeyaml.reader import UnicodeReader
from typing import Any, Callable, Iterable, Tuple


class YamlConfiguration(FileConfiguration):
    """
    An implementation of Configuration which saves all files in Yaml.
    Note that this implementation is not synchronized.
    """

    def __init__(self):
        ...


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
