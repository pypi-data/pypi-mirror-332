"""
Python module generated from Java source file com.google.common.reflect.TypeToken

Java source file obtained from artifact guava version 33.3.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import VisibleForTesting
from com.google.common.base import Joiner
from com.google.common.base import Predicate
from com.google.common.collect import FluentIterable
from com.google.common.collect import ForwardingSet
from com.google.common.collect import ImmutableList
from com.google.common.collect import ImmutableMap
from com.google.common.collect import ImmutableSet
from com.google.common.collect import Maps
from com.google.common.collect import Ordering
from com.google.common.primitives import Primitives
from com.google.common.reflect import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from com.google.errorprone.annotations.concurrent import LazyInit
from java.io import Serializable
from java.lang.reflect import Constructor
from java.lang.reflect import GenericArrayType
from java.lang.reflect import Method
from java.lang.reflect import Modifier
from java.lang.reflect import ParameterizedType
from java.lang.reflect import Type
from java.lang.reflect import TypeVariable
from java.lang.reflect import WildcardType
from java.util import Arrays
from java.util import Comparator
from javax.annotation import CheckForNull
from typing import Any, Callable, Iterable, Tuple


class TypeToken(TypeCapture, Serializable):
    """
    A Type with generics.
    
    Operations that are otherwise only available in Class are implemented to support
    `Type`, for example .isSubtypeOf, .isArray and .getComponentType.
    It also provides additional utilities such as .getTypes, .resolveType, etc.
    
    There are three ways to get a `TypeToken` instance:
    
    
      - Wrap a `Type` obtained via reflection. For example: `TypeToken.of(method.getGenericReturnType())`.
      - Capture a generic type with a (usually anonymous) subclass. For example:
          ````new TypeToken<List<String>>() {`
    }```
          Note that it's critical that the actual type argument is carried by a subclass. The
          following code is wrong because it only captures the `<T>` type variable of the
          `listType()` method signature; while `<String>` is lost in erasure:
          ````class Util {
      static <T> TypeToken<List<T>> listType() {
        return new TypeToken<List<T>>() {`;
      }
    }
    
    TypeToken<List<String>> stringListType = Util.<String>listType();
    }```
      - Capture a generic type with a (usually anonymous) subclass and resolve it against a context
          class that knows what the type parameters are. For example:
          ````abstract class IKnowMyType<T> {
      TypeToken<T> type = new TypeToken<T>(getClass()) {`;
    }
    new IKnowMyType<String>() {}.type => String
    }```
    
    
    `TypeToken` is serializable when no type variable is contained in the type.
    
    Note to Guice users: `TypeToken` is similar to Guice's `TypeLiteral` class except
    that it is serializable and offers numerous additional utility methods.

    Author(s)
    - Ben Yu

    Since
    - 12.0
    """

    @staticmethod
    def of(type: type["T"]) -> "TypeToken"["T"]:
        """
        Returns an instance of type token that wraps `type`.
        """
        ...


    @staticmethod
    def of(type: "Type") -> "TypeToken"[Any]:
        """
        Returns an instance of type token that wraps `type`.
        """
        ...


    def getRawType(self) -> type["T"]:
        """
        Returns the raw type of `T`. Formally speaking, if `T` is returned by java.lang.reflect.Method.getGenericReturnType, the raw type is what's returned by java.lang.reflect.Method.getReturnType of the same method object. Specifically:
        
        
          - If `T` is a `Class` itself, `T` itself is returned.
          - If `T` is a ParameterizedType, the raw type of the parameterized type is
              returned.
          - If `T` is a GenericArrayType, the returned type is the corresponding array
              class. For example: `List<Integer>[] => List[]`.
          - If `T` is a type variable or a wildcard type, the raw type of the first upper bound
              is returned. For example: `<X extends Foo> => Foo`.
        """
        ...


    def getType(self) -> "Type":
        """
        Returns the represented type.
        """
        ...


    def where(self, typeParam: "TypeParameter"["X"], typeArg: "TypeToken"["X"]) -> "TypeToken"["T"]:
        ...


    def where(self, typeParam: "TypeParameter"["X"], typeArg: type["X"]) -> "TypeToken"["T"]:
        ...


    def resolveType(self, type: "Type") -> "TypeToken"[Any]:
        """
        Resolves the given `type` against the type context represented by this type. For example:
        
        ````new TypeToken<List<String>>() {`.resolveType(
            List.class.getMethod("get", int.class).getGenericReturnType())
        => String.class
        }```
        """
        ...


    def getTypes(self) -> "TypeSet":
        """
        Returns the set of interfaces and classes that this type is or is a subtype of. The returned
        types are parameterized with proper type arguments.
        
        Subtypes are always listed before supertypes. But the reverse is not True. A type isn't
        necessarily a subtype of all the types following. Order between types without subtype
        relationship is arbitrary and not guaranteed.
        
        If this type is a type variable or wildcard, upper bounds that are themselves type variables
        aren't included (their super interfaces and superclasses are).
        """
        ...


    def getSupertype(self, superclass: type["T"]) -> "TypeToken"["T"]:
        """
        Returns the generic form of `superclass`. For example, if this is `ArrayList<String>`, `Iterable<String>` is returned given the input `Iterable.class`.
        """
        ...


    def getSubtype(self, subclass: type[Any]) -> "TypeToken"["T"]:
        """
        Returns subtype of `this` with `subclass` as the raw class. For example, if this is
        `Iterable<String>` and `subclass` is `List`, `List<String>` is
        returned.
        """
        ...


    def isSupertypeOf(self, type: "TypeToken"[Any]) -> bool:
        """
        Returns True if this type is a supertype of the given `type`. "Supertype" is defined
        according to <a
        href="http://docs.oracle.com/javase/specs/jls/se8/html/jls-4.html#jls-4.5.1">the rules for type
        arguments</a> introduced with Java generics.

        Since
        - 19.0
        """
        ...


    def isSupertypeOf(self, type: "Type") -> bool:
        """
        Returns True if this type is a supertype of the given `type`. "Supertype" is defined
        according to <a
        href="http://docs.oracle.com/javase/specs/jls/se8/html/jls-4.html#jls-4.5.1">the rules for type
        arguments</a> introduced with Java generics.

        Since
        - 19.0
        """
        ...


    def isSubtypeOf(self, type: "TypeToken"[Any]) -> bool:
        """
        Returns True if this type is a subtype of the given `type`. "Subtype" is defined
        according to <a
        href="http://docs.oracle.com/javase/specs/jls/se8/html/jls-4.html#jls-4.5.1">the rules for type
        arguments</a> introduced with Java generics.

        Since
        - 19.0
        """
        ...


    def isSubtypeOf(self, supertype: "Type") -> bool:
        """
        Returns True if this type is a subtype of the given `type`. "Subtype" is defined
        according to <a
        href="http://docs.oracle.com/javase/specs/jls/se8/html/jls-4.html#jls-4.5.1">the rules for type
        arguments</a> introduced with Java generics.

        Since
        - 19.0
        """
        ...


    def isArray(self) -> bool:
        """
        Returns True if this type is known to be an array type, such as `int[]`, `T[]`,
        `<? extends Map<String, Integer>[]>` etc.
        """
        ...


    def isPrimitive(self) -> bool:
        """
        Returns True if this type is one of the nine primitive types (including `void`).

        Since
        - 15.0
        """
        ...


    def wrap(self) -> "TypeToken"["T"]:
        """
        Returns the corresponding wrapper type if this is a primitive type; otherwise returns `this` itself. Idempotent.

        Since
        - 15.0
        """
        ...


    def unwrap(self) -> "TypeToken"["T"]:
        """
        Returns the corresponding primitive type if this is a wrapper type; otherwise returns `this` itself. Idempotent.

        Since
        - 15.0
        """
        ...


    def getComponentType(self) -> "TypeToken"[Any]:
        """
        Returns the array component type if this type represents an array (`int[]`, `T[]`,
        `<? extends Map<String, Integer>[]>` etc.), or else `null` is returned.
        """
        ...


    def method(self, method: "Method") -> "Invokable"["T", "Object"]:
        """
        Returns the Invokable for `method`, which must be a member of `T`.

        Since
        - 14.0
        """
        ...


    def constructor(self, constructor: "Constructor"[Any]) -> "Invokable"["T", "T"]:
        """
        Returns the Invokable for `constructor`, which must be a member of `T`.

        Since
        - 14.0
        """
        ...


    def equals(self, o: "Object") -> bool:
        """
        Returns True if `o` is another `TypeToken` that represents the same Type.
        """
        ...


    def hashCode(self) -> int:
        ...


    def toString(self) -> str:
        ...


    class TypeSet(ForwardingSet, Serializable):
        """
        The set of interfaces and classes that `T` is or is a subtype of. Object is not
        included in the set if this type is an interface.

        Since
        - 13.0
        """

        def interfaces(self) -> "TypeSet":
            """
            Returns the types that are interfaces implemented by this type.
            """
            ...


        def classes(self) -> "TypeSet":
            """
            Returns the types that are classes.
            """
            ...


        def rawTypes(self) -> set[type["T"]]:
            """
            Returns the raw types of the types in this set, in the same order.
            """
            ...
