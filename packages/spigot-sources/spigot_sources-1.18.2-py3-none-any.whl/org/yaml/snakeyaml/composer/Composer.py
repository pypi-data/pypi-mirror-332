"""
Python module generated from Java source file org.yaml.snakeyaml.composer.Composer

Java source file obtained from artifact snakeyaml version 1.30

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util import Collections
from org.yaml.snakeyaml.DumperOptions import FlowStyle
from org.yaml.snakeyaml import LoaderOptions
from org.yaml.snakeyaml.comments import CommentEventsCollector
from org.yaml.snakeyaml.comments import CommentLine
from org.yaml.snakeyaml.comments import CommentType
from org.yaml.snakeyaml.composer import *
from org.yaml.snakeyaml.error import Mark
from org.yaml.snakeyaml.error import YAMLException
from org.yaml.snakeyaml.events import AliasEvent
from org.yaml.snakeyaml.events import Event
from org.yaml.snakeyaml.events import MappingStartEvent
from org.yaml.snakeyaml.events import NodeEvent
from org.yaml.snakeyaml.events import ScalarEvent
from org.yaml.snakeyaml.events import SequenceStartEvent
from org.yaml.snakeyaml.nodes import MappingNode
from org.yaml.snakeyaml.nodes import Node
from org.yaml.snakeyaml.nodes import NodeId
from org.yaml.snakeyaml.nodes import NodeTuple
from org.yaml.snakeyaml.nodes import ScalarNode
from org.yaml.snakeyaml.nodes import SequenceNode
from org.yaml.snakeyaml.nodes import Tag
from org.yaml.snakeyaml.parser import Parser
from org.yaml.snakeyaml.resolver import Resolver
from typing import Any, Callable, Iterable, Tuple


class Composer:
    """
    Creates a node graph from parser events.
    
    Corresponds to the 'Compose' step as described in chapter 3.1 of the
    <a href="http://yaml.org/spec/1.1/">YAML Specification</a>.
    """

    def __init__(self, parser: "Parser", resolver: "Resolver"):
        ...


    def __init__(self, parser: "Parser", resolver: "Resolver", loadingConfig: "LoaderOptions"):
        ...


    def checkNode(self) -> bool:
        """
        Checks if further documents are available.

        Returns
        - `True` if there is at least one more document.
        """
        ...


    def getNode(self) -> "Node":
        """
        Reads and composes the next document.

        Returns
        - The root node of the document or `null` if no more documents are available.
        """
        ...


    def getSingleNode(self) -> "Node":
        """
        Reads a document from a source that contains only one document.
        
        If the stream contains more than one document an exception is thrown.

        Returns
        - The root node of the document or `null` if no document
        is available.
        """
        ...
