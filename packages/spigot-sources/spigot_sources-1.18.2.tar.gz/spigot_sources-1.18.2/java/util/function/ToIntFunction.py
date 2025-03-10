"""
Python module generated from Java source file java.util.function.ToIntFunction

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util.function import *
from typing import Any, Callable, Iterable, Tuple


class ToIntFunction:
    """
    Represents a function that produces an int-valued result.  This is the
    `int`-producing primitive specialization for Function.
    
    This is a <a href="package-summary.html">functional interface</a>
    whose functional method is .applyAsInt(Object).
    
    Type `<T>`: the type of the input to the function

    See
    - Function

    Since
    - 1.8
    """

    def applyAsInt(self, value: "T") -> int:
        """
        Applies this function to the given argument.

        Arguments
        - value: the function argument

        Returns
        - the function result
        """
        ...
