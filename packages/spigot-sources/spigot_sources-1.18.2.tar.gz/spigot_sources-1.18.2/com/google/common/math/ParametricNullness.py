"""
Python module generated from Java source file com.google.common.math.ParametricNullness

Java source file obtained from artifact guava version 31.0.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.math import *
from javax.annotation import Nonnull
from javax.annotation.meta import TypeQualifierNickname
from typing import Any, Callable, Iterable, Tuple


class ParametricNullness:
    """
    Marks a "top-level" type-variable usage as (a) a Kotlin platform type when the type argument is
    non-nullable and (b) nullable when the type argument is nullable. This is the closest we can get
    to "non-nullable when non-nullable; nullable when nullable" (like the Android <a
    href="https://android.googlesource.com/platform/libcore/+/master/luni/src/main/java/libcore/util/NullFromTypeParam.java">`NullFromTypeParam`</a>). We use this to "undo" ElementTypesAreNonnullByDefault.
    """


