"""
Python module generated from Java source file org.yaml.snakeyaml.inspector.TrustedTagInspector

Java source file obtained from artifact snakeyaml version 2.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.yaml.snakeyaml.inspector import *
from org.yaml.snakeyaml.nodes import Tag
from typing import Any, Callable, Iterable, Tuple


class TrustedTagInspector(TagInspector):
    """
    TagInspector which allows to create any custom instance. Should not be used when the data comes
    from untrusted source to prevent possible remote code invocation.
    """

    def isGlobalTagAllowed(self, tag: "Tag") -> bool:
        """
        Allow any

        Arguments
        - tag: - the global tag to allow

        Returns
        - always return True
        """
        ...
