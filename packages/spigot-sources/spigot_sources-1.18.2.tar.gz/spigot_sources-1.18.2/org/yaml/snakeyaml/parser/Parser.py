"""
Python module generated from Java source file org.yaml.snakeyaml.parser.Parser

Java source file obtained from artifact snakeyaml version 1.30

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.yaml.snakeyaml.events import Event
from org.yaml.snakeyaml.parser import *
from typing import Any, Callable, Iterable, Tuple


class Parser:
    """
    This interface represents an input stream of Event Events.
    
    The parser and the scanner form together the 'Parse' step in the loading
    process (see chapter 3.1 of the <a href="http://yaml.org/spec/1.1/">YAML
    Specification</a>).

    See
    - org.yaml.snakeyaml.events.Event
    """

    def checkEvent(self, choice: "Event.ID") -> bool:
        """
        Check if the next event is one of the given type.

        Arguments
        - choice: Event ID.

        Returns
        - `True` if the next event can be assigned to a variable
                of the given type. Returns `False` if no more events
                are available.

        Raises
        - ParserException: Thrown in case of malformed input.
        """
        ...


    def peekEvent(self) -> "Event":
        """
        Return the next event, but do not delete it from the stream.

        Returns
        - The event that will be returned on the next call to
                .getEvent

        Raises
        - ParserException: Thrown in case of malformed input.
        """
        ...


    def getEvent(self) -> "Event":
        """
        Returns the next event.
        
        The event will be removed from the stream.

        Returns
        - the next parsed event

        Raises
        - ParserException: Thrown in case of malformed input.
        """
        ...
