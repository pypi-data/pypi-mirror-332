"""
Python module generated from Java source file org.yaml.snakeyaml.events.ImplicitTuple

Java source file obtained from artifact snakeyaml version 2.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.yaml.snakeyaml.events import *
from typing import Any, Callable, Iterable, Tuple


class ImplicitTuple:
    """
    The implicit flag of a scalar event is a pair of boolean values that indicate if the tag may be
    omitted when the scalar is emitted in a plain and non-plain style correspondingly.

    See
    - <a href="http://pyyaml.org/wiki/PyYAMLDocumentation.Events">Events</a>
    """

    def __init__(self, plain: bool, nonplain: bool):
        """
        Create

        Arguments
        - plain: - True when tag can be omitted in plain
        - nonplain: - True when tag can be omitted in non-plain
        """
        ...


    def canOmitTagInPlainScalar(self) -> bool:
        """
        Returns
        - True when tag may be omitted when the scalar is emitted in a plain style.
        """
        ...


    def canOmitTagInNonPlainScalar(self) -> bool:
        """
        Returns
        - True when tag may be omitted when the scalar is emitted in a non-plain style.
        """
        ...


    def bothFalse(self) -> bool:
        """
        getter

        Returns
        - True when both are False
        """
        ...


    def toString(self) -> str:
        ...
