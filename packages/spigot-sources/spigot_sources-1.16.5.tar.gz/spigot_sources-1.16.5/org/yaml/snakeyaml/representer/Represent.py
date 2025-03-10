"""
Python module generated from Java source file org.yaml.snakeyaml.representer.Represent

Java source file obtained from artifact snakeyaml version 1.27

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.yaml.snakeyaml.nodes import Node
from org.yaml.snakeyaml.representer import *
from typing import Any, Callable, Iterable, Tuple


class Represent:
    """
    Create a Node Graph out of the provided Native Data Structure (Java
    instance).

    See
    - <a href="http://yaml.org/spec/1.1/.id859109">Chapter 3. Processing YAML
         Information</a>
    """

    def representData(self, data: "Object") -> "Node":
        """
        Create a Node

        Arguments
        - data: the instance to represent

        Returns
        - Node to dump
        """
        ...
