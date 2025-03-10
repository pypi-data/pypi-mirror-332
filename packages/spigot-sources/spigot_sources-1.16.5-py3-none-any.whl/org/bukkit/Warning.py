"""
Python module generated from Java source file org.bukkit.Warning

Java source file obtained from artifact spigot-api version 1.16.5-R0.1-20210611.041013-99

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.collect import ImmutableMap
from org.bukkit import *
from typing import Any, Callable, Iterable, Tuple


class Warning:
    """
    This designates the warning state for a specific item.
    
    When the server settings dictate 'default' warnings, warnings are printed
    if the .value() is True.
    """

    def value(self) -> bool:
        """
        This sets if the deprecation warnings when registering events gets
        printed when the setting is in the default state.

        Returns
        - False normally, or True to encourage warning printout
        """
        return False


    def reason(self) -> str:
        """
        This can provide detailed information on why the event is deprecated.

        Returns
        - The reason an event is deprecated
        """
        return ""
