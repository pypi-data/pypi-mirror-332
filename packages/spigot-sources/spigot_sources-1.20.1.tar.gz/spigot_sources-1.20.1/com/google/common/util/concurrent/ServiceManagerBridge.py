"""
Python module generated from Java source file com.google.common.util.concurrent.ServiceManagerBridge

Java source file obtained from artifact guava version 31.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtIncompatible
from com.google.common.collect import ImmutableMultimap
from com.google.common.util.concurrent import *
from com.google.common.util.concurrent.Service import State
from typing import Any, Callable, Iterable, Tuple


class ServiceManagerBridge:
    """
    Superinterface of ServiceManager to introduce a bridge method for `servicesByState()`, to ensure binary compatibility with older Guava versions that specified
    `servicesByState()` to return `ImmutableMultimap`.
    """

    def servicesByState(self) -> "ImmutableMultimap"["State", "Service"]:
        ...
