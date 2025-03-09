"""
Python module generated from Java source file org.yaml.snakeyaml.parser.ParserException

Java source file obtained from artifact snakeyaml version 2.2

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.yaml.snakeyaml.error import Mark
from org.yaml.snakeyaml.error import MarkedYAMLException
from org.yaml.snakeyaml.parser import *
from typing import Any, Callable, Iterable, Tuple


class ParserException(MarkedYAMLException):
    """
    Exception thrown by the Parser implementations in case of malformed input.
    """

    def __init__(self, context: str, contextMark: "Mark", problem: str, problemMark: "Mark"):
        """
        Constructs an instance.

        Arguments
        - context: Part of the input document in which vicinity the problem occurred.
        - contextMark: Position of the `context` within the document.
        - problem: Part of the input document that caused the problem.
        - problemMark: Position of the `problem`. within the document.
        """
        ...
