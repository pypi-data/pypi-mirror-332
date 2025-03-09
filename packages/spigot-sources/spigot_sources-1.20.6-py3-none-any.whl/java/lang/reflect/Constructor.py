"""
Python module generated from Java source file java.lang.reflect.Constructor

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.lang.reflect import *
from java.util import StringJoiner
from jdk.internal.access import SharedSecrets
from jdk.internal.reflect import CallerSensitive
from jdk.internal.reflect import ConstructorAccessor
from jdk.internal.reflect import Reflection
from jdk.internal.vm.annotation import ForceInline
from sun.reflect.annotation import TypeAnnotation
from sun.reflect.annotation import TypeAnnotationParser
from sun.reflect.generics.factory import CoreReflectionFactory
from sun.reflect.generics.factory import GenericsFactory
from sun.reflect.generics.repository import ConstructorRepository
from sun.reflect.generics.scope import ConstructorScope
from typing import Any, Callable, Iterable, Tuple


class Constructor(Executable):
    """
    `Constructor` provides information about, and access to, a single
    constructor for a class.
    
    `Constructor` permits widening conversions to occur when matching the
    actual parameters to newInstance() with the underlying
    constructor's formal parameters, but throws an
    `IllegalArgumentException` if a narrowing conversion would occur.
    
    Type `<T>`: the class in which the constructor is declared

    Author(s)
    - Nakul Saraiya

    See
    - java.lang.Class.getDeclaredConstructors()

    Since
    - 1.1
    """

    def setAccessible(self, flag: bool) -> None:
        """
        
        
         A `SecurityException` is also thrown if this object is a
        `Constructor` object for the class `Class` and `flag`
        is True. 

        Arguments
        - flag: 

        Raises
        - InaccessibleObjectException: 
        - SecurityException: if the request is denied by the security manager
                or this is a constructor for `java.lang.Class`
        """
        ...


    def getDeclaringClass(self) -> type["T"]:
        """
        Returns the `Class` object representing the class that
        declares the constructor represented by this object.
        """
        ...


    def getName(self) -> str:
        """
        Returns the name of this constructor, as a string.  This is
        the binary name of the constructor's declaring class.
        """
        ...


    def getModifiers(self) -> int:
        """
        Unknown Tags
        - 8.8.3 Constructor Modifiers
        """
        ...


    def getTypeParameters(self) -> list["TypeVariable"["Constructor"["T"]]]:
        """
        Raises
        - GenericSignatureFormatError: 

        Since
        - 1.5
        """
        ...


    def getParameterTypes(self) -> list[type[Any]]:
        """

        """
        ...


    def getParameterCount(self) -> int:
        """
        Since
        - 1.8
        """
        ...


    def getGenericParameterTypes(self) -> list["Type"]:
        """
        Raises
        - GenericSignatureFormatError: 
        - TypeNotPresentException: 
        - MalformedParameterizedTypeException: 

        Since
        - 1.5
        """
        ...


    def getExceptionTypes(self) -> list[type[Any]]:
        """

        """
        ...


    def getGenericExceptionTypes(self) -> list["Type"]:
        """
        Raises
        - GenericSignatureFormatError: 
        - TypeNotPresentException: 
        - MalformedParameterizedTypeException: 

        Since
        - 1.5
        """
        ...


    def equals(self, obj: "Object") -> bool:
        """
        Compares this `Constructor` against the specified object.
        Returns True if the objects are the same.  Two `Constructor` objects are
        the same if they were declared by the same class and have the
        same formal parameter types.
        """
        ...


    def hashCode(self) -> int:
        """
        Returns a hashcode for this `Constructor`. The hashcode is
        the same as the hashcode for the underlying constructor's
        declaring class name.
        """
        ...


    def toString(self) -> str:
        """
        Returns a string describing this `Constructor`.  The string is
        formatted as the constructor access modifiers, if any,
        followed by the fully-qualified name of the declaring class,
        followed by a parenthesized, comma-separated list of the
        constructor's formal parameter types.  For example:
        ````public java.util.HashMap(int,float)````
        
        If the constructor is declared to throw exceptions, the
        parameter list is followed by a space, followed by the word
        "`throws`" followed by a comma-separated list of the
        thrown exception types.
        
        The only possible modifiers for constructors are the access
        modifiers `public`, `protected` or
        `private`.  Only one of these may appear, or none if the
        constructor has default (package) access.

        Returns
        - a string describing this `Constructor`

        Unknown Tags
        - 8.8.3 Constructor Modifiers
        - 8.9.2 Enum Body Declarations
        """
        ...


    def toGenericString(self) -> str:
        """
        Returns a string describing this `Constructor`,
        including type parameters.  The string is formatted as the
        constructor access modifiers, if any, followed by an
        angle-bracketed comma separated list of the constructor's type
        parameters, if any, including  informative bounds of the
        type parameters, if any, followed by the fully-qualified name of the
        declaring class, followed by a parenthesized, comma-separated
        list of the constructor's generic formal parameter types.
        
        If this constructor was declared to take a variable number of
        arguments, instead of denoting the last parameter as
        "`*Type*[]`", it is denoted as
        "`*Type*...`".
        
        A space is used to separate access modifiers from one another
        and from the type parameters or class name.  If there are no
        type parameters, the type parameter list is elided; if the type
        parameter list is present, a space separates the list from the
        class name.  If the constructor is declared to throw
        exceptions, the parameter list is followed by a space, followed
        by the word "`throws`" followed by a
        comma-separated list of the generic thrown exception types.
        
        The only possible modifiers for constructors are the access
        modifiers `public`, `protected` or
        `private`.  Only one of these may appear, or none if the
        constructor has default (package) access.

        Returns
        - a string describing this `Constructor`,
        include type parameters

        Since
        - 1.5

        Unknown Tags
        - 8.8.3 Constructor Modifiers
        - 8.9.2 Enum Body Declarations
        """
        ...


    def newInstance(self, *initargs: Tuple["Object", ...]) -> "T":
        """
        Uses the constructor represented by this `Constructor` object to
        create and initialize a new instance of the constructor's
        declaring class, with the specified initialization parameters.
        Individual parameters are automatically unwrapped to match
        primitive formal parameters, and both primitive and reference
        parameters are subject to method invocation conversions as necessary.
        
        If the number of formal parameters required by the underlying constructor
        is 0, the supplied `initargs` array may be of length 0 or null.
        
        If the constructor's declaring class is an inner class in a
        non-static context, the first argument to the constructor needs
        to be the enclosing instance; see section 15.9.3 of
        <cite>The Java Language Specification</cite>.
        
        If the required access and argument checks succeed and the
        instantiation will proceed, the constructor's declaring class
        is initialized if it has not already been initialized.
        
        If the constructor completes normally, returns the newly
        created and initialized instance.

        Arguments
        - initargs: array of objects to be passed as arguments to
        the constructor call; values of primitive types are wrapped in
        a wrapper object of the appropriate type (e.g. a `float`
        in a java.lang.Float Float)

        Returns
        - a new object created by calling the constructor
        this object represents

        Raises
        - IllegalAccessException: if this `Constructor` object
                     is enforcing Java language access control and the underlying
                     constructor is inaccessible.
        - IllegalArgumentException: if the number of actual
                     and formal parameters differ; if an unwrapping
                     conversion for primitive arguments fails; or if,
                     after possible unwrapping, a parameter value
                     cannot be converted to the corresponding formal
                     parameter type by a method invocation conversion; if
                     this constructor pertains to an enum class.
        - InstantiationException: if the class that declares the
                     underlying constructor represents an abstract class.
        - InvocationTargetException: if the underlying constructor
                     throws an exception.
        - ExceptionInInitializerError: if the initialization provoked
                     by this method fails.
        """
        ...


    def isVarArgs(self) -> bool:
        """
        Since
        - 1.5

        Unknown Tags
        - 8.4.1 Formal Parameters
        """
        ...


    def isSynthetic(self) -> bool:
        """
        See
        - <a
        href="/java.base/java/lang/reflect/package-summary.html.LanguageJvmModel">Java
        programming language and JVM modeling in core reflection</a>

        Since
        - 1.5

        Unknown Tags
        - 13.1 The Form of a Binary
        - 4.6 Methods
        """
        ...


    def getAnnotation(self, annotationClass: type["T"]) -> "T":
        """
        Raises
        - NullPointerException: 

        Since
        - 1.5
        """
        ...


    def getDeclaredAnnotations(self) -> list["Annotation"]:
        """
        Since
        - 1.5
        """
        ...


    def getParameterAnnotations(self) -> list[list["Annotation"]]:
        """
        Since
        - 1.5
        """
        ...


    def getAnnotatedReturnType(self) -> "AnnotatedType":
        """
        Since
        - 1.8
        """
        ...


    def getAnnotatedReceiverType(self) -> "AnnotatedType":
        """
        Since
        - 1.8
        """
        ...
