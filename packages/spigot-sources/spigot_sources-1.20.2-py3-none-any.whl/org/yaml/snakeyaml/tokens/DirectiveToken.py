"""
Python module generated from Java source file org.yaml.snakeyaml.tokens.DirectiveToken

Java source file obtained from artifact snakeyaml version 2.2

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.yaml.snakeyaml.error import Mark
from org.yaml.snakeyaml.error import YAMLException
from org.yaml.snakeyaml.tokens import *
from typing import Any, Callable, Iterable, Tuple


class DirectiveToken(Token):
    """
    Directive Token
    
    Type `<T>`: it is either Integer for the YAML directive or String for the TAG directive
    """

    def __init__(self, name: str, value: list["T"], startMark: "Mark", endMark: "Mark"):
        """
        Create

        Arguments
        - name: - directive name
        - value: - directive value
        - startMark: - start
        - endMark: - end
        """
        ...


    def getName(self) -> str:
        """
        getter

        Returns
        - name
        """
        ...


    def getValue(self) -> list["T"]:
        """
        getter

        Returns
        - value
        """
        ...


    def getTokenId(self) -> "Token.ID":
        """
        getter

        Returns
        - its identity
        """
        ...
