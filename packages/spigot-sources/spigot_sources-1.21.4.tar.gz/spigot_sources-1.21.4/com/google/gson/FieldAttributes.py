"""
Python module generated from Java source file com.google.gson.FieldAttributes

Java source file obtained from artifact gson version 2.11.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.gson import *
from java.lang.reflect import Field
from java.lang.reflect import Type
from java.util import Arrays
from java.util import Objects
from typing import Any, Callable, Iterable, Tuple


class FieldAttributes:
    """
    A data object that stores attributes of a field.
    
    This class is immutable; therefore, it can be safely shared across threads.

    Author(s)
    - Joel Leitch

    Since
    - 1.4
    """

    def __init__(self, f: "Field"):
        """
        Constructs a Field Attributes object from the `f`.

        Arguments
        - f: the field to pull attributes from
        """
        ...


    def getDeclaringClass(self) -> type[Any]:
        """
        Gets the declaring Class that contains this field

        Returns
        - the declaring class that contains this field
        """
        ...


    def getName(self) -> str:
        """
        Gets the name of the field

        Returns
        - the name of the field
        """
        ...


    def getDeclaredType(self) -> "Type":
        """
        Returns the declared generic type of the field.
        
        For example, assume the following class definition:
        
        <pre class="code">
        public class Foo {
          private String bar;
          private List&lt;String&gt; red;
        }
        
        Type listParameterizedType = new TypeToken&lt;List&lt;String&gt;&gt;() {}.getType();
        ```
        
        This method would return `String.class` for the `bar` field and `listParameterizedType` for the `red` field.

        Returns
        - the specific type declared for this field
        """
        ...


    def getDeclaredClass(self) -> type[Any]:
        """
        Returns the `Class` object that was declared for this field.
        
        For example, assume the following class definition:
        
        <pre class="code">
        public class Foo {
          private String bar;
          private List&lt;String&gt; red;
        }
        ```
        
        This method would return `String.class` for the `bar` field and `List.class` for the `red` field.

        Returns
        - the specific class object that was declared for the field
        """
        ...


    def getAnnotation(self, annotation: type["T"]) -> "T":
        """
        Returns the `T` annotation object from this field if it exists; otherwise returns `null`.

        Arguments
        - annotation: the class of the annotation that will be retrieved

        Returns
        - the annotation instance if it is bound to the field; otherwise `null`
        """
        ...


    def getAnnotations(self) -> Iterable["Annotation"]:
        """
        Returns the annotations that are present on this field.

        Returns
        - an array of all the annotations set on the field

        Since
        - 1.4
        """
        ...


    def hasModifier(self, modifier: int) -> bool:
        """
        Returns `True` if the field is defined with the `modifier`.
        
        This method is meant to be called as:
        
        <pre class="code">
        boolean hasPublicModifier = fieldAttribute.hasModifier(java.lang.reflect.Modifier.PUBLIC);
        ```

        See
        - java.lang.reflect.Modifier
        """
        ...


    def toString(self) -> str:
        ...
