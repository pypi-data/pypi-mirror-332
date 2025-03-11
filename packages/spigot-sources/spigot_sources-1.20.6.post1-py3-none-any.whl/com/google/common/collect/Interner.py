"""
Python module generated from Java source file com.google.common.collect.Interner

Java source file obtained from artifact guava version 32.1.2-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtIncompatible
from com.google.common.annotations import J2ktIncompatible
from com.google.common.collect import *
from com.google.errorprone.annotations import DoNotMock
from typing import Any, Callable, Iterable, Tuple


class Interner:
    """
    Provides similar behavior to String.intern for any immutable type. Common implementations
    are available from the Interners class.
    
    Note that `String.intern()` has some well-known performance limitations, and should
    generally be avoided. Prefer Interners.newWeakInterner or another `Interner`
    implementation even for `String` interning.

    Author(s)
    - Kevin Bourrillion

    Since
    - 3.0
    """

    def intern(self, sample: "E") -> "E":
        """
        Chooses and returns the representative instance for any of a collection of instances that are
        equal to each other. If two Object.equals equal inputs are given to this method,
        both calls will return the same instance. That is, `intern(a).equals(a)` always holds,
        and `intern(a) == intern(b)` if and only if `a.equals(b)`. Note that `intern(a)` is permitted to return one instance now and a different instance later if the
        original interned instance was garbage-collected.
        
        **Warning:** do not use with mutable objects.

        Raises
        - NullPointerException: if `sample` is null
        """
        ...
