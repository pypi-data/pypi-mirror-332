"""
Python module generated from Java source file org.yaml.snakeyaml.constructor.AbstractConstruct

Java source file obtained from artifact snakeyaml version 2.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.yaml.snakeyaml.constructor import *
from org.yaml.snakeyaml.error import YAMLException
from org.yaml.snakeyaml.nodes import Node
from typing import Any, Callable, Iterable, Tuple


class AbstractConstruct(Construct):
    """
    Because recursive structures are not very common we provide a way to save some typing when
    extending a constructor
    """

    def construct2ndStep(self, node: "Node", data: "Object") -> None:
        """
        Fail with a reminder to provide the seconds step for a recursive structure

        See
        - org.yaml.snakeyaml.constructor.Construct.construct2ndStep(org.yaml.snakeyaml.nodes.Node,
             java.lang.Object)
        """
        ...
