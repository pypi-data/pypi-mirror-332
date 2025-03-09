"""
Python module generated from Java source file org.yaml.snakeyaml.emitter.Emitter

Java source file obtained from artifact snakeyaml version 2.2

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.io import IOException
from java.io import Writer
from java.util import ArrayDeque
from java.util import Iterator
from java.util import Queue
from java.util.regex import Matcher
from java.util.regex import Pattern
from org.yaml.snakeyaml import DumperOptions
from org.yaml.snakeyaml.DumperOptions import ScalarStyle
from org.yaml.snakeyaml.DumperOptions import Version
from org.yaml.snakeyaml.comments import CommentEventsCollector
from org.yaml.snakeyaml.comments import CommentLine
from org.yaml.snakeyaml.comments import CommentType
from org.yaml.snakeyaml.emitter import *
from org.yaml.snakeyaml.error import YAMLException
from org.yaml.snakeyaml.events import AliasEvent
from org.yaml.snakeyaml.events import CollectionEndEvent
from org.yaml.snakeyaml.events import CollectionStartEvent
from org.yaml.snakeyaml.events import CommentEvent
from org.yaml.snakeyaml.events import DocumentEndEvent
from org.yaml.snakeyaml.events import DocumentStartEvent
from org.yaml.snakeyaml.events import Event
from org.yaml.snakeyaml.events.Event import ID
from org.yaml.snakeyaml.events import MappingEndEvent
from org.yaml.snakeyaml.events import MappingStartEvent
from org.yaml.snakeyaml.events import NodeEvent
from org.yaml.snakeyaml.events import ScalarEvent
from org.yaml.snakeyaml.events import SequenceEndEvent
from org.yaml.snakeyaml.events import SequenceStartEvent
from org.yaml.snakeyaml.events import StreamEndEvent
from org.yaml.snakeyaml.events import StreamStartEvent
from org.yaml.snakeyaml.nodes import Tag
from org.yaml.snakeyaml.reader import StreamReader
from org.yaml.snakeyaml.scanner import Constant
from org.yaml.snakeyaml.util import ArrayStack
from typing import Any, Callable, Iterable, Tuple


class Emitter(Emitable):
    """
    ```
    Emitter expects events obeying the following grammar:
    stream ::= STREAM-START document* STREAM-END
    document ::= DOCUMENT-START node DOCUMENT-END
    node ::= SCALAR | sequence | mapping
    sequence ::= SEQUENCE-START node* SEQUENCE-END
    mapping ::= MAPPING-START (node node)* MAPPING-END
    ```
    """

    MIN_INDENT = 1
    """
    indent cannot be zero spaces
    """
    MAX_INDENT = 10
    """
    indent should not be more than 10 spaces
    """


    def __init__(self, stream: "Writer", opts: "DumperOptions"):
        """
        Create

        Arguments
        - stream: - output to write to
        - opts: - options
        """
        ...


    def emit(self, event: "Event") -> None:
        ...
