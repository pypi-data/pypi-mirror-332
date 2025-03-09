"""
Python module generated from Java source file java.util.function.BiConsumer

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util import Objects
from java.util.function import *
from typing import Any, Callable, Iterable, Tuple


class BiConsumer:
    """
    Represents an operation that accepts two input arguments and returns no
    result.  This is the two-arity specialization of Consumer.
    Unlike most other functional interfaces, `BiConsumer` is expected
    to operate via side-effects.
    
    This is a <a href="package-summary.html">functional interface</a>
    whose functional method is .accept(Object, Object).
    
    Type `<T>`: the type of the first argument to the operation
    
    Type `<U>`: the type of the second argument to the operation

    See
    - Consumer

    Since
    - 1.8
    """

    def accept(self, t: "T", u: "U") -> None:
        """
        Performs this operation on the given arguments.

        Arguments
        - t: the first input argument
        - u: the second input argument
        """
        ...


    def andThen(self, after: "BiConsumer"["T", "U"]) -> "BiConsumer"["T", "U"]:
        """
        Returns a composed `BiConsumer` that performs, in sequence, this
        operation followed by the `after` operation. If performing either
        operation throws an exception, it is relayed to the caller of the
        composed operation.  If performing this operation throws an exception,
        the `after` operation will not be performed.

        Arguments
        - after: the operation to perform after this operation

        Returns
        - a composed `BiConsumer` that performs in sequence this
        operation followed by the `after` operation

        Raises
        - NullPointerException: if `after` is null
        """
        ...
