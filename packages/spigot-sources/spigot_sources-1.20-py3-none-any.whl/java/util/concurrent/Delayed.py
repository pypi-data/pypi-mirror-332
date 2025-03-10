"""
Python module generated from Java source file java.util.concurrent.Delayed

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util.concurrent import *
from typing import Any, Callable, Iterable, Tuple


class Delayed(Comparable):
    """
    A mix-in style interface for marking objects that should be
    acted upon after a given delay.
    
    An implementation of this interface must define a
    `compareTo` method that provides an ordering consistent with
    its `getDelay` method.

    Author(s)
    - Doug Lea

    Since
    - 1.5
    """

    def getDelay(self, unit: "TimeUnit") -> int:
        """
        Returns the remaining delay associated with this object, in the
        given time unit.

        Arguments
        - unit: the time unit

        Returns
        - the remaining delay; zero or negative values indicate
        that the delay has already elapsed
        """
        ...
