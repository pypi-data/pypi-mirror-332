"""
Python module generated from Java source file org.yaml.snakeyaml.constructor.BaseConstructor

Java source file obtained from artifact snakeyaml version 2.2

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.lang.reflect import Array
from java.lang.reflect import Modifier
from java.util import EnumMap
from java.util import LinkedHashSet
from java.util import NoSuchElementException
from java.util import SortedMap
from java.util import SortedSet
from org.yaml.snakeyaml import LoaderOptions
from org.yaml.snakeyaml import TypeDescription
from org.yaml.snakeyaml.composer import Composer
from org.yaml.snakeyaml.composer import ComposerException
from org.yaml.snakeyaml.constructor import *
from org.yaml.snakeyaml.error import YAMLException
from org.yaml.snakeyaml.introspector import PropertyUtils
from org.yaml.snakeyaml.nodes import CollectionNode
from org.yaml.snakeyaml.nodes import MappingNode
from org.yaml.snakeyaml.nodes import Node
from org.yaml.snakeyaml.nodes import NodeId
from org.yaml.snakeyaml.nodes import NodeTuple
from org.yaml.snakeyaml.nodes import ScalarNode
from org.yaml.snakeyaml.nodes import SequenceNode
from org.yaml.snakeyaml.nodes import Tag
from typing import Any, Callable, Iterable, Tuple


class BaseConstructor:
    """
    Base code
    """

    def __init__(self, loadingConfig: "LoaderOptions"):
        """
        Create

        Arguments
        - loadingConfig: - options
        """
        ...


    def setComposer(self, composer: "Composer") -> None:
        ...


    def checkData(self) -> bool:
        """
        Check if more documents available

        Returns
        - True when there are more YAML documents in the stream
        """
        ...


    def getData(self) -> "Object":
        """
        Construct and return the next document

        Returns
        - constructed instance
        """
        ...


    def getSingleData(self, type: type[Any]) -> "Object":
        """
        Ensure that the stream contains a single document and construct it

        Arguments
        - type: the class of the instance being created

        Returns
        - constructed instance

        Raises
        - ComposerException: in case there are more documents in the stream
        """
        ...


    def setPropertyUtils(self, propertyUtils: "PropertyUtils") -> None:
        ...


    def getPropertyUtils(self) -> "PropertyUtils":
        ...


    def addTypeDescription(self, definition: "TypeDescription") -> "TypeDescription":
        """
        Make YAML aware how to parse a custom Class. If there is no root Class assigned in constructor
        then the 'root' property of this definition is respected.

        Arguments
        - definition: to be added to the Constructor

        Returns
        - the previous value associated with `definition`, or `null` if
                there was no mapping for `definition`.
        """
        ...


    def isExplicitPropertyUtils(self) -> bool:
        ...


    def isAllowDuplicateKeys(self) -> bool:
        ...


    def setAllowDuplicateKeys(self, allowDuplicateKeys: bool) -> None:
        ...


    def isWrappedToRootException(self) -> bool:
        ...


    def setWrappedToRootException(self, wrappedToRootException: bool) -> None:
        ...


    def isEnumCaseSensitive(self) -> bool:
        ...


    def setEnumCaseSensitive(self, enumCaseSensitive: bool) -> None:
        ...


    def getLoadingConfig(self) -> "LoaderOptions":
        ...
