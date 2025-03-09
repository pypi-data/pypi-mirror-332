"""
Python module generated from Java source file org.yaml.snakeyaml.serializer.AnchorGenerator

Java source file obtained from artifact snakeyaml version 2.2

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.yaml.snakeyaml.nodes import Node
from org.yaml.snakeyaml.serializer import *
from typing import Any, Callable, Iterable, Tuple


class AnchorGenerator:
    """
    Support different anchors
    """

    def nextAnchor(self, node: "Node") -> str:
        """
        Create a custom anchor to the provided Node

        Arguments
        - node: - the data to anchor

        Returns
        - value to be used in the YAML document
        """
        ...
