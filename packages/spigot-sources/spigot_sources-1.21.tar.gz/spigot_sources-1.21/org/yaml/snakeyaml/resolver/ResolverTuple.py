"""
Python module generated from Java source file org.yaml.snakeyaml.resolver.ResolverTuple

Java source file obtained from artifact snakeyaml version 2.2

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util.regex import Pattern
from org.yaml.snakeyaml.nodes import Tag
from org.yaml.snakeyaml.resolver import *
from typing import Any, Callable, Iterable, Tuple


class ResolverTuple:

    def __init__(self, tag: "Tag", regexp: "Pattern", limit: int):
        ...


    def getTag(self) -> "Tag":
        ...


    def getRegexp(self) -> "Pattern":
        ...


    def getLimit(self) -> int:
        ...


    def toString(self) -> str:
        ...
