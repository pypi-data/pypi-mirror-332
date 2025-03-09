"""
Python module generated from Java source file com.google.common.collect.ForwardingSet

Java source file obtained from artifact guava version 32.1.2-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.collect import *
from javax.annotation import CheckForNull
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class ForwardingSet(ForwardingCollection, Set):
    """
    A set which forwards all its method calls to another set. Subclasses should override one or more
    methods to modify the behavior of the backing set as desired per the <a
    href="http://en.wikipedia.org/wiki/Decorator_pattern">decorator pattern</a>.
    
    **Warning:** The methods of `ForwardingSet` forward **indiscriminately** to the
    methods of the delegate. For example, overriding .add alone **will not** change the
    behavior of .addAll, which can lead to unexpected behavior. In this case, you should
    override `addAll` as well, either providing your own implementation, or delegating to the
    provided `standardAddAll` method.
    
    **`default` method warning:** This class does *not* forward calls to `default` methods. Instead, it inherits their default implementations. When those implementations
    invoke methods, they invoke methods on the `ForwardingSet`.
    
    The `standard` methods are not guaranteed to be thread-safe, even when all of the
    methods that they depend on are thread-safe.

    Author(s)
    - Louis Wasserman

    Since
    - 2.0
    """

    def equals(self, object: "Object") -> bool:
        ...


    def hashCode(self) -> int:
        ...
