"""
Python module generated from Java source file java.lang.reflect.Field

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.lang.reflect import *
from java.util import Objects
from jdk.internal.access import SharedSecrets
from jdk.internal.reflect import CallerSensitive
from jdk.internal.reflect import FieldAccessor
from jdk.internal.reflect import Reflection
from jdk.internal.vm.annotation import ForceInline
from sun.reflect.annotation import AnnotationParser
from sun.reflect.annotation import AnnotationSupport
from sun.reflect.annotation import TypeAnnotation
from sun.reflect.annotation import TypeAnnotationParser
from sun.reflect.generics.factory import CoreReflectionFactory
from sun.reflect.generics.factory import GenericsFactory
from sun.reflect.generics.repository import FieldRepository
from sun.reflect.generics.scope import ClassScope
from typing import Any, Callable, Iterable, Tuple


class Field(AccessibleObject, Member):
    """
    A `Field` provides information about, and dynamic access to, a
    single field of a class or an interface.  The reflected field may
    be a class (static) field or an instance field.
    
    A `Field` permits widening conversions to occur during a get or
    set access operation, but throws an `IllegalArgumentException` if a
    narrowing conversion would occur.

    Author(s)
    - Nakul Saraiya

    See
    - java.lang.Class.getDeclaredField(String)

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
        that declares the field represented by this `Field` object.
        """
        ...


    def getName(self) -> str:
        """
        Returns the name of the field represented by this `Field` object.
        """
        ...


    def getModifiers(self) -> int:
        """
        Returns the Java language modifiers for the field represented
        by this `Field` object, as an integer. The `Modifier` class should
        be used to decode the modifiers.

        See
        - Modifier

        Unknown Tags
        - 8.3 Field Declarations
        - 9.3 Field (Constant) Declarations
        """
        ...


    def isEnumConstant(self) -> bool:
        """
        Returns `True` if this field represents an element of
        an enumerated class; returns `False` otherwise.

        Returns
        - `True` if and only if this field represents an element of
        an enumerated class.

        Since
        - 1.5

        Unknown Tags
        - 8.9.1 Enum Constants
        """
        ...


    def isSynthetic(self) -> bool:
        """
        Returns `True` if this field is a synthetic
        field; returns `False` otherwise.

        Returns
        - True if and only if this field is a synthetic
        field as defined by the Java Language Specification.

        See
        - <a
        href="/java.base/java/lang/reflect/package-summary.html.LanguageJvmModel">Java
        programming language and JVM modeling in core reflection</a>

        Since
        - 1.5
        """
        ...


    def getType(self) -> type[Any]:
        """
        Returns a `Class` object that identifies the
        declared type for the field represented by this
        `Field` object.

        Returns
        - a `Class` object identifying the declared
        type of the field represented by this object
        """
        ...


    def getGenericType(self) -> "Type":
        """
        Returns a `Type` object that represents the declared type for
        the field represented by this `Field` object.
        
        If the declared type of the field is a parameterized type,
        the `Type` object returned must accurately reflect the
        actual type arguments used in the source code.
        
        If the type of the underlying field is a type variable or a
        parameterized type, it is created. Otherwise, it is resolved.

        Returns
        - a `Type` object that represents the declared type for
            the field represented by this `Field` object

        Raises
        - GenericSignatureFormatError: if the generic field
            signature does not conform to the format specified in
            <cite>The Java Virtual Machine Specification</cite>
        - TypeNotPresentException: if the generic type
            signature of the underlying field refers to a non-existent
            class or interface declaration
        - MalformedParameterizedTypeException: if the generic
            signature of the underlying field refers to a parameterized type
            that cannot be instantiated for any reason

        Since
        - 1.5
        """
        ...


    def equals(self, obj: "Object") -> bool:
        """
        Compares this `Field` against the specified object.  Returns
        True if the objects are the same.  Two `Field` objects are the same if
        they were declared by the same class and have the same name
        and type.
        """
        ...


    def hashCode(self) -> int:
        """
        Returns a hashcode for this `Field`.  This is computed as the
        exclusive-or of the hashcodes for the underlying field's
        declaring class name and its name.
        """
        ...


    def toString(self) -> str:
        """
        Returns a string describing this `Field`.  The format is
        the access modifiers for the field, if any, followed
        by the field type, followed by a space, followed by
        the fully-qualified name of the class declaring the field,
        followed by a period, followed by the name of the field.
        For example:
        ```
           public static final int java.lang.Thread.MIN_PRIORITY
           private int java.io.FileDescriptor.fd
        ```
        
        The modifiers are placed in canonical order as specified by
        "The Java Language Specification".  This is `public`,
        `protected` or `private` first, and then other
        modifiers in the following order: `static`, `final`,
        `transient`, `volatile`.

        Returns
        - a string describing this `Field`

        Unknown Tags
        - 8.3.1 Field Modifiers
        """
        ...


    def toGenericString(self) -> str:
        """
        Returns a string describing this `Field`, including
        its generic type.  The format is the access modifiers for the
        field, if any, followed by the generic field type, followed by
        a space, followed by the fully-qualified name of the class
        declaring the field, followed by a period, followed by the name
        of the field.
        
        The modifiers are placed in canonical order as specified by
        "The Java Language Specification".  This is `public`,
        `protected` or `private` first, and then other
        modifiers in the following order: `static`, `final`,
        `transient`, `volatile`.

        Returns
        - a string describing this `Field`, including
        its generic type

        Since
        - 1.5

        Unknown Tags
        - 8.3.1 Field Modifiers
        """
        ...


    def get(self, obj: "Object") -> "Object":
        """
        Returns the value of the field represented by this `Field`, on
        the specified object. The value is automatically wrapped in an
        object if it has a primitive type.
        
        The underlying field's value is obtained as follows:
        
        If the underlying field is a static field, the `obj` argument
        is ignored; it may be null.
        
        Otherwise, the underlying field is an instance field.  If the
        specified `obj` argument is null, the method throws a
        `NullPointerException`. If the specified object is not an
        instance of the class or interface declaring the underlying
        field, the method throws an `IllegalArgumentException`.
        
        If this `Field` object is enforcing Java language access control, and
        the underlying field is inaccessible, the method throws an
        `IllegalAccessException`.
        If the underlying field is static, the class that declared the
        field is initialized if it has not already been initialized.
        
        Otherwise, the value is retrieved from the underlying instance
        or static field.  If the field has a primitive type, the value
        is wrapped in an object before being returned, otherwise it is
        returned as is.
        
        If the field is hidden in the type of `obj`,
        the field's value is obtained according to the preceding rules.

        Arguments
        - obj: object from which the represented field's value is
        to be extracted

        Returns
        - the value of the represented field in object
        `obj`; primitive values are wrapped in an appropriate
        object before being returned

        Raises
        - IllegalAccessException: if this `Field` object
                     is enforcing Java language access control and the underlying
                     field is inaccessible.
        - IllegalArgumentException: if the specified object is not an
                     instance of the class or interface declaring the underlying
                     field (or a subclass or implementor thereof).
        - NullPointerException: if the specified object is null
                     and the field is an instance field.
        - ExceptionInInitializerError: if the initialization provoked
                     by this method fails.
        """
        ...


    def getBoolean(self, obj: "Object") -> bool:
        """
        Gets the value of a static or instance `boolean` field.

        Arguments
        - obj: the object to extract the `boolean` value
        from

        Returns
        - the value of the `boolean` field

        Raises
        - IllegalAccessException: if this `Field` object
                     is enforcing Java language access control and the underlying
                     field is inaccessible.
        - IllegalArgumentException: if the specified object is not
                     an instance of the class or interface declaring the
                     underlying field (or a subclass or implementor
                     thereof), or if the field value cannot be
                     converted to the type `boolean` by a
                     widening conversion.
        - NullPointerException: if the specified object is null
                     and the field is an instance field.
        - ExceptionInInitializerError: if the initialization provoked
                     by this method fails.

        See
        - Field.get
        """
        ...


    def getByte(self, obj: "Object") -> int:
        """
        Gets the value of a static or instance `byte` field.

        Arguments
        - obj: the object to extract the `byte` value
        from

        Returns
        - the value of the `byte` field

        Raises
        - IllegalAccessException: if this `Field` object
                     is enforcing Java language access control and the underlying
                     field is inaccessible.
        - IllegalArgumentException: if the specified object is not
                     an instance of the class or interface declaring the
                     underlying field (or a subclass or implementor
                     thereof), or if the field value cannot be
                     converted to the type `byte` by a
                     widening conversion.
        - NullPointerException: if the specified object is null
                     and the field is an instance field.
        - ExceptionInInitializerError: if the initialization provoked
                     by this method fails.

        See
        - Field.get
        """
        ...


    def getChar(self, obj: "Object") -> str:
        """
        Gets the value of a static or instance field of type
        `char` or of another primitive type convertible to
        type `char` via a widening conversion.

        Arguments
        - obj: the object to extract the `char` value
        from

        Returns
        - the value of the field converted to type `char`

        Raises
        - IllegalAccessException: if this `Field` object
                     is enforcing Java language access control and the underlying
                     field is inaccessible.
        - IllegalArgumentException: if the specified object is not
                     an instance of the class or interface declaring the
                     underlying field (or a subclass or implementor
                     thereof), or if the field value cannot be
                     converted to the type `char` by a
                     widening conversion.
        - NullPointerException: if the specified object is null
                     and the field is an instance field.
        - ExceptionInInitializerError: if the initialization provoked
                     by this method fails.

        See
        - Field.get
        """
        ...


    def getShort(self, obj: "Object") -> int:
        """
        Gets the value of a static or instance field of type
        `short` or of another primitive type convertible to
        type `short` via a widening conversion.

        Arguments
        - obj: the object to extract the `short` value
        from

        Returns
        - the value of the field converted to type `short`

        Raises
        - IllegalAccessException: if this `Field` object
                     is enforcing Java language access control and the underlying
                     field is inaccessible.
        - IllegalArgumentException: if the specified object is not
                     an instance of the class or interface declaring the
                     underlying field (or a subclass or implementor
                     thereof), or if the field value cannot be
                     converted to the type `short` by a
                     widening conversion.
        - NullPointerException: if the specified object is null
                     and the field is an instance field.
        - ExceptionInInitializerError: if the initialization provoked
                     by this method fails.

        See
        - Field.get
        """
        ...


    def getInt(self, obj: "Object") -> int:
        """
        Gets the value of a static or instance field of type
        `int` or of another primitive type convertible to
        type `int` via a widening conversion.

        Arguments
        - obj: the object to extract the `int` value
        from

        Returns
        - the value of the field converted to type `int`

        Raises
        - IllegalAccessException: if this `Field` object
                     is enforcing Java language access control and the underlying
                     field is inaccessible.
        - IllegalArgumentException: if the specified object is not
                     an instance of the class or interface declaring the
                     underlying field (or a subclass or implementor
                     thereof), or if the field value cannot be
                     converted to the type `int` by a
                     widening conversion.
        - NullPointerException: if the specified object is null
                     and the field is an instance field.
        - ExceptionInInitializerError: if the initialization provoked
                     by this method fails.

        See
        - Field.get
        """
        ...


    def getLong(self, obj: "Object") -> int:
        """
        Gets the value of a static or instance field of type
        `long` or of another primitive type convertible to
        type `long` via a widening conversion.

        Arguments
        - obj: the object to extract the `long` value
        from

        Returns
        - the value of the field converted to type `long`

        Raises
        - IllegalAccessException: if this `Field` object
                     is enforcing Java language access control and the underlying
                     field is inaccessible.
        - IllegalArgumentException: if the specified object is not
                     an instance of the class or interface declaring the
                     underlying field (or a subclass or implementor
                     thereof), or if the field value cannot be
                     converted to the type `long` by a
                     widening conversion.
        - NullPointerException: if the specified object is null
                     and the field is an instance field.
        - ExceptionInInitializerError: if the initialization provoked
                     by this method fails.

        See
        - Field.get
        """
        ...


    def getFloat(self, obj: "Object") -> float:
        """
        Gets the value of a static or instance field of type
        `float` or of another primitive type convertible to
        type `float` via a widening conversion.

        Arguments
        - obj: the object to extract the `float` value
        from

        Returns
        - the value of the field converted to type `float`

        Raises
        - IllegalAccessException: if this `Field` object
                     is enforcing Java language access control and the underlying
                     field is inaccessible.
        - IllegalArgumentException: if the specified object is not
                     an instance of the class or interface declaring the
                     underlying field (or a subclass or implementor
                     thereof), or if the field value cannot be
                     converted to the type `float` by a
                     widening conversion.
        - NullPointerException: if the specified object is null
                     and the field is an instance field.
        - ExceptionInInitializerError: if the initialization provoked
                     by this method fails.

        See
        - Field.get
        """
        ...


    def getDouble(self, obj: "Object") -> float:
        """
        Gets the value of a static or instance field of type
        `double` or of another primitive type convertible to
        type `double` via a widening conversion.

        Arguments
        - obj: the object to extract the `double` value
        from

        Returns
        - the value of the field converted to type `double`

        Raises
        - IllegalAccessException: if this `Field` object
                     is enforcing Java language access control and the underlying
                     field is inaccessible.
        - IllegalArgumentException: if the specified object is not
                     an instance of the class or interface declaring the
                     underlying field (or a subclass or implementor
                     thereof), or if the field value cannot be
                     converted to the type `double` by a
                     widening conversion.
        - NullPointerException: if the specified object is null
                     and the field is an instance field.
        - ExceptionInInitializerError: if the initialization provoked
                     by this method fails.

        See
        - Field.get
        """
        ...


    def set(self, obj: "Object", value: "Object") -> None:
        """
        Sets the field represented by this `Field` object on the
        specified object argument to the specified new value. The new
        value is automatically unwrapped if the underlying field has a
        primitive type.
        
        The operation proceeds as follows:
        
        If the underlying field is static, the `obj` argument is
        ignored; it may be null.
        
        Otherwise the underlying field is an instance field.  If the
        specified object argument is null, the method throws a
        `NullPointerException`.  If the specified object argument is not
        an instance of the class or interface declaring the underlying
        field, the method throws an `IllegalArgumentException`.
        
        If this `Field` object is enforcing Java language access control, and
        the underlying field is inaccessible, the method throws an
        `IllegalAccessException`.
        
        If the underlying field is final, this `Field` object has
        *write* access if and only if the following conditions are met:
        
        - .setAccessible(boolean) setAccessible(True) has succeeded for
            this `Field` object;
        - the field is non-static; and
        - the field's declaring class is not a Class.isHidden()
            hidden class; and
        - the field's declaring class is not a Class.isRecord()
            record class.
        
        If any of the above checks is not met, this method throws an
        `IllegalAccessException`.
        
         Setting a final field in this way
        is meaningful only during deserialization or reconstruction of
        instances of classes with blank final fields, before they are
        made available for access by other parts of a program. Use in
        any other context may have unpredictable effects, including cases
        in which other parts of a program continue to use the original
        value of this field.
        
        If the underlying field is of a primitive type, an unwrapping
        conversion is attempted to convert the new value to a value of
        a primitive type.  If this attempt fails, the method throws an
        `IllegalArgumentException`.
        
        If, after possible unwrapping, the new value cannot be
        converted to the type of the underlying field by an identity or
        widening conversion, the method throws an
        `IllegalArgumentException`.
        
        If the underlying field is static, the class that declared the
        field is initialized if it has not already been initialized.
        
        The field is set to the possibly unwrapped and widened new value.
        
        If the field is hidden in the type of `obj`,
        the field's value is set according to the preceding rules.

        Arguments
        - obj: the object whose field should be modified
        - value: the new value for the field of `obj`
        being modified

        Raises
        - IllegalAccessException: if this `Field` object
                     is enforcing Java language access control and the underlying
                     field is inaccessible or final;
                     or if this `Field` object has no write access.
        - IllegalArgumentException: if the specified object is not an
                     instance of the class or interface declaring the underlying
                     field (or a subclass or implementor thereof),
                     or if an unwrapping conversion fails.
        - NullPointerException: if the specified object is null
                     and the field is an instance field.
        - ExceptionInInitializerError: if the initialization provoked
                     by this method fails.
        """
        ...


    def setBoolean(self, obj: "Object", z: bool) -> None:
        """
        Sets the value of a field as a `boolean` on the specified object.
        This method is equivalent to
        `set(obj, zObj)`,
        where `zObj` is a `Boolean` object and
        `zObj.booleanValue() == z`.

        Arguments
        - obj: the object whose field should be modified
        - z: the new value for the field of `obj`
        being modified

        Raises
        - IllegalAccessException: if this `Field` object
                     is enforcing Java language access control and the underlying
                     field is either inaccessible or final;
                     or if this `Field` object has no write access.
        - IllegalArgumentException: if the specified object is not an
                     instance of the class or interface declaring the underlying
                     field (or a subclass or implementor thereof),
                     or if an unwrapping conversion fails.
        - NullPointerException: if the specified object is null
                     and the field is an instance field.
        - ExceptionInInitializerError: if the initialization provoked
                     by this method fails.

        See
        - Field.set
        """
        ...


    def setByte(self, obj: "Object", b: int) -> None:
        """
        Sets the value of a field as a `byte` on the specified object.
        This method is equivalent to
        `set(obj, bObj)`,
        where `bObj` is a `Byte` object and
        `bObj.byteValue() == b`.

        Arguments
        - obj: the object whose field should be modified
        - b: the new value for the field of `obj`
        being modified

        Raises
        - IllegalAccessException: if this `Field` object
                     is enforcing Java language access control and the underlying
                     field is either inaccessible or final;
                     or if this `Field` object has no write access.
        - IllegalArgumentException: if the specified object is not an
                     instance of the class or interface declaring the underlying
                     field (or a subclass or implementor thereof),
                     or if an unwrapping conversion fails.
        - NullPointerException: if the specified object is null
                     and the field is an instance field.
        - ExceptionInInitializerError: if the initialization provoked
                     by this method fails.

        See
        - Field.set
        """
        ...


    def setChar(self, obj: "Object", c: str) -> None:
        """
        Sets the value of a field as a `char` on the specified object.
        This method is equivalent to
        `set(obj, cObj)`,
        where `cObj` is a `Character` object and
        `cObj.charValue() == c`.

        Arguments
        - obj: the object whose field should be modified
        - c: the new value for the field of `obj`
        being modified

        Raises
        - IllegalAccessException: if this `Field` object
                     is enforcing Java language access control and the underlying
                     field is either inaccessible or final;
                     or if this `Field` object has no write access.
        - IllegalArgumentException: if the specified object is not an
                     instance of the class or interface declaring the underlying
                     field (or a subclass or implementor thereof),
                     or if an unwrapping conversion fails.
        - NullPointerException: if the specified object is null
                     and the field is an instance field.
        - ExceptionInInitializerError: if the initialization provoked
                     by this method fails.

        See
        - Field.set
        """
        ...


    def setShort(self, obj: "Object", s: int) -> None:
        """
        Sets the value of a field as a `short` on the specified object.
        This method is equivalent to
        `set(obj, sObj)`,
        where `sObj` is a `Short` object and
        `sObj.shortValue() == s`.

        Arguments
        - obj: the object whose field should be modified
        - s: the new value for the field of `obj`
        being modified

        Raises
        - IllegalAccessException: if this `Field` object
                     is enforcing Java language access control and the underlying
                     field is either inaccessible or final;
                     or if this `Field` object has no write access.
        - IllegalArgumentException: if the specified object is not an
                     instance of the class or interface declaring the underlying
                     field (or a subclass or implementor thereof),
                     or if an unwrapping conversion fails.
        - NullPointerException: if the specified object is null
                     and the field is an instance field.
        - ExceptionInInitializerError: if the initialization provoked
                     by this method fails.

        See
        - Field.set
        """
        ...


    def setInt(self, obj: "Object", i: int) -> None:
        """
        Sets the value of a field as an `int` on the specified object.
        This method is equivalent to
        `set(obj, iObj)`,
        where `iObj` is an `Integer` object and
        `iObj.intValue() == i`.

        Arguments
        - obj: the object whose field should be modified
        - i: the new value for the field of `obj`
        being modified

        Raises
        - IllegalAccessException: if this `Field` object
                     is enforcing Java language access control and the underlying
                     field is either inaccessible or final;
                     or if this `Field` object has no write access.
        - IllegalArgumentException: if the specified object is not an
                     instance of the class or interface declaring the underlying
                     field (or a subclass or implementor thereof),
                     or if an unwrapping conversion fails.
        - NullPointerException: if the specified object is null
                     and the field is an instance field.
        - ExceptionInInitializerError: if the initialization provoked
                     by this method fails.

        See
        - Field.set
        """
        ...


    def setLong(self, obj: "Object", l: int) -> None:
        """
        Sets the value of a field as a `long` on the specified object.
        This method is equivalent to
        `set(obj, lObj)`,
        where `lObj` is a `Long` object and
        `lObj.longValue() == l`.

        Arguments
        - obj: the object whose field should be modified
        - l: the new value for the field of `obj`
        being modified

        Raises
        - IllegalAccessException: if this `Field` object
                     is enforcing Java language access control and the underlying
                     field is either inaccessible or final;
                     or if this `Field` object has no write access.
        - IllegalArgumentException: if the specified object is not an
                     instance of the class or interface declaring the underlying
                     field (or a subclass or implementor thereof),
                     or if an unwrapping conversion fails.
        - NullPointerException: if the specified object is null
                     and the field is an instance field.
        - ExceptionInInitializerError: if the initialization provoked
                     by this method fails.

        See
        - Field.set
        """
        ...


    def setFloat(self, obj: "Object", f: float) -> None:
        """
        Sets the value of a field as a `float` on the specified object.
        This method is equivalent to
        `set(obj, fObj)`,
        where `fObj` is a `Float` object and
        `fObj.floatValue() == f`.

        Arguments
        - obj: the object whose field should be modified
        - f: the new value for the field of `obj`
        being modified

        Raises
        - IllegalAccessException: if this `Field` object
                     is enforcing Java language access control and the underlying
                     field is either inaccessible or final;
                     or if this `Field` object has no write access.
        - IllegalArgumentException: if the specified object is not an
                     instance of the class or interface declaring the underlying
                     field (or a subclass or implementor thereof),
                     or if an unwrapping conversion fails.
        - NullPointerException: if the specified object is null
                     and the field is an instance field.
        - ExceptionInInitializerError: if the initialization provoked
                     by this method fails.

        See
        - Field.set
        """
        ...


    def setDouble(self, obj: "Object", d: float) -> None:
        """
        Sets the value of a field as a `double` on the specified object.
        This method is equivalent to
        `set(obj, dObj)`,
        where `dObj` is a `Double` object and
        `dObj.doubleValue() == d`.

        Arguments
        - obj: the object whose field should be modified
        - d: the new value for the field of `obj`
        being modified

        Raises
        - IllegalAccessException: if this `Field` object
                     is enforcing Java language access control and the underlying
                     field is either inaccessible or final;
                     or if this `Field` object has no write access.
        - IllegalArgumentException: if the specified object is not an
                     instance of the class or interface declaring the underlying
                     field (or a subclass or implementor thereof),
                     or if an unwrapping conversion fails.
        - NullPointerException: if the specified object is null
                     and the field is an instance field.
        - ExceptionInInitializerError: if the initialization provoked
                     by this method fails.

        See
        - Field.set
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


    def getAnnotationsByType(self, annotationClass: type["T"]) -> list["T"]:
        """
        Raises
        - NullPointerException: 

        Since
        - 1.8
        """
        ...


    def getDeclaredAnnotations(self) -> list["Annotation"]:
        """

        """
        ...


    def getAnnotatedType(self) -> "AnnotatedType":
        """
        Returns an AnnotatedType object that represents the use of a type to specify
        the declared type of the field represented by this Field.

        Returns
        - an object representing the declared type of the field
        represented by this Field

        Since
        - 1.8
        """
        ...
