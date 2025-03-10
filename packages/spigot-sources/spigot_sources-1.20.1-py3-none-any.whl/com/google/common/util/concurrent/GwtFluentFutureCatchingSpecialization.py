"""
Python module generated from Java source file com.google.common.util.concurrent.GwtFluentFutureCatchingSpecialization

Java source file obtained from artifact guava version 31.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.util.concurrent import *
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class GwtFluentFutureCatchingSpecialization(AbstractFuture):
    """
    Hidden superclass of FluentFuture that provides us a place to declare special GWT
    versions of the FluentFuture.catching(Class, com.google.common.base.Function)
    FluentFuture.catching family of methods. Those versions have slightly different signatures.
    """


