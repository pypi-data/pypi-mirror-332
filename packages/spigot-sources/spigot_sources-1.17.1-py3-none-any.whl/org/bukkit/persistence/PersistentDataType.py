"""
Python module generated from Java source file org.bukkit.persistence.PersistentDataType

Java source file obtained from artifact spigot-api version 1.17.1-R0.1-20211121.234319-104

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.persistence import *
from typing import Any, Callable, Iterable, Tuple


class PersistentDataType:
    """
    This class represents an enum with a generic content type. It defines the
    types a custom tag can have.
    
    This interface can be used to create your own custom
    PersistentDataType with different complex types. This may be useful
    for the likes of a UUIDTagType:
    ```
    `public class UUIDTagType implements PersistentDataType<byte[], UUID> {
    
            {@literal @Override`
            public Class<byte[]> getPrimitiveType() {
                return byte[].class;
            }
    
            @Override
            public Class<UUID> getComplexType() {
                return UUID.class;
            }
    
            @Override
            public byte[] toPrimitive(UUID complex, PersistentDataAdapterContext context) {
                ByteBuffer bb = ByteBuffer.wrap(new byte[16]);
                bb.putLong(complex.getMostSignificantBits());
                bb.putLong(complex.getLeastSignificantBits());
                return bb.array();
            }
    
            @Override
            public UUID fromPrimitive(byte[] primitive, PersistentDataAdapterContext context) {
                ByteBuffer bb = ByteBuffer.wrap(primitive);
                long firstLong = bb.getLong();
                long secondLong = bb.getLong();
                return new UUID(firstLong, secondLong);
            }
        }}```
    
    Type `<T>`: the primary object type that is stored in the given tag
    
    Type `<Z>`: the retrieved object type when applying this tag type
    """

    BYTE = PrimitivePersistentDataType<>(Byte.class)
    SHORT = PrimitivePersistentDataType<>(Short.class)
    INTEGER = PrimitivePersistentDataType<>(Integer.class)
    LONG = PrimitivePersistentDataType<>(Long.class)
    FLOAT = PrimitivePersistentDataType<>(Float.class)
    DOUBLE = PrimitivePersistentDataType<>(Double.class)
    STRING = PrimitivePersistentDataType<>(String.class)
    BYTE_ARRAY = PrimitivePersistentDataType<>(byte[].class)
    INTEGER_ARRAY = PrimitivePersistentDataType<>(int[].class)
    LONG_ARRAY = PrimitivePersistentDataType<>(long[].class)
    TAG_CONTAINER_ARRAY = PrimitivePersistentDataType<>(PersistentDataContainer[].class)
    TAG_CONTAINER = PrimitivePersistentDataType<>(PersistentDataContainer.class)


    def getPrimitiveType(self) -> type["T"]:
        """
        Returns the primitive data type of this tag.

        Returns
        - the class
        """
        ...


    def getComplexType(self) -> type["Z"]:
        """
        Returns the complex object type the primitive value resembles.

        Returns
        - the class type
        """
        ...


    def toPrimitive(self, complex: "Z", context: "PersistentDataAdapterContext") -> "T":
        """
        Returns the primitive data that resembles the complex object passed to
        this method.

        Arguments
        - complex: the complex object instance
        - context: the context this operation is running in

        Returns
        - the primitive value
        """
        ...


    def fromPrimitive(self, primitive: "T", context: "PersistentDataAdapterContext") -> "Z":
        """
        Creates a complex object based of the passed primitive value

        Arguments
        - primitive: the primitive value
        - context: the context this operation is running in

        Returns
        - the complex object instance
        """
        ...
