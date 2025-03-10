"""
Python module generated from Java source file org.yaml.snakeyaml.events.CollectionEndEvent

Java source file obtained from artifact snakeyaml version 1.28

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.yaml.snakeyaml.error import Mark
from org.yaml.snakeyaml.events import *
from typing import Any, Callable, Iterable, Tuple


class CollectionEndEvent(Event):
    """
    Base class for the end events of the collection nodes.
    """

    def __init__(self, startMark: "Mark", endMark: "Mark"):
        ...
