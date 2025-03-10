"""
Python module generated from Java source file org.yaml.snakeyaml.tokens.Token

Java source file obtained from artifact snakeyaml version 1.33

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.yaml.snakeyaml.error import Mark
from org.yaml.snakeyaml.error import YAMLException
from org.yaml.snakeyaml.tokens import *
from typing import Any, Callable, Iterable, Tuple


class Token:

    def __init__(self, startMark: "Mark", endMark: "Mark"):
        ...


    def getStartMark(self) -> "Mark":
        ...


    def getEndMark(self) -> "Mark":
        ...


    def getTokenId(self) -> "Token.ID":
        """
        For error reporting.

        Returns
        - ID of this token

        See
        - "class variable 'id' in PyYAML"
        """
        ...


    class ID(Enum):

        Alias = ("<alias>")
        Anchor = ("<anchor>")
        BlockEnd = ("<block end>")
        BlockEntry = ("-")
        BlockMappingStart = ("<block mapping start>")
        BlockSequenceStart = ("<block sequence start>")
        Directive = ("<directive>")
        DocumentEnd = ("<document end>")
        DocumentStart = ("<document start>")
        FlowEntry = (",")
        FlowMappingEnd = ("}")
        FlowMappingStart = ("{")
        FlowSequenceEnd = ("]")
        FlowSequenceStart = ("[")
        Key = ("?")
        Scalar = ("<scalar>")
        StreamEnd = ("<stream end>")
        StreamStart = ("<stream start>")
        Tag = ("<tag>")
        Value = (":")
        Whitespace = ("<whitespace>")
        Comment = ("#")
        Error = ("<error>")


        def toString(self) -> str:
            ...
