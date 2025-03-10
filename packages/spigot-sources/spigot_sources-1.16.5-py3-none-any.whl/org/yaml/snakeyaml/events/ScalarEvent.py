"""
Python module generated from Java source file org.yaml.snakeyaml.events.ScalarEvent

Java source file obtained from artifact snakeyaml version 1.27

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.yaml.snakeyaml import DumperOptions
from org.yaml.snakeyaml.error import Mark
from org.yaml.snakeyaml.events import *
from typing import Any, Callable, Iterable, Tuple


class ScalarEvent(NodeEvent):
    """
    Marks a scalar value.
    """

    def __init__(self, anchor: str, tag: str, implicit: "ImplicitTuple", value: str, startMark: "Mark", endMark: "Mark", style: "DumperOptions.ScalarStyle"):
        ...


    def __init__(self, anchor: str, tag: str, implicit: "ImplicitTuple", value: str, startMark: "Mark", endMark: "Mark", style: "Character"):
        ...


    def getTag(self) -> str:
        """
        Tag of this scalar.

        Returns
        - The tag of this scalar, or `null` if no explicit tag
                is available.
        """
        ...


    def getScalarStyle(self) -> "DumperOptions.ScalarStyle":
        """
        Style of the scalar.
        <dl>
        <dt>null</dt>
        <dd>Flow Style - Plain</dd>
        <dt>'\''</dt>
        <dd>Flow Style - Single-Quoted</dd>
        <dt>'"'</dt>
        <dd>Flow Style - Double-Quoted</dd>
        <dt>'|'</dt>
        <dd>Block Style - Literal</dd>
        <dt>'&gt;'</dt>
        <dd>Block Style - Folded</dd>
        </dl>

        Returns
        - Style of the scalar.

        See
        - <a href="http://yaml.org/spec/1.1/.id864487">Kind/Style
             Combinations</a>
        """
        ...


    def getStyle(self) -> "Character":
        """
        Returns
        - char which is a value behind ScalarStyle

        Deprecated
        - use getScalarStyle()  instead
        """
        ...


    def getValue(self) -> str:
        """
        String representation of the value.
        
        Without quotes and escaping.

        Returns
        - Value as Unicode string.
        """
        ...


    def getImplicit(self) -> "ImplicitTuple":
        ...


    def getEventId(self) -> "Event.ID":
        ...


    def isPlain(self) -> bool:
        ...
