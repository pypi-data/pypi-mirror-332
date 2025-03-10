"""
Python module generated from Java source file org.yaml.snakeyaml.serializer.Serializer

Java source file obtained from artifact snakeyaml version 1.28

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.io import IOException
from org.yaml.snakeyaml import DumperOptions
from org.yaml.snakeyaml.DumperOptions import Version
from org.yaml.snakeyaml.comments import CommentLine
from org.yaml.snakeyaml.emitter import Emitable
from org.yaml.snakeyaml.events import AliasEvent
from org.yaml.snakeyaml.events import CommentEvent
from org.yaml.snakeyaml.events import DocumentEndEvent
from org.yaml.snakeyaml.events import DocumentStartEvent
from org.yaml.snakeyaml.events import ImplicitTuple
from org.yaml.snakeyaml.events import MappingEndEvent
from org.yaml.snakeyaml.events import MappingStartEvent
from org.yaml.snakeyaml.events import ScalarEvent
from org.yaml.snakeyaml.events import SequenceEndEvent
from org.yaml.snakeyaml.events import SequenceStartEvent
from org.yaml.snakeyaml.events import StreamEndEvent
from org.yaml.snakeyaml.events import StreamStartEvent
from org.yaml.snakeyaml.nodes import AnchorNode
from org.yaml.snakeyaml.nodes import MappingNode
from org.yaml.snakeyaml.nodes import Node
from org.yaml.snakeyaml.nodes import NodeId
from org.yaml.snakeyaml.nodes import NodeTuple
from org.yaml.snakeyaml.nodes import ScalarNode
from org.yaml.snakeyaml.nodes import SequenceNode
from org.yaml.snakeyaml.nodes import Tag
from org.yaml.snakeyaml.resolver import Resolver
from org.yaml.snakeyaml.serializer import *
from typing import Any, Callable, Iterable, Tuple


class Serializer:

    def __init__(self, emitter: "Emitable", resolver: "Resolver", opts: "DumperOptions", rootTag: "Tag"):
        ...


    def open(self) -> None:
        ...


    def close(self) -> None:
        ...


    def serialize(self, node: "Node") -> None:
        ...
