"""
Python module generated from Java source file com.google.gson.internal.$Gson$Preconditions

Java source file obtained from artifact gson version 2.8.9

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.gson.internal import *
from typing import Any, Callable, Iterable, Tuple


class $Gson$Preconditions:
    """
    A simple utility class used to check method Preconditions.
    
    ```
    public long divideBy(long value) {
      Preconditions.checkArgument(value != 0);
      return this.value / value;
    }
    ```

    Author(s)
    - Joel Leitch
    """

    @staticmethod
    def checkNotNull(obj: "T") -> "T":
        ...


    @staticmethod
    def checkArgument(condition: bool) -> None:
        ...
