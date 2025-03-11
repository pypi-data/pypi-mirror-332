"""
Python module generated from Java source file org.bukkit.structure.StructureManager

Java source file obtained from artifact spigot-api version 1.21.3-R0.1-20241203.162251-46

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.io import File
from java.io import IOException
from java.io import InputStream
from java.io import OutputStream
from org.bukkit import NamespacedKey
from org.bukkit.structure import *
from typing import Any, Callable, Iterable, Tuple


class StructureManager:

    def getStructures(self) -> dict["NamespacedKey", "Structure"]:
        """
        Gets the currently registered structures.
        
        These are the currently loaded structures that the StructureManager is
        aware of. When a structure block refers to a structure, these structures
        are checked first. If the specified structure is not found among the
        currently registered structures, the StructureManager may dynamically
        read the structure from the primary world folder, DataPacks, or the
        server's own resources. Structures can be registered via .registerStructure(NamespacedKey, Structure)

        Returns
        - an unmodifiable shallow copy of the currently registered
        structures
        """
        ...


    def getStructure(self, structureKey: "NamespacedKey") -> "Structure":
        """
        Gets a registered Structure.

        Arguments
        - structureKey: The key for which to get the structure

        Returns
        - The structure that belongs to the structureKey or
        `null` if there is none registered for that key.
        """
        ...


    def registerStructure(self, structureKey: "NamespacedKey", structure: "Structure") -> "Structure":
        """
        Registers the given structure. See .getStructures().

        Arguments
        - structureKey: The key for which to register the structure
        - structure: The structure to register

        Returns
        - The structure for the specified key, or `null` if the
        structure could not be found.
        """
        ...


    def unregisterStructure(self, structureKey: "NamespacedKey") -> "Structure":
        """
        Unregisters a structure. Unregisters the specified structure. If the
        structure still exists in the primary world folder, a DataPack, or is
        part of the server's own resources, it may be loaded and registered again
        when it is requested by a plugin or the server itself.

        Arguments
        - structureKey: The key for which to save the structure for

        Returns
        - The structure that was registered for that key or
        `null` if there was none
        """
        ...


    def loadStructure(self, structureKey: "NamespacedKey", register: bool) -> "Structure":
        """
        Loads a structure for the specified key and optionally .registerStructure(NamespacedKey, Structure) registers it.
        
        This will first check the already loaded .getStructures()
        registered structures, and otherwise load the structure from the primary
        world folder, DataPacks, and the server's own resources (in this order).
        
        When loading the structure from the primary world folder, the given key
        is translated to a file as specified by
        .getStructureFile(NamespacedKey).

        Arguments
        - structureKey: The key for which to load the structure
        - register: `True` to register the loaded structure.

        Returns
        - The structure, or `null` if no structure was found for
        the specified key
        """
        ...


    def loadStructure(self, structureKey: "NamespacedKey") -> "Structure":
        """
        Loads the structure for the specified key and automatically registers it.
        See .loadStructure(NamespacedKey, boolean).

        Arguments
        - structureKey: The key for which to load the structure

        Returns
        - The structure for the specified key, or `null` if the
        structure could not be found.
        """
        ...


    def saveStructure(self, structureKey: "NamespacedKey") -> None:
        """
        Saves the currently .getStructures() registered structure for the
        specified NamespacedKey key to the primary world folder as
        specified by {#getStructureFile(NamespacedKey}.

        Arguments
        - structureKey: The key for which to save the structure for
        """
        ...


    def saveStructure(self, structureKey: "NamespacedKey", structure: "Structure") -> None:
        """
        Saves a structure with a given key to the primary world folder.

        Arguments
        - structureKey: The key for which to save the structure for
        - structure: The structure to save for this structureKey
        """
        ...


    def deleteStructure(self, structureKey: "NamespacedKey") -> None:
        """
        Unregisters the specified structure and deletes its .getStructureFile(NamespacedKey) structure file from the primary world
        folder. Note that this method cannot be used to delete vanilla Minecraft
        structures, or structures from DataPacks. Unregistering these structures
        will however work fine.

        Arguments
        - structureKey: The key of the structure to remove

        Raises
        - IOException: If the file could not be removed for some reason.
        """
        ...


    def deleteStructure(self, structureKey: "NamespacedKey", unregister: bool) -> None:
        """
        Deletes the .getStructureFile(NamespacedKey) structure file for
        the specified structure from the primary world folder. Note that this
        method cannot be used to delete vanilla Minecraft structures, or
        structures from DataPacks. Unregistering these structures will however
        work fine.

        Arguments
        - structureKey: The key of the structure to remove
        - unregister: Whether to also unregister the specified structure if
        it is currently loaded.

        Raises
        - IOException: If the file could not be removed for some reason.
        """
        ...


    def getStructureFile(self, structureKey: "NamespacedKey") -> "File":
        """
        Gets the location where a structure file would exist in the primary world
        directory based on the NamespacedKey using the format
        world/generated/{NAMESPACE}/structures/{KEY}.nbt. This method will always
        return a file, even if none exists at the moment.

        Arguments
        - structureKey: The key to build the filepath from.

        Returns
        - The location where a file with this key would be.
        """
        ...


    def loadStructure(self, file: "File") -> "Structure":
        """
        Reads a Structure from disk.

        Arguments
        - file: The file of the structure

        Returns
        - The read structure

        Raises
        - IOException: when the given file can not be read from
        """
        ...


    def loadStructure(self, inputStream: "InputStream") -> "Structure":
        """
        Reads a Structure from a stream.

        Arguments
        - inputStream: The file of the structure

        Returns
        - The read Structure
        """
        ...


    def saveStructure(self, file: "File", structure: "Structure") -> None:
        """
        Save a structure to a file. This will overwrite a file if it already
        exists.

        Arguments
        - file: the target to save to.
        - structure: the Structure to save.

        Raises
        - IOException: when the given file can not be written to.
        """
        ...


    def saveStructure(self, outputStream: "OutputStream", structure: "Structure") -> None:
        """
        Save a structure to a stream.

        Arguments
        - outputStream: the stream to write to.
        - structure: the Structure to save.

        Raises
        - IOException: when the given file can not be written to.
        """
        ...


    def createStructure(self) -> "Structure":
        """
        Creates a new empty structure.

        Returns
        - an empty structure.
        """
        ...


    def copy(self, structure: "Structure") -> "Structure":
        """
        Creates a copy of this structure.

        Arguments
        - structure: The structure to copy

        Returns
        - a copy of the structure
        """
        ...
