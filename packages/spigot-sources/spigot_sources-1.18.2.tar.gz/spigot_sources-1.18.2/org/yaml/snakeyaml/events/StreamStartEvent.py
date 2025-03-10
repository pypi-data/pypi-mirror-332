"""
Python module generated from Java source file org.yaml.snakeyaml.events.StreamStartEvent

Java source file obtained from artifact snakeyaml version 1.30

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.yaml.snakeyaml.error import Mark
from org.yaml.snakeyaml.events import *
from typing import Any, Callable, Iterable, Tuple


class StreamStartEvent(Event):
    """
    Marks the start of a stream that might contain multiple documents.
    
    This event is the first event that a parser emits. Together with
    StreamEndEvent (which is the last event a parser emits) they mark the
    beginning and the end of a stream of documents.
    
    
    See Event for an exemplary output.
    """

    def __init__(self, startMark: "Mark", endMark: "Mark"):
        ...


    def getEventId(self) -> "Event.ID":
        ...
