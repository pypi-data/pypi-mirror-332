"""
Python module generated from Java source file java.lang.invoke.MethodHandles

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from java.lang.constant import ConstantDescs
from java.lang.invoke import *
from java.lang.invoke.LambdaForm import BasicType
from java.lang.reflect import Constructor
from java.lang.reflect import Field
from java.lang.reflect import Member
from java.lang.reflect import Method
from java.lang.reflect import Modifier
from java.lang.reflect import ReflectPermission
from java.security import ProtectionDomain
from java.util import Arrays
from java.util import BitSet
from java.util import Iterator
from java.util import Objects
from java.util.concurrent import ConcurrentHashMap
from java.util.stream import Stream
from jdk.internal.access import SharedSecrets
from jdk.internal.misc import Unsafe
from jdk.internal.misc import VM
from jdk.internal.org.objectweb.asm import ClassReader
from jdk.internal.org.objectweb.asm import Opcodes
from jdk.internal.org.objectweb.asm import Type
from jdk.internal.reflect import CallerSensitive
from jdk.internal.reflect import Reflection
from jdk.internal.vm.annotation import ForceInline
from sun.invoke.util import ValueConversions
from sun.invoke.util import VerifyAccess
from sun.invoke.util import Wrapper
from sun.reflect.misc import ReflectUtil
from sun.security.util import SecurityConstants
from typing import Any, Callable, Iterable, Tuple


class MethodHandles:
    """
    This class consists exclusively of static methods that operate on or return
    method handles. They fall into several categories:
    
    - Lookup methods which help create method handles for methods and fields.
    - Combinator methods, which combine or transform pre-existing method handles into new ones.
    - Other factory methods to create method handles that emulate other common JVM operations or control flow patterns.
    
    A lookup, combinator, or factory method will fail and throw an
    `IllegalArgumentException` if the created method handle's type
    would have <a href="MethodHandle.html#maxarity">too many parameters</a>.

    Author(s)
    - John Rose, JSR 292 EG

    Since
    - 1.7
    """

    @staticmethod
    def lookup() -> "Lookup":
        """
        Returns a Lookup lookup object with
        full capabilities to emulate all supported bytecode behaviors of the caller.
        These capabilities include Lookup.hasFullPrivilegeAccess() full privilege access to the caller.
        Factory methods on the lookup object can create
        <a href="MethodHandleInfo.html#directmh">direct method handles</a>
        for any member that the caller has access to via bytecodes,
        including protected and private fields and methods.
        This lookup object is created by the original lookup class
        and has the Lookup.ORIGINAL ORIGINAL bit set.
        This lookup object is a *capability* which may be delegated to trusted agents.
        Do not store it in place where untrusted code can access it.
        
        This method is caller sensitive, which means that it may return different
        values to different callers.

        Returns
        - a lookup object for the caller of this method, with
        Lookup.ORIGINAL original and
        Lookup.hasFullPrivilegeAccess() full privilege access.
        """
        ...


    @staticmethod
    def publicLookup() -> "Lookup":
        """
        Returns a Lookup lookup object which is trusted minimally.
        The lookup has the `UNCONDITIONAL` mode.
        It can only be used to create method handles to public members of
        public classes in packages that are exported unconditionally.
        
        As a matter of pure convention, the Lookup.lookupClass() lookup class
        of this lookup object will be java.lang.Object.

        Returns
        - a lookup object which is trusted minimally

        Unknown Tags
        - The use of Object is conventional, and because the lookup modes are
        limited, there is no special access provided to the internals of Object, its package
        or its module.  This public lookup object or other lookup object with
        `UNCONDITIONAL` mode assumes readability. Consequently, the lookup class
        is not used to determine the lookup context.
        
        <p style="font-size:smaller;">
        *Discussion:*
        The lookup class can be changed to any other class `C` using an expression of the form
        Lookup.in publicLookup().in(C.class).
        A public lookup object is always subject to
        <a href="MethodHandles.Lookup.html#secmgr">security manager checks</a>.
        Also, it cannot access
        <a href="MethodHandles.Lookup.html#callsens">caller sensitive methods</a>.
        - 9
        """
        ...


    @staticmethod
    def privateLookupIn(targetClass: type[Any], caller: "Lookup") -> "Lookup":
        """
        Returns a Lookup lookup object on a target class to emulate all supported
        bytecode behaviors, including <a href="MethodHandles.Lookup.html#privacc">private access</a>.
        The returned lookup object can provide access to classes in modules and packages,
        and members of those classes, outside the normal rules of Java access control,
        instead conforming to the more permissive rules for modular *deep reflection*.
        
        A caller, specified as a `Lookup` object, in module `M1` is
        allowed to do deep reflection on module `M2` and package of the target class
        if and only if all of the following conditions are `True`:
        
        - If there is a security manager, its `checkPermission` method is
        called to check `ReflectPermission("suppressAccessChecks")` and
        that must return normally.
        - The caller lookup object must have Lookup.hasFullPrivilegeAccess()
        full privilege access.  Specifically:
          
            - The caller lookup object must have the Lookup.MODULE MODULE lookup mode.
                (This is because otherwise there would be no way to ensure the original lookup
                creator was a member of any particular module, and so any subsequent checks
                for readability and qualified exports would become ineffective.)
            - The caller lookup object must have Lookup.PRIVATE PRIVATE access.
                (This is because an application intending to share intra-module access
                using Lookup.MODULE MODULE alone will inadvertently also share
                deep reflection to its own module.)
          
        - The target class must be a proper class, not a primitive or array class.
        (Thus, `M2` is well-defined.)
        - If the caller module `M1` differs from
        the target module `M2` then both of the following must be True:
          
            - `M1` Module.canRead reads `M2`.
            - `M2` Module.isOpen(String,Module) opens the package
                containing the target class to at least `M1`.
          
        
        
        If any of the above checks is violated, this method fails with an
        exception.
        
        Otherwise, if `M1` and `M2` are the same module, this method
        returns a `Lookup` on `targetClass` with
        Lookup.hasFullPrivilegeAccess() full privilege access
        with `null` previous lookup class.
        
        Otherwise, `M1` and `M2` are two different modules.  This method
        returns a `Lookup` on `targetClass` that records
        the lookup class of the caller as the new previous lookup class with
        `PRIVATE` access but no `MODULE` access.
        
        The resulting `Lookup` object has no `ORIGINAL` access.

        Arguments
        - targetClass: the target class
        - caller: the caller lookup object

        Returns
        - a lookup object for the target class, with private access

        Raises
        - IllegalArgumentException: if `targetClass` is a primitive type or void or array class
        - NullPointerException: if `targetClass` or `caller` is `null`
        - SecurityException: if denied by the security manager
        - IllegalAccessException: if any of the other access checks specified above fails

        See
        - <a href="MethodHandles.Lookup.html.cross-module-lookup">Cross-module lookups</a>

        Since
        - 9
        """
        ...


    @staticmethod
    def classData(caller: "Lookup", name: str, type: type["T"]) -> "T":
        """
        Returns the *class data* associated with the lookup class
        of the given `caller` lookup object, or `null`.
        
         A hidden class with class data can be created by calling
        Lookup.defineHiddenClassWithClassData(byte[], Object, boolean, Lookup.ClassOption...)
        Lookup::defineHiddenClassWithClassData.
        This method will cause the static class initializer of the lookup
        class of the given `caller` lookup object be executed if
        it has not been initialized.
        
         A hidden class created by Lookup.defineHiddenClass(byte[], boolean, Lookup.ClassOption...)
        Lookup::defineHiddenClass and non-hidden classes have no class data.
        `null` is returned if this method is called on the lookup object
        on these classes.
        
         The Lookup.lookupModes() lookup modes for this lookup
        must have Lookup.ORIGINAL original access
        in order to retrieve the class data.
        
        Type `<T>`: the type to cast the class data object to

        Arguments
        - caller: the lookup context describing the class performing the
        operation (normally stacked by the JVM)
        - name: must be ConstantDescs.DEFAULT_NAME
                    (`"_"`)
        - type: the type of the class data

        Returns
        - the value of the class data if present in the lookup class;
        otherwise `null`

        Raises
        - IllegalArgumentException: if name is not `"_"`
        - IllegalAccessException: if the lookup context does not have
        Lookup.ORIGINAL original access
        - ClassCastException: if the class data cannot be converted to
        the given `type`
        - NullPointerException: if `caller` or `type` argument
        is `null`

        See
        - MethodHandles.classDataAt(Lookup, String, Class, int)

        Since
        - 16

        Unknown Tags
        - This method can be called as a bootstrap method for a dynamically computed
        constant.  A framework can create a hidden class with class data, for
        example that can be `Class` or `MethodHandle` object.
        The class data is accessible only to the lookup object
        created by the original caller but inaccessible to other members
        in the same nest.  If a framework passes security sensitive objects
        to a hidden class via class data, it is recommended to load the value
        of class data as a dynamically computed constant instead of storing
        the class data in private static field(s) which are accessible to
        other nestmates.
        - 5.5 Initialization
        """
        ...


    @staticmethod
    def classDataAt(caller: "Lookup", name: str, type: type["T"], index: int) -> "T":
        """
        Returns the element at the specified index in the
        .classData(Lookup, String, Class) class data,
        if the class data associated with the lookup class
        of the given `caller` lookup object is a `List`.
        If the class data is not present in this lookup class, this method
        returns `null`.
        
         A hidden class with class data can be created by calling
        Lookup.defineHiddenClassWithClassData(byte[], Object, boolean, Lookup.ClassOption...)
        Lookup::defineHiddenClassWithClassData.
        This method will cause the static class initializer of the lookup
        class of the given `caller` lookup object be executed if
        it has not been initialized.
        
         A hidden class created by Lookup.defineHiddenClass(byte[], boolean, Lookup.ClassOption...)
        Lookup::defineHiddenClass and non-hidden classes have no class data.
        `null` is returned if this method is called on the lookup object
        on these classes.
        
         The Lookup.lookupModes() lookup modes for this lookup
        must have Lookup.ORIGINAL original access
        in order to retrieve the class data.
        
        Type `<T>`: the type to cast the result object to

        Arguments
        - caller: the lookup context describing the class performing the
        operation (normally stacked by the JVM)
        - name: must be java.lang.constant.ConstantDescs.DEFAULT_NAME
                    (`"_"`)
        - type: the type of the element at the given index in the class data
        - index: index of the element in the class data

        Returns
        - the element at the given index in the class data
        if the class data is present; otherwise `null`

        Raises
        - IllegalArgumentException: if name is not `"_"`
        - IllegalAccessException: if the lookup context does not have
        Lookup.ORIGINAL original access
        - ClassCastException: if the class data cannot be converted to `List`
        or the element at the specified index cannot be converted to the given type
        - IndexOutOfBoundsException: if the index is out of range
        - NullPointerException: if `caller` or `type` argument is
        `null`; or if unboxing operation fails because
        the element at the given index is `null`

        See
        - Lookup.defineHiddenClassWithClassData(byte[], Object, boolean, Lookup.ClassOption...)

        Since
        - 16

        Unknown Tags
        - This method can be called as a bootstrap method for a dynamically computed
        constant.  A framework can create a hidden class with class data, for
        example that can be `List.of(o1, o2, o3....)` containing more than
        one object and use this method to load one element at a specific index.
        The class data is accessible only to the lookup object
        created by the original caller but inaccessible to other members
        in the same nest.  If a framework passes security sensitive objects
        to a hidden class via class data, it is recommended to load the value
        of class data as a dynamically computed constant instead of storing
        the class data in private static field(s) which are accessible to other
        nestmates.
        """
        ...


    @staticmethod
    def reflectAs(expected: type["T"], target: "MethodHandle") -> "T":
        """
        Performs an unchecked "crack" of a
        <a href="MethodHandleInfo.html#directmh">direct method handle</a>.
        The result is as if the user had obtained a lookup object capable enough
        to crack the target method handle, called
        java.lang.invoke.MethodHandles.Lookup.revealDirect Lookup.revealDirect
        on the target to obtain its symbolic reference, and then called
        java.lang.invoke.MethodHandleInfo.reflectAs MethodHandleInfo.reflectAs
        to resolve the symbolic reference to a member.
        
        If there is a security manager, its `checkPermission` method
        is called with a `ReflectPermission("suppressAccessChecks")` permission.
        
        Type `<T>`: the desired type of the result, either Member or a subtype

        Arguments
        - target: a direct method handle to crack into symbolic reference components
        - expected: a class object representing the desired result type `T`

        Returns
        - a reference to the method, constructor, or field object

        Raises
        - SecurityException: if the caller is not privileged to call `setAccessible`
        - NullPointerException: if either argument is `null`
        - IllegalArgumentException: if the target is not a direct method handle
        - ClassCastException: if the member is not of the expected type

        Since
        - 1.8
        """
        ...


    @staticmethod
    def arrayConstructor(arrayClass: type[Any]) -> "MethodHandle":
        """
        Produces a method handle constructing arrays of a desired type,
        as if by the `anewarray` bytecode.
        The return type of the method handle will be the array type.
        The type of its sole argument will be `int`, which specifies the size of the array.
        
         If the returned method handle is invoked with a negative
        array size, a `NegativeArraySizeException` will be thrown.

        Arguments
        - arrayClass: an array type

        Returns
        - a method handle which can create arrays of the given type

        Raises
        - NullPointerException: if the argument is `null`
        - IllegalArgumentException: if `arrayClass` is not an array type

        See
        - java.lang.reflect.Array.newInstance(Class, int)

        Since
        - 9

        Unknown Tags
        - 6.5 `anewarray` Instruction
        """
        ...


    @staticmethod
    def arrayLength(arrayClass: type[Any]) -> "MethodHandle":
        """
        Produces a method handle returning the length of an array,
        as if by the `arraylength` bytecode.
        The type of the method handle will have `int` as return type,
        and its sole argument will be the array type.
        
         If the returned method handle is invoked with a `null`
        array reference, a `NullPointerException` will be thrown.

        Arguments
        - arrayClass: an array type

        Returns
        - a method handle which can retrieve the length of an array of the given array type

        Raises
        - NullPointerException: if the argument is `null`
        - IllegalArgumentException: if arrayClass is not an array type

        Since
        - 9

        Unknown Tags
        - 6.5 `arraylength` Instruction
        """
        ...


    @staticmethod
    def arrayElementGetter(arrayClass: type[Any]) -> "MethodHandle":
        """
        Produces a method handle giving read access to elements of an array,
        as if by the `aaload` bytecode.
        The type of the method handle will have a return type of the array's
        element type.  Its first argument will be the array type,
        and the second will be `int`.
        
         When the returned method handle is invoked,
        the array reference and array index are checked.
        A `NullPointerException` will be thrown if the array reference
        is `null` and an `ArrayIndexOutOfBoundsException` will be
        thrown if the index is negative or if it is greater than or equal to
        the length of the array.

        Arguments
        - arrayClass: an array type

        Returns
        - a method handle which can load values from the given array type

        Raises
        - NullPointerException: if the argument is null
        - IllegalArgumentException: if arrayClass is not an array type

        Unknown Tags
        - 6.5 `aaload` Instruction
        """
        ...


    @staticmethod
    def arrayElementSetter(arrayClass: type[Any]) -> "MethodHandle":
        """
        Produces a method handle giving write access to elements of an array,
        as if by the `astore` bytecode.
        The type of the method handle will have a void return type.
        Its last argument will be the array's element type.
        The first and second arguments will be the array type and int.
        
         When the returned method handle is invoked,
        the array reference and array index are checked.
        A `NullPointerException` will be thrown if the array reference
        is `null` and an `ArrayIndexOutOfBoundsException` will be
        thrown if the index is negative or if it is greater than or equal to
        the length of the array.

        Arguments
        - arrayClass: the class of an array

        Returns
        - a method handle which can store values into the array type

        Raises
        - NullPointerException: if the argument is null
        - IllegalArgumentException: if arrayClass is not an array type

        Unknown Tags
        - 6.5 `aastore` Instruction
        """
        ...


    @staticmethod
    def arrayElementVarHandle(arrayClass: type[Any]) -> "VarHandle":
        """
        Produces a VarHandle giving access to elements of an array of type
        `arrayClass`.  The VarHandle's variable type is the component type
        of `arrayClass` and the list of coordinate types is
        `(arrayClass, int)`, where the `int` coordinate type
        corresponds to an argument that is an index into an array.
        
        Certain access modes of the returned VarHandle are unsupported under
        the following conditions:
        
        - if the component type is anything other than `byte`,
            `short`, `char`, `int`, `long`,
            `float`, or `double` then numeric atomic update access
            modes are unsupported.
        - if the component type is anything other than `boolean`,
            `byte`, `short`, `char`, `int` or
            `long` then bitwise atomic update access modes are
            unsupported.
        
        
        If the component type is `float` or `double` then numeric
        and atomic update access modes compare values using their bitwise
        representation (see Float.floatToRawIntBits and
        Double.doubleToRawLongBits, respectively).
        
         When the returned `VarHandle` is invoked,
        the array reference and array index are checked.
        A `NullPointerException` will be thrown if the array reference
        is `null` and an `ArrayIndexOutOfBoundsException` will be
        thrown if the index is negative or if it is greater than or equal to
        the length of the array.

        Arguments
        - arrayClass: the class of an array, of type `T[]`

        Returns
        - a VarHandle giving access to elements of an array

        Raises
        - NullPointerException: if the arrayClass is null
        - IllegalArgumentException: if arrayClass is not an array type

        Since
        - 9

        Unknown Tags
        - Bitwise comparison of `float` values or `double` values,
        as performed by the numeric and atomic update access modes, differ
        from the primitive `==` operator and the Float.equals
        and Double.equals methods, specifically with respect to
        comparing NaN values or comparing `-0.0` with `+0.0`.
        Care should be taken when performing a compare and set or a compare
        and exchange operation with such values since the operation may
        unexpectedly fail.
        There are many possible NaN values that are considered to be
        `NaN` in Java, although no IEEE 754 floating-point operation
        provided by Java can distinguish between them.  Operation failure can
        occur if the expected or witness value is a NaN value and it is
        transformed (perhaps in a platform specific manner) into another NaN
        value, and thus has a different bitwise representation (see
        Float.intBitsToFloat or Double.longBitsToDouble for more
        details).
        The values `-0.0` and `+0.0` have different bitwise
        representations but are considered equal when using the primitive
        `==` operator.  Operation failure can occur if, for example, a
        numeric algorithm computes an expected value to be say `-0.0`
        and previously computed the witness value to be say `+0.0`.
        """
        ...


    @staticmethod
    def byteArrayViewVarHandle(viewArrayClass: type[Any], byteOrder: "ByteOrder") -> "VarHandle":
        """
        Produces a VarHandle giving access to elements of a `byte[]` array
        viewed as if it were a different primitive array type, such as
        `int[]` or `long[]`.
        The VarHandle's variable type is the component type of
        `viewArrayClass` and the list of coordinate types is
        `(byte[], int)`, where the `int` coordinate type
        corresponds to an argument that is an index into a `byte[]` array.
        The returned VarHandle accesses bytes at an index in a `byte[]`
        array, composing bytes to or from a value of the component type of
        `viewArrayClass` according to the given endianness.
        
        The supported component types (variables types) are `short`,
        `char`, `int`, `long`, `float` and
        `double`.
        
        Access of bytes at a given index will result in an
        `ArrayIndexOutOfBoundsException` if the index is less than `0`
        or greater than the `byte[]` array length minus the size (in bytes)
        of `T`.
        
        Access of bytes at an index may be aligned or misaligned for `T`,
        with respect to the underlying memory address, `A` say, associated
        with the array and index.
        If access is misaligned then access for anything other than the
        `get` and `set` access modes will result in an
        `IllegalStateException`.  In such cases atomic access is only
        guaranteed with respect to the largest power of two that divides the GCD
        of `A` and the size (in bytes) of `T`.
        If access is aligned then following access modes are supported and are
        guaranteed to support atomic access:
        
        - read write access modes for all `T`, with the exception of
            access modes `get` and `set` for `long` and
            `double` on 32-bit platforms.
        - atomic update access modes for `int`, `long`,
            `float` or `double`.
            (Future major platform releases of the JDK may support additional
            types for certain currently unsupported access modes.)
        - numeric atomic update access modes for `int` and `long`.
            (Future major platform releases of the JDK may support additional
            numeric types for certain currently unsupported access modes.)
        - bitwise atomic update access modes for `int` and `long`.
            (Future major platform releases of the JDK may support additional
            numeric types for certain currently unsupported access modes.)
        
        
        Misaligned access, and therefore atomicity guarantees, may be determined
        for `byte[]` arrays without operating on a specific array.  Given
        an `index`, `T` and it's corresponding boxed type,
        `T_BOX`, misalignment may be determined as follows:
        ````int sizeOfT = T_BOX.BYTES;  // size in bytes of T
        int misalignedAtZeroIndex = ByteBuffer.wrap(new byte[0]).
            alignmentOffset(0, sizeOfT);
        int misalignedAtIndex = (misalignedAtZeroIndex + index) % sizeOfT;
        boolean isMisaligned = misalignedAtIndex != 0;````
        
        If the variable type is `float` or `double` then atomic
        update access modes compare values using their bitwise representation
        (see Float.floatToRawIntBits and
        Double.doubleToRawLongBits, respectively).

        Arguments
        - viewArrayClass: the view array class, with a component type of
        type `T`
        - byteOrder: the endianness of the view array elements, as
        stored in the underlying `byte` array

        Returns
        - a VarHandle giving access to elements of a `byte[]` array
        viewed as if elements corresponding to the components type of the view
        array class

        Raises
        - NullPointerException: if viewArrayClass or byteOrder is null
        - IllegalArgumentException: if viewArrayClass is not an array type
        - UnsupportedOperationException: if the component type of
        viewArrayClass is not supported as a variable type

        Since
        - 9
        """
        ...


    @staticmethod
    def byteBufferViewVarHandle(viewArrayClass: type[Any], byteOrder: "ByteOrder") -> "VarHandle":
        """
        Produces a VarHandle giving access to elements of a `ByteBuffer`
        viewed as if it were an array of elements of a different primitive
        component type to that of `byte`, such as `int[]` or
        `long[]`.
        The VarHandle's variable type is the component type of
        `viewArrayClass` and the list of coordinate types is
        `(ByteBuffer, int)`, where the `int` coordinate type
        corresponds to an argument that is an index into a `byte[]` array.
        The returned VarHandle accesses bytes at an index in a
        `ByteBuffer`, composing bytes to or from a value of the component
        type of `viewArrayClass` according to the given endianness.
        
        The supported component types (variables types) are `short`,
        `char`, `int`, `long`, `float` and
        `double`.
        
        Access will result in a `ReadOnlyBufferException` for anything
        other than the read access modes if the `ByteBuffer` is read-only.
        
        Access of bytes at a given index will result in an
        `IndexOutOfBoundsException` if the index is less than `0`
        or greater than the `ByteBuffer` limit minus the size (in bytes) of
        `T`.
        
        Access of bytes at an index may be aligned or misaligned for `T`,
        with respect to the underlying memory address, `A` say, associated
        with the `ByteBuffer` and index.
        If access is misaligned then access for anything other than the
        `get` and `set` access modes will result in an
        `IllegalStateException`.  In such cases atomic access is only
        guaranteed with respect to the largest power of two that divides the GCD
        of `A` and the size (in bytes) of `T`.
        If access is aligned then following access modes are supported and are
        guaranteed to support atomic access:
        
        - read write access modes for all `T`, with the exception of
            access modes `get` and `set` for `long` and
            `double` on 32-bit platforms.
        - atomic update access modes for `int`, `long`,
            `float` or `double`.
            (Future major platform releases of the JDK may support additional
            types for certain currently unsupported access modes.)
        - numeric atomic update access modes for `int` and `long`.
            (Future major platform releases of the JDK may support additional
            numeric types for certain currently unsupported access modes.)
        - bitwise atomic update access modes for `int` and `long`.
            (Future major platform releases of the JDK may support additional
            numeric types for certain currently unsupported access modes.)
        
        
        Misaligned access, and therefore atomicity guarantees, may be determined
        for a `ByteBuffer`, `bb` (direct or otherwise), an
        `index`, `T` and it's corresponding boxed type,
        `T_BOX`, as follows:
        ````int sizeOfT = T_BOX.BYTES;  // size in bytes of T
        ByteBuffer bb = ...
        int misalignedAtIndex = bb.alignmentOffset(index, sizeOfT);
        boolean isMisaligned = misalignedAtIndex != 0;````
        
        If the variable type is `float` or `double` then atomic
        update access modes compare values using their bitwise representation
        (see Float.floatToRawIntBits and
        Double.doubleToRawLongBits, respectively).

        Arguments
        - viewArrayClass: the view array class, with a component type of
        type `T`
        - byteOrder: the endianness of the view array elements, as
        stored in the underlying `ByteBuffer` (Note this overrides the
        endianness of a `ByteBuffer`)

        Returns
        - a VarHandle giving access to elements of a `ByteBuffer`
        viewed as if elements corresponding to the components type of the view
        array class

        Raises
        - NullPointerException: if viewArrayClass or byteOrder is null
        - IllegalArgumentException: if viewArrayClass is not an array type
        - UnsupportedOperationException: if the component type of
        viewArrayClass is not supported as a variable type

        Since
        - 9
        """
        ...


    @staticmethod
    def spreadInvoker(type: "MethodType", leadingArgCount: int) -> "MethodHandle":
        """
        Produces a method handle which will invoke any method handle of the
        given `type`, with a given number of trailing arguments replaced by
        a single trailing `Object[]` array.
        The resulting invoker will be a method handle with the following
        arguments:
        
        - a single `MethodHandle` target
        - zero or more leading values (counted by `leadingArgCount`)
        - an `Object[]` array containing trailing arguments
        
        
        The invoker will invoke its target like a call to MethodHandle.invoke invoke with
        the indicated `type`.
        That is, if the target is exactly of the given `type`, it will behave
        like `invokeExact`; otherwise it behave as if MethodHandle.asType asType
        is used to convert the target to the required `type`.
        
        The type of the returned invoker will not be the given `type`, but rather
        will have all parameters except the first `leadingArgCount`
        replaced by a single array of type `Object[]`, which will be
        the final parameter.
        
        Before invoking its target, the invoker will spread the final array, apply
        reference casts as necessary, and unbox and widen primitive arguments.
        If, when the invoker is called, the supplied array argument does
        not have the correct number of elements, the invoker will throw
        an IllegalArgumentException instead of invoking the target.
        
        This method is equivalent to the following code (though it may be more efficient):
        <blockquote>````MethodHandle invoker = MethodHandles.invoker(type);
        int spreadArgCount = type.parameterCount() - leadingArgCount;
        invoker = invoker.asSpreader(Object[].class, spreadArgCount);
        return invoker;````</blockquote>
        This method throws no reflective or security exceptions.

        Arguments
        - type: the desired target type
        - leadingArgCount: number of fixed arguments, to be passed unchanged to the target

        Returns
        - a method handle suitable for invoking any method handle of the given type

        Raises
        - NullPointerException: if `type` is null
        - IllegalArgumentException: if `leadingArgCount` is not in
                         the range from 0 to `type.parameterCount()` inclusive,
                         or if the resulting method handle's type would have
                 <a href="MethodHandle.html#maxarity">too many parameters</a>
        """
        ...


    @staticmethod
    def exactInvoker(type: "MethodType") -> "MethodHandle":
        """
        Produces a special *invoker method handle* which can be used to
        invoke any method handle of the given type, as if by MethodHandle.invokeExact invokeExact.
        The resulting invoker will have a type which is
        exactly equal to the desired type, except that it will accept
        an additional leading argument of type `MethodHandle`.
        
        This method is equivalent to the following code (though it may be more efficient):
        `publicLookup().findVirtual(MethodHandle.class, "invokeExact", type)`
        
        <p style="font-size:smaller;">
        *Discussion:*
        Invoker method handles can be useful when working with variable method handles
        of unknown types.
        For example, to emulate an `invokeExact` call to a variable method
        handle `M`, extract its type `T`,
        look up the invoker method `X` for `T`,
        and call the invoker method, as `X.invoke(T, A...)`.
        (It would not work to call `X.invokeExact`, since the type `T`
        is unknown.)
        If spreading, collecting, or other argument transformations are required,
        they can be applied once to the invoker `X` and reused on many `M`
        method handle values, as long as they are compatible with the type of `X`.
        <p style="font-size:smaller;">
        *(Note:  The invoker method is not available via the Core Reflection API.
        An attempt to call java.lang.reflect.Method.invoke java.lang.reflect.Method.invoke
        on the declared `invokeExact` or `invoke` method will raise an
        java.lang.UnsupportedOperationException UnsupportedOperationException.)*
        
        This method throws no reflective or security exceptions.

        Arguments
        - type: the desired target type

        Returns
        - a method handle suitable for invoking any method handle of the given type

        Raises
        - IllegalArgumentException: if the resulting method handle's type would have
                 <a href="MethodHandle.html#maxarity">too many parameters</a>
        """
        ...


    @staticmethod
    def invoker(type: "MethodType") -> "MethodHandle":
        """
        Produces a special *invoker method handle* which can be used to
        invoke any method handle compatible with the given type, as if by MethodHandle.invoke invoke.
        The resulting invoker will have a type which is
        exactly equal to the desired type, except that it will accept
        an additional leading argument of type `MethodHandle`.
        
        Before invoking its target, if the target differs from the expected type,
        the invoker will apply reference casts as
        necessary and box, unbox, or widen primitive values, as if by MethodHandle.asType asType.
        Similarly, the return value will be converted as necessary.
        If the target is a MethodHandle.asVarargsCollector variable arity method handle,
        the required arity conversion will be made, again as if by MethodHandle.asType asType.
        
        This method is equivalent to the following code (though it may be more efficient):
        `publicLookup().findVirtual(MethodHandle.class, "invoke", type)`
        <p style="font-size:smaller;">
        *Discussion:*
        A MethodType.genericMethodType general method type is one which
        mentions only `Object` arguments and return values.
        An invoker for such a type is capable of calling any method handle
        of the same arity as the general type.
        <p style="font-size:smaller;">
        *(Note:  The invoker method is not available via the Core Reflection API.
        An attempt to call java.lang.reflect.Method.invoke java.lang.reflect.Method.invoke
        on the declared `invokeExact` or `invoke` method will raise an
        java.lang.UnsupportedOperationException UnsupportedOperationException.)*
        
        This method throws no reflective or security exceptions.

        Arguments
        - type: the desired target type

        Returns
        - a method handle suitable for invoking any method handle convertible to the given type

        Raises
        - IllegalArgumentException: if the resulting method handle's type would have
                 <a href="MethodHandle.html#maxarity">too many parameters</a>
        """
        ...


    @staticmethod
    def varHandleExactInvoker(accessMode: "VarHandle.AccessMode", type: "MethodType") -> "MethodHandle":
        """
        Produces a special *invoker method handle* which can be used to
        invoke a signature-polymorphic access mode method on any VarHandle whose
        associated access mode type is compatible with the given type.
        The resulting invoker will have a type which is exactly equal to the
        desired given type, except that it will accept an additional leading
        argument of type `VarHandle`.

        Arguments
        - accessMode: the VarHandle access mode
        - type: the desired target type

        Returns
        - a method handle suitable for invoking an access mode method of
                any VarHandle whose access mode type is of the given type.

        Since
        - 9
        """
        ...


    @staticmethod
    def varHandleInvoker(accessMode: "VarHandle.AccessMode", type: "MethodType") -> "MethodHandle":
        """
        Produces a special *invoker method handle* which can be used to
        invoke a signature-polymorphic access mode method on any VarHandle whose
        associated access mode type is compatible with the given type.
        The resulting invoker will have a type which is exactly equal to the
        desired given type, except that it will accept an additional leading
        argument of type `VarHandle`.
        
        Before invoking its target, if the access mode type differs from the
        desired given type, the invoker will apply reference casts as necessary
        and box, unbox, or widen primitive values, as if by
        MethodHandle.asType asType.  Similarly, the return value will be
        converted as necessary.
        
        This method is equivalent to the following code (though it may be more
        efficient): `publicLookup().findVirtual(VarHandle.class, accessMode.name(), type)`

        Arguments
        - accessMode: the VarHandle access mode
        - type: the desired target type

        Returns
        - a method handle suitable for invoking an access mode method of
                any VarHandle whose access mode type is convertible to the given
                type.

        Since
        - 9
        """
        ...


    @staticmethod
    def explicitCastArguments(target: "MethodHandle", newType: "MethodType") -> "MethodHandle":
        """
        Produces a method handle which adapts the type of the
        given method handle to a new type by pairwise argument and return type conversion.
        The original type and new type must have the same number of arguments.
        The resulting method handle is guaranteed to report a type
        which is equal to the desired new type.
        
        If the original type and new type are equal, returns target.
        
        The same conversions are allowed as for MethodHandle.asType MethodHandle.asType,
        and some additional conversions are also applied if those conversions fail.
        Given types *T0*, *T1*, one of the following conversions is applied
        if possible, before or instead of any conversions done by `asType`:
        
        - If *T0* and *T1* are references, and *T1* is an interface type,
            then the value of type *T0* is passed as a *T1* without a cast.
            (This treatment of interfaces follows the usage of the bytecode verifier.)
        - If *T0* is boolean and *T1* is another primitive,
            the boolean is converted to a byte value, 1 for True, 0 for False.
            (This treatment follows the usage of the bytecode verifier.)
        - If *T1* is boolean and *T0* is another primitive,
            *T0* is converted to byte via Java casting conversion (JLS 5.5),
            and the low order bit of the result is tested, as if by `(x & 1) != 0`.
        - If *T0* and *T1* are primitives other than boolean,
            then a Java casting conversion (JLS 5.5) is applied.
            (Specifically, *T0* will convert to *T1* by
            widening and/or narrowing.)
        - If *T0* is a reference and *T1* a primitive, an unboxing
            conversion will be applied at runtime, possibly followed
            by a Java casting conversion (JLS 5.5) on the primitive value,
            possibly followed by a conversion from byte to boolean by testing
            the low-order bit.
        - If *T0* is a reference and *T1* a primitive,
            and if the reference is null at runtime, a zero value is introduced.

        Arguments
        - target: the method handle to invoke after arguments are retyped
        - newType: the expected type of the new method handle

        Returns
        - a method handle which delegates to the target after performing
                  any necessary argument conversions, and arranges for any
                  necessary return value conversions

        Raises
        - NullPointerException: if either argument is null
        - WrongMethodTypeException: if the conversion cannot be made

        See
        - MethodHandle.asType
        """
        ...


    @staticmethod
    def permuteArguments(target: "MethodHandle", newType: "MethodType", *reorder: Tuple[int, ...]) -> "MethodHandle":
        """
        Produces a method handle which adapts the calling sequence of the
        given method handle to a new type, by reordering the arguments.
        The resulting method handle is guaranteed to report a type
        which is equal to the desired new type.
        
        The given array controls the reordering.
        Call `.I` the number of incoming parameters (the value
        `newType.parameterCount()`, and call `.O` the number
        of outgoing parameters (the value `target.type().parameterCount()`).
        Then the length of the reordering array must be `.O`,
        and each element must be a non-negative number less than `.I`.
        For every `N` less than `.O`, the `N`-th
        outgoing argument will be taken from the `I`-th incoming
        argument, where `I` is `reorder[N]`.
        
        No argument or return value conversions are applied.
        The type of each incoming argument, as determined by `newType`,
        must be identical to the type of the corresponding outgoing parameter
        or parameters in the target method handle.
        The return type of `newType` must be identical to the return
        type of the original target.
        
        The reordering array need not specify an actual permutation.
        An incoming argument will be duplicated if its index appears
        more than once in the array, and an incoming argument will be dropped
        if its index does not appear in the array.
        As in the case of .dropArguments(MethodHandle,int,List) dropArguments,
        incoming arguments which are not mentioned in the reordering array
        may be of any type, as determined only by `newType`.
        <blockquote>````import static java.lang.invoke.MethodHandles.*;
        import static java.lang.invoke.MethodType.*;
        ...
        MethodType intfn1 = methodType(int.class, int.class);
        MethodType intfn2 = methodType(int.class, int.class, int.class);
        MethodHandle sub = ... (int x, int y) -> (x-y) ...;
        assert(sub.type().equals(intfn2));
        MethodHandle sub1 = permuteArguments(sub, intfn2, 0, 1);
        MethodHandle rsub = permuteArguments(sub, intfn2, 1, 0);
        assert((int)rsub.invokeExact(1, 100) == 99);
        MethodHandle add = ... (int x, int y) -> (x+y) ...;
        assert(add.type().equals(intfn2));
        MethodHandle twice = permuteArguments(add, intfn1, 0, 0);
        assert(twice.type().equals(intfn1));
        assert((int)twice.invokeExact(21) == 42);````</blockquote>
        
        *Note:* The resulting adapter is never a MethodHandle.asVarargsCollector
        variable-arity method handle, even if the original target method handle was.

        Arguments
        - target: the method handle to invoke after arguments are reordered
        - newType: the expected type of the new method handle
        - reorder: an index array which controls the reordering

        Returns
        - a method handle which delegates to the target after it
                  drops unused arguments and moves and/or duplicates the other arguments

        Raises
        - NullPointerException: if any argument is null
        - IllegalArgumentException: if the index array length is not equal to
                         the arity of the target, or if any index array element
                         not a valid index for a parameter of `newType`,
                         or if two corresponding parameter types in
                         `target.type()` and `newType` are not identical,
        """
        ...


    @staticmethod
    def constant(type: type[Any], value: "Object") -> "MethodHandle":
        """
        Produces a method handle of the requested return type which returns the given
        constant value every time it is invoked.
        
        Before the method handle is returned, the passed-in value is converted to the requested type.
        If the requested type is primitive, widening primitive conversions are attempted,
        else reference conversions are attempted.
        The returned method handle is equivalent to `identity(type).bindTo(value)`.

        Arguments
        - type: the return type of the desired method handle
        - value: the value to return

        Returns
        - a method handle of the given return type and no arguments, which always returns the given value

        Raises
        - NullPointerException: if the `type` argument is null
        - ClassCastException: if the value cannot be converted to the required return type
        - IllegalArgumentException: if the given type is `void.class`
        """
        ...


    @staticmethod
    def identity(type: type[Any]) -> "MethodHandle":
        """
        Produces a method handle which returns its sole argument when invoked.

        Arguments
        - type: the type of the sole parameter and return value of the desired method handle

        Returns
        - a unary method handle which accepts and returns the given type

        Raises
        - NullPointerException: if the argument is null
        - IllegalArgumentException: if the given type is `void.class`
        """
        ...


    @staticmethod
    def zero(type: type[Any]) -> "MethodHandle":
        """
        Produces a constant method handle of the requested return type which
        returns the default value for that type every time it is invoked.
        The resulting constant method handle will have no side effects.
        The returned method handle is equivalent to `empty(methodType(type))`.
        It is also equivalent to `explicitCastArguments(constant(Object.class, null), methodType(type))`,
        since `explicitCastArguments` converts `null` to default values.

        Arguments
        - type: the expected return type of the desired method handle

        Returns
        - a constant method handle that takes no arguments
                and returns the default value of the given type (or void, if the type is void)

        Raises
        - NullPointerException: if the argument is null

        See
        - MethodHandles.explicitCastArguments

        Since
        - 9
        """
        ...


    @staticmethod
    def empty(type: "MethodType") -> "MethodHandle":
        """
        Produces a method handle of the requested type which ignores any arguments, does nothing,
        and returns a suitable default depending on the return type.
        That is, it returns a zero primitive value, a `null`, or `void`.
        The returned method handle is equivalent to
        `dropArguments(zero(type.returnType()), 0, type.parameterList())`.

        Arguments
        - type: the type of the desired method handle

        Returns
        - a constant method handle of the given type, which returns a default value of the given return type

        Raises
        - NullPointerException: if the argument is null

        See
        - MethodHandles.constant

        Since
        - 9

        Unknown Tags
        - Given a predicate and target, a useful "if-then" construct can be produced as
        `guardWithTest(pred, target, empty(target.type())`.
        """
        ...


    @staticmethod
    def insertArguments(target: "MethodHandle", pos: int, *values: Tuple["Object", ...]) -> "MethodHandle":
        """
        Provides a target method handle with one or more *bound arguments*
        in advance of the method handle's invocation.
        The formal parameters to the target corresponding to the bound
        arguments are called *bound parameters*.
        Returns a new method handle which saves away the bound arguments.
        When it is invoked, it receives arguments for any non-bound parameters,
        binds the saved arguments to their corresponding parameters,
        and calls the original target.
        
        The type of the new method handle will drop the types for the bound
        parameters from the original target type, since the new method handle
        will no longer require those arguments to be supplied by its callers.
        
        Each given argument object must match the corresponding bound parameter type.
        If a bound parameter type is a primitive, the argument object
        must be a wrapper, and will be unboxed to produce the primitive value.
        
        The `pos` argument selects which parameters are to be bound.
        It may range between zero and *N-L* (inclusively),
        where *N* is the arity of the target method handle
        and *L* is the length of the values array.
        
        *Note:* The resulting adapter is never a MethodHandle.asVarargsCollector
        variable-arity method handle, even if the original target method handle was.

        Arguments
        - target: the method handle to invoke after the argument is inserted
        - pos: where to insert the argument (zero for the first)
        - values: the series of arguments to insert

        Returns
        - a method handle which inserts an additional argument,
                before calling the original method handle

        Raises
        - NullPointerException: if the target or the `values` array is null
        - IllegalArgumentException: if (@code pos) is less than `0` or greater than
                `N - L` where `N` is the arity of the target method handle and `L`
                is the length of the values array.
        - ClassCastException: if an argument does not match the corresponding bound parameter
                type.

        See
        - MethodHandle.bindTo
        """
        ...


    @staticmethod
    def dropArguments(target: "MethodHandle", pos: int, valueTypes: list[type[Any]]) -> "MethodHandle":
        """
        Produces a method handle which will discard some dummy arguments
        before calling some other specified *target* method handle.
        The type of the new method handle will be the same as the target's type,
        except it will also include the dummy argument types,
        at some given position.
        
        The `pos` argument may range between zero and *N*,
        where *N* is the arity of the target.
        If `pos` is zero, the dummy arguments will precede
        the target's real arguments; if `pos` is *N*
        they will come after.
        
        **Example:**
        <blockquote>````import static java.lang.invoke.MethodHandles.*;
        import static java.lang.invoke.MethodType.*;
        ...
        MethodHandle cat = lookup().findVirtual(String.class,
          "concat", methodType(String.class, String.class));
        assertEquals("xy", (String) cat.invokeExact("x", "y"));
        MethodType bigType = cat.type().insertParameterTypes(0, int.class, String.class);
        MethodHandle d0 = dropArguments(cat, 0, bigType.parameterList().subList(0,2));
        assertEquals(bigType, d0.type());
        assertEquals("yz", (String) d0.invokeExact(123, "x", "y", "z"));````</blockquote>
        
        This method is also equivalent to the following code:
        <blockquote>```
        .dropArguments(MethodHandle,int,Class...) dropArguments`(target, pos, valueTypes.toArray(new Class[0]))`
        ```</blockquote>

        Arguments
        - target: the method handle to invoke after the arguments are dropped
        - pos: position of first argument to drop (zero for the leftmost)
        - valueTypes: the type(s) of the argument(s) to drop

        Returns
        - a method handle which drops arguments of the given types,
                before calling the original method handle

        Raises
        - NullPointerException: if the target is null,
                                     or if the `valueTypes` list or any of its elements is null
        - IllegalArgumentException: if any element of `valueTypes` is `void.class`,
                         or if `pos` is negative or greater than the arity of the target,
                         or if the new method handle's type would have too many parameters
        """
        ...


    @staticmethod
    def dropArguments(target: "MethodHandle", pos: int, *valueTypes: Tuple[type[Any], ...]) -> "MethodHandle":
        """
        Produces a method handle which will discard some dummy arguments
        before calling some other specified *target* method handle.
        The type of the new method handle will be the same as the target's type,
        except it will also include the dummy argument types,
        at some given position.
        
        The `pos` argument may range between zero and *N*,
        where *N* is the arity of the target.
        If `pos` is zero, the dummy arguments will precede
        the target's real arguments; if `pos` is *N*
        they will come after.

        Arguments
        - target: the method handle to invoke after the arguments are dropped
        - pos: position of first argument to drop (zero for the leftmost)
        - valueTypes: the type(s) of the argument(s) to drop

        Returns
        - a method handle which drops arguments of the given types,
                before calling the original method handle

        Raises
        - NullPointerException: if the target is null,
                                     or if the `valueTypes` array or any of its elements is null
        - IllegalArgumentException: if any element of `valueTypes` is `void.class`,
                         or if `pos` is negative or greater than the arity of the target,
                         or if the new method handle's type would have
                         <a href="MethodHandle.html#maxarity">too many parameters</a>

        Unknown Tags
        - <blockquote>````import static java.lang.invoke.MethodHandles.*;
        import static java.lang.invoke.MethodType.*;
        ...
        MethodHandle cat = lookup().findVirtual(String.class,
          "concat", methodType(String.class, String.class));
        assertEquals("xy", (String) cat.invokeExact("x", "y"));
        MethodHandle d0 = dropArguments(cat, 0, String.class);
        assertEquals("yz", (String) d0.invokeExact("x", "y", "z"));
        MethodHandle d1 = dropArguments(cat, 1, String.class);
        assertEquals("xz", (String) d1.invokeExact("x", "y", "z"));
        MethodHandle d2 = dropArguments(cat, 2, String.class);
        assertEquals("xy", (String) d2.invokeExact("x", "y", "z"));
        MethodHandle d12 = dropArguments(cat, 1, int.class, boolean.class);
        assertEquals("xz", (String) d12.invokeExact("x", 12, True, "z"));````</blockquote>
        
        This method is also equivalent to the following code:
        <blockquote>```
        .dropArguments(MethodHandle,int,List) dropArguments`(target, pos, Arrays.asList(valueTypes))`
        ```</blockquote>
        """
        ...


    @staticmethod
    def dropArgumentsToMatch(target: "MethodHandle", skip: int, newTypes: list[type[Any]], pos: int) -> "MethodHandle":
        """
        Adapts a target method handle to match the given parameter type list. If necessary, adds dummy arguments. Some
        leading parameters can be skipped before matching begins. The remaining types in the `target`'s parameter
        type list must be a sub-list of the `newTypes` type list at the starting position `pos`. The
        resulting handle will have the target handle's parameter type list, with any non-matching parameter types (before
        or after the matching sub-list) inserted in corresponding positions of the target's original parameters, as if by
        .dropArguments(MethodHandle, int, Class[]).
        
        The resulting handle will have the same return type as the target handle.
        
        In more formal terms, assume these two type lists:
        - The target handle has the parameter type list `S..., M...`, with as many types in `S` as
        indicated by `skip`. The `M` types are those that are supposed to match part of the given type list,
        `newTypes`.
        - The `newTypes` list contains types `P..., M..., A...`, with as many types in `P` as
        indicated by `pos`. The `M` types are precisely those that the `M` types in the target handle's
        parameter type list are supposed to match. The types in `A` are additional types found after the matching
        sub-list.
        
        Given these assumptions, the result of an invocation of `dropArgumentsToMatch` will have the parameter type
        list `S..., P..., M..., A...`, with the `P` and `A` types inserted as if by
        .dropArguments(MethodHandle, int, Class[]).

        Arguments
        - target: the method handle to adapt
        - skip: number of targets parameters to disregard (they will be unchanged)
        - newTypes: the list of types to match `target`'s parameter type list to
        - pos: place in `newTypes` where the non-skipped target parameters must occur

        Returns
        - a possibly adapted method handle

        Raises
        - NullPointerException: if either argument is null
        - IllegalArgumentException: if any element of `newTypes` is `void.class`,
                or if `skip` is negative or greater than the arity of the target,
                or if `pos` is negative or greater than the newTypes list size,
                or if `newTypes` does not contain the `target`'s non-skipped parameter types at position
                `pos`.

        Since
        - 9

        Unknown Tags
        - Two method handles whose argument lists are "effectively identical" (i.e., identical in a common prefix) may be
        mutually converted to a common type by two calls to `dropArgumentsToMatch`, as follows:
        <blockquote>````import static java.lang.invoke.MethodHandles.*;
        import static java.lang.invoke.MethodType.*;
        ...
        ...
        MethodHandle h0 = constant(boolean.class, True);
        MethodHandle h1 = lookup().findVirtual(String.class, "concat", methodType(String.class, String.class));
        MethodType bigType = h1.type().insertParameterTypes(1, String.class, int.class);
        MethodHandle h2 = dropArguments(h1, 0, bigType.parameterList());
        if (h1.type().parameterCount() < h2.type().parameterCount())
            h1 = dropArgumentsToMatch(h1, 0, h2.type().parameterList(), 0);  // lengthen h1
        else
            h2 = dropArgumentsToMatch(h2, 0, h1.type().parameterList(), 0);    // lengthen h2
        MethodHandle h3 = guardWithTest(h0, h1, h2);
        assertEquals("xy", h3.invoke("x", "y", 1, "a", "b", "c"));````</blockquote>
        """
        ...


    @staticmethod
    def dropReturn(target: "MethodHandle") -> "MethodHandle":
        """
        Drop the return value of the target handle (if any).
        The returned method handle will have a `void` return type.

        Arguments
        - target: the method handle to adapt

        Returns
        - a possibly adapted method handle

        Raises
        - NullPointerException: if `target` is null

        Since
        - 16
        """
        ...


    @staticmethod
    def filterArguments(target: "MethodHandle", pos: int, *filters: Tuple["MethodHandle", ...]) -> "MethodHandle":
        """
        Adapts a target method handle by pre-processing
        one or more of its arguments, each with its own unary filter function,
        and then calling the target with each pre-processed argument
        replaced by the result of its corresponding filter function.
        
        The pre-processing is performed by one or more method handles,
        specified in the elements of the `filters` array.
        The first element of the filter array corresponds to the `pos`
        argument of the target, and so on in sequence.
        The filter functions are invoked in left to right order.
        
        Null arguments in the array are treated as identity functions,
        and the corresponding arguments left unchanged.
        (If there are no non-null elements in the array, the original target is returned.)
        Each filter is applied to the corresponding argument of the adapter.
        
        If a filter `F` applies to the `N`th argument of
        the target, then `F` must be a method handle which
        takes exactly one argument.  The type of `F`'s sole argument
        replaces the corresponding argument type of the target
        in the resulting adapted method handle.
        The return type of `F` must be identical to the corresponding
        parameter type of the target.
        
        It is an error if there are elements of `filters`
        (null or not)
        which do not correspond to argument positions in the target.
        **Example:**
        <blockquote>````import static java.lang.invoke.MethodHandles.*;
        import static java.lang.invoke.MethodType.*;
        ...
        MethodHandle cat = lookup().findVirtual(String.class,
          "concat", methodType(String.class, String.class));
        MethodHandle upcase = lookup().findVirtual(String.class,
          "toUpperCase", methodType(String.class));
        assertEquals("xy", (String) cat.invokeExact("x", "y"));
        MethodHandle f0 = filterArguments(cat, 0, upcase);
        assertEquals("Xy", (String) f0.invokeExact("x", "y")); // Xy
        MethodHandle f1 = filterArguments(cat, 1, upcase);
        assertEquals("xY", (String) f1.invokeExact("x", "y")); // xY
        MethodHandle f2 = filterArguments(cat, 0, upcase, upcase);
        assertEquals("XY", (String) f2.invokeExact("x", "y")); // XY````</blockquote>
        Here is pseudocode for the resulting adapter. In the code, `T`
        denotes the return type of both the `target` and resulting adapter.
        `P`/`p` and `B`/`b` represent the types and values
        of the parameters and arguments that precede and follow the filter position
        `pos`, respectively. `A[i]`/`a[i]` stand for the types and
        values of the filtered parameters and arguments; they also represent the
        return types of the `filter[i]` handles. The latter accept arguments
        `v[i]` of type `V[i]`, which also appear in the signature of
        the resulting adapter.
        <blockquote>````T target(P... p, A[i]... a[i], B... b);
        A[i] filter[i](V[i]);
        T adapter(P... p, V[i]... v[i], B... b) {
          return target(p..., filter[i](v[i])..., b...);`
        }```</blockquote>
        
        *Note:* The resulting adapter is never a MethodHandle.asVarargsCollector
        variable-arity method handle, even if the original target method handle was.

        Arguments
        - target: the method handle to invoke after arguments are filtered
        - pos: the position of the first argument to filter
        - filters: method handles to call initially on filtered arguments

        Returns
        - method handle which incorporates the specified argument filtering logic

        Raises
        - NullPointerException: if the target is null
                                     or if the `filters` array is null
        - IllegalArgumentException: if a non-null element of `filters`
                 does not match a corresponding argument type of target as described above,
                 or if the `pos+filters.length` is greater than `target.type().parameterCount()`,
                 or if the resulting method handle's type would have
                 <a href="MethodHandle.html#maxarity">too many parameters</a>
        """
        ...


    @staticmethod
    def collectArguments(target: "MethodHandle", pos: int, filter: "MethodHandle") -> "MethodHandle":
        """
        Adapts a target method handle by pre-processing
        a sub-sequence of its arguments with a filter (another method handle).
        The pre-processed arguments are replaced by the result (if any) of the
        filter function.
        The target is then called on the modified (usually shortened) argument list.
        
        If the filter returns a value, the target must accept that value as
        its argument in position `pos`, preceded and/or followed by
        any arguments not passed to the filter.
        If the filter returns void, the target must accept all arguments
        not passed to the filter.
        No arguments are reordered, and a result returned from the filter
        replaces (in order) the whole subsequence of arguments originally
        passed to the adapter.
        
        The argument types (if any) of the filter
        replace zero or one argument types of the target, at position `pos`,
        in the resulting adapted method handle.
        The return type of the filter (if any) must be identical to the
        argument type of the target at position `pos`, and that target argument
        is supplied by the return value of the filter.
        
        In all cases, `pos` must be greater than or equal to zero, and
        `pos` must also be less than or equal to the target's arity.
        **Example:**
        <blockquote>````import static java.lang.invoke.MethodHandles.*;
        import static java.lang.invoke.MethodType.*;
        ...
        MethodHandle deepToString = publicLookup()
          .findStatic(Arrays.class, "deepToString", methodType(String.class, Object[].class));
        
        MethodHandle ts1 = deepToString.asCollector(String[].class, 1);
        assertEquals("[strange]", (String) ts1.invokeExact("strange"));
        
        MethodHandle ts2 = deepToString.asCollector(String[].class, 2);
        assertEquals("[up, down]", (String) ts2.invokeExact("up", "down"));
        
        MethodHandle ts3 = deepToString.asCollector(String[].class, 3);
        MethodHandle ts3_ts2 = collectArguments(ts3, 1, ts2);
        assertEquals("[top, [up, down], strange]",
                     (String) ts3_ts2.invokeExact("top", "up", "down", "strange"));
        
        MethodHandle ts3_ts2_ts1 = collectArguments(ts3_ts2, 3, ts1);
        assertEquals("[top, [up, down], [strange]]",
                     (String) ts3_ts2_ts1.invokeExact("top", "up", "down", "strange"));
        
        MethodHandle ts3_ts2_ts3 = collectArguments(ts3_ts2, 1, ts3);
        assertEquals("[top, [[up, down, strange], charm], bottom]",
                     (String) ts3_ts2_ts3.invokeExact("top", "up", "down", "strange", "charm", "bottom"));````</blockquote>
        Here is pseudocode for the resulting adapter. In the code, `T`
        represents the return type of the `target` and resulting adapter.
        `V`/`v` stand for the return type and value of the
        `filter`, which are also found in the signature and arguments of
        the `target`, respectively, unless `V` is `void`.
        `A`/`a` and `C`/`c` represent the parameter types
        and values preceding and following the collection position, `pos`,
        in the `target`'s signature. They also turn up in the resulting
        adapter's signature and arguments, where they surround
        `B`/`b`, which represent the parameter types and arguments
        to the `filter` (if any).
        <blockquote>````T target(A...,V,C...);
        V filter(B...);
        T adapter(A... a,B... b,C... c) {
          V v = filter(b...);
          return target(a...,v,c...);`
        // and if the filter has no arguments:
        T target2(A...,V,C...);
        V filter2();
        T adapter2(A... a,C... c) {
          V v = filter2();
          return target2(a...,v,c...);
        }
        // and if the filter has a void return:
        T target3(A...,C...);
        void filter3(B...);
        T adapter3(A... a,B... b,C... c) {
          filter3(b...);
          return target3(a...,c...);
        }
        }```</blockquote>
        
        A collection adapter `collectArguments(mh, 0, coll)` is equivalent to
        one which first "folds" the affected arguments, and then drops them, in separate
        steps as follows:
        <blockquote>````mh = MethodHandles.dropArguments(mh, 1, coll.type().parameterList()); //step 2
        mh = MethodHandles.foldArguments(mh, coll); //step 1````</blockquote>
        If the target method handle consumes no arguments besides than the result
        (if any) of the filter `coll`, then `collectArguments(mh, 0, coll)`
        is equivalent to `filterReturnValue(coll, mh)`.
        If the filter method handle `coll` consumes one argument and produces
        a non-void result, then `collectArguments(mh, N, coll)`
        is equivalent to `filterArguments(mh, N, coll)`.
        Other equivalences are possible but would require argument permutation.
        
        *Note:* The resulting adapter is never a MethodHandle.asVarargsCollector
        variable-arity method handle, even if the original target method handle was.

        Arguments
        - target: the method handle to invoke after filtering the subsequence of arguments
        - pos: the position of the first adapter argument to pass to the filter,
                   and/or the target argument which receives the result of the filter
        - filter: method handle to call on the subsequence of arguments

        Returns
        - method handle which incorporates the specified argument subsequence filtering logic

        Raises
        - NullPointerException: if either argument is null
        - IllegalArgumentException: if the return type of `filter`
                 is non-void and is not the same as the `pos` argument of the target,
                 or if `pos` is not between 0 and the target's arity, inclusive,
                 or if the resulting method handle's type would have
                 <a href="MethodHandle.html#maxarity">too many parameters</a>

        See
        - MethodHandles.filterReturnValue
        """
        ...


    @staticmethod
    def filterReturnValue(target: "MethodHandle", filter: "MethodHandle") -> "MethodHandle":
        """
        Adapts a target method handle by post-processing
        its return value (if any) with a filter (another method handle).
        The result of the filter is returned from the adapter.
        
        If the target returns a value, the filter must accept that value as
        its only argument.
        If the target returns void, the filter must accept no arguments.
        
        The return type of the filter
        replaces the return type of the target
        in the resulting adapted method handle.
        The argument type of the filter (if any) must be identical to the
        return type of the target.
        **Example:**
        <blockquote>````import static java.lang.invoke.MethodHandles.*;
        import static java.lang.invoke.MethodType.*;
        ...
        MethodHandle cat = lookup().findVirtual(String.class,
          "concat", methodType(String.class, String.class));
        MethodHandle length = lookup().findVirtual(String.class,
          "length", methodType(int.class));
        System.out.println((String) cat.invokeExact("x", "y")); // xy
        MethodHandle f0 = filterReturnValue(cat, length);
        System.out.println((int) f0.invokeExact("x", "y")); // 2````</blockquote>
        Here is pseudocode for the resulting adapter. In the code,
        `T`/`t` represent the result type and value of the
        `target`; `V`, the result type of the `filter`; and
        `A`/`a`, the types and values of the parameters and arguments
        of the `target` as well as the resulting adapter.
        <blockquote>````T target(A...);
        V filter(T);
        V adapter(A... a) {
          T t = target(a...);
          return filter(t);`
        // and if the target has a void return:
        void target2(A...);
        V filter2();
        V adapter2(A... a) {
          target2(a...);
          return filter2();
        }
        // and if the filter has a void return:
        T target3(A...);
        void filter3(V);
        void adapter3(A... a) {
          T t = target3(a...);
          filter3(t);
        }
        }```</blockquote>
        
        *Note:* The resulting adapter is never a MethodHandle.asVarargsCollector
        variable-arity method handle, even if the original target method handle was.

        Arguments
        - target: the method handle to invoke before filtering the return value
        - filter: method handle to call on the return value

        Returns
        - method handle which incorporates the specified return value filtering logic

        Raises
        - NullPointerException: if either argument is null
        - IllegalArgumentException: if the argument list of `filter`
                 does not match the return type of target as described above
        """
        ...


    @staticmethod
    def foldArguments(target: "MethodHandle", combiner: "MethodHandle") -> "MethodHandle":
        """
        Adapts a target method handle by pre-processing
        some of its arguments, and then calling the target with
        the result of the pre-processing, inserted into the original
        sequence of arguments.
        
        The pre-processing is performed by `combiner`, a second method handle.
        Of the arguments passed to the adapter, the first `N` arguments
        are copied to the combiner, which is then called.
        (Here, `N` is defined as the parameter count of the combiner.)
        After this, control passes to the target, with any result
        from the combiner inserted before the original `N` incoming
        arguments.
        
        If the combiner returns a value, the first parameter type of the target
        must be identical with the return type of the combiner, and the next
        `N` parameter types of the target must exactly match the parameters
        of the combiner.
        
        If the combiner has a void return, no result will be inserted,
        and the first `N` parameter types of the target
        must exactly match the parameters of the combiner.
        
        The resulting adapter is the same type as the target, except that the
        first parameter type is dropped,
        if it corresponds to the result of the combiner.
        
        (Note that .dropArguments(MethodHandle,int,List) dropArguments can be used to remove any arguments
        that either the combiner or the target does not wish to receive.
        If some of the incoming arguments are destined only for the combiner,
        consider using MethodHandle.asCollector asCollector instead, since those
        arguments will not need to be live on the stack on entry to the
        target.)
        **Example:**
        <blockquote>````import static java.lang.invoke.MethodHandles.*;
        import static java.lang.invoke.MethodType.*;
        ...
        MethodHandle trace = publicLookup().findVirtual(java.io.PrintStream.class,
          "println", methodType(void.class, String.class))
            .bindTo(System.out);
        MethodHandle cat = lookup().findVirtual(String.class,
          "concat", methodType(String.class, String.class));
        assertEquals("boojum", (String) cat.invokeExact("boo", "jum"));
        MethodHandle catTrace = foldArguments(cat, trace);
        // also prints "boo":
        assertEquals("boojum", (String) catTrace.invokeExact("boo", "jum"));````</blockquote>
        Here is pseudocode for the resulting adapter. In the code, `T`
        represents the result type of the `target` and resulting adapter.
        `V`/`v` represent the type and value of the parameter and argument
        of `target` that precedes the folding position; `V` also is
        the result type of the `combiner`. `A`/`a` denote the
        types and values of the `N` parameters and arguments at the folding
        position. `B`/`b` represent the types and values of the
        `target` parameters and arguments that follow the folded parameters
        and arguments.
        <blockquote>````// there are N arguments in A...
        T target(V, A[N]..., B...);
        V combiner(A...);
        T adapter(A... a, B... b) {
          V v = combiner(a...);
          return target(v, a..., b...);`
        // and if the combiner has a void return:
        T target2(A[N]..., B...);
        void combiner2(A...);
        T adapter2(A... a, B... b) {
          combiner2(a...);
          return target2(a..., b...);
        }
        }```</blockquote>
        
        *Note:* The resulting adapter is never a MethodHandle.asVarargsCollector
        variable-arity method handle, even if the original target method handle was.

        Arguments
        - target: the method handle to invoke after arguments are combined
        - combiner: method handle to call initially on the incoming arguments

        Returns
        - method handle which incorporates the specified argument folding logic

        Raises
        - NullPointerException: if either argument is null
        - IllegalArgumentException: if `combiner`'s return type
                 is non-void and not the same as the first argument type of
                 the target, or if the initial `N` argument types
                 of the target
                 (skipping one matching the `combiner`'s return type)
                 are not identical with the argument types of `combiner`
        """
        ...


    @staticmethod
    def foldArguments(target: "MethodHandle", pos: int, combiner: "MethodHandle") -> "MethodHandle":
        """
        Adapts a target method handle by pre-processing some of its arguments, starting at a given position, and then
        calling the target with the result of the pre-processing, inserted into the original sequence of arguments just
        before the folded arguments.
        
        This method is closely related to .foldArguments(MethodHandle, MethodHandle), but allows to control the
        position in the parameter list at which folding takes place. The argument controlling this, `pos`, is a
        zero-based index. The aforementioned method .foldArguments(MethodHandle, MethodHandle) assumes position
        0.

        Arguments
        - target: the method handle to invoke after arguments are combined
        - pos: the position at which to start folding and at which to insert the folding result; if this is `0`, the effect is the same as for .foldArguments(MethodHandle, MethodHandle).
        - combiner: method handle to call initially on the incoming arguments

        Returns
        - method handle which incorporates the specified argument folding logic

        Raises
        - NullPointerException: if either argument is null
        - IllegalArgumentException: if either of the following two conditions holds:
                 (1) `combiner`'s return type is non-`void` and not the same as the argument type at position
                     `pos` of the target signature;
                 (2) the `N` argument types at position `pos` of the target signature (skipping one matching
                     the `combiner`'s return type) are not identical with the argument types of `combiner`.

        See
        - .foldArguments(MethodHandle, MethodHandle)

        Since
        - 9

        Unknown Tags
        - Example:
        <blockquote>````import static java.lang.invoke.MethodHandles.*;
            import static java.lang.invoke.MethodType.*;
            ...
            MethodHandle trace = publicLookup().findVirtual(java.io.PrintStream.class,
            "println", methodType(void.class, String.class))
            .bindTo(System.out);
            MethodHandle cat = lookup().findVirtual(String.class,
            "concat", methodType(String.class, String.class));
            assertEquals("boojum", (String) cat.invokeExact("boo", "jum"));
            MethodHandle catTrace = foldArguments(cat, 1, trace);
            // also prints "jum":
            assertEquals("boojum", (String) catTrace.invokeExact("boo", "jum"));````</blockquote>
        Here is pseudocode for the resulting adapter. In the code, `T`
        represents the result type of the `target` and resulting adapter.
        `V`/`v` represent the type and value of the parameter and argument
        of `target` that precedes the folding position; `V` also is
        the result type of the `combiner`. `A`/`a` denote the
        types and values of the `N` parameters and arguments at the folding
        position. `Z`/`z` and `B`/`b` represent the types
        and values of the `target` parameters and arguments that precede and
        follow the folded parameters and arguments starting at `pos`,
        respectively.
        <blockquote>````// there are N arguments in A...
        T target(Z..., V, A[N]..., B...);
        V combiner(A...);
        T adapter(Z... z, A... a, B... b) {
          V v = combiner(a...);
          return target(z..., v, a..., b...);`
        // and if the combiner has a void return:
        T target2(Z..., A[N]..., B...);
        void combiner2(A...);
        T adapter2(Z... z, A... a, B... b) {
          combiner2(a...);
          return target2(z..., a..., b...);
        }
        }```</blockquote>
        
        *Note:* The resulting adapter is never a MethodHandle.asVarargsCollector
        variable-arity method handle, even if the original target method handle was.
        """
        ...


    @staticmethod
    def guardWithTest(test: "MethodHandle", target: "MethodHandle", fallback: "MethodHandle") -> "MethodHandle":
        """
        Makes a method handle which adapts a target method handle,
        by guarding it with a test, a boolean-valued method handle.
        If the guard fails, a fallback handle is called instead.
        All three method handles must have the same corresponding
        argument and return types, except that the return type
        of the test must be boolean, and the test is allowed
        to have fewer arguments than the other two method handles.
        
        Here is pseudocode for the resulting adapter. In the code, `T`
        represents the uniform result type of the three involved handles;
        `A`/`a`, the types and values of the `target`
        parameters and arguments that are consumed by the `test`; and
        `B`/`b`, those types and values of the `target`
        parameters and arguments that are not consumed by the `test`.
        <blockquote>````boolean test(A...);
        T target(A...,B...);
        T fallback(A...,B...);
        T adapter(A... a,B... b) {
          if (test(a...))
            return target(a..., b...);
          else
            return fallback(a..., b...);`
        }```</blockquote>
        Note that the test arguments (`a...` in the pseudocode) cannot
        be modified by execution of the test, and so are passed unchanged
        from the caller to the target or fallback as appropriate.

        Arguments
        - test: method handle used for test, must return boolean
        - target: method handle to call if test passes
        - fallback: method handle to call if test fails

        Returns
        - method handle which incorporates the specified if/then/else logic

        Raises
        - NullPointerException: if any argument is null
        - IllegalArgumentException: if `test` does not return boolean,
                 or if all three method types do not match (with the return
                 type of `test` changed to match that of the target).
        """
        ...


    @staticmethod
    def catchException(target: "MethodHandle", exType: type["Throwable"], handler: "MethodHandle") -> "MethodHandle":
        """
        Makes a method handle which adapts a target method handle,
        by running it inside an exception handler.
        If the target returns normally, the adapter returns that value.
        If an exception matching the specified type is thrown, the fallback
        handle is called instead on the exception, plus the original arguments.
        
        The target and handler must have the same corresponding
        argument and return types, except that handler may omit trailing arguments
        (similarly to the predicate in .guardWithTest guardWithTest).
        Also, the handler must have an extra leading parameter of `exType` or a supertype.
        
        Here is pseudocode for the resulting adapter. In the code, `T`
        represents the return type of the `target` and `handler`,
        and correspondingly that of the resulting adapter; `A`/`a`,
        the types and values of arguments to the resulting handle consumed by
        `handler`; and `B`/`b`, those of arguments to the
        resulting handle discarded by `handler`.
        <blockquote>````T target(A..., B...);
        T handler(ExType, A...);
        T adapter(A... a, B... b) {
          try {
            return target(a..., b...);` catch (ExType ex) {
            return handler(ex, a...);
          }
        }
        }```</blockquote>
        Note that the saved arguments (`a...` in the pseudocode) cannot
        be modified by execution of the target, and so are passed unchanged
        from the caller to the handler, if the handler is invoked.
        
        The target and handler must return the same type, even if the handler
        always throws.  (This might happen, for instance, because the handler
        is simulating a `finally` clause).
        To create such a throwing handler, compose the handler creation logic
        with .throwException throwException,
        in order to create a method handle of the correct return type.

        Arguments
        - target: method handle to call
        - exType: the type of exception which the handler will catch
        - handler: method handle to call if a matching exception is thrown

        Returns
        - method handle which incorporates the specified try/catch logic

        Raises
        - NullPointerException: if any argument is null
        - IllegalArgumentException: if `handler` does not accept
                 the given exception type, or if the method handle types do
                 not match in their return types and their
                 corresponding parameters

        See
        - MethodHandles.tryFinally(MethodHandle, MethodHandle)
        """
        ...


    @staticmethod
    def throwException(returnType: type[Any], exType: type["Throwable"]) -> "MethodHandle":
        """
        Produces a method handle which will throw exceptions of the given `exType`.
        The method handle will accept a single argument of `exType`,
        and immediately throw it as an exception.
        The method type will nominally specify a return of `returnType`.
        The return type may be anything convenient:  It doesn't matter to the
        method handle's behavior, since it will never return normally.

        Arguments
        - returnType: the return type of the desired method handle
        - exType: the parameter type of the desired method handle

        Returns
        - method handle which can throw the given exceptions

        Raises
        - NullPointerException: if either argument is null
        """
        ...


    @staticmethod
    def loop(*clauses: Tuple[list["MethodHandle"], ...]) -> "MethodHandle":
        """
        Constructs a method handle representing a loop with several loop variables that are updated and checked upon each
        iteration. Upon termination of the loop due to one of the predicates, a corresponding finalizer is run and
        delivers the loop's result, which is the return value of the resulting handle.
        
        Intuitively, every loop is formed by one or more "clauses", each specifying a local *iteration variable* and/or a loop
        exit. Each iteration of the loop executes each clause in order. A clause can optionally update its iteration
        variable; it can also optionally perform a test and conditional loop exit. In order to express this logic in
        terms of method handles, each clause will specify up to four independent actions:
        - *init:* Before the loop executes, the initialization of an iteration variable `v` of type `V`.
        - *step:* When a clause executes, an update step for the iteration variable `v`.
        - *pred:* When a clause executes, a predicate execution to test for loop exit.
        - *fini:* If a clause causes a loop exit, a finalizer execution to compute the loop's return value.
        
        The full sequence of all iteration variable types, in clause order, will be notated as `(V...)`.
        The values themselves will be `(v...)`.  When we speak of "parameter lists", we will usually
        be referring to types, but in some contexts (describing execution) the lists will be of actual values.
        
        Some of these clause parts may be omitted according to certain rules, and useful default behavior is provided in
        this case. See below for a detailed description.
        
        *Parameters optional everywhere:*
        Each clause function is allowed but not required to accept a parameter for each iteration variable `v`.
        As an exception, the init functions cannot take any `v` parameters,
        because those values are not yet computed when the init functions are executed.
        Any clause function may neglect to take any trailing subsequence of parameters it is entitled to take.
        In fact, any clause function may take no arguments at all.
        
        *Loop parameters:*
        A clause function may take all the iteration variable values it is entitled to, in which case
        it may also take more trailing parameters. Such extra values are called *loop parameters*,
        with their types and values notated as `(A...)` and `(a...)`.
        These become the parameters of the resulting loop handle, to be supplied whenever the loop is executed.
        (Since init functions do not accept iteration variables `v`, any parameter to an
        init function is automatically a loop parameter `a`.)
        As with iteration variables, clause functions are allowed but not required to accept loop parameters.
        These loop parameters act as loop-invariant values visible across the whole loop.
        
        *Parameters visible everywhere:*
        Each non-init clause function is permitted to observe the entire loop state, because it can be passed the full
        list `(v... a...)` of current iteration variable values and incoming loop parameters.
        The init functions can observe initial pre-loop state, in the form `(a...)`.
        Most clause functions will not need all of this information, but they will be formally connected to it
        as if by .dropArguments.
        <a id="astar"></a>
        More specifically, we shall use the notation `(V*)` to express an arbitrary prefix of a full
        sequence `(V...)` (and likewise for `(v*)`, `(A*)`, `(a*)`).
        In that notation, the general form of an init function parameter list
        is `(A*)`, and the general form of a non-init function parameter list is `(V*)` or `(V... A*)`.
        
        *Checking clause structure:*
        Given a set of clauses, there is a number of checks and adjustments performed to connect all the parts of the
        loop. They are spelled out in detail in the steps below. In these steps, every occurrence of the word "must"
        corresponds to a place where IllegalArgumentException will be thrown if the required constraint is not
        met by the inputs to the loop combinator.
        
        *Effectively identical sequences:*
        <a id="effid"></a>
        A parameter list `A` is defined to be *effectively identical* to another parameter list `B`
        if `A` and `B` are identical, or if `A` is shorter and is identical with a proper prefix of `B`.
        When speaking of an unordered set of parameter lists, we say they the set is "effectively identical"
        as a whole if the set contains a longest list, and all members of the set are effectively identical to
        that longest list.
        For example, any set of type sequences of the form `(V*)` is effectively identical,
        and the same is True if more sequences of the form `(V... A*)` are added.
        
        *Step 0: Determine clause structure.*<ol type="a">
        - The clause array (of type `MethodHandle[][]`) must be non-`null` and contain at least one element.
        - The clause array may not contain `null`s or sub-arrays longer than four elements.
        - Clauses shorter than four elements are treated as if they were padded by `null` elements to length
        four. Padding takes place by appending elements to the array.
        - Clauses with all `null`s are disregarded.
        - Each clause is treated as a four-tuple of functions, called "init", "step", "pred", and "fini".
        </ol>
        
        *Step 1A: Determine iteration variable types `(V...)`.*<ol type="a">
        - The iteration variable type for each clause is determined using the clause's init and step return types.
        - If both functions are omitted, there is no iteration variable for the corresponding clause (`void` is
        used as the type to indicate that). If one of them is omitted, the other's return type defines the clause's
        iteration variable type. If both are given, the common return type (they must be identical) defines the clause's
        iteration variable type.
        - Form the list of return types (in clause order), omitting all occurrences of `void`.
        - This list of types is called the "iteration variable types" (`(V...)`).
        </ol>
        
        *Step 1B: Determine loop parameters `(A...)`.*
        - Examine and collect init function parameter lists (which are of the form `(A*)`).
        - Examine and collect the suffixes of the step, pred, and fini parameter lists, after removing the iteration variable types.
        (They must have the form `(V... A*)`; collect the `(A*)` parts only.)
        - Do not collect suffixes from step, pred, and fini parameter lists that do not begin with all the iteration variable types.
        (These types will be checked in step 2, along with all the clause function types.)
        - Omitted clause functions are ignored.  (Equivalently, they are deemed to have empty parameter lists.)
        - All of the collected parameter lists must be effectively identical.
        - The longest parameter list (which is necessarily unique) is called the "external parameter list" (`(A...)`).
        - If there is no such parameter list, the external parameter list is taken to be the empty sequence.
        - The combined list consisting of iteration variable types followed by the external parameter types is called
        the "internal parameter list".
        
        
        *Step 1C: Determine loop return type.*<ol type="a">
        - Examine fini function return types, disregarding omitted fini functions.
        - If there are no fini functions, the loop return type is `void`.
        - Otherwise, the common return type `R` of the fini functions (their return types must be identical) defines the loop return
        type.
        </ol>
        
        *Step 1D: Check other types.*<ol type="a">
        - There must be at least one non-omitted pred function.
        - Every non-omitted pred function must have a `boolean` return type.
        </ol>
        
        *Step 2: Determine parameter lists.*<ol type="a">
        - The parameter list for the resulting loop handle will be the external parameter list `(A...)`.
        - The parameter list for init functions will be adjusted to the external parameter list.
        (Note that their parameter lists are already effectively identical to this list.)
        - The parameter list for every non-omitted, non-init (step, pred, and fini) function must be
        effectively identical to the internal parameter list `(V... A...)`.
        </ol>
        
        *Step 3: Fill in omitted functions.*<ol type="a">
        - If an init function is omitted, use a .empty default value for the clause's iteration variable
        type.
        - If a step function is omitted, use an .identity identity function of the clause's iteration
        variable type; insert dropped argument parameters before the identity function parameter for the non-`void`
        iteration variables of preceding clauses. (This will turn the loop variable into a local loop invariant.)
        - If a pred function is omitted, use a constant `True` function. (This will keep the loop going, as far
        as this clause is concerned.  Note that in such cases the corresponding fini function is unreachable.)
        - If a fini function is omitted, use a .empty default value for the
        loop return type.
        </ol>
        
        *Step 4: Fill in missing parameter types.*<ol type="a">
        - At this point, every init function parameter list is effectively identical to the external parameter list `(A...)`,
        but some lists may be shorter. For every init function with a short parameter list, pad out the end of the list.
        - At this point, every non-init function parameter list is effectively identical to the internal parameter
        list `(V... A...)`, but some lists may be shorter. For every non-init function with a short parameter list,
        pad out the end of the list.
        - Argument lists are padded out by .dropArgumentsToMatch(MethodHandle, int, List, int) dropping unused trailing arguments.
        </ol>
        
        *Final observations.*<ol type="a">
        - After these steps, all clauses have been adjusted by supplying omitted functions and arguments.
        - All init functions have a common parameter type list `(A...)`, which the final loop handle will also have.
        - All fini functions have a common return type `R`, which the final loop handle will also have.
        - All non-init functions have a common parameter type list `(V... A...)`, of
        (non-`void`) iteration variables `V` followed by loop parameters.
        - Each pair of init and step functions agrees in their return type `V`.
        - Each non-init function will be able to observe the current values `(v...)` of all iteration variables.
        - Every function will be able to observe the incoming values `(a...)` of all loop parameters.
        </ol>
        
        *Example.* As a consequence of step 1A above, the `loop` combinator has the following property:
        
        - Given `N` clauses `Cn = {null, Sn, Pn`} with `n = 1..N`.
        - Suppose predicate handles `Pn` are either `null` or have no parameters.
        (Only one `Pn` has to be non-`null`.)
        - Suppose step handles `Sn` have signatures `(B1..BX)Rn`, for some constant `X>=N`.
        - Suppose `Q` is the count of non-void types `Rn`, and `(V1...VQ)` is the sequence of those types.
        - It must be that `Vn == Bn` for `n = 1..min(X,Q)`.
        - The parameter types `Vn` will be interpreted as loop-local state elements `(V...)`.
        - Any remaining types `BQ+1..BX` (if `Q<X`) will determine
        the resulting loop handle's parameter types `(A...)`.
        
        In this example, the loop handle parameters `(A...)` were derived from the step functions,
        which is natural if most of the loop computation happens in the steps.  For some loops,
        the burden of computation might be heaviest in the pred functions, and so the pred functions
        might need to accept the loop parameter values.  For loops with complex exit logic, the fini
        functions might need to accept loop parameters, and likewise for loops with complex entry logic,
        where the init functions will need the extra parameters.  For such reasons, the rules for
        determining these parameters are as symmetric as possible, across all clause parts.
        In general, the loop parameters function as common invariant values across the whole
        loop, while the iteration variables function as common variant values, or (if there is
        no step function) as internal loop invariant temporaries.
        
        *Loop execution.*<ol type="a">
        - When the loop is called, the loop input values are saved in locals, to be passed to
        every clause function. These locals are loop invariant.
        - Each init function is executed in clause order (passing the external arguments `(a...)`)
        and the non-`void` values are saved (as the iteration variables `(v...)`) into locals.
        These locals will be loop varying (unless their steps behave as identity functions, as noted above).
        - All function executions (except init functions) will be passed the internal parameter list, consisting of
        the non-`void` iteration values `(v...)` (in clause order) and then the loop inputs `(a...)`
        (in argument order).
        - The step and pred functions are then executed, in clause order (step before pred), until a pred function
        returns `False`.
        - The non-`void` result from a step function call is used to update the corresponding value in the
        sequence `(v...)` of loop variables.
        The updated value is immediately visible to all subsequent function calls.
        - If a pred function returns `False`, the corresponding fini function is called, and the resulting value
        (of type `R`) is returned from the loop as a whole.
        - If all the pred functions always return True, no fini function is ever invoked, and the loop cannot exit
        except by throwing an exception.
        </ol>
        
        *Usage tips.*
        
        - Although each step function will receive the current values of *all* the loop variables,
        sometimes a step function only needs to observe the current value of its own variable.
        In that case, the step function may need to explicitly .dropArguments drop all preceding loop variables.
        This will require mentioning their types, in an expression like `dropArguments(step, 0, V0.class, ...)`.
        - Loop variables are not required to vary; they can be loop invariant.  A clause can create
        a loop invariant by a suitable init function with no step, pred, or fini function.  This may be
        useful to "wire" an incoming loop argument into the step or pred function of an adjacent loop variable.
        - If some of the clause functions are virtual methods on an instance, the instance
        itself can be conveniently placed in an initial invariant loop "variable", using an initial clause
        like `new MethodHandle[]{identity(ObjType.class)`}.  In that case, the instance reference
        will be the first iteration variable value, and it will be easy to use virtual
        methods as clause parts, since all of them will take a leading instance reference matching that value.
        
        
        Here is pseudocode for the resulting loop handle. As above, `V` and `v` represent the types
        and values of loop variables; `A` and `a` represent arguments passed to the whole loop;
        and `R` is the common result type of all finalizers as well as of the resulting loop.
        <blockquote>````V... init...(A...);
        boolean pred...(V..., A...);
        V... step...(V..., A...);
        R fini...(V..., A...);
        R loop(A... a) {
          V... v... = init...(a...);
          for (;;) {
            for ((v, p, s, f) in (v..., pred..., step..., fini...)) {
              v = s(v..., a...);
              if (!p(v..., a...)) {
                return f(v..., a...);`
            }
          }
        }
        }```</blockquote>
        Note that the parameter type lists `(V...)` and `(A...)` have been expanded
        to their full length, even though individual clause functions may neglect to take them all.
        As noted above, missing parameters are filled in as if by .dropArgumentsToMatch(MethodHandle, int, List, int).

        Arguments
        - clauses: an array of arrays (4-tuples) of MethodHandles adhering to the rules described above.

        Returns
        - a method handle embodying the looping behavior as defined by the arguments.

        Raises
        - IllegalArgumentException: in case any of the constraints described above is violated.

        See
        - MethodHandles.iteratedLoop(MethodHandle, MethodHandle, MethodHandle)

        Since
        - 9

        Unknown Tags
        - Example:
        <blockquote>````// iterative implementation of the factorial function as a loop handle
        static int one(int k) { return 1;`
        static int inc(int i, int acc, int k) { return i + 1; }
        static int mult(int i, int acc, int k) { return i * acc; }
        static boolean pred(int i, int acc, int k) { return i < k; }
        static int fin(int i, int acc, int k) { return acc; }
        // assume MH_one, MH_inc, MH_mult, MH_pred, and MH_fin are handles to the above methods
        // null initializer for counter, should initialize to 0
        MethodHandle[] counterClause = new MethodHandle[]{null, MH_inc};
        MethodHandle[] accumulatorClause = new MethodHandle[]{MH_one, MH_mult, MH_pred, MH_fin};
        MethodHandle loop = MethodHandles.loop(counterClause, accumulatorClause);
        assertEquals(120, loop.invoke(5));
        }```</blockquote>
        The same example, dropping arguments and using combinators:
        <blockquote>````// simplified implementation of the factorial function as a loop handle
        static int inc(int i) { return i + 1;` // drop acc, k
        static int mult(int i, int acc) { return i * acc; } //drop k
        static boolean cmp(int i, int k) { return i < k; }
        // assume MH_inc, MH_mult, and MH_cmp are handles to the above methods
        // null initializer for counter, should initialize to 0
        MethodHandle MH_one = MethodHandles.constant(int.class, 1);
        MethodHandle MH_pred = MethodHandles.dropArguments(MH_cmp, 1, int.class); // drop acc
        MethodHandle MH_fin = MethodHandles.dropArguments(MethodHandles.identity(int.class), 0, int.class); // drop i
        MethodHandle[] counterClause = new MethodHandle[]{null, MH_inc};
        MethodHandle[] accumulatorClause = new MethodHandle[]{MH_one, MH_mult, MH_pred, MH_fin};
        MethodHandle loop = MethodHandles.loop(counterClause, accumulatorClause);
        assertEquals(720, loop.invoke(6));
        }```</blockquote>
        A similar example, using a helper object to hold a loop parameter:
        <blockquote>````// instance-based implementation of the factorial function as a loop handle
        static class FacLoop {
          final int k;
          FacLoop(int k) { this.k = k;`
          int inc(int i) { return i + 1; }
          int mult(int i, int acc) { return i * acc; }
          boolean pred(int i) { return i < k; }
          int fin(int i, int acc) { return acc; }
        }
        // assume MH_FacLoop is a handle to the constructor
        // assume MH_inc, MH_mult, MH_pred, and MH_fin are handles to the above methods
        // null initializer for counter, should initialize to 0
        MethodHandle MH_one = MethodHandles.constant(int.class, 1);
        MethodHandle[] instanceClause = new MethodHandle[]{MH_FacLoop};
        MethodHandle[] counterClause = new MethodHandle[]{null, MH_inc};
        MethodHandle[] accumulatorClause = new MethodHandle[]{MH_one, MH_mult, MH_pred, MH_fin};
        MethodHandle loop = MethodHandles.loop(instanceClause, counterClause, accumulatorClause);
        assertEquals(5040, loop.invoke(7));
        }```</blockquote>
        """
        ...


    @staticmethod
    def whileLoop(init: "MethodHandle", pred: "MethodHandle", body: "MethodHandle") -> "MethodHandle":
        """
        Constructs a `while` loop from an initializer, a body, and a predicate.
        This is a convenience wrapper for the .loop(MethodHandle[][]) generic loop combinator.
        
        The `pred` handle describes the loop condition; and `body`, its body. The loop resulting from this
        method will, in each iteration, first evaluate the predicate and then execute its body (if the predicate
        evaluates to `True`).
        The loop will terminate once the predicate evaluates to `False` (the body will not be executed in this case).
        
        The `init` handle describes the initial value of an additional optional loop-local variable.
        In each iteration, this loop-local variable, if present, will be passed to the `body`
        and updated with the value returned from its invocation. The result of loop execution will be
        the final value of the additional loop-local variable (if present).
        
        The following rules hold for these argument handles:
        - The `body` handle must not be `null`; its type must be of the form
        `(V A...)V`, where `V` is non-`void`, or else `(A...)void`.
        (In the `void` case, we assign the type `void` to the name `V`,
        and we will write `(V A...)V` with the understanding that a `void` type `V`
        is quietly dropped from the parameter list, leaving `(A...)V`.)
        - The parameter list `(V A...)` of the body is called the *internal parameter list*.
        It will constrain the parameter lists of the other loop parts.
        - If the iteration variable type `V` is dropped from the internal parameter list, the resulting shorter
        list `(A...)` is called the *external parameter list*.
        - The body return type `V`, if non-`void`, determines the type of an
        additional state variable of the loop.
        The body must both accept and return a value of this type `V`.
        - If `init` is non-`null`, it must have return type `V`.
        Its parameter list (of some <a href="MethodHandles.html#astar">form `(A*)`</a>) must be
        <a href="MethodHandles.html#effid">effectively identical</a>
        to the external parameter list `(A...)`.
        - If `init` is `null`, the loop variable will be initialized to its
        .empty default value.
        - The `pred` handle must not be `null`.  It must have `boolean` as its return type.
        Its parameter list (either empty or of the form `(V A*)`) must be
        effectively identical to the internal parameter list.
        
        
        The resulting loop handle's result type and parameter signature are determined as follows:
        - The loop handle's result type is the result type `V` of the body.
        - The loop handle's parameter types are the types `(A...)`,
        from the external parameter list.
        
        
        Here is pseudocode for the resulting loop handle. In the code, `V`/`v` represent the type / value of
        the sole loop variable as well as the result type of the loop; and `A`/`a`, that of the argument
        passed to the loop.
        <blockquote>````V init(A...);
        boolean pred(V, A...);
        V body(V, A...);
        V whileLoop(A... a...) {
          V v = init(a...);
          while (pred(v, a...)) {
            v = body(v, a...);`
          return v;
        }
        }```</blockquote>

        Arguments
        - init: optional initializer, providing the initial value of the loop variable.
                    May be `null`, implying a default initial value.  See above for other constraints.
        - pred: condition for the loop, which may not be `null`. Its result type must be `boolean`. See
                    above for other constraints.
        - body: body of the loop, which may not be `null`. It controls the loop parameters and result type.
                    See above for other constraints.

        Returns
        - a method handle implementing the `while` loop as described by the arguments.

        Raises
        - IllegalArgumentException: if the rules for the arguments are violated.
        - NullPointerException: if `pred` or `body` are `null`.

        See
        - .doWhileLoop(MethodHandle, MethodHandle, MethodHandle)

        Since
        - 9

        Unknown Tags
        - Example:
        <blockquote>````// implement the zip function for lists as a loop handle
        static List<String> initZip(Iterator<String> a, Iterator<String> b) { return new ArrayList<>();`
        static boolean zipPred(List<String> zip, Iterator<String> a, Iterator<String> b) { return a.hasNext() && b.hasNext(); }
        static List<String> zipStep(List<String> zip, Iterator<String> a, Iterator<String> b) {
          zip.add(a.next());
          zip.add(b.next());
          return zip;
        }
        // assume MH_initZip, MH_zipPred, and MH_zipStep are handles to the above methods
        MethodHandle loop = MethodHandles.whileLoop(MH_initZip, MH_zipPred, MH_zipStep);
        List<String> a = Arrays.asList("a", "b", "c", "d");
        List<String> b = Arrays.asList("e", "f", "g", "h");
        List<String> zipped = Arrays.asList("a", "e", "b", "f", "c", "g", "d", "h");
        assertEquals(zipped, (List<String>) loop.invoke(a.iterator(), b.iterator()));
        }```</blockquote>
        - The implementation of this method can be expressed as follows:
        <blockquote>````MethodHandle whileLoop(MethodHandle init, MethodHandle pred, MethodHandle body) {
            MethodHandle fini = (body.type().returnType() == void.class
                                ? null : identity(body.type().returnType()));
            MethodHandle[]
                checkExit = { null, null, pred, fini`,
                varBody   = { init, body };
            return loop(checkExit, varBody);
        }
        }```</blockquote>
        """
        ...


    @staticmethod
    def doWhileLoop(init: "MethodHandle", body: "MethodHandle", pred: "MethodHandle") -> "MethodHandle":
        """
        Constructs a `do-while` loop from an initializer, a body, and a predicate.
        This is a convenience wrapper for the .loop(MethodHandle[][]) generic loop combinator.
        
        The `pred` handle describes the loop condition; and `body`, its body. The loop resulting from this
        method will, in each iteration, first execute its body and then evaluate the predicate.
        The loop will terminate once the predicate evaluates to `False` after an execution of the body.
        
        The `init` handle describes the initial value of an additional optional loop-local variable.
        In each iteration, this loop-local variable, if present, will be passed to the `body`
        and updated with the value returned from its invocation. The result of loop execution will be
        the final value of the additional loop-local variable (if present).
        
        The following rules hold for these argument handles:
        - The `body` handle must not be `null`; its type must be of the form
        `(V A...)V`, where `V` is non-`void`, or else `(A...)void`.
        (In the `void` case, we assign the type `void` to the name `V`,
        and we will write `(V A...)V` with the understanding that a `void` type `V`
        is quietly dropped from the parameter list, leaving `(A...)V`.)
        - The parameter list `(V A...)` of the body is called the *internal parameter list*.
        It will constrain the parameter lists of the other loop parts.
        - If the iteration variable type `V` is dropped from the internal parameter list, the resulting shorter
        list `(A...)` is called the *external parameter list*.
        - The body return type `V`, if non-`void`, determines the type of an
        additional state variable of the loop.
        The body must both accept and return a value of this type `V`.
        - If `init` is non-`null`, it must have return type `V`.
        Its parameter list (of some <a href="MethodHandles.html#astar">form `(A*)`</a>) must be
        <a href="MethodHandles.html#effid">effectively identical</a>
        to the external parameter list `(A...)`.
        - If `init` is `null`, the loop variable will be initialized to its
        .empty default value.
        - The `pred` handle must not be `null`.  It must have `boolean` as its return type.
        Its parameter list (either empty or of the form `(V A*)`) must be
        effectively identical to the internal parameter list.
        
        
        The resulting loop handle's result type and parameter signature are determined as follows:
        - The loop handle's result type is the result type `V` of the body.
        - The loop handle's parameter types are the types `(A...)`,
        from the external parameter list.
        
        
        Here is pseudocode for the resulting loop handle. In the code, `V`/`v` represent the type / value of
        the sole loop variable as well as the result type of the loop; and `A`/`a`, that of the argument
        passed to the loop.
        <blockquote>````V init(A...);
        boolean pred(V, A...);
        V body(V, A...);
        V doWhileLoop(A... a...) {
          V v = init(a...);
          do {
            v = body(v, a...);` while (pred(v, a...));
          return v;
        }
        }```</blockquote>

        Arguments
        - init: optional initializer, providing the initial value of the loop variable.
                    May be `null`, implying a default initial value.  See above for other constraints.
        - body: body of the loop, which may not be `null`. It controls the loop parameters and result type.
                    See above for other constraints.
        - pred: condition for the loop, which may not be `null`. Its result type must be `boolean`. See
                    above for other constraints.

        Returns
        - a method handle implementing the `while` loop as described by the arguments.

        Raises
        - IllegalArgumentException: if the rules for the arguments are violated.
        - NullPointerException: if `pred` or `body` are `null`.

        See
        - .whileLoop(MethodHandle, MethodHandle, MethodHandle)

        Since
        - 9

        Unknown Tags
        - Example:
        <blockquote>````// int i = 0; while (i < limit) { ++i;` return i; => limit
        static int zero(int limit) { return 0; }
        static int step(int i, int limit) { return i + 1; }
        static boolean pred(int i, int limit) { return i < limit; }
        // assume MH_zero, MH_step, and MH_pred are handles to the above methods
        MethodHandle loop = MethodHandles.doWhileLoop(MH_zero, MH_step, MH_pred);
        assertEquals(23, loop.invoke(23));
        }```</blockquote>
        - The implementation of this method can be expressed as follows:
        <blockquote>````MethodHandle doWhileLoop(MethodHandle init, MethodHandle body, MethodHandle pred) {
            MethodHandle fini = (body.type().returnType() == void.class
                                ? null : identity(body.type().returnType()));
            MethodHandle[] clause = { init, body, pred, fini`;
            return loop(clause);
        }
        }```</blockquote>
        """
        ...


    @staticmethod
    def countedLoop(iterations: "MethodHandle", init: "MethodHandle", body: "MethodHandle") -> "MethodHandle":
        """
        Constructs a loop that runs a given number of iterations.
        This is a convenience wrapper for the .loop(MethodHandle[][]) generic loop combinator.
        
        The number of iterations is determined by the `iterations` handle evaluation result.
        The loop counter `i` is an extra loop iteration variable of type `int`.
        It will be initialized to 0 and incremented by 1 in each iteration.
        
        If the `body` handle returns a non-`void` type `V`, a leading loop iteration variable
        of that type is also present.  This variable is initialized using the optional `init` handle,
        or to the .empty default value of type `V` if that handle is `null`.
        
        In each iteration, the iteration variables are passed to an invocation of the `body` handle.
        A non-`void` value returned from the body (of type `V`) updates the leading
        iteration variable.
        The result of the loop handle execution will be the final `V` value of that variable
        (or `void` if there is no `V` variable).
        
        The following rules hold for the argument handles:
        - The `iterations` handle must not be `null`, and must return
        the type `int`, referred to here as `I` in parameter type lists.
        - The `body` handle must not be `null`; its type must be of the form
        `(V I A...)V`, where `V` is non-`void`, or else `(I A...)void`.
        (In the `void` case, we assign the type `void` to the name `V`,
        and we will write `(V I A...)V` with the understanding that a `void` type `V`
        is quietly dropped from the parameter list, leaving `(I A...)V`.)
        - The parameter list `(V I A...)` of the body contributes to a list
        of types called the *internal parameter list*.
        It will constrain the parameter lists of the other loop parts.
        - As a special case, if the body contributes only `V` and `I` types,
        with no additional `A` types, then the internal parameter list is extended by
        the argument types `A...` of the `iterations` handle.
        - If the iteration variable types `(V I)` are dropped from the internal parameter list, the resulting shorter
        list `(A...)` is called the *external parameter list*.
        - The body return type `V`, if non-`void`, determines the type of an
        additional state variable of the loop.
        The body must both accept a leading parameter and return a value of this type `V`.
        - If `init` is non-`null`, it must have return type `V`.
        Its parameter list (of some <a href="MethodHandles.html#astar">form `(A*)`</a>) must be
        <a href="MethodHandles.html#effid">effectively identical</a>
        to the external parameter list `(A...)`.
        - If `init` is `null`, the loop variable will be initialized to its
        .empty default value.
        - The parameter list of `iterations` (of some form `(A*)`) must be
        effectively identical to the external parameter list `(A...)`.
        
        
        The resulting loop handle's result type and parameter signature are determined as follows:
        - The loop handle's result type is the result type `V` of the body.
        - The loop handle's parameter types are the types `(A...)`,
        from the external parameter list.
        
        
        Here is pseudocode for the resulting loop handle. In the code, `V`/`v` represent the type / value of
        the second loop variable as well as the result type of the loop; and `A...`/`a...` represent
        arguments passed to the loop.
        <blockquote>````int iterations(A...);
        V init(A...);
        V body(V, int, A...);
        V countedLoop(A... a...) {
          int end = iterations(a...);
          V v = init(a...);
          for (int i = 0; i < end; ++i) {
            v = body(v, i, a...);`
          return v;
        }
        }```</blockquote>

        Arguments
        - iterations: a non-`null` handle to return the number of iterations this loop should run. The handle's
                          result type must be `int`. See above for other constraints.
        - init: optional initializer, providing the initial value of the loop variable.
                    May be `null`, implying a default initial value.  See above for other constraints.
        - body: body of the loop, which may not be `null`.
                    It controls the loop parameters and result type in the standard case (see above for details).
                    It must accept its own return type (if non-void) plus an `int` parameter (for the counter),
                    and may accept any number of additional types.
                    See above for other constraints.

        Returns
        - a method handle representing the loop.

        Raises
        - NullPointerException: if either of the `iterations` or `body` handles is `null`.
        - IllegalArgumentException: if any argument violates the rules formulated above.

        See
        - .countedLoop(MethodHandle, MethodHandle, MethodHandle, MethodHandle)

        Since
        - 9

        Unknown Tags
        - Example with a fully conformant body method:
        <blockquote>````// String s = "Lambdaman!"; for (int i = 0; i < 13; ++i) { s = "na " + s;` return s;
        // => a variation on a well known theme
        static String step(String v, int counter, String init) { return "na " + v; }
        // assume MH_step is a handle to the method above
        MethodHandle fit13 = MethodHandles.constant(int.class, 13);
        MethodHandle start = MethodHandles.identity(String.class);
        MethodHandle loop = MethodHandles.countedLoop(fit13, start, MH_step);
        assertEquals("na na na na na na na na na na na na na Lambdaman!", loop.invoke("Lambdaman!"));
        }```</blockquote>
        - Example with the simplest possible body method type,
        and passing the number of iterations to the loop invocation:
        <blockquote>````// String s = "Lambdaman!"; for (int i = 0; i < 13; ++i) { s = "na " + s;` return s;
        // => a variation on a well known theme
        static String step(String v, int counter ) { return "na " + v; }
        // assume MH_step is a handle to the method above
        MethodHandle count = MethodHandles.dropArguments(MethodHandles.identity(int.class), 1, String.class);
        MethodHandle start = MethodHandles.dropArguments(MethodHandles.identity(String.class), 0, int.class);
        MethodHandle loop = MethodHandles.countedLoop(count, start, MH_step);  // (v, i) -> "na " + v
        assertEquals("na na na na na na na na na na na na na Lambdaman!", loop.invoke(13, "Lambdaman!"));
        }```</blockquote>
        - Example that treats the number of iterations, string to append to, and string to append
        as loop parameters:
        <blockquote>````// String s = "Lambdaman!", t = "na"; for (int i = 0; i < 13; ++i) { s = t + " " + s;` return s;
        // => a variation on a well known theme
        static String step(String v, int counter, int iterations_, String pre, String start_) { return pre + " " + v; }
        // assume MH_step is a handle to the method above
        MethodHandle count = MethodHandles.identity(int.class);
        MethodHandle start = MethodHandles.dropArguments(MethodHandles.identity(String.class), 0, int.class, String.class);
        MethodHandle loop = MethodHandles.countedLoop(count, start, MH_step);  // (v, i, _, pre, _) -> pre + " " + v
        assertEquals("na na na na na na na na na na na na na Lambdaman!", loop.invoke(13, "na", "Lambdaman!"));
        }```</blockquote>
        - Example that illustrates the usage of .dropArgumentsToMatch(MethodHandle, int, List, int)
        to enforce a loop type:
        <blockquote>````// String s = "Lambdaman!", t = "na"; for (int i = 0; i < 13; ++i) { s = t + " " + s;` return s;
        // => a variation on a well known theme
        static String step(String v, int counter, String pre) { return pre + " " + v; }
        // assume MH_step is a handle to the method above
        MethodType loopType = methodType(String.class, String.class, int.class, String.class);
        MethodHandle count = MethodHandles.dropArgumentsToMatch(MethodHandles.identity(int.class),    0, loopType.parameterList(), 1);
        MethodHandle start = MethodHandles.dropArgumentsToMatch(MethodHandles.identity(String.class), 0, loopType.parameterList(), 2);
        MethodHandle body  = MethodHandles.dropArgumentsToMatch(MH_step,                              2, loopType.parameterList(), 0);
        MethodHandle loop = MethodHandles.countedLoop(count, start, body);  // (v, i, pre, _, _) -> pre + " " + v
        assertEquals("na na na na na na na na na na na na na Lambdaman!", loop.invoke("na", 13, "Lambdaman!"));
        }```</blockquote>
        - The implementation of this method can be expressed as follows:
        <blockquote>````MethodHandle countedLoop(MethodHandle iterations, MethodHandle init, MethodHandle body) {
            return countedLoop(empty(iterations.type()), iterations, init, body);`
        }```</blockquote>
        """
        ...


    @staticmethod
    def countedLoop(start: "MethodHandle", end: "MethodHandle", init: "MethodHandle", body: "MethodHandle") -> "MethodHandle":
        """
        Constructs a loop that counts over a range of numbers.
        This is a convenience wrapper for the .loop(MethodHandle[][]) generic loop combinator.
        
        The loop counter `i` is a loop iteration variable of type `int`.
        The `start` and `end` handles determine the start (inclusive) and end (exclusive)
        values of the loop counter.
        The loop counter will be initialized to the `int` value returned from the evaluation of the
        `start` handle and run to the value returned from `end` (exclusively) with a step width of 1.
        
        If the `body` handle returns a non-`void` type `V`, a leading loop iteration variable
        of that type is also present.  This variable is initialized using the optional `init` handle,
        or to the .empty default value of type `V` if that handle is `null`.
        
        In each iteration, the iteration variables are passed to an invocation of the `body` handle.
        A non-`void` value returned from the body (of type `V`) updates the leading
        iteration variable.
        The result of the loop handle execution will be the final `V` value of that variable
        (or `void` if there is no `V` variable).
        
        The following rules hold for the argument handles:
        - The `start` and `end` handles must not be `null`, and must both return
        the common type `int`, referred to here as `I` in parameter type lists.
        - The `body` handle must not be `null`; its type must be of the form
        `(V I A...)V`, where `V` is non-`void`, or else `(I A...)void`.
        (In the `void` case, we assign the type `void` to the name `V`,
        and we will write `(V I A...)V` with the understanding that a `void` type `V`
        is quietly dropped from the parameter list, leaving `(I A...)V`.)
        - The parameter list `(V I A...)` of the body contributes to a list
        of types called the *internal parameter list*.
        It will constrain the parameter lists of the other loop parts.
        - As a special case, if the body contributes only `V` and `I` types,
        with no additional `A` types, then the internal parameter list is extended by
        the argument types `A...` of the `end` handle.
        - If the iteration variable types `(V I)` are dropped from the internal parameter list, the resulting shorter
        list `(A...)` is called the *external parameter list*.
        - The body return type `V`, if non-`void`, determines the type of an
        additional state variable of the loop.
        The body must both accept a leading parameter and return a value of this type `V`.
        - If `init` is non-`null`, it must have return type `V`.
        Its parameter list (of some <a href="MethodHandles.html#astar">form `(A*)`</a>) must be
        <a href="MethodHandles.html#effid">effectively identical</a>
        to the external parameter list `(A...)`.
        - If `init` is `null`, the loop variable will be initialized to its
        .empty default value.
        - The parameter list of `start` (of some form `(A*)`) must be
        effectively identical to the external parameter list `(A...)`.
        - Likewise, the parameter list of `end` must be effectively identical
        to the external parameter list.
        
        
        The resulting loop handle's result type and parameter signature are determined as follows:
        - The loop handle's result type is the result type `V` of the body.
        - The loop handle's parameter types are the types `(A...)`,
        from the external parameter list.
        
        
        Here is pseudocode for the resulting loop handle. In the code, `V`/`v` represent the type / value of
        the second loop variable as well as the result type of the loop; and `A...`/`a...` represent
        arguments passed to the loop.
        <blockquote>````int start(A...);
        int end(A...);
        V init(A...);
        V body(V, int, A...);
        V countedLoop(A... a...) {
          int e = end(a...);
          int s = start(a...);
          V v = init(a...);
          for (int i = s; i < e; ++i) {
            v = body(v, i, a...);`
          return v;
        }
        }```</blockquote>

        Arguments
        - start: a non-`null` handle to return the start value of the loop counter, which must be `int`.
                     See above for other constraints.
        - end: a non-`null` handle to return the end value of the loop counter (the loop will run to
                   `end-1`). The result type must be `int`. See above for other constraints.
        - init: optional initializer, providing the initial value of the loop variable.
                    May be `null`, implying a default initial value.  See above for other constraints.
        - body: body of the loop, which may not be `null`.
                    It controls the loop parameters and result type in the standard case (see above for details).
                    It must accept its own return type (if non-void) plus an `int` parameter (for the counter),
                    and may accept any number of additional types.
                    See above for other constraints.

        Returns
        - a method handle representing the loop.

        Raises
        - NullPointerException: if any of the `start`, `end`, or `body` handles is `null`.
        - IllegalArgumentException: if any argument violates the rules formulated above.

        See
        - .countedLoop(MethodHandle, MethodHandle, MethodHandle)

        Since
        - 9

        Unknown Tags
        - The implementation of this method can be expressed as follows:
        <blockquote>````MethodHandle countedLoop(MethodHandle start, MethodHandle end, MethodHandle init, MethodHandle body) {
            MethodHandle returnVar = dropArguments(identity(init.type().returnType()), 0, int.class, int.class);
            // assume MH_increment and MH_predicate are handles to implementation-internal methods with
            // the following semantics:
            // MH_increment: (int limit, int counter) -> counter + 1
            // MH_predicate: (int limit, int counter) -> counter < limit
            Class<?> counterType = start.type().returnType();  // int
            Class<?> returnType = body.type().returnType();
            MethodHandle incr = MH_increment, pred = MH_predicate, retv = null;
            if (returnType != void.class) {  // ignore the V variable
                incr = dropArguments(incr, 1, returnType);  // (limit, v, i) => (limit, i)
                pred = dropArguments(pred, 1, returnType);  // ditto
                retv = dropArguments(identity(returnType), 0, counterType); // ignore limit`
            body = dropArguments(body, 0, counterType);  // ignore the limit variable
            MethodHandle[]
                loopLimit  = { end, null, pred, retv }, // limit = end(); i < limit || return v
                bodyClause = { init, body },            // v = init(); v = body(v, i)
                indexVar   = { start, incr };           // i = start(); i = i + 1
            return loop(loopLimit, bodyClause, indexVar);
        }
        }```</blockquote>
        """
        ...


    @staticmethod
    def iteratedLoop(iterator: "MethodHandle", init: "MethodHandle", body: "MethodHandle") -> "MethodHandle":
        """
        Constructs a loop that ranges over the values produced by an `Iterator<T>`.
        This is a convenience wrapper for the .loop(MethodHandle[][]) generic loop combinator.
        
        The iterator itself will be determined by the evaluation of the `iterator` handle.
        Each value it produces will be stored in a loop iteration variable of type `T`.
        
        If the `body` handle returns a non-`void` type `V`, a leading loop iteration variable
        of that type is also present.  This variable is initialized using the optional `init` handle,
        or to the .empty default value of type `V` if that handle is `null`.
        
        In each iteration, the iteration variables are passed to an invocation of the `body` handle.
        A non-`void` value returned from the body (of type `V`) updates the leading
        iteration variable.
        The result of the loop handle execution will be the final `V` value of that variable
        (or `void` if there is no `V` variable).
        
        The following rules hold for the argument handles:
        - The `body` handle must not be `null`; its type must be of the form
        `(V T A...)V`, where `V` is non-`void`, or else `(T A...)void`.
        (In the `void` case, we assign the type `void` to the name `V`,
        and we will write `(V T A...)V` with the understanding that a `void` type `V`
        is quietly dropped from the parameter list, leaving `(T A...)V`.)
        - The parameter list `(V T A...)` of the body contributes to a list
        of types called the *internal parameter list*.
        It will constrain the parameter lists of the other loop parts.
        - As a special case, if the body contributes only `V` and `T` types,
        with no additional `A` types, then the internal parameter list is extended by
        the argument types `A...` of the `iterator` handle; if it is `null` the
        single type `Iterable` is added and constitutes the `A...` list.
        - If the iteration variable types `(V T)` are dropped from the internal parameter list, the resulting shorter
        list `(A...)` is called the *external parameter list*.
        - The body return type `V`, if non-`void`, determines the type of an
        additional state variable of the loop.
        The body must both accept a leading parameter and return a value of this type `V`.
        - If `init` is non-`null`, it must have return type `V`.
        Its parameter list (of some <a href="MethodHandles.html#astar">form `(A*)`</a>) must be
        <a href="MethodHandles.html#effid">effectively identical</a>
        to the external parameter list `(A...)`.
        - If `init` is `null`, the loop variable will be initialized to its
        .empty default value.
        - If the `iterator` handle is non-`null`, it must have the return
        type `java.util.Iterator` or a subtype thereof.
        The iterator it produces when the loop is executed will be assumed
        to yield values which can be converted to type `T`.
        - The parameter list of an `iterator` that is non-`null` (of some form `(A*)`) must be
        effectively identical to the external parameter list `(A...)`.
        - If `iterator` is `null` it defaults to a method handle which behaves
        like java.lang.Iterable.iterator().  In that case, the internal parameter list
        `(V T A...)` must have at least one `A` type, and the default iterator
        handle parameter is adjusted to accept the leading `A` type, as if by
        the MethodHandle.asType asType conversion method.
        The leading `A` type must be `Iterable` or a subtype thereof.
        This conversion step, done at loop construction time, must not throw a `WrongMethodTypeException`.
        
        
        The type `T` may be either a primitive or reference.
        Since type `Iterator<T>` is erased in the method handle representation to the raw type `Iterator`,
        the `iteratedLoop` combinator adjusts the leading argument type for `body` to `Object`
        as if by the MethodHandle.asType asType conversion method.
        Therefore, if an iterator of the wrong type appears as the loop is executed, runtime exceptions may occur
        as the result of dynamic conversions performed by MethodHandle.asType(MethodType).
        
        The resulting loop handle's result type and parameter signature are determined as follows:
        - The loop handle's result type is the result type `V` of the body.
        - The loop handle's parameter types are the types `(A...)`,
        from the external parameter list.
        
        
        Here is pseudocode for the resulting loop handle. In the code, `V`/`v` represent the type / value of
        the loop variable as well as the result type of the loop; `T`/`t`, that of the elements of the
        structure the loop iterates over, and `A...`/`a...` represent arguments passed to the loop.
        <blockquote>````Iterator<T> iterator(A...);  // defaults to Iterable::iterator
        V init(A...);
        V body(V,T,A...);
        V iteratedLoop(A... a...) {
          Iterator<T> it = iterator(a...);
          V v = init(a...);
          while (it.hasNext()) {
            T t = it.next();
            v = body(v, t, a...);`
          return v;
        }
        }```</blockquote>

        Arguments
        - iterator: an optional handle to return the iterator to start the loop.
                        If non-`null`, the handle must return java.util.Iterator or a subtype.
                        See above for other constraints.
        - init: optional initializer, providing the initial value of the loop variable.
                    May be `null`, implying a default initial value.  See above for other constraints.
        - body: body of the loop, which may not be `null`.
                    It controls the loop parameters and result type in the standard case (see above for details).
                    It must accept its own return type (if non-void) plus a `T` parameter (for the iterated values),
                    and may accept any number of additional types.
                    See above for other constraints.

        Returns
        - a method handle embodying the iteration loop functionality.

        Raises
        - NullPointerException: if the `body` handle is `null`.
        - IllegalArgumentException: if any argument violates the above requirements.

        Since
        - 9

        Unknown Tags
        - Example:
        <blockquote>````// get an iterator from a list
        static List<String> reverseStep(List<String> r, String e) {
          r.add(0, e);
          return r;`
        static List<String> newArrayList() { return new ArrayList<>(); }
        // assume MH_reverseStep and MH_newArrayList are handles to the above methods
        MethodHandle loop = MethodHandles.iteratedLoop(null, MH_newArrayList, MH_reverseStep);
        List<String> list = Arrays.asList("a", "b", "c", "d", "e");
        List<String> reversedList = Arrays.asList("e", "d", "c", "b", "a");
        assertEquals(reversedList, (List<String>) loop.invoke(list));
        }```</blockquote>
        - The implementation of this method can be expressed approximately as follows:
        <blockquote>````MethodHandle iteratedLoop(MethodHandle iterator, MethodHandle init, MethodHandle body) {
            // assume MH_next, MH_hasNext, MH_startIter are handles to methods of Iterator/Iterable
            Class<?> returnType = body.type().returnType();
            Class<?> ttype = body.type().parameterType(returnType == void.class ? 0 : 1);
            MethodHandle nextVal = MH_next.asType(MH_next.type().changeReturnType(ttype));
            MethodHandle retv = null, step = body, startIter = iterator;
            if (returnType != void.class) {
                // the simple thing first:  in (I V A...), drop the I to get V
                retv = dropArguments(identity(returnType), 0, Iterator.class);
                // body type signature (V T A...), internal loop types (I V A...)
                step = swapArguments(body, 0, 1);  // swap V <-> T`
            if (startIter == null)  startIter = MH_getIter;
            MethodHandle[]
                iterVar    = { startIter, null, MH_hasNext, retv }, // it = iterator; while (it.hasNext())
                bodyClause = { init, filterArguments(step, 0, nextVal) };  // v = body(v, t, a)
            return loop(iterVar, bodyClause);
        }
        }```</blockquote>
        """
        ...


    @staticmethod
    def tryFinally(target: "MethodHandle", cleanup: "MethodHandle") -> "MethodHandle":
        """
        Makes a method handle that adapts a `target` method handle by wrapping it in a `try-finally` block.
        Another method handle, `cleanup`, represents the functionality of the `finally` block. Any exception
        thrown during the execution of the `target` handle will be passed to the `cleanup` handle. The
        exception will be rethrown, unless `cleanup` handle throws an exception first.  The
        value returned from the `cleanup` handle's execution will be the result of the execution of the
        `try-finally` handle.
        
        The `cleanup` handle will be passed one or two additional leading arguments.
        The first is the exception thrown during the
        execution of the `target` handle, or `null` if no exception was thrown.
        The second is the result of the execution of the `target` handle, or, if it throws an exception,
        a `null`, zero, or `False` value of the required type is supplied as a placeholder.
        The second argument is not present if the `target` handle has a `void` return type.
        (Note that, except for argument type conversions, combinators represent `void` values in parameter lists
        by omitting the corresponding paradoxical arguments, not by inserting `null` or zero values.)
        
        The `target` and `cleanup` handles must have the same corresponding argument and return types, except
        that the `cleanup` handle may omit trailing arguments. Also, the `cleanup` handle must have one or
        two extra leading parameters:
        - a `Throwable`, which will carry the exception thrown by the `target` handle (if any); and
        - a parameter of the same type as the return type of both `target` and `cleanup`, which will carry
        the result from the execution of the `target` handle.
        This parameter is not present if the `target` returns `void`.
        
        
        The pseudocode for the resulting adapter looks as follows. In the code, `V` represents the result type of
        the `try/finally` construct; `A`/`a`, the types and values of arguments to the resulting
        handle consumed by the cleanup; and `B`/`b`, those of arguments to the resulting handle discarded by
        the cleanup.
        <blockquote>````V target(A..., B...);
        V cleanup(Throwable, V, A...);
        V adapter(A... a, B... b) {
          V result = (zero value for V);
          Throwable throwable = null;
          try {
            result = target(a..., b...);` catch (Throwable t) {
            throwable = t;
            throw t;
          } finally {
            result = cleanup(throwable, result, a...);
          }
          return result;
        }
        }```</blockquote>
        
        Note that the saved arguments (`a...` in the pseudocode) cannot
        be modified by execution of the target, and so are passed unchanged
        from the caller to the cleanup, if it is invoked.
        
        The target and cleanup must return the same type, even if the cleanup
        always throws.
        To create such a throwing cleanup, compose the cleanup logic
        with .throwException throwException,
        in order to create a method handle of the correct return type.
        
        Note that `tryFinally` never converts exceptions into normal returns.
        In rare cases where exceptions must be converted in that way, first wrap
        the target with .catchException(MethodHandle, Class, MethodHandle)
        to capture an outgoing exception, and then wrap with `tryFinally`.
        
        It is recommended that the first parameter type of `cleanup` be
        declared `Throwable` rather than a narrower subtype.  This ensures
        `cleanup` will always be invoked with whatever exception that
        `target` throws.  Declaring a narrower type may result in a
        `ClassCastException` being thrown by the `try-finally`
        handle if the type of the exception thrown by `target` is not
        assignable to the first parameter type of `cleanup`.  Note that
        various exception types of `VirtualMachineError`,
        `LinkageError`, and `RuntimeException` can in principle be
        thrown by almost any kind of Java code, and a finally clause that
        catches (say) only `IOException` would mask any of the others
        behind a `ClassCastException`.

        Arguments
        - target: the handle whose execution is to be wrapped in a `try` block.
        - cleanup: the handle that is invoked in the finally block.

        Returns
        - a method handle embodying the `try-finally` block composed of the two arguments.

        Raises
        - NullPointerException: if any argument is null
        - IllegalArgumentException: if `cleanup` does not accept
                 the required leading arguments, or if the method handle types do
                 not match in their return types and their
                 corresponding trailing parameters

        See
        - MethodHandles.catchException(MethodHandle, Class, MethodHandle)

        Since
        - 9
        """
        ...


    @staticmethod
    def tableSwitch(fallback: "MethodHandle", *targets: Tuple["MethodHandle", ...]) -> "MethodHandle":
        """
        Creates a table switch method handle, which can be used to switch over a set of target
        method handles, based on a given target index, called selector.
        
        For a selector value of `n`, where `n` falls in the range `[0, N)`,
        and where `N` is the number of target method handles, the table switch method
        handle will invoke the n-th target method handle from the list of target method handles.
        
        For a selector value that does not fall in the range `[0, N)`, the table switch
        method handle will invoke the given fallback method handle.
        
        All method handles passed to this method must have the same type, with the additional
        requirement that the leading parameter be of type `int`. The leading parameter
        represents the selector.
        
        Any trailing parameters present in the type will appear on the returned table switch
        method handle as well. Any arguments assigned to these parameters will be forwarded,
        together with the selector value, to the selected method handle when invoking it.

        Arguments
        - fallback: the fallback method handle that is called when the selector is not
                        within the range `[0, N)`.
        - targets: array of target method handles.

        Returns
        - the table switch method handle.

        Raises
        - NullPointerException: if `fallback`, the `targets` array, or any
                                     any of the elements of the `targets` array are
                                     `null`.
        - IllegalArgumentException: if the `targets` array is empty, if the leading
                                         parameter of the fallback handle or any of the target
                                         handles is not `int`, or if the types of
                                         the fallback handle and all of target handles are
                                         not the same.

        Unknown Tags
        - Example:
        The cases each drop the `selector` value they are given, and take an additional
        `String` argument, which is concatenated (using String.concat(String))
        to a specific constant label string for each case:
        <blockquote>````MethodHandles.Lookup lookup = MethodHandles.lookup();
        MethodHandle caseMh = lookup.findVirtual(String.class, "concat",
                MethodType.methodType(String.class, String.class));
        caseMh = MethodHandles.dropArguments(caseMh, 0, int.class);
        
        MethodHandle caseDefault = MethodHandles.insertArguments(caseMh, 1, "default: ");
        MethodHandle case0 = MethodHandles.insertArguments(caseMh, 1, "case 0: ");
        MethodHandle case1 = MethodHandles.insertArguments(caseMh, 1, "case 1: ");
        
        MethodHandle mhSwitch = MethodHandles.tableSwitch(
            caseDefault,
            case0,
            case1
        );
        
        assertEquals("default: data", (String) mhSwitch.invokeExact(-1, "data"));
        assertEquals("case 0: data", (String) mhSwitch.invokeExact(0, "data"));
        assertEquals("case 1: data", (String) mhSwitch.invokeExact(1, "data"));
        assertEquals("default: data", (String) mhSwitch.invokeExact(2, "data"));````</blockquote>
        """
        ...


    class Lookup:
        """
        A *lookup object* is a factory for creating method handles,
        when the creation requires access checking.
        Method handles do not perform
        access checks when they are called, but rather when they are created.
        Therefore, method handle access
        restrictions must be enforced when a method handle is created.
        The caller class against which those restrictions are enforced
        is known as the .lookupClass() lookup class.
        
        A lookup class which needs to create method handles will call
        MethodHandles.lookup() MethodHandles.lookup to create a factory for itself.
        When the `Lookup` factory object is created, the identity of the lookup class is
        determined, and securely stored in the `Lookup` object.
        The lookup class (or its delegates) may then use factory methods
        on the `Lookup` object to create method handles for access-checked members.
        This includes all methods, constructors, and fields which are allowed to the lookup class,
        even private ones.
        
        <h2><a id="lookups"></a>Lookup Factory Methods</h2>
        The factory methods on a `Lookup` object correspond to all major
        use cases for methods, constructors, and fields.
        Each method handle created by a factory method is the functional
        equivalent of a particular *bytecode behavior*.
        (Bytecode behaviors are described in section 5.4.3.5 of
        the Java Virtual Machine Specification.)
        Here is a summary of the correspondence between these factory methods and
        the behavior of the resulting method handles:
        <table class="striped">
        <caption style="display:none">lookup method behaviors</caption>
        <thead>
        <tr>
            <th scope="col"><a id="equiv"></a>lookup expression</th>
            <th scope="col">member</th>
            <th scope="col">bytecode behavior</th>
        </tr>
        </thead>
        <tbody>
        <tr>
            <th scope="row">java.lang.invoke.MethodHandles.Lookup.findGetter lookup.findGetter(C.class,"f",FT.class)</th>
            <td>`FT f;`</td><td>`(T) this.f;`</td>
        </tr>
        <tr>
            <th scope="row">java.lang.invoke.MethodHandles.Lookup.findStaticGetter lookup.findStaticGetter(C.class,"f",FT.class)</th>
            <td>`static``FT f;`</td><td>`(FT) C.f;`</td>
        </tr>
        <tr>
            <th scope="row">java.lang.invoke.MethodHandles.Lookup.findSetter lookup.findSetter(C.class,"f",FT.class)</th>
            <td>`FT f;`</td><td>`this.f = x;`</td>
        </tr>
        <tr>
            <th scope="row">java.lang.invoke.MethodHandles.Lookup.findStaticSetter lookup.findStaticSetter(C.class,"f",FT.class)</th>
            <td>`static``FT f;`</td><td>`C.f = arg;`</td>
        </tr>
        <tr>
            <th scope="row">java.lang.invoke.MethodHandles.Lookup.findVirtual lookup.findVirtual(C.class,"m",MT)</th>
            <td>`T m(A*);`</td><td>`(T) this.m(arg*);`</td>
        </tr>
        <tr>
            <th scope="row">java.lang.invoke.MethodHandles.Lookup.findStatic lookup.findStatic(C.class,"m",MT)</th>
            <td>`static``T m(A*);`</td><td>`(T) C.m(arg*);`</td>
        </tr>
        <tr>
            <th scope="row">java.lang.invoke.MethodHandles.Lookup.findSpecial lookup.findSpecial(C.class,"m",MT,this.class)</th>
            <td>`T m(A*);`</td><td>`(T) super.m(arg*);`</td>
        </tr>
        <tr>
            <th scope="row">java.lang.invoke.MethodHandles.Lookup.findConstructor lookup.findConstructor(C.class,MT)</th>
            <td>`C(A*);`</td><td>`new C(arg*);`</td>
        </tr>
        <tr>
            <th scope="row">java.lang.invoke.MethodHandles.Lookup.unreflectGetter lookup.unreflectGetter(aField)</th>
            <td>(`static`)?`FT f;`</td><td>`(FT) aField.get(thisOrNull);`</td>
        </tr>
        <tr>
            <th scope="row">java.lang.invoke.MethodHandles.Lookup.unreflectSetter lookup.unreflectSetter(aField)</th>
            <td>(`static`)?`FT f;`</td><td>`aField.set(thisOrNull, arg);`</td>
        </tr>
        <tr>
            <th scope="row">java.lang.invoke.MethodHandles.Lookup.unreflect lookup.unreflect(aMethod)</th>
            <td>(`static`)?`T m(A*);`</td><td>`(T) aMethod.invoke(thisOrNull, arg*);`</td>
        </tr>
        <tr>
            <th scope="row">java.lang.invoke.MethodHandles.Lookup.unreflectConstructor lookup.unreflectConstructor(aConstructor)</th>
            <td>`C(A*);`</td><td>`(C) aConstructor.newInstance(arg*);`</td>
        </tr>
        <tr>
            <th scope="row">java.lang.invoke.MethodHandles.Lookup.unreflectSpecial lookup.unreflectSpecial(aMethod,this.class)</th>
            <td>`T m(A*);`</td><td>`(T) super.m(arg*);`</td>
        </tr>
        <tr>
            <th scope="row">java.lang.invoke.MethodHandles.Lookup.findClass lookup.findClass("C")</th>
            <td>`class C { ...`}</td><td>`C.class;`</td>
        </tr>
        </tbody>
        </table>
        
        Here, the type `C` is the class or interface being searched for a member,
        documented as a parameter named `refc` in the lookup methods.
        The method type `MT` is composed from the return type `T`
        and the sequence of argument types `A*`.
        The constructor also has a sequence of argument types `A*` and
        is deemed to return the newly-created object of type `C`.
        Both `MT` and the field type `FT` are documented as a parameter named `type`.
        The formal parameter `this` stands for the self-reference of type `C`;
        if it is present, it is always the leading argument to the method handle invocation.
        (In the case of some `protected` members, `this` may be
        restricted in type to the lookup class; see below.)
        The name `arg` stands for all the other method handle arguments.
        In the code examples for the Core Reflection API, the name `thisOrNull`
        stands for a null reference if the accessed method or field is static,
        and `this` otherwise.
        The names `aMethod`, `aField`, and `aConstructor` stand
        for reflective objects corresponding to the given members declared in type `C`.
        
        The bytecode behavior for a `findClass` operation is a load of a constant class,
        as if by `ldc CONSTANT_Class`.
        The behavior is represented, not as a method handle, but directly as a `Class` constant.
        
        In cases where the given member is of variable arity (i.e., a method or constructor)
        the returned method handle will also be of MethodHandle.asVarargsCollector variable arity.
        In all other cases, the returned method handle will be of fixed arity.
        <p style="font-size:smaller;">
        *Discussion:*
        The equivalence between looked-up method handles and underlying
        class members and bytecode behaviors
        can break down in a few ways:
        <ul style="font-size:smaller;">
        - If `C` is not symbolically accessible from the lookup class's loader,
        the lookup can still succeed, even when there is no equivalent
        Java expression or bytecoded constant.
        - Likewise, if `T` or `MT`
        is not symbolically accessible from the lookup class's loader,
        the lookup can still succeed.
        For example, lookups for `MethodHandle.invokeExact` and
        `MethodHandle.invoke` will always succeed, regardless of requested type.
        - If there is a security manager installed, it can forbid the lookup
        on various grounds (<a href="MethodHandles.Lookup.html#secmgr">see below</a>).
        By contrast, the `ldc` instruction on a `CONSTANT_MethodHandle`
        constant is not subject to security manager checks.
        - If the looked-up method has a
        <a href="MethodHandle.html#maxarity">very large arity</a>,
        the method handle creation may fail with an
        `IllegalArgumentException`, due to the method handle type having
        <a href="MethodHandle.html#maxarity">too many parameters.</a>
        
        
        <h2><a id="access"></a>Access checking</h2>
        Access checks are applied in the factory methods of `Lookup`,
        when a method handle is created.
        This is a key difference from the Core Reflection API, since
        java.lang.reflect.Method.invoke java.lang.reflect.Method.invoke
        performs access checking against every caller, on every call.
        
        All access checks start from a `Lookup` object, which
        compares its recorded lookup class against all requests to
        create method handles.
        A single `Lookup` object can be used to create any number
        of access-checked method handles, all checked against a single
        lookup class.
        
        A `Lookup` object can be shared with other trusted code,
        such as a metaobject protocol.
        A shared `Lookup` object delegates the capability
        to create method handles on private members of the lookup class.
        Even if privileged code uses the `Lookup` object,
        the access checking is confined to the privileges of the
        original lookup class.
        
        A lookup can fail, because
        the containing class is not accessible to the lookup class, or
        because the desired class member is missing, or because the
        desired class member is not accessible to the lookup class, or
        because the lookup object is not trusted enough to access the member.
        In the case of a field setter function on a `final` field,
        finality enforcement is treated as a kind of access control,
        and the lookup will fail, except in special cases of
        Lookup.unreflectSetter Lookup.unreflectSetter.
        In any of these cases, a `ReflectiveOperationException` will be
        thrown from the attempted lookup.  The exact class will be one of
        the following:
        
        - NoSuchMethodException &mdash; if a method is requested but does not exist
        - NoSuchFieldException &mdash; if a field is requested but does not exist
        - IllegalAccessException &mdash; if the member exists but an access check fails
        
        
        In general, the conditions under which a method handle may be
        looked up for a method `M` are no more restrictive than the conditions
        under which the lookup class could have compiled, verified, and resolved a call to `M`.
        Where the JVM would raise exceptions like `NoSuchMethodError`,
        a method handle lookup will generally raise a corresponding
        checked exception, such as `NoSuchMethodException`.
        And the effect of invoking the method handle resulting from the lookup
        is <a href="MethodHandles.Lookup.html#equiv">exactly equivalent</a>
        to executing the compiled, verified, and resolved call to `M`.
        The same point is True of fields and constructors.
        <p style="font-size:smaller;">
        *Discussion:*
        Access checks only apply to named and reflected methods,
        constructors, and fields.
        Other method handle creation methods, such as
        MethodHandle.asType MethodHandle.asType,
        do not require any access checks, and are used
        independently of any `Lookup` object.
        
        If the desired member is `protected`, the usual JVM rules apply,
        including the requirement that the lookup class must either be in the
        same package as the desired member, or must inherit that member.
        (See the Java Virtual Machine Specification, sections 4.9.2, 5.4.3.5, and 6.4.)
        In addition, if the desired member is a non-static field or method
        in a different package, the resulting method handle may only be applied
        to objects of the lookup class or one of its subclasses.
        This requirement is enforced by narrowing the type of the leading
        `this` parameter from `C`
        (which will necessarily be a superclass of the lookup class)
        to the lookup class itself.
        
        The JVM imposes a similar requirement on `invokespecial` instruction,
        that the receiver argument must match both the resolved method *and*
        the current class.  Again, this requirement is enforced by narrowing the
        type of the leading parameter to the resulting method handle.
        (See the Java Virtual Machine Specification, section 4.10.1.9.)
        
        The JVM represents constructors and static initializer blocks as internal methods
        with special names (`"<init>"` and `"<clinit>"`).
        The internal syntax of invocation instructions allows them to refer to such internal
        methods as if they were normal methods, but the JVM bytecode verifier rejects them.
        A lookup of such an internal method will produce a `NoSuchMethodException`.
        
        If the relationship between nested types is expressed directly through the
        `NestHost` and `NestMembers` attributes
        (see the Java Virtual Machine Specification, sections 4.7.28 and 4.7.29),
        then the associated `Lookup` object provides direct access to
        the lookup class and all of its nestmates
        (see java.lang.Class.getNestHost Class.getNestHost).
        Otherwise, access between nested classes is obtained by the Java compiler creating
        a wrapper method to access a private method of another class in the same nest.
        For example, a nested class `C.D`
        can access private members within other related classes such as
        `C`, `C.D.E`, or `C.B`,
        but the Java compiler may need to generate wrapper methods in
        those related classes.  In such cases, a `Lookup` object on
        `C.E` would be unable to access those private members.
        A workaround for this limitation is the Lookup.in Lookup.in method,
        which can transform a lookup on `C.E` into one on any of those other
        classes, without special elevation of privilege.
        
        The accesses permitted to a given lookup object may be limited,
        according to its set of .lookupModes lookupModes,
        to a subset of members normally accessible to the lookup class.
        For example, the MethodHandles.publicLookup publicLookup
        method produces a lookup object which is only allowed to access
        public members in public classes of exported packages.
        The caller sensitive method MethodHandles.lookup lookup
        produces a lookup object with full capabilities relative to
        its caller class, to emulate all supported bytecode behaviors.
        Also, the Lookup.in Lookup.in method may produce a lookup object
        with fewer access modes than the original lookup object.
        
        <p style="font-size:smaller;">
        <a id="privacc"></a>
        *Discussion of private and module access:*
        We say that a lookup has *private access*
        if its .lookupModes lookup modes
        include the possibility of accessing `private` members
        (which includes the private members of nestmates).
        As documented in the relevant methods elsewhere,
        only lookups with private access possess the following capabilities:
        <ul style="font-size:smaller;">
        - access private fields, methods, and constructors of the lookup class and its nestmates
        - create method handles which Lookup.findSpecial emulate invokespecial instructions
        - avoid <a href="MethodHandles.Lookup.html#secmgr">package access checks</a>
            for classes accessible to the lookup class
        - create Lookup.in delegated lookup objects which have private access to other classes
            within the same package member
        
        <p style="font-size:smaller;">
        Similarly, a lookup with module access ensures that the original lookup creator was
        a member in the same module as the lookup class.
        <p style="font-size:smaller;">
        Private and module access are independently determined modes; a lookup may have
        either or both or neither.  A lookup which possesses both access modes is said to
        possess .hasFullPrivilegeAccess() full privilege access.
        <p style="font-size:smaller;">
        A lookup with *original access* ensures that this lookup is created by
        the original lookup class and the bootstrap method invoked by the VM.
        Such a lookup with original access also has private and module access
        which has the following additional capability:
        <ul style="font-size:smaller;">
        - create method handles which invoke <a href="MethodHandles.Lookup.html#callsens">caller sensitive</a> methods,
            such as `Class.forName`
        - obtain the MethodHandles.classData(Lookup, String, Class)
        class data associated with the lookup class
        
        <p style="font-size:smaller;">
        Each of these permissions is a consequence of the fact that a lookup object
        with private access can be securely traced back to an originating class,
        whose <a href="MethodHandles.Lookup.html#equiv">bytecode behaviors</a> and Java language access permissions
        can be reliably determined and emulated by method handles.
        
        <h2><a id="cross-module-lookup"></a>Cross-module lookups</h2>
        When a lookup class in one module `M1` accesses a class in another module
        `M2`, extra access checking is performed beyond the access mode bits.
        A `Lookup` with .PUBLIC mode and a lookup class in `M1`
        can access public types in `M2` when `M2` is readable to `M1`
        and when the type is in a package of `M2` that is exported to
        at least `M1`.
        
        A `Lookup` on `C` can also *teleport* to a target class
        via .in(Class) Lookup.in and MethodHandles.privateLookupIn(Class, Lookup)
        MethodHandles.privateLookupIn methods.
        Teleporting across modules will always record the original lookup class as
        the *.previousLookupClass() previous lookup class*
        and drops Lookup.MODULE MODULE access.
        If the target class is in the same module as the lookup class `C`,
        then the target class becomes the new lookup class
        and there is no change to the previous lookup class.
        If the target class is in a different module from `M1` (`C`'s module),
        `C` becomes the new previous lookup class
        and the target class becomes the new lookup class.
        In that case, if there was already a previous lookup class in `M0`,
        and it differs from `M1` and `M2`, then the resulting lookup
        drops all privileges.
        For example,
        <blockquote>```
        `Lookup lookup = MethodHandles.lookup();   // in class C
        Lookup lookup2 = lookup.in(D.class);
        MethodHandle mh = lookup2.findStatic(E.class, "m", MT);````</blockquote>
        
        The .lookup() factory method produces a `Lookup` object
        with `null` previous lookup class.
        Lookup.in lookup.in(D.class) transforms the `lookup` on class `C`
        to class `D` without elevation of privileges.
        If `C` and `D` are in the same module,
        `lookup2` records `D` as the new lookup class and keeps the
        same previous lookup class as the original `lookup`, or
        `null` if not present.
        
        When a `Lookup` teleports from a class
        in one nest to another nest, `PRIVATE` access is dropped.
        When a `Lookup` teleports from a class in one package to
        another package, `PACKAGE` access is dropped.
        When a `Lookup` teleports from a class in one module to another module,
        `MODULE` access is dropped.
        Teleporting across modules drops the ability to access non-exported classes
        in both the module of the new lookup class and the module of the old lookup class
        and the resulting `Lookup` remains only `PUBLIC` access.
        A `Lookup` can teleport back and forth to a class in the module of
        the lookup class and the module of the previous class lookup.
        Teleporting across modules can only decrease access but cannot increase it.
        Teleporting to some third module drops all accesses.
        
        In the above example, if `C` and `D` are in different modules,
        `lookup2` records `D` as its lookup class and
        `C` as its previous lookup class and `lookup2` has only
        `PUBLIC` access. `lookup2` can teleport to other class in
        `C`'s module and `D`'s module.
        If class `E` is in a third module, `lookup2.in(E.class)` creates
        a `Lookup` on `E` with no access and `lookup2`'s lookup
        class `D` is recorded as its previous lookup class.
        
        Teleporting across modules restricts access to the public types that
        both the lookup class and the previous lookup class can equally access
        (see below).
        
        MethodHandles.privateLookupIn(Class, Lookup) MethodHandles.privateLookupIn(T.class, lookup)
        can be used to teleport a `lookup` from class `C` to class `T`
        and create a new `Lookup` with <a href="#privacc">private access</a>
        if the lookup class is allowed to do *deep reflection* on `T`.
        The `lookup` must have .MODULE and .PRIVATE access
        to call `privateLookupIn`.
        A `lookup` on `C` in module `M1` is allowed to do deep reflection
        on all classes in `M1`.  If `T` is in `M1`, `privateLookupIn`
        produces a new `Lookup` on `T` with full capabilities.
        A `lookup` on `C` is also allowed
        to do deep reflection on `T` in another module `M2` if
        `M1` reads `M2` and `M2` Module.isOpen(String,Module) opens
        the package containing `T` to at least `M1`.
        `T` becomes the new lookup class and `C` becomes the new previous
        lookup class and `MODULE` access is dropped from the resulting `Lookup`.
        The resulting `Lookup` can be used to do member lookup or teleport
        to another lookup class by calling .in Lookup::in.  But
        it cannot be used to obtain another private `Lookup` by calling
        MethodHandles.privateLookupIn(Class, Lookup) privateLookupIn
        because it has no `MODULE` access.
        
        <h2><a id="module-access-check"></a>Cross-module access checks</h2>
        
        A `Lookup` with .PUBLIC or with .UNCONDITIONAL mode
        allows cross-module access. The access checking is performed with respect
        to both the lookup class and the previous lookup class if present.
        
        A `Lookup` with .UNCONDITIONAL mode can access public type
        in all modules when the type is in a package that is Module.isExported(String)
        exported unconditionally.
        
        If a `Lookup` on `LC` in `M1` has no previous lookup class,
        the lookup with .PUBLIC mode can access all public types in modules
        that are readable to `M1` and the type is in a package that is exported
        at least to `M1`.
        
        If a `Lookup` on `LC` in `M1` has a previous lookup class
        `PLC` on `M0`, the lookup with .PUBLIC mode can access
        the intersection of all public types that are accessible to `M1`
        with all public types that are accessible to `M0`. `M0`
        reads `M1` and hence the set of accessible types includes:
        
        <table class="striped">
        <caption style="display:none">
        Public types in the following packages are accessible to the
        lookup class and the previous lookup class.
        </caption>
        <thead>
        <tr>
        <th scope="col">Equally accessible types to `M0` and `M1`</th>
        </tr>
        </thead>
        <tbody>
        <tr>
        <th scope="row" style="text-align:left">unconditional-exported packages from `M1`</th>
        </tr>
        <tr>
        <th scope="row" style="text-align:left">unconditional-exported packages from `M0` if `M1` reads `M0`</th>
        </tr>
        <tr>
        <th scope="row" style="text-align:left">unconditional-exported packages from a third module `M2`
        if both `M0` and `M1` read `M2`</th>
        </tr>
        <tr>
        <th scope="row" style="text-align:left">qualified-exported packages from `M1` to `M0`</th>
        </tr>
        <tr>
        <th scope="row" style="text-align:left">qualified-exported packages from `M0` to `M1`
        if `M1` reads `M0`</th>
        </tr>
        <tr>
        <th scope="row" style="text-align:left">qualified-exported packages from a third module `M2` to
        both `M0` and `M1` if both `M0` and `M1` read `M2`</th>
        </tr>
        </tbody>
        </table>
        
        <h2><a id="access-modes"></a>Access modes</h2>
        
        The table below shows the access modes of a `Lookup` produced by
        any of the following factory or transformation methods:
        
        - .lookup() MethodHandles::lookup
        - .publicLookup() MethodHandles::publicLookup
        - .privateLookupIn(Class, Lookup) MethodHandles::privateLookupIn
        - Lookup.in Lookup::in
        - Lookup.dropLookupMode(int) Lookup::dropLookupMode
        
        
        <table class="striped">
        <caption style="display:none">
        Access mode summary
        </caption>
        <thead>
        <tr>
        <th scope="col">Lookup object</th>
        <th style="text-align:center">original</th>
        <th style="text-align:center">protected</th>
        <th style="text-align:center">private</th>
        <th style="text-align:center">package</th>
        <th style="text-align:center">module</th>
        <th style="text-align:center">public</th>
        </tr>
        </thead>
        <tbody>
        <tr>
        <th scope="row" style="text-align:left">`CL = MethodHandles.lookup()` in `C`</th>
        <td style="text-align:center">ORI</td>
        <td style="text-align:center">PRO</td>
        <td style="text-align:center">PRI</td>
        <td style="text-align:center">PAC</td>
        <td style="text-align:center">MOD</td>
        <td style="text-align:center">1R</td>
        </tr>
        <tr>
        <th scope="row" style="text-align:left">`CL.in(C1)` same package</th>
        <td></td>
        <td></td>
        <td></td>
        <td style="text-align:center">PAC</td>
        <td style="text-align:center">MOD</td>
        <td style="text-align:center">1R</td>
        </tr>
        <tr>
        <th scope="row" style="text-align:left">`CL.in(C1)` same module</th>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td style="text-align:center">MOD</td>
        <td style="text-align:center">1R</td>
        </tr>
        <tr>
        <th scope="row" style="text-align:left">`CL.in(D)` different module</th>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td style="text-align:center">2R</td>
        </tr>
        <tr>
        <td>`CL.in(D).in(C)` hop back to module</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td style="text-align:center">2R</td>
        </tr>
        <tr>
        <td>`PRI1 = privateLookupIn(C1,CL)`</td>
        <td></td>
        <td style="text-align:center">PRO</td>
        <td style="text-align:center">PRI</td>
        <td style="text-align:center">PAC</td>
        <td style="text-align:center">MOD</td>
        <td style="text-align:center">1R</td>
        </tr>
        <tr>
        <td>`PRI1a = privateLookupIn(C,PRI1)`</td>
        <td></td>
        <td style="text-align:center">PRO</td>
        <td style="text-align:center">PRI</td>
        <td style="text-align:center">PAC</td>
        <td style="text-align:center">MOD</td>
        <td style="text-align:center">1R</td>
        </tr>
        <tr>
        <td>`PRI1.in(C1)` same package</td>
        <td></td>
        <td></td>
        <td></td>
        <td style="text-align:center">PAC</td>
        <td style="text-align:center">MOD</td>
        <td style="text-align:center">1R</td>
        </tr>
        <tr>
        <td>`PRI1.in(C1)` different package</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td style="text-align:center">MOD</td>
        <td style="text-align:center">1R</td>
        </tr>
        <tr>
        <td>`PRI1.in(D)` different module</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td style="text-align:center">2R</td>
        </tr>
        <tr>
        <td>`PRI1.dropLookupMode(PROTECTED)`</td>
        <td></td>
        <td></td>
        <td style="text-align:center">PRI</td>
        <td style="text-align:center">PAC</td>
        <td style="text-align:center">MOD</td>
        <td style="text-align:center">1R</td>
        </tr>
        <tr>
        <td>`PRI1.dropLookupMode(PRIVATE)`</td>
        <td></td>
        <td></td>
        <td></td>
        <td style="text-align:center">PAC</td>
        <td style="text-align:center">MOD</td>
        <td style="text-align:center">1R</td>
        </tr>
        <tr>
        <td>`PRI1.dropLookupMode(PACKAGE)`</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td style="text-align:center">MOD</td>
        <td style="text-align:center">1R</td>
        </tr>
        <tr>
        <td>`PRI1.dropLookupMode(MODULE)`</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td style="text-align:center">1R</td>
        </tr>
        <tr>
        <td>`PRI1.dropLookupMode(PUBLIC)`</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td style="text-align:center">none</td>
        <tr>
        <td>`PRI2 = privateLookupIn(D,CL)`</td>
        <td></td>
        <td style="text-align:center">PRO</td>
        <td style="text-align:center">PRI</td>
        <td style="text-align:center">PAC</td>
        <td></td>
        <td style="text-align:center">2R</td>
        </tr>
        <tr>
        <td>`privateLookupIn(D,PRI1)`</td>
        <td></td>
        <td style="text-align:center">PRO</td>
        <td style="text-align:center">PRI</td>
        <td style="text-align:center">PAC</td>
        <td></td>
        <td style="text-align:center">2R</td>
        </tr>
        <tr>
        <td>`privateLookupIn(C,PRI2)` fails</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td style="text-align:center">IAE</td>
        </tr>
        <tr>
        <td>`PRI2.in(D2)` same package</td>
        <td></td>
        <td></td>
        <td></td>
        <td style="text-align:center">PAC</td>
        <td></td>
        <td style="text-align:center">2R</td>
        </tr>
        <tr>
        <td>`PRI2.in(D2)` different package</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td style="text-align:center">2R</td>
        </tr>
        <tr>
        <td>`PRI2.in(C1)` hop back to module</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td style="text-align:center">2R</td>
        </tr>
        <tr>
        <td>`PRI2.in(E)` hop to third module</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td style="text-align:center">none</td>
        </tr>
        <tr>
        <td>`PRI2.dropLookupMode(PROTECTED)`</td>
        <td></td>
        <td></td>
        <td style="text-align:center">PRI</td>
        <td style="text-align:center">PAC</td>
        <td></td>
        <td style="text-align:center">2R</td>
        </tr>
        <tr>
        <td>`PRI2.dropLookupMode(PRIVATE)`</td>
        <td></td>
        <td></td>
        <td></td>
        <td style="text-align:center">PAC</td>
        <td></td>
        <td style="text-align:center">2R</td>
        </tr>
        <tr>
        <td>`PRI2.dropLookupMode(PACKAGE)`</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td style="text-align:center">2R</td>
        </tr>
        <tr>
        <td>`PRI2.dropLookupMode(MODULE)`</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td style="text-align:center">2R</td>
        </tr>
        <tr>
        <td>`PRI2.dropLookupMode(PUBLIC)`</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td style="text-align:center">none</td>
        </tr>
        <tr>
        <td>`CL.dropLookupMode(PROTECTED)`</td>
        <td></td>
        <td></td>
        <td style="text-align:center">PRI</td>
        <td style="text-align:center">PAC</td>
        <td style="text-align:center">MOD</td>
        <td style="text-align:center">1R</td>
        </tr>
        <tr>
        <td>`CL.dropLookupMode(PRIVATE)`</td>
        <td></td>
        <td></td>
        <td></td>
        <td style="text-align:center">PAC</td>
        <td style="text-align:center">MOD</td>
        <td style="text-align:center">1R</td>
        </tr>
        <tr>
        <td>`CL.dropLookupMode(PACKAGE)`</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td style="text-align:center">MOD</td>
        <td style="text-align:center">1R</td>
        </tr>
        <tr>
        <td>`CL.dropLookupMode(MODULE)`</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td style="text-align:center">1R</td>
        </tr>
        <tr>
        <td>`CL.dropLookupMode(PUBLIC)`</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td style="text-align:center">none</td>
        </tr>
        <tr>
        <td>`PUB = publicLookup()`</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td style="text-align:center">U</td>
        </tr>
        <tr>
        <td>`PUB.in(D)` different module</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td style="text-align:center">U</td>
        </tr>
        <tr>
        <td>`PUB.in(D).in(E)` third module</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td style="text-align:center">U</td>
        </tr>
        <tr>
        <td>`PUB.dropLookupMode(UNCONDITIONAL)`</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td style="text-align:center">none</td>
        </tr>
        <tr>
        <td>`privateLookupIn(C1,PUB)` fails</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td style="text-align:center">IAE</td>
        </tr>
        <tr>
        <td>`ANY.in(X)`, for inaccessible `X`</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td style="text-align:center">none</td>
        </tr>
        </tbody>
        </table>
        
        
        Notes:
        
        - Class `C` and class `C1` are in module `M1`,
            but `D` and `D2` are in module `M2`, and `E`
            is in module `M3`. `X` stands for class which is inaccessible
            to the lookup. `ANY` stands for any of the example lookups.
        - `ORI` indicates .ORIGINAL bit set,
            `PRO` indicates .PROTECTED bit set,
            `PRI` indicates .PRIVATE bit set,
            `PAC` indicates .PACKAGE bit set,
            `MOD` indicates .MODULE bit set,
            `1R` and `2R` indicate .PUBLIC bit set,
            `U` indicates .UNCONDITIONAL bit set,
            `IAE` indicates `IllegalAccessException` thrown.
        - Public access comes in three kinds:
        
        - unconditional (`U`): the lookup assumes readability.
            The lookup has `null` previous lookup class.
        - one-module-reads (`1R`): the module access checking is
            performed with respect to the lookup class.  The lookup has `null`
            previous lookup class.
        - two-module-reads (`2R`): the module access checking is
            performed with respect to the lookup class and the previous lookup class.
            The lookup has a non-null previous lookup class which is in a
            different module from the current lookup class.
        
        - Any attempt to reach a third module loses all access.
        - If a target class `X` is not accessible to `Lookup::in`
        all access modes are dropped.
        
        
        <h2><a id="secmgr"></a>Security manager interactions</h2>
        Although bytecode instructions can only refer to classes in
        a related class loader, this API can search for methods in any
        class, as long as a reference to its `Class` object is
        available.  Such cross-loader references are also possible with the
        Core Reflection API, and are impossible to bytecode instructions
        such as `invokestatic` or `getfield`.
        There is a java.lang.SecurityManager security manager API
        to allow applications to check such cross-loader references.
        These checks apply to both the `MethodHandles.Lookup` API
        and the Core Reflection API
        (as found on java.lang.Class Class).
        
        If a security manager is present, member and class lookups are subject to
        additional checks.
        From one to three calls are made to the security manager.
        Any of these calls can refuse access by throwing a
        java.lang.SecurityException SecurityException.
        Define `smgr` as the security manager,
        `lookc` as the lookup class of the current lookup object,
        `refc` as the containing class in which the member
        is being sought, and `defc` as the class in which the
        member is actually defined.
        (If a class or other type is being accessed,
        the `refc` and `defc` values are the class itself.)
        The value `lookc` is defined as *not present*
        if the current lookup object does not have
        .hasFullPrivilegeAccess() full privilege access.
        The calls are made according to the following rules:
        
        - **Step 1:**
            If `lookc` is not present, or if its class loader is not
            the same as or an ancestor of the class loader of `refc`,
            then SecurityManager.checkPackageAccess
            smgr.checkPackageAccess(refcPkg) is called,
            where `refcPkg` is the package of `refc`.
        - **Step 2a:**
            If the retrieved member is not public and
            `lookc` is not present, then
            SecurityManager.checkPermission smgr.checkPermission
            with `RuntimePermission("accessDeclaredMembers")` is called.
        - **Step 2b:**
            If the retrieved class has a `null` class loader,
            and `lookc` is not present, then
            SecurityManager.checkPermission smgr.checkPermission
            with `RuntimePermission("getClassLoader")` is called.
        - **Step 3:**
            If the retrieved member is not public,
            and if `lookc` is not present,
            and if `defc` and `refc` are different,
            then SecurityManager.checkPackageAccess
            smgr.checkPackageAccess(defcPkg) is called,
            where `defcPkg` is the package of `defc`.
        
        Security checks are performed after other access checks have passed.
        Therefore, the above rules presuppose a member or class that is public,
        or else that is being accessed from a lookup class that has
        rights to access the member or class.
        
        If a security manager is present and the current lookup object does not have
        .hasFullPrivilegeAccess() full privilege access, then
        .defineClass(byte[]) defineClass,
        .defineHiddenClass(byte[], boolean, ClassOption...) defineHiddenClass,
        .defineHiddenClassWithClassData(byte[], Object, boolean, ClassOption...)
        defineHiddenClassWithClassData
        calls SecurityManager.checkPermission smgr.checkPermission
        with `RuntimePermission("defineClass")`.
        
        <h2><a id="callsens"></a>Caller sensitive methods</h2>
        A small number of Java methods have a special property called caller sensitivity.
        A *caller-sensitive* method can behave differently depending on the
        identity of its immediate caller.
        
        If a method handle for a caller-sensitive method is requested,
        the general rules for <a href="MethodHandles.Lookup.html#equiv">bytecode behaviors</a> apply,
        but they take account of the lookup class in a special way.
        The resulting method handle behaves as if it were called
        from an instruction contained in the lookup class,
        so that the caller-sensitive method detects the lookup class.
        (By contrast, the invoker of the method handle is disregarded.)
        Thus, in the case of caller-sensitive methods,
        different lookup classes may give rise to
        differently behaving method handles.
        
        In cases where the lookup object is
        MethodHandles.publicLookup() publicLookup(),
        or some other lookup object without the
        .ORIGINAL original access,
        the lookup class is disregarded.
        In such cases, no caller-sensitive method handle can be created,
        access is forbidden, and the lookup fails with an
        `IllegalAccessException`.
        <p style="font-size:smaller;">
        *Discussion:*
        For example, the caller-sensitive method
        java.lang.Class.forName(String) Class.forName(x)
        can return varying classes or throw varying exceptions,
        depending on the class loader of the class that calls it.
        A public lookup of `Class.forName` will fail, because
        there is no reasonable way to determine its bytecode behavior.
        <p style="font-size:smaller;">
        If an application caches method handles for broad sharing,
        it should use `publicLookup()` to create them.
        If there is a lookup of `Class.forName`, it will fail,
        and the application must take appropriate action in that case.
        It may be that a later lookup, perhaps during the invocation of a
        bootstrap method, can incorporate the specific identity
        of the caller, making the method accessible.
        <p style="font-size:smaller;">
        The function `MethodHandles.lookup` is caller sensitive
        so that there can be a secure foundation for lookups.
        Nearly all other methods in the JSR 292 API rely on lookup
        objects to check access requests.

        Unknown Tags
        - 9
        """

        PUBLIC = Modifier.PUBLIC
        """
        A single-bit mask representing `public` access,
         which may contribute to the result of .lookupModes lookupModes.
         The value, `0x01`, happens to be the same as the value of the
         `public` java.lang.reflect.Modifier.PUBLIC modifier bit.
         
         A `Lookup` with this lookup mode performs cross-module access check
         with respect to the .lookupClass() lookup class and
         .previousLookupClass() previous lookup class if present.
        """
        PRIVATE = Modifier.PRIVATE
        """
        A single-bit mask representing `private` access,
         which may contribute to the result of .lookupModes lookupModes.
         The value, `0x02`, happens to be the same as the value of the
         `private` java.lang.reflect.Modifier.PRIVATE modifier bit.
        """
        PROTECTED = Modifier.PROTECTED
        """
        A single-bit mask representing `protected` access,
         which may contribute to the result of .lookupModes lookupModes.
         The value, `0x04`, happens to be the same as the value of the
         `protected` java.lang.reflect.Modifier.PROTECTED modifier bit.
        """
        PACKAGE = Modifier.STATIC
        """
        A single-bit mask representing `package` access (default access),
         which may contribute to the result of .lookupModes lookupModes.
         The value is `0x08`, which does not correspond meaningfully to
         any particular java.lang.reflect.Modifier modifier bit.
        """
        MODULE = PACKAGE << 1
        """
        A single-bit mask representing `module` access,
         which may contribute to the result of .lookupModes lookupModes.
         The value is `0x10`, which does not correspond meaningfully to
         any particular java.lang.reflect.Modifier modifier bit.
         In conjunction with the `PUBLIC` modifier bit, a `Lookup`
         with this lookup mode can access all public types in the module of the
         lookup class and public types in packages exported by other modules
         to the module of the lookup class.
         
         If this lookup mode is set, the .previousLookupClass()
         previous lookup class is always `null`.

        Since
        - 9
        """
        UNCONDITIONAL = PACKAGE << 2
        """
        A single-bit mask representing `unconditional` access
         which may contribute to the result of .lookupModes lookupModes.
         The value is `0x20`, which does not correspond meaningfully to
         any particular java.lang.reflect.Modifier modifier bit.
         A `Lookup` with this lookup mode assumes java.lang.Module.canRead(java.lang.Module) readability.
         This lookup mode can access all public members of public types
         of all modules when the type is in a package that is java.lang.Module.isExported(String) exported unconditionally.
        
         
         If this lookup mode is set, the .previousLookupClass()
         previous lookup class is always `null`.

        See
        - .publicLookup()

        Since
        - 9
        """
        ORIGINAL = PACKAGE << 3
        """
        A single-bit mask representing `original` access
         which may contribute to the result of .lookupModes lookupModes.
         The value is `0x40`, which does not correspond meaningfully to
         any particular java.lang.reflect.Modifier modifier bit.
        
         
         If this lookup mode is set, the `Lookup` object must be
         created by the original lookup class by calling
         MethodHandles.lookup() method or by a bootstrap method
         invoked by the VM.  The `Lookup` object with this lookup
         mode has .hasFullPrivilegeAccess() full privilege access.

        Since
        - 16
        """


        def lookupClass(self) -> type[Any]:
            """
            Tells which class is performing the lookup.  It is this class against
             which checks are performed for visibility and access permissions.
             
             If this lookup object has a .previousLookupClass() previous lookup class,
             access checks are performed against both the lookup class and the previous lookup class.
             
             The class implies a maximum level of access permission,
             but the permissions may be additionally limited by the bitmask
             .lookupModes lookupModes, which controls whether non-public members
             can be accessed.

            Returns
            - the lookup class, on behalf of which this lookup object finds members

            See
            - <a href=".cross-module-lookup">Cross-module lookups</a>
            """
            ...


        def previousLookupClass(self) -> type[Any]:
            """
            Reports a lookup class in another module that this lookup object
            was previously teleported from, or `null`.
            
            A `Lookup` object produced by the factory methods, such as the
            .lookup() lookup() and .publicLookup() publicLookup() method,
            has `null` previous lookup class.
            A `Lookup` object has a non-null previous lookup class
            when this lookup was teleported from an old lookup class
            in one module to a new lookup class in another module.

            Returns
            - the lookup class in another module that this lookup object was
                    previously teleported from, or `null`

            See
            - <a href=".cross-module-lookup">Cross-module lookups</a>

            Since
            - 14
            """
            ...


        def lookupModes(self) -> int:
            """
            Tells which access-protection classes of members this lookup object can produce.
             The result is a bit-mask of the bits
             .PUBLIC PUBLIC (0x01),
             .PRIVATE PRIVATE (0x02),
             .PROTECTED PROTECTED (0x04),
             .PACKAGE PACKAGE (0x08),
             .MODULE MODULE (0x10),
             .UNCONDITIONAL UNCONDITIONAL (0x20),
             and .ORIGINAL ORIGINAL (0x40).
             
             A freshly-created lookup object
             on the java.lang.invoke.MethodHandles.lookup() caller's class has
             all possible bits set, except `UNCONDITIONAL`.
             A lookup object on a new lookup class
             java.lang.invoke.MethodHandles.Lookup.in created from a previous lookup object
             may have some mode bits set to zero.
             Mode bits can also be
             java.lang.invoke.MethodHandles.Lookup.dropLookupMode directly cleared.
             Once cleared, mode bits cannot be restored from the downgraded lookup object.
             The purpose of this is to restrict access via the new lookup object,
             so that it can access only names which can be reached by the original
             lookup object, and also by the new lookup class.

            Returns
            - the lookup modes, which limit the kinds of access performed by this lookup object

            See
            - .dropLookupMode

            Unknown Tags
            - 9
            """
            ...


        def in(self, requestedLookupClass: type[Any]) -> "Lookup":
            """
            Creates a lookup on the specified new lookup class.
            The resulting object will report the specified
            class as its own .lookupClass() lookupClass.
            
            
            However, the resulting `Lookup` object is guaranteed
            to have no more access capabilities than the original.
            In particular, access capabilities can be lost as follows:
            - If the new lookup class is different from the old lookup class,
            i.e. .ORIGINAL ORIGINAL access is lost.
            - If the new lookup class is in a different module from the old one,
            i.e. .MODULE MODULE access is lost.
            - If the new lookup class is in a different package
            than the old one, protected and default (package) members will not be accessible,
            i.e. .PROTECTED PROTECTED and .PACKAGE PACKAGE access are lost.
            - If the new lookup class is not within the same package member
            as the old one, private members will not be accessible, and protected members
            will not be accessible by virtue of inheritance,
            i.e. .PRIVATE PRIVATE access is lost.
            (Protected members may continue to be accessible because of package sharing.)
            - If the new lookup class is not
            .accessClass(Class) accessible to this lookup,
            then no members, not even public members, will be accessible
            i.e. all access modes are lost.
            - If the new lookup class, the old lookup class and the previous lookup class
            are all in different modules i.e. teleporting to a third module,
            all access modes are lost.
            
            
            The new previous lookup class is chosen as follows:
            
            - If the new lookup object has .UNCONDITIONAL UNCONDITIONAL bit,
            the new previous lookup class is `null`.
            - If the new lookup class is in the same module as the old lookup class,
            the new previous lookup class is the old previous lookup class.
            - If the new lookup class is in a different module from the old lookup class,
            the new previous lookup class is the old lookup class.
            
            
            The resulting lookup's capabilities for loading classes
            (used during .findClass invocations)
            are determined by the lookup class' loader,
            which may change due to this operation.

            Arguments
            - requestedLookupClass: the desired lookup class for the new lookup object

            Returns
            - a lookup object which reports the desired lookup class, or the same object
            if there is no change

            Raises
            - IllegalArgumentException: if `requestedLookupClass` is a primitive type or void or array class
            - NullPointerException: if the argument is null

            See
            - <a href=".cross-module-lookup">Cross-module lookups</a>

            Unknown Tags
            - 9
            """
            ...


        def dropLookupMode(self, modeToDrop: int) -> "Lookup":
            """
            Creates a lookup on the same lookup class which this lookup object
            finds members, but with a lookup mode that has lost the given lookup mode.
            The lookup mode to drop is one of .PUBLIC PUBLIC, .MODULE
            MODULE, .PACKAGE PACKAGE, .PROTECTED PROTECTED,
            .PRIVATE PRIVATE, .ORIGINAL ORIGINAL, or
            .UNCONDITIONAL UNCONDITIONAL.
            
             If this lookup is a MethodHandles.publicLookup() public lookup,
            this lookup has `UNCONDITIONAL` mode set and it has no other mode set.
            When dropping `UNCONDITIONAL` on a public lookup then the resulting
            lookup has no access.
            
             If this lookup is not a public lookup, then the following applies
            regardless of its .lookupModes() lookup modes.
            .PROTECTED PROTECTED and .ORIGINAL ORIGINAL are always
            dropped and so the resulting lookup mode will never have these access
            capabilities. When dropping `PACKAGE`
            then the resulting lookup will not have `PACKAGE` or `PRIVATE`
            access. When dropping `MODULE` then the resulting lookup will not
            have `MODULE`, `PACKAGE`, or `PRIVATE` access.
            When dropping `PUBLIC` then the resulting lookup has no access.

            Arguments
            - modeToDrop: the lookup mode to drop

            Returns
            - a lookup object which lacks the indicated mode, or the same object if there is no change

            Raises
            - IllegalArgumentException: if `modeToDrop` is not one of `PUBLIC`,
            `MODULE`, `PACKAGE`, `PROTECTED`, `PRIVATE`, `ORIGINAL`
            or `UNCONDITIONAL`

            See
            - MethodHandles.privateLookupIn

            Since
            - 9

            Unknown Tags
            - A lookup with `PACKAGE` but not `PRIVATE` mode can safely
            delegate non-public access within the package of the lookup class without
            conferring  <a href="MethodHandles.Lookup.html#privacc">private access</a>.
            A lookup with `MODULE` but not
            `PACKAGE` mode can safely delegate `PUBLIC` access within
            the module of the lookup class without conferring package access.
            A lookup with a .previousLookupClass() previous lookup class
            (and `PUBLIC` but not `MODULE` mode) can safely delegate access
            to public classes accessible to both the module of the lookup class
            and the module of the previous lookup class.
            """
            ...


        def defineClass(self, bytes: list[int]) -> type[Any]:
            """
            Creates and links a class or interface from `bytes`
            with the same class loader and in the same runtime package and
            java.security.ProtectionDomain protection domain as this lookup's
            .lookupClass() lookup class as if calling
            ClassLoader.defineClass(String,byte[],int,int,ProtectionDomain)
            ClassLoader::defineClass.
            
             The .lookupModes() lookup modes for this lookup must include
            .PACKAGE PACKAGE access as default (package) members will be
            accessible to the class. The `PACKAGE` lookup mode serves to authenticate
            that the lookup object was created by a caller in the runtime package (or derived
            from a lookup originally created by suitably privileged code to a target class in
            the runtime package). 
            
             The `bytes` parameter is the class bytes of a valid class file (as defined
            by the *The Java Virtual Machine Specification*) with a class name in the
            same package as the lookup class. 
            
             This method does not run the class initializer. The class initializer may
            run at a later time, as detailed in section 12.4 of the *The Java Language
            Specification*. 
            
             If there is a security manager and this lookup does not have .hasFullPrivilegeAccess() full privilege access, its `checkPermission` method
            is first called to check `RuntimePermission("defineClass")`. 

            Arguments
            - bytes: the class bytes

            Returns
            - the `Class` object for the class

            Raises
            - IllegalAccessException: if this lookup does not have `PACKAGE` access
            - ClassFormatError: if `bytes` is not a `ClassFile` structure
            - IllegalArgumentException: if `bytes` denotes a class in a different package
            than the lookup class or `bytes` is not a class or interface
            (`ACC_MODULE` flag is set in the value of the `access_flags` item)
            - VerifyError: if the newly created class cannot be verified
            - LinkageError: if the newly created class cannot be linked for any other reason
            - SecurityException: if a security manager is present and it
                                      <a href="MethodHandles.Lookup.html#secmgr">refuses access</a>
            - NullPointerException: if `bytes` is `null`

            See
            - ClassLoader.defineClass(String,byte[],int,int,ProtectionDomain)

            Since
            - 9
            """
            ...


        def defineHiddenClass(self, bytes: list[int], initialize: bool, *options: Tuple["ClassOption", ...]) -> "Lookup":
            """
            Creates a *hidden* class or interface from `bytes`,
            returning a `Lookup` on the newly created class or interface.
            
             Ordinarily, a class or interface `C` is created by a class loader,
            which either defines `C` directly or delegates to another class loader.
            A class loader defines `C` directly by invoking
            ClassLoader.defineClass(String, byte[], int, int, ProtectionDomain)
            ClassLoader::defineClass, which causes the Java Virtual Machine
            to derive `C` from a purported representation in `class` file format.
            In situations where use of a class loader is undesirable, a class or interface
            `C` can be created by this method instead. This method is capable of
            defining `C`, and thereby creating it, without invoking
            `ClassLoader::defineClass`.
            Instead, this method defines `C` as if by arranging for
            the Java Virtual Machine to derive a nonarray class or interface `C`
            from a purported representation in `class` file format
            using the following rules:
            
            <ol>
            -  The .lookupModes() lookup modes for this `Lookup`
            must include .hasFullPrivilegeAccess() full privilege access.
            This level of access is needed to create `C` in the module
            of the lookup class of this `Lookup`.
            
            -  The purported representation in `bytes` must be a `ClassFile`
            structure (JVMS 4.1) of a supported major and minor version.
            The major and minor version may differ from the `class` file version
            of the lookup class of this `Lookup`.
            
            -  The value of `this_class` must be a valid index in the
            `constant_pool` table, and the entry at that index must be a valid
            `CONSTANT_Class_info` structure. Let `N` be the binary name
            encoded in internal form that is specified by this structure. `N` must
            denote a class or interface in the same package as the lookup class.
            
            -  Let `CN` be the string `N + "." + <suffix>`,
            where `<suffix>` is an unqualified name.
            
             Let `newBytes` be the `ClassFile` structure given by
            `bytes` with an additional entry in the `constant_pool` table,
            indicating a `CONSTANT_Utf8_info` structure for `CN`, and
            where the `CONSTANT_Class_info` structure indicated by `this_class`
            refers to the new `CONSTANT_Utf8_info` structure.
            
             Let `L` be the defining class loader of the lookup class of this `Lookup`.
            
             `C` is derived with name `CN`, class loader `L`, and
            purported representation `newBytes` as if by the rules of JVMS 5.3.5,
            with the following adjustments:
            
            -  The constant indicated by `this_class` is permitted to specify a name
            that includes a single `"."` character, even though this is not a valid
            binary class or interface name in internal form.
            
            -  The Java Virtual Machine marks `L` as the defining class loader of `C`,
            but no class loader is recorded as an initiating class loader of `C`.
            
            -  `C` is considered to have the same runtime
            Class.getPackage() package, Class.getModule() module
            and java.security.ProtectionDomain protection domain
            as the lookup class of this `Lookup`.
            -  Let `GN` be the binary name obtained by taking `N`
            (a binary name encoded in internal form) and replacing ASCII forward slashes with
            ASCII periods. For the instance of java.lang.Class representing `C`:
            
            -  Class.getName() returns the string `GN + "/" + <suffix>`,
                 even though this is not a valid binary class or interface name.
            -  Class.descriptorString() returns the string
                 `"L" + N + "." + <suffix> + ";"`,
                 even though this is not a valid type descriptor name.
            -  Class.describeConstable() returns an empty optional as `C`
                 cannot be described in java.lang.constant.ClassDesc nominal form.
            
            
            
            </ol>
            
             After `C` is derived, it is linked by the Java Virtual Machine.
            Linkage occurs as specified in JVMS 5.4.3, with the following adjustments:
            
            -  During verification, whenever it is necessary to load the class named
            `CN`, the attempt succeeds, producing class `C`. No request is
            made of any class loader.
            
            -  On any attempt to resolve the entry in the run-time constant pool indicated
            by `this_class`, the symbolic reference is considered to be resolved to
            `C` and resolution always succeeds immediately.
            
            
             If the `initialize` parameter is `True`,
            then `C` is initialized by the Java Virtual Machine.
            
             The newly created class or interface `C` serves as the
            .lookupClass() lookup class of the `Lookup` object
            returned by this method. `C` is *hidden* in the sense that
            no other class or interface can refer to `C` via a constant pool entry.
            That is, a hidden class or interface cannot be named as a supertype, a field type,
            a method parameter type, or a method return type by any other class.
            This is because a hidden class or interface does not have a binary name, so
            there is no internal form available to record in any class's constant pool.
            A hidden class or interface is not discoverable by Class.forName(String, boolean, ClassLoader),
            ClassLoader.loadClass(String, boolean), or .findClass(String), and
            is not java.lang.instrument.Instrumentation.isModifiableClass(Class)
            modifiable by Java agents or tool agents using the <a href="/../specs/jvmti.html">
            JVM Tool Interface</a>.
            
             A class or interface created by
            ClassLoader.defineClass(String, byte[], int, int, ProtectionDomain)
            a class loader has a strong relationship with that class loader.
            That is, every `Class` object contains a reference to the `ClassLoader`
            that Class.getClassLoader() defined it.
            This means that a class created by a class loader may be unloaded if and
            only if its defining loader is not reachable and thus may be reclaimed
            by a garbage collector (JLS 12.7).
            
            By default, however, a hidden class or interface may be unloaded even if
            the class loader that is marked as its defining loader is
            <a href="../ref/package-summary.html#reachability">reachable</a>.
            This behavior is useful when a hidden class or interface serves multiple
            classes defined by arbitrary class loaders.  In other cases, a hidden
            class or interface may be linked to a single class (or a small number of classes)
            with the same defining loader as the hidden class or interface.
            In such cases, where the hidden class or interface must be coterminous
            with a normal class or interface, the ClassOption.STRONG STRONG
            option may be passed in `options`.
            This arranges for a hidden class to have the same strong relationship
            with the class loader marked as its defining loader,
            as a normal class or interface has with its own defining loader.
            
            If `STRONG` is not used, then the invoker of `defineHiddenClass`
            may still prevent a hidden class or interface from being
            unloaded by ensuring that the `Class` object is reachable.
            
             The unloading characteristics are set for each hidden class when it is
            defined, and cannot be changed later.  An advantage of allowing hidden classes
            to be unloaded independently of the class loader marked as their defining loader
            is that a very large number of hidden classes may be created by an application.
            In contrast, if `STRONG` is used, then the JVM may run out of memory,
            just as if normal classes were created by class loaders.
            
             Classes and interfaces in a nest are allowed to have mutual access to
            their private members.  The nest relationship is determined by
            the `NestHost` attribute (JVMS 4.7.28) and
            the `NestMembers` attribute (JVMS 4.7.29) in a `class` file.
            By default, a hidden class belongs to a nest consisting only of itself
            because a hidden class has no binary name.
            The ClassOption.NESTMATE NESTMATE option can be passed in `options`
            to create a hidden class or interface `C` as a member of a nest.
            The nest to which `C` belongs is not based on any `NestHost` attribute
            in the `ClassFile` structure from which `C` was derived.
            Instead, the following rules determine the nest host of `C`:
            
            - If the nest host of the lookup class of this `Lookup` has previously
                been determined, then let `H` be the nest host of the lookup class.
                Otherwise, the nest host of the lookup class is determined using the
                algorithm in JVMS 5.4.4, yielding `H`.
            - The nest host of `C` is determined to be `H`,
                the nest host of the lookup class.
            
            
             A hidden class or interface may be serializable, but this requires a custom
            serialization mechanism in order to ensure that instances are properly serialized
            and deserialized. The default serialization mechanism supports only classes and
            interfaces that are discoverable by their class name.

            Arguments
            - bytes: the bytes that make up the class data,
            in the format of a valid `class` file as defined by
            <cite>The Java Virtual Machine Specification</cite>.
            - initialize: if `True` the class will be initialized.
            - options: ClassOption class options

            Returns
            - the `Lookup` object on the hidden class,
            with .ORIGINAL original and
            Lookup.hasFullPrivilegeAccess() full privilege access

            Raises
            - IllegalAccessException: if this `Lookup` does not have
            .hasFullPrivilegeAccess() full privilege access
            - SecurityException: if a security manager is present and it
            <a href="MethodHandles.Lookup.html#secmgr">refuses access</a>
            - ClassFormatError: if `bytes` is not a `ClassFile` structure
            - UnsupportedClassVersionError: if `bytes` is not of a supported major or minor version
            - IllegalArgumentException: if `bytes` denotes a class in a different package
            than the lookup class or `bytes` is not a class or interface
            (`ACC_MODULE` flag is set in the value of the `access_flags` item)
            - IncompatibleClassChangeError: if the class or interface named as
            the direct superclass of `C` is in fact an interface, or if any of the classes
            or interfaces named as direct superinterfaces of `C` are not in fact interfaces
            - ClassCircularityError: if any of the superclasses or superinterfaces of
            `C` is `C` itself
            - VerifyError: if the newly created class cannot be verified
            - LinkageError: if the newly created class cannot be linked for any other reason
            - NullPointerException: if any parameter is `null`

            See
            - Class.isHidden()

            Since
            - 15

            Unknown Tags
            - 4.2.1 Binary Class and Interface Names
            - 4.2.2 Unqualified Names
            - 4.7.28 The `NestHost` Attribute
            - 4.7.29 The `NestMembers` Attribute
            - 5.4.3.1 Class and Interface Resolution
            - 5.4.4 Access Control
            - 5.3.5 Deriving a `Class` from a `class` File Representation
            - 5.4 Linking
            - 5.5 Initialization
            - 12.7 Unloading of Classes and Interfaces
            """
            ...


        def defineHiddenClassWithClassData(self, bytes: list[int], classData: "Object", initialize: bool, *options: Tuple["ClassOption", ...]) -> "Lookup":
            """
            Creates a *hidden* class or interface from `bytes` with associated
            MethodHandles.classData(Lookup, String, Class) class data,
            returning a `Lookup` on the newly created class or interface.
            
             This method is equivalent to calling
            .defineHiddenClass(byte[], boolean, ClassOption...) defineHiddenClass(bytes, initialize, options)
            as if the hidden class is injected with a private static final *unnamed*
            field which is initialized with the given `classData` at
            the first instruction of the class initializer.
            The newly created class is linked by the Java Virtual Machine.
            
             The MethodHandles.classData(Lookup, String, Class) MethodHandles::classData
            and MethodHandles.classDataAt(Lookup, String, Class, int) MethodHandles::classDataAt
            methods can be used to retrieve the `classData`.

            Arguments
            - bytes: the class bytes
            - classData: pre-initialized class data
            - initialize: if `True` the class will be initialized.
            - options: ClassOption class options

            Returns
            - the `Lookup` object on the hidden class,
            with .ORIGINAL original and
            Lookup.hasFullPrivilegeAccess() full privilege access

            Raises
            - IllegalAccessException: if this `Lookup` does not have
            .hasFullPrivilegeAccess() full privilege access
            - SecurityException: if a security manager is present and it
            <a href="MethodHandles.Lookup.html#secmgr">refuses access</a>
            - ClassFormatError: if `bytes` is not a `ClassFile` structure
            - UnsupportedClassVersionError: if `bytes` is not of a supported major or minor version
            - IllegalArgumentException: if `bytes` denotes a class in a different package
            than the lookup class or `bytes` is not a class or interface
            (`ACC_MODULE` flag is set in the value of the `access_flags` item)
            - IncompatibleClassChangeError: if the class or interface named as
            the direct superclass of `C` is in fact an interface, or if any of the classes
            or interfaces named as direct superinterfaces of `C` are not in fact interfaces
            - ClassCircularityError: if any of the superclasses or superinterfaces of
            `C` is `C` itself
            - VerifyError: if the newly created class cannot be verified
            - LinkageError: if the newly created class cannot be linked for any other reason
            - NullPointerException: if any parameter is `null`

            See
            - MethodHandles.classDataAt(Lookup, String, Class, int)

            Since
            - 16

            Unknown Tags
            - A framework can create a hidden class with class data with one or more
            objects and load the class data as dynamically-computed constant(s)
            via a bootstrap method.  MethodHandles.classData(Lookup, String, Class)
            Class data is accessible only to the lookup object created by the newly
            defined hidden class but inaccessible to other members in the same nest
            (unlike private static fields that are accessible to nestmates).
            Care should be taken w.r.t. mutability for example when passing
            an array or other mutable structure through the class data.
            Changing any value stored in the class data at runtime may lead to
            unpredictable behavior.
            If the class data is a `List`, it is good practice to make it
            unmodifiable for example via List.of List::of.
            - 4.2.1 Binary Class and Interface Names
            - 4.2.2 Unqualified Names
            - 4.7.28 The `NestHost` Attribute
            - 4.7.29 The `NestMembers` Attribute
            - 5.4.3.1 Class and Interface Resolution
            - 5.4.4 Access Control
            - 5.3.5 Deriving a `Class` from a `class` File Representation
            - 5.4 Linking
            - 5.5 Initialization
            - 12.7 Unloading of Classes and Interface
            """
            ...


        def toString(self) -> str:
            """
            Displays the name of the class from which lookups are to be made,
            followed by "/" and the name of the .previousLookupClass()
            previous lookup class if present.
            (The name is the one reported by java.lang.Class.getName() Class.getName.)
            If there are restrictions on the access permitted to this lookup,
            this is indicated by adding a suffix to the class name, consisting
            of a slash and a keyword.  The keyword represents the strongest
            allowed access, and is chosen as follows:
            
            - If no access is allowed, the suffix is "/noaccess".
            - If only unconditional access is allowed, the suffix is "/publicLookup".
            - If only public access to types in exported packages is allowed, the suffix is "/public".
            - If only public and module access are allowed, the suffix is "/module".
            - If public and package access are allowed, the suffix is "/package".
            - If public, package, and private access are allowed, the suffix is "/private".
            
            If none of the above cases apply, it is the case that
            .hasFullPrivilegeAccess() full privilege access
            (public, module, package, private, and protected) is allowed.
            In this case, no suffix is added.
            This is True only of an object obtained originally from
            java.lang.invoke.MethodHandles.lookup MethodHandles.lookup.
            Objects created by java.lang.invoke.MethodHandles.Lookup.in Lookup.in
            always have restricted access, and will display a suffix.
            
            (It may seem strange that protected access should be
            stronger than private access.  Viewed independently from
            package access, protected access is the first to be lost,
            because it requires a direct subclass relationship between
            caller and callee.)

            See
            - .in

            Unknown Tags
            - 9
            """
            ...


        def findStatic(self, refc: type[Any], name: str, type: "MethodType") -> "MethodHandle":
            """
            Produces a method handle for a static method.
            The type of the method handle will be that of the method.
            (Since static methods do not take receivers, there is no
            additional receiver argument inserted into the method handle type,
            as there would be with .findVirtual findVirtual or .findSpecial findSpecial.)
            The method and all its argument types must be accessible to the lookup object.
            
            The returned method handle will have
            MethodHandle.asVarargsCollector variable arity if and only if
            the method's variable arity modifier bit (`0x0080`) is set.
            
            If the returned method handle is invoked, the method's class will
            be initialized, if it has not already been initialized.
            **Example:**
            <blockquote>````import static java.lang.invoke.MethodHandles.*;
            import static java.lang.invoke.MethodType.*;
            ...
            MethodHandle MH_asList = publicLookup().findStatic(Arrays.class,
              "asList", methodType(List.class, Object[].class));
            assertEquals("[x, y]", MH_asList.invoke("x", "y").toString());````</blockquote>

            Arguments
            - refc: the class from which the method is accessed
            - name: the name of the method
            - type: the type of the method

            Returns
            - the desired method handle

            Raises
            - NoSuchMethodException: if the method does not exist
            - IllegalAccessException: if access checking fails,
                                           or if the method is not `static`,
                                           or if the method's variable arity modifier bit
                                           is set and `asVarargsCollector` fails
            - SecurityException: if a security manager is present and it
                                         <a href="MethodHandles.Lookup.html#secmgr">refuses access</a>
            - NullPointerException: if any argument is null
            """
            ...


        def findVirtual(self, refc: type[Any], name: str, type: "MethodType") -> "MethodHandle":
            """
            Produces a method handle for a virtual method.
            The type of the method handle will be that of the method,
            with the receiver type (usually `refc`) prepended.
            The method and all its argument types must be accessible to the lookup object.
            
            When called, the handle will treat the first argument as a receiver
            and, for non-private methods, dispatch on the receiver's type to determine which method
            implementation to enter.
            For private methods the named method in `refc` will be invoked on the receiver.
            (The dispatching action is identical with that performed by an
            `invokevirtual` or `invokeinterface` instruction.)
            
            The first argument will be of type `refc` if the lookup
            class has full privileges to access the member.  Otherwise
            the member must be `protected` and the first argument
            will be restricted in type to the lookup class.
            
            The returned method handle will have
            MethodHandle.asVarargsCollector variable arity if and only if
            the method's variable arity modifier bit (`0x0080`) is set.
            
            Because of the general <a href="MethodHandles.Lookup.html#equiv">equivalence</a> between `invokevirtual`
            instructions and method handles produced by `findVirtual`,
            if the class is `MethodHandle` and the name string is
            `invokeExact` or `invoke`, the resulting
            method handle is equivalent to one produced by
            java.lang.invoke.MethodHandles.exactInvoker MethodHandles.exactInvoker or
            java.lang.invoke.MethodHandles.invoker MethodHandles.invoker
            with the same `type` argument.
            
            If the class is `VarHandle` and the name string corresponds to
            the name of a signature-polymorphic access mode method, the resulting
            method handle is equivalent to one produced by
            java.lang.invoke.MethodHandles.varHandleInvoker with
            the access mode corresponding to the name string and with the same
            `type` arguments.
            
            **Example:**
            <blockquote>````import static java.lang.invoke.MethodHandles.*;
            import static java.lang.invoke.MethodType.*;
            ...
            MethodHandle MH_concat = publicLookup().findVirtual(String.class,
              "concat", methodType(String.class, String.class));
            MethodHandle MH_hashCode = publicLookup().findVirtual(Object.class,
              "hashCode", methodType(int.class));
            MethodHandle MH_hashCode_String = publicLookup().findVirtual(String.class,
              "hashCode", methodType(int.class));
            assertEquals("xy", (String) MH_concat.invokeExact("x", "y"));
            assertEquals("xy".hashCode(), (int) MH_hashCode.invokeExact((Object)"xy"));
            assertEquals("xy".hashCode(), (int) MH_hashCode_String.invokeExact("xy"));
            // interface method:
            MethodHandle MH_subSequence = publicLookup().findVirtual(CharSequence.class,
              "subSequence", methodType(CharSequence.class, int.class, int.class));
            assertEquals("def", MH_subSequence.invoke("abcdefghi", 3, 6).toString());
            // constructor "internal method" must be accessed differently:
            MethodType MT_newString = methodType(void.class); //()V for new String()
            try { assertEquals("impossible", lookup()
                    .findVirtual(String.class, "<init>", MT_newString));` catch (NoSuchMethodException ex) { } // OK
            MethodHandle MH_newString = publicLookup()
              .findConstructor(String.class, MT_newString);
            assertEquals("", (String) MH_newString.invokeExact());
            }```</blockquote>

            Arguments
            - refc: the class or interface from which the method is accessed
            - name: the name of the method
            - type: the type of the method, with the receiver argument omitted

            Returns
            - the desired method handle

            Raises
            - NoSuchMethodException: if the method does not exist
            - IllegalAccessException: if access checking fails,
                                           or if the method is `static`,
                                           or if the method's variable arity modifier bit
                                           is set and `asVarargsCollector` fails
            - SecurityException: if a security manager is present and it
                                         <a href="MethodHandles.Lookup.html#secmgr">refuses access</a>
            - NullPointerException: if any argument is null
            """
            ...


        def findConstructor(self, refc: type[Any], type: "MethodType") -> "MethodHandle":
            """
            Produces a method handle which creates an object and initializes it, using
            the constructor of the specified type.
            The parameter types of the method handle will be those of the constructor,
            while the return type will be a reference to the constructor's class.
            The constructor and all its argument types must be accessible to the lookup object.
            
            The requested type must have a return type of `void`.
            (This is consistent with the JVM's treatment of constructor type descriptors.)
            
            The returned method handle will have
            MethodHandle.asVarargsCollector variable arity if and only if
            the constructor's variable arity modifier bit (`0x0080`) is set.
            
            If the returned method handle is invoked, the constructor's class will
            be initialized, if it has not already been initialized.
            **Example:**
            <blockquote>````import static java.lang.invoke.MethodHandles.*;
            import static java.lang.invoke.MethodType.*;
            ...
            MethodHandle MH_newArrayList = publicLookup().findConstructor(
              ArrayList.class, methodType(void.class, Collection.class));
            Collection orig = Arrays.asList("x", "y");
            Collection copy = (ArrayList) MH_newArrayList.invokeExact(orig);
            assert(orig != copy);
            assertEquals(orig, copy);
            // a variable-arity constructor:
            MethodHandle MH_newProcessBuilder = publicLookup().findConstructor(
              ProcessBuilder.class, methodType(void.class, String[].class));
            ProcessBuilder pb = (ProcessBuilder)
              MH_newProcessBuilder.invoke("x", "y", "z");
            assertEquals("[x, y, z]", pb.command().toString());````</blockquote>

            Arguments
            - refc: the class or interface from which the method is accessed
            - type: the type of the method, with the receiver argument omitted, and a void return type

            Returns
            - the desired method handle

            Raises
            - NoSuchMethodException: if the constructor does not exist
            - IllegalAccessException: if access checking fails
                                           or if the method's variable arity modifier bit
                                           is set and `asVarargsCollector` fails
            - SecurityException: if a security manager is present and it
                                         <a href="MethodHandles.Lookup.html#secmgr">refuses access</a>
            - NullPointerException: if any argument is null
            """
            ...


        def findClass(self, targetName: str) -> type[Any]:
            """
            Looks up a class by name from the lookup context defined by this `Lookup` object,
            <a href="MethodHandles.Lookup.html#equiv">as if resolved</a> by an `ldc` instruction.
            Such a resolution, as specified in JVMS 5.4.3.1 section, attempts to locate and load the class,
            and then determines whether the class is accessible to this lookup object.
            
            The lookup context here is determined by the .lookupClass() lookup class,
            its class loader, and the .lookupModes() lookup modes.

            Arguments
            - targetName: the fully qualified name of the class to be looked up.

            Returns
            - the requested class.

            Raises
            - SecurityException: if a security manager is present and it
                                      <a href="MethodHandles.Lookup.html#secmgr">refuses access</a>
            - LinkageError: if the linkage fails
            - ClassNotFoundException: if the class cannot be loaded by the lookup class' loader.
            - IllegalAccessException: if the class is not accessible, using the allowed access
            modes.
            - NullPointerException: if `targetName` is null

            Since
            - 9

            Unknown Tags
            - 5.4.3.1 Class and Interface Resolution
            """
            ...


        def ensureInitialized(self, targetClass: type[Any]) -> type[Any]:
            """
            Ensures that `targetClass` has been initialized. The class
            to be initialized must be .accessClass accessible
            to this `Lookup` object.  This method causes `targetClass`
            to be initialized if it has not been already initialized,
            as specified in JVMS 5.5.

            Arguments
            - targetClass: the class to be initialized

            Returns
            - `targetClass` that has been initialized

            Raises
            - IllegalArgumentException: if `targetClass` is a primitive type or `void`
                     or array class
            - IllegalAccessException: if `targetClass` is not
                     .accessClass accessible to this lookup
            - ExceptionInInitializerError: if the class initialization provoked
                     by this method fails
            - SecurityException: if a security manager is present and it
                     <a href="MethodHandles.Lookup.html#secmgr">refuses access</a>

            Since
            - 15

            Unknown Tags
            - 5.5 Initialization
            """
            ...


        def accessClass(self, targetClass: type[Any]) -> type[Any]:
            """
            Determines if a class can be accessed from the lookup context defined by
            this `Lookup` object. The static initializer of the class is not run.
            If `targetClass` is an array class, `targetClass` is accessible
            if the element type of the array class is accessible.  Otherwise,
            `targetClass` is determined as accessible as follows.
            
            
            If `targetClass` is in the same module as the lookup class,
            the lookup class is `LC` in module `M1` and
            the previous lookup class is in module `M0` or
            `null` if not present,
            `targetClass` is accessible if and only if one of the following is True:
            
            - If this lookup has .PRIVATE access, `targetClass` is
                `LC` or other class in the same nest of `LC`.
            - If this lookup has .PACKAGE access, `targetClass` is
                in the same runtime package of `LC`.
            - If this lookup has .MODULE access, `targetClass` is
                a public type in `M1`.
            - If this lookup has .PUBLIC access, `targetClass` is
                a public type in a package exported by `M1` to at least  `M0`
                if the previous lookup class is present; otherwise, `targetClass`
                is a public type in a package exported by `M1` unconditionally.
            
            
            
            Otherwise, if this lookup has .UNCONDITIONAL access, this lookup
            can access public types in all modules when the type is in a package
            that is exported unconditionally.
            
            Otherwise, `targetClass` is in a different module from `lookupClass`,
            and if this lookup does not have `PUBLIC` access, `lookupClass`
            is inaccessible.
            
            Otherwise, if this lookup has no .previousLookupClass() previous lookup class,
            `M1` is the module containing `lookupClass` and
            `M2` is the module containing `targetClass`,
            then `targetClass` is accessible if and only if
            
            - `M1` reads `M2`, and
            - `targetClass` is public and in a package exported by
                `M2` at least to `M1`.
            
            
            Otherwise, if this lookup has a .previousLookupClass() previous lookup class,
            `M1` and `M2` are as before, and `M0` is the module
            containing the previous lookup class, then `targetClass` is accessible
            if and only if one of the following is True:
            
            - `targetClass` is in `M0` and `M1`
                Module.reads reads `M0` and the type is
                in a package that is exported to at least `M1`.
            - `targetClass` is in `M1` and `M0`
                Module.reads reads `M1` and the type is
                in a package that is exported to at least `M0`.
            - `targetClass` is in a third module `M2` and both `M0`
                and `M1` reads `M2` and the type is in a package
                that is exported to at least both `M0` and `M2`.
            
            
            Otherwise, `targetClass` is not accessible.

            Arguments
            - targetClass: the class to be access-checked

            Returns
            - the class that has been access-checked

            Raises
            - IllegalAccessException: if the class is not accessible from the lookup class
            and previous lookup class, if present, using the allowed access modes.
            - SecurityException: if a security manager is present and it
                                      <a href="MethodHandles.Lookup.html#secmgr">refuses access</a>
            - NullPointerException: if `targetClass` is `null`

            See
            - <a href=".cross-module-lookup">Cross-module lookups</a>

            Since
            - 9
            """
            ...


        def findSpecial(self, refc: type[Any], name: str, type: "MethodType", specialCaller: type[Any]) -> "MethodHandle":
            """
            Produces an early-bound method handle for a virtual method.
            It will bypass checks for overriding methods on the receiver,
            <a href="MethodHandles.Lookup.html#equiv">as if called</a> from an `invokespecial`
            instruction from within the explicitly specified `specialCaller`.
            The type of the method handle will be that of the method,
            with a suitably restricted receiver type prepended.
            (The receiver type will be `specialCaller` or a subtype.)
            The method and all its argument types must be accessible
            to the lookup object.
            
            Before method resolution,
            if the explicitly specified caller class is not identical with the
            lookup class, or if this lookup object does not have
            <a href="MethodHandles.Lookup.html#privacc">private access</a>
            privileges, the access fails.
            
            The returned method handle will have
            MethodHandle.asVarargsCollector variable arity if and only if
            the method's variable arity modifier bit (`0x0080`) is set.
            <p style="font-size:smaller;">
            *(Note:  JVM internal methods named `"<init>"` are not visible to this API,
            even though the `invokespecial` instruction can refer to them
            in special circumstances.  Use .findConstructor findConstructor
            to access instance initialization methods in a safe manner.)*
            **Example:**
            <blockquote>````import static java.lang.invoke.MethodHandles.*;
            import static java.lang.invoke.MethodType.*;
            ...
            static class Listie extends ArrayList {
              public String toString() { return "[wee Listie]";`
              static Lookup lookup() { return MethodHandles.lookup(); }
            }
            ...
            // no access to constructor via invokeSpecial:
            MethodHandle MH_newListie = Listie.lookup()
              .findConstructor(Listie.class, methodType(void.class));
            Listie l = (Listie) MH_newListie.invokeExact();
            try { assertEquals("impossible", Listie.lookup().findSpecial(
                    Listie.class, "<init>", methodType(void.class), Listie.class));
             } catch (NoSuchMethodException ex) { } // OK
            // access to super and self methods via invokeSpecial:
            MethodHandle MH_super = Listie.lookup().findSpecial(
              ArrayList.class, "toString" , methodType(String.class), Listie.class);
            MethodHandle MH_this = Listie.lookup().findSpecial(
              Listie.class, "toString" , methodType(String.class), Listie.class);
            MethodHandle MH_duper = Listie.lookup().findSpecial(
              Object.class, "toString" , methodType(String.class), Listie.class);
            assertEquals("[]", (String) MH_super.invokeExact(l));
            assertEquals(""+l, (String) MH_this.invokeExact(l));
            assertEquals("[]", (String) MH_duper.invokeExact(l)); // ArrayList method
            try { assertEquals("inaccessible", Listie.lookup().findSpecial(
                    String.class, "toString", methodType(String.class), Listie.class));
             } catch (IllegalAccessException ex) { } // OK
            Listie subl = new Listie() { public String toString() { return "[subclass]"; } };
            assertEquals(""+l, (String) MH_this.invokeExact(subl)); // Listie method
            }```</blockquote>

            Arguments
            - refc: the class or interface from which the method is accessed
            - name: the name of the method (which must not be "&lt;init&gt;")
            - type: the type of the method, with the receiver argument omitted
            - specialCaller: the proposed calling class to perform the `invokespecial`

            Returns
            - the desired method handle

            Raises
            - NoSuchMethodException: if the method does not exist
            - IllegalAccessException: if access checking fails,
                                           or if the method is `static`,
                                           or if the method's variable arity modifier bit
                                           is set and `asVarargsCollector` fails
            - SecurityException: if a security manager is present and it
                                         <a href="MethodHandles.Lookup.html#secmgr">refuses access</a>
            - NullPointerException: if any argument is null
            """
            ...


        def findGetter(self, refc: type[Any], name: str, type: type[Any]) -> "MethodHandle":
            """
            Produces a method handle giving read access to a non-static field.
            The type of the method handle will have a return type of the field's
            value type.
            The method handle's single argument will be the instance containing
            the field.
            Access checking is performed immediately on behalf of the lookup class.

            Arguments
            - refc: the class or interface from which the method is accessed
            - name: the field's name
            - type: the field's type

            Returns
            - a method handle which can load values from the field

            Raises
            - NoSuchFieldException: if the field does not exist
            - IllegalAccessException: if access checking fails, or if the field is `static`
            - SecurityException: if a security manager is present and it
                                         <a href="MethodHandles.Lookup.html#secmgr">refuses access</a>
            - NullPointerException: if any argument is null

            See
            - .findVarHandle(Class, String, Class)
            """
            ...


        def findSetter(self, refc: type[Any], name: str, type: type[Any]) -> "MethodHandle":
            """
            Produces a method handle giving write access to a non-static field.
            The type of the method handle will have a void return type.
            The method handle will take two arguments, the instance containing
            the field, and the value to be stored.
            The second argument will be of the field's value type.
            Access checking is performed immediately on behalf of the lookup class.

            Arguments
            - refc: the class or interface from which the method is accessed
            - name: the field's name
            - type: the field's type

            Returns
            - a method handle which can store values into the field

            Raises
            - NoSuchFieldException: if the field does not exist
            - IllegalAccessException: if access checking fails, or if the field is `static`
                                           or `final`
            - SecurityException: if a security manager is present and it
                                         <a href="MethodHandles.Lookup.html#secmgr">refuses access</a>
            - NullPointerException: if any argument is null

            See
            - .findVarHandle(Class, String, Class)
            """
            ...


        def findVarHandle(self, recv: type[Any], name: str, type: type[Any]) -> "VarHandle":
            """
            Produces a VarHandle giving access to a non-static field `name`
            of type `type` declared in a class of type `recv`.
            The VarHandle's variable type is `type` and it has one
            coordinate type, `recv`.
            
            Access checking is performed immediately on behalf of the lookup
            class.
            
            Certain access modes of the returned VarHandle are unsupported under
            the following conditions:
            
            - if the field is declared `final`, then the write, atomic
                update, numeric atomic update, and bitwise atomic update access
                modes are unsupported.
            - if the field type is anything other than `byte`,
                `short`, `char`, `int`, `long`,
                `float`, or `double` then numeric atomic update
                access modes are unsupported.
            - if the field type is anything other than `boolean`,
                `byte`, `short`, `char`, `int` or
                `long` then bitwise atomic update access modes are
                unsupported.
            
            
            If the field is declared `volatile` then the returned VarHandle
            will override access to the field (effectively ignore the
            `volatile` declaration) in accordance to its specified
            access modes.
            
            If the field type is `float` or `double` then numeric
            and atomic update access modes compare values using their bitwise
            representation (see Float.floatToRawIntBits and
            Double.doubleToRawLongBits, respectively).

            Arguments
            - recv: the receiver class, of type `R`, that declares the
            non-static field
            - name: the field's name
            - type: the field's type, of type `T`

            Returns
            - a VarHandle giving access to non-static fields.

            Raises
            - NoSuchFieldException: if the field does not exist
            - IllegalAccessException: if access checking fails, or if the field is `static`
            - SecurityException: if a security manager is present and it
                                         <a href="MethodHandles.Lookup.html#secmgr">refuses access</a>
            - NullPointerException: if any argument is null

            Since
            - 9

            Unknown Tags
            - Bitwise comparison of `float` values or `double` values,
            as performed by the numeric and atomic update access modes, differ
            from the primitive `==` operator and the Float.equals
            and Double.equals methods, specifically with respect to
            comparing NaN values or comparing `-0.0` with `+0.0`.
            Care should be taken when performing a compare and set or a compare
            and exchange operation with such values since the operation may
            unexpectedly fail.
            There are many possible NaN values that are considered to be
            `NaN` in Java, although no IEEE 754 floating-point operation
            provided by Java can distinguish between them.  Operation failure can
            occur if the expected or witness value is a NaN value and it is
            transformed (perhaps in a platform specific manner) into another NaN
            value, and thus has a different bitwise representation (see
            Float.intBitsToFloat or Double.longBitsToDouble for more
            details).
            The values `-0.0` and `+0.0` have different bitwise
            representations but are considered equal when using the primitive
            `==` operator.  Operation failure can occur if, for example, a
            numeric algorithm computes an expected value to be say `-0.0`
            and previously computed the witness value to be say `+0.0`.
            """
            ...


        def findStaticGetter(self, refc: type[Any], name: str, type: type[Any]) -> "MethodHandle":
            """
            Produces a method handle giving read access to a static field.
            The type of the method handle will have a return type of the field's
            value type.
            The method handle will take no arguments.
            Access checking is performed immediately on behalf of the lookup class.
            
            If the returned method handle is invoked, the field's class will
            be initialized, if it has not already been initialized.

            Arguments
            - refc: the class or interface from which the method is accessed
            - name: the field's name
            - type: the field's type

            Returns
            - a method handle which can load values from the field

            Raises
            - NoSuchFieldException: if the field does not exist
            - IllegalAccessException: if access checking fails, or if the field is not `static`
            - SecurityException: if a security manager is present and it
                                         <a href="MethodHandles.Lookup.html#secmgr">refuses access</a>
            - NullPointerException: if any argument is null
            """
            ...


        def findStaticSetter(self, refc: type[Any], name: str, type: type[Any]) -> "MethodHandle":
            """
            Produces a method handle giving write access to a static field.
            The type of the method handle will have a void return type.
            The method handle will take a single
            argument, of the field's value type, the value to be stored.
            Access checking is performed immediately on behalf of the lookup class.
            
            If the returned method handle is invoked, the field's class will
            be initialized, if it has not already been initialized.

            Arguments
            - refc: the class or interface from which the method is accessed
            - name: the field's name
            - type: the field's type

            Returns
            - a method handle which can store values into the field

            Raises
            - NoSuchFieldException: if the field does not exist
            - IllegalAccessException: if access checking fails, or if the field is not `static`
                                           or is `final`
            - SecurityException: if a security manager is present and it
                                         <a href="MethodHandles.Lookup.html#secmgr">refuses access</a>
            - NullPointerException: if any argument is null
            """
            ...


        def findStaticVarHandle(self, decl: type[Any], name: str, type: type[Any]) -> "VarHandle":
            """
            Produces a VarHandle giving access to a static field `name` of
            type `type` declared in a class of type `decl`.
            The VarHandle's variable type is `type` and it has no
            coordinate types.
            
            Access checking is performed immediately on behalf of the lookup
            class.
            
            If the returned VarHandle is operated on, the declaring class will be
            initialized, if it has not already been initialized.
            
            Certain access modes of the returned VarHandle are unsupported under
            the following conditions:
            
            - if the field is declared `final`, then the write, atomic
                update, numeric atomic update, and bitwise atomic update access
                modes are unsupported.
            - if the field type is anything other than `byte`,
                `short`, `char`, `int`, `long`,
                `float`, or `double`, then numeric atomic update
                access modes are unsupported.
            - if the field type is anything other than `boolean`,
                `byte`, `short`, `char`, `int` or
                `long` then bitwise atomic update access modes are
                unsupported.
            
            
            If the field is declared `volatile` then the returned VarHandle
            will override access to the field (effectively ignore the
            `volatile` declaration) in accordance to its specified
            access modes.
            
            If the field type is `float` or `double` then numeric
            and atomic update access modes compare values using their bitwise
            representation (see Float.floatToRawIntBits and
            Double.doubleToRawLongBits, respectively).

            Arguments
            - decl: the class that declares the static field
            - name: the field's name
            - type: the field's type, of type `T`

            Returns
            - a VarHandle giving access to a static field

            Raises
            - NoSuchFieldException: if the field does not exist
            - IllegalAccessException: if access checking fails, or if the field is not `static`
            - SecurityException: if a security manager is present and it
                                         <a href="MethodHandles.Lookup.html#secmgr">refuses access</a>
            - NullPointerException: if any argument is null

            Since
            - 9

            Unknown Tags
            - Bitwise comparison of `float` values or `double` values,
            as performed by the numeric and atomic update access modes, differ
            from the primitive `==` operator and the Float.equals
            and Double.equals methods, specifically with respect to
            comparing NaN values or comparing `-0.0` with `+0.0`.
            Care should be taken when performing a compare and set or a compare
            and exchange operation with such values since the operation may
            unexpectedly fail.
            There are many possible NaN values that are considered to be
            `NaN` in Java, although no IEEE 754 floating-point operation
            provided by Java can distinguish between them.  Operation failure can
            occur if the expected or witness value is a NaN value and it is
            transformed (perhaps in a platform specific manner) into another NaN
            value, and thus has a different bitwise representation (see
            Float.intBitsToFloat or Double.longBitsToDouble for more
            details).
            The values `-0.0` and `+0.0` have different bitwise
            representations but are considered equal when using the primitive
            `==` operator.  Operation failure can occur if, for example, a
            numeric algorithm computes an expected value to be say `-0.0`
            and previously computed the witness value to be say `+0.0`.
            """
            ...


        def bind(self, receiver: "Object", name: str, type: "MethodType") -> "MethodHandle":
            """
            Produces an early-bound method handle for a non-static method.
            The receiver must have a supertype `defc` in which a method
            of the given name and type is accessible to the lookup class.
            The method and all its argument types must be accessible to the lookup object.
            The type of the method handle will be that of the method,
            without any insertion of an additional receiver parameter.
            The given receiver will be bound into the method handle,
            so that every call to the method handle will invoke the
            requested method on the given receiver.
            
            The returned method handle will have
            MethodHandle.asVarargsCollector variable arity if and only if
            the method's variable arity modifier bit (`0x0080`) is set
            *and* the trailing array argument is not the only argument.
            (If the trailing array argument is the only argument,
            the given receiver value will be bound to it.)
            
            This is almost equivalent to the following code, with some differences noted below:
            <blockquote>````import static java.lang.invoke.MethodHandles.*;
            import static java.lang.invoke.MethodType.*;
            ...
            MethodHandle mh0 = lookup().findVirtual(defc, name, type);
            MethodHandle mh1 = mh0.bindTo(receiver);
            mh1 = mh1.withVarargs(mh0.isVarargsCollector());
            return mh1;````</blockquote>
            where `defc` is either `receiver.getClass()` or a super
            type of that class, in which the requested method is accessible
            to the lookup class.
            (Unlike `bind`, `bindTo` does not preserve variable arity.
            Also, `bindTo` may throw a `ClassCastException` in instances where `bind` would
            throw an `IllegalAccessException`, as in the case where the member is `protected` and
            the receiver is restricted by `findVirtual` to the lookup class.)

            Arguments
            - receiver: the object from which the method is accessed
            - name: the name of the method
            - type: the type of the method, with the receiver argument omitted

            Returns
            - the desired method handle

            Raises
            - NoSuchMethodException: if the method does not exist
            - IllegalAccessException: if access checking fails
                                           or if the method's variable arity modifier bit
                                           is set and `asVarargsCollector` fails
            - SecurityException: if a security manager is present and it
                                         <a href="MethodHandles.Lookup.html#secmgr">refuses access</a>
            - NullPointerException: if any argument is null

            See
            - .findVirtual
            """
            ...


        def unreflect(self, m: "Method") -> "MethodHandle":
            """
            Makes a <a href="MethodHandleInfo.html#directmh">direct method handle</a>
            to *m*, if the lookup class has permission.
            If *m* is non-static, the receiver argument is treated as an initial argument.
            If *m* is virtual, overriding is respected on every call.
            Unlike the Core Reflection API, exceptions are *not* wrapped.
            The type of the method handle will be that of the method,
            with the receiver type prepended (but only if it is non-static).
            If the method's `accessible` flag is not set,
            access checking is performed immediately on behalf of the lookup class.
            If *m* is not public, do not share the resulting handle with untrusted parties.
            
            The returned method handle will have
            MethodHandle.asVarargsCollector variable arity if and only if
            the method's variable arity modifier bit (`0x0080`) is set.
            
            If *m* is static, and
            if the returned method handle is invoked, the method's class will
            be initialized, if it has not already been initialized.

            Arguments
            - m: the reflected method

            Returns
            - a method handle which can invoke the reflected method

            Raises
            - IllegalAccessException: if access checking fails
                                           or if the method's variable arity modifier bit
                                           is set and `asVarargsCollector` fails
            - NullPointerException: if the argument is null
            """
            ...


        def unreflectSpecial(self, m: "Method", specialCaller: type[Any]) -> "MethodHandle":
            """
            Produces a method handle for a reflected method.
            It will bypass checks for overriding methods on the receiver,
            <a href="MethodHandles.Lookup.html#equiv">as if called</a> from an `invokespecial`
            instruction from within the explicitly specified `specialCaller`.
            The type of the method handle will be that of the method,
            with a suitably restricted receiver type prepended.
            (The receiver type will be `specialCaller` or a subtype.)
            If the method's `accessible` flag is not set,
            access checking is performed immediately on behalf of the lookup class,
            as if `invokespecial` instruction were being linked.
            
            Before method resolution,
            if the explicitly specified caller class is not identical with the
            lookup class, or if this lookup object does not have
            <a href="MethodHandles.Lookup.html#privacc">private access</a>
            privileges, the access fails.
            
            The returned method handle will have
            MethodHandle.asVarargsCollector variable arity if and only if
            the method's variable arity modifier bit (`0x0080`) is set.

            Arguments
            - m: the reflected method
            - specialCaller: the class nominally calling the method

            Returns
            - a method handle which can invoke the reflected method

            Raises
            - IllegalAccessException: if access checking fails,
                                           or if the method is `static`,
                                           or if the method's variable arity modifier bit
                                           is set and `asVarargsCollector` fails
            - NullPointerException: if any argument is null
            """
            ...


        def unreflectConstructor(self, c: "Constructor"[Any]) -> "MethodHandle":
            """
            Produces a method handle for a reflected constructor.
            The type of the method handle will be that of the constructor,
            with the return type changed to the declaring class.
            The method handle will perform a `newInstance` operation,
            creating a new instance of the constructor's class on the
            arguments passed to the method handle.
            
            If the constructor's `accessible` flag is not set,
            access checking is performed immediately on behalf of the lookup class.
            
            The returned method handle will have
            MethodHandle.asVarargsCollector variable arity if and only if
            the constructor's variable arity modifier bit (`0x0080`) is set.
            
            If the returned method handle is invoked, the constructor's class will
            be initialized, if it has not already been initialized.

            Arguments
            - c: the reflected constructor

            Returns
            - a method handle which can invoke the reflected constructor

            Raises
            - IllegalAccessException: if access checking fails
                                           or if the method's variable arity modifier bit
                                           is set and `asVarargsCollector` fails
            - NullPointerException: if the argument is null
            """
            ...


        def unreflectGetter(self, f: "Field") -> "MethodHandle":
            """
            Produces a method handle giving read access to a reflected field.
            The type of the method handle will have a return type of the field's
            value type.
            If the field is `static`, the method handle will take no arguments.
            Otherwise, its single argument will be the instance containing
            the field.
            If the `Field` object's `accessible` flag is not set,
            access checking is performed immediately on behalf of the lookup class.
            
            If the field is static, and
            if the returned method handle is invoked, the field's class will
            be initialized, if it has not already been initialized.

            Arguments
            - f: the reflected field

            Returns
            - a method handle which can load values from the reflected field

            Raises
            - IllegalAccessException: if access checking fails
            - NullPointerException: if the argument is null
            """
            ...


        def unreflectSetter(self, f: "Field") -> "MethodHandle":
            """
            Produces a method handle giving write access to a reflected field.
            The type of the method handle will have a void return type.
            If the field is `static`, the method handle will take a single
            argument, of the field's value type, the value to be stored.
            Otherwise, the two arguments will be the instance containing
            the field, and the value to be stored.
            If the `Field` object's `accessible` flag is not set,
            access checking is performed immediately on behalf of the lookup class.
            
            If the field is `final`, write access will not be
            allowed and access checking will fail, except under certain
            narrow circumstances documented for Field.set Field.set.
            A method handle is returned only if a corresponding call to
            the `Field` object's `set` method could return
            normally.  In particular, fields which are both `static`
            and `final` may never be set.
            
            If the field is `static`, and
            if the returned method handle is invoked, the field's class will
            be initialized, if it has not already been initialized.

            Arguments
            - f: the reflected field

            Returns
            - a method handle which can store values into the reflected field

            Raises
            - IllegalAccessException: if access checking fails,
                    or if the field is `final` and write access
                    is not enabled on the `Field` object
            - NullPointerException: if the argument is null
            """
            ...


        def unreflectVarHandle(self, f: "Field") -> "VarHandle":
            """
            Produces a VarHandle giving access to a reflected field `f`
            of type `T` declared in a class of type `R`.
            The VarHandle's variable type is `T`.
            If the field is non-static the VarHandle has one coordinate type,
            `R`.  Otherwise, the field is static, and the VarHandle has no
            coordinate types.
            
            Access checking is performed immediately on behalf of the lookup
            class, regardless of the value of the field's `accessible`
            flag.
            
            If the field is static, and if the returned VarHandle is operated
            on, the field's declaring class will be initialized, if it has not
            already been initialized.
            
            Certain access modes of the returned VarHandle are unsupported under
            the following conditions:
            
            - if the field is declared `final`, then the write, atomic
                update, numeric atomic update, and bitwise atomic update access
                modes are unsupported.
            - if the field type is anything other than `byte`,
                `short`, `char`, `int`, `long`,
                `float`, or `double` then numeric atomic update
                access modes are unsupported.
            - if the field type is anything other than `boolean`,
                `byte`, `short`, `char`, `int` or
                `long` then bitwise atomic update access modes are
                unsupported.
            
            
            If the field is declared `volatile` then the returned VarHandle
            will override access to the field (effectively ignore the
            `volatile` declaration) in accordance to its specified
            access modes.
            
            If the field type is `float` or `double` then numeric
            and atomic update access modes compare values using their bitwise
            representation (see Float.floatToRawIntBits and
            Double.doubleToRawLongBits, respectively).

            Arguments
            - f: the reflected field, with a field of type `T`, and
            a declaring class of type `R`

            Returns
            - a VarHandle giving access to non-static fields or a static
            field

            Raises
            - IllegalAccessException: if access checking fails
            - NullPointerException: if the argument is null

            Since
            - 9

            Unknown Tags
            - Bitwise comparison of `float` values or `double` values,
            as performed by the numeric and atomic update access modes, differ
            from the primitive `==` operator and the Float.equals
            and Double.equals methods, specifically with respect to
            comparing NaN values or comparing `-0.0` with `+0.0`.
            Care should be taken when performing a compare and set or a compare
            and exchange operation with such values since the operation may
            unexpectedly fail.
            There are many possible NaN values that are considered to be
            `NaN` in Java, although no IEEE 754 floating-point operation
            provided by Java can distinguish between them.  Operation failure can
            occur if the expected or witness value is a NaN value and it is
            transformed (perhaps in a platform specific manner) into another NaN
            value, and thus has a different bitwise representation (see
            Float.intBitsToFloat or Double.longBitsToDouble for more
            details).
            The values `-0.0` and `+0.0` have different bitwise
            representations but are considered equal when using the primitive
            `==` operator.  Operation failure can occur if, for example, a
            numeric algorithm computes an expected value to be say `-0.0`
            and previously computed the witness value to be say `+0.0`.
            """
            ...


        def revealDirect(self, target: "MethodHandle") -> "MethodHandleInfo":
            """
            Cracks a <a href="MethodHandleInfo.html#directmh">direct method handle</a>
            created by this lookup object or a similar one.
            Security and access checks are performed to ensure that this lookup object
            is capable of reproducing the target method handle.
            This means that the cracking may fail if target is a direct method handle
            but was created by an unrelated lookup object.
            This can happen if the method handle is <a href="MethodHandles.Lookup.html#callsens">caller sensitive</a>
            and was created by a lookup object for a different class.

            Arguments
            - target: a direct method handle to crack into symbolic reference components

            Returns
            - a symbolic reference which can be used to reconstruct this method handle from this lookup object

            Raises
            - SecurityException: if a security manager is present and it
                                         <a href="MethodHandles.Lookup.html#secmgr">refuses access</a>
            - IllegalArgumentException: if the target is not a direct method handle or if access checking fails
            - NullPointerException: if the target is `null`

            See
            - MethodHandleInfo

            Since
            - 1.8
            """
            ...


        def hasPrivateAccess(self) -> bool:
            """
            Returns `True` if this lookup has `PRIVATE` and `MODULE` access.

            Returns
            - `True` if this lookup has `PRIVATE` and `MODULE` access.

            Since
            - 9

            Deprecated
            - This method was originally designed to test `PRIVATE` access
            that implies full privilege access but `MODULE` access has since become
            independent of `PRIVATE` access.  It is recommended to call
            .hasFullPrivilegeAccess() instead.
            """
            ...


        def hasFullPrivilegeAccess(self) -> bool:
            """
            Returns `True` if this lookup has *full privilege access*,
            i.e. `PRIVATE` and `MODULE` access.
            A `Lookup` object must have full privilege access in order to
            access all members that are allowed to the
            .lookupClass() lookup class.

            Returns
            - `True` if this lookup has full privilege access.

            See
            - <a href="MethodHandles.Lookup.html.privacc">private and module access</a>

            Since
            - 14
            """
            ...


        class ClassOption(Enum):
            """
            The set of class options that specify whether a hidden class created by
            Lookup.defineHiddenClass(byte[], boolean, ClassOption...)
            Lookup::defineHiddenClass method is dynamically added as a new member
            to the nest of a lookup class and/or whether a hidden class has
            a strong relationship with the class loader marked as its defining loader.

            Since
            - 15
            """

            NESTMATE = (NESTMATE_CLASS)
            """
            Specifies that a hidden class be added to Class.getNestHost nest
            of a lookup class as a nestmate.
            
             A hidden nestmate class has access to the private members of all
            classes and interfaces in the same nest.

            See
            - Class.getNestHost()
            """
            STRONG = (STRONG_LOADER_LINK)
            """
            Specifies that a hidden class has a *strong*
            relationship with the class loader marked as its defining loader,
            as a normal class or interface has with its own defining loader.
            This means that the hidden class may be unloaded if and only if
            its defining loader is not reachable and thus may be reclaimed
            by a garbage collector (JLS 12.7).
            
             By default, a hidden class or interface may be unloaded
            even if the class loader that is marked as its defining loader is
            <a href="../ref/package-summary.html#reachability">reachable</a>.

            Unknown Tags
            - 12.7 Unloading of Classes and Interfaces
            """
