"""
Python module generated from Java source file com.google.common.collect.ClassToInstanceMap

Java source file obtained from artifact guava version 32.1.2-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.collect import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from com.google.errorprone.annotations import DoNotMock
from javax.annotation import CheckForNull
from org.checkerframework.checker.nullness.qual import NonNull
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class ClassToInstanceMap(Map):
    """
    A map, each entry of which maps a Java <a href="http://tinyurl.com/2cmwkz">raw type</a> to an
    instance of that type. In addition to implementing `Map`, the additional type-safe
    operations .putInstance and .getInstance are available.
    
    Like any other `Map<Class, Object>`, this map may contain entries for primitive types,
    and a primitive type and its corresponding wrapper type may map to different values.
    
    <h3>Implementations</h3>
    
    
      - ImmutableClassToInstanceMap
      - MutableClassToInstanceMap
    
    
    To map a generic type to an instance of that type, use com.google.common.reflect.TypeToInstanceMap instead.
    
    See the Guava User Guide article on <a href=
    "https://github.com/google/guava/wiki/NewCollectionTypesExplained#classtoinstancemap">`ClassToInstanceMap`</a>.
    
    Type `<B>`: the common supertype that all values will share. When in doubt, just use Object, or use `@Nullable Object` to allow null values.

    Since
    - 2.0
    """

    def getInstance(self, type: type["T"]) -> "T":
        """
        Returns the value the specified class is mapped to, or `null` if no entry for this class
        is present. This will only return a value that was bound to this specific class, not a value
        that may have been bound to a subtype.
        """
        ...


    def putInstance(self, type: type["T"], value: "T") -> "T":
        """
        Maps the specified class to the specified value. Does *not* associate this value with any
        of the class's supertypes.

        Returns
        - the value previously associated with this class (possibly `null`), or `null` if there was no previous entry.
        """
        ...
