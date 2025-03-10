"""
Python module generated from Java source file java.util.function.ObjIntConsumer

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util.function import *
from typing import Any, Callable, Iterable, Tuple


class ObjIntConsumer:
    """
    Represents an operation that accepts an object-valued and a
    `int`-valued argument, and returns no result.  This is the
    `(reference, int)` specialization of BiConsumer.
    Unlike most other functional interfaces, `ObjIntConsumer` is
    expected to operate via side-effects.
    
    This is a <a href="package-summary.html">functional interface</a>
    whose functional method is .accept(Object, int).
    
    Type `<T>`: the type of the object argument to the operation

    See
    - BiConsumer

    Since
    - 1.8
    """

    def accept(self, t: "T", value: int) -> None:
        """
        Performs this operation on the given arguments.

        Arguments
        - t: the first input argument
        - value: the second input argument
        """
        ...
