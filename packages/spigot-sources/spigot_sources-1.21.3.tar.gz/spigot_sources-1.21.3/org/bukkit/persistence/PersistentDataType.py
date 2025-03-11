"""
Python module generated from Java source file org.bukkit.persistence.PersistentDataType

Java source file obtained from artifact spigot-api version 1.21.3-R0.1-20241203.162251-46

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
    {@code
    public class UUIDTagType implements PersistentDataType<byte[], UUID> {
    
    Type `<P>`: the primary object type that is stored in the given tag
    
    Type `<C>`: the retrieved object type when applying this tag type

    Unknown Tags
    - public Class<byte[]> getPrimitiveType() {
                return byte[].class;
            }
    - public Class<UUID> getComplexType() {
                return UUID.class;
            }
    - public byte[] toPrimitive(UUID complex, PersistentDataAdapterContext context) {
                ByteBuffer bb = ByteBuffer.wrap(new byte[16]);
                bb.putLong(complex.getMostSignificantBits());
                bb.putLong(complex.getLeastSignificantBits());
                return bb.array();
            }
    - public UUID fromPrimitive(byte[] primitive, PersistentDataAdapterContext context) {
                ByteBuffer bb = ByteBuffer.wrap(primitive);
                long firstLong = bb.getLong();
                long secondLong = bb.getLong();
                return new UUID(firstLong, secondLong);
            }
        }
    }```
    
    Any plugin owned implementation of this interface is required to define one
    of the existing primitive types found in this interface. Notably
    .BOOLEAN is not a primitive type but a convenience type.
    """

    BYTE = PrimitivePersistentDataType<>(Byte.class)
    SHORT = PrimitivePersistentDataType<>(Short.class)
    INTEGER = PrimitivePersistentDataType<>(Integer.class)
    LONG = PrimitivePersistentDataType<>(Long.class)
    FLOAT = PrimitivePersistentDataType<>(Float.class)
    DOUBLE = PrimitivePersistentDataType<>(Double.class)
    BOOLEAN = BooleanPersistentDataType()
    """
    A convenience implementation to convert between Byte and Boolean as there is
    no native implementation for booleans. 
    Any byte value not equal to 0 is considered to be True.
    """
    STRING = PrimitivePersistentDataType<>(String.class)
    BYTE_ARRAY = PrimitivePersistentDataType<>(byte[].class)
    INTEGER_ARRAY = PrimitivePersistentDataType<>(int[].class)
    LONG_ARRAY = PrimitivePersistentDataType<>(long[].class)
    TAG_CONTAINER_ARRAY = PrimitivePersistentDataType<>(PersistentDataContainer[].class)
    """
    Deprecated
    - Use .LIST's ListPersistentDataTypeProvider.dataContainers() instead as
    ListPersistentDataTypes offer full support for primitive types, such as the
    PersistentDataContainer.
    """
    TAG_CONTAINER = PrimitivePersistentDataType<>(PersistentDataContainer.class)
    LIST = ListPersistentDataTypeProvider()
    """
    A data type provider type that itself cannot be used as a
    PersistentDataType.
    
    ListPersistentDataTypeProvider exposes shared persistent data
    types for storing lists of other data types, however.
    
    Its existence in the PersistentDataType interface does not permit
    java.util.List as a primitive type in combination with a plain
    PersistentDataType. java.util.Lists are only valid
    primitive types when used via a ListPersistentDataType.

    See
    - ListPersistentDataTypeProvider
    """


    def getPrimitiveType(self) -> type["P"]:
        """
        Returns the primitive data type of this tag.

        Returns
        - the class
        """
        ...


    def getComplexType(self) -> type["C"]:
        """
        Returns the complex object type the primitive value resembles.

        Returns
        - the class type
        """
        ...


    def toPrimitive(self, complex: "C", context: "PersistentDataAdapterContext") -> "P":
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


    def fromPrimitive(self, primitive: "P", context: "PersistentDataAdapterContext") -> "C":
        """
        Creates a complex object based of the passed primitive value

        Arguments
        - primitive: the primitive value
        - context: the context this operation is running in

        Returns
        - the complex object instance
        """
        ...
