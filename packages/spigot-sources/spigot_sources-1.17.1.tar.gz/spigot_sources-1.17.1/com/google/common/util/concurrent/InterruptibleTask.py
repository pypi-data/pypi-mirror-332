"""
Python module generated from Java source file com.google.common.util.concurrent.InterruptibleTask

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.util.concurrent import *
from java.util.concurrent.atomic import AtomicReferenceFieldUpdater
from typing import Any, Callable, Iterable, Tuple


class InterruptibleTask(Runnable):

    def run(self) -> None:
        ...
