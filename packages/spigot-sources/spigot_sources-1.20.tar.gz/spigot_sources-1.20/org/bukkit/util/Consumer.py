"""
Python module generated from Java source file org.bukkit.util.Consumer

Java source file obtained from artifact spigot-api version 1.20-R0.1-20230612.113428-32

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.util import *
from typing import Any, Callable, Iterable, Tuple


class Consumer:
    """
    Represents an operation that accepts a single input argument and returns no
    result.
    
    Type `<T>`: the type of the input to the operation
    """

    def accept(self, t: "T") -> None:
        """
        Performs this operation on the given argument.

        Arguments
        - t: the input argument
        """
        ...
