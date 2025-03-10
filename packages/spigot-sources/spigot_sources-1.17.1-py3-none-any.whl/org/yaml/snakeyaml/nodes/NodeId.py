"""
Python module generated from Java source file org.yaml.snakeyaml.nodes.NodeId

Java source file obtained from artifact snakeyaml version 1.28

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.yaml.snakeyaml.nodes import *
from typing import Any, Callable, Iterable, Tuple


class NodeId(Enum):
    """
    Enum for the basic YAML types: scalar, sequence, mapping or anchor.
    """

    scalar = 0
    sequence = 1
    mapping = 2
    anchor = 3
