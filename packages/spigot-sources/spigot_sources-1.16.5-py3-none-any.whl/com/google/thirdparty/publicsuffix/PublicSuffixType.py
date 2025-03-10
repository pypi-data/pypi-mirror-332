"""
Python module generated from Java source file com.google.thirdparty.publicsuffix.PublicSuffixType

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.thirdparty.publicsuffix import *
from enum import Enum
from typing import Any, Callable, Iterable, Tuple


class PublicSuffixType(Enum):
    """
    Specifies the type of a top-level domain definition.
    """

    PRIVATE = (':', ',')
    """
    private definition of a top-level domain
    """
    ICANN = ('!', '?')
    """
    ICANN definition of a top-level domain
    """
