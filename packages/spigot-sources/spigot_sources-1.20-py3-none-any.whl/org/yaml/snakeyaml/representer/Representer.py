"""
Python module generated from Java source file org.yaml.snakeyaml.representer.Representer

Java source file obtained from artifact snakeyaml version 2.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util import Arrays
from java.util import Collections
from java.util import Iterator
from org.yaml.snakeyaml import DumperOptions
from org.yaml.snakeyaml.DumperOptions import FlowStyle
from org.yaml.snakeyaml import TypeDescription
from org.yaml.snakeyaml.introspector import Property
from org.yaml.snakeyaml.introspector import PropertyUtils
from org.yaml.snakeyaml.nodes import MappingNode
from org.yaml.snakeyaml.nodes import Node
from org.yaml.snakeyaml.nodes import NodeId
from org.yaml.snakeyaml.nodes import NodeTuple
from org.yaml.snakeyaml.nodes import ScalarNode
from org.yaml.snakeyaml.nodes import SequenceNode
from org.yaml.snakeyaml.nodes import Tag
from org.yaml.snakeyaml.representer import *
from typing import Any, Callable, Iterable, Tuple


class Representer(SafeRepresenter):
    """
    Represent JavaBeans
    """

    def __init__(self, options: "DumperOptions"):
        ...


    def addTypeDescription(self, td: "TypeDescription") -> "TypeDescription":
        ...


    def setPropertyUtils(self, propertyUtils: "PropertyUtils") -> None:
        ...
