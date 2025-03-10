"""
Python module generated from Java source file org.yaml.snakeyaml.constructor.CustomClassLoaderConstructor

Java source file obtained from artifact snakeyaml version 2.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.yaml.snakeyaml import LoaderOptions
from org.yaml.snakeyaml.constructor import *
from typing import Any, Callable, Iterable, Tuple


class CustomClassLoaderConstructor(Constructor):
    """
    Construct instances with a custom Class Loader.
    """

    def __init__(self, loader: "ClassLoader", loadingConfig: "LoaderOptions"):
        """
        Create

        Arguments
        - loader: - the class loader to find the class definition
        - loadingConfig: - options
        """
        ...


    def __init__(self, theRoot: type["Object"], theLoader: "ClassLoader", loadingConfig: "LoaderOptions"):
        """
        Create

        Arguments
        - loadingConfig: - options
        - theRoot: - the class to instantiate
        - theLoader: - the class loader to find the class definition
        """
        ...
