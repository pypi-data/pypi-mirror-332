"""
Python module generated from Java source file com.google.gson.FieldNamingPolicy

Java source file obtained from artifact gson version 2.8.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.gson import *
from enum import Enum
from java.lang.reflect import Field
from java.util import Locale
from typing import Any, Callable, Iterable, Tuple


class FieldNamingPolicy(Enum):
    """
    An enumeration that defines a few standard naming conventions for JSON field names.
    This enumeration should be used in conjunction with com.google.gson.GsonBuilder
    to configure a com.google.gson.Gson instance to properly translate Java field
    names into the desired JSON field names.

    Author(s)
    - Joel Leitch
    """

    IDENTITY = 0
    """
    Using this naming policy with Gson will ensure that the field name is
    unchanged.
    """
    UPPER_CAMEL_CASE = 1
    """
    Using this naming policy with Gson will ensure that the first "letter" of the Java
    field name is capitalized when serialized to its JSON form.
    
    Here's a few examples of the form "Java Field Name" ---> "JSON Field Name":
    
      - someFieldName ---> SomeFieldName
      - _someFieldName ---> _SomeFieldName
    """
    UPPER_CAMEL_CASE_WITH_SPACES = 2
    """
    Using this naming policy with Gson will ensure that the first "letter" of the Java
    field name is capitalized when serialized to its JSON form and the words will be
    separated by a space.
    
    Here's a few examples of the form "Java Field Name" ---> "JSON Field Name":
    
      - someFieldName ---> Some Field Name
      - _someFieldName ---> _Some Field Name

    Since
    - 1.4
    """
    LOWER_CASE_WITH_UNDERSCORES = 3
    """
    Using this naming policy with Gson will modify the Java Field name from its camel cased
    form to a lower case field name where each word is separated by an underscore (_).
    
    Here's a few examples of the form "Java Field Name" ---> "JSON Field Name":
    
      - someFieldName ---> some_field_name
      - _someFieldName ---> _some_field_name
      - aStringField ---> a_string_field
      - aURL ---> a_u_r_l
    """
    LOWER_CASE_WITH_DASHES = 4
    """
    Using this naming policy with Gson will modify the Java Field name from its camel cased
    form to a lower case field name where each word is separated by a dash (-).
    
    Here's a few examples of the form "Java Field Name" ---> "JSON Field Name":
    
      - someFieldName ---> some-field-name
      - _someFieldName ---> _some-field-name
      - aStringField ---> a-string-field
      - aURL ---> a-u-r-l
    
    Using dashes in JavaScript is not recommended since dash is also used for a minus sign in
    expressions. This requires that a field named with dashes is always accessed as a quoted
    property like `myobject['my-field']`. Accessing it as an object field
    `myobject.my-field` will result in an unintended javascript expression.

    Since
    - 1.4
    """
