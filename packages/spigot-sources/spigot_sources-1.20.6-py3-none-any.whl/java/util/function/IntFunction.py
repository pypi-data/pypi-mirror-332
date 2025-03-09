"""
Python module generated from Java source file java.util.function.IntFunction

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util.function import *
from typing import Any, Callable, Iterable, Tuple


class IntFunction:
    """
    Represents a function that accepts an int-valued argument and produces a
    result.  This is the `int`-consuming primitive specialization for
    Function.
    
    This is a <a href="package-summary.html">functional interface</a>
    whose functional method is .apply(int).
    
    Type `<R>`: the type of the result of the function

    See
    - Function

    Since
    - 1.8
    """

    def apply(self, value: int) -> "R":
        """
        Applies this function to the given argument.

        Arguments
        - value: the function argument

        Returns
        - the function result
        """
        ...
