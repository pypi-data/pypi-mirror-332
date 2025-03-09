"""
Python module generated from Java source file java.util.jar.Manifest

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.io import DataOutputStream
from java.io import FilterInputStream
from java.io import IOException
from java.io import InputStream
from java.io import OutputStream
from java.util.jar import *
from sun.nio.cs import UTF_8
from sun.security.util import SecurityProperties
from typing import Any, Callable, Iterable, Tuple


class Manifest(Cloneable):
    """
    The Manifest class is used to maintain Manifest entry names and their
    associated Attributes. There are main Manifest Attributes as well as
    per-entry Attributes. For information on the Manifest format, please
    see the
    <a href="/../specs/jar/jar.html">
    Manifest format specification</a>.

    Author(s)
    - David Connelly

    See
    - Attributes

    Since
    - 1.2
    """

    def __init__(self):
        """
        Constructs a new, empty Manifest.
        """
        ...


    def __init__(self, is: "InputStream"):
        """
        Constructs a new Manifest from the specified input stream.

        Arguments
        - is: the input stream containing manifest data

        Raises
        - IOException: if an I/O error has occurred
        """
        ...


    def __init__(self, man: "Manifest"):
        """
        Constructs a new Manifest that is a copy of the specified Manifest.

        Arguments
        - man: the Manifest to copy
        """
        ...


    def getMainAttributes(self) -> "Attributes":
        """
        Returns the main Attributes for the Manifest.

        Returns
        - the main Attributes for the Manifest
        """
        ...


    def getEntries(self) -> dict[str, "Attributes"]:
        """
        Returns a Map of the entries contained in this Manifest. Each entry
        is represented by a String name (key) and associated Attributes (value).
        The Map permits the `null` key, but no entry with a null key is
        created by .read, nor is such an entry written by using .write.

        Returns
        - a Map of the entries contained in this Manifest
        """
        ...


    def getAttributes(self, name: str) -> "Attributes":
        """
        Returns the Attributes for the specified entry name.
        This method is defined as:
        ```
             return (Attributes)getEntries().get(name)
        ```
        Though `null` is a valid `name`, when
        `getAttributes(null)` is invoked on a `Manifest`
        obtained from a jar file, `null` will be returned.  While jar
        files themselves do not allow `null`-named attributes, it is
        possible to invoke .getEntries on a `Manifest`, and
        on that result, invoke `put` with a null key and an
        arbitrary value.  Subsequent invocations of
        `getAttributes(null)` will return the just-`put`
        value.
        
        Note that this method does not return the manifest's main attributes;
        see .getMainAttributes.

        Arguments
        - name: entry name

        Returns
        - the Attributes for the specified entry name
        """
        ...


    def clear(self) -> None:
        """
        Clears the main Attributes as well as the entries in this Manifest.
        """
        ...


    def write(self, out: "OutputStream") -> None:
        """
        Writes the Manifest to the specified OutputStream.
        Attributes.Name.MANIFEST_VERSION must be set in
        MainAttributes prior to invoking this method.

        Arguments
        - out: the output stream

        Raises
        - IOException: if an I/O error has occurred

        See
        - .getMainAttributes
        """
        ...


    def read(self, is: "InputStream") -> None:
        """
        Reads the Manifest from the specified InputStream. The entry
        names and attributes read will be merged in with the current
        manifest entries.

        Arguments
        - is: the input stream

        Raises
        - IOException: if an I/O error has occurred
        """
        ...


    def equals(self, o: "Object") -> bool:
        """
        Returns True if the specified Object is also a Manifest and has
        the same main Attributes and entries.

        Arguments
        - o: the object to be compared

        Returns
        - True if the specified Object is also a Manifest and has
        the same main Attributes and entries
        """
        ...


    def hashCode(self) -> int:
        """
        Returns the hash code for this Manifest.
        """
        ...


    def clone(self) -> "Object":
        """
        Returns a shallow copy of this Manifest.  The shallow copy is
        implemented as follows:
        ```
            public Object clone() { return new Manifest(this); }
        ```

        Returns
        - a shallow copy of this Manifest
        """
        ...
