"""
Python module generated from Java source file com.google.common.primitives.ElementTypesAreNonnullByDefault

Java source file obtained from artifact guava version 32.1.2-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.primitives import *
from javax.annotation import Nonnull
from javax.annotation.meta import TypeQualifierDefault
from typing import Any, Callable, Iterable, Tuple


class ElementTypesAreNonnullByDefault:
    """
    Marks all "top-level" types as non-null in a way that is recognized by Kotlin. Note that this
    unfortunately includes type-variable usages, so we also provide ParametricNullness to
    "undo" it as best we can.
    """


