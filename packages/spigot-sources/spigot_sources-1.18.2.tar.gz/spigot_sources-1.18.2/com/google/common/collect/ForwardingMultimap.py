"""
Python module generated from Java source file com.google.common.collect.ForwardingMultimap

Java source file obtained from artifact guava version 31.0.1-jre

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


class ForwardingMultimap(ForwardingObject, Multimap):
    """
    A multimap which forwards all its method calls to another multimap. Subclasses should override
    one or more methods to modify the behavior of the backing multimap as desired per the <a
    href="http://en.wikipedia.org/wiki/Decorator_pattern">decorator pattern</a>.
    
    **`default` method warning:** This class does *not* forward calls to `default` methods. Instead, it inherits their default implementations. When those implementations
    invoke methods, they invoke methods on the `ForwardingMultimap`.

    Author(s)
    - Robert Konigsberg

    Since
    - 2.0
    """

    def asMap(self) -> dict["K", Iterable["V"]]:
        ...


    def clear(self) -> None:
        ...


    def containsEntry(self, key: "Object", value: "Object") -> bool:
        ...


    def containsKey(self, key: "Object") -> bool:
        ...


    def containsValue(self, value: "Object") -> bool:
        ...


    def entries(self) -> Iterable["Entry"["K", "V"]]:
        ...


    def get(self, key: "K") -> Iterable["V"]:
        ...


    def isEmpty(self) -> bool:
        ...


    def keys(self) -> "Multiset"["K"]:
        ...


    def keySet(self) -> set["K"]:
        ...


    def put(self, key: "K", value: "V") -> bool:
        ...


    def putAll(self, key: "K", values: Iterable["V"]) -> bool:
        ...


    def putAll(self, multimap: "Multimap"["K", "V"]) -> bool:
        ...


    def remove(self, key: "Object", value: "Object") -> bool:
        ...


    def removeAll(self, key: "Object") -> Iterable["V"]:
        ...


    def replaceValues(self, key: "K", values: Iterable["V"]) -> Iterable["V"]:
        ...


    def size(self) -> int:
        ...


    def values(self) -> Iterable["V"]:
        ...


    def equals(self, object: "Object") -> bool:
        ...


    def hashCode(self) -> int:
        ...
