"""
Python module generated from Java source file org.yaml.snakeyaml.representer.SafeRepresenter

Java source file obtained from artifact snakeyaml version 1.27

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.io import UnsupportedEncodingException
from java.math import BigInteger
from java.util import Arrays
from java.util import Calendar
from java.util import Date
from java.util import Iterator
from java.util import TimeZone
from java.util import UUID
from java.util.regex import Pattern
from org.yaml.snakeyaml import DumperOptions
from org.yaml.snakeyaml.error import YAMLException
from org.yaml.snakeyaml.external.biz.base64Coder import Base64Coder
from org.yaml.snakeyaml.nodes import Node
from org.yaml.snakeyaml.nodes import Tag
from org.yaml.snakeyaml.reader import StreamReader
from org.yaml.snakeyaml.representer import *
from typing import Any, Callable, Iterable, Tuple


class SafeRepresenter(BaseRepresenter):
    """
    Represent standard Java classes
    """

    def __init__(self):
        ...


    def __init__(self, options: "DumperOptions"):
        ...


    def addClassTag(self, clazz: type["Object"], tag: "Tag") -> "Tag":
        """
        Define a tag for the `Class` to serialize.

        Arguments
        - clazz: `Class` which tag is changed
        - tag: new tag to be used for every instance of the specified
                   `Class`

        Returns
        - the previous tag associated with the `Class`
        """
        ...


    def getTimeZone(self) -> "TimeZone":
        ...


    def setTimeZone(self, timeZone: "TimeZone") -> None:
        ...
