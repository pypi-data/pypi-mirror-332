"""
Python module generated from Java source file org.yaml.snakeyaml.nodes.Tag

Java source file obtained from artifact snakeyaml version 1.30

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.math import BigDecimal
from java.math import BigInteger
from java.net import URI
from java.util import Date
from org.yaml.snakeyaml.error import YAMLException
from org.yaml.snakeyaml.nodes import *
from org.yaml.snakeyaml.util import UriEncoder
from typing import Any, Callable, Iterable, Tuple


class Tag:

    PREFIX = "tag:yaml.org,2002:"
    YAML = Tag(PREFIX + "yaml")
    MERGE = Tag(PREFIX + "merge")
    SET = Tag(PREFIX + "set")
    PAIRS = Tag(PREFIX + "pairs")
    OMAP = Tag(PREFIX + "omap")
    BINARY = Tag(PREFIX + "binary")
    INT = Tag(PREFIX + "int")
    FLOAT = Tag(PREFIX + "float")
    TIMESTAMP = Tag(PREFIX + "timestamp")
    BOOL = Tag(PREFIX + "bool")
    NULL = Tag(PREFIX + "null")
    STR = Tag(PREFIX + "str")
    SEQ = Tag(PREFIX + "seq")
    MAP = Tag(PREFIX + "map")
    COMMENT = Tag(PREFIX + "comment")


    def __init__(self, tag: str):
        ...


    def __init__(self, clazz: type["Object"]):
        ...


    def __init__(self, uri: "URI"):
        """
        Arguments
        - uri: - URI to be encoded as tag value

        Deprecated
        - - it will be removed
        """
        ...


    def isSecondary(self) -> bool:
        ...


    def getValue(self) -> str:
        ...


    def startsWith(self, prefix: str) -> bool:
        ...


    def getClassName(self) -> str:
        ...


    def toString(self) -> str:
        ...


    def equals(self, obj: "Object") -> bool:
        ...


    def hashCode(self) -> int:
        ...


    def isCompatible(self, clazz: type[Any]) -> bool:
        """
        Java has more then 1 class compatible with a language-independent tag (!!int, !!float, !!timestamp etc)

        Arguments
        - clazz: - Class to check compatibility

        Returns
        - True when the Class can be represented by this language-independent tag
        """
        ...


    def matches(self, clazz: type["Object"]) -> bool:
        """
        Check whether this tag matches the global tag for the Class

        Arguments
        - clazz: - Class to check

        Returns
        - True when the this tag can be used as a global tag for the Class
        """
        ...
