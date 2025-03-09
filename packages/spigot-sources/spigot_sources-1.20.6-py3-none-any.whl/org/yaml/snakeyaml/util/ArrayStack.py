"""
Python module generated from Java source file org.yaml.snakeyaml.util.ArrayStack

Java source file obtained from artifact snakeyaml version 2.2

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.yaml.snakeyaml.util import *
from typing import Any, Callable, Iterable, Tuple


class ArrayStack:
    """
    Custom stack
    
    Type `<T>`: data to keep in stack
    """

    def __init__(self, initSize: int):
        """
        Create

        Arguments
        - initSize: - book the size
        """
        ...


    def push(self, obj: "T") -> None:
        """
        Add the element to the head

        Arguments
        - obj: - data to be added
        """
        ...


    def pop(self) -> "T":
        """
        Get the head and remove it from the stack

        Returns
        - the head
        """
        ...


    def isEmpty(self) -> bool:
        """
        Check

        Returns
        - True when it contains nothing
        """
        ...


    def clear(self) -> None:
        """
        remove all items in the stack
        """
        ...
