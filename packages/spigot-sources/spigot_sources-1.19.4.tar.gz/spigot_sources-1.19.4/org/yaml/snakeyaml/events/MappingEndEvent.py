"""
Python module generated from Java source file org.yaml.snakeyaml.events.MappingEndEvent

Java source file obtained from artifact snakeyaml version 1.33

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.yaml.snakeyaml.error import Mark
from org.yaml.snakeyaml.events import *
from typing import Any, Callable, Iterable, Tuple


class MappingEndEvent(CollectionEndEvent):
    """
    Marks the end of a mapping node.

    See
    - MappingStartEvent
    """

    def __init__(self, startMark: "Mark", endMark: "Mark"):
        """
        Create

        Arguments
        - startMark: - start
        - endMark: - end
        """
        ...


    def getEventId(self) -> "Event.ID":
        """
        getter

        Returns
        - its identity
        """
        ...
