"""
Python module generated from Java source file org.yaml.snakeyaml.inspector.UnTrustedTagInspector

Java source file obtained from artifact snakeyaml version 2.2

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.yaml.snakeyaml.inspector import *
from org.yaml.snakeyaml.nodes import Tag
from typing import Any, Callable, Iterable, Tuple


class UnTrustedTagInspector(TagInspector):
    """
    TagInspector which does not allow to create any custom instance. It should not be used when the
    data comes from untrusted source to prevent possible remote code invocation.
    """

    def isGlobalTagAllowed(self, tag: "Tag") -> bool:
        """
        Allow none

        Arguments
        - tag: - the global tag to reject

        Returns
        - always return False
        """
        ...
