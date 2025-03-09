"""
Python module generated from Java source file java.util.function.Supplier

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util.function import *
from typing import Any, Callable, Iterable, Tuple


class Supplier:
    """
    Represents a supplier of results.
    
    There is no requirement that a new or distinct result be returned each
    time the supplier is invoked.
    
    This is a <a href="package-summary.html">functional interface</a>
    whose functional method is .get().
    
    Type `<T>`: the type of results supplied by this supplier

    Since
    - 1.8
    """

    def get(self) -> "T":
        """
        Gets a result.

        Returns
        - a result
        """
        ...
