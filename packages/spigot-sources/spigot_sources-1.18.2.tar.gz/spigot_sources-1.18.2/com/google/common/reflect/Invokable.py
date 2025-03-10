"""
Python module generated from Java source file com.google.common.reflect.Invokable

Java source file obtained from artifact guava version 31.0.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.collect import ImmutableList
from com.google.common.reflect import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from java.lang.reflect import AccessibleObject
from java.lang.reflect import AnnotatedElement
from java.lang.reflect import AnnotatedType
from java.lang.reflect import Constructor
from java.lang.reflect import InvocationTargetException
from java.lang.reflect import Member
from java.lang.reflect import Method
from java.lang.reflect import Modifier
from java.lang.reflect import Type
from java.lang.reflect import TypeVariable
from java.util import Arrays
from javax.annotation import CheckForNull
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class Invokable(AnnotatedElement, Member):
    """
    Wrapper around either a Method or a Constructor. Convenience API is provided to
    make common reflective operation easier to deal with, such as .isPublic, .getParameters etc.
    
    In addition to convenience methods, TypeToken.method and TypeToken.constructor
    will resolve the type parameters of the method or constructor in the context of the owner type,
    which may be a subtype of the declaring class. For example:
    
    ````Method getMethod = List.class.getMethod("get", int.class);
    Invokable<List<String>, ?> invokable = new TypeToken<List<String>>() {`.method(getMethod);
    assertEquals(TypeToken.of(String.class), invokable.getReturnType()); // Not Object.class!
    assertEquals(new TypeToken<List<String>>() {}, invokable.getOwnerType());
    }```
    
    **Note:** earlier versions of this class inherited from java.lang.reflect.AccessibleObject AccessibleObject and java.lang.reflect.GenericDeclaration GenericDeclaration. Since version 31.0 that is no longer
    the case. However, most methods from those types are present with the same signature in this
    class.
    
    Type `<T>`: the type that owns this method or constructor.
    
    Type `<R>`: the return type of (or supertype thereof) the method or the declaring type of the
        constructor.

    Author(s)
    - Ben Yu

    Since
    - 14.0 (no longer implements AccessibleObject or `GenericDeclaration` since
        31.0)
    """

    @staticmethod
    def from(method: "Method") -> "Invokable"[Any, "Object"]:
        """
        Returns Invokable of `method`.
        """
        ...


    @staticmethod
    def from(constructor: "Constructor"["T"]) -> "Invokable"["T", "T"]:
        """
        Returns Invokable of `constructor`.
        """
        ...


    def isAnnotationPresent(self, annotationClass: type["Annotation"]) -> bool:
        ...


    def getAnnotation(self, annotationClass: type["A"]) -> "A":
        ...


    def getAnnotations(self) -> list["Annotation"]:
        ...


    def getDeclaredAnnotations(self) -> list["Annotation"]:
        ...


    def getTypeParameters(self) -> list["TypeVariable"[Any]]:
        """
        See java.lang.reflect.GenericDeclaration.getTypeParameters().
        """
        ...


    def setAccessible(self, flag: bool) -> None:
        """
        See java.lang.reflect.AccessibleObject.setAccessible(boolean).
        """
        ...


    def trySetAccessible(self) -> bool:
        """
        See java.lang.reflect.AccessibleObject.trySetAccessible().
        """
        ...


    def isAccessible(self) -> bool:
        """
        See java.lang.reflect.AccessibleObject.isAccessible().
        """
        ...


    def getName(self) -> str:
        ...


    def getModifiers(self) -> int:
        ...


    def isSynthetic(self) -> bool:
        ...


    def isPublic(self) -> bool:
        """
        Returns True if the element is public.
        """
        ...


    def isProtected(self) -> bool:
        """
        Returns True if the element is protected.
        """
        ...


    def isPackagePrivate(self) -> bool:
        """
        Returns True if the element is package-private.
        """
        ...


    def isPrivate(self) -> bool:
        """
        Returns True if the element is private.
        """
        ...


    def isStatic(self) -> bool:
        """
        Returns True if the element is static.
        """
        ...


    def isFinal(self) -> bool:
        """
        Returns `True` if this method is final, per `Modifier.isFinal(getModifiers())`.
        
        Note that a method may still be effectively "final", or non-overridable when it has no
        `final` keyword. For example, it could be private, or it could be declared by a final
        class. To tell whether a method is overridable, use Invokable.isOverridable.
        """
        ...


    def isAbstract(self) -> bool:
        """
        Returns True if the method is abstract.
        """
        ...


    def isNative(self) -> bool:
        """
        Returns True if the element is native.
        """
        ...


    def isSynchronized(self) -> bool:
        """
        Returns True if the method is synchronized.
        """
        ...


    def equals(self, obj: "Object") -> bool:
        ...


    def hashCode(self) -> int:
        ...


    def toString(self) -> str:
        ...


    def isOverridable(self) -> bool:
        """
        Returns `True` if this is an overridable method. Constructors, private, static or final
        methods, or methods declared by final classes are not overridable.
        """
        ...


    def isVarArgs(self) -> bool:
        """
        Returns `True` if this was declared to take a variable number of arguments.
        """
        ...


    def invoke(self, receiver: "T", *args: Tuple["Object", ...]) -> "R":
        ...


    def getReturnType(self) -> "TypeToken"["R"]:
        ...


    def getParameters(self) -> "ImmutableList"["Parameter"]:
        """
        Returns all declared parameters of this `Invokable`. Note that if this is a constructor
        of a non-static inner class, unlike Constructor.getParameterTypes, the hidden `this` parameter of the enclosing class is excluded from the returned parameters.
        """
        ...


    def getExceptionTypes(self) -> "ImmutableList"["TypeToken"["Throwable"]]:
        """
        Returns all declared exception types of this `Invokable`.
        """
        ...


    def returning(self, returnType: type["R1"]) -> "Invokable"["T", "R1"]:
        """
        Explicitly specifies the return type of this `Invokable`. For example:
        
        ````Method factoryMethod = Person.class.getMethod("create");
        Invokable<?, Person> factory = Invokable.of(getNameMethod).returning(Person.class);````
        """
        ...


    def returning(self, returnType: "TypeToken"["R1"]) -> "Invokable"["T", "R1"]:
        """
        Explicitly specifies the return type of this `Invokable`.
        """
        ...


    def getDeclaringClass(self) -> type["T"]:
        ...


    def getOwnerType(self) -> "TypeToken"["T"]:
        ...


    def getAnnotatedReturnType(self) -> "AnnotatedType":
        ...
