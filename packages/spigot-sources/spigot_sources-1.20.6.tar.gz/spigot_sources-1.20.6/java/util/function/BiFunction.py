"""
Python module generated from Java source file java.util.function.BiFunction

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util import Objects
from java.util.function import *
from typing import Any, Callable, Iterable, Tuple


class BiFunction:
    """
    Represents a function that accepts two arguments and produces a result.
    This is the two-arity specialization of Function.
    
    This is a <a href="package-summary.html">functional interface</a>
    whose functional method is .apply(Object, Object).
    
    Type `<T>`: the type of the first argument to the function
    
    Type `<U>`: the type of the second argument to the function
    
    Type `<R>`: the type of the result of the function

    See
    - Function

    Since
    - 1.8
    """

    def apply(self, t: "T", u: "U") -> "R":
        """
        Applies this function to the given arguments.

        Arguments
        - t: the first function argument
        - u: the second function argument

        Returns
        - the function result
        """
        ...


    def andThen(self, after: "Function"["R", "V"]) -> "BiFunction"["T", "U", "V"]:
        """
        Returns a composed function that first applies this function to
        its input, and then applies the `after` function to the result.
        If evaluation of either function throws an exception, it is relayed to
        the caller of the composed function.
        
        Type `<V>`: the type of output of the `after` function, and of the
                  composed function

        Arguments
        - after: the function to apply after this function is applied

        Returns
        - a composed function that first applies this function and then
        applies the `after` function

        Raises
        - NullPointerException: if after is null
        """
        ...
