"""
Python module generated from Java source file org.yaml.snakeyaml.scanner.ScannerImpl

Java source file obtained from artifact snakeyaml version 2.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.nio.charset import CharacterCodingException
from java.util import Iterator
from java.util.regex import Pattern
from org.yaml.snakeyaml import DumperOptions
from org.yaml.snakeyaml import LoaderOptions
from org.yaml.snakeyaml.comments import CommentType
from org.yaml.snakeyaml.error import Mark
from org.yaml.snakeyaml.error import YAMLException
from org.yaml.snakeyaml.reader import StreamReader
from org.yaml.snakeyaml.scanner import *
from org.yaml.snakeyaml.tokens import AliasToken
from org.yaml.snakeyaml.tokens import AnchorToken
from org.yaml.snakeyaml.tokens import BlockEndToken
from org.yaml.snakeyaml.tokens import BlockEntryToken
from org.yaml.snakeyaml.tokens import BlockMappingStartToken
from org.yaml.snakeyaml.tokens import BlockSequenceStartToken
from org.yaml.snakeyaml.tokens import CommentToken
from org.yaml.snakeyaml.tokens import DirectiveToken
from org.yaml.snakeyaml.tokens import DocumentEndToken
from org.yaml.snakeyaml.tokens import DocumentStartToken
from org.yaml.snakeyaml.tokens import FlowEntryToken
from org.yaml.snakeyaml.tokens import FlowMappingEndToken
from org.yaml.snakeyaml.tokens import FlowMappingStartToken
from org.yaml.snakeyaml.tokens import FlowSequenceEndToken
from org.yaml.snakeyaml.tokens import FlowSequenceStartToken
from org.yaml.snakeyaml.tokens import KeyToken
from org.yaml.snakeyaml.tokens import ScalarToken
from org.yaml.snakeyaml.tokens import StreamEndToken
from org.yaml.snakeyaml.tokens import StreamStartToken
from org.yaml.snakeyaml.tokens import TagToken
from org.yaml.snakeyaml.tokens import TagTuple
from org.yaml.snakeyaml.tokens import Token
from org.yaml.snakeyaml.tokens import ValueToken
from org.yaml.snakeyaml.util import ArrayStack
from org.yaml.snakeyaml.util import UriEncoder
from typing import Any, Callable, Iterable, Tuple


class ScannerImpl(Scanner):
    """
    ```
    Scanner produces tokens of the following types:
    STREAM-START
    STREAM-END
    COMMENT
    DIRECTIVE(name, value)
    DOCUMENT-START
    DOCUMENT-END
    BLOCK-SEQUENCE-START
    BLOCK-MAPPING-START
    BLOCK-END
    FLOW-SEQUENCE-START
    FLOW-MAPPING-START
    FLOW-SEQUENCE-END
    FLOW-MAPPING-END
    BLOCK-ENTRY
    FLOW-ENTRY
    KEY
    VALUE
    ALIAS(value)
    ANCHOR(value)
    TAG(value)
    SCALAR(value, plain, style)
    Read comments in the Scanner code for more details.
    ```
    """

    ESCAPE_REPLACEMENTS = HashMap<Character, String>()
    """
    A mapping from an escaped character in the input stream to the string representation that they
    should be replaced with.
    
    YAML defines several common and a few uncommon escape sequences.

    See
    - <a href="http://www.yaml.org/spec/current.html.id2517668">4.1.6. Escape Sequences</a>
    """
    ESCAPE_CODES = HashMap<Character, Integer>()
    """
    A mapping from a character to a number of bytes to read-ahead for that escape sequence. These
    escape sequences are used to handle unicode escaping in the following formats, where H is a
    hexadecimal character:
    
    ```
    &#92;xHH         : escaped 8-bit Unicode character
    &#92;uHHHH       : escaped 16-bit Unicode character
    &#92;UHHHHHHHH   : escaped 32-bit Unicode character
    ```

    See
    - <a href="http://yaml.org/spec/1.1/current.html.id872840">5.6. Escape Sequences</a>
    """


    def __init__(self, reader: "StreamReader", options: "LoaderOptions"):
        ...


    def checkToken(self, *choices: Tuple["Token.ID", ...]) -> bool:
        """
        Check whether the next token is one of the given types.
        """
        ...


    def peekToken(self) -> "Token":
        """
        Return the next token, but do not delete it from the queue.
        """
        ...


    def getToken(self) -> "Token":
        """
        Return the next token, removing it from the queue.
        """
        ...
