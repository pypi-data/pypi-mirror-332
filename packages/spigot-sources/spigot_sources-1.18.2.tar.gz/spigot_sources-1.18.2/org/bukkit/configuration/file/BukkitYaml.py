"""
Python module generated from Java source file org.bukkit.configuration.file.BukkitYaml

Java source file obtained from artifact spigot-api version 1.18.2-R0.1-20220607.160742-53

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.io import IOException
from java.io import Writer
from java.lang.reflect import Field
from java.util import ArrayDeque
from java.util import Queue
from org.bukkit.configuration.file import *
from org.yaml.snakeyaml import DumperOptions
from org.yaml.snakeyaml import LoaderOptions
from org.yaml.snakeyaml import Yaml
from org.yaml.snakeyaml.comments import CommentEventsCollector
from org.yaml.snakeyaml.comments import CommentType
from org.yaml.snakeyaml.constructor import BaseConstructor
from org.yaml.snakeyaml.emitter import Emitter
from org.yaml.snakeyaml.error import YAMLException
from org.yaml.snakeyaml.events import Event
from org.yaml.snakeyaml.nodes import Node
from org.yaml.snakeyaml.representer import Representer
from org.yaml.snakeyaml.serializer import Serializer
from typing import Any, Callable, Iterable, Tuple


class BukkitYaml(Yaml):

    def __init__(self, constructor: "BaseConstructor", representer: "Representer", dumperOptions: "DumperOptions", loadingConfig: "LoaderOptions"):
        ...


    def serialize(self, node: "Node", output: "Writer") -> None:
        ...
