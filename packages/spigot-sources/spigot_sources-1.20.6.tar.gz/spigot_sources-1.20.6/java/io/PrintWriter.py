"""
Python module generated from Java source file java.io.PrintWriter

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.io import *
from java.nio.charset import Charset
from java.nio.charset import IllegalCharsetNameException
from java.nio.charset import UnsupportedCharsetException
from java.util import Formatter
from java.util import Locale
from java.util import Objects
from typing import Any, Callable, Iterable, Tuple


class PrintWriter(Writer):

    def __init__(self, out: "Writer"):
        """
        Creates a new PrintWriter, without automatic line flushing.

        Arguments
        - out: A character-output stream
        """
        ...


    def __init__(self, out: "Writer", autoFlush: bool):
        """
        Creates a new PrintWriter.

        Arguments
        - out: A character-output stream
        - autoFlush: A boolean; if True, the `println`,
                           `printf`, or `format` methods will
                           flush the output buffer
        """
        ...


    def __init__(self, out: "OutputStream"):
        """
        Creates a new PrintWriter, without automatic line flushing, from an
        existing OutputStream.  This convenience constructor creates the
        necessary intermediate OutputStreamWriter, which will convert characters
        into bytes using the default character encoding.

        Arguments
        - out: An output stream

        See
        - java.io.OutputStreamWriter.OutputStreamWriter(java.io.OutputStream)
        """
        ...


    def __init__(self, out: "OutputStream", autoFlush: bool):
        """
        Creates a new PrintWriter from an existing OutputStream.  This
        convenience constructor creates the necessary intermediate
        OutputStreamWriter, which will convert characters into bytes using the
        default character encoding.

        Arguments
        - out: An output stream
        - autoFlush: A boolean; if True, the `println`,
                           `printf`, or `format` methods will
                           flush the output buffer

        See
        - java.io.OutputStreamWriter.OutputStreamWriter(java.io.OutputStream)
        """
        ...


    def __init__(self, out: "OutputStream", autoFlush: bool, charset: "Charset"):
        """
        Creates a new PrintWriter from an existing OutputStream.  This
        convenience constructor creates the necessary intermediate
        OutputStreamWriter, which will convert characters into bytes using the
        specified charset.

        Arguments
        - out: An output stream
        - autoFlush: A boolean; if True, the `println`,
                           `printf`, or `format` methods will
                           flush the output buffer
        - charset: A java.nio.charset.Charset charset

        Since
        - 10
        """
        ...


    def __init__(self, fileName: str):
        """
        Creates a new PrintWriter, without automatic line flushing, with the
        specified file name.  This convenience constructor creates the necessary
        intermediate java.io.OutputStreamWriter OutputStreamWriter,
        which will encode characters using the java.nio.charset.Charset.defaultCharset() default charset for this
        instance of the Java virtual machine.

        Arguments
        - fileName: The name of the file to use as the destination of this writer.
                If the file exists then it will be truncated to zero size;
                otherwise, a new file will be created.  The output will be
                written to the file and is buffered.

        Raises
        - FileNotFoundException: If the given string does not denote an existing, writable
                 regular file and a new regular file of that name cannot be
                 created, or if some other error occurs while opening or
                 creating the file
        - SecurityException: If a security manager is present and SecurityManager.checkWrite checkWrite(fileName) denies write
                 access to the file

        Since
        - 1.5
        """
        ...


    def __init__(self, fileName: str, csn: str):
        """
        Creates a new PrintWriter, without automatic line flushing, with the
        specified file name and charset.  This convenience constructor creates
        the necessary intermediate java.io.OutputStreamWriter
        OutputStreamWriter, which will encode characters using the provided
        charset.

        Arguments
        - fileName: The name of the file to use as the destination of this writer.
                If the file exists then it will be truncated to zero size;
                otherwise, a new file will be created.  The output will be
                written to the file and is buffered.
        - csn: The name of a supported java.nio.charset.Charset
                charset

        Raises
        - FileNotFoundException: If the given string does not denote an existing, writable
                 regular file and a new regular file of that name cannot be
                 created, or if some other error occurs while opening or
                 creating the file
        - SecurityException: If a security manager is present and SecurityManager.checkWrite checkWrite(fileName) denies write
                 access to the file
        - UnsupportedEncodingException: If the named charset is not supported

        Since
        - 1.5
        """
        ...


    def __init__(self, fileName: str, charset: "Charset"):
        """
        Creates a new PrintWriter, without automatic line flushing, with the
        specified file name and charset.  This convenience constructor creates
        the necessary intermediate java.io.OutputStreamWriter
        OutputStreamWriter, which will encode characters using the provided
        charset.

        Arguments
        - fileName: The name of the file to use as the destination of this writer.
                If the file exists then it will be truncated to zero size;
                otherwise, a new file will be created.  The output will be
                written to the file and is buffered.
        - charset: A java.nio.charset.Charset charset

        Raises
        - IOException: if an I/O error occurs while opening or creating the file
        - SecurityException: If a security manager is present and SecurityManager.checkWrite checkWrite(fileName) denies write
                 access to the file

        Since
        - 10
        """
        ...


    def __init__(self, file: "File"):
        """
        Creates a new PrintWriter, without automatic line flushing, with the
        specified file.  This convenience constructor creates the necessary
        intermediate java.io.OutputStreamWriter OutputStreamWriter,
        which will encode characters using the java.nio.charset.Charset.defaultCharset() default charset for this
        instance of the Java virtual machine.

        Arguments
        - file: The file to use as the destination of this writer.  If the file
                exists then it will be truncated to zero size; otherwise, a new
                file will be created.  The output will be written to the file
                and is buffered.

        Raises
        - FileNotFoundException: If the given file object does not denote an existing, writable
                 regular file and a new regular file of that name cannot be
                 created, or if some other error occurs while opening or
                 creating the file
        - SecurityException: If a security manager is present and SecurityManager.checkWrite checkWrite(file.getPath())
                 denies write access to the file

        Since
        - 1.5
        """
        ...


    def __init__(self, file: "File", csn: str):
        """
        Creates a new PrintWriter, without automatic line flushing, with the
        specified file and charset.  This convenience constructor creates the
        necessary intermediate java.io.OutputStreamWriter
        OutputStreamWriter, which will encode characters using the provided
        charset.

        Arguments
        - file: The file to use as the destination of this writer.  If the file
                exists then it will be truncated to zero size; otherwise, a new
                file will be created.  The output will be written to the file
                and is buffered.
        - csn: The name of a supported java.nio.charset.Charset
                charset

        Raises
        - FileNotFoundException: If the given file object does not denote an existing, writable
                 regular file and a new regular file of that name cannot be
                 created, or if some other error occurs while opening or
                 creating the file
        - SecurityException: If a security manager is present and SecurityManager.checkWrite checkWrite(file.getPath())
                 denies write access to the file
        - UnsupportedEncodingException: If the named charset is not supported

        Since
        - 1.5
        """
        ...


    def __init__(self, file: "File", charset: "Charset"):
        """
        Creates a new PrintWriter, without automatic line flushing, with the
        specified file and charset.  This convenience constructor creates the
        necessary intermediate java.io.OutputStreamWriter
        OutputStreamWriter, which will encode characters using the provided
        charset.

        Arguments
        - file: The file to use as the destination of this writer.  If the file
                exists then it will be truncated to zero size; otherwise, a new
                file will be created.  The output will be written to the file
                and is buffered.
        - charset: A java.nio.charset.Charset charset

        Raises
        - IOException: if an I/O error occurs while opening or creating the file
        - SecurityException: If a security manager is present and SecurityManager.checkWrite checkWrite(file.getPath())
                 denies write access to the file

        Since
        - 10
        """
        ...


    def flush(self) -> None:
        """
        Flushes the stream.

        See
        - .checkError()
        """
        ...


    def close(self) -> None:
        """
        Closes the stream and releases any system resources associated
        with it. Closing a previously closed stream has no effect.

        See
        - .checkError()
        """
        ...


    def checkError(self) -> bool:
        """
        Flushes the stream if it's not closed and checks its error state.

        Returns
        - `True` if the print stream has encountered an error,
                 either on the underlying output stream or during a format
                 conversion.
        """
        ...


    def write(self, c: int) -> None:
        """
        Writes a single character.

        Arguments
        - c: int specifying a character to be written.
        """
        ...


    def write(self, buf: list[str], off: int, len: int) -> None:
        """
        Writes A Portion of an array of characters.

        Arguments
        - buf: Array of characters
        - off: Offset from which to start writing characters
        - len: Number of characters to write

        Raises
        - IndexOutOfBoundsException: If the values of the `off` and `len` parameters
                 cause the corresponding method of the underlying `Writer`
                 to throw an `IndexOutOfBoundsException`
        """
        ...


    def write(self, buf: list[str]) -> None:
        """
        Writes an array of characters.  This method cannot be inherited from the
        Writer class because it must suppress I/O exceptions.

        Arguments
        - buf: Array of characters to be written
        """
        ...


    def write(self, s: str, off: int, len: int) -> None:
        """
        Writes a portion of a string.

        Arguments
        - s: A String
        - off: Offset from which to start writing characters
        - len: Number of characters to write

        Raises
        - IndexOutOfBoundsException: If the values of the `off` and `len` parameters
                 cause the corresponding method of the underlying `Writer`
                 to throw an `IndexOutOfBoundsException`
        """
        ...


    def write(self, s: str) -> None:
        """
        Writes a string.  This method cannot be inherited from the Writer class
        because it must suppress I/O exceptions.

        Arguments
        - s: String to be written
        """
        ...


    def print(self, b: bool) -> None:
        """
        Prints a boolean value.  The string produced by java.lang.String.valueOf(boolean) is translated into bytes
        according to the platform's default character encoding, and these bytes
        are written in exactly the manner of the .write(int) method.

        Arguments
        - b: The `boolean` to be printed
        """
        ...


    def print(self, c: str) -> None:
        """
        Prints a character.  The character is translated into one or more bytes
        according to the platform's default character encoding, and these bytes
        are written in exactly the manner of the .write(int) method.

        Arguments
        - c: The `char` to be printed
        """
        ...


    def print(self, i: int) -> None:
        """
        Prints an integer.  The string produced by java.lang.String.valueOf(int) is translated into bytes according
        to the platform's default character encoding, and these bytes are
        written in exactly the manner of the .write(int)
        method.

        Arguments
        - i: The `int` to be printed

        See
        - java.lang.Integer.toString(int)
        """
        ...


    def print(self, l: int) -> None:
        """
        Prints a long integer.  The string produced by java.lang.String.valueOf(long) is translated into bytes
        according to the platform's default character encoding, and these bytes
        are written in exactly the manner of the .write(int)
        method.

        Arguments
        - l: The `long` to be printed

        See
        - java.lang.Long.toString(long)
        """
        ...


    def print(self, f: float) -> None:
        """
        Prints a floating-point number.  The string produced by java.lang.String.valueOf(float) is translated into bytes
        according to the platform's default character encoding, and these bytes
        are written in exactly the manner of the .write(int)
        method.

        Arguments
        - f: The `float` to be printed

        See
        - java.lang.Float.toString(float)
        """
        ...


    def print(self, d: float) -> None:
        """
        Prints a double-precision floating-point number.  The string produced by
        java.lang.String.valueOf(double) is translated into
        bytes according to the platform's default character encoding, and these
        bytes are written in exactly the manner of the .write(int) method.

        Arguments
        - d: The `double` to be printed

        See
        - java.lang.Double.toString(double)
        """
        ...


    def print(self, s: list[str]) -> None:
        """
        Prints an array of characters.  The characters are converted into bytes
        according to the platform's default character encoding, and these bytes
        are written in exactly the manner of the .write(int)
        method.

        Arguments
        - s: The array of chars to be printed

        Raises
        - NullPointerException: If `s` is `null`
        """
        ...


    def print(self, s: str) -> None:
        """
        Prints a string.  If the argument is `null` then the string
        `"null"` is printed.  Otherwise, the string's characters are
        converted into bytes according to the platform's default character
        encoding, and these bytes are written in exactly the manner of the
        .write(int) method.

        Arguments
        - s: The `String` to be printed
        """
        ...


    def print(self, obj: "Object") -> None:
        """
        Prints an object.  The string produced by the java.lang.String.valueOf(Object) method is translated into bytes
        according to the platform's default character encoding, and these bytes
        are written in exactly the manner of the .write(int)
        method.

        Arguments
        - obj: The `Object` to be printed

        See
        - java.lang.Object.toString()
        """
        ...


    def println(self) -> None:
        """
        Terminates the current line by writing the line separator string.  The
        line separator is System.lineSeparator() and is not necessarily
        a single newline character (`'\n'`).
        """
        ...


    def println(self, x: bool) -> None:
        """
        Prints a boolean value and then terminates the line.  This method behaves
        as though it invokes .print(boolean) and then
        .println().

        Arguments
        - x: the `boolean` value to be printed
        """
        ...


    def println(self, x: str) -> None:
        """
        Prints a character and then terminates the line.  This method behaves as
        though it invokes .print(char) and then .println().

        Arguments
        - x: the `char` value to be printed
        """
        ...


    def println(self, x: int) -> None:
        """
        Prints an integer and then terminates the line.  This method behaves as
        though it invokes .print(int) and then .println().

        Arguments
        - x: the `int` value to be printed
        """
        ...


    def println(self, x: int) -> None:
        """
        Prints a long integer and then terminates the line.  This method behaves
        as though it invokes .print(long) and then
        .println().

        Arguments
        - x: the `long` value to be printed
        """
        ...


    def println(self, x: float) -> None:
        """
        Prints a floating-point number and then terminates the line.  This method
        behaves as though it invokes .print(float) and then
        .println().

        Arguments
        - x: the `float` value to be printed
        """
        ...


    def println(self, x: float) -> None:
        """
        Prints a double-precision floating-point number and then terminates the
        line.  This method behaves as though it invokes .print(double) and then .println().

        Arguments
        - x: the `double` value to be printed
        """
        ...


    def println(self, x: list[str]) -> None:
        """
        Prints an array of characters and then terminates the line.  This method
        behaves as though it invokes .print(char[]) and then
        .println().

        Arguments
        - x: the array of `char` values to be printed
        """
        ...


    def println(self, x: str) -> None:
        """
        Prints a String and then terminates the line.  This method behaves as
        though it invokes .print(String) and then
        .println().

        Arguments
        - x: the `String` value to be printed
        """
        ...


    def println(self, x: "Object") -> None:
        """
        Prints an Object and then terminates the line.  This method calls
        at first String.valueOf(x) to get the printed object's string value,
        then behaves as
        though it invokes .print(String) and then
        .println().

        Arguments
        - x: The `Object` to be printed.
        """
        ...


    def printf(self, format: str, *args: Tuple["Object", ...]) -> "PrintWriter":
        """
        A convenience method to write a formatted string to this writer using
        the specified format string and arguments.  If automatic flushing is
        enabled, calls to this method will flush the output buffer.
        
         An invocation of this method of the form
        `out.printf(format, args)`
        behaves in exactly the same way as the invocation
        
        ````out.format(format, args)````

        Arguments
        - format: A format string as described in <a
                href="../util/Formatter.html#syntax">Format string syntax</a>.
        - args: Arguments referenced by the format specifiers in the format
                string.  If there are more arguments than format specifiers, the
                extra arguments are ignored.  The number of arguments is
                variable and may be zero.  The maximum number of arguments is
                limited by the maximum dimension of a Java array as defined by
                <cite>The Java Virtual Machine Specification</cite>.
                The behaviour on a
                `null` argument depends on the <a
                href="../util/Formatter.html#syntax">conversion</a>.

        Returns
        - This writer

        Raises
        - java.util.IllegalFormatException: If a format string contains an illegal syntax, a format
                 specifier that is incompatible with the given arguments,
                 insufficient arguments given the format string, or other
                 illegal conditions.  For specification of all possible
                 formatting errors, see the <a
                 href="../util/Formatter.html#detail">Details</a> section of the
                 formatter class specification.
        - NullPointerException: If the `format` is `null`

        Since
        - 1.5
        """
        ...


    def printf(self, l: "Locale", format: str, *args: Tuple["Object", ...]) -> "PrintWriter":
        """
        A convenience method to write a formatted string to this writer using
        the specified format string and arguments.  If automatic flushing is
        enabled, calls to this method will flush the output buffer.
        
         An invocation of this method of the form
        `out.printf(l, format, args)`
        behaves in exactly the same way as the invocation
        
        ````out.format(l, format, args)````

        Arguments
        - l: The java.util.Locale locale to apply during
                formatting.  If `l` is `null` then no localization
                is applied.
        - format: A format string as described in <a
                href="../util/Formatter.html#syntax">Format string syntax</a>.
        - args: Arguments referenced by the format specifiers in the format
                string.  If there are more arguments than format specifiers, the
                extra arguments are ignored.  The number of arguments is
                variable and may be zero.  The maximum number of arguments is
                limited by the maximum dimension of a Java array as defined by
                <cite>The Java Virtual Machine Specification</cite>.
                The behaviour on a
                `null` argument depends on the <a
                href="../util/Formatter.html#syntax">conversion</a>.

        Returns
        - This writer

        Raises
        - java.util.IllegalFormatException: If a format string contains an illegal syntax, a format
                 specifier that is incompatible with the given arguments,
                 insufficient arguments given the format string, or other
                 illegal conditions.  For specification of all possible
                 formatting errors, see the <a
                 href="../util/Formatter.html#detail">Details</a> section of the
                 formatter class specification.
        - NullPointerException: If the `format` is `null`

        Since
        - 1.5
        """
        ...


    def format(self, format: str, *args: Tuple["Object", ...]) -> "PrintWriter":
        """
        Writes a formatted string to this writer using the specified format
        string and arguments.  If automatic flushing is enabled, calls to this
        method will flush the output buffer.
        
         The locale always used is the one returned by java.util.Locale.getDefault() Locale.getDefault(), regardless of any
        previous invocations of other formatting methods on this object.

        Arguments
        - format: A format string as described in <a
                href="../util/Formatter.html#syntax">Format string syntax</a>.
        - args: Arguments referenced by the format specifiers in the format
                string.  If there are more arguments than format specifiers, the
                extra arguments are ignored.  The number of arguments is
                variable and may be zero.  The maximum number of arguments is
                limited by the maximum dimension of a Java array as defined by
                <cite>The Java Virtual Machine Specification</cite>.
                The behaviour on a
                `null` argument depends on the <a
                href="../util/Formatter.html#syntax">conversion</a>.

        Returns
        - This writer

        Raises
        - java.util.IllegalFormatException: If a format string contains an illegal syntax, a format
                 specifier that is incompatible with the given arguments,
                 insufficient arguments given the format string, or other
                 illegal conditions.  For specification of all possible
                 formatting errors, see the <a
                 href="../util/Formatter.html#detail">Details</a> section of the
                 Formatter class specification.
        - NullPointerException: If the `format` is `null`

        Since
        - 1.5
        """
        ...


    def format(self, l: "Locale", format: str, *args: Tuple["Object", ...]) -> "PrintWriter":
        """
        Writes a formatted string to this writer using the specified format
        string and arguments.  If automatic flushing is enabled, calls to this
        method will flush the output buffer.

        Arguments
        - l: The java.util.Locale locale to apply during
                formatting.  If `l` is `null` then no localization
                is applied.
        - format: A format string as described in <a
                href="../util/Formatter.html#syntax">Format string syntax</a>.
        - args: Arguments referenced by the format specifiers in the format
                string.  If there are more arguments than format specifiers, the
                extra arguments are ignored.  The number of arguments is
                variable and may be zero.  The maximum number of arguments is
                limited by the maximum dimension of a Java array as defined by
                <cite>The Java Virtual Machine Specification</cite>.
                The behaviour on a
                `null` argument depends on the <a
                href="../util/Formatter.html#syntax">conversion</a>.

        Returns
        - This writer

        Raises
        - java.util.IllegalFormatException: If a format string contains an illegal syntax, a format
                 specifier that is incompatible with the given arguments,
                 insufficient arguments given the format string, or other
                 illegal conditions.  For specification of all possible
                 formatting errors, see the <a
                 href="../util/Formatter.html#detail">Details</a> section of the
                 formatter class specification.
        - NullPointerException: If the `format` is `null`

        Since
        - 1.5
        """
        ...


    def append(self, csq: "CharSequence") -> "PrintWriter":
        """
        Appends the specified character sequence to this writer.
        
         An invocation of this method of the form `out.append(csq)`
        behaves in exactly the same way as the invocation
        
        ````out.write(csq.toString())````
        
         Depending on the specification of `toString` for the
        character sequence `csq`, the entire sequence may not be
        appended. For instance, invoking the `toString` method of a
        character buffer will return a subsequence whose content depends upon
        the buffer's position and limit.

        Arguments
        - csq: The character sequence to append.  If `csq` is
                `null`, then the four characters `"null"` are
                appended to this writer.

        Returns
        - This writer

        Since
        - 1.5
        """
        ...


    def append(self, csq: "CharSequence", start: int, end: int) -> "PrintWriter":
        """
        Appends a subsequence of the specified character sequence to this writer.
        
         An invocation of this method of the form
        `out.append(csq, start, end)`
        when `csq` is not `null`, behaves in
        exactly the same way as the invocation
        
        ````out.write(csq.subSequence(start, end).toString())````

        Arguments
        - csq: The character sequence from which a subsequence will be
                appended.  If `csq` is `null`, then characters
                will be appended as if `csq` contained the four
                characters `"null"`.
        - start: The index of the first character in the subsequence
        - end: The index of the character following the last character in the
                subsequence

        Returns
        - This writer

        Raises
        - IndexOutOfBoundsException: If `start` or `end` are negative, `start`
                 is greater than `end`, or `end` is greater than
                 `csq.length()`

        Since
        - 1.5
        """
        ...


    def append(self, c: str) -> "PrintWriter":
        """
        Appends the specified character to this writer.
        
         An invocation of this method of the form `out.append(c)`
        behaves in exactly the same way as the invocation
        
        ````out.write(c)````

        Arguments
        - c: The 16-bit character to append

        Returns
        - This writer

        Since
        - 1.5
        """
        ...
