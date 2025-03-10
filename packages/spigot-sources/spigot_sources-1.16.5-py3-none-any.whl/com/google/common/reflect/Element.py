"""
Python module generated from Java source file com.google.common.reflect.Element

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.reflect import *
from java.lang.reflect import AccessibleObject
from java.lang.reflect import Constructor
from java.lang.reflect import Field
from java.lang.reflect import Member
from java.lang.reflect import Method
from java.lang.reflect import Modifier
from javax.annotation import Nullable
from typing import Any, Callable, Iterable, Tuple


class Element(AccessibleObject, Member):
    """
    Represents either a Field, a Method or a Constructor. Provides
    convenience methods such as .isPublic and .isPackagePrivate.

    Author(s)
    - Ben Yu
    """

    def getOwnerType(self) -> "TypeToken"[Any]:
        ...


    def isAnnotationPresent(self, annotationClass: type["Annotation"]) -> bool:
        ...


    def getAnnotation(self, annotationClass: type["A"]) -> "A":
        ...


    def getAnnotations(self) -> list["Annotation"]:
        ...


    def getDeclaredAnnotations(self) -> list["Annotation"]:
        ...


    def setAccessible(self, flag: bool) -> None:
        ...


    def isAccessible(self) -> bool:
        ...


    def getDeclaringClass(self) -> type[Any]:
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
