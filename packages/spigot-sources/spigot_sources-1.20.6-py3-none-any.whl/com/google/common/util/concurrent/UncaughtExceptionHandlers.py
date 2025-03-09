"""
Python module generated from Java source file com.google.common.util.concurrent.UncaughtExceptionHandlers

Java source file obtained from artifact guava version 32.1.2-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtIncompatible
from com.google.common.annotations import J2ktIncompatible
from com.google.common.annotations import VisibleForTesting
from com.google.common.util.concurrent import *
from java.util import Locale
from typing import Any, Callable, Iterable, Tuple


class UncaughtExceptionHandlers:
    """
    Factories for UncaughtExceptionHandler instances.

    Author(s)
    - Gregory Kick

    Since
    - 8.0
    """

    @staticmethod
    def systemExit() -> "UncaughtExceptionHandler":
        """
        Returns an exception handler that exits the system. This is particularly useful for the main
        thread, which may start up other, non-daemon threads, but fail to fully initialize the
        application successfully.
        
        Example usage:
        
        ```
        public static void main(String[] args) {
          Thread.currentThread().setUncaughtExceptionHandler(UncaughtExceptionHandlers.systemExit());
          ...
        ```
        
        The returned handler logs any exception at severity `SEVERE` and then shuts down the
        process with an exit status of 1, indicating abnormal termination.
        """
        ...
