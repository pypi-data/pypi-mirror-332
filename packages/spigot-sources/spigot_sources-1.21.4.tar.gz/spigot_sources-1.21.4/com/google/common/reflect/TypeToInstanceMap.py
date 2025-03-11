"""
Python module generated from Java source file com.google.common.reflect.TypeToInstanceMap

Java source file obtained from artifact guava version 33.3.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.reflect import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from com.google.errorprone.annotations import DoNotMock
from javax.annotation import CheckForNull
from org.checkerframework.checker.nullness.qual import NonNull
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class TypeToInstanceMap(Map):
    """
    A map, each entry of which maps a TypeToken to an instance of that type. In addition to
    implementing `Map`, the additional type-safe operations .putInstance and .getInstance are available.
    
    Generally, implementations don't support .put and .putAll because there is no
    way to check an object at runtime to be an instance of a TypeToken. Instead, caller
    should use the type safe .putInstance.
    
    Also, if caller suppresses unchecked warnings and passes in an `Iterable<String>` for
    type `Iterable<Integer>`, the map won't be able to detect and throw type error.
    
    Like any other `Map<Class, Object>`, this map may contain entries for primitive types,
    and a primitive type and its corresponding wrapper type may map to different values.
    
    Type `<B>`: the common supertype that all entries must share; often this is simply Object

    Author(s)
    - Ben Yu

    Since
    - 13.0
    """

    def getInstance(self, type: type["T"]) -> "T":
        """
        Returns the value the specified class is mapped to, or `null` if no entry for this class
        is present. This will only return a value that was bound to this specific class, not a value
        that may have been bound to a subtype.
        
        `getInstance(Foo.class)` is equivalent to `getInstance(TypeToken.of(Foo.class))`.
        """
        ...


    def getInstance(self, type: "TypeToken"["T"]) -> "T":
        """
        Returns the value the specified type is mapped to, or `null` if no entry for this type is
        present. This will only return a value that was bound to this specific type, not a value that
        may have been bound to a subtype.
        """
        ...


    def putInstance(self, type: type["T"], value: "T") -> "T":
        """
        Maps the specified class to the specified value. Does *not* associate this value with any
        of the class's supertypes.
        
        `putInstance(Foo.class, foo)` is equivalent to `putInstance(TypeToken.of(Foo.class), foo)`.

        Returns
        - the value previously associated with this class (possibly `null`), or `null` if there was no previous entry.
        """
        ...


    def putInstance(self, type: "TypeToken"["T"], value: "T") -> "T":
        """
        Maps the specified type to the specified value. Does *not* associate this value with any
        of the type's supertypes.

        Returns
        - the value previously associated with this type (possibly `null`), or `null`
            if there was no previous entry.
        """
        ...
