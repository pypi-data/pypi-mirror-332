"""
Python module generated from Java source file org.bukkit.inventory.meta.tags.CustomItemTagContainer

Java source file obtained from artifact spigot-api version 1.21.1-R0.1-20241022.152140-54

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import NamespacedKey
from org.bukkit.inventory.meta import ItemMeta
from org.bukkit.inventory.meta.tags import *
from typing import Any, Callable, Iterable, Tuple


class CustomItemTagContainer:
    """
    This interface represents a map like object, capable of storing custom tags
    in it.

    Deprecated
    - this API part has been replaced by the
    org.bukkit.persistence.PersistentDataHolder API. Please use
    org.bukkit.persistence.PersistentDataHolder instead of this.
    """

    def setCustomTag(self, key: "NamespacedKey", type: "ItemTagType"["T", "Z"], value: "Z") -> None:
        """
        Stores a custom value on the ItemMeta.
        
        This API cannot be used to manipulate minecraft tags, as the values will
        be stored using your namespace. This method will override any existing
        value the meta may have stored under the provided key.
        
        Type `<T>`: the generic java type of the tag value
        
        Type `<Z>`: the generic type of the object to store

        Arguments
        - key: the key this value will be stored under
        - type: the type this item tag uses
        - value: the value stored in the tag

        Raises
        - NullPointerException: if the key is null
        - NullPointerException: if the type is null
        - NullPointerException: if the value is null. Removing a custom tag
        should be done using .removeCustomTag(org.bukkit.NamespacedKey)
        - IllegalArgumentException: if no suitable adapter will be found for
        the ItemTagType.getPrimitiveType()
        """
        ...


    def hasCustomTag(self, key: "NamespacedKey", type: "ItemTagType"["T", "Z"]) -> bool:
        """
        Returns if the item meta has a custom tag registered matching the
        provided parameters.
        
        This method will only return if the found value has the same primitive
        data type as the provided key.
        
        Storing a value using a custom ItemTagType implementation will
        not store the complex data type. Therefore storing a UUID (by storing a
        byte[]) will match hasCustomTag("key" , ItemTagType.BYTE_ARRAY).
        Likewise a stored byte[] will always match your UUID ItemTagType
        even if it is not 16 bytes long.
        
        This method is only usable for custom object keys. Overwriting existing
        tags, like the the display name, will not work as the values are stored
        using your namespace.
        
        Type `<T>`: the generic type of the stored primitive
        
        Type `<Z>`: the generic type of the eventually created complex object

        Arguments
        - key: the key the value is stored under
        - type: the type which primitive storage type has to match the value

        Returns
        - if a value

        Raises
        - NullPointerException: if the key to look up is null
        - NullPointerException: if the type to cast the found object to is
        null
        """
        ...


    def getCustomTag(self, key: "NamespacedKey", type: "ItemTagType"["T", "Z"]) -> "Z":
        """
        Returns the custom tag's value that is stored on the item.
        
        Type `<T>`: the generic type of the stored primitive
        
        Type `<Z>`: the generic type of the eventually created complex object

        Arguments
        - key: the key to look up in the custom tag map
        - type: the type the value must have and will be casted to

        Returns
        - the value or `null` if no value was mapped under the given
        value

        Raises
        - NullPointerException: if the key to look up is null
        - NullPointerException: if the type to cast the found object to is
        null
        - IllegalArgumentException: if the value exists under the given key,
        but cannot be access using the given type
        - IllegalArgumentException: if no suitable adapter will be found for
        the ItemTagType.getPrimitiveType()
        """
        ...


    def removeCustomTag(self, key: "NamespacedKey") -> None:
        """
        Removes a custom key from the item meta.

        Arguments
        - key: the key

        Raises
        - NullPointerException: if the provided key is null
        """
        ...


    def isEmpty(self) -> bool:
        """
        Returns if the container instance is empty, therefore has no entries
        inside it.

        Returns
        - the boolean
        """
        ...


    def getAdapterContext(self) -> "ItemTagAdapterContext":
        """
        Returns the adapter context this tag container uses.

        Returns
        - the tag context
        """
        ...
