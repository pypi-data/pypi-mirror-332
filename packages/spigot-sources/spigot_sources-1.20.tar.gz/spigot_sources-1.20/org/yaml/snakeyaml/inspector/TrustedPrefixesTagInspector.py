"""
Python module generated from Java source file org.yaml.snakeyaml.inspector.TrustedPrefixesTagInspector

Java source file obtained from artifact snakeyaml version 2.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.yaml.snakeyaml.inspector import *
from org.yaml.snakeyaml.nodes import Tag
from typing import Any, Callable, Iterable, Tuple


class TrustedPrefixesTagInspector(TagInspector):
    """
    Allow to create classes with custom global tag if the class name matches any of the provided
    prefixes.
    """

    def __init__(self, trustedList: list[str]):
        """
        Create

        Arguments
        - trustedList: - list of prefixes to allow. It may be the package names
        """
        ...


    def isGlobalTagAllowed(self, tag: "Tag") -> bool:
        """
        Check

        Arguments
        - tag: - the global tag to allow

        Returns
        - True when the custom global tag is allowed to create a custom Java instance
        """
        ...
