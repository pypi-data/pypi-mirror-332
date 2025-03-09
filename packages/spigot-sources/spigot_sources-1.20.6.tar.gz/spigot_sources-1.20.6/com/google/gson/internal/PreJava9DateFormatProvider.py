"""
Python module generated from Java source file com.google.gson.internal.PreJava9DateFormatProvider

Java source file obtained from artifact gson version 2.10.1

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.gson.internal import *
from java.text import DateFormat
from java.text import SimpleDateFormat
from java.util import Locale
from typing import Any, Callable, Iterable, Tuple


class PreJava9DateFormatProvider:
    """
    Provides DateFormats for US locale with patterns which were the default ones before Java 9.
    """

    @staticmethod
    def getUSDateFormat(style: int) -> "DateFormat":
        """
        Returns the same DateFormat as `DateFormat.getDateInstance(style, Locale.US)` in Java 8 or below.
        """
        ...


    @staticmethod
    def getUSDateTimeFormat(dateStyle: int, timeStyle: int) -> "DateFormat":
        """
        Returns the same DateFormat as `DateFormat.getDateTimeInstance(dateStyle, timeStyle, Locale.US)`
        in Java 8 or below.
        """
        ...
