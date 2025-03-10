"""
Python module generated from Java source file org.bukkit.inventory.meta.tags.ItemTagType

Java source file obtained from artifact spigot-api version 1.19.4-R0.1-20230607.155743-88

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.inventory.meta.tags import *
from org.bukkit.persistence import PersistentDataType
from typing import Any, Callable, Iterable, Tuple


class ItemTagType:
    """
    This class represents an enum with a generic content type. It defines the
    types a custom item tag can have.
    
    This interface can be used to create your own custom ItemTagType with
    different complex types. This may be useful for the likes of a
    UUIDItemTagType:
    ```
    `public class UUIDItemTagType implements ItemTagType<byte[], UUID> {
    
            {@literal @Override`
            public Class<byte[]> getPrimitiveType() {
                return byte[].class;
            }
    
            @Override
            public Class<UUID> getComplexType() {
                return UUID.class;
            }
    
            @Override
            public byte[] toPrimitive(UUID complex, ItemTagAdapterContext context) {
                ByteBuffer bb = ByteBuffer.wrap(new byte[16]);
                bb.putLong(complex.getMostSignificantBits());
                bb.putLong(complex.getLeastSignificantBits());
                return bb.array();
            }
    
            @Override
            public UUID fromPrimitive(byte[] primitive, ItemTagAdapterContext context) {
                ByteBuffer bb = ByteBuffer.wrap(primitive);
                long firstLong = bb.getLong();
                long secondLong = bb.getLong();
                return new UUID(firstLong, secondLong);
            }
        }}```
    
    Type `<T>`: the primary object type that is stored in the given tag
    
    Type `<Z>`: the retrieved object type when applying this item tag type

    Deprecated
    - please use PersistentDataType as this part of the api is being replaced
    """

    BYTE = PrimitiveTagType<>(Byte.class)
    SHORT = PrimitiveTagType<>(Short.class)
    INTEGER = PrimitiveTagType<>(Integer.class)
    LONG = PrimitiveTagType<>(Long.class)
    FLOAT = PrimitiveTagType<>(Float.class)
    DOUBLE = PrimitiveTagType<>(Double.class)
    STRING = PrimitiveTagType<>(String.class)
    BYTE_ARRAY = PrimitiveTagType<>(byte[].class)
    INTEGER_ARRAY = PrimitiveTagType<>(int[].class)
    LONG_ARRAY = PrimitiveTagType<>(long[].class)
    TAG_CONTAINER = PrimitiveTagType<>(CustomItemTagContainer.class)


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


    def toPrimitive(self, complex: "Z", context: "ItemTagAdapterContext") -> "T":
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


    def fromPrimitive(self, primitive: "T", context: "ItemTagAdapterContext") -> "Z":
        """
        Creates a complex object based of the passed primitive value

        Arguments
        - primitive: the primitive value
        - context: the context this operation is running in

        Returns
        - the complex object instance
        """
        ...
