"""
Python module generated from Java source file java.nio.file.attribute.AclEntry

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.nio.file.attribute import *
from java.util import *
from typing import Any, Callable, Iterable, Tuple


class AclEntry:

    @staticmethod
    def newBuilder() -> "Builder":
        """
        Constructs a new builder. The initial value of the type and who
        components is `null`. The initial value of the permissions and
        flags components is the empty set.

        Returns
        - a new builder
        """
        ...


    @staticmethod
    def newBuilder(entry: "AclEntry") -> "Builder":
        """
        Constructs a new builder with the components of an existing ACL entry.

        Arguments
        - entry: an ACL entry

        Returns
        - a new builder
        """
        ...


    def type(self) -> "AclEntryType":
        """
        Returns the ACL entry type.

        Returns
        - the ACL entry type
        """
        ...


    def principal(self) -> "UserPrincipal":
        """
        Returns the principal component.

        Returns
        - the principal component
        """
        ...


    def permissions(self) -> set["AclEntryPermission"]:
        """
        Returns a copy of the permissions component.
        
         The returned set is a modifiable copy of the permissions.

        Returns
        - the permissions component
        """
        ...


    def flags(self) -> set["AclEntryFlag"]:
        """
        Returns a copy of the flags component.
        
         The returned set is a modifiable copy of the flags.

        Returns
        - the flags component
        """
        ...


    def equals(self, ob: "Object") -> bool:
        """
        Compares the specified object with this ACL entry for equality.
        
         If the given object is not an `AclEntry` then this method
        immediately returns `False`.
        
         For two ACL entries to be considered equals requires that they are
        both the same type, their who components are equal, their permissions
        components are equal, and their flags components are equal.
        
         This method satisfies the general contract of the java.lang.Object.equals(Object) Object.equals method. 

        Arguments
        - ob: the object to which this object is to be compared

        Returns
        - `True` if, and only if, the given object is an AclEntry that
                 is identical to this AclEntry
        """
        ...


    def hashCode(self) -> int:
        """
        Returns the hash-code value for this ACL entry.
        
         This method satisfies the general contract of the Object.hashCode method.
        """
        ...


    def toString(self) -> str:
        """
        Returns the string representation of this ACL entry.

        Returns
        - the string representation of this entry
        """
        ...


    class Builder:
        """
        A builder of AclEntry objects.
        
         A `Builder` object is obtained by invoking one of the AclEntry.newBuilder newBuilder methods defined by the `AclEntry`
        class.
        
         Builder objects are mutable and are not safe for use by multiple
        concurrent threads without appropriate synchronization.

        Since
        - 1.7
        """

        def build(self) -> "AclEntry":
            """
            Constructs an AclEntry from the components of this builder.
            The type and who components are required to have been set in order
            to construct an `AclEntry`.

            Returns
            - a new ACL entry

            Raises
            - IllegalStateException: if the type or who component have not been set
            """
            ...


        def setType(self, type: "AclEntryType") -> "Builder":
            """
            Sets the type component of this builder.

            Arguments
            - type: the component type

            Returns
            - this builder
            """
            ...


        def setPrincipal(self, who: "UserPrincipal") -> "Builder":
            """
            Sets the principal component of this builder.

            Arguments
            - who: the principal component

            Returns
            - this builder
            """
            ...


        def setPermissions(self, perms: set["AclEntryPermission"]) -> "Builder":
            """
            Sets the permissions component of this builder. On return, the
            permissions component of this builder is a copy of the given set.

            Arguments
            - perms: the permissions component

            Returns
            - this builder

            Raises
            - ClassCastException: if the set contains elements that are not of type `AclEntryPermission`
            """
            ...


        def setPermissions(self, *perms: Tuple["AclEntryPermission", ...]) -> "Builder":
            """
            Sets the permissions component of this builder. On return, the
            permissions component of this builder is a copy of the permissions in
            the given array.

            Arguments
            - perms: the permissions component

            Returns
            - this builder
            """
            ...


        def setFlags(self, flags: set["AclEntryFlag"]) -> "Builder":
            """
            Sets the flags component of this builder. On return, the flags
            component of this builder is a copy of the given set.

            Arguments
            - flags: the flags component

            Returns
            - this builder

            Raises
            - ClassCastException: if the set contains elements that are not of type `AclEntryFlag`
            """
            ...


        def setFlags(self, *flags: Tuple["AclEntryFlag", ...]) -> "Builder":
            """
            Sets the flags component of this builder. On return, the flags
            component of this builder is a copy of the flags in the given
            array.

            Arguments
            - flags: the flags component

            Returns
            - this builder
            """
            ...
