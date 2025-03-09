"""
Python module generated from Java source file java.nio.charset.CodingErrorAction

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.nio.charset import *
from typing import Any, Callable, Iterable, Tuple


class CodingErrorAction:

    IGNORE = CodingErrorAction("IGNORE")
    """
    Action indicating that a coding error is to be handled by dropping the
    erroneous input and resuming the coding operation.
    """
    REPLACE = CodingErrorAction("REPLACE")
    """
    Action indicating that a coding error is to be handled by dropping the
    erroneous input, appending the coder's replacement value to the output
    buffer, and resuming the coding operation.
    """
    REPORT = CodingErrorAction("REPORT")
    """
    Action indicating that a coding error is to be reported, either by
    returning a CoderResult object or by throwing a CharacterCodingException, whichever is appropriate for the method
    implementing the coding process.
    """


    def toString(self) -> str:
        """
        Returns a string describing this action.

        Returns
        - A descriptive string
        """
        ...
