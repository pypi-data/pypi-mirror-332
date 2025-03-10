"""
Python module generated from Java source file com.google.common.collect.FilteredMultimap

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.base import Predicate
from com.google.common.collect import *
from typing import Any, Callable, Iterable, Tuple


class FilteredMultimap(Multimap):
    """
    An interface for all filtered multimap types.

    Author(s)
    - Louis Wasserman
    """

    def unfiltered(self) -> "Multimap"["K", "V"]:
        ...


    def entryPredicate(self) -> "Predicate"["Entry"["K", "V"]]:
        ...
