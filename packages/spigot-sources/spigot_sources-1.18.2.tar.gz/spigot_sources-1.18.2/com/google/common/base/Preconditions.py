"""
Python module generated from Java source file com.google.common.base.Preconditions

Java source file obtained from artifact guava version 31.0.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.base import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from javax.annotation import CheckForNull
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class Preconditions:
    """
    Static convenience methods that help a method or constructor check whether it was invoked
    correctly (that is, whether its *preconditions* were met).
    
    If the precondition is not met, the `Preconditions` method throws an unchecked exception
    of a specified type, which helps the method in which the exception was thrown communicate that
    its caller has made a mistake. This allows constructs such as
    
    ````public static double sqrt(double value) {
      if (value < 0) {
        throw new IllegalArgumentException("input is negative: " + value);`
      // calculate square root
    }
    }```
    
    to be replaced with the more compact
    
    ````public static double sqrt(double value) {
      checkArgument(value >= 0, "input is negative: %s", value);
      // calculate square root`
    }```
    
    so that a hypothetical bad caller of this method, such as:
    
    ````void exampleBadCaller() {
      double d = sqrt(-1.0);`
    }```
    
    would be flagged as having called `sqrt()` with an illegal argument.
    
    <h3>Performance</h3>
    
    Avoid passing message arguments that are expensive to compute; your code will always compute
    them, even though they usually won't be needed. If you have such arguments, use the conventional
    if/throw idiom instead.
    
    Depending on your message arguments, memory may be allocated for boxing and varargs array
    creation. However, the methods of this class have a large number of overloads that prevent such
    allocations in many common cases.
    
    The message string is not formatted unless the exception will be thrown, so the cost of the
    string formatting itself should not be a concern.
    
    As with any performance concerns, you should consider profiling your code (in a production
    environment if possible) before spending a lot of effort on tweaking a particular element.
    
    <h3>Other types of preconditions</h3>
    
    Not every type of precondition failure is supported by these methods. Continue to throw
    standard JDK exceptions such as java.util.NoSuchElementException or UnsupportedOperationException in the situations they are intended for.
    
    <h3>Non-preconditions</h3>
    
    It is of course possible to use the methods of this class to check for invalid conditions
    which are *not the caller's fault*. Doing so is **not recommended** because it is
    misleading to future readers of the code and of stack traces. See <a
    href="https://github.com/google/guava/wiki/ConditionalFailuresExplained">Conditional failures
    explained</a> in the Guava User Guide for more advice. Notably, Verify offers assertions
    similar to those in this class for non-precondition checks.
    
    <h3>`java.util.Objects.requireNonNull()`</h3>
    
    Projects which use `com.google.common` should generally avoid the use of java.util.Objects.requireNonNull(Object). Instead, use whichever of .checkNotNull(Object) or Verify.verifyNotNull(Object) is appropriate to the situation.
    (The same goes for the message-accepting overloads.)
    
    <h3>Only `%s` is supported</h3>
    
    `Preconditions` uses Strings.lenientFormat to format error message template
    strings. This only supports the `"%s"` specifier, not the full range of java.util.Formatter specifiers. However, note that if the number of arguments does not match the
    number of occurrences of `"%s"` in the format string, `Preconditions` will still
    behave as expected, and will still include all argument values in the error message; the message
    will simply not be formatted exactly as intended.
    
    <h3>More information</h3>
    
    See the Guava User Guide on <a
    href="https://github.com/google/guava/wiki/PreconditionsExplained">using `Preconditions`</a>.

    Author(s)
    - Kevin Bourrillion

    Since
    - 2.0
    """

    @staticmethod
    def checkArgument(expression: bool) -> None:
        """
        Ensures the truth of an expression involving one or more parameters to the calling method.

        Arguments
        - expression: a boolean expression

        Raises
        - IllegalArgumentException: if `expression` is False
        """
        ...


    @staticmethod
    def checkArgument(expression: bool, errorMessage: "Object") -> None:
        """
        Ensures the truth of an expression involving one or more parameters to the calling method.

        Arguments
        - expression: a boolean expression
        - errorMessage: the exception message to use if the check fails; will be converted to a
            string using String.valueOf(Object)

        Raises
        - IllegalArgumentException: if `expression` is False
        """
        ...


    @staticmethod
    def checkArgument(expression: bool, errorMessageTemplate: str, *errorMessageArgs: Tuple["Object", ...]) -> None:
        """
        Ensures the truth of an expression involving one or more parameters to the calling method.

        Arguments
        - expression: a boolean expression
        - errorMessageTemplate: a template for the exception message should the check fail. The
            message is formed by replacing each `%s` placeholder in the template with an
            argument. These are matched by position - the first `%s` gets `errorMessageArgs[0]`, etc. Unmatched arguments will be appended to the formatted message in
            square braces. Unmatched placeholders will be left as-is.
        - errorMessageArgs: the arguments to be substituted into the message template. Arguments
            are converted to strings using String.valueOf(Object).

        Raises
        - IllegalArgumentException: if `expression` is False
        """
        ...


    @staticmethod
    def checkArgument(b: bool, errorMessageTemplate: str, p1: str) -> None:
        """
        Ensures the truth of an expression involving one or more parameters to the calling method.
        
        See .checkArgument(boolean, String, Object...) for details.

        Since
        - 20.0 (varargs overload since 2.0)
        """
        ...


    @staticmethod
    def checkArgument(b: bool, errorMessageTemplate: str, p1: int) -> None:
        """
        Ensures the truth of an expression involving one or more parameters to the calling method.
        
        See .checkArgument(boolean, String, Object...) for details.

        Since
        - 20.0 (varargs overload since 2.0)
        """
        ...


    @staticmethod
    def checkArgument(b: bool, errorMessageTemplate: str, p1: int) -> None:
        """
        Ensures the truth of an expression involving one or more parameters to the calling method.
        
        See .checkArgument(boolean, String, Object...) for details.

        Since
        - 20.0 (varargs overload since 2.0)
        """
        ...


    @staticmethod
    def checkArgument(b: bool, errorMessageTemplate: str, p1: "Object") -> None:
        """
        Ensures the truth of an expression involving one or more parameters to the calling method.
        
        See .checkArgument(boolean, String, Object...) for details.

        Since
        - 20.0 (varargs overload since 2.0)
        """
        ...


    @staticmethod
    def checkArgument(b: bool, errorMessageTemplate: str, p1: str, p2: str) -> None:
        """
        Ensures the truth of an expression involving one or more parameters to the calling method.
        
        See .checkArgument(boolean, String, Object...) for details.

        Since
        - 20.0 (varargs overload since 2.0)
        """
        ...


    @staticmethod
    def checkArgument(b: bool, errorMessageTemplate: str, p1: str, p2: int) -> None:
        """
        Ensures the truth of an expression involving one or more parameters to the calling method.
        
        See .checkArgument(boolean, String, Object...) for details.

        Since
        - 20.0 (varargs overload since 2.0)
        """
        ...


    @staticmethod
    def checkArgument(b: bool, errorMessageTemplate: str, p1: str, p2: int) -> None:
        """
        Ensures the truth of an expression involving one or more parameters to the calling method.
        
        See .checkArgument(boolean, String, Object...) for details.

        Since
        - 20.0 (varargs overload since 2.0)
        """
        ...


    @staticmethod
    def checkArgument(b: bool, errorMessageTemplate: str, p1: str, p2: "Object") -> None:
        """
        Ensures the truth of an expression involving one or more parameters to the calling method.
        
        See .checkArgument(boolean, String, Object...) for details.

        Since
        - 20.0 (varargs overload since 2.0)
        """
        ...


    @staticmethod
    def checkArgument(b: bool, errorMessageTemplate: str, p1: int, p2: str) -> None:
        """
        Ensures the truth of an expression involving one or more parameters to the calling method.
        
        See .checkArgument(boolean, String, Object...) for details.

        Since
        - 20.0 (varargs overload since 2.0)
        """
        ...


    @staticmethod
    def checkArgument(b: bool, errorMessageTemplate: str, p1: int, p2: int) -> None:
        """
        Ensures the truth of an expression involving one or more parameters to the calling method.
        
        See .checkArgument(boolean, String, Object...) for details.

        Since
        - 20.0 (varargs overload since 2.0)
        """
        ...


    @staticmethod
    def checkArgument(b: bool, errorMessageTemplate: str, p1: int, p2: int) -> None:
        """
        Ensures the truth of an expression involving one or more parameters to the calling method.
        
        See .checkArgument(boolean, String, Object...) for details.

        Since
        - 20.0 (varargs overload since 2.0)
        """
        ...


    @staticmethod
    def checkArgument(b: bool, errorMessageTemplate: str, p1: int, p2: "Object") -> None:
        """
        Ensures the truth of an expression involving one or more parameters to the calling method.
        
        See .checkArgument(boolean, String, Object...) for details.

        Since
        - 20.0 (varargs overload since 2.0)
        """
        ...


    @staticmethod
    def checkArgument(b: bool, errorMessageTemplate: str, p1: int, p2: str) -> None:
        """
        Ensures the truth of an expression involving one or more parameters to the calling method.
        
        See .checkArgument(boolean, String, Object...) for details.

        Since
        - 20.0 (varargs overload since 2.0)
        """
        ...


    @staticmethod
    def checkArgument(b: bool, errorMessageTemplate: str, p1: int, p2: int) -> None:
        """
        Ensures the truth of an expression involving one or more parameters to the calling method.
        
        See .checkArgument(boolean, String, Object...) for details.

        Since
        - 20.0 (varargs overload since 2.0)
        """
        ...


    @staticmethod
    def checkArgument(b: bool, errorMessageTemplate: str, p1: int, p2: int) -> None:
        """
        Ensures the truth of an expression involving one or more parameters to the calling method.
        
        See .checkArgument(boolean, String, Object...) for details.

        Since
        - 20.0 (varargs overload since 2.0)
        """
        ...


    @staticmethod
    def checkArgument(b: bool, errorMessageTemplate: str, p1: int, p2: "Object") -> None:
        """
        Ensures the truth of an expression involving one or more parameters to the calling method.
        
        See .checkArgument(boolean, String, Object...) for details.

        Since
        - 20.0 (varargs overload since 2.0)
        """
        ...


    @staticmethod
    def checkArgument(b: bool, errorMessageTemplate: str, p1: "Object", p2: str) -> None:
        """
        Ensures the truth of an expression involving one or more parameters to the calling method.
        
        See .checkArgument(boolean, String, Object...) for details.

        Since
        - 20.0 (varargs overload since 2.0)
        """
        ...


    @staticmethod
    def checkArgument(b: bool, errorMessageTemplate: str, p1: "Object", p2: int) -> None:
        """
        Ensures the truth of an expression involving one or more parameters to the calling method.
        
        See .checkArgument(boolean, String, Object...) for details.

        Since
        - 20.0 (varargs overload since 2.0)
        """
        ...


    @staticmethod
    def checkArgument(b: bool, errorMessageTemplate: str, p1: "Object", p2: int) -> None:
        """
        Ensures the truth of an expression involving one or more parameters to the calling method.
        
        See .checkArgument(boolean, String, Object...) for details.

        Since
        - 20.0 (varargs overload since 2.0)
        """
        ...


    @staticmethod
    def checkArgument(b: bool, errorMessageTemplate: str, p1: "Object", p2: "Object") -> None:
        """
        Ensures the truth of an expression involving one or more parameters to the calling method.
        
        See .checkArgument(boolean, String, Object...) for details.

        Since
        - 20.0 (varargs overload since 2.0)
        """
        ...


    @staticmethod
    def checkArgument(b: bool, errorMessageTemplate: str, p1: "Object", p2: "Object", p3: "Object") -> None:
        """
        Ensures the truth of an expression involving one or more parameters to the calling method.
        
        See .checkArgument(boolean, String, Object...) for details.

        Since
        - 20.0 (varargs overload since 2.0)
        """
        ...


    @staticmethod
    def checkArgument(b: bool, errorMessageTemplate: str, p1: "Object", p2: "Object", p3: "Object", p4: "Object") -> None:
        """
        Ensures the truth of an expression involving one or more parameters to the calling method.
        
        See .checkArgument(boolean, String, Object...) for details.

        Since
        - 20.0 (varargs overload since 2.0)
        """
        ...


    @staticmethod
    def checkState(expression: bool) -> None:
        """
        Ensures the truth of an expression involving the state of the calling instance, but not
        involving any parameters to the calling method.

        Arguments
        - expression: a boolean expression

        Raises
        - IllegalStateException: if `expression` is False

        See
        - Verify.verify Verify.verify()
        """
        ...


    @staticmethod
    def checkState(expression: bool, errorMessage: "Object") -> None:
        """
        Ensures the truth of an expression involving the state of the calling instance, but not
        involving any parameters to the calling method.

        Arguments
        - expression: a boolean expression
        - errorMessage: the exception message to use if the check fails; will be converted to a
            string using String.valueOf(Object)

        Raises
        - IllegalStateException: if `expression` is False

        See
        - Verify.verify Verify.verify()
        """
        ...


    @staticmethod
    def checkState(expression: bool, errorMessageTemplate: str, *errorMessageArgs: Tuple["Object", ...]) -> None:
        """
        Ensures the truth of an expression involving the state of the calling instance, but not
        involving any parameters to the calling method.

        Arguments
        - expression: a boolean expression
        - errorMessageTemplate: a template for the exception message should the check fail. The
            message is formed by replacing each `%s` placeholder in the template with an
            argument. These are matched by position - the first `%s` gets `errorMessageArgs[0]`, etc. Unmatched arguments will be appended to the formatted message in
            square braces. Unmatched placeholders will be left as-is.
        - errorMessageArgs: the arguments to be substituted into the message template. Arguments
            are converted to strings using String.valueOf(Object).

        Raises
        - IllegalStateException: if `expression` is False

        See
        - Verify.verify Verify.verify()
        """
        ...


    @staticmethod
    def checkState(b: bool, errorMessageTemplate: str, p1: str) -> None:
        """
        Ensures the truth of an expression involving the state of the calling instance, but not
        involving any parameters to the calling method.
        
        See .checkState(boolean, String, Object...) for details.

        Since
        - 20.0 (varargs overload since 2.0)
        """
        ...


    @staticmethod
    def checkState(b: bool, errorMessageTemplate: str, p1: int) -> None:
        """
        Ensures the truth of an expression involving the state of the calling instance, but not
        involving any parameters to the calling method.
        
        See .checkState(boolean, String, Object...) for details.

        Since
        - 20.0 (varargs overload since 2.0)
        """
        ...


    @staticmethod
    def checkState(b: bool, errorMessageTemplate: str, p1: int) -> None:
        """
        Ensures the truth of an expression involving the state of the calling instance, but not
        involving any parameters to the calling method.
        
        See .checkState(boolean, String, Object...) for details.

        Since
        - 20.0 (varargs overload since 2.0)
        """
        ...


    @staticmethod
    def checkState(b: bool, errorMessageTemplate: str, p1: "Object") -> None:
        """
        Ensures the truth of an expression involving the state of the calling instance, but not
        involving any parameters to the calling method.
        
        See .checkState(boolean, String, Object...) for details.

        Since
        - 20.0 (varargs overload since 2.0)
        """
        ...


    @staticmethod
    def checkState(b: bool, errorMessageTemplate: str, p1: str, p2: str) -> None:
        """
        Ensures the truth of an expression involving the state of the calling instance, but not
        involving any parameters to the calling method.
        
        See .checkState(boolean, String, Object...) for details.

        Since
        - 20.0 (varargs overload since 2.0)
        """
        ...


    @staticmethod
    def checkState(b: bool, errorMessageTemplate: str, p1: str, p2: int) -> None:
        """
        Ensures the truth of an expression involving the state of the calling instance, but not
        involving any parameters to the calling method.
        
        See .checkState(boolean, String, Object...) for details.

        Since
        - 20.0 (varargs overload since 2.0)
        """
        ...


    @staticmethod
    def checkState(b: bool, errorMessageTemplate: str, p1: str, p2: int) -> None:
        """
        Ensures the truth of an expression involving the state of the calling instance, but not
        involving any parameters to the calling method.
        
        See .checkState(boolean, String, Object...) for details.

        Since
        - 20.0 (varargs overload since 2.0)
        """
        ...


    @staticmethod
    def checkState(b: bool, errorMessageTemplate: str, p1: str, p2: "Object") -> None:
        """
        Ensures the truth of an expression involving the state of the calling instance, but not
        involving any parameters to the calling method.
        
        See .checkState(boolean, String, Object...) for details.

        Since
        - 20.0 (varargs overload since 2.0)
        """
        ...


    @staticmethod
    def checkState(b: bool, errorMessageTemplate: str, p1: int, p2: str) -> None:
        """
        Ensures the truth of an expression involving the state of the calling instance, but not
        involving any parameters to the calling method.
        
        See .checkState(boolean, String, Object...) for details.

        Since
        - 20.0 (varargs overload since 2.0)
        """
        ...


    @staticmethod
    def checkState(b: bool, errorMessageTemplate: str, p1: int, p2: int) -> None:
        """
        Ensures the truth of an expression involving the state of the calling instance, but not
        involving any parameters to the calling method.
        
        See .checkState(boolean, String, Object...) for details.

        Since
        - 20.0 (varargs overload since 2.0)
        """
        ...


    @staticmethod
    def checkState(b: bool, errorMessageTemplate: str, p1: int, p2: int) -> None:
        """
        Ensures the truth of an expression involving the state of the calling instance, but not
        involving any parameters to the calling method.
        
        See .checkState(boolean, String, Object...) for details.

        Since
        - 20.0 (varargs overload since 2.0)
        """
        ...


    @staticmethod
    def checkState(b: bool, errorMessageTemplate: str, p1: int, p2: "Object") -> None:
        """
        Ensures the truth of an expression involving the state of the calling instance, but not
        involving any parameters to the calling method.
        
        See .checkState(boolean, String, Object...) for details.

        Since
        - 20.0 (varargs overload since 2.0)
        """
        ...


    @staticmethod
    def checkState(b: bool, errorMessageTemplate: str, p1: int, p2: str) -> None:
        """
        Ensures the truth of an expression involving the state of the calling instance, but not
        involving any parameters to the calling method.
        
        See .checkState(boolean, String, Object...) for details.

        Since
        - 20.0 (varargs overload since 2.0)
        """
        ...


    @staticmethod
    def checkState(b: bool, errorMessageTemplate: str, p1: int, p2: int) -> None:
        """
        Ensures the truth of an expression involving the state of the calling instance, but not
        involving any parameters to the calling method.
        
        See .checkState(boolean, String, Object...) for details.

        Since
        - 20.0 (varargs overload since 2.0)
        """
        ...


    @staticmethod
    def checkState(b: bool, errorMessageTemplate: str, p1: int, p2: int) -> None:
        """
        Ensures the truth of an expression involving the state of the calling instance, but not
        involving any parameters to the calling method.
        
        See .checkState(boolean, String, Object...) for details.

        Since
        - 20.0 (varargs overload since 2.0)
        """
        ...


    @staticmethod
    def checkState(b: bool, errorMessageTemplate: str, p1: int, p2: "Object") -> None:
        """
        Ensures the truth of an expression involving the state of the calling instance, but not
        involving any parameters to the calling method.
        
        See .checkState(boolean, String, Object...) for details.

        Since
        - 20.0 (varargs overload since 2.0)
        """
        ...


    @staticmethod
    def checkState(b: bool, errorMessageTemplate: str, p1: "Object", p2: str) -> None:
        """
        Ensures the truth of an expression involving the state of the calling instance, but not
        involving any parameters to the calling method.
        
        See .checkState(boolean, String, Object...) for details.

        Since
        - 20.0 (varargs overload since 2.0)
        """
        ...


    @staticmethod
    def checkState(b: bool, errorMessageTemplate: str, p1: "Object", p2: int) -> None:
        """
        Ensures the truth of an expression involving the state of the calling instance, but not
        involving any parameters to the calling method.
        
        See .checkState(boolean, String, Object...) for details.

        Since
        - 20.0 (varargs overload since 2.0)
        """
        ...


    @staticmethod
    def checkState(b: bool, errorMessageTemplate: str, p1: "Object", p2: int) -> None:
        """
        Ensures the truth of an expression involving the state of the calling instance, but not
        involving any parameters to the calling method.
        
        See .checkState(boolean, String, Object...) for details.

        Since
        - 20.0 (varargs overload since 2.0)
        """
        ...


    @staticmethod
    def checkState(b: bool, errorMessageTemplate: str, p1: "Object", p2: "Object") -> None:
        """
        Ensures the truth of an expression involving the state of the calling instance, but not
        involving any parameters to the calling method.
        
        See .checkState(boolean, String, Object...) for details.

        Since
        - 20.0 (varargs overload since 2.0)
        """
        ...


    @staticmethod
    def checkState(b: bool, errorMessageTemplate: str, p1: "Object", p2: "Object", p3: "Object") -> None:
        """
        Ensures the truth of an expression involving the state of the calling instance, but not
        involving any parameters to the calling method.
        
        See .checkState(boolean, String, Object...) for details.

        Since
        - 20.0 (varargs overload since 2.0)
        """
        ...


    @staticmethod
    def checkState(b: bool, errorMessageTemplate: str, p1: "Object", p2: "Object", p3: "Object", p4: "Object") -> None:
        """
        Ensures the truth of an expression involving the state of the calling instance, but not
        involving any parameters to the calling method.
        
        See .checkState(boolean, String, Object...) for details.

        Since
        - 20.0 (varargs overload since 2.0)
        """
        ...


    @staticmethod
    def checkNotNull(reference: "T") -> "T":
        """
        Ensures that an object reference passed as a parameter to the calling method is not null.

        Arguments
        - reference: an object reference

        Returns
        - the non-null reference that was validated

        Raises
        - NullPointerException: if `reference` is null

        See
        - Verify.verifyNotNull Verify.verifyNotNull()
        """
        ...


    @staticmethod
    def checkNotNull(reference: "T", errorMessage: "Object") -> "T":
        """
        Ensures that an object reference passed as a parameter to the calling method is not null.

        Arguments
        - reference: an object reference
        - errorMessage: the exception message to use if the check fails; will be converted to a
            string using String.valueOf(Object)

        Returns
        - the non-null reference that was validated

        Raises
        - NullPointerException: if `reference` is null

        See
        - Verify.verifyNotNull Verify.verifyNotNull()
        """
        ...


    @staticmethod
    def checkNotNull(reference: "T", errorMessageTemplate: str, *errorMessageArgs: Tuple["Object", ...]) -> "T":
        """
        Ensures that an object reference passed as a parameter to the calling method is not null.

        Arguments
        - reference: an object reference
        - errorMessageTemplate: a template for the exception message should the check fail. The
            message is formed by replacing each `%s` placeholder in the template with an
            argument. These are matched by position - the first `%s` gets `errorMessageArgs[0]`, etc. Unmatched arguments will be appended to the formatted message in
            square braces. Unmatched placeholders will be left as-is.
        - errorMessageArgs: the arguments to be substituted into the message template. Arguments
            are converted to strings using String.valueOf(Object).

        Returns
        - the non-null reference that was validated

        Raises
        - NullPointerException: if `reference` is null

        See
        - Verify.verifyNotNull Verify.verifyNotNull()
        """
        ...


    @staticmethod
    def checkNotNull(obj: "T", errorMessageTemplate: str, p1: str) -> "T":
        """
        Ensures that an object reference passed as a parameter to the calling method is not null.
        
        See .checkNotNull(Object, String, Object...) for details.

        Since
        - 20.0 (varargs overload since 2.0)
        """
        ...


    @staticmethod
    def checkNotNull(obj: "T", errorMessageTemplate: str, p1: int) -> "T":
        """
        Ensures that an object reference passed as a parameter to the calling method is not null.
        
        See .checkNotNull(Object, String, Object...) for details.

        Since
        - 20.0 (varargs overload since 2.0)
        """
        ...


    @staticmethod
    def checkNotNull(obj: "T", errorMessageTemplate: str, p1: int) -> "T":
        """
        Ensures that an object reference passed as a parameter to the calling method is not null.
        
        See .checkNotNull(Object, String, Object...) for details.

        Since
        - 20.0 (varargs overload since 2.0)
        """
        ...


    @staticmethod
    def checkNotNull(obj: "T", errorMessageTemplate: str, p1: "Object") -> "T":
        """
        Ensures that an object reference passed as a parameter to the calling method is not null.
        
        See .checkNotNull(Object, String, Object...) for details.

        Since
        - 20.0 (varargs overload since 2.0)
        """
        ...


    @staticmethod
    def checkNotNull(obj: "T", errorMessageTemplate: str, p1: str, p2: str) -> "T":
        """
        Ensures that an object reference passed as a parameter to the calling method is not null.
        
        See .checkNotNull(Object, String, Object...) for details.

        Since
        - 20.0 (varargs overload since 2.0)
        """
        ...


    @staticmethod
    def checkNotNull(obj: "T", errorMessageTemplate: str, p1: str, p2: int) -> "T":
        """
        Ensures that an object reference passed as a parameter to the calling method is not null.
        
        See .checkNotNull(Object, String, Object...) for details.

        Since
        - 20.0 (varargs overload since 2.0)
        """
        ...


    @staticmethod
    def checkNotNull(obj: "T", errorMessageTemplate: str, p1: str, p2: int) -> "T":
        """
        Ensures that an object reference passed as a parameter to the calling method is not null.
        
        See .checkNotNull(Object, String, Object...) for details.

        Since
        - 20.0 (varargs overload since 2.0)
        """
        ...


    @staticmethod
    def checkNotNull(obj: "T", errorMessageTemplate: str, p1: str, p2: "Object") -> "T":
        """
        Ensures that an object reference passed as a parameter to the calling method is not null.
        
        See .checkNotNull(Object, String, Object...) for details.

        Since
        - 20.0 (varargs overload since 2.0)
        """
        ...


    @staticmethod
    def checkNotNull(obj: "T", errorMessageTemplate: str, p1: int, p2: str) -> "T":
        """
        Ensures that an object reference passed as a parameter to the calling method is not null.
        
        See .checkNotNull(Object, String, Object...) for details.

        Since
        - 20.0 (varargs overload since 2.0)
        """
        ...


    @staticmethod
    def checkNotNull(obj: "T", errorMessageTemplate: str, p1: int, p2: int) -> "T":
        """
        Ensures that an object reference passed as a parameter to the calling method is not null.
        
        See .checkNotNull(Object, String, Object...) for details.

        Since
        - 20.0 (varargs overload since 2.0)
        """
        ...


    @staticmethod
    def checkNotNull(obj: "T", errorMessageTemplate: str, p1: int, p2: int) -> "T":
        """
        Ensures that an object reference passed as a parameter to the calling method is not null.
        
        See .checkNotNull(Object, String, Object...) for details.

        Since
        - 20.0 (varargs overload since 2.0)
        """
        ...


    @staticmethod
    def checkNotNull(obj: "T", errorMessageTemplate: str, p1: int, p2: "Object") -> "T":
        """
        Ensures that an object reference passed as a parameter to the calling method is not null.
        
        See .checkNotNull(Object, String, Object...) for details.

        Since
        - 20.0 (varargs overload since 2.0)
        """
        ...


    @staticmethod
    def checkNotNull(obj: "T", errorMessageTemplate: str, p1: int, p2: str) -> "T":
        """
        Ensures that an object reference passed as a parameter to the calling method is not null.
        
        See .checkNotNull(Object, String, Object...) for details.

        Since
        - 20.0 (varargs overload since 2.0)
        """
        ...


    @staticmethod
    def checkNotNull(obj: "T", errorMessageTemplate: str, p1: int, p2: int) -> "T":
        """
        Ensures that an object reference passed as a parameter to the calling method is not null.
        
        See .checkNotNull(Object, String, Object...) for details.

        Since
        - 20.0 (varargs overload since 2.0)
        """
        ...


    @staticmethod
    def checkNotNull(obj: "T", errorMessageTemplate: str, p1: int, p2: int) -> "T":
        """
        Ensures that an object reference passed as a parameter to the calling method is not null.
        
        See .checkNotNull(Object, String, Object...) for details.

        Since
        - 20.0 (varargs overload since 2.0)
        """
        ...


    @staticmethod
    def checkNotNull(obj: "T", errorMessageTemplate: str, p1: int, p2: "Object") -> "T":
        """
        Ensures that an object reference passed as a parameter to the calling method is not null.
        
        See .checkNotNull(Object, String, Object...) for details.

        Since
        - 20.0 (varargs overload since 2.0)
        """
        ...


    @staticmethod
    def checkNotNull(obj: "T", errorMessageTemplate: str, p1: "Object", p2: str) -> "T":
        """
        Ensures that an object reference passed as a parameter to the calling method is not null.
        
        See .checkNotNull(Object, String, Object...) for details.

        Since
        - 20.0 (varargs overload since 2.0)
        """
        ...


    @staticmethod
    def checkNotNull(obj: "T", errorMessageTemplate: str, p1: "Object", p2: int) -> "T":
        """
        Ensures that an object reference passed as a parameter to the calling method is not null.
        
        See .checkNotNull(Object, String, Object...) for details.

        Since
        - 20.0 (varargs overload since 2.0)
        """
        ...


    @staticmethod
    def checkNotNull(obj: "T", errorMessageTemplate: str, p1: "Object", p2: int) -> "T":
        """
        Ensures that an object reference passed as a parameter to the calling method is not null.
        
        See .checkNotNull(Object, String, Object...) for details.

        Since
        - 20.0 (varargs overload since 2.0)
        """
        ...


    @staticmethod
    def checkNotNull(obj: "T", errorMessageTemplate: str, p1: "Object", p2: "Object") -> "T":
        """
        Ensures that an object reference passed as a parameter to the calling method is not null.
        
        See .checkNotNull(Object, String, Object...) for details.

        Since
        - 20.0 (varargs overload since 2.0)
        """
        ...


    @staticmethod
    def checkNotNull(obj: "T", errorMessageTemplate: str, p1: "Object", p2: "Object", p3: "Object") -> "T":
        """
        Ensures that an object reference passed as a parameter to the calling method is not null.
        
        See .checkNotNull(Object, String, Object...) for details.

        Since
        - 20.0 (varargs overload since 2.0)
        """
        ...


    @staticmethod
    def checkNotNull(obj: "T", errorMessageTemplate: str, p1: "Object", p2: "Object", p3: "Object", p4: "Object") -> "T":
        """
        Ensures that an object reference passed as a parameter to the calling method is not null.
        
        See .checkNotNull(Object, String, Object...) for details.

        Since
        - 20.0 (varargs overload since 2.0)
        """
        ...


    @staticmethod
    def checkElementIndex(index: int, size: int) -> int:
        """
        Ensures that `index` specifies a valid *element* in an array, list or string of size
        `size`. An element index may range from zero, inclusive, to `size`, exclusive.

        Arguments
        - index: a user-supplied index identifying an element of an array, list or string
        - size: the size of that array, list or string

        Returns
        - the value of `index`

        Raises
        - IndexOutOfBoundsException: if `index` is negative or is not less than `size`
        - IllegalArgumentException: if `size` is negative
        """
        ...


    @staticmethod
    def checkElementIndex(index: int, size: int, desc: str) -> int:
        """
        Ensures that `index` specifies a valid *element* in an array, list or string of size
        `size`. An element index may range from zero, inclusive, to `size`, exclusive.

        Arguments
        - index: a user-supplied index identifying an element of an array, list or string
        - size: the size of that array, list or string
        - desc: the text to use to describe this index in an error message

        Returns
        - the value of `index`

        Raises
        - IndexOutOfBoundsException: if `index` is negative or is not less than `size`
        - IllegalArgumentException: if `size` is negative
        """
        ...


    @staticmethod
    def checkPositionIndex(index: int, size: int) -> int:
        """
        Ensures that `index` specifies a valid *position* in an array, list or string of
        size `size`. A position index may range from zero to `size`, inclusive.

        Arguments
        - index: a user-supplied index identifying a position in an array, list or string
        - size: the size of that array, list or string

        Returns
        - the value of `index`

        Raises
        - IndexOutOfBoundsException: if `index` is negative or is greater than `size`
        - IllegalArgumentException: if `size` is negative
        """
        ...


    @staticmethod
    def checkPositionIndex(index: int, size: int, desc: str) -> int:
        """
        Ensures that `index` specifies a valid *position* in an array, list or string of
        size `size`. A position index may range from zero to `size`, inclusive.

        Arguments
        - index: a user-supplied index identifying a position in an array, list or string
        - size: the size of that array, list or string
        - desc: the text to use to describe this index in an error message

        Returns
        - the value of `index`

        Raises
        - IndexOutOfBoundsException: if `index` is negative or is greater than `size`
        - IllegalArgumentException: if `size` is negative
        """
        ...


    @staticmethod
    def checkPositionIndexes(start: int, end: int, size: int) -> None:
        """
        Ensures that `start` and `end` specify valid *positions* in an array, list or
        string of size `size`, and are in order. A position index may range from zero to `size`, inclusive.

        Arguments
        - start: a user-supplied index identifying a starting position in an array, list or string
        - end: a user-supplied index identifying an ending position in an array, list or string
        - size: the size of that array, list or string

        Raises
        - IndexOutOfBoundsException: if either index is negative or is greater than `size`,
            or if `end` is less than `start`
        - IllegalArgumentException: if `size` is negative
        """
        ...
