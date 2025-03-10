"""
Python module generated from Java source file org.yaml.snakeyaml.extensions.compactnotation.CompactConstructor

Java source file obtained from artifact snakeyaml version 1.33

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util import Iterator
from java.util.regex import Matcher
from java.util.regex import Pattern
from org.yaml.snakeyaml import LoaderOptions
from org.yaml.snakeyaml.constructor import Construct
from org.yaml.snakeyaml.constructor import Constructor
from org.yaml.snakeyaml.error import YAMLException
from org.yaml.snakeyaml.extensions.compactnotation import *
from org.yaml.snakeyaml.introspector import Property
from org.yaml.snakeyaml.nodes import MappingNode
from org.yaml.snakeyaml.nodes import Node
from org.yaml.snakeyaml.nodes import NodeTuple
from org.yaml.snakeyaml.nodes import ScalarNode
from org.yaml.snakeyaml.nodes import SequenceNode
from typing import Any, Callable, Iterable, Tuple


class CompactConstructor(Constructor):
    """
    Construct a custom Java instance out of a compact object notation format.
    """

    def __init__(self, loadingConfig: "LoaderOptions"):
        """
        Create with provided options

        Arguments
        - loadingConfig: - options
        """
        ...


    def __init__(self):
        """
        Create with defaults
        """
        ...


    def getCompactData(self, scalar: str) -> "CompactData":
        ...


    class ConstructCompactObject(ConstructMapping):
        """
        Custom ConstructMapping
        """

        def construct2ndStep(self, node: "Node", object: "Object") -> None:
            ...


        def construct(self, node: "Node") -> "Object":
            ...
