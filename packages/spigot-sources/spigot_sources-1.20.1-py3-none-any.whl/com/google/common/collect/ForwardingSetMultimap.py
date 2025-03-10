"""
Python module generated from Java source file com.google.common.collect.ForwardingSetMultimap

Java source file obtained from artifact guava version 31.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.collect import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from javax.annotation import CheckForNull
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class ForwardingSetMultimap(ForwardingMultimap, SetMultimap):
    """
    A set multimap which forwards all its method calls to another set multimap. Subclasses should
    override one or more methods to modify the behavior of the backing multimap as desired per the <a
    href="http://en.wikipedia.org/wiki/Decorator_pattern">decorator pattern</a>.
    
    **`default` method warning:** This class does *not* forward calls to `default` methods. Instead, it inherits their default implementations. When those implementations
    invoke methods, they invoke methods on the `ForwardingSetMultimap`.

    Author(s)
    - Kurt Alfred Kluever

    Since
    - 3.0
    """

    def entries(self) -> set["Entry"["K", "V"]]:
        ...


    def get(self, key: "K") -> set["V"]:
        ...


    def removeAll(self, key: "Object") -> set["V"]:
        ...


    def replaceValues(self, key: "K", values: Iterable["V"]) -> set["V"]:
        ...
