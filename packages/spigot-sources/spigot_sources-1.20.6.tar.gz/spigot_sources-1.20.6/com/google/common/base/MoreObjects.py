"""
Python module generated from Java source file com.google.common.base.MoreObjects

Java source file obtained from artifact guava version 32.1.2-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.base import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from java.lang.reflect import Array
from java.util import Arrays
from java.util import OptionalDouble
from java.util import OptionalInt
from java.util import OptionalLong
from javax.annotation import CheckForNull
from typing import Any, Callable, Iterable, Tuple


class MoreObjects:
    """
    Helper functions that operate on any `Object`, and are not already provided in java.util.Objects.
    
    See the Guava User Guide on <a
    href="https://github.com/google/guava/wiki/CommonObjectUtilitiesExplained">writing `Object`
    methods with `MoreObjects`</a>.

    Author(s)
    - Laurence Gonsalves

    Since
    - 18.0 (since 2.0 as `Objects`)
    """

    @staticmethod
    def firstNonNull(first: "T", second: "T") -> "T":
        """
        Returns the first of two given parameters that is not `null`, if either is, or otherwise
        throws a NullPointerException.
        
        To find the first non-null element in an iterable, use `Iterables.find(iterable,
        Predicates.notNull())`. For varargs, use `Iterables.find(Arrays.asList(a, b, c, ...),
        Predicates.notNull())`, static importing as necessary.
        
        **Note:** if `first` is represented as an Optional, this can be
        accomplished with Optional.or(Object) first.or(second). That approach also allows for
        lazy evaluation of the fallback instance, using Optional.or(Supplier)
        first.or(supplier).
        
        **Java 9 users:** use `java.util.Objects.requireNonNullElse(first, second)`
        instead.

        Returns
        - `first` if it is non-null; otherwise `second` if it is non-null

        Raises
        - NullPointerException: if both `first` and `second` are null

        Since
        - 18.0 (since 3.0 as `Objects.firstNonNull()`).
        """
        ...


    @staticmethod
    def toStringHelper(self: "Object") -> "ToStringHelper":
        """
        Creates an instance of ToStringHelper.
        
        This is helpful for implementing Object.toString(). Specification by example:
        
        ````// Returns "ClassName{`"
        MoreObjects.toStringHelper(this)
            .toString();
        
        // Returns "ClassName{x=1}"
        MoreObjects.toStringHelper(this)
            .add("x", 1)
            .toString();
        
        // Returns "MyObject{x=1}"
        MoreObjects.toStringHelper("MyObject")
            .add("x", 1)
            .toString();
        
        // Returns "ClassName{x=1, y=foo}"
        MoreObjects.toStringHelper(this)
            .add("x", 1)
            .add("y", "foo")
            .toString();
        
        // Returns "ClassName{x=1}"
        MoreObjects.toStringHelper(this)
            .omitNullValues()
            .add("x", 1)
            .add("y", null)
            .toString();
        }```
        
        Note that in GWT, class names are often obfuscated.

        Arguments
        - self: the object to generate the string for (typically `this`), used only for its
            class name

        Since
        - 18.0 (since 2.0 as `Objects.toStringHelper()`).
        """
        ...


    @staticmethod
    def toStringHelper(clazz: type[Any]) -> "ToStringHelper":
        """
        Creates an instance of ToStringHelper in the same manner as .toStringHelper(Object), but using the simple name of `clazz` instead of using an
        instance's Object.getClass().
        
        Note that in GWT, class names are often obfuscated.

        Arguments
        - clazz: the Class of the instance

        Since
        - 18.0 (since 7.0 as `Objects.toStringHelper()`).
        """
        ...


    @staticmethod
    def toStringHelper(className: str) -> "ToStringHelper":
        """
        Creates an instance of ToStringHelper in the same manner as .toStringHelper(Object), but using `className` instead of using an instance's Object.getClass().

        Arguments
        - className: the name of the instance type

        Since
        - 18.0 (since 7.0 as `Objects.toStringHelper()`).
        """
        ...


    class ToStringHelper:
        """
        Support class for MoreObjects.toStringHelper.

    Author(s)
        - Jason Lee

        Since
        - 18.0 (since 2.0 as `Objects.ToStringHelper`).
        """

        def omitNullValues(self) -> "ToStringHelper":
            """
            Configures the ToStringHelper so .toString() will ignore properties with null
            value. The order of calling this method, relative to the `add()`/`addValue()`
            methods, is not significant.

            Since
            - 18.0 (since 12.0 as `Objects.ToStringHelper.omitNullValues()`).
            """
            ...


        def add(self, name: str, value: "Object") -> "ToStringHelper":
            """
            Adds a name/value pair to the formatted output in `name=value` format. If `value`
            is `null`, the string `"null"` is used, unless .omitNullValues() is
            called, in which case this name/value pair will not be added.
            """
            ...


        def add(self, name: str, value: bool) -> "ToStringHelper":
            """
            Adds a name/value pair to the formatted output in `name=value` format.

            Since
            - 18.0 (since 11.0 as `Objects.ToStringHelper.add()`).
            """
            ...


        def add(self, name: str, value: str) -> "ToStringHelper":
            """
            Adds a name/value pair to the formatted output in `name=value` format.

            Since
            - 18.0 (since 11.0 as `Objects.ToStringHelper.add()`).
            """
            ...


        def add(self, name: str, value: float) -> "ToStringHelper":
            """
            Adds a name/value pair to the formatted output in `name=value` format.

            Since
            - 18.0 (since 11.0 as `Objects.ToStringHelper.add()`).
            """
            ...


        def add(self, name: str, value: float) -> "ToStringHelper":
            """
            Adds a name/value pair to the formatted output in `name=value` format.

            Since
            - 18.0 (since 11.0 as `Objects.ToStringHelper.add()`).
            """
            ...


        def add(self, name: str, value: int) -> "ToStringHelper":
            """
            Adds a name/value pair to the formatted output in `name=value` format.

            Since
            - 18.0 (since 11.0 as `Objects.ToStringHelper.add()`).
            """
            ...


        def add(self, name: str, value: int) -> "ToStringHelper":
            """
            Adds a name/value pair to the formatted output in `name=value` format.

            Since
            - 18.0 (since 11.0 as `Objects.ToStringHelper.add()`).
            """
            ...


        def addValue(self, value: "Object") -> "ToStringHelper":
            """
            Adds an unnamed value to the formatted output.
            
            It is strongly encouraged to use .add(String, Object) instead and give value a
            readable name.
            """
            ...


        def addValue(self, value: bool) -> "ToStringHelper":
            """
            Adds an unnamed value to the formatted output.
            
            It is strongly encouraged to use .add(String, boolean) instead and give value a
            readable name.

            Since
            - 18.0 (since 11.0 as `Objects.ToStringHelper.addValue()`).
            """
            ...


        def addValue(self, value: str) -> "ToStringHelper":
            """
            Adds an unnamed value to the formatted output.
            
            It is strongly encouraged to use .add(String, char) instead and give value a
            readable name.

            Since
            - 18.0 (since 11.0 as `Objects.ToStringHelper.addValue()`).
            """
            ...


        def addValue(self, value: float) -> "ToStringHelper":
            """
            Adds an unnamed value to the formatted output.
            
            It is strongly encouraged to use .add(String, double) instead and give value a
            readable name.

            Since
            - 18.0 (since 11.0 as `Objects.ToStringHelper.addValue()`).
            """
            ...


        def addValue(self, value: float) -> "ToStringHelper":
            """
            Adds an unnamed value to the formatted output.
            
            It is strongly encouraged to use .add(String, float) instead and give value a
            readable name.

            Since
            - 18.0 (since 11.0 as `Objects.ToStringHelper.addValue()`).
            """
            ...


        def addValue(self, value: int) -> "ToStringHelper":
            """
            Adds an unnamed value to the formatted output.
            
            It is strongly encouraged to use .add(String, int) instead and give value a
            readable name.

            Since
            - 18.0 (since 11.0 as `Objects.ToStringHelper.addValue()`).
            """
            ...


        def addValue(self, value: int) -> "ToStringHelper":
            """
            Adds an unnamed value to the formatted output.
            
            It is strongly encouraged to use .add(String, long) instead and give value a
            readable name.

            Since
            - 18.0 (since 11.0 as `Objects.ToStringHelper.addValue()`).
            """
            ...


        def toString(self) -> str:
            """
            Returns a string in the format specified by MoreObjects.toStringHelper(Object).
            
            After calling this method, you can keep adding more properties to later call toString()
            again and get a more complete representation of the same object; but properties cannot be
            removed, so this only allows limited reuse of the helper instance. The helper allows
            duplication of properties (multiple name/value pairs with the same name can be added).
            """
            ...
