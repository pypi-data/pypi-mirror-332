"""
Python module generated from Java source file java.util.concurrent.locks.AbstractOwnableSynchronizer

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util.concurrent.locks import *
from typing import Any, Callable, Iterable, Tuple


class AbstractOwnableSynchronizer(Serializable):
    """
    A synchronizer that may be exclusively owned by a thread.  This
    class provides a basis for creating locks and related synchronizers
    that may entail a notion of ownership.  The
    `AbstractOwnableSynchronizer` class itself does not manage or
    use this information. However, subclasses and tools may use
    appropriately maintained values to help control and monitor access
    and provide diagnostics.

    Author(s)
    - Doug Lea

    Since
    - 1.6
    """


