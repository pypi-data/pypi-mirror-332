"""
Python module generated from Java source file java.lang.invoke.MethodType

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.lang.constant import ClassDesc
from java.lang.constant import Constable
from java.lang.constant import MethodTypeDesc
from java.lang.invoke import *
from java.lang.ref import Reference
from java.lang.ref import ReferenceQueue
from java.lang.ref import WeakReference
from java.util import Arrays
from java.util import Collections
from java.util import NoSuchElementException
from java.util import Objects
from java.util import Optional
from java.util import StringJoiner
from java.util.concurrent import ConcurrentHashMap
from java.util.concurrent import ConcurrentMap
from java.util.stream import Stream
from jdk.internal.vm.annotation import Stable
from sun.invoke.util import BytecodeDescriptor
from sun.invoke.util import VerifyType
from sun.invoke.util import Wrapper
from sun.security.util import SecurityConstants
from typing import Any, Callable, Iterable, Tuple


class MethodType(Constable, OfMethod, Serializable):
    """
    A method type represents the arguments and return type accepted and
    returned by a method handle, or the arguments and return type passed
    and expected  by a method handle caller.  Method types must be properly
    matched between a method handle and all its callers,
    and the JVM's operations enforce this matching at, specifically
    during calls to MethodHandle.invokeExact MethodHandle.invokeExact
    and MethodHandle.invoke MethodHandle.invoke, and during execution
    of `invokedynamic` instructions.
    
    The structure is a return type accompanied by any number of parameter types.
    The types (primitive, `void`, and reference) are represented by Class objects.
    (For ease of exposition, we treat `void` as if it were a type.
    In fact, it denotes the absence of a return type.)
    
    All instances of `MethodType` are immutable.
    Two instances are completely interchangeable if they compare equal.
    Equality depends on pairwise correspondence of the return and parameter types and on nothing else.
    
    This type can be created only by factory methods.
    All factory methods may cache values, though caching is not guaranteed.
    Some factory methods are static, while others are virtual methods which
    modify precursor method types, e.g., by changing a selected parameter.
    
    Factory methods which operate on groups of parameter types
    are systematically presented in two versions, so that both Java arrays and
    Java lists can be used to work with groups of parameter types.
    The query methods `parameterArray` and `parameterList`
    also provide a choice between arrays and lists.
    
    `MethodType` objects are sometimes derived from bytecode instructions
    such as `invokedynamic`, specifically from the type descriptor strings associated
    with the instructions in a class file's constant pool.
    
    Like classes and strings, method types can also be represented directly
    in a class file's constant pool as constants.
    A method type may be loaded by an `ldc` instruction which refers
    to a suitable `CONSTANT_MethodType` constant pool entry.
    The entry refers to a `CONSTANT_Utf8` spelling for the descriptor string.
    (For full details on method type constants, see sections 4.4.8 and 5.4.3.5 of the Java Virtual Machine
    Specification.)
    
    When the JVM materializes a `MethodType` from a descriptor string,
    all classes named in the descriptor must be accessible, and will be loaded.
    (But the classes need not be initialized, as is the case with a `CONSTANT_Class`.)
    This loading may occur at any time before the `MethodType` object is first derived.
    
    **<a id="descriptor">Nominal Descriptors</a>**
    
    A `MethodType` can be described in MethodTypeDesc nominal form
    if and only if all of the parameter types and return type can be described
    with a Class.describeConstable() nominal descriptor represented by
    ClassDesc.  If a method type can be described nominally, then:
    
    - The method type has a MethodTypeDesc nominal descriptor
        returned by .describeConstable() MethodType::describeConstable.
    - The descriptor string returned by
        .descriptorString() MethodType::descriptorString or
        .toMethodDescriptorString() MethodType::toMethodDescriptorString
        for the method type is a method descriptor (JVMS 4.3.3).
    
    
    If any of the parameter types or return type cannot be described
    nominally, i.e. Class.describeConstable() Class::describeConstable
    returns an empty optional for that type,
    then the method type cannot be described nominally:
    
    - The method type has no MethodTypeDesc nominal descriptor and
        .describeConstable() MethodType::describeConstable returns
        an empty optional.
    - The descriptor string returned by
        .descriptorString() MethodType::descriptorString or
        .toMethodDescriptorString() MethodType::toMethodDescriptorString
        for the method type is not a type descriptor.

    Author(s)
    - John Rose, JSR 292 EG

    Since
    - 1.7
    """

    @staticmethod
    def methodType(rtype: type[Any], ptypes: list[type[Any]]) -> "MethodType":
        """
        Finds or creates an instance of the given method type.

        Arguments
        - rtype: the return type
        - ptypes: the parameter types

        Returns
        - a method type with the given components

        Raises
        - NullPointerException: if `rtype` or `ptypes` or any element of `ptypes` is null
        - IllegalArgumentException: if any element of `ptypes` is `void.class`
        """
        ...


    @staticmethod
    def methodType(rtype: type[Any], ptypes: list[type[Any]]) -> "MethodType":
        """
        Finds or creates a method type with the given components.
        Convenience method for .methodType(java.lang.Class, java.lang.Class[]) methodType.

        Arguments
        - rtype: the return type
        - ptypes: the parameter types

        Returns
        - a method type with the given components

        Raises
        - NullPointerException: if `rtype` or `ptypes` or any element of `ptypes` is null
        - IllegalArgumentException: if any element of `ptypes` is `void.class`
        """
        ...


    @staticmethod
    def methodType(rtype: type[Any], ptype0: type[Any], *ptypes: Tuple[type[Any], ...]) -> "MethodType":
        """
        Finds or creates a method type with the given components.
        Convenience method for .methodType(java.lang.Class, java.lang.Class[]) methodType.
        The leading parameter type is prepended to the remaining array.

        Arguments
        - rtype: the return type
        - ptype0: the first parameter type
        - ptypes: the remaining parameter types

        Returns
        - a method type with the given components

        Raises
        - NullPointerException: if `rtype` or `ptype0` or `ptypes` or any element of `ptypes` is null
        - IllegalArgumentException: if `ptype0` or `ptypes` or any element of `ptypes` is `void.class`
        """
        ...


    @staticmethod
    def methodType(rtype: type[Any]) -> "MethodType":
        """
        Finds or creates a method type with the given components.
        Convenience method for .methodType(java.lang.Class, java.lang.Class[]) methodType.
        The resulting method has no parameter types.

        Arguments
        - rtype: the return type

        Returns
        - a method type with the given return value

        Raises
        - NullPointerException: if `rtype` is null
        """
        ...


    @staticmethod
    def methodType(rtype: type[Any], ptype0: type[Any]) -> "MethodType":
        """
        Finds or creates a method type with the given components.
        Convenience method for .methodType(java.lang.Class, java.lang.Class[]) methodType.
        The resulting method has the single given parameter type.

        Arguments
        - rtype: the return type
        - ptype0: the parameter type

        Returns
        - a method type with the given return value and parameter type

        Raises
        - NullPointerException: if `rtype` or `ptype0` is null
        - IllegalArgumentException: if `ptype0` is `void.class`
        """
        ...


    @staticmethod
    def methodType(rtype: type[Any], ptypes: "MethodType") -> "MethodType":
        """
        Finds or creates a method type with the given components.
        Convenience method for .methodType(java.lang.Class, java.lang.Class[]) methodType.
        The resulting method has the same parameter types as `ptypes`,
        and the specified return type.

        Arguments
        - rtype: the return type
        - ptypes: the method type which supplies the parameter types

        Returns
        - a method type with the given components

        Raises
        - NullPointerException: if `rtype` or `ptypes` is null
        """
        ...


    @staticmethod
    def genericMethodType(objectArgCount: int, finalArray: bool) -> "MethodType":
        """
        Finds or creates a method type whose components are `Object` with an optional trailing `Object[]` array.
        Convenience method for .methodType(java.lang.Class, java.lang.Class[]) methodType.
        All parameters and the return type will be `Object`,
        except the final array parameter if any, which will be `Object[]`.

        Arguments
        - objectArgCount: number of parameters (excluding the final array parameter if any)
        - finalArray: whether there will be a trailing array parameter, of type `Object[]`

        Returns
        - a generally applicable method type, for all calls of the given fixed argument count and a collected array of further arguments

        Raises
        - IllegalArgumentException: if `objectArgCount` is negative or greater than 255 (or 254, if `finalArray` is True)

        See
        - .genericMethodType(int)
        """
        ...


    @staticmethod
    def genericMethodType(objectArgCount: int) -> "MethodType":
        """
        Finds or creates a method type whose components are all `Object`.
        Convenience method for .methodType(java.lang.Class, java.lang.Class[]) methodType.
        All parameters and the return type will be Object.

        Arguments
        - objectArgCount: number of parameters

        Returns
        - a generally applicable method type, for all calls of the given argument count

        Raises
        - IllegalArgumentException: if `objectArgCount` is negative or greater than 255

        See
        - .genericMethodType(int, boolean)
        """
        ...


    def changeParameterType(self, num: int, nptype: type[Any]) -> "MethodType":
        """
        Finds or creates a method type with a single different parameter type.
        Convenience method for .methodType(java.lang.Class, java.lang.Class[]) methodType.

        Arguments
        - num: the index (zero-based) of the parameter type to change
        - nptype: a new parameter type to replace the old one with

        Returns
        - the same type, except with the selected parameter changed

        Raises
        - IndexOutOfBoundsException: if `num` is not a valid index into `parameterArray()`
        - IllegalArgumentException: if `nptype` is `void.class`
        - NullPointerException: if `nptype` is null
        """
        ...


    def insertParameterTypes(self, num: int, *ptypesToInsert: Tuple[type[Any], ...]) -> "MethodType":
        """
        Finds or creates a method type with additional parameter types.
        Convenience method for .methodType(java.lang.Class, java.lang.Class[]) methodType.

        Arguments
        - num: the position (zero-based) of the inserted parameter type(s)
        - ptypesToInsert: zero or more new parameter types to insert into the parameter list

        Returns
        - the same type, except with the selected parameter(s) inserted

        Raises
        - IndexOutOfBoundsException: if `num` is negative or greater than `parameterCount()`
        - IllegalArgumentException: if any element of `ptypesToInsert` is `void.class`
                                         or if the resulting method type would have more than 255 parameter slots
        - NullPointerException: if `ptypesToInsert` or any of its elements is null
        """
        ...


    def appendParameterTypes(self, *ptypesToInsert: Tuple[type[Any], ...]) -> "MethodType":
        """
        Finds or creates a method type with additional parameter types.
        Convenience method for .methodType(java.lang.Class, java.lang.Class[]) methodType.

        Arguments
        - ptypesToInsert: zero or more new parameter types to insert after the end of the parameter list

        Returns
        - the same type, except with the selected parameter(s) appended

        Raises
        - IllegalArgumentException: if any element of `ptypesToInsert` is `void.class`
                                         or if the resulting method type would have more than 255 parameter slots
        - NullPointerException: if `ptypesToInsert` or any of its elements is null
        """
        ...


    def insertParameterTypes(self, num: int, ptypesToInsert: list[type[Any]]) -> "MethodType":
        """
        Finds or creates a method type with additional parameter types.
        Convenience method for .methodType(java.lang.Class, java.lang.Class[]) methodType.

        Arguments
        - num: the position (zero-based) of the inserted parameter type(s)
        - ptypesToInsert: zero or more new parameter types to insert into the parameter list

        Returns
        - the same type, except with the selected parameter(s) inserted

        Raises
        - IndexOutOfBoundsException: if `num` is negative or greater than `parameterCount()`
        - IllegalArgumentException: if any element of `ptypesToInsert` is `void.class`
                                         or if the resulting method type would have more than 255 parameter slots
        - NullPointerException: if `ptypesToInsert` or any of its elements is null
        """
        ...


    def appendParameterTypes(self, ptypesToInsert: list[type[Any]]) -> "MethodType":
        """
        Finds or creates a method type with additional parameter types.
        Convenience method for .methodType(java.lang.Class, java.lang.Class[]) methodType.

        Arguments
        - ptypesToInsert: zero or more new parameter types to insert after the end of the parameter list

        Returns
        - the same type, except with the selected parameter(s) appended

        Raises
        - IllegalArgumentException: if any element of `ptypesToInsert` is `void.class`
                                         or if the resulting method type would have more than 255 parameter slots
        - NullPointerException: if `ptypesToInsert` or any of its elements is null
        """
        ...


    def dropParameterTypes(self, start: int, end: int) -> "MethodType":
        """
        Finds or creates a method type with some parameter types omitted.
        Convenience method for .methodType(java.lang.Class, java.lang.Class[]) methodType.

        Arguments
        - start: the index (zero-based) of the first parameter type to remove
        - end: the index (greater than `start`) of the first parameter type after not to remove

        Returns
        - the same type, except with the selected parameter(s) removed

        Raises
        - IndexOutOfBoundsException: if `start` is negative or greater than `parameterCount()`
                                         or if `end` is negative or greater than `parameterCount()`
                                         or if `start` is greater than `end`
        """
        ...


    def changeReturnType(self, nrtype: type[Any]) -> "MethodType":
        """
        Finds or creates a method type with a different return type.
        Convenience method for .methodType(java.lang.Class, java.lang.Class[]) methodType.

        Arguments
        - nrtype: a return parameter type to replace the old one with

        Returns
        - the same type, except with the return type change

        Raises
        - NullPointerException: if `nrtype` is null
        """
        ...


    def hasPrimitives(self) -> bool:
        """
        Reports if this type contains a primitive argument or return value.
        The return type `void` counts as a primitive.

        Returns
        - True if any of the types are primitives
        """
        ...


    def hasWrappers(self) -> bool:
        """
        Reports if this type contains a wrapper argument or return value.
        Wrappers are types which box primitive values, such as Integer.
        The reference type `java.lang.Void` counts as a wrapper,
        if it occurs as a return type.

        Returns
        - True if any of the types are wrappers
        """
        ...


    def erase(self) -> "MethodType":
        """
        Erases all reference types to `Object`.
        Convenience method for .methodType(java.lang.Class, java.lang.Class[]) methodType.
        All primitive types (including `void`) will remain unchanged.

        Returns
        - a version of the original type with all reference types replaced
        """
        ...


    def generic(self) -> "MethodType":
        """
        Converts all types, both reference and primitive, to `Object`.
        Convenience method for .genericMethodType(int) genericMethodType.
        The expression `type.wrap().erase()` produces the same value
        as `type.generic()`.

        Returns
        - a version of the original type with all types replaced
        """
        ...


    def wrap(self) -> "MethodType":
        """
        Converts all primitive types to their corresponding wrapper types.
        Convenience method for .methodType(java.lang.Class, java.lang.Class[]) methodType.
        All reference types (including wrapper types) will remain unchanged.
        A `void` return type is changed to the type `java.lang.Void`.
        The expression `type.wrap().erase()` produces the same value
        as `type.generic()`.

        Returns
        - a version of the original type with all primitive types replaced
        """
        ...


    def unwrap(self) -> "MethodType":
        """
        Converts all wrapper types to their corresponding primitive types.
        Convenience method for .methodType(java.lang.Class, java.lang.Class[]) methodType.
        All primitive types (including `void`) will remain unchanged.
        A return type of `java.lang.Void` is changed to `void`.

        Returns
        - a version of the original type with all wrapper types replaced
        """
        ...


    def parameterType(self, num: int) -> type[Any]:
        """
        Returns the parameter type at the specified index, within this method type.

        Arguments
        - num: the index (zero-based) of the desired parameter type

        Returns
        - the selected parameter type

        Raises
        - IndexOutOfBoundsException: if `num` is not a valid index into `parameterArray()`
        """
        ...


    def parameterCount(self) -> int:
        """
        Returns the number of parameter types in this method type.

        Returns
        - the number of parameter types
        """
        ...


    def returnType(self) -> type[Any]:
        """
        Returns the return type of this method type.

        Returns
        - the return type
        """
        ...


    def parameterList(self) -> list[type[Any]]:
        """
        Presents the parameter types as a list (a convenience method).
        The list will be immutable.

        Returns
        - the parameter types (as an immutable list)
        """
        ...


    def lastParameterType(self) -> type[Any]:
        """
        Returns the last parameter type of this method type.
        If this type has no parameters, the sentinel value
        `void.class` is returned instead.

        Returns
        - the last parameter type if any, else `void.class`

        Since
        - 10

        Unknown Tags
        - 
        The sentinel value is chosen so that reflective queries can be
        made directly against the result value.
        The sentinel value cannot be confused with a real parameter,
        since `void` is never acceptable as a parameter type.
        For variable arity invocation modes, the expression
        Class.getComponentType lastParameterType().getComponentType()
        is useful to query the type of the "varargs" parameter.
        """
        ...


    def parameterArray(self) -> list[type[Any]]:
        """
        Presents the parameter types as an array (a convenience method).
        Changes to the array will not result in changes to the type.

        Returns
        - the parameter types (as a fresh copy if necessary)
        """
        ...


    def equals(self, x: "Object") -> bool:
        ...


    def hashCode(self) -> int:
        """
        Returns the hash code value for this method type.
        It is defined to be the same as the hashcode of a List
        whose elements are the return type followed by the
        parameter types.

        Returns
        - the hash code value for this method type

        See
        - List.hashCode()
        """
        ...


    def toString(self) -> str:
        """
        Returns a string representation of the method type,
        of the form `"(PT0,PT1...)RT"`.
        The string representation of a method type is a
        parenthesis enclosed, comma separated list of type names,
        followed immediately by the return type.
        
        Each type is represented by its
        java.lang.Class.getSimpleName simple name.
        """
        ...


    @staticmethod
    def fromMethodDescriptorString(descriptor: str, loader: "ClassLoader") -> "MethodType":
        """
        Finds or creates an instance of a method type, given the spelling of its bytecode descriptor.
        Convenience method for .methodType(java.lang.Class, java.lang.Class[]) methodType.
        Any class or interface name embedded in the descriptor string will be
        resolved by the given loader (or if it is null, on the system class loader).
        
        Note that it is possible to encounter method types which cannot be
        constructed by this method, because their component types are
        not all reachable from a common class loader.
        
        This method is included for the benefit of applications that must
        generate bytecodes that process method handles and `invokedynamic`.

        Arguments
        - descriptor: a bytecode-level type descriptor string "(T...)T"
        - loader: the class loader in which to look up the types

        Returns
        - a method type matching the bytecode-level type descriptor

        Raises
        - NullPointerException: if the string is null
        - IllegalArgumentException: if the string is not well-formed
        - TypeNotPresentException: if a named type cannot be found
        - SecurityException: if the security manager is present and
                `loader` is `null` and the caller does not have the
                RuntimePermission`("getClassLoader")`
        """
        ...


    def toMethodDescriptorString(self) -> str:
        """
        Returns a descriptor string for the method type.  This method
        is equivalent to calling .descriptorString() MethodType::descriptorString.
        
        
        Note that this is not a strict inverse of .fromMethodDescriptorString fromMethodDescriptorString.
        Two distinct classes which share a common name but have different class loaders
        will appear identical when viewed within descriptor strings.
        
        This method is included for the benefit of applications that must
        generate bytecodes that process method handles and `invokedynamic`.
        .fromMethodDescriptorString(java.lang.String, java.lang.ClassLoader) fromMethodDescriptorString,
        because the latter requires a suitable class loader argument.

        Returns
        - the descriptor string for this method type

        See
        - <a href=".descriptor">Nominal Descriptor for `MethodType`</a>

        Unknown Tags
        - 4.3.3 Method Descriptors
        """
        ...


    def descriptorString(self) -> str:
        """
        Returns a descriptor string for this method type.
        
        
        If this method type can be <a href="#descriptor">described nominally</a>,
        then the result is a method type descriptor (JVMS 4.3.3).
        MethodTypeDesc MethodTypeDesc for this method type
        can be produced by calling MethodTypeDesc.ofDescriptor(String)
        MethodTypeDesc::ofDescriptor with the result descriptor string.
        
        If this method type cannot be <a href="#descriptor">described nominally</a>
        and the result is a string of the form:
        <blockquote>`"(<parameter-descriptors>)<return-descriptor>"`</blockquote>
        where `<parameter-descriptors>` is the concatenation of the
        Class.descriptorString() descriptor string of all
        of the parameter types and the Class.descriptorString() descriptor string
        of the return type. No java.lang.constant.MethodTypeDesc MethodTypeDesc
        can be produced from the result string.

        Returns
        - the descriptor string for this method type

        See
        - <a href=".descriptor">Nominal Descriptor for `MethodType`</a>

        Since
        - 12

        Unknown Tags
        - 4.3.3 Method Descriptors
        """
        ...


    def describeConstable(self) -> "Optional"["MethodTypeDesc"]:
        """
        Returns a nominal descriptor for this instance, if one can be
        constructed, or an empty Optional if one cannot be.

        Returns
        - An Optional containing the resulting nominal descriptor,
        or an empty Optional if one cannot be constructed.

        See
        - <a href=".descriptor">Nominal Descriptor for `MethodType`</a>

        Since
        - 12
        """
        ...
