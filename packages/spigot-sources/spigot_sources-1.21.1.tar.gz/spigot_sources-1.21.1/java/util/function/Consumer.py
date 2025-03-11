"""
Python module generated from Java source file java.util.function.Consumer

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util import Objects
from java.util.function import *
from typing import Any, Callable, Iterable, Tuple


class Consumer:
    """
    Represents an operation that accepts a single input argument and returns no
    result. Unlike most other functional interfaces, `Consumer` is expected
    to operate via side-effects.
    
    This is a <a href="package-summary.html">functional interface</a>
    whose functional method is .accept(Object).
    
    Type `<T>`: the type of the input to the operation

    Since
    - 1.8
    """

    def accept(self, t: "T") -> None:
        """
        Performs this operation on the given argument.

        Arguments
        - t: the input argument
        """
        ...


    def andThen(self, after: "Consumer"["T"]) -> "Consumer"["T"]:
        """
        Returns a composed `Consumer` that performs, in sequence, this
        operation followed by the `after` operation. If performing either
        operation throws an exception, it is relayed to the caller of the
        composed operation.  If performing this operation throws an exception,
        the `after` operation will not be performed.

        Arguments
        - after: the operation to perform after this operation

        Returns
        - a composed `Consumer` that performs in sequence this
        operation followed by the `after` operation

        Raises
        - NullPointerException: if `after` is null
        """
        ...
