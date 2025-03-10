"""
Python module generated from Java source file org.yaml.snakeyaml.events.MappingStartEvent

Java source file obtained from artifact snakeyaml version 2.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.yaml.snakeyaml import DumperOptions
from org.yaml.snakeyaml.error import Mark
from org.yaml.snakeyaml.events import *
from typing import Any, Callable, Iterable, Tuple


class MappingStartEvent(CollectionStartEvent):
    """
    Marks the beginning of a mapping node.
    
    This event is followed by a number of key value pairs. 
    The pairs are not in any particular order. However, the value always directly follows the
    corresponding key. 
    After the key value pairs follows a MappingEndEvent.
    
    
    There must be an even number of node events between the start and end event.

    See
    - MappingEndEvent
    """

    def __init__(self, anchor: str, tag: str, implicit: bool, startMark: "Mark", endMark: "Mark", flowStyle: "DumperOptions.FlowStyle"):
        ...


    def getEventId(self) -> "Event.ID":
        """
        getter

        Returns
        - its identity
        """
        ...
