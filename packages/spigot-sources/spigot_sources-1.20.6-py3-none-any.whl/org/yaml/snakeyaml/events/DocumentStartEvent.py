"""
Python module generated from Java source file org.yaml.snakeyaml.events.DocumentStartEvent

Java source file obtained from artifact snakeyaml version 2.2

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.yaml.snakeyaml.DumperOptions import Version
from org.yaml.snakeyaml.error import Mark
from org.yaml.snakeyaml.events import *
from typing import Any, Callable, Iterable, Tuple


class DocumentStartEvent(Event):
    """
    Marks the beginning of a document.
    
    This event followed by the document's content and a DocumentEndEvent.
    """

    def __init__(self, startMark: "Mark", endMark: "Mark", explicit: bool, version: "Version", tags: dict[str, str]):
        """
        Create

        Arguments
        - startMark: - start
        - endMark: - end
        - explicit: - True when it is present in the document
        - version: - YAML version
        - tags: - tag directives
        """
        ...


    def getExplicit(self) -> bool:
        """
        getter

        Returns
        - True when document end is present
        """
        ...


    def getVersion(self) -> "Version":
        """
        YAML version the document conforms to.

        Returns
        - `null`if the document has no explicit `%YAML` directive.
                Otherwise an array with two components, the major and minor part of the version (in
                this order).
        """
        ...


    def getTags(self) -> dict[str, str]:
        """
        Tag shorthands as defined by the `%TAG` directive.

        Returns
        - Mapping of 'handles' to 'prefixes' (the handles include the '!' characters).
        """
        ...


    def getEventId(self) -> "Event.ID":
        ...
