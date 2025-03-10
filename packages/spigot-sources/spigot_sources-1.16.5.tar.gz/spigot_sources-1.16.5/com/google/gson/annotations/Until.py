"""
Python module generated from Java source file com.google.gson.annotations.Until

Java source file obtained from artifact gson version 2.8.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.gson.annotations import *
from typing import Any, Callable, Iterable, Tuple


class Until:
    """
    An annotation that indicates the version number until a member or a type should be present.
    Basically, if Gson is created with a version number that exceeds the value stored in the
    `Until` annotation then the field will be ignored from the JSON output.  This annotation
    is useful to manage versioning of your JSON classes for a web-service.
    
    
    This annotation has no effect unless you build com.google.gson.Gson with a
    com.google.gson.GsonBuilder and invoke
    com.google.gson.GsonBuilder.setVersion(double) method.
    
    Here is an example of how this annotation is meant to be used:
    ```
    public class User {
      private String firstName;
      private String lastName;
      &#64Until(1.1) private String emailAddress;
      &#64Until(1.1) private String password;
    }
    ```
    
    If you created Gson with `new Gson()`, the `toJson()` and `fromJson()`
    methods will use all the fields for serialization and deserialization. However, if you created
    Gson with `Gson gson = new GsonBuilder().setVersion(1.2).create()` then the
    `toJson()` and `fromJson()` methods of Gson will exclude the `emailAddress`
    and `password` fields from the example above, because the version number passed to the 
    GsonBuilder, `1.2`, exceeds the version number set on the `Until` annotation,
    `1.1`, for those fields.

    Author(s)
    - Joel Leitch

    Since
    - 1.3
    """

    def value(self) -> float:
        """
        the value indicating a version number until this member
        or type should be ignored.
        """
        ...
