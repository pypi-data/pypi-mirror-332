"""
Python module generated from Java source file com.google.gson.annotations.Since

Java source file obtained from artifact gson version 2.8.9

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.gson.annotations import *
from typing import Any, Callable, Iterable, Tuple


class Since:
    """
    An annotation that indicates the version number since a member or a type has been present.
    This annotation is useful to manage versioning of your Json classes for a web-service.
    
    
    This annotation has no effect unless you build com.google.gson.Gson with a
    com.google.gson.GsonBuilder and invoke
    com.google.gson.GsonBuilder.setVersion(double) method.
    
    Here is an example of how this annotation is meant to be used:
    ```
    public class User {
      private String firstName;
      private String lastName;
      &#64;Since(1.0) private String emailAddress;
      &#64;Since(1.0) private String password;
      &#64;Since(1.1) private Address address;
    }
    ```
    
    If you created Gson with `new Gson()`, the `toJson()` and `fromJson()`
    methods will use all the fields for serialization and deserialization. However, if you created
    Gson with `Gson gson = new GsonBuilder().setVersion(1.0).create()` then the
    `toJson()` and `fromJson()` methods of Gson will exclude the `address` field
    since it's version number is set to `1.1`.

    Author(s)
    - Joel Leitch
    """

    def value(self) -> float:
        """
        the value indicating a version number since this member
        or type has been present.
        """
        ...
