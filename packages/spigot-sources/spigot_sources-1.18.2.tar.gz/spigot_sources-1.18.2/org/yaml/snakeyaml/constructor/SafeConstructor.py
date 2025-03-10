"""
Python module generated from Java source file org.yaml.snakeyaml.constructor.SafeConstructor

Java source file obtained from artifact snakeyaml version 1.30

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.math import BigInteger
from java.util import Calendar
from java.util import Iterator
from java.util import TimeZone
from java.util.regex import Matcher
from java.util.regex import Pattern
from org.yaml.snakeyaml import LoaderOptions
from org.yaml.snakeyaml.constructor import *
from org.yaml.snakeyaml.error import YAMLException
from org.yaml.snakeyaml.external.biz.base64Coder import Base64Coder
from org.yaml.snakeyaml.nodes import MappingNode
from org.yaml.snakeyaml.nodes import Node
from org.yaml.snakeyaml.nodes import NodeId
from org.yaml.snakeyaml.nodes import NodeTuple
from org.yaml.snakeyaml.nodes import ScalarNode
from org.yaml.snakeyaml.nodes import SequenceNode
from org.yaml.snakeyaml.nodes import Tag
from typing import Any, Callable, Iterable, Tuple


class SafeConstructor(BaseConstructor):
    """
    Construct standard Java classes
    """

    undefinedConstructor = ConstructUndefined()


    def __init__(self):
        ...


    def __init__(self, loadingConfig: "LoaderOptions"):
        ...


    class ConstructYamlNull(AbstractConstruct):

        def construct(self, node: "Node") -> "Object":
            ...


    class ConstructYamlBool(AbstractConstruct):

        def construct(self, node: "Node") -> "Object":
            ...


    class ConstructYamlInt(AbstractConstruct):

        def construct(self, node: "Node") -> "Object":
            ...


    class ConstructYamlFloat(AbstractConstruct):

        def construct(self, node: "Node") -> "Object":
            ...


    class ConstructYamlBinary(AbstractConstruct):

        def construct(self, node: "Node") -> "Object":
            ...


    class ConstructYamlTimestamp(AbstractConstruct):

        def getCalendar(self) -> "Calendar":
            ...


        def construct(self, node: "Node") -> "Object":
            ...


    class ConstructYamlOmap(AbstractConstruct):

        def construct(self, node: "Node") -> "Object":
            ...


    class ConstructYamlPairs(AbstractConstruct):

        def construct(self, node: "Node") -> "Object":
            ...


    class ConstructYamlSet(Construct):

        def construct(self, node: "Node") -> "Object":
            ...


        def construct2ndStep(self, node: "Node", object: "Object") -> None:
            ...


    class ConstructYamlStr(AbstractConstruct):

        def construct(self, node: "Node") -> "Object":
            ...


    class ConstructYamlSeq(Construct):

        def construct(self, node: "Node") -> "Object":
            ...


        def construct2ndStep(self, node: "Node", data: "Object") -> None:
            ...


    class ConstructYamlMap(Construct):

        def construct(self, node: "Node") -> "Object":
            ...


        def construct2ndStep(self, node: "Node", object: "Object") -> None:
            ...


    class ConstructUndefined(AbstractConstruct):

        def construct(self, node: "Node") -> "Object":
            ...
