"""
Python module generated from Java source file java.io.PrintStream

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
from typing import Any, Callable, Iterable, Tuple


class PrintStream(FilterOutputStream, Appendable, Closeable):

    def __init__(self, out: "OutputStream"):
        """
        Creates a new print stream, without automatic line flushing, with the
        specified OutputStream. Characters written to the stream are converted
        to bytes using the platform's default character encoding.

        Arguments
        - out: The output stream to which values and objects will be
                           printed

        See
        - java.io.PrintWriter.PrintWriter(java.io.OutputStream)
        """
        ...


    def __init__(self, out: "OutputStream", autoFlush: bool):
        """
        Creates a new print stream, with the specified OutputStream and line
        flushing. Characters written to the stream are converted to bytes using
        the platform's default character encoding.

        Arguments
        - out: The output stream to which values and objects will be
                           printed
        - autoFlush: Whether the output buffer will be flushed
                           whenever a byte array is written, one of the
                           `println` methods is invoked, or a newline
                           character or byte (`'\n'`) is written

        See
        - java.io.PrintWriter.PrintWriter(java.io.OutputStream, boolean)
        """
        ...


    def __init__(self, out: "OutputStream", autoFlush: bool, encoding: str):
        """
        Creates a new print stream, with the specified OutputStream, line
        flushing, and character encoding.

        Arguments
        - out: The output stream to which values and objects will be
                           printed
        - autoFlush: Whether the output buffer will be flushed
                           whenever a byte array is written, one of the
                           `println` methods is invoked, or a newline
                           character or byte (`'\n'`) is written
        - encoding: The name of a supported
                           <a href="../lang/package-summary.html#charenc">
                           character encoding</a>

        Raises
        - UnsupportedEncodingException: If the named encoding is not supported

        Since
        - 1.4
        """
        ...


    def __init__(self, out: "OutputStream", autoFlush: bool, charset: "Charset"):
        """
        Creates a new print stream, with the specified OutputStream, line
        flushing and charset.  This convenience constructor creates the necessary
        intermediate java.io.OutputStreamWriter OutputStreamWriter,
        which will encode characters using the provided charset.

        Arguments
        - out: The output stream to which values and objects will be
                           printed
        - autoFlush: Whether the output buffer will be flushed
                           whenever a byte array is written, one of the
                           `println` methods is invoked, or a newline
                           character or byte (`'\n'`) is written
        - charset: A java.nio.charset.Charset charset

        Since
        - 10
        """
        ...


    def __init__(self, fileName: str):
        """
        Creates a new print stream, without automatic line flushing, with the
        specified file name.  This convenience constructor creates
        the necessary intermediate java.io.OutputStreamWriter
        OutputStreamWriter, which will encode characters using the
        java.nio.charset.Charset.defaultCharset() default charset
        for this instance of the Java virtual machine.

        Arguments
        - fileName: The name of the file to use as the destination of this print
                stream.  If the file exists, then it will be truncated to
                zero size; otherwise, a new file will be created.  The output
                will be written to the file and is buffered.

        Raises
        - FileNotFoundException: If the given file object does not denote an existing, writable
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
        Creates a new print stream, without automatic line flushing, with the
        specified file name and charset.  This convenience constructor creates
        the necessary intermediate java.io.OutputStreamWriter
        OutputStreamWriter, which will encode characters using the provided
        charset.

        Arguments
        - fileName: The name of the file to use as the destination of this print
                stream.  If the file exists, then it will be truncated to
                zero size; otherwise, a new file will be created.  The output
                will be written to the file and is buffered.
        - csn: The name of a supported java.nio.charset.Charset
                charset

        Raises
        - FileNotFoundException: If the given file object does not denote an existing, writable
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
        Creates a new print stream, without automatic line flushing, with the
        specified file name and charset.  This convenience constructor creates
        the necessary intermediate java.io.OutputStreamWriter
        OutputStreamWriter, which will encode characters using the provided
        charset.

        Arguments
        - fileName: The name of the file to use as the destination of this print
                stream.  If the file exists, then it will be truncated to
                zero size; otherwise, a new file will be created.  The output
                will be written to the file and is buffered.
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
        Creates a new print stream, without automatic line flushing, with the
        specified file.  This convenience constructor creates the necessary
        intermediate java.io.OutputStreamWriter OutputStreamWriter,
        which will encode characters using the java.nio.charset.Charset.defaultCharset() default charset for this
        instance of the Java virtual machine.

        Arguments
        - file: The file to use as the destination of this print stream.  If the
                file exists, then it will be truncated to zero size; otherwise,
                a new file will be created.  The output will be written to the
                file and is buffered.

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
        Creates a new print stream, without automatic line flushing, with the
        specified file and charset.  This convenience constructor creates
        the necessary intermediate java.io.OutputStreamWriter
        OutputStreamWriter, which will encode characters using the provided
        charset.

        Arguments
        - file: The file to use as the destination of this print stream.  If the
                file exists, then it will be truncated to zero size; otherwise,
                a new file will be created.  The output will be written to the
                file and is buffered.
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
        Creates a new print stream, without automatic line flushing, with the
        specified file and charset.  This convenience constructor creates
        the necessary intermediate java.io.OutputStreamWriter
        OutputStreamWriter, which will encode characters using the provided
        charset.

        Arguments
        - file: The file to use as the destination of this print stream.  If the
                file exists, then it will be truncated to zero size; otherwise,
                a new file will be created.  The output will be written to the
                file and is buffered.
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
        Flushes the stream.  This is done by writing any buffered output bytes to
        the underlying output stream and then flushing that stream.

        See
        - java.io.OutputStream.flush()
        """
        ...


    def close(self) -> None:
        """
        Closes the stream.  This is done by flushing the stream and then closing
        the underlying output stream.

        See
        - java.io.OutputStream.close()
        """
        ...


    def checkError(self) -> bool:
        """
        Flushes the stream and checks its error state. The internal error state
        is set to `True` when the underlying output stream throws an
        `IOException` other than `InterruptedIOException`,
        and when the `setError` method is invoked.  If an operation
        on the underlying output stream throws an
        `InterruptedIOException`, then the `PrintStream`
        converts the exception back into an interrupt by doing:
        ````Thread.currentThread().interrupt();````
        or the equivalent.

        Returns
        - `True` if and only if this stream has encountered an
                `IOException` other than
                `InterruptedIOException`, or the
                `setError` method has been invoked
        """
        ...


    def write(self, b: int) -> None:
        """
        Writes the specified byte to this stream.  If the byte is a newline and
        automatic flushing is enabled then the `flush` method will be
        invoked on the underlying output stream.
        
         Note that the byte is written as given; to write a character that
        will be translated according to the platform's default character
        encoding, use the `print(char)` or `println(char)`
        methods.

        Arguments
        - b: The byte to be written

        See
        - .println(char)
        """
        ...


    def write(self, buf: list[int], off: int, len: int) -> None:
        """
        Writes `len` bytes from the specified byte array starting at
        offset `off` to this stream.  If automatic flushing is
        enabled then the `flush` method will be invoked on the underlying
        output stream.
        
         Note that the bytes will be written as given; to write characters
        that will be translated according to the platform's default character
        encoding, use the `print(char)` or `println(char)`
        methods.

        Arguments
        - buf: A byte array
        - off: Offset from which to start taking bytes
        - len: Number of bytes to write
        """
        ...


    def write(self, buf: list[int]) -> None:
        """
        Writes all bytes from the specified byte array to this stream. If
        automatic flushing is enabled then the `flush` method will be
        invoked on the underlying output stream.
        
         Note that the bytes will be written as given; to write characters
        that will be translated according to the platform's default character
        encoding, use the `print(char[])` or `println(char[])`
        methods.

        Arguments
        - buf: A byte array

        Raises
        - IOException: If an I/O error occurs.

        See
        - .write(byte[],int,int)

        Since
        - 14

        Unknown Tags
        - Although declared to throw `IOException`, this method never
        actually does so. Instead, like other methods that this class
        overrides, it sets an internal flag which may be tested via the
        .checkError() method. To write an array of bytes without having
        to write a `catch` block for the `IOException`, use either
        .writeBytes(byte[] buf) writeBytes(buf) or
        .write(byte[], int, int) write(buf, 0, buf.length).
        - This method is equivalent to
        java.io.PrintStream.write(byte[],int,int)
        this.write(buf, 0, buf.length).
        """
        ...


    def writeBytes(self, buf: list[int]) -> None:
        """
        Writes all bytes from the specified byte array to this stream.
        If automatic flushing is enabled then the `flush` method
        will be invoked.
        
         Note that the bytes will be written as given; to write characters
        that will be translated according to the platform's default character
        encoding, use the `print(char[])` or `println(char[])`
        methods.

        Arguments
        - buf: A byte array

        Since
        - 14

        Unknown Tags
        - This method is equivalent to
        .write(byte[], int, int) this.write(buf, 0, buf.length).
        """
        ...


    def print(self, b: bool) -> None:
        """
        Prints a boolean value.  The string produced by java.lang.String.valueOf(boolean) is translated into bytes
        according to the platform's default character encoding, and these bytes
        are written in exactly the manner of the
        .write(int) method.

        Arguments
        - b: The `boolean` to be printed
        """
        ...


    def print(self, c: str) -> None:
        """
        Prints a character.  The character is translated into one or more bytes
        according to the character encoding given to the constructor, or the
        platform's default character encoding if none specified. These bytes
        are written in exactly the manner of the .write(int) method.

        Arguments
        - c: The `char` to be printed
        """
        ...


    def print(self, i: int) -> None:
        """
        Prints an integer.  The string produced by java.lang.String.valueOf(int) is translated into bytes
        according to the platform's default character encoding, and these bytes
        are written in exactly the manner of the
        .write(int) method.

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
        are written in exactly the manner of the
        .write(int) method.

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
        are written in exactly the manner of the
        .write(int) method.

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
        according to the character encoding given to the constructor, or the
        platform's default character encoding if none specified. These bytes
        are written in exactly the manner of the .write(int) method.

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
        converted into bytes according to the character encoding given to the
        constructor, or the platform's default character encoding if none
        specified. These bytes are written in exactly the manner of the
        .write(int) method.

        Arguments
        - s: The `String` to be printed
        """
        ...


    def print(self, obj: "Object") -> None:
        """
        Prints an object.  The string produced by the java.lang.String.valueOf(Object) method is translated into bytes
        according to the platform's default character encoding, and these bytes
        are written in exactly the manner of the
        .write(int) method.

        Arguments
        - obj: The `Object` to be printed

        See
        - java.lang.Object.toString()
        """
        ...


    def println(self) -> None:
        """
        Terminates the current line by writing the line separator string.  The
        line separator string is defined by the system property
        `line.separator`, and is not necessarily a single newline
        character (`'\n'`).
        """
        ...


    def println(self, x: bool) -> None:
        """
        Prints a boolean and then terminate the line.  This method behaves as
        though it invokes .print(boolean) and then
        .println().

        Arguments
        - x: The `boolean` to be printed
        """
        ...


    def println(self, x: str) -> None:
        """
        Prints a character and then terminate the line.  This method behaves as
        though it invokes .print(char) and then
        .println().

        Arguments
        - x: The `char` to be printed.
        """
        ...


    def println(self, x: int) -> None:
        """
        Prints an integer and then terminate the line.  This method behaves as
        though it invokes .print(int) and then
        .println().

        Arguments
        - x: The `int` to be printed.
        """
        ...


    def println(self, x: int) -> None:
        """
        Prints a long and then terminate the line.  This method behaves as
        though it invokes .print(long) and then
        .println().

        Arguments
        - x: a The `long` to be printed.
        """
        ...


    def println(self, x: float) -> None:
        """
        Prints a float and then terminate the line.  This method behaves as
        though it invokes .print(float) and then
        .println().

        Arguments
        - x: The `float` to be printed.
        """
        ...


    def println(self, x: float) -> None:
        """
        Prints a double and then terminate the line.  This method behaves as
        though it invokes .print(double) and then
        .println().

        Arguments
        - x: The `double` to be printed.
        """
        ...


    def println(self, x: list[str]) -> None:
        """
        Prints an array of characters and then terminate the line.  This method
        behaves as though it invokes .print(char[]) and
        then .println().

        Arguments
        - x: an array of chars to print.
        """
        ...


    def println(self, x: str) -> None:
        """
        Prints a String and then terminate the line.  This method behaves as
        though it invokes .print(String) and then
        .println().

        Arguments
        - x: The `String` to be printed.
        """
        ...


    def println(self, x: "Object") -> None:
        """
        Prints an Object and then terminate the line.  This method calls
        at first String.valueOf(x) to get the printed object's string value,
        then behaves as
        though it invokes .print(String) and then
        .println().

        Arguments
        - x: The `Object` to be printed.
        """
        ...


    def printf(self, format: str, *args: Tuple["Object", ...]) -> "PrintStream":
        """
        A convenience method to write a formatted string to this output stream
        using the specified format string and arguments.
        
         An invocation of this method of the form
        `out.printf(format, args)` behaves
        in exactly the same way as the invocation
        
        ````out.format(format, args)````

        Arguments
        - format: A format string as described in <a
                href="../util/Formatter.html#syntax">Format string syntax</a>
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
        - This output stream

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


    def printf(self, l: "Locale", format: str, *args: Tuple["Object", ...]) -> "PrintStream":
        """
        A convenience method to write a formatted string to this output stream
        using the specified format string and arguments.
        
         An invocation of this method of the form
        `out.printf(l, format, args)` behaves
        in exactly the same way as the invocation
        
        ````out.format(l, format, args)````

        Arguments
        - l: The java.util.Locale locale to apply during
                formatting.  If `l` is `null` then no localization
                is applied.
        - format: A format string as described in <a
                href="../util/Formatter.html#syntax">Format string syntax</a>
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
        - This output stream

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


    def format(self, format: str, *args: Tuple["Object", ...]) -> "PrintStream":
        """
        Writes a formatted string to this output stream using the specified
        format string and arguments.
        
         The locale always used is the one returned by java.util.Locale.getDefault(Locale.Category) with
        java.util.Locale.Category.FORMAT FORMAT category specified,
        regardless of any previous invocations of other formatting methods on
        this object.

        Arguments
        - format: A format string as described in <a
                href="../util/Formatter.html#syntax">Format string syntax</a>
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
        - This output stream

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


    def format(self, l: "Locale", format: str, *args: Tuple["Object", ...]) -> "PrintStream":
        """
        Writes a formatted string to this output stream using the specified
        format string and arguments.

        Arguments
        - l: The java.util.Locale locale to apply during
                formatting.  If `l` is `null` then no localization
                is applied.
        - format: A format string as described in <a
                href="../util/Formatter.html#syntax">Format string syntax</a>
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
        - This output stream

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


    def append(self, csq: "CharSequence") -> "PrintStream":
        """
        Appends the specified character sequence to this output stream.
        
         An invocation of this method of the form `out.append(csq)`
        behaves in exactly the same way as the invocation
        
        ````out.print(csq.toString())````
        
         Depending on the specification of `toString` for the
        character sequence `csq`, the entire sequence may not be
        appended.  For instance, invoking then `toString` method of a
        character buffer will return a subsequence whose content depends upon
        the buffer's position and limit.

        Arguments
        - csq: The character sequence to append.  If `csq` is
                `null`, then the four characters `"null"` are
                appended to this output stream.

        Returns
        - This output stream

        Since
        - 1.5
        """
        ...


    def append(self, csq: "CharSequence", start: int, end: int) -> "PrintStream":
        """
        Appends a subsequence of the specified character sequence to this output
        stream.
        
         An invocation of this method of the form
        `out.append(csq, start, end)` when
        `csq` is not `null`, behaves in
        exactly the same way as the invocation
        
        ````out.print(csq.subSequence(start, end).toString())````

        Arguments
        - csq: The character sequence from which a subsequence will be
                appended.  If `csq` is `null`, then characters
                will be appended as if `csq` contained the four
                characters `"null"`.
        - start: The index of the first character in the subsequence
        - end: The index of the character following the last character in the
                subsequence

        Returns
        - This output stream

        Raises
        - IndexOutOfBoundsException: If `start` or `end` are negative, `start`
                 is greater than `end`, or `end` is greater than
                 `csq.length()`

        Since
        - 1.5
        """
        ...


    def append(self, c: str) -> "PrintStream":
        """
        Appends the specified character to this output stream.
        
         An invocation of this method of the form `out.append(c)`
        behaves in exactly the same way as the invocation
        
        ````out.print(c)````

        Arguments
        - c: The 16-bit character to append

        Returns
        - This output stream

        Since
        - 1.5
        """
        ...
