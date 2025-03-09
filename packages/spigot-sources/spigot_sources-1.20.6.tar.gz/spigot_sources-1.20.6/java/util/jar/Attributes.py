"""
Python module generated from Java source file java.util.jar.Attributes

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.io import ByteArrayOutputStream
from java.io import DataOutputStream
from java.io import IOException
from java.util import Objects
from java.util.jar import *
from jdk.internal.misc import CDS
from jdk.internal.vm.annotation import Stable
from sun.nio.cs import UTF_8
from sun.util.logging import PlatformLogger
from typing import Any, Callable, Iterable, Tuple


class Attributes(Map, Cloneable):
    """
    The Attributes class maps Manifest attribute names to associated string
    values. Valid attribute names are case-insensitive, are restricted to
    the ASCII characters in the set [0-9a-zA-Z_-], and cannot exceed 70
    characters in length. There must be a colon and a SPACE after the name;
    the combined length will not exceed 72 characters.
    Attribute values can contain any characters and
    will be UTF8-encoded when written to the output stream.  See the
    <a href="/../specs/jar/jar.html">JAR File Specification</a>
    for more information about valid attribute names and values.
    
    This map and its views have a predictable iteration order, namely the
    order that keys were inserted into the map, as with LinkedHashMap.

    Author(s)
    - David Connelly

    See
    - Manifest

    Since
    - 1.2
    """

    def __init__(self):
        """
        Constructs a new, empty Attributes object with default size.
        """
        ...


    def __init__(self, size: int):
        """
        Constructs a new, empty Attributes object with the specified
        initial size.

        Arguments
        - size: the initial number of attributes
        """
        ...


    def __init__(self, attr: "Attributes"):
        """
        Constructs a new Attributes object with the same attribute name-value
        mappings as in the specified Attributes.

        Arguments
        - attr: the specified Attributes
        """
        ...


    def get(self, name: "Object") -> "Object":
        """
        Returns the value of the specified attribute name, or null if the
        attribute name was not found.

        Arguments
        - name: the attribute name

        Returns
        - the value of the specified attribute name, or null if
                not found.
        """
        ...


    def getValue(self, name: str) -> str:
        """
        Returns the value of the specified attribute name, specified as
        a string, or null if the attribute was not found. The attribute
        name is case-insensitive.
        
        This method is defined as:
        ```
             return (String)get(new Attributes.Name((String)name));
        ```

        Arguments
        - name: the attribute name as a string

        Returns
        - the String value of the specified attribute name, or null if
                not found.

        Raises
        - IllegalArgumentException: if the attribute name is invalid
        """
        ...


    def getValue(self, name: "Name") -> str:
        """
        Returns the value of the specified Attributes.Name, or null if the
        attribute was not found.
        
        This method is defined as:
        ```
            return (String)get(name);
        ```

        Arguments
        - name: the Attributes.Name object

        Returns
        - the String value of the specified Attribute.Name, or null if
                not found.
        """
        ...


    def put(self, name: "Object", value: "Object") -> "Object":
        """
        Associates the specified value with the specified attribute name
        (key) in this Map. If the Map previously contained a mapping for
        the attribute name, the old value is replaced.

        Arguments
        - name: the attribute name
        - value: the attribute value

        Returns
        - the previous value of the attribute, or null if none

        Raises
        - ClassCastException: if the name is not a Attributes.Name
                   or the value is not a String
        """
        ...


    def putValue(self, name: str, value: str) -> str:
        """
        Associates the specified value with the specified attribute name,
        specified as a String. The attributes name is case-insensitive.
        If the Map previously contained a mapping for the attribute name,
        the old value is replaced.
        
        This method is defined as:
        ```
             return (String)put(new Attributes.Name(name), value);
        ```

        Arguments
        - name: the attribute name as a string
        - value: the attribute value

        Returns
        - the previous value of the attribute, or null if none

        Raises
        - IllegalArgumentException: if the attribute name is invalid
        """
        ...


    def remove(self, name: "Object") -> "Object":
        """
        Removes the attribute with the specified name (key) from this Map.
        Returns the previous attribute value, or null if none.

        Arguments
        - name: attribute name

        Returns
        - the previous value of the attribute, or null if none
        """
        ...


    def containsValue(self, value: "Object") -> bool:
        """
        Returns True if this Map maps one or more attribute names (keys)
        to the specified value.

        Arguments
        - value: the attribute value

        Returns
        - True if this Map maps one or more attribute names to
                the specified value
        """
        ...


    def containsKey(self, name: "Object") -> bool:
        """
        Returns True if this Map contains the specified attribute name (key).

        Arguments
        - name: the attribute name

        Returns
        - True if this Map contains the specified attribute name
        """
        ...


    def putAll(self, attr: dict[Any, Any]) -> None:
        """
        Copies all of the attribute name-value mappings from the specified
        Attributes to this Map. Duplicate mappings will be replaced.

        Arguments
        - attr: the Attributes to be stored in this map

        Raises
        - ClassCastException: if attr is not an Attributes
        """
        ...


    def clear(self) -> None:
        """
        Removes all attributes from this Map.
        """
        ...


    def size(self) -> int:
        """
        Returns the number of attributes in this Map.
        """
        ...


    def isEmpty(self) -> bool:
        """
        Returns True if this Map contains no attributes.
        """
        ...


    def keySet(self) -> set["Object"]:
        """
        Returns a Set view of the attribute names (keys) contained in this Map.
        """
        ...


    def values(self) -> Iterable["Object"]:
        """
        Returns a Collection view of the attribute values contained in this Map.
        """
        ...


    def entrySet(self) -> set["Map.Entry"["Object", "Object"]]:
        """
        Returns a Collection view of the attribute name-value mappings
        contained in this Map.
        """
        ...


    def equals(self, o: "Object") -> bool:
        """
        Compares the specified object to the underlying
        Attributes.map map for equality.
        Returns True if the given object is also a Map
        and the two maps represent the same mappings.

        Arguments
        - o: the Object to be compared

        Returns
        - True if the specified Object is equal to this Map
        """
        ...


    def hashCode(self) -> int:
        """
        Returns the hash code value for this Map.
        """
        ...


    def clone(self) -> "Object":
        """
        Returns a copy of the Attributes, implemented as follows:
        ```
            public Object clone() { return new Attributes(this); }
        ```
        Since the attribute names and values are themselves immutable,
        the Attributes returned can be safely modified without affecting
        the original.
        """
        ...


    class Name:
        """
        The Attributes.Name class represents an attribute name stored in
        this Map. Valid attribute names are case-insensitive, are restricted
        to the ASCII characters in the set [0-9a-zA-Z_-], and cannot exceed
        70 characters in length. Attribute values can contain any characters
        and will be UTF8-encoded when written to the output stream.  See the
        <a href="/../specs/jar/jar.html">JAR File Specification</a>
        for more information about valid attribute names and values.
        """

        MANIFEST_VERSION = None
        """
        `Name` object for `Manifest-Version`
        manifest attribute. This attribute indicates the version number
        of the manifest standard to which a JAR file's manifest conforms.

        See
        - <a href="/../specs/jar/jar.html.jar-manifest">
             Manifest and Signature Specification</a>
        """
        SIGNATURE_VERSION = None
        """
        `Name` object for `Signature-Version`
        manifest attribute used when signing JAR files.

        See
        - <a href="/../specs/jar/jar.html.jar-manifest">
             Manifest and Signature Specification</a>
        """
        CONTENT_TYPE = None
        """
        `Name` object for `Content-Type`
        manifest attribute.
        """
        CLASS_PATH = None
        """
        `Name` object for `Class-Path`
        manifest attribute.

        See
        - <a href="/../specs/jar/jar.html.class-path-attribute">
             JAR file specification</a>
        """
        MAIN_CLASS = None
        """
        `Name` object for `Main-Class` manifest
        attribute used for launching applications packaged in JAR files.
        The `Main-Class` attribute is used in conjunction
        with the `-jar` command-line option of the
        `java` application launcher.
        """
        SEALED = None
        """
        `Name` object for `Sealed` manifest attribute
        used for sealing.

        See
        - <a href="/../specs/jar/jar.html.package-sealing">
             Package Sealing</a>
        """
        EXTENSION_LIST = None
        """
        `Name` object for `Extension-List` manifest attribute
        used for the extension mechanism that is no longer supported.
        """
        EXTENSION_NAME = None
        """
        `Name` object for `Extension-Name` manifest attribute
        used for the extension mechanism that is no longer supported.
        """
        EXTENSION_INSTALLATION = None
        """
        `Name` object for `Extension-Installation` manifest attribute.

        Deprecated
        - Extension mechanism is no longer supported.
        """
        IMPLEMENTATION_TITLE = None
        """
        `Name` object for `Implementation-Title`
        manifest attribute used for package versioning.
        """
        IMPLEMENTATION_VERSION = None
        """
        `Name` object for `Implementation-Version`
        manifest attribute used for package versioning.
        """
        IMPLEMENTATION_VENDOR = None
        """
        `Name` object for `Implementation-Vendor`
        manifest attribute used for package versioning.
        """
        IMPLEMENTATION_VENDOR_ID = None
        """
        `Name` object for `Implementation-Vendor-Id`
        manifest attribute.

        Deprecated
        - Extension mechanism is no longer supported.
        """
        IMPLEMENTATION_URL = None
        """
        `Name` object for `Implementation-URL`
        manifest attribute.

        Deprecated
        - Extension mechanism is no longer supported.
        """
        SPECIFICATION_TITLE = None
        """
        `Name` object for `Specification-Title`
        manifest attribute used for package versioning.
        """
        SPECIFICATION_VERSION = None
        """
        `Name` object for `Specification-Version`
        manifest attribute used for package versioning.
        """
        SPECIFICATION_VENDOR = None
        """
        `Name` object for `Specification-Vendor`
        manifest attribute used for package versioning.
        """
        MULTI_RELEASE = None
        """
        `Name` object for `Multi-Release`
        manifest attribute that indicates this is a multi-release JAR file.

        Since
        - 9
        """


        def __init__(self, name: str):
            """
            Constructs a new attribute name using the given string name.

            Arguments
            - name: the attribute string name

            Raises
            - IllegalArgumentException: if the attribute name was
                       invalid
            - NullPointerException: if the attribute name was null
            """
            ...


        def equals(self, o: "Object") -> bool:
            """
            Compares this attribute name to another for equality.

            Arguments
            - o: the object to compare

            Returns
            - True if this attribute name is equal to the
                    specified attribute object
            """
            ...


        def hashCode(self) -> int:
            """
            Computes the hash value for this attribute name.
            """
            ...


        def toString(self) -> str:
            """
            Returns the attribute name as a String.
            """
            ...
