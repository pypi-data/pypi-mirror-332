"""
Python module generated from Java source file com.google.common.base.Function

Java source file obtained from artifact guava version 33.3.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.base import *
from javax.annotation import CheckForNull
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class Function(Function):
    """
    Legacy version of java.util.function.Function java.util.function.Function.
    
    The Functions class provides common functions and related utilities.
    
    As this interface extends `java.util.function.Function`, an instance of this type can be
    used as a `java.util.function.Function` directly. To use a `java.util.function.Function` in a context where a `com.google.common.base.Function` is
    needed, use `function::apply`.
    
    This interface is now a legacy type. Use `java.util.function.Function` (or the
    appropriate primitive specialization such as `ToIntFunction`) instead whenever possible.
    Otherwise, at least reduce *explicit* dependencies on this type by using lambda expressions
    or method references instead of classes, leaving your code easier to migrate in the future.
    
    See the Guava User Guide article on <a
    href="https://github.com/google/guava/wiki/FunctionalExplained">the use of `Function`</a>.

    Author(s)
    - Kevin Bourrillion

    Since
    - 2.0
    """

    def apply(self, input: "F") -> "T":
        ...


    def equals(self, object: "Object") -> bool:
        """
        *May* return `True` if `object` is a `Function` that behaves identically
        to this function.
        
        **Warning: do not depend** on the behavior of this method.
        
        Historically, `Function` instances in this library have implemented this method to
        recognize certain cases where distinct `Function` instances would in fact behave
        identically. However, as code migrates to `java.util.function`, that behavior will
        disappear. It is best not to depend on it.
        """
        ...
