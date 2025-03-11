"""
Python module generated from Java source file com.google.common.reflect.TypeVisitor

Java source file obtained from artifact guava version 33.3.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.collect import Sets
from com.google.common.reflect import *
from java.lang.reflect import GenericArrayType
from java.lang.reflect import ParameterizedType
from java.lang.reflect import Type
from java.lang.reflect import TypeVariable
from java.lang.reflect import WildcardType
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class TypeVisitor:
    """
    Based on what a Type is, dispatch it to the corresponding `visit*` method. By
    default, no recursion is done for type arguments or type bounds. But subclasses can opt to do
    recursion by calling .visit for any `Type` while visitation is in progress. For
    example, this can be used to reject wildcards or type variables contained in a type as in:
    
    ````new TypeVisitor() {
      protected void visitParameterizedType(ParameterizedType t) {
        visit(t.getOwnerType());
        visit(t.getActualTypeArguments());`
      protected void visitGenericArrayType(GenericArrayType t) {
        visit(t.getGenericComponentType());
      }
      protected void visitTypeVariable(TypeVariable<?> t) {
        throw new IllegalArgumentException("Cannot contain type variable.");
      }
      protected void visitWildcardType(WildcardType t) {
        throw new IllegalArgumentException("Cannot contain wildcard type.");
      }
    }.visit(type);
    }```
    
    One `Type` is visited at most once. The second time the same type is visited, it's
    ignored by .visit. This avoids infinite recursion caused by recursive type bounds.
    
    This class is *not* thread safe.

    Author(s)
    - Ben Yu
    """

    def visit(self, *types: Tuple["Type", ...]) -> None:
        """
        Visits the given types. Null types are ignored. This allows subclasses to call `visit(parameterizedType.getOwnerType())` safely without having to check nulls.
        """
        ...
