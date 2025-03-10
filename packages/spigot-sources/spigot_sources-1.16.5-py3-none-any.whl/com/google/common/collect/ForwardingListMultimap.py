"""
Python module generated from Java source file com.google.common.collect.ForwardingListMultimap

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.collect import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from javax.annotation import Nullable
from typing import Any, Callable, Iterable, Tuple


class ForwardingListMultimap(ForwardingMultimap, ListMultimap):
    """
    A list multimap which forwards all its method calls to another list multimap.
    Subclasses should override one or more methods to modify the behavior of
    the backing multimap as desired per the <a
    href="http://en.wikipedia.org/wiki/Decorator_pattern">decorator pattern</a>.

    Author(s)
    - Kurt Alfred Kluever

    Since
    - 3.0
    """

    def get(self, key: "K") -> list["V"]:
        ...


    def removeAll(self, key: "Object") -> list["V"]:
        ...


    def replaceValues(self, key: "K", values: Iterable["V"]) -> list["V"]:
        ...
