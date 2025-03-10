"""
Python module generated from Java source file com.google.gson.annotations.Expose

Java source file obtained from artifact gson version 2.8.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.gson.annotations import *
from typing import Any, Callable, Iterable, Tuple


class Expose:
    """
    An annotation that indicates this member should be exposed for JSON
    serialization or deserialization.
    
    This annotation has no effect unless you build com.google.gson.Gson
    with a com.google.gson.GsonBuilder and invoke
    com.google.gson.GsonBuilder.excludeFieldsWithoutExposeAnnotation()
    method.
    
    Here is an example of how this annotation is meant to be used:
    ```
    public class User {
      &#64Expose private String firstName;
      &#64Expose(serialize = False) private String lastName;
      &#64Expose (serialize = False, deserialize = False) private String emailAddress;
      private String password;
    }
    ```
    If you created Gson with `new Gson()`, the `toJson()` and `fromJson()`
    methods will use the `password` field along-with `firstName`, `lastName`,
    and `emailAddress` for serialization and deserialization. However, if you created Gson
    with `Gson gson = new GsonBuilder().excludeFieldsWithoutExposeAnnotation().create()`
    then the `toJson()` and `fromJson()` methods of Gson will exclude the
    `password` field. This is because the `password` field is not marked with the
    `@Expose` annotation. Gson will also exclude `lastName` and `emailAddress`
    from serialization since `serialize` is set to `False`. Similarly, Gson will
    exclude `emailAddress` from deserialization since `deserialize` is set to False.
    
    Note that another way to achieve the same effect would have been to just mark the
    `password` field as `transient`, and Gson would have excluded it even with default
    settings. The `@Expose` annotation is useful in a style of programming where you want to
    explicitly specify all fields that should get considered for serialization or deserialization.

    Author(s)
    - Joel Leitch
    """

    def serialize(self) -> bool:
        """
        If `True`, the field marked with this annotation is written out in the JSON while
        serializing. If `False`, the field marked with this annotation is skipped from the
        serialized output. Defaults to `True`.

        Since
        - 1.4
        """
        return True


    def deserialize(self) -> bool:
        """
        If `True`, the field marked with this annotation is deserialized from the JSON.
        If `False`, the field marked with this annotation is skipped during deserialization. 
        Defaults to `True`.

        Since
        - 1.4
        """
        return True
