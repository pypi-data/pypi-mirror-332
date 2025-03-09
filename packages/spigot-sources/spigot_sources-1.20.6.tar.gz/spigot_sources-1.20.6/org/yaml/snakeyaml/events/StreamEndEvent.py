"""
Python module generated from Java source file org.yaml.snakeyaml.events.StreamEndEvent

Java source file obtained from artifact snakeyaml version 2.2

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.yaml.snakeyaml.error import Mark
from org.yaml.snakeyaml.events import *
from typing import Any, Callable, Iterable, Tuple


class StreamEndEvent(Event):
    """
    Marks the end of a stream that might have contained multiple documents.
    
    This event is the last event that a parser emits. Together with StreamStartEvent (which
    is the first event a parser emits) they mark the beginning and the end of a stream of documents.
    
    
    See Event for an exemplary output.
    """

    def __init__(self, startMark: "Mark", endMark: "Mark"):
        ...


    def getEventId(self) -> "Event.ID":
        ...
