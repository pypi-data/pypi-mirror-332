"""
Python module generated from Java source file org.yaml.snakeyaml.emitter.Emitable

Java source file obtained from artifact snakeyaml version 1.33

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.io import IOException
from org.yaml.snakeyaml.emitter import *
from org.yaml.snakeyaml.events import Event
from typing import Any, Callable, Iterable, Tuple


class Emitable:
    """
    Drefine a way to serialize an event to output stream
    """

    def emit(self, event: "Event") -> None:
        """
        Push event to bytes

        Arguments
        - event: - the source

        Raises
        - IOException: if bytes bite
        """
        ...
