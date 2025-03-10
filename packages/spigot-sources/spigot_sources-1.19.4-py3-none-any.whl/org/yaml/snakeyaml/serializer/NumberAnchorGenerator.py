"""
Python module generated from Java source file org.yaml.snakeyaml.serializer.NumberAnchorGenerator

Java source file obtained from artifact snakeyaml version 1.33

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.text import NumberFormat
from org.yaml.snakeyaml.nodes import Node
from org.yaml.snakeyaml.serializer import *
from typing import Any, Callable, Iterable, Tuple


class NumberAnchorGenerator(AnchorGenerator):

    def __init__(self, lastAnchorId: int):
        ...


    def nextAnchor(self, node: "Node") -> str:
        ...
