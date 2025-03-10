"""
Python module generated from Java source file com.google.common.util.concurrent.Partially

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.util.concurrent import *
from typing import Any, Callable, Iterable, Tuple


class Partially:
    """
    Outer class that exists solely to let us write `Partially.GwtIncompatible` instead of plain
    `GwtIncompatible`. This is more accurate for Futures.catching, which is available
    under GWT but with a slightly different signature.
    
    We can't use `PartiallyGwtIncompatible` because then the GWT compiler wouldn't recognize
    it as a `GwtIncompatible` annotation. And for `Futures.catching`, we need the GWT
    compiler to autostrip the normal server method in order to expose the special, inherited GWT
    version.
    """


