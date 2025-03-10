"""
Python module generated from Java source file java.nio.charset.Charset

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.nio.charset import *
from java.nio.charset.spi import CharsetProvider
from java.security import AccessController
from java.security import PrivilegedAction
from java.util import Arrays
from java.util import Collections
from java.util import Iterator
from java.util import Locale
from java.util import NoSuchElementException
from java.util import Objects
from java.util import ServiceConfigurationError
from java.util import ServiceLoader
from java.util import SortedMap
from jdk.internal.misc import VM
from sun.nio.cs import ThreadLocalCoders
from sun.security.action import GetPropertyAction
from typing import Any, Callable, Iterable, Tuple


class Charset(Comparable):

    @staticmethod
    def isSupported(charsetName: str) -> bool:
        """
        Tells whether the named charset is supported.

        Arguments
        - charsetName: The name of the requested charset; may be either
                a canonical name or an alias

        Returns
        - `True` if, and only if, support for the named charset
                 is available in the current Java virtual machine

        Raises
        - IllegalCharsetNameException: If the given charset name is illegal
        - IllegalArgumentException: If the given `charsetName` is null
        """
        ...


    @staticmethod
    def forName(charsetName: str) -> "Charset":
        """
        Returns a charset object for the named charset.

        Arguments
        - charsetName: The name of the requested charset; may be either
                a canonical name or an alias

        Returns
        - A charset object for the named charset

        Raises
        - IllegalCharsetNameException: If the given charset name is illegal
        - IllegalArgumentException: If the given `charsetName` is null
        - UnsupportedCharsetException: If no support for the named charset is available
                 in this instance of the Java virtual machine
        """
        ...


    @staticmethod
    def availableCharsets() -> "SortedMap"[str, "Charset"]:
        """
        Constructs a sorted map from canonical charset names to charset objects.
        
         The map returned by this method will have one entry for each charset
        for which support is available in the current Java virtual machine.  If
        two or more supported charsets have the same canonical name then the
        resulting map will contain just one of them; which one it will contain
        is not specified. 
        
         The invocation of this method, and the subsequent use of the
        resulting map, may cause time-consuming disk or network I/O operations
        to occur.  This method is provided for applications that need to
        enumerate all of the available charsets, for example to allow user
        charset selection.  This method is not used by the .forName
        forName method, which instead employs an efficient incremental lookup
        algorithm.
        
         This method may return different results at different times if new
        charset providers are dynamically made available to the current Java
        virtual machine.  In the absence of such changes, the charsets returned
        by this method are exactly those that can be retrieved via the .forName forName method.  

        Returns
        - An immutable, case-insensitive map from canonical charset names
                to charset objects
        """
        ...


    @staticmethod
    def defaultCharset() -> "Charset":
        """
        Returns the default charset of this Java virtual machine.
        
         The default charset is determined during virtual-machine startup and
        typically depends upon the locale and charset of the underlying
        operating system.

        Returns
        - A charset object for the default charset

        Since
        - 1.5
        """
        ...


    def name(self) -> str:
        """
        Returns this charset's canonical name.

        Returns
        - The canonical name of this charset
        """
        ...


    def aliases(self) -> set[str]:
        """
        Returns a set containing this charset's aliases.

        Returns
        - An immutable set of this charset's aliases
        """
        ...


    def displayName(self) -> str:
        """
        Returns this charset's human-readable name for the default locale.
        
         The default implementation of this method simply returns this
        charset's canonical name.  Concrete subclasses of this class may
        override this method in order to provide a localized display name. 

        Returns
        - The display name of this charset in the default locale
        """
        ...


    def isRegistered(self) -> bool:
        """
        Tells whether or not this charset is registered in the <a
        href="http://www.iana.org/assignments/character-sets">IANA Charset
        Registry</a>.

        Returns
        - `True` if, and only if, this charset is known by its
                 implementor to be registered with the IANA
        """
        ...


    def displayName(self, locale: "Locale") -> str:
        """
        Returns this charset's human-readable name for the given locale.
        
         The default implementation of this method simply returns this
        charset's canonical name.  Concrete subclasses of this class may
        override this method in order to provide a localized display name. 

        Arguments
        - locale: The locale for which the display name is to be retrieved

        Returns
        - The display name of this charset in the given locale
        """
        ...


    def contains(self, cs: "Charset") -> bool:
        """
        Tells whether or not this charset contains the given charset.
        
         A charset *C* is said to *contain* a charset *D* if,
        and only if, every character representable in *D* is also
        representable in *C*.  If this relationship holds then it is
        guaranteed that every string that can be encoded in *D* can also be
        encoded in *C* without performing any replacements.
        
         That *C* contains *D* does not imply that each character
        representable in *C* by a particular byte sequence is represented
        in *D* by the same byte sequence, although sometimes this is the
        case.
        
         Every charset contains itself.
        
         This method computes an approximation of the containment relation:
        If it returns `True` then the given charset is known to be
        contained by this charset; if it returns `False`, however, then
        it is not necessarily the case that the given charset is not contained
        in this charset.

        Arguments
        - cs: The given charset

        Returns
        - `True` if the given charset is contained in this charset
        """
        ...


    def newDecoder(self) -> "CharsetDecoder":
        """
        Constructs a new decoder for this charset.

        Returns
        - A new decoder for this charset
        """
        ...


    def newEncoder(self) -> "CharsetEncoder":
        """
        Constructs a new encoder for this charset.

        Returns
        - A new encoder for this charset

        Raises
        - UnsupportedOperationException: If this charset does not support encoding
        """
        ...


    def canEncode(self) -> bool:
        """
        Tells whether or not this charset supports encoding.
        
         Nearly all charsets support encoding.  The primary exceptions are
        special-purpose *auto-detect* charsets whose decoders can determine
        which of several possible encoding schemes is in use by examining the
        input byte sequence.  Such charsets do not support encoding because
        there is no way to determine which encoding should be used on output.
        Implementations of such charsets should override this method to return
        `False`. 

        Returns
        - `True` if, and only if, this charset supports encoding
        """
        ...


    def decode(self, bb: "ByteBuffer") -> "CharBuffer":
        """
        Convenience method that decodes bytes in this charset into Unicode
        characters.
        
         An invocation of this method upon a charset `cs` returns the
        same result as the expression
        
        ```
            cs.newDecoder()
              .onMalformedInput(CodingErrorAction.REPLACE)
              .onUnmappableCharacter(CodingErrorAction.REPLACE)
              .decode(bb); ```
        
        except that it is potentially more efficient because it can cache
        decoders between successive invocations.
        
         This method always replaces malformed-input and unmappable-character
        sequences with this charset's default replacement byte array.  In order
        to detect such sequences, use the CharsetDecoder.decode(java.nio.ByteBuffer) method directly.  

        Arguments
        - bb: The byte buffer to be decoded

        Returns
        - A char buffer containing the decoded characters
        """
        ...


    def encode(self, cb: "CharBuffer") -> "ByteBuffer":
        """
        Convenience method that encodes Unicode characters into bytes in this
        charset.
        
         An invocation of this method upon a charset `cs` returns the
        same result as the expression
        
        ```
            cs.newEncoder()
              .onMalformedInput(CodingErrorAction.REPLACE)
              .onUnmappableCharacter(CodingErrorAction.REPLACE)
              .encode(bb); ```
        
        except that it is potentially more efficient because it can cache
        encoders between successive invocations.
        
         This method always replaces malformed-input and unmappable-character
        sequences with this charset's default replacement string.  In order to
        detect such sequences, use the CharsetEncoder.encode(java.nio.CharBuffer) method directly.  

        Arguments
        - cb: The char buffer to be encoded

        Returns
        - A byte buffer containing the encoded characters
        """
        ...


    def encode(self, str: str) -> "ByteBuffer":
        """
        Convenience method that encodes a string into bytes in this charset.
        
         An invocation of this method upon a charset `cs` returns the
        same result as the expression
        
        ```
            cs.encode(CharBuffer.wrap(s)); ```

        Arguments
        - str: The string to be encoded

        Returns
        - A byte buffer containing the encoded characters
        """
        ...


    def compareTo(self, that: "Charset") -> int:
        """
        Compares this charset to another.
        
         Charsets are ordered by their canonical names, without regard to
        case. 

        Arguments
        - that: The charset to which this charset is to be compared

        Returns
        - A negative integer, zero, or a positive integer as this charset
                is less than, equal to, or greater than the specified charset
        """
        ...


    def hashCode(self) -> int:
        """
        Computes a hashcode for this charset.

        Returns
        - An integer hashcode
        """
        ...


    def equals(self, ob: "Object") -> bool:
        """
        Tells whether or not this object is equal to another.
        
         Two charsets are equal if, and only if, they have the same canonical
        names.  A charset is never equal to any other type of object.  

        Returns
        - `True` if, and only if, this charset is equal to the
                 given object
        """
        ...


    def toString(self) -> str:
        """
        Returns a string describing this charset.

        Returns
        - A string describing this charset
        """
        ...
