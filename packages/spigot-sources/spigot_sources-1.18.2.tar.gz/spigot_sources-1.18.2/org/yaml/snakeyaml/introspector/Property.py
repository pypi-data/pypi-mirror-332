"""
Python module generated from Java source file org.yaml.snakeyaml.introspector.Property

Java source file obtained from artifact snakeyaml version 1.30

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.yaml.snakeyaml.introspector import *
from typing import Any, Callable, Iterable, Tuple


class Property(Comparable):
    """
    
    A `Property` represents a single member variable of a class,
    possibly including its accessor methods (getX, setX). The name stored in this
    class is the actual name of the property as given for the class, not an
    alias.
    
    
    
    Objects of this class have a total ordering which defaults to ordering based
    on the name of the property.
    """

    def __init__(self, name: str, type: type[Any]):
        ...


    def getType(self) -> type[Any]:
        ...


    def getActualTypeArguments(self) -> list[type[Any]]:
        ...


    def getName(self) -> str:
        ...


    def toString(self) -> str:
        ...


    def compareTo(self, o: "Property") -> int:
        ...


    def isWritable(self) -> bool:
        ...


    def isReadable(self) -> bool:
        ...


    def set(self, object: "Object", value: "Object") -> None:
        ...


    def get(self, object: "Object") -> "Object":
        ...


    def getAnnotations(self) -> list["Annotation"]:
        """
        Returns the annotations that are present on this property or empty `List` if there're no annotations.

        Returns
        - the annotations that are present on this property or empty `List` if there're no annotations
        """
        ...


    def getAnnotation(self, annotationType: type["A"]) -> "A":
        """
        Returns property's annotation for the given type or `null` if it's not present.
        
        Type `<A>`: class of the annotation

        Arguments
        - annotationType: the type of the annotation to be returned

        Returns
        - property's annotation for the given type or `null` if it's not present
        """
        ...


    def hashCode(self) -> int:
        ...


    def equals(self, other: "Object") -> bool:
        ...
