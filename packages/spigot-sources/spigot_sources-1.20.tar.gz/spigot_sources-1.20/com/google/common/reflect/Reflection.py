"""
Python module generated from Java source file com.google.common.reflect.Reflection

Java source file obtained from artifact guava version 31.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.reflect import *
from java.lang.reflect import InvocationHandler
from java.lang.reflect import Proxy
from typing import Any, Callable, Iterable, Tuple


class Reflection:
    """
    Static utilities relating to Java reflection.

    Since
    - 12.0
    """

    @staticmethod
    def getPackageName(clazz: type[Any]) -> str:
        """
        Returns the package name of `clazz` according to the Java Language Specification (section
        6.7). Unlike Class.getPackage, this method only parses the class name, without
        attempting to define the Package and hence load files.
        """
        ...


    @staticmethod
    def getPackageName(classFullName: str) -> str:
        """
        Returns the package name of `classFullName` according to the Java Language Specification
        (section 6.7). Unlike Class.getPackage, this method only parses the class name, without
        attempting to define the Package and hence load files.
        """
        ...


    @staticmethod
    def initialize(*classes: Tuple[type[Any], ...]) -> None:
        """
        Ensures that the given classes are initialized, as described in <a
        href="http://java.sun.com/docs/books/jls/third_edition/html/execution.html#12.4.2">JLS Section
        12.4.2</a>.
        
        WARNING: Normally it's a smell if a class needs to be explicitly initialized, because static
        state hurts system maintainability and testability. In cases when you have no choice while
        inter-operating with a legacy framework, this method helps to keep the code less ugly.

        Raises
        - ExceptionInInitializerError: if an exception is thrown during initialization of a class
        """
        ...


    @staticmethod
    def newProxy(interfaceType: type["T"], handler: "InvocationHandler") -> "T":
        """
        Returns a proxy instance that implements `interfaceType` by dispatching method
        invocations to `handler`. The class loader of `interfaceType` will be used to
        define the proxy class. To implement multiple interfaces or specify a class loader, use Proxy.newProxyInstance.

        Raises
        - IllegalArgumentException: if `interfaceType` does not specify the type of a Java
            interface
        """
        ...
