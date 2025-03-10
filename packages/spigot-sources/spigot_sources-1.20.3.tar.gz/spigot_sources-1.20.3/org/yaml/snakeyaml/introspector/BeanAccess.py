"""
Python module generated from Java source file org.yaml.snakeyaml.introspector.BeanAccess

Java source file obtained from artifact snakeyaml version 2.2

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.yaml.snakeyaml.introspector import *
from typing import Any, Callable, Iterable, Tuple


class BeanAccess(Enum):
    """
    Control instance variables.
    """

    DEFAULT = 0
    """
    use JavaBean properties and public fields
    """
    FIELD = 1
    """
    use all declared fields (including inherited)
    """
    PROPERTY = 2
    """
    reserved
    """
