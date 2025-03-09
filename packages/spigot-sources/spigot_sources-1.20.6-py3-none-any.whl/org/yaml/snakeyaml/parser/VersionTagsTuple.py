"""
Python module generated from Java source file org.yaml.snakeyaml.parser.VersionTagsTuple

Java source file obtained from artifact snakeyaml version 2.2

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.yaml.snakeyaml.DumperOptions import Version
from org.yaml.snakeyaml.parser import *
from typing import Any, Callable, Iterable, Tuple


class VersionTagsTuple:
    """
    Store the internal state for directives
    """

    def __init__(self, version: "Version", tags: dict[str, str]):
        ...


    def getVersion(self) -> "Version":
        ...


    def getTags(self) -> dict[str, str]:
        ...


    def toString(self) -> str:
        ...
