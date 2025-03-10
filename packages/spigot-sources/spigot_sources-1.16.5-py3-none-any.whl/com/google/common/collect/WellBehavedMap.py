"""
Python module generated from Java source file com.google.common.collect.WellBehavedMap

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.collect import *
from com.google.j2objc.annotations import WeakOuter
from java.util import Iterator
from typing import Any, Callable, Iterable, Tuple


class WellBehavedMap(ForwardingMap):
    """
    Workaround for
    <a href="http://bugs.sun.com/bugdatabase/view_bug.do?bug_id=6312706">
    EnumMap bug</a>. If you want to pass an `EnumMap`, with the
    intention of using its `entrySet()` method, you should
    wrap the `EnumMap` in this class instead.
    
    This class is not thread-safe even if the underlying map is.

    Author(s)
    - Dimitris Andreou
    """

    def entrySet(self) -> set["Entry"["K", "V"]]:
        ...
