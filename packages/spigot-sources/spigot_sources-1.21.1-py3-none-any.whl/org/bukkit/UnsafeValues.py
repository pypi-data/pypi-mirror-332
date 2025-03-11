"""
Python module generated from Java source file org.bukkit.UnsafeValues

Java source file obtained from artifact spigot-api version 1.21.1-R0.1-20241022.152140-54

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.collect import Multimap
from org.bukkit import *
from org.bukkit.advancement import Advancement
from org.bukkit.attribute import Attribute
from org.bukkit.attribute import AttributeModifier
from org.bukkit.block.data import BlockData
from org.bukkit.damage import DamageEffect
from org.bukkit.damage import DamageSource
from org.bukkit.damage import DamageType
from org.bukkit.entity import EntityType
from org.bukkit.inventory import CreativeCategory
from org.bukkit.inventory import EquipmentSlot
from org.bukkit.inventory import ItemStack
from org.bukkit.material import MaterialData
from org.bukkit.plugin import InvalidPluginException
from org.bukkit.plugin import PluginDescriptionFile
from org.bukkit.potion import PotionType
from typing import Any, Callable, Iterable, Tuple


class UnsafeValues:
    """
    This interface provides value conversions that may be specific to a
    runtime, or have arbitrary meaning (read: magic values).
    
    Their existence and behavior is not guaranteed across future versions. They
    may be poorly named, throw exceptions, have misleading parameters, or any
    other bad programming practice.
    """

    def toLegacy(self, material: "Material") -> "Material":
        ...


    def fromLegacy(self, material: "Material") -> "Material":
        ...


    def fromLegacy(self, material: "MaterialData") -> "Material":
        ...


    def fromLegacy(self, material: "MaterialData", itemPriority: bool) -> "Material":
        ...


    def fromLegacy(self, material: "Material", data: int) -> "BlockData":
        ...


    def getMaterial(self, material: str, version: int) -> "Material":
        ...


    def getDataVersion(self) -> int:
        ...


    def modifyItemStack(self, stack: "ItemStack", arguments: str) -> "ItemStack":
        ...


    def checkSupported(self, pdf: "PluginDescriptionFile") -> None:
        ...


    def processClass(self, pdf: "PluginDescriptionFile", path: str, clazz: list[int]) -> list[int]:
        ...


    def loadAdvancement(self, key: "NamespacedKey", advancement: str) -> "Advancement":
        """
        Load an advancement represented by the specified string into the server.
        The advancement format is governed by Minecraft and has no specified
        layout.
        
        It is currently a JSON object, as described by the <a href="https://minecraft.wiki/w/Advancements">Minecraft wiki</a>.
        
        Loaded advancements will be stored and persisted across server restarts
        and reloads.
        
        Callers should be prepared for Exception to be thrown.

        Arguments
        - key: the unique advancement key
        - advancement: representation of the advancement

        Returns
        - the loaded advancement or null if an error occurred
        """
        ...


    def removeAdvancement(self, key: "NamespacedKey") -> bool:
        """
        Delete an advancement which was loaded and saved by
        .loadAdvancement(org.bukkit.NamespacedKey, java.lang.String).
        
        This method will only remove advancement from persistent storage. It
        should be accompanied by a call to Server.reloadData() in order
        to fully remove it from the running instance.

        Arguments
        - key: the unique advancement key

        Returns
        - True if a file matching this key was found and deleted
        """
        ...


    def getDefaultAttributeModifiers(self, material: "Material", slot: "EquipmentSlot") -> "Multimap"["Attribute", "AttributeModifier"]:
        ...


    def getCreativeCategory(self, material: "Material") -> "CreativeCategory":
        ...


    def getBlockTranslationKey(self, material: "Material") -> str:
        ...


    def getItemTranslationKey(self, material: "Material") -> str:
        ...


    def getTranslationKey(self, entityType: "EntityType") -> str:
        ...


    def getTranslationKey(self, itemStack: "ItemStack") -> str:
        ...


    def getTranslationKey(self, attribute: "Attribute") -> str:
        ...


    def getFeatureFlag(self, key: "NamespacedKey") -> "FeatureFlag":
        ...


    def getInternalPotionData(self, key: "NamespacedKey") -> "PotionType.InternalPotionData":
        """
        Do not use, method will get removed, and the plugin won't run

        Arguments
        - key: of the potion type

        Returns
        - an internal potion data
        """
        ...


    def getDamageEffect(self, key: str) -> "DamageEffect":
        ...


    def createDamageSourceBuilder(self, damageType: "DamageType") -> "DamageSource.Builder":
        """
        Create a new DamageSource.Builder.

        Arguments
        - damageType: the DamageType to use

        Returns
        - a DamageSource.Builder
        """
        ...


    def get(self, aClass: type[Any], value: str) -> str:
        ...


    def get(self, registry: "Registry"["B"], key: "NamespacedKey") -> "B":
        ...
