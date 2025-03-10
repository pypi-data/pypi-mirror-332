"""
Python module generated from Java source file org.yaml.snakeyaml.constructor.Constructor

Java source file obtained from artifact snakeyaml version 1.28

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

    def __init__(self):
        ...


    def __init__(self, loadingConfig: "LoaderOptions"):
        ...


    def __init__(self, theRoot: type["Object"]):
        """
        Create Constructor for the specified class as the root.

        Arguments
        - theRoot: - the class (usually JavaBean) to be constructed
        """
        ...


    def __init__(self, theRoot: type["Object"], loadingConfig: "LoaderOptions"):
        ...


    def __init__(self, theRoot: "TypeDescription"):
        ...


    def __init__(self, theRoot: "TypeDescription", loadingConfig: "LoaderOptions"):
        ...


    def __init__(self, theRoot: "TypeDescription", moreTDs: Iterable["TypeDescription"]):
        ...


    def __init__(self, theRoot: "TypeDescription", moreTDs: Iterable["TypeDescription"], loadingConfig: "LoaderOptions"):
        ...


    def __init__(self, theRoot: str):
        """
        Create Constructor for a class which does not have to be in the classpath
        or for a definition from a Spring ApplicationContext.

        Arguments
        - theRoot: fully qualified class name of the root class (usually
                   JavaBean)

        Raises
        - ClassNotFoundException: if cannot be loaded by the classloader
        """
        ...


    def __init__(self, theRoot: str, loadingConfig: "LoaderOptions"):
        ...
