"""
Python module generated from Java source file org.bukkit.inventory.meta.ItemMeta

Java source file obtained from artifact spigot-api version 1.20-R0.1-20230612.113428-32

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.collect import Multimap
from org.bukkit.attribute import Attribute
from org.bukkit.attribute import AttributeModifier
from org.bukkit.configuration.serialization import ConfigurationSerializable
from org.bukkit.enchantments import Enchantment
from org.bukkit.inventory import EquipmentSlot
from org.bukkit.inventory import ItemFlag
from org.bukkit.inventory.meta import *
from org.bukkit.inventory.meta.tags import CustomItemTagContainer
from org.bukkit.persistence import PersistentDataHolder
from typing import Any, Callable, Iterable, Tuple


class ItemMeta(Cloneable, ConfigurationSerializable, PersistentDataHolder):
    """
    This type represents the storage mechanism for auxiliary item data.
    
    An implementation will handle the creation and application for ItemMeta.
    This class should not be implemented by a plugin in a live environment.
    """

    def hasDisplayName(self) -> bool:
        """
        Checks for existence of a display name.

        Returns
        - True if this has a display name
        """
        ...


    def getDisplayName(self) -> str:
        """
        Gets the display name that is set.
        
        Plugins should check that hasDisplayName() returns `True`
        before calling this method.

        Returns
        - the display name that is set
        """
        ...


    def setDisplayName(self, name: str) -> None:
        """
        Sets the display name.

        Arguments
        - name: the name to set
        """
        ...


    def hasLocalizedName(self) -> bool:
        """
        Checks for existence of a localized name.

        Returns
        - True if this has a localized name
        """
        ...


    def getLocalizedName(self) -> str:
        """
        Gets the localized display name that is set.
        
        Plugins should check that hasLocalizedName() returns `True`
        before calling this method.

        Returns
        - the localized name that is set
        """
        ...


    def setLocalizedName(self, name: str) -> None:
        """
        Sets the localized name.

        Arguments
        - name: the name to set
        """
        ...


    def hasLore(self) -> bool:
        """
        Checks for existence of lore.

        Returns
        - True if this has lore
        """
        ...


    def getLore(self) -> list[str]:
        """
        Gets the lore that is set.
        
        Plugins should check if hasLore() returns `True` before
        calling this method.

        Returns
        - a list of lore that is set
        """
        ...


    def setLore(self, lore: list[str]) -> None:
        """
        Sets the lore for this item.
        Removes lore when given null.

        Arguments
        - lore: the lore that will be set
        """
        ...


    def hasCustomModelData(self) -> bool:
        """
        Checks for existence of custom model data.
        
        CustomModelData is an integer that may be associated client side with a
        custom item model.

        Returns
        - True if this has custom model data
        """
        ...


    def getCustomModelData(self) -> int:
        """
        Gets the custom model data that is set.
        
        CustomModelData is an integer that may be associated client side with a
        custom item model.
        
        Plugins should check that hasCustomModelData() returns `True`
        before calling this method.

        Returns
        - the custom model data that is set
        """
        ...


    def setCustomModelData(self, data: "Integer") -> None:
        """
        Sets the custom model data.
        
        CustomModelData is an integer that may be associated client side with a
        custom item model.

        Arguments
        - data: the data to set, or null to clear
        """
        ...


    def hasEnchants(self) -> bool:
        """
        Checks for the existence of any enchantments.

        Returns
        - True if an enchantment exists on this meta
        """
        ...


    def hasEnchant(self, ench: "Enchantment") -> bool:
        """
        Checks for existence of the specified enchantment.

        Arguments
        - ench: enchantment to check

        Returns
        - True if this enchantment exists for this meta
        """
        ...


    def getEnchantLevel(self, ench: "Enchantment") -> int:
        """
        Checks for the level of the specified enchantment.

        Arguments
        - ench: enchantment to check

        Returns
        - The level that the specified enchantment has, or 0 if none
        """
        ...


    def getEnchants(self) -> dict["Enchantment", "Integer"]:
        """
        Returns a copy the enchantments in this ItemMeta. 
        Returns an empty map if none.

        Returns
        - An immutable copy of the enchantments
        """
        ...


    def addEnchant(self, ench: "Enchantment", level: int, ignoreLevelRestriction: bool) -> bool:
        """
        Adds the specified enchantment to this item meta.

        Arguments
        - ench: Enchantment to add
        - level: Level for the enchantment
        - ignoreLevelRestriction: this indicates the enchantment should be
            applied, ignoring the level limit

        Returns
        - True if the item meta changed as a result of this call, False
            otherwise
        """
        ...


    def removeEnchant(self, ench: "Enchantment") -> bool:
        """
        Removes the specified enchantment from this item meta.

        Arguments
        - ench: Enchantment to remove

        Returns
        - True if the item meta changed as a result of this call, False
            otherwise
        """
        ...


    def hasConflictingEnchant(self, ench: "Enchantment") -> bool:
        """
        Checks if the specified enchantment conflicts with any enchantments in
        this ItemMeta.

        Arguments
        - ench: enchantment to test

        Returns
        - True if the enchantment conflicts, False otherwise
        """
        ...


    def addItemFlags(self, *itemFlags: Tuple["ItemFlag", ...]) -> None:
        """
        Set itemflags which should be ignored when rendering a ItemStack in the Client. This Method does silently ignore double set itemFlags.

        Arguments
        - itemFlags: The hideflags which shouldn't be rendered
        """
        ...


    def removeItemFlags(self, *itemFlags: Tuple["ItemFlag", ...]) -> None:
        """
        Remove specific set of itemFlags. This tells the Client it should render it again. This Method does silently ignore double removed itemFlags.

        Arguments
        - itemFlags: Hideflags which should be removed
        """
        ...


    def getItemFlags(self) -> set["ItemFlag"]:
        """
        Get current set itemFlags. The collection returned is unmodifiable.

        Returns
        - A set of all itemFlags set
        """
        ...


    def hasItemFlag(self, flag: "ItemFlag") -> bool:
        """
        Check if the specified flag is present on this item.

        Arguments
        - flag: the flag to check

        Returns
        - if it is present
        """
        ...


    def isUnbreakable(self) -> bool:
        """
        Return if the unbreakable tag is True. An unbreakable item will not lose
        durability.

        Returns
        - True if the unbreakable tag is True
        """
        ...


    def setUnbreakable(self, unbreakable: bool) -> None:
        """
        Sets the unbreakable tag. An unbreakable item will not lose durability.

        Arguments
        - unbreakable: True if set unbreakable
        """
        ...


    def hasAttributeModifiers(self) -> bool:
        """
        Checks for the existence of any AttributeModifiers.

        Returns
        - True if any AttributeModifiers exist
        """
        ...


    def getAttributeModifiers(self) -> "Multimap"["Attribute", "AttributeModifier"]:
        """
        Return an immutable copy of all Attributes and
        their modifiers in this ItemMeta.
        Returns null if none exist.

        Returns
        - an immutable Multimap of Attributes
                and their AttributeModifiers, or null if none exist
        """
        ...


    def getAttributeModifiers(self, slot: "EquipmentSlot") -> "Multimap"["Attribute", "AttributeModifier"]:
        """
        Return an immutable copy of all Attributes and their
        AttributeModifiers for a given EquipmentSlot.
        Any AttributeModifier that does have have a given
        EquipmentSlot will be returned. This is because
        AttributeModifiers without a slot are active in any slot.
        If there are no attributes set for the given slot, an empty map
        will be returned.

        Arguments
        - slot: the EquipmentSlot to check

        Returns
        - the immutable Multimap with the
                respective Attributes and modifiers, or an empty map
                if no attributes are set.
        """
        ...


    def getAttributeModifiers(self, attribute: "Attribute") -> Iterable["AttributeModifier"]:
        """
        Return an immutable copy of all AttributeModifiers
        for a given Attribute

        Arguments
        - attribute: the Attribute

        Returns
        - an immutable collection of AttributeModifiers
                 or null if no AttributeModifiers exist for the Attribute.

        Raises
        - NullPointerException: if Attribute is null
        """
        ...


    def addAttributeModifier(self, attribute: "Attribute", modifier: "AttributeModifier") -> bool:
        """
        Add an Attribute and it's Modifier.
        AttributeModifiers can now support EquipmentSlots.
        If not set, the AttributeModifier will be active in ALL slots.
        
        Two AttributeModifiers that have the same java.util.UUID
        cannot exist on the same Attribute.

        Arguments
        - attribute: the Attribute to modify
        - modifier: the AttributeModifier specifying the modification

        Returns
        - True if the Attribute and AttributeModifier were
                successfully added

        Raises
        - NullPointerException: if Attribute is null
        - NullPointerException: if AttributeModifier is null
        - IllegalArgumentException: if AttributeModifier already exists
        """
        ...


    def setAttributeModifiers(self, attributeModifiers: "Multimap"["Attribute", "AttributeModifier"]) -> None:
        """
        Set all Attributes and their AttributeModifiers.
        To clear all currently set Attributes and AttributeModifiers use
        null or an empty Multimap.
        If not null nor empty, this will filter all entries that are not-null
        and add them to the ItemStack.

        Arguments
        - attributeModifiers: the new Multimap containing the Attributes
                                  and their AttributeModifiers
        """
        ...


    def removeAttributeModifier(self, attribute: "Attribute") -> bool:
        """
        Remove all AttributeModifiers associated with the given
        Attribute.
        This will return False if nothing was removed.

        Arguments
        - attribute: attribute to remove

        Returns
        - True if all modifiers were removed from a given
                         Attribute. Returns False if no attributes were
                         removed.

        Raises
        - NullPointerException: if Attribute is null
        """
        ...


    def removeAttributeModifier(self, slot: "EquipmentSlot") -> bool:
        """
        Remove all Attributes and AttributeModifiers for a
        given EquipmentSlot.
        If the given EquipmentSlot is null, this will remove all
        AttributeModifiers that do not have an EquipmentSlot set.

        Arguments
        - slot: the EquipmentSlot to clear all Attributes and
                    their modifiers for

        Returns
        - True if all modifiers were removed that match the given
                EquipmentSlot.
        """
        ...


    def removeAttributeModifier(self, attribute: "Attribute", modifier: "AttributeModifier") -> bool:
        """
        Remove a specific Attribute and AttributeModifier.
        AttributeModifiers are matched according to their java.util.UUID.

        Arguments
        - attribute: the Attribute to remove
        - modifier: the AttributeModifier to remove

        Returns
        - if any attribute modifiers were remove

        Raises
        - NullPointerException: if the Attribute is null
        - NullPointerException: if the AttributeModifier is null

        See
        - AttributeModifier.getUniqueId()
        """
        ...


    def getAsString(self) -> str:
        """
        Get this ItemMeta as an NBT string.
        
        This string should not be relied upon as a serializable value. If
        serialization is desired, the ConfigurationSerializable API
        should be used instead.

        Returns
        - the NBT string
        """
        ...


    def getCustomTagContainer(self) -> "CustomItemTagContainer":
        """
        Returns a public custom tag container capable of storing tags on the
        item.
        
        Those tags will be sent to the client with all of their content, so the
        client is capable of reading them. This will result in the player seeing
        a NBT Tag notification on the item.
        
        These tags can also be modified by the client once in creative mode

        Returns
        - the custom tag container

        Deprecated
        - this API part has been replaced by the PersistentDataHolder API.
        Please use PersistentDataHolder.getPersistentDataContainer() instead of this.
        """
        ...


    def setVersion(self, version: int) -> None:
        """
        Internal use only! Do not use under any circumstances!

        Arguments
        - version: version

        Deprecated
        - internal use only
        """
        ...


    def clone(self) -> "ItemMeta":
        ...
