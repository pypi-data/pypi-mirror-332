"""
Python module generated from Java source file org.yaml.snakeyaml.resolver.ResolverTuple

Java source file obtained from artifact snakeyaml version 1.27

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util.regex import Pattern
from org.yaml.snakeyaml.nodes import Tag
from org.yaml.snakeyaml.resolver import *
from typing import Any, Callable, Iterable, Tuple


class ResolverTuple:

    def __init__(self, tag: "Tag", regexp: "Pattern"):
        ...


    def getTag(self) -> "Tag":
        ...


    def getRegexp(self) -> "Pattern":
        ...


    def toString(self) -> str:
        ...
