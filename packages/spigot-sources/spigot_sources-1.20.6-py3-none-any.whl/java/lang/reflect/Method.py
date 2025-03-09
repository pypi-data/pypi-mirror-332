"""
Python module generated from Java source file java.lang.reflect.Method

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.lang.reflect import *
from java.util import StringJoiner
from jdk.internal.access import SharedSecrets
from jdk.internal.reflect import CallerSensitive
from jdk.internal.reflect import MethodAccessor
from jdk.internal.reflect import Reflection
from jdk.internal.vm.annotation import ForceInline
from jdk.internal.vm.annotation import IntrinsicCandidate
from jdk.internal.vm.annotation import Stable
from sun.reflect.annotation import AnnotationParser
from sun.reflect.annotation import AnnotationType
from sun.reflect.annotation import ExceptionProxy
from sun.reflect.annotation import TypeNotPresentExceptionProxy
from sun.reflect.generics.factory import CoreReflectionFactory
from sun.reflect.generics.factory import GenericsFactory
from sun.reflect.generics.repository import MethodRepository
from sun.reflect.generics.scope import MethodScope
from typing import Any, Callable, Iterable, Tuple


class Method(Executable):
    """
    A `Method` provides information about, and access to, a single method
    on a class or interface.  The reflected method may be a class method
    or an instance method (including an abstract method).
    
    A `Method` permits widening conversions to occur when matching the
    actual parameters to invoke with the underlying method's formal
    parameters, but it throws an `IllegalArgumentException` if a
    narrowing conversion would occur.

    Author(s)
    - Nakul Saraiya

    See
    - java.lang.Class.getDeclaredMethod(String, Class[])

    Since
    - 1.1
    """

    def setAccessible(self, flag: bool) -> None:
        """
        Raises
        - InaccessibleObjectException: 
        - SecurityException: 
        """
        ...


    def getDeclaringClass(self) -> type[Any]:
        """
        Returns the `Class` object representing the class or interface
        that declares the method represented by this object.
        """
        ...


    def getName(self) -> str:
        """
        Returns the name of the method represented by this `Method`
        object, as a `String`.
        """
        ...


    def getModifiers(self) -> int:
        """
        Unknown Tags
        - 8.4.3 Method Modifiers
        """
        ...


    def getTypeParameters(self) -> list["TypeVariable"["Method"]]:
        """
        Raises
        - GenericSignatureFormatError: 

        Since
        - 1.5

        Unknown Tags
        - 8.4.4 Generic Methods
        """
        ...


    def getReturnType(self) -> type[Any]:
        """
        Returns a `Class` object that represents the formal return type
        of the method represented by this `Method` object.

        Returns
        - the return type for the method this object represents
        """
        ...


    def getGenericReturnType(self) -> "Type":
        """
        Returns a `Type` object that represents the formal return
        type of the method represented by this `Method` object.
        
        If the return type is a parameterized type,
        the `Type` object returned must accurately reflect
        the actual type arguments used in the source code.
        
        If the return type is a type variable or a parameterized type, it
        is created. Otherwise, it is resolved.

        Returns
        - a `Type` object that represents the formal return
            type of the underlying  method

        Raises
        - GenericSignatureFormatError: if the generic method signature does not conform to the format
            specified in
            <cite>The Java Virtual Machine Specification</cite>
        - TypeNotPresentException: if the underlying method's
            return type refers to a non-existent class or interface declaration
        - MalformedParameterizedTypeException: if the
            underlying method's return type refers to a parameterized
            type that cannot be instantiated for any reason

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
        Compares this `Method` against the specified object.  Returns
        True if the objects are the same.  Two `Methods` are the same if
        they were declared by the same class and have the same name
        and formal parameter types and return type.
        """
        ...


    def hashCode(self) -> int:
        """
        Returns a hashcode for this `Method`.  The hashcode is computed
        as the exclusive-or of the hashcodes for the underlying
        method's declaring class name and the method's name.
        """
        ...


    def toString(self) -> str:
        """
        Returns a string describing this `Method`.  The string is
        formatted as the method access modifiers, if any, followed by
        the method return type, followed by a space, followed by the
        class declaring the method, followed by a period, followed by
        the method name, followed by a parenthesized, comma-separated
        list of the method's formal parameter types. If the method
        throws checked exceptions, the parameter list is followed by a
        space, followed by the word "`throws`" followed by a
        comma-separated list of the thrown exception types.
        For example:
        ```
           public boolean java.lang.Object.equals(java.lang.Object)
        ```
        
        The access modifiers are placed in canonical order as
        specified by "The Java Language Specification".  This is
        `public`, `protected` or `private` first,
        and then other modifiers in the following order:
        `abstract`, `default`, `static`, `final`,
        `synchronized`, `native`, `strictfp`.

        Returns
        - a string describing this `Method`

        Unknown Tags
        - 8.4.3 Method Modifiers
        - 9.4 Method Declarations
        - 9.6.1 Annotation Interface Elements
        """
        ...


    def toGenericString(self) -> str:
        """
        Returns a string describing this `Method`, including type
        parameters.  The string is formatted as the method access
        modifiers, if any, followed by an angle-bracketed
        comma-separated list of the method's type parameters, if any,
        including informative bounds of the type parameters, if any,
        followed by the method's generic return type, followed by a
        space, followed by the class declaring the method, followed by
        a period, followed by the method name, followed by a
        parenthesized, comma-separated list of the method's generic
        formal parameter types.
        
        If this method was declared to take a variable number of
        arguments, instead of denoting the last parameter as
        "`*Type*[]`", it is denoted as
        "`*Type*...`".
        
        A space is used to separate access modifiers from one another
        and from the type parameters or return type.  If there are no
        type parameters, the type parameter list is elided; if the type
        parameter list is present, a space separates the list from the
        class name.  If the method is declared to throw exceptions, the
        parameter list is followed by a space, followed by the word
        "`throws`" followed by a comma-separated list of the generic
        thrown exception types.
        
        The access modifiers are placed in canonical order as
        specified by "The Java Language Specification".  This is
        `public`, `protected` or `private` first,
        and then other modifiers in the following order:
        `abstract`, `default`, `static`, `final`,
        `synchronized`, `native`, `strictfp`.

        Returns
        - a string describing this `Method`,
        include type parameters

        Since
        - 1.5

        Unknown Tags
        - 8.4.3 Method Modifiers
        - 9.4 Method Declarations
        - 9.6.1 Annotation Interface Elements
        """
        ...


    def invoke(self, obj: "Object", *args: Tuple["Object", ...]) -> "Object":
        """
        Invokes the underlying method represented by this `Method`
        object, on the specified object with the specified parameters.
        Individual parameters are automatically unwrapped to match
        primitive formal parameters, and both primitive and reference
        parameters are subject to method invocation conversions as
        necessary.
        
        If the underlying method is static, then the specified `obj`
        argument is ignored. It may be null.
        
        If the number of formal parameters required by the underlying method is
        0, the supplied `args` array may be of length 0 or null.
        
        If the underlying method is an instance method, it is invoked
        using dynamic method lookup as documented in The Java Language
        Specification, section 15.12.4.4; in particular,
        overriding based on the runtime type of the target object may occur.
        
        If the underlying method is static, the class that declared
        the method is initialized if it has not already been initialized.
        
        If the method completes normally, the value it returns is
        returned to the caller of invoke; if the value has a primitive
        type, it is first appropriately wrapped in an object. However,
        if the value has the type of an array of a primitive type, the
        elements of the array are *not* wrapped in objects; in
        other words, an array of primitive type is returned.  If the
        underlying method return type is void, the invocation returns
        null.

        Arguments
        - obj: the object the underlying method is invoked from
        - args: the arguments used for the method call

        Returns
        - the result of dispatching the method represented by
        this object on `obj` with parameters
        `args`

        Raises
        - IllegalAccessException: if this `Method` object
                     is enforcing Java language access control and the underlying
                     method is inaccessible.
        - IllegalArgumentException: if the method is an
                     instance method and the specified object argument
                     is not an instance of the class or interface
                     declaring the underlying method (or of a subclass
                     or implementor thereof); if the number of actual
                     and formal parameters differ; if an unwrapping
                     conversion for primitive arguments fails; or if,
                     after possible unwrapping, a parameter value
                     cannot be converted to the corresponding formal
                     parameter type by a method invocation conversion.
        - InvocationTargetException: if the underlying method
                     throws an exception.
        - NullPointerException: if the specified object is null
                     and the method is an instance method.
        - ExceptionInInitializerError: if the initialization
        provoked by this method fails.
        """
        ...


    def isBridge(self) -> bool:
        """
        {@code True if this method is a bridge
        method; returns `False` otherwise}

        See
        - <a
        href="/java.base/java/lang/reflect/package-summary.html.LanguageJvmModel">Java
        programming language and JVM modeling in core reflection</a>

        Since
        - 1.5

        Unknown Tags
        - A bridge method is a isSynthetic synthetic method
        created by a Java compiler alongside a method originating from
        the source code. Bridge methods are used by Java compilers in
        various circumstances to span differences in Java programming
        language semantics and JVM semantics.
        
        One example use of bridge methods is as a technique for a
        Java compiler to support *covariant overrides*, where a
        subclass overrides a method and gives the new method a more
        specific return type than the method in the superclass.  While
        the Java language specification forbids a class declaring two
        methods with the same parameter types but a different return
        type, the virtual machine does not. A common case where
        covariant overrides are used is for a java.lang.Cloneable Cloneable class where the Object.clone() clone method inherited from `java.lang.Object` is overridden and declared to return the type
        of the class. For example, `Object` declares
        ````protected Object clone() throws CloneNotSupportedException {...`}```
        and `EnumSet<E>` declares its language-level java.util.EnumSet.clone() covariant override
        ````public EnumSet<E> clone() {...`}```
        If this technique was being used, the resulting class file for
        `EnumSet` would have two `clone` methods, one
        returning `EnumSet<E>` and the second a bridge method
        returning `Object`. The bridge method is a JVM-level
        override of `Object.clone()`.  The body of the `clone` bridge method calls its non-bridge counterpart and
        returns its result.
        - 8.4.8.3 Requirements in Overriding and Hiding
        - 15.12.4.5 Create Frame, Synchronize, Transfer Control
        - 4.6 Methods
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


    def isDefault(self) -> bool:
        """
        Returns `True` if this method is a default
        method; returns `False` otherwise.
        
        A default method is a public non-abstract instance method, that
        is, a non-static method with a body, declared in an interface.

        Returns
        - True if and only if this method is a default
        method as defined by the Java Language Specification.

        Since
        - 1.8

        Unknown Tags
        - 9.4 Method Declarations
        """
        ...


    def getDefaultValue(self) -> "Object":
        """
        Returns the default value for the annotation member represented by
        this `Method` instance.  If the member is of a primitive type,
        an instance of the corresponding wrapper type is returned. Returns
        null if no default is associated with the member, or if the method
        instance does not represent a declared member of an annotation type.

        Returns
        - the default value for the annotation member represented
            by this `Method` instance.

        Raises
        - TypeNotPresentException: if the annotation is of type
            Class and no definition can be found for the
            default class value.

        Since
        - 1.5

        Unknown Tags
        - 9.6.2 Defaults for Annotation Type Elements
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
