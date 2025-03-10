"""
Python module generated from Java source file org.yaml.snakeyaml.representer.BaseRepresenter

Java source file obtained from artifact snakeyaml version 1.28

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util import IdentityHashMap
from org.yaml.snakeyaml import DumperOptions
from org.yaml.snakeyaml.DumperOptions import FlowStyle
from org.yaml.snakeyaml.DumperOptions import ScalarStyle
from org.yaml.snakeyaml.introspector import PropertyUtils
from org.yaml.snakeyaml.nodes import AnchorNode
from org.yaml.snakeyaml.nodes import MappingNode
from org.yaml.snakeyaml.nodes import Node
from org.yaml.snakeyaml.nodes import NodeTuple
from org.yaml.snakeyaml.nodes import ScalarNode
from org.yaml.snakeyaml.nodes import SequenceNode
from org.yaml.snakeyaml.nodes import Tag
from org.yaml.snakeyaml.representer import *
from typing import Any, Callable, Iterable, Tuple


class BaseRepresenter:
    """
    Represent basic YAML structures: scalar, sequence, mapping
    """

    def represent(self, data: "Object") -> "Node":
        ...


    def setDefaultScalarStyle(self, defaultStyle: "ScalarStyle") -> None:
        ...


    def getDefaultScalarStyle(self) -> "ScalarStyle":
        ...


    def setDefaultFlowStyle(self, defaultFlowStyle: "FlowStyle") -> None:
        ...


    def getDefaultFlowStyle(self) -> "FlowStyle":
        ...


    def setPropertyUtils(self, propertyUtils: "PropertyUtils") -> None:
        ...


    def getPropertyUtils(self) -> "PropertyUtils":
        ...


    def isExplicitPropertyUtils(self) -> bool:
        ...
