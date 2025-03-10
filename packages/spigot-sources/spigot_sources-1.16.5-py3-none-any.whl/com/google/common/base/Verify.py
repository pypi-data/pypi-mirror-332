"""
Python module generated from Java source file com.google.common.base.Verify

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.annotations import GwtCompatible
from com.google.common.base import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from javax.annotation import Nullable
from typing import Any, Callable, Iterable, Tuple


class Verify:
    """
    Static convenience methods that serve the same purpose as Java language
    <a href="http://docs.oracle.com/javase/7/docs/technotes/guides/language/assert.html">
    assertions</a>, except that they are always enabled. These methods should be used instead of Java
    assertions whenever there is a chance the check may fail "in real life". Example: ```   `Bill bill = remoteService.getLastUnpaidBill();
    
      // In case bug 12345 happens again we'd rather just die
      Verify.verify(bill.status() == Status.UNPAID,
          "Unexpected bill status: %s", bill.status());````
    
    <h3>Comparison to alternatives</h3>
    
    **Note:** In some cases the differences explained below can be subtle. When it's unclear
    which approach to use, **don't worry** too much about it; just pick something that seems
    reasonable and it will be fine.
    
    
    - If checking whether the *caller* has violated your method or constructor's contract
        (such as by passing an invalid argument), use the utilities of the Preconditions
        class instead.
    
    - If checking an *impossible* condition (which *cannot* happen unless your own class
        or its *trusted* dependencies is badly broken), this is what ordinary Java assertions
        are for. Note that assertions are not enabled by default; they are essentially considered
        "compiled comments."
    
    - An explicit `if/throw` (as illustrated below) is always acceptable; we still recommend
        using our VerifyException exception type. Throwing a plain RuntimeException
        is frowned upon.
    
    - Use of java.util.Objects.requireNonNull(Object) is generally discouraged, since
        .verifyNotNull(Object) and Preconditions.checkNotNull(Object) perform the
        same function with more clarity.
    
    
    <h3>Warning about performance</h3>
    
    Remember that parameter values for message construction must all be computed eagerly, and
    autoboxing and varargs array creation may happen as well, even when the verification succeeds and
    the message ends up unneeded. Performance-sensitive verification checks should continue to use
    usual form: ```   `Bill bill = remoteService.getLastUnpaidBill();
      if (bill.status() != Status.UNPAID) {
        throw new VerifyException("Unexpected bill status: " + bill.status());`}```
    
    <h3>Only `%s` is supported</h3>
    
    As with Preconditions error message template strings, only the `"%s"` specifier
    is supported, not the full range of java.util.Formatter specifiers. However, note that if
    the number of arguments does not match the number of occurrences of `"%s"` in the format
    string, `Verify` will still behave as expected, and will still include all argument values
    in the error message; the message will simply not be formatted exactly as intended.
    
    <h3>More information</h3>
    
    See <a href="https://github.com/google/guava/wiki/ConditionalFailuresExplained">Conditional
    failures explained</a> in the Guava User Guide for advice on when this class should be used.

    Since
    - 17.0
    """

    @staticmethod
    def verify(expression: bool) -> None:
        """
        Ensures that `expression` is `True`, throwing a `VerifyException` with no
        message otherwise.

        Raises
        - VerifyException: if `expression` is `False`
        """
        ...


    @staticmethod
    def verify(expression: bool, errorMessageTemplate: str, *errorMessageArgs: Tuple["Object", ...]) -> None:
        """
        Ensures that `expression` is `True`, throwing a `VerifyException` with a
        custom message otherwise.

        Arguments
        - expression: a boolean expression
        - errorMessageTemplate: a template for the exception message should the check fail. The
            message is formed by replacing each `%s` placeholder in the template with an
            argument. These are matched by position - the first `%s` gets
            `errorMessageArgs[0]`, etc. Unmatched arguments will be appended to the formatted
            message in square braces. Unmatched placeholders will be left as-is.
        - errorMessageArgs: the arguments to be substituted into the message template. Arguments
            are converted to strings using String.valueOf(Object).

        Raises
        - VerifyException: if `expression` is `False`
        """
        ...


    @staticmethod
    def verifyNotNull(reference: "T") -> "T":
        """
        Ensures that `reference` is non-null, throwing a `VerifyException` with a default
        message otherwise.

        Returns
        - `reference`, guaranteed to be non-null, for convenience

        Raises
        - VerifyException: if `reference` is `null`
        """
        ...


    @staticmethod
    def verifyNotNull(reference: "T", errorMessageTemplate: str, *errorMessageArgs: Tuple["Object", ...]) -> "T":
        """
        Ensures that `reference` is non-null, throwing a `VerifyException` with a custom
        message otherwise.

        Arguments
        - errorMessageTemplate: a template for the exception message should the check fail. The
            message is formed by replacing each `%s` placeholder in the template with an
            argument. These are matched by position - the first `%s` gets
            `errorMessageArgs[0]`, etc. Unmatched arguments will be appended to the formatted
            message in square braces. Unmatched placeholders will be left as-is.
        - errorMessageArgs: the arguments to be substituted into the message template. Arguments
            are converted to strings using String.valueOf(Object).

        Returns
        - `reference`, guaranteed to be non-null, for convenience

        Raises
        - VerifyException: if `reference` is `null`
        """
        ...
