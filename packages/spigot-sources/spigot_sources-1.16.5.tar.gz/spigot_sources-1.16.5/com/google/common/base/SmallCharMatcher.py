"""
Python module generated from Java source file com.google.common.base.SmallCharMatcher

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtIncompatible
from com.google.common.annotations import VisibleForTesting
from com.google.common.base import *
from com.google.common.base.CharMatcher import NamedFastMatcher
from java.util import BitSet
from typing import Any, Callable, Iterable, Tuple


class SmallCharMatcher(NamedFastMatcher):
    """
    An immutable version of CharMatcher for smallish sets of characters that uses a hash table with
    linear probing to check for matches.

    Author(s)
    - Christopher Swenson
    """

    def matches(self, c: str) -> bool:
        ...
