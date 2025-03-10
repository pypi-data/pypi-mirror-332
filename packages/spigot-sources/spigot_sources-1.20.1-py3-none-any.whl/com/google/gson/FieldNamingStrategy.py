"""
Python module generated from Java source file com.google.gson.FieldNamingStrategy

Java source file obtained from artifact gson version 2.10

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.gson import *
from java.lang.reflect import Field
from typing import Any, Callable, Iterable, Tuple


class FieldNamingStrategy:
    """
    A mechanism for providing custom field naming in Gson. This allows the client code to translate
    field names into a particular convention that is not supported as a normal Java field
    declaration rules. For example, Java does not support "-" characters in a field name.

    Author(s)
    - Joel Leitch

    Since
    - 1.3
    """

    def translateName(self, f: "Field") -> str:
        """
        Translates the field name into its JSON field name representation.

        Arguments
        - f: the field object that we are translating

        Returns
        - the translated field name.

        Since
        - 1.3
        """
        ...
