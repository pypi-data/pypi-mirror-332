"""
Python module generated from Java source file org.yaml.snakeyaml.util.EnumUtils

Java source file obtained from artifact snakeyaml version 1.30

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.yaml.snakeyaml.util import *
from typing import Any, Callable, Iterable, Tuple


class EnumUtils:

    @staticmethod
    def findEnumInsensitiveCase(enumType: type["T"], name: str) -> "T":
        """
        Looks for an enumeration constant that matches the string without being case sensitive
        
        Type `<T>`: - the enum type whose constant is to be returned

        Arguments
        - enumType: - the Class object of the enum type from which to return a constant
        - name: - the name of the constant to return

        Returns
        - the enum constant of the specified enum type with the specified name, insensitive to case

        Raises
        - IllegalArgumentException: – if the specified enum type has no constant with the specified name, insensitive case
        """
        ...
