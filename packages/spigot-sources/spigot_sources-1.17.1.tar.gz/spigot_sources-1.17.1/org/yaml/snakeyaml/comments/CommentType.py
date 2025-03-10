"""
Python module generated from Java source file org.yaml.snakeyaml.comments.CommentType

Java source file obtained from artifact snakeyaml version 1.28

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.yaml.snakeyaml.comments import *
from typing import Any, Callable, Iterable, Tuple


class CommentType(Enum):
    """
    The type of a comment line.
    """

    BLANK_LINE = 0
    BLOCK = 1
    IN_LINE = 2
