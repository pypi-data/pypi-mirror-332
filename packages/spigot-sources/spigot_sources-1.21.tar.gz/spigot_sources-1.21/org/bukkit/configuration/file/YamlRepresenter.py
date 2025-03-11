"""
Python module generated from Java source file org.bukkit.configuration.file.YamlRepresenter

Java source file obtained from artifact spigot-api version 1.21-R0.1-20240807.214924-87

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.configuration import ConfigurationSection
from org.bukkit.configuration.file import *
from org.bukkit.configuration.serialization import ConfigurationSerializable
from org.bukkit.configuration.serialization import ConfigurationSerialization
from org.yaml.snakeyaml import DumperOptions
from org.yaml.snakeyaml.nodes import Node
from org.yaml.snakeyaml.representer import Representer
from typing import Any, Callable, Iterable, Tuple


class YamlRepresenter(Representer):

    def __init__(self):
        """
        Deprecated
        - options required
        """
        ...


    def __init__(self, options: "DumperOptions"):
        ...
