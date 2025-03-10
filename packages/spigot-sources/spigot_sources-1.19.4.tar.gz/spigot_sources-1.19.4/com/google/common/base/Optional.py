"""
Python module generated from Java source file com.google.common.base.Optional

Java source file obtained from artifact guava version 31.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.annotations import GwtCompatible
from com.google.common.base import *
from com.google.errorprone.annotations import DoNotMock
from java.io import Serializable
from java.util import Iterator
from javax.annotation import CheckForNull
from typing import Any, Callable, Iterable, Tuple


class Optional(Serializable):
    """
    An immutable object that may contain a non-null reference to another object. Each instance of
    this type either contains a non-null reference, or contains nothing (in which case we say that
    the reference is "absent"); it is never said to "contain `null`".
    
    A non-null `Optional<T>` reference can be used as a replacement for a nullable `T`
    reference. It allows you to represent "a `T` that must be present" and a "a `T` that
    might be absent" as two distinct types in your program, which can aid clarity.
    
    Some uses of this class include
    
    
      - As a method return type, as an alternative to returning `null` to indicate that no
          value was available
      - To distinguish between "unknown" (for example, not present in a map) and "known to have no
          value" (present in the map, with value `Optional.absent()`)
      - To wrap nullable references for storage in a collection that does not support `null`
          (though there are <a
          href="https://github.com/google/guava/wiki/LivingWithNullHostileCollections">several other
          approaches to this</a> that should be considered first)
    
    
    A common alternative to using this class is to find or create a suitable <a
    href="http://en.wikipedia.org/wiki/Null_Object_pattern">null object</a> for the type in question.
    
    This class is not intended as a direct analogue of any existing "option" or "maybe" construct
    from other programming environments, though it may bear some similarities.
    
    **Comparison to `java.util.Optional` (JDK 8 and higher):** A new `Optional`
    class was added for Java 8. The two classes are extremely similar, but incompatible (they cannot
    share a common supertype). *All* known differences are listed either here or with the
    relevant methods below.
    
    
      - This class is serializable; `java.util.Optional` is not.
      - `java.util.Optional` has the additional methods `ifPresent`, `filter`,
          `flatMap`, and `orElseThrow`.
      - `java.util` offers the primitive-specialized versions `OptionalInt`, `OptionalLong` and `OptionalDouble`, the use of which is recommended; Guava does not
          have these.
    
    
    **There are no plans to deprecate this class in the foreseeable future.** However, we do
    gently recommend that you prefer the new, standard Java class whenever possible.
    
    See the Guava User Guide article on <a
    href="https://github.com/google/guava/wiki/UsingAndAvoidingNullExplained#optional">using `Optional`</a>.
    
    Type `<T>`: the type of instance that can be contained. `Optional` is naturally covariant on
        this type, so it is safe to cast an `Optional<T>` to `Optional<S>` for any
        supertype `S` of `T`.

    Author(s)
    - Kevin Bourrillion

    Since
    - 10.0
    """

    @staticmethod
    def absent() -> "Optional"["T"]:
        """
        Returns an `Optional` instance with no contained reference.
        
        **Comparison to `java.util.Optional`:** this method is equivalent to Java 8's
        `Optional.empty`.
        """
        ...


    @staticmethod
    def of(reference: "T") -> "Optional"["T"]:
        """
        Returns an `Optional` instance containing the given non-null reference. To have `null` treated as .absent, use .fromNullable instead.
        
        **Comparison to `java.util.Optional`:** no differences.

        Raises
        - NullPointerException: if `reference` is null
        """
        ...


    @staticmethod
    def fromNullable(nullableReference: "T") -> "Optional"["T"]:
        """
        If `nullableReference` is non-null, returns an `Optional` instance containing that
        reference; otherwise returns Optional.absent.
        
        **Comparison to `java.util.Optional`:** this method is equivalent to Java 8's
        `Optional.ofNullable`.
        """
        ...


    @staticmethod
    def fromJavaUtil(javaUtilOptional: "java.util.Optional"["T"]) -> "Optional"["T"]:
        """
        Returns the equivalent `com.google.common.base.Optional` value to the given `java.util.Optional`, or `null` if the argument is null.

        Since
        - 21.0
        """
        ...


    @staticmethod
    def toJavaUtil(googleOptional: "Optional"["T"]) -> "java.util.Optional"["T"]:
        """
        Returns the equivalent `java.util.Optional` value to the given `com.google.common.base.Optional`, or `null` if the argument is null.
        
        If `googleOptional` is known to be non-null, use `googleOptional.toJavaUtil()`
        instead.
        
        Unfortunately, the method reference `Optional::toJavaUtil` will not work, because it
        could refer to either the static or instance version of this method. Write out the lambda
        expression `o -> Optional.toJavaUtil(o)` instead.

        Since
        - 21.0
        """
        ...


    def toJavaUtil(self) -> "java.util.Optional"["T"]:
        """
        Returns the equivalent `java.util.Optional` value to this optional.
        
        Unfortunately, the method reference `Optional::toJavaUtil` will not work, because it
        could refer to either the static or instance version of this method. Write out the lambda
        expression `o -> o.toJavaUtil()` instead.

        Since
        - 21.0
        """
        ...


    def isPresent(self) -> bool:
        """
        Returns `True` if this holder contains a (non-null) instance.
        
        **Comparison to `java.util.Optional`:** no differences.
        """
        ...


    def get(self) -> "T":
        """
        Returns the contained instance, which must be present. If the instance might be absent, use
        .or(Object) or .orNull instead.
        
        **Comparison to `java.util.Optional`:** when the value is absent, this method
        throws IllegalStateException, whereas the Java 8 counterpart throws java.util.NoSuchElementException NoSuchElementException.

        Raises
        - IllegalStateException: if the instance is absent (.isPresent returns `False`); depending on this *specific* exception type (over the more general RuntimeException) is discouraged
        """
        ...


    def or(self, defaultValue: "T") -> "T":
        """
        Returns the contained instance if it is present; `defaultValue` otherwise. If no default
        value should be required because the instance is known to be present, use .get()
        instead. For a default value of `null`, use .orNull.
        
        Note about generics: The signature `public T or(T defaultValue)` is overly
        restrictive. However, the ideal signature, `public <S super T> S or(S)`, is not legal
        Java. As a result, some sensible operations involving subtypes are compile errors:
        
        ````Optional<Integer> optionalInt = getSomeOptionalInt();
        Number value = optionalInt.or(0.5); // error
        
        FluentIterable<? extends Number> numbers = getSomeNumbers();
        Optional<? extends Number> first = numbers.first();
        Number value = first.or(0.5); // error````
        
        As a workaround, it is always safe to cast an `Optional<? extends T>` to `Optional<T>`. Casting either of the above example `Optional` instances to `Optional<Number>` (where `Number` is the desired output type) solves the problem:
        
        ````Optional<Number> optionalInt = (Optional) getSomeOptionalInt();
        Number value = optionalInt.or(0.5); // fine
        
        FluentIterable<? extends Number> numbers = getSomeNumbers();
        Optional<Number> first = (Optional) numbers.first();
        Number value = first.or(0.5); // fine````
        
        **Comparison to `java.util.Optional`:** this method is similar to Java 8's `Optional.orElse`, but will not accept `null` as a `defaultValue` (.orNull
        must be used instead). As a result, the value returned by this method is guaranteed non-null,
        which is not the case for the `java.util` equivalent.
        """
        ...


    def or(self, secondChoice: "Optional"["T"]) -> "Optional"["T"]:
        """
        Returns this `Optional` if it has a value present; `secondChoice` otherwise.
        
        **Comparison to `java.util.Optional`:** this method has no equivalent in Java 8's
        `Optional` class; write `thisOptional.isPresent() ? thisOptional : secondChoice`
        instead.
        """
        ...


    def or(self, supplier: "Supplier"["T"]) -> "T":
        """
        Returns the contained instance if it is present; `supplier.get()` otherwise.
        
        **Comparison to `java.util.Optional`:** this method is similar to Java 8's `Optional.orElseGet`, except when `supplier` returns `null`. In this case this
        method throws an exception, whereas the Java 8 method returns the `null` to the caller.

        Raises
        - NullPointerException: if this optional's value is absent and the supplier returns `null`
        """
        ...


    def orNull(self) -> "T":
        """
        Returns the contained instance if it is present; `null` otherwise. If the instance is
        known to be present, use .get() instead.
        
        **Comparison to `java.util.Optional`:** this method is equivalent to Java 8's
        `Optional.orElse(null)`.
        """
        ...


    def asSet(self) -> set["T"]:
        """
        Returns an immutable singleton Set whose only element is the contained instance if it
        is present; an empty immutable Set otherwise.
        
        **Comparison to `java.util.Optional`:** this method has no equivalent in Java 8's
        `Optional` class. However, this common usage:
        
        ````for (Foo foo : possibleFoo.asSet()) {
          doSomethingWith(foo);`
        }```
        
        ... can be replaced with:
        
        ````possibleFoo.ifPresent(foo -> doSomethingWith(foo));````
        
        **Java 9 users:** some use cases can be written with calls to `optional.stream()`.

        Since
        - 11.0
        """
        ...


    def transform(self, function: "Function"["T", "V"]) -> "Optional"["V"]:
        """
        If the instance is present, it is transformed with the given Function; otherwise,
        Optional.absent is returned.
        
        **Comparison to `java.util.Optional`:** this method is similar to Java 8's `Optional.map`, except when `function` returns `null`. In this case this method
        throws an exception, whereas the Java 8 method returns `Optional.absent()`.

        Raises
        - NullPointerException: if the function returns `null`

        Since
        - 12.0
        """
        ...


    def equals(self, object: "Object") -> bool:
        """
        Returns `True` if `object` is an `Optional` instance, and either the
        contained references are Object.equals equal to each other or both are absent.
        Note that `Optional` instances of differing parameterized types can be equal.
        
        **Comparison to `java.util.Optional`:** no differences.
        """
        ...


    def hashCode(self) -> int:
        """
        Returns a hash code for this instance.
        
        **Comparison to `java.util.Optional`:** this class leaves the specific choice of
        hash code unspecified, unlike the Java 8 equivalent.
        """
        ...


    def toString(self) -> str:
        """
        Returns a string representation for this instance.
        
        **Comparison to `java.util.Optional`:** this class leaves the specific string
        representation unspecified, unlike the Java 8 equivalent.
        """
        ...


    @staticmethod
    def presentInstances(optionals: Iterable["Optional"["T"]]) -> Iterable["T"]:
        """
        Returns the value of each present instance from the supplied `optionals`, in order,
        skipping over occurrences of Optional.absent. Iterators are unmodifiable and are
        evaluated lazily.
        
        **Comparison to `java.util.Optional`:** this method has no equivalent in Java 8's
        `Optional` class; use `optionals.stream().filter(Optional::isPresent).map(Optional::get)` instead.
        
        **Java 9 users:** use `optionals.stream().flatMap(Optional::stream)` instead.

        Since
        - 11.0 (generics widened in 13.0)
        """
        ...
