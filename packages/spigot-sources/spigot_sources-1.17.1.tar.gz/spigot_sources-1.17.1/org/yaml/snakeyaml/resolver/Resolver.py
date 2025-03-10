"""
Python module generated from Java source file org.yaml.snakeyaml.resolver.Resolver

Java source file obtained from artifact snakeyaml version 1.28

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util.regex import Pattern
from org.yaml.snakeyaml.nodes import NodeId
from org.yaml.snakeyaml.nodes import Tag
from org.yaml.snakeyaml.resolver import *
from typing import Any, Callable, Iterable, Tuple


class Resolver:
    """
    Resolver tries to detect a type by content (when the tag is implicit)
    """

    BOOL = Pattern.compile("^(?:yes|Yes|YES|no|No|NO|true|True|TRUE|false|False|FALSE|on|On|ON|off|Off|OFF)$")
    FLOAT = Pattern.compile("^([-+]?(\\.[0-9]+|[0-9_]+(\\.[0-9_]*)?)([eE][-+]?[0-9]+)?|[-+]?[0-9][0-9_]*(?::[0-5]?[0-9])+\\.[0-9_]*|[-+]?\\.(?:inf|Inf|INF)|\\.(?:nan|NaN|NAN))$")
    """
    The regular expression is taken from the 1.2 specification but '_'s are
    added to keep backwards compatibility
    """
    INT = Pattern.compile("^(?:[-+]?0b[0-1_]+|[-+]?0[0-7_]+|[-+]?(?:0|[1-9][0-9_]*)|[-+]?0x[0-9a-fA-F_]+|[-+]?[1-9][0-9_]*(?::[0-5]?[0-9])+)$")
    MERGE = Pattern.compile("^(?:<<)$")
    NULL = Pattern.compile("^(?:~|null|Null|NULL| )$")
    EMPTY = Pattern.compile("^$")
    TIMESTAMP = Pattern.compile("^(?:[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]|[0-9][0-9][0-9][0-9]-[0-9][0-9]?-[0-9][0-9]?(?:[Tt]|[ \t]+)[0-9][0-9]?:[0-9][0-9]:[0-9][0-9](?:\\.[0-9]*)?(?:[ \t]*(?:Z|[-+][0-9][0-9]?(?::[0-9][0-9])?))?)$")
    VALUE = Pattern.compile("^(?:=)$")
    YAML = Pattern.compile("^(?:!|&|\\*)$")


    def __init__(self):
        ...


    def addImplicitResolver(self, tag: "Tag", regexp: "Pattern", first: str) -> None:
        ...


    def resolve(self, kind: "NodeId", value: str, implicit: bool) -> "Tag":
        ...
