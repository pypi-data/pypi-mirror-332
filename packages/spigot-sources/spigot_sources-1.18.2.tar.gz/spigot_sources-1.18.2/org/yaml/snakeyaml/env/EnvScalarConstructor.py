"""
Python module generated from Java source file org.yaml.snakeyaml.env.EnvScalarConstructor

Java source file obtained from artifact snakeyaml version 1.30

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util.regex import Matcher
from java.util.regex import Pattern
from org.yaml.snakeyaml.constructor import AbstractConstruct
from org.yaml.snakeyaml.constructor import Constructor
from org.yaml.snakeyaml.env import *
from org.yaml.snakeyaml.error import MissingEnvironmentVariableException
from org.yaml.snakeyaml.nodes import Node
from org.yaml.snakeyaml.nodes import ScalarNode
from org.yaml.snakeyaml.nodes import Tag
from typing import Any, Callable, Iterable, Tuple


class EnvScalarConstructor(Constructor):
    """
    Construct scalar for format ${VARIABLE} replacing the template with the value from environment.

    See
    - <a href="https://docs.docker.com/compose/compose-file/.variable-substitution">Variable substitution</a>
    """

    ENV_TAG = Tag("!ENV")
    ENV_FORMAT = Pattern.compile("^\\$\\{\\s*((?<name>\\w+)((?<separator>:?(-|\\?))(?<value>\\S+)?)?)\\s*\\}$")


    def __init__(self):
        ...


    def apply(self, name: str, separator: str, value: str, environment: str) -> str:
        """
        Implement the logic for missing and unset variables

        Arguments
        - name: - variable name in the template
        - separator: - separator in the template, can be :-, -, :?, ?
        - value: - default value or the error in the template
        - environment: - the value from environment for the provided variable

        Returns
        - the value to apply in the template
        """
        ...


    def getEnv(self, key: str) -> str:
        """
        Get value of the environment variable

        Arguments
        - key: - the name of the variable

        Returns
        - value or null if not set
        """
        ...
