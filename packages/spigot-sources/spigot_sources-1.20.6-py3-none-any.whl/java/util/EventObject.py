"""
Python module generated from Java source file java.util.EventObject

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util import *
from typing import Any, Callable, Iterable, Tuple


class EventObject(Serializable):

    def __init__(self, source: "Object"):
        """
        Constructs a prototypical Event.

        Arguments
        - source: the object on which the Event initially occurred

        Raises
        - IllegalArgumentException: if source is null
        """
        ...


    def getSource(self) -> "Object":
        """
        The object on which the Event initially occurred.

        Returns
        - the object on which the Event initially occurred
        """
        ...


    def toString(self) -> str:
        """
        Returns a String representation of this EventObject.

        Returns
        - a String representation of this EventObject
        """
        ...
