"""
Python module generated from Java source file org.yaml.snakeyaml.extensions.compactnotation.CompactData

Java source file obtained from artifact snakeyaml version 2.2

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.yaml.snakeyaml.extensions.compactnotation import *
from typing import Any, Callable, Iterable, Tuple


class CompactData:
    """
    Custom data structure to support compact notation
    https://bitbucket.org/snakeyaml/snakeyaml/wiki/CompactObjectNotation
    """

    def __init__(self, prefix: str):
        """
        Create

        Arguments
        - prefix: - by default is serves as a full class Name, but it can be changed
        """
        ...


    def getPrefix(self) -> str:
        """
        getter

        Returns
        - prefix from the document
        """
        ...


    def getProperties(self) -> dict[str, str]:
        """
        Getter

        Returns
        - properties
        """
        ...


    def getArguments(self) -> list[str]:
        """
        getter

        Returns
        - arguments
        """
        ...


    def toString(self) -> str:
        """
        visual representation

        Returns
        - readable data
        """
        ...
