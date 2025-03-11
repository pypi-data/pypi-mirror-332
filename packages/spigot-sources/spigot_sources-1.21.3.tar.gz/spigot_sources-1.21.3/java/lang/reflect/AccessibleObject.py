"""
Python module generated from Java source file java.lang.reflect.AccessibleObject

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.lang.invoke import MethodHandle
from java.lang.ref import WeakReference
from java.lang.reflect import *
from java.security import AccessController
from jdk.internal.access import SharedSecrets
from jdk.internal.misc import VM
from jdk.internal.reflect import CallerSensitive
from jdk.internal.reflect import Reflection
from jdk.internal.reflect import ReflectionFactory
from sun.security.action import GetPropertyAction
from sun.security.util import SecurityConstants
from typing import Any, Callable, Iterable, Tuple


class AccessibleObject(AnnotatedElement):
    """
    The `AccessibleObject` class is the base class for `Field`,
    `Method`, and `Constructor` objects (known as *reflected
    objects*). It provides the ability to flag a reflected object as
    suppressing checks for Java language access control when it is used. This
    permits sophisticated applications with sufficient privilege, such as Java
    Object Serialization or other persistence mechanisms, to manipulate objects
    in a manner that would normally be prohibited.
    
     Java language access control prevents use of private members outside
    their top-level class; package access members outside their package; protected members
    outside their package or subclasses; and public members outside their
    module unless they are declared in an Module.isExported(String,Module)
    exported package and the user Module.canRead reads their module. By
    default, Java language access control is enforced (with one variation) when
    `Field`s, `Method`s, or `Constructor`s are used to get or
    set fields, to invoke methods, or to create and initialize new instances of
    classes, respectively. Every reflected object checks that the code using it
    is in an appropriate class, package, or module. The check when invoked by
    <a href="/../specs/jni/index.html">JNI code</a> with no Java
    class on the stack only succeeds if the member and the declaring class are
    public, and the class is in a package that is exported to all modules. 
    
     The one variation from Java language access control is that the checks
    by reflected objects assume readability. That is, the module containing
    the use of a reflected object is assumed to read the module in which
    the underlying field, method, or constructor is declared. 
    
     Whether the checks for Java language access control can be suppressed
    (and thus, whether access can be enabled) depends on whether the reflected
    object corresponds to a member in an exported or open package
    (see .setAccessible(boolean)). 

    Since
    - 1.2

    Unknown Tags
    - 6.6 Access Control
    - 9
    """

    @staticmethod
    def setAccessible(array: list["AccessibleObject"], flag: bool) -> None:
        """
        Convenience method to set the `accessible` flag for an
        array of reflected objects with a single security check (for efficiency).
        
         This method may be used to enable access to all reflected objects in
        the array when access to each reflected object can be enabled as
        specified by .setAccessible(boolean) setAccessible(boolean). 
        
        If there is a security manager, its
        `checkPermission` method is first called with a
        `ReflectPermission("suppressAccessChecks")` permission.
        
        A `SecurityException` is also thrown if any of the elements of
        the input `array` is a java.lang.reflect.Constructor
        object for the class `java.lang.Class` and `flag` is True.

        Arguments
        - array: the array of AccessibleObjects
        - flag: the new value for the `accessible` flag
                     in each object

        Raises
        - InaccessibleObjectException: if access cannot be enabled for all
                objects in the array
        - SecurityException: if the request is denied by the security manager
                or an element in the array is a constructor for `java.lang.Class`

        See
        - ReflectPermission

        Unknown Tags
        - 9
        """
        ...


    def setAccessible(self, flag: bool) -> None:
        """
        Set the `accessible` flag for this reflected object to
        the indicated boolean value.  A value of `True` indicates that
        the reflected object should suppress checks for Java language access
        control when it is used. A value of `False` indicates that
        the reflected object should enforce checks for Java language access
        control when it is used, with the variation noted in the class description.
        
         This method may be used by a caller in class `C` to enable
        access to a Member member of Member.getDeclaringClass()
        declaring class `D` if any of the following hold: 
        
        
            -  `C` and `D` are in the same module. 
        
            -  The member is `public` and `D` is `public` in
            a package that the module containing `D` Module.isExported(String,Module) exports to at least the module
            containing `C`. 
        
            -  The member is `protected` `static`, `D` is
            `public` in a package that the module containing `D`
            exports to at least the module containing `C`, and `C`
            is a subclass of `D`. 
        
            -  `D` is in a package that the module containing `D`
            Module.isOpen(String,Module) opens to at least the module
            containing `C`.
            All packages in unnamed and open modules are open to all modules and
            so this method always succeeds when `D` is in an unnamed or
            open module. 
        
        
         This method cannot be used to enable access to private members,
        members with default (package) access, protected instance members, or
        protected constructors when the declaring class is in a different module
        to the caller and the package containing the declaring class is not open
        to the caller's module. 
        
         This method cannot be used to enable Field.set *write*
        access to a *non-modifiable* final field.  The following fields
        are non-modifiable:
        
        - static final fields declared in any class or interface
        - final fields declared in a Class.isHidden() hidden class
        - final fields declared in a Class.isRecord() record
        
         The `accessible` flag when `True` suppresses Java language access
        control checks to only enable Field.get *read* access to
        these non-modifiable final fields.
        
         If there is a security manager, its
        `checkPermission` method is first called with a
        `ReflectPermission("suppressAccessChecks")` permission.

        Arguments
        - flag: the new value for the `accessible` flag

        Raises
        - InaccessibleObjectException: if access cannot be enabled
        - SecurityException: if the request is denied by the security manager

        See
        - java.lang.invoke.MethodHandles.privateLookupIn

        Unknown Tags
        - 9
        """
        ...


    def trySetAccessible(self) -> bool:
        """
        Set the `accessible` flag for this reflected object to `True`
        if possible. This method sets the `accessible` flag, as if by
        invoking .setAccessible(boolean) setAccessible(True), and returns
        the possibly-updated value for the `accessible` flag. If access
        cannot be enabled, i.e. the checks or Java language access control cannot
        be suppressed, this method returns `False` (as opposed to `setAccessible(True)` throwing `InaccessibleObjectException` when
        it fails).
        
         This method is a no-op if the `accessible` flag for
        this reflected object is `True`.
        
         For example, a caller can invoke `trySetAccessible`
        on a `Method` object for a private instance method
        `p.T::privateMethod` to suppress the checks for Java language access
        control when the `Method` is invoked.
        If `p.T` class is in a different module to the caller and
        package `p` is open to at least the caller's module,
        the code below successfully sets the `accessible` flag
        to `True`.
        
        ```
        `p.T obj = ....;  // instance of p.T
            :
            Method m = p.T.class.getDeclaredMethod("privateMethod");
            if (m.trySetAccessible()) {
                m.invoke(obj);` else {
                // package p is not opened to the caller to access private member of T
                ...
            }
        }```
        
         If there is a security manager, its `checkPermission` method
        is first called with a `ReflectPermission("suppressAccessChecks")`
        permission. 

        Returns
        - `True` if the `accessible` flag is set to `True`;
                `False` if access cannot be enabled.

        Raises
        - SecurityException: if the request is denied by the security manager

        See
        - java.lang.invoke.MethodHandles.privateLookupIn

        Since
        - 9
        """
        ...


    def isAccessible(self) -> bool:
        """
        Get the value of the `accessible` flag for this reflected object.

        Returns
        - the value of the object's `accessible` flag

        Deprecated
        - This method is deprecated because its name hints that it checks
        if the reflected object is accessible when it actually indicates
        if the checks for Java language access control are suppressed.
        This method may return `False` on a reflected object that is
        accessible to the caller. To test if this reflected object is accessible,
        it should use .canAccess(Object).

        Unknown Tags
        - 9
        """
        ...


    def canAccess(self, obj: "Object") -> bool:
        """
        Test if the caller can access this reflected object. If this reflected
        object corresponds to an instance method or field then this method tests
        if the caller can access the given `obj` with the reflected object.
        For instance methods or fields then the `obj` argument must be an
        instance of the Member.getDeclaringClass() declaring class. For
        static members and constructors then `obj` must be `null`.
        
         This method returns `True` if the `accessible` flag
        is set to `True`, i.e. the checks for Java language access control
        are suppressed, or if the caller can access the member as
        specified in <cite>The Java Language Specification</cite>,
        with the variation noted in the class description. 

        Arguments
        - obj: an instance object of the declaring class of this reflected
                   object if it is an instance method or field

        Returns
        - `True` if the caller can access this reflected object.

        Raises
        - IllegalArgumentException: 
                -  if this reflected object is a static member or constructor and
                     the given `obj` is non-`null`, or 
                -  if this reflected object is an instance method or field
                     and the given `obj` is `null` or of type
                     that is not a subclass of the Member.getDeclaringClass()
                     declaring class of the member.
                

        See
        - .setAccessible(boolean)

        Since
        - 9

        Unknown Tags
        - 6.6 Access Control
        """
        ...


    def getAnnotation(self, annotationClass: type["T"]) -> "T":
        """
        
        
         Note that any annotation returned by this method is a
        declaration annotation.

        Raises
        - NullPointerException: 

        Since
        - 1.5

        Unknown Tags
        - The default implementation throws UnsupportedOperationException; subclasses should override this method.
        """
        ...


    def isAnnotationPresent(self, annotationClass: type["Annotation"]) -> bool:
        """
        Raises
        - NullPointerException: 

        Since
        - 1.5
        """
        ...


    def getAnnotationsByType(self, annotationClass: type["T"]) -> list["T"]:
        """
        
        
         Note that any annotations returned by this method are
        declaration annotations.

        Raises
        - NullPointerException: 

        Since
        - 1.8

        Unknown Tags
        - The default implementation throws UnsupportedOperationException; subclasses should override this method.
        """
        ...


    def getAnnotations(self) -> list["Annotation"]:
        """
        
        
         Note that any annotations returned by this method are
        declaration annotations.

        Since
        - 1.5
        """
        ...


    def getDeclaredAnnotation(self, annotationClass: type["T"]) -> "T":
        """
        
        
         Note that any annotation returned by this method is a
        declaration annotation.

        Raises
        - NullPointerException: 

        Since
        - 1.8
        """
        ...


    def getDeclaredAnnotationsByType(self, annotationClass: type["T"]) -> list["T"]:
        """
        
        
         Note that any annotations returned by this method are
        declaration annotations.

        Raises
        - NullPointerException: 

        Since
        - 1.8
        """
        ...


    def getDeclaredAnnotations(self) -> list["Annotation"]:
        """
        
        
         Note that any annotations returned by this method are
        declaration annotations.

        Since
        - 1.5

        Unknown Tags
        - The default implementation throws UnsupportedOperationException; subclasses should override this method.
        """
        ...
