"""
Python module generated from Java source file com.google.gson.annotations.SerializedName

Java source file obtained from artifact gson version 2.10

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.gson.annotations import *
from typing import Any, Callable, Iterable, Tuple


class SerializedName:
    """
    An annotation that indicates this member should be serialized to JSON with
    the provided name value as its field name.
    
    This annotation will override any com.google.gson.FieldNamingPolicy, including
    the default field naming policy, that may have been set on the com.google.gson.Gson
    instance. A different naming policy can set using the `GsonBuilder` class. See
    com.google.gson.GsonBuilder.setFieldNamingPolicy(com.google.gson.FieldNamingPolicy)
    for more information.
    
    Here is an example of how this annotation is meant to be used:
    ```
    public class MyClass {
      &#64;SerializedName("name") String a;
      &#64;SerializedName(value="name1", alternate={"name2", "name3"}) String b;
      String c;
    
      public MyClass(String a, String b, String c) {
        this.a = a;
        this.b = b;
        this.c = c;
      }
    }
    ```
    
    The following shows the output that is generated when serializing an instance of the
    above example class:
    ```
    MyClass target = new MyClass("v1", "v2", "v3");
    Gson gson = new Gson();
    String json = gson.toJson(target);
    System.out.println(json);
    
    ===== OUTPUT =====
    {"name":"v1","name1":"v2","c":"v3"}
    ```
    
    NOTE: The value you specify in this annotation must be a valid JSON field name.
    While deserializing, all values specified in the annotation will be deserialized into the field.
    For example:
    ```
      MyClass target = gson.fromJson("{'name1':'v1'}", MyClass.class);
      assertEquals("v1", target.b);
      target = gson.fromJson("{'name2':'v2'}", MyClass.class);
      assertEquals("v2", target.b);
      target = gson.fromJson("{'name3':'v3'}", MyClass.class);
      assertEquals("v3", target.b);
    ```
    Note that MyClass.b is now deserialized from either name1, name2 or name3.

    Author(s)
    - Joel Leitch

    See
    - com.google.gson.FieldNamingPolicy
    """

    def value(self) -> str:
        """
        Returns
        - the desired name of the field when it is serialized or deserialized
        """
        ...


    def alternate(self) -> list[str]:
        """
        Returns
        - the alternative names of the field when it is deserialized
        """
        return {}
