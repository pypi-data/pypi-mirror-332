"""
Python module generated from Java source file org.yaml.snakeyaml.parser.ParserImpl

Java source file obtained from artifact snakeyaml version 1.33

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.yaml.snakeyaml import DumperOptions
from org.yaml.snakeyaml.DumperOptions import Version
from org.yaml.snakeyaml import LoaderOptions
from org.yaml.snakeyaml.comments import CommentType
from org.yaml.snakeyaml.error import Mark
from org.yaml.snakeyaml.error import YAMLException
from org.yaml.snakeyaml.events import AliasEvent
from org.yaml.snakeyaml.events import CommentEvent
from org.yaml.snakeyaml.events import DocumentEndEvent
from org.yaml.snakeyaml.events import DocumentStartEvent
from org.yaml.snakeyaml.events import Event
from org.yaml.snakeyaml.events import ImplicitTuple
from org.yaml.snakeyaml.events import MappingEndEvent
from org.yaml.snakeyaml.events import MappingStartEvent
from org.yaml.snakeyaml.events import ScalarEvent
from org.yaml.snakeyaml.events import SequenceEndEvent
from org.yaml.snakeyaml.events import SequenceStartEvent
from org.yaml.snakeyaml.events import StreamEndEvent
from org.yaml.snakeyaml.events import StreamStartEvent
from org.yaml.snakeyaml.nodes import Tag
from org.yaml.snakeyaml.parser import *
from org.yaml.snakeyaml.reader import StreamReader
from org.yaml.snakeyaml.scanner import Scanner
from org.yaml.snakeyaml.scanner import ScannerImpl
from org.yaml.snakeyaml.tokens import AliasToken
from org.yaml.snakeyaml.tokens import AnchorToken
from org.yaml.snakeyaml.tokens import BlockEntryToken
from org.yaml.snakeyaml.tokens import CommentToken
from org.yaml.snakeyaml.tokens import DirectiveToken
from org.yaml.snakeyaml.tokens import ScalarToken
from org.yaml.snakeyaml.tokens import StreamEndToken
from org.yaml.snakeyaml.tokens import StreamStartToken
from org.yaml.snakeyaml.tokens import TagToken
from org.yaml.snakeyaml.tokens import TagTuple
from org.yaml.snakeyaml.tokens import Token
from org.yaml.snakeyaml.util import ArrayStack
from typing import Any, Callable, Iterable, Tuple


class ParserImpl(Parser):
    """
    ```
    # The following YAML grammar is LL(1) and is parsed by a recursive descent
    parser.
    stream            ::= STREAM-START implicit_document? explicit_document* STREAM-END
    implicit_document ::= block_node DOCUMENT-END*
    explicit_document ::= DIRECTIVE* DOCUMENT-START block_node? DOCUMENT-END*
    block_node_or_indentless_sequence ::=
                          ALIAS
                          | properties (block_content | indentless_block_sequence)?
                          | block_content
                          | indentless_block_sequence
    block_node        ::= ALIAS
                          | properties block_content?
                          | block_content
    flow_node         ::= ALIAS
                          | properties flow_content?
                          | flow_content
    properties        ::= TAG ANCHOR? | ANCHOR TAG?
    block_content     ::= block_collection | flow_collection | SCALAR
    flow_content      ::= flow_collection | SCALAR
    block_collection  ::= block_sequence | block_mapping
    flow_collection   ::= flow_sequence | flow_mapping
    block_sequence    ::= BLOCK-SEQUENCE-START (BLOCK-ENTRY block_node?)* BLOCK-END
    indentless_sequence   ::= (BLOCK-ENTRY block_node?)+
    block_mapping     ::= BLOCK-MAPPING_START
                          ((KEY block_node_or_indentless_sequence?)?
                          (VALUE block_node_or_indentless_sequence?)?)*
                          BLOCK-END
    flow_sequence     ::= FLOW-SEQUENCE-START
                          (flow_sequence_entry FLOW-ENTRY)*
                          flow_sequence_entry?
                          FLOW-SEQUENCE-END
    flow_sequence_entry   ::= flow_node | KEY flow_node? (VALUE flow_node?)?
    flow_mapping      ::= FLOW-MAPPING-START
                          (flow_mapping_entry FLOW-ENTRY)*
                          flow_mapping_entry?
                          FLOW-MAPPING-END
    flow_mapping_entry    ::= flow_node | KEY flow_node? (VALUE flow_node?)?
    FIRST sets:
    stream: { STREAM-START }
    explicit_document: { DIRECTIVE DOCUMENT-START }
    implicit_document: FIRST(block_node)
    block_node: { ALIAS TAG ANCHOR SCALAR BLOCK-SEQUENCE-START BLOCK-MAPPING-START FLOW-SEQUENCE-START FLOW-MAPPING-START }
    flow_node: { ALIAS ANCHOR TAG SCALAR FLOW-SEQUENCE-START FLOW-MAPPING-START }
    block_content: { BLOCK-SEQUENCE-START BLOCK-MAPPING-START FLOW-SEQUENCE-START FLOW-MAPPING-START SCALAR }
    flow_content: { FLOW-SEQUENCE-START FLOW-MAPPING-START SCALAR }
    block_collection: { BLOCK-SEQUENCE-START BLOCK-MAPPING-START }
    flow_collection: { FLOW-SEQUENCE-START FLOW-MAPPING-START }
    block_sequence: { BLOCK-SEQUENCE-START }
    block_mapping: { BLOCK-MAPPING-START }
    block_node_or_indentless_sequence: { ALIAS ANCHOR TAG SCALAR BLOCK-SEQUENCE-START BLOCK-MAPPING-START FLOW-SEQUENCE-START FLOW-MAPPING-START BLOCK-ENTRY }
    indentless_sequence: { ENTRY }
    flow_collection: { FLOW-SEQUENCE-START FLOW-MAPPING-START }
    flow_sequence: { FLOW-SEQUENCE-START }
    flow_mapping: { FLOW-MAPPING-START }
    flow_sequence_entry: { ALIAS ANCHOR TAG SCALAR FLOW-SEQUENCE-START FLOW-MAPPING-START KEY }
    flow_mapping_entry: { ALIAS ANCHOR TAG SCALAR FLOW-SEQUENCE-START FLOW-MAPPING-START KEY }
    ```
    
    Since writing a recursive-descendant parser is a straightforward task, we do not give many
    comments here.
    """

    def __init__(self, reader: "StreamReader"):
        """
        Create

        Arguments
        - reader: - input

        Deprecated
        - use options
        """
        ...


    def __init__(self, reader: "StreamReader", parseComments: bool):
        """
        Create

        Arguments
        - reader: - input
        - parseComments: - True to keep the comments

        Deprecated
        - use options instead
        """
        ...


    def __init__(self, reader: "StreamReader", options: "LoaderOptions"):
        ...


    def __init__(self, scanner: "Scanner"):
        ...


    def checkEvent(self, choice: "Event.ID") -> bool:
        """
        Check the type of the next event.
        """
        ...


    def peekEvent(self) -> "Event":
        """
        Get the next event.
        """
        ...


    def getEvent(self) -> "Event":
        """
        Get the next event and proceed further.
        """
        ...
