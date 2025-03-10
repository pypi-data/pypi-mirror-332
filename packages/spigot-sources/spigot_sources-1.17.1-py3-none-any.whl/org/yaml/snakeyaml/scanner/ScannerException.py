"""
Python module generated from Java source file org.yaml.snakeyaml.scanner.ScannerException

Java source file obtained from artifact snakeyaml version 1.28

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.yaml.snakeyaml.error import Mark
from org.yaml.snakeyaml.error import MarkedYAMLException
from org.yaml.snakeyaml.scanner import *
from typing import Any, Callable, Iterable, Tuple


class ScannerException(MarkedYAMLException):
    """
    Exception thrown by the Scanner implementations in case of malformed
    input.
    """

    def __init__(self, context: str, contextMark: "Mark", problem: str, problemMark: "Mark", note: str):
        """
        Constructs an instance.

        Arguments
        - context: Part of the input document in which vicinity the problem
                   occurred.
        - contextMark: Position of the `context` within the document.
        - problem: Part of the input document that caused the problem.
        - problemMark: Position of the `problem` within the document.
        - note: Message for the user with further information about the
                   problem.
        """
        ...


    def __init__(self, context: str, contextMark: "Mark", problem: str, problemMark: "Mark"):
        """
        Constructs an instance.

        Arguments
        - context: Part of the input document in which vicinity the problem
                   occurred.
        - contextMark: Position of the `context` within the document.
        - problem: Part of the input document that caused the problem.
        - problemMark: Position of the `problem` within the document.
        """
        ...
