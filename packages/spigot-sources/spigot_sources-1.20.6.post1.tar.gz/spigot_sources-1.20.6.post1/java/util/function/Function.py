"""
Python module generated from Java source file java.util.function.Function

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util import Objects
from java.util.function import *
from typing import Any, Callable, Iterable, Tuple


class Function:
    """
    Represents a function that accepts one argument and produces a result.
    
    This is a <a href="package-summary.html">functional interface</a>
    whose functional method is .apply(Object).
    
    Type `<T>`: the type of the input to the function
    
    Type `<R>`: the type of the result of the function

    Since
    - 1.8
    """

    def apply(self, t: "T") -> "R":
        """
        Applies this function to the given argument.

        Arguments
        - t: the function argument

        Returns
        - the function result
        """
        ...


    def compose(self, before: "Function"["V", "T"]) -> "Function"["V", "R"]:
        """
        Returns a composed function that first applies the `before`
        function to its input, and then applies this function to the result.
        If evaluation of either function throws an exception, it is relayed to
        the caller of the composed function.
        
        Type `<V>`: the type of input to the `before` function, and to the
                  composed function

        Arguments
        - before: the function to apply before this function is applied

        Returns
        - a composed function that first applies the `before`
        function and then applies this function

        Raises
        - NullPointerException: if before is null

        See
        - .andThen(Function)
        """
        ...


    def andThen(self, after: "Function"["R", "V"]) -> "Function"["T", "V"]:
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

        See
        - .compose(Function)
        """
        ...


    @staticmethod
    def identity() -> "Function"["T", "T"]:
        """
        Returns a function that always returns its input argument.
        
        Type `<T>`: the type of the input and output objects to the function

        Returns
        - a function that always returns its input argument
        """
        ...
