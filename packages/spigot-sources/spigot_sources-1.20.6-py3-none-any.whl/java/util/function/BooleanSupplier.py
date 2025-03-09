"""
Python module generated from Java source file java.util.function.BooleanSupplier

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util.function import *
from typing import Any, Callable, Iterable, Tuple


class BooleanSupplier:
    """
    Represents a supplier of `boolean`-valued results.  This is the
    `boolean`-producing primitive specialization of Supplier.
    
    There is no requirement that a new or distinct result be returned each
    time the supplier is invoked.
    
    This is a <a href="package-summary.html">functional interface</a>
    whose functional method is .getAsBoolean().

    See
    - Supplier

    Since
    - 1.8
    """

    def getAsBoolean(self) -> bool:
        """
        Gets a result.

        Returns
        - a result
        """
        ...
