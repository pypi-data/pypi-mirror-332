"""
Python module generated from Java source file org.yaml.snakeyaml.constructor.Constructor

Java source file obtained from artifact snakeyaml version 2.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.math import BigDecimal
from java.math import BigInteger
from java.util import Calendar
from java.util import Date
from java.util import UUID
from org.yaml.snakeyaml import LoaderOptions
from org.yaml.snakeyaml import TypeDescription
from org.yaml.snakeyaml.constructor import *
from org.yaml.snakeyaml.error import YAMLException
from org.yaml.snakeyaml.introspector import Property
from org.yaml.snakeyaml.nodes import MappingNode
from org.yaml.snakeyaml.nodes import Node
from org.yaml.snakeyaml.nodes import NodeId
from org.yaml.snakeyaml.nodes import NodeTuple
from org.yaml.snakeyaml.nodes import ScalarNode
from org.yaml.snakeyaml.nodes import SequenceNode
from org.yaml.snakeyaml.nodes import Tag
from org.yaml.snakeyaml.util import EnumUtils
from typing import Any, Callable, Iterable, Tuple


class Constructor(SafeConstructor):
    """
    Construct a custom Java instance.
    """

    def __init__(self, loadingConfig: "LoaderOptions"):
        """
        Create with options

        Arguments
        - loadingConfig: - config
        """
        ...


    def __init__(self, theRoot: type["Object"], loadingConfig: "LoaderOptions"):
        """
        Create

        Arguments
        - theRoot: - the class to create (to be the root of the YAML document)
        - loadingConfig: - options
        """
        ...


    def __init__(self, theRoot: "TypeDescription", loadingConfig: "LoaderOptions"):
        """
        Create

        Arguments
        - theRoot: - the root class to create
        - loadingConfig: options
        """
        ...


    def __init__(self, theRoot: "TypeDescription", moreTDs: Iterable["TypeDescription"], loadingConfig: "LoaderOptions"):
        """
        Create with all possible arguments

        Arguments
        - theRoot: - the class (usually JavaBean) to be constructed
        - moreTDs: - collection of classes used by the root class
        - loadingConfig: - configuration
        """
        ...


    def __init__(self, theRoot: str, loadingConfig: "LoaderOptions"):
        """
        Create

        Arguments
        - theRoot: - the main class to crate
        - loadingConfig: - options

        Raises
        - ClassNotFoundException: if something goes wrong
        """
        ...
