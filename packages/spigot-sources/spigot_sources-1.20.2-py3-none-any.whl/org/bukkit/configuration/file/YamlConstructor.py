"""
Python module generated from Java source file org.bukkit.configuration.file.YamlConstructor

Java source file obtained from artifact spigot-api version 1.20.2-R0.1-20231205.164257-71

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.configuration.file import *
from org.bukkit.configuration.serialization import ConfigurationSerialization
from org.yaml.snakeyaml import LoaderOptions
from org.yaml.snakeyaml.constructor import SafeConstructor
from org.yaml.snakeyaml.error import YAMLException
from org.yaml.snakeyaml.nodes import MappingNode
from org.yaml.snakeyaml.nodes import Node
from org.yaml.snakeyaml.nodes import Tag
from typing import Any, Callable, Iterable, Tuple


class YamlConstructor(SafeConstructor):

    def __init__(self):
        """
        Deprecated
        - options required
        """
        ...


    def __init__(self, loaderOptions: "LoaderOptions"):
        ...


    def flattenMapping(self, node: "MappingNode") -> None:
        ...


    def construct(self, node: "Node") -> "Object":
        ...
