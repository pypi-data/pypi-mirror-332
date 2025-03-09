"""
Python module generated from Java source file org.yaml.snakeyaml.inspector.TagInspector

Java source file obtained from artifact snakeyaml version 2.2

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.yaml.snakeyaml.inspector import *
from org.yaml.snakeyaml.nodes import Tag
from typing import Any, Callable, Iterable, Tuple


class TagInspector:
    """
    Check if the global tags are allowed (the local tags are always allowed). It should control the
    classes to create to prevent possible remote code invocation when the data comes from untrusted
    source. The standard tags are always allowed (https://yaml.org/type/index.html)
    """

    def isGlobalTagAllowed(self, tag: "Tag") -> bool:
        """
        Check

        Arguments
        - tag: - the global tag to check

        Returns
        - True when the custom global tag is allowed to create a custom Java instance
        """
        ...
