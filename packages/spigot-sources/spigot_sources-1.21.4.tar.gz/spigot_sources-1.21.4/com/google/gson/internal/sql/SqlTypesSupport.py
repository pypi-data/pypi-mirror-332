"""
Python module generated from Java source file com.google.gson.internal.sql.SqlTypesSupport

Java source file obtained from artifact gson version 2.11.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.gson import TypeAdapterFactory
from com.google.gson.internal.bind.DefaultDateTypeAdapter import DateType
from com.google.gson.internal.sql import *
from java.util import Date
from typing import Any, Callable, Iterable, Tuple


class SqlTypesSupport:
    """
    Encapsulates access to `java.sql` types, to allow Gson to work without the `java.sql`
    module being present. No ClassNotFoundExceptions will be thrown in case the `java.sql` module is not present.
    
    If .SUPPORTS_SQL_TYPES is `True`, all other constants of this class will be
    non-`null`. However, if it is `False` all other constants will be `null` and
    there will be no support for `java.sql` types.
    """

    SUPPORTS_SQL_TYPES = None
    """
    `True` if `java.sql` types are supported, `False` otherwise
    """
    DATE_DATE_TYPE = None
    TIMESTAMP_DATE_TYPE = None
    DATE_FACTORY = None
    TIME_FACTORY = None
    TIMESTAMP_FACTORY = None
