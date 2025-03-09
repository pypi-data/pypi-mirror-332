"""
Python module generated from Java source file com.google.common.base.Supplier

Java source file obtained from artifact guava version 32.1.2-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.base import *
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class Supplier(Supplier):
    """
    Legacy version of java.util.function.Supplier java.util.function.Supplier. Semantically,
    this could be a factory, generator, builder, closure, or something else entirely. No guarantees
    are implied by this interface.
    
    The Suppliers class provides common suppliers and related utilities.
    
    As this interface extends `java.util.function.Supplier`, an instance of this type can be
    used as a `java.util.function.Supplier` directly. To use a `java.util.function.Supplier` in a context where a `com.google.common.base.Supplier` is
    needed, use `supplier::get`.
    
    See the Guava User Guide article on <a
    href="https://github.com/google/guava/wiki/FunctionalExplained">the use of `Function`</a>.

    Author(s)
    - Harry Heymann

    Since
    - 2.0
    """

    def get(self) -> "T":
        """
        Retrieves an instance of the appropriate type. The returned object may or may not be a new
        instance, depending on the implementation.

        Returns
        - an instance of the appropriate type
        """
        ...
