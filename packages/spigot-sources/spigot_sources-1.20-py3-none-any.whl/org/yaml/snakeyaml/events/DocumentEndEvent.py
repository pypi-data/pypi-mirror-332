"""
Python module generated from Java source file org.yaml.snakeyaml.events.DocumentEndEvent

Java source file obtained from artifact snakeyaml version 2.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.yaml.snakeyaml.error import Mark
from org.yaml.snakeyaml.events import *
from typing import Any, Callable, Iterable, Tuple


class DocumentEndEvent(Event):
    """
    Marks the end of a document.
    
    This event follows the document's content.
    """

    def __init__(self, startMark: "Mark", endMark: "Mark", explicit: bool):
        """
        Create

        Arguments
        - startMark: - start
        - endMark: - end
        - explicit: - True when it is present in the document, False for implicitly added
        """
        ...


    def getExplicit(self) -> bool:
        """
        getter

        Returns
        - True when document end is present in the document
        """
        ...


    def getEventId(self) -> "Event.ID":
        """
        getter

        Returns
        - its identity
        """
        ...
