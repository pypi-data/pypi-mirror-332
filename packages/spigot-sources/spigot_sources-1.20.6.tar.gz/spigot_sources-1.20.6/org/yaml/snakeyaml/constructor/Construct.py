"""
Python module generated from Java source file org.yaml.snakeyaml.constructor.Construct

Java source file obtained from artifact snakeyaml version 2.2

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.yaml.snakeyaml.constructor import *
from org.yaml.snakeyaml.nodes import Node
from typing import Any, Callable, Iterable, Tuple


class Construct:
    """
    Provide a way to construct a Java instance out of the composed Node. Support recursive objects if
    it is required. (create Native Data Structure out of Node Graph)

    See
    - <a href="http://yaml.org/spec/1.1/.id859109">Chapter 3. Processing YAML Information</a>
    """

    def construct(self, node: "Node") -> "Object":
        """
        Construct a Java instance with all the properties injected when it is possible.

        Arguments
        - node: composed Node

        Returns
        - a complete Java instance
        """
        ...


    def construct2ndStep(self, node: "Node", object: "Object") -> None:
        """
        Apply the second step when constructing recursive structures. Because the instance is already
        created it can assign a reference to itself.

        Arguments
        - node: composed Node
        - object: the instance constructed earlier by `construct(Node node)` for the
               provided Node
        """
        ...
