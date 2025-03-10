"""
Python module generated from Java source file com.google.common.collect.ForwardingConcurrentMap

Java source file obtained from artifact guava version 31.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.collect import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from java.util.concurrent import ConcurrentMap
from javax.annotation import CheckForNull
from typing import Any, Callable, Iterable, Tuple


class ForwardingConcurrentMap(ForwardingMap, ConcurrentMap):
    """
    A concurrent map which forwards all its method calls to another concurrent map. Subclasses should
    override one or more methods to modify the behavior of the backing map as desired per the <a
    href="http://en.wikipedia.org/wiki/Decorator_pattern">decorator pattern</a>.
    
    **`default` method warning:** This class forwards calls to *only some* `default` methods. Specifically, it forwards calls only for methods that existed <a
    href="https://docs.oracle.com/javase/7/docs/api/java/util/concurrent/ConcurrentMap.html">before
    `default` methods were introduced</a>. For newer methods, like `forEach`, it inherits
    their default implementations. When those implementations invoke methods, they invoke methods on
    the `ForwardingConcurrentMap`.

    Author(s)
    - Charles Fry

    Since
    - 2.0
    """

    def putIfAbsent(self, key: "K", value: "V") -> "V":
        ...


    def remove(self, key: "Object", value: "Object") -> bool:
        ...


    def replace(self, key: "K", value: "V") -> "V":
        ...


    def replace(self, key: "K", oldValue: "V", newValue: "V") -> bool:
        ...
