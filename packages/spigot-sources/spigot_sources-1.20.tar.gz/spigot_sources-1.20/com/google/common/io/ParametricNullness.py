"""
Python module generated from Java source file com.google.common.io.ParametricNullness

Java source file obtained from artifact guava version 31.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.io import *
from typing import Any, Callable, Iterable, Tuple


class ParametricNullness:
    """
    Marks a "top-level" type-variable usage as the closest we can get to "non-nullable when
    non-nullable; nullable when nullable" (like the Android <a
    href="https://android.googlesource.com/platform/libcore/+/master/luni/src/main/java/libcore/util/NullFromTypeParam.java">`NullFromTypeParam`</a>).
    
    Consumers of this annotation include:
    
    
      - Kotlin, for which it makes the type-variable usage (a) a Kotlin platform type when the type
          argument is non-nullable and (b) nullable when the type argument is nullable. We use this
          to "undo" ElementTypesAreNonnullByDefault.
      - <a href="https://developers.google.com/j2objc">J2ObjC</a>
      - `NullPointerTester`, at least in the Android backport (where the type-use annotations
          `NullPointerTester` would need are not available) and in case of <a
          href="https://bugs.openjdk.java.net/browse/JDK-8202469">JDK-8202469</a>
    """


