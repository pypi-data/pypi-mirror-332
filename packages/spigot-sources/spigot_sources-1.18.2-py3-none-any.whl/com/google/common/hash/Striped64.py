"""
Python module generated from Java source file com.google.common.hash.Striped64

Java source file obtained from artifact guava version 31.0.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtIncompatible
from com.google.common.hash import *
from java.util import Random
from javax.annotation import CheckForNull
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class Striped64(Number):
    """
    A package-local class holding common representation and mechanics for classes supporting dynamic
    striping on 64bit values. The class extends Number so that concrete subclasses must publicly do
    so.
    """


