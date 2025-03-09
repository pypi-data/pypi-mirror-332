"""
Python module generated from Java source file java.util.function.UnaryOperator

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util.function import *
from typing import Any, Callable, Iterable, Tuple


class UnaryOperator(Function):
    """
    Represents an operation on a single operand that produces a result of the
    same type as its operand.  This is a specialization of `Function` for
    the case where the operand and result are of the same type.
    
    This is a <a href="package-summary.html">functional interface</a>
    whose functional method is .apply(Object).
    
    Type `<T>`: the type of the operand and result of the operator

    See
    - Function

    Since
    - 1.8
    """

    @staticmethod
    def identity() -> "UnaryOperator"["T"]:
        """
        Returns a unary operator that always returns its input argument.
        
        Type `<T>`: the type of the input and output of the operator

        Returns
        - a unary operator that always returns its input argument
        """
        ...
