"""
Python module generated from Java source file com.google.common.reflect.TypeParameter

Java source file obtained from artifact guava version 31.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.reflect import *
from java.lang.reflect import Type
from java.lang.reflect import TypeVariable
from javax.annotation import CheckForNull
from typing import Any, Callable, Iterable, Tuple


class TypeParameter(TypeCapture):
    """
    Captures a free type variable that can be used in TypeToken.where. For example:
    
    ````static <T> TypeToken<List<T>> listOf(Class<T> elementType) {
      return new TypeToken<List<T>>() {`
          .where(new TypeParameter<T>() {}, elementType);
    }
    }```

    Author(s)
    - Ben Yu

    Since
    - 12.0
    """

    def hashCode(self) -> int:
        ...


    def equals(self, o: "Object") -> bool:
        ...


    def toString(self) -> str:
        ...
