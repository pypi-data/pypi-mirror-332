"""
Python module generated from Java source file org.bukkit.entity.HumanEntity

Java source file obtained from artifact spigot-api version 1.20.2-R0.1-20231205.164257-71

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import GameMode
from org.bukkit import Location
from org.bukkit import Material
from org.bukkit import NamespacedKey
from org.bukkit.entity import *
from org.bukkit.inventory import Inventory
from org.bukkit.inventory import InventoryHolder
from org.bukkit.inventory import InventoryView
from org.bukkit.inventory import ItemStack
from org.bukkit.inventory import MainHand
from org.bukkit.inventory import Merchant
from org.bukkit.inventory import PlayerInventory
from org.bukkit.inventory.meta import FireworkMeta
from typing import Any, Callable, Iterable, Tuple


class HumanEntity(LivingEntity, AnimalTamer, InventoryHolder):
    """
    Represents a human entity, such as an NPC or a player
    """

    def getName(self) -> str:
        """
        Returns the name of this player

        Returns
        - Player name
        """
        ...


    def getInventory(self) -> "PlayerInventory":
        """
        Get the player's inventory.

        Returns
        - The inventory of the player, this also contains the armor
            slots.
        """
        ...


    def getEnderChest(self) -> "Inventory":
        """
        Get the player's EnderChest inventory

        Returns
        - The EnderChest of the player
        """
        ...


    def getMainHand(self) -> "MainHand":
        """
        Gets the player's selected main hand

        Returns
        - the players main hand
        """
        ...


    def setWindowProperty(self, prop: "InventoryView.Property", value: int) -> bool:
        """
        If the player currently has an inventory window open, this method will
        set a property of that window, such as the state of a progress bar.

        Arguments
        - prop: The property.
        - value: The value to set the property to.

        Returns
        - True if the property was successfully set.
        """
        ...


    def getEnchantmentSeed(self) -> int:
        """
        Gets the player's current enchantment seed.
        
        The Seed is used to generate enchantment options in the enchanting table
        for the player.

        Returns
        - the player's enchantment seed
        """
        ...


    def setEnchantmentSeed(self, seed: int) -> None:
        """
        Sets the player's enchantment seed.
        
        The Seed is used to generate enchantment options in the enchanting table
        for the player.

        Arguments
        - seed: the player's new enchantment seed
        """
        ...


    def getOpenInventory(self) -> "InventoryView":
        """
        Gets the inventory view the player is currently viewing. If they do not
        have an inventory window open, it returns their internal crafting view.

        Returns
        - The inventory view.
        """
        ...


    def openInventory(self, inventory: "Inventory") -> "InventoryView":
        """
        Opens an inventory window with the specified inventory on the top and
        the player's inventory on the bottom.

        Arguments
        - inventory: The inventory to open

        Returns
        - The newly opened inventory view
        """
        ...


    def openWorkbench(self, location: "Location", force: bool) -> "InventoryView":
        """
        Opens an empty workbench inventory window with the player's inventory
        on the bottom.

        Arguments
        - location: The location to attach it to. If null, the player's
            location is used.
        - force: If False, and there is no workbench block at the location,
            no inventory will be opened and null will be returned.

        Returns
        - The newly opened inventory view, or null if it could not be
            opened.
        """
        ...


    def openEnchanting(self, location: "Location", force: bool) -> "InventoryView":
        """
        Opens an empty enchanting inventory window with the player's inventory
        on the bottom.

        Arguments
        - location: The location to attach it to. If null, the player's
            location is used.
        - force: If False, and there is no enchanting table at the
            location, no inventory will be opened and null will be returned.

        Returns
        - The newly opened inventory view, or null if it could not be
            opened.
        """
        ...


    def openInventory(self, inventory: "InventoryView") -> None:
        """
        Opens an inventory window to the specified inventory view.

        Arguments
        - inventory: The view to open
        """
        ...


    def openMerchant(self, trader: "Villager", force: bool) -> "InventoryView":
        """
        Starts a trade between the player and the villager.
        
        Note that only one player may trade with a villager at once. You must use
        the force parameter for this.

        Arguments
        - trader: The merchant to trade with. Cannot be null.
        - force: whether to force the trade even if another player is trading

        Returns
        - The newly opened inventory view, or null if it could not be
        opened.
        """
        ...


    def openMerchant(self, merchant: "Merchant", force: bool) -> "InventoryView":
        """
        Starts a trade between the player and the merchant.
        
        Note that only one player may trade with a merchant at once. You must use
        the force parameter for this.

        Arguments
        - merchant: The merchant to trade with. Cannot be null.
        - force: whether to force the trade even if another player is trading

        Returns
        - The newly opened inventory view, or null if it could not be
        opened.
        """
        ...


    def closeInventory(self) -> None:
        """
        Force-closes the currently open inventory view for this player, if any.
        """
        ...


    def getItemInHand(self) -> "ItemStack":
        """
        Returns the ItemStack currently in your hand, can be empty.

        Returns
        - The ItemStack of the item you are currently holding.

        Deprecated
        - Humans may now dual wield in their off hand, use explicit
        methods in PlayerInventory.
        """
        ...


    def setItemInHand(self, item: "ItemStack") -> None:
        """
        Sets the item to the given ItemStack, this will replace whatever the
        user was holding.

        Arguments
        - item: The ItemStack which will end up in the hand

        Deprecated
        - Humans may now dual wield in their off hand, use explicit
        methods in PlayerInventory.
        """
        ...


    def getItemOnCursor(self) -> "ItemStack":
        """
        Returns the ItemStack currently on your cursor, can be empty. Will
        always be empty if the player currently has no open window.

        Returns
        - The ItemStack of the item you are currently moving around.
        """
        ...


    def setItemOnCursor(self, item: "ItemStack") -> None:
        """
        Sets the item to the given ItemStack, this will replace whatever the
        user was moving. Will always be empty if the player currently has no
        open window.

        Arguments
        - item: The ItemStack which will end up in the hand
        """
        ...


    def hasCooldown(self, material: "Material") -> bool:
        """
        Check whether a cooldown is active on the specified material.

        Arguments
        - material: the material to check

        Returns
        - if a cooldown is active on the material

        Raises
        - IllegalArgumentException: if the material is not an item
        """
        ...


    def getCooldown(self, material: "Material") -> int:
        """
        Get the cooldown time in ticks remaining for the specified material.

        Arguments
        - material: the material to check

        Returns
        - the remaining cooldown time in ticks

        Raises
        - IllegalArgumentException: if the material is not an item
        """
        ...


    def setCooldown(self, material: "Material", ticks: int) -> None:
        """
        Set a cooldown on the specified material for a certain amount of ticks.
        ticks. 0 ticks will result in the removal of the cooldown.
        
        Cooldowns are used by the server for items such as ender pearls and
        shields to prevent them from being used repeatedly.
        
        Note that cooldowns will not by themselves stop an item from being used
        for attacking.

        Arguments
        - material: the material to set the cooldown for
        - ticks: the amount of ticks to set or 0 to remove

        Raises
        - IllegalArgumentException: if the material is not an item
        """
        ...


    def getSleepTicks(self) -> int:
        """
        Get the sleep ticks of the player. This value may be capped.

        Returns
        - slumber ticks
        """
        ...


    def sleep(self, location: "Location", force: bool) -> bool:
        """
        Attempts to make the entity sleep at the given location.
        
        The location must be in the current world and have a bed placed at the
        location. The game may also enforce other requirements such as proximity
        to bed, monsters, and dimension type if force is not set.

        Arguments
        - location: the location of the bed
        - force: whether to try and sleep at the location even if not
        normally possible

        Returns
        - whether the sleep was successful
        """
        ...


    def wakeup(self, setSpawnLocation: bool) -> None:
        """
        Causes the player to wakeup if they are currently sleeping.

        Arguments
        - setSpawnLocation: whether to set their spawn location to the bed
        they are currently sleeping in

        Raises
        - IllegalStateException: if not sleeping
        """
        ...


    def getBedLocation(self) -> "Location":
        """
        Gets the location of the bed the player is currently sleeping in

        Returns
        - location

        Raises
        - IllegalStateException: if not sleeping
        """
        ...


    def getGameMode(self) -> "GameMode":
        """
        Gets this human's current GameMode

        Returns
        - Current game mode
        """
        ...


    def setGameMode(self, mode: "GameMode") -> None:
        """
        Sets this human's current GameMode

        Arguments
        - mode: New game mode
        """
        ...


    def isBlocking(self) -> bool:
        """
        Check if the player is currently blocking (ie with a shield).

        Returns
        - Whether they are blocking.
        """
        ...


    def isHandRaised(self) -> bool:
        """
        Check if the player currently has their hand raised (ie about to begin
        blocking).

        Returns
        - Whether their hand is raised
        """
        ...


    def getItemInUse(self) -> "ItemStack":
        """
        Gets the item that the player is using (eating food, drawing back a bow,
        blocking, etc.)

        Returns
        - the item being used by the player, or null if they are not using
        an item
        """
        ...


    def getExpToLevel(self) -> int:
        """
        Get the total amount of experience required for the player to level

        Returns
        - Experience required to level up
        """
        ...


    def getAttackCooldown(self) -> float:
        """
        Gets the current cooldown for a player's attack.
        
        This is used to calculate damage, with 1.0 representing a fully charged
        attack and 0.0 representing a non-charged attack

        Returns
        - A float between 0.0-1.0 representing the progress of the charge
        """
        ...


    def discoverRecipe(self, recipe: "NamespacedKey") -> bool:
        """
        Discover a recipe for this player such that it has not already been
        discovered. This method will add the key's associated recipe to the
        player's recipe book.

        Arguments
        - recipe: the key of the recipe to discover

        Returns
        - whether or not the recipe was newly discovered
        """
        ...


    def discoverRecipes(self, recipes: Iterable["NamespacedKey"]) -> int:
        """
        Discover a collection of recipes for this player such that they have not
        already been discovered. This method will add the keys' associated
        recipes to the player's recipe book. If a recipe in the provided
        collection has already been discovered, it will be silently ignored.

        Arguments
        - recipes: the keys of the recipes to discover

        Returns
        - the amount of newly discovered recipes where 0 indicates that
        none were newly discovered and a number equal to `recipes.size()`
        indicates that all were new
        """
        ...


    def undiscoverRecipe(self, recipe: "NamespacedKey") -> bool:
        """
        Undiscover a recipe for this player such that it has already been
        discovered. This method will remove the key's associated recipe from the
        player's recipe book.

        Arguments
        - recipe: the key of the recipe to undiscover

        Returns
        - whether or not the recipe was successfully undiscovered (i.e. it
        was previously discovered)
        """
        ...


    def undiscoverRecipes(self, recipes: Iterable["NamespacedKey"]) -> int:
        """
        Undiscover a collection of recipes for this player such that they have
        already been discovered. This method will remove the keys' associated
        recipes from the player's recipe book. If a recipe in the provided
        collection has not yet been discovered, it will be silently ignored.

        Arguments
        - recipes: the keys of the recipes to undiscover

        Returns
        - the amount of undiscovered recipes where 0 indicates that none
        were undiscovered and a number equal to `recipes.size()` indicates
        that all were undiscovered
        """
        ...


    def hasDiscoveredRecipe(self, recipe: "NamespacedKey") -> bool:
        """
        Check whether or not this entity has discovered the specified recipe.

        Arguments
        - recipe: the key of the recipe to check

        Returns
        - True if discovered, False otherwise
        """
        ...


    def getDiscoveredRecipes(self) -> set["NamespacedKey"]:
        """
        Get an immutable set of recipes this entity has discovered.

        Returns
        - all discovered recipes
        """
        ...


    def getShoulderEntityLeft(self) -> "Entity":
        """
        Gets the entity currently perched on the left shoulder or null if no
        entity.
        
        The returned entity will not be spawned within the world, so most
        operations are invalid unless the entity is first spawned in.

        Returns
        - left shoulder entity

        Deprecated
        - There are currently no well defined semantics regarding
        serialized entities in Bukkit. Use with care.
        """
        ...


    def setShoulderEntityLeft(self, entity: "Entity") -> None:
        """
        Sets the entity currently perched on the left shoulder, or null to
        remove. This method will remove the entity from the world.
        
        Note that only a copy of the entity will be set to display on the
        shoulder.
        
        Also note that the client will currently only render Parrot
        entities.

        Arguments
        - entity: left shoulder entity

        Deprecated
        - There are currently no well defined semantics regarding
        serialized entities in Bukkit. Use with care.
        """
        ...


    def getShoulderEntityRight(self) -> "Entity":
        """
        Gets the entity currently perched on the right shoulder or null if no
        entity.
        
        The returned entity will not be spawned within the world, so most
        operations are invalid unless the entity is first spawned in.

        Returns
        - right shoulder entity

        Deprecated
        - There are currently no well defined semantics regarding
        serialized entities in Bukkit. Use with care.
        """
        ...


    def setShoulderEntityRight(self, entity: "Entity") -> None:
        """
        Sets the entity currently perched on the right shoulder, or null to
        remove. This method will remove the entity from the world.
        
        Note that only a copy of the entity will be set to display on the
        shoulder.
        
        Also note that the client will currently only render Parrot
        entities.

        Arguments
        - entity: right shoulder entity

        Deprecated
        - There are currently no well defined semantics regarding
        serialized entities in Bukkit. Use with care.
        """
        ...


    def dropItem(self, dropAll: bool) -> bool:
        """
        Make the entity drop the item in their hand.
        
        This will force the entity to drop the item they are holding with
        an option to drop the entire ItemStack or just 1 of the items.

        Arguments
        - dropAll: True to drop entire stack, False to drop 1 of the stack

        Returns
        - True if item was dropped successfully
        """
        ...


    def getExhaustion(self) -> float:
        """
        Gets the players current exhaustion level.
        
        Exhaustion controls how fast the food level drops. While you have a
        certain amount of exhaustion, your saturation will drop to zero, and
        then your food will drop to zero.

        Returns
        - Exhaustion level
        """
        ...


    def setExhaustion(self, value: float) -> None:
        """
        Sets the players current exhaustion level

        Arguments
        - value: Exhaustion level
        """
        ...


    def getSaturation(self) -> float:
        """
        Gets the players current saturation level.
        
        Saturation is a buffer for food level. Your food level will not drop if
        you are saturated > 0.

        Returns
        - Saturation level
        """
        ...


    def setSaturation(self, value: float) -> None:
        """
        Sets the players current saturation level

        Arguments
        - value: Saturation level
        """
        ...


    def getFoodLevel(self) -> int:
        """
        Gets the players current food level

        Returns
        - Food level
        """
        ...


    def setFoodLevel(self, value: int) -> None:
        """
        Sets the players current food level

        Arguments
        - value: New food level
        """
        ...


    def getSaturatedRegenRate(self) -> int:
        """
        Get the regeneration rate (1 health per x ticks) of
        the HumanEntity when they have saturation and
        their food level is >= 20. Default is 10.

        Returns
        - the regeneration rate
        """
        ...


    def setSaturatedRegenRate(self, ticks: int) -> None:
        """
        Set the regeneration rate (1 health per x ticks) of
        the HumanEntity when they have saturation and
        their food level is >= 20. Default is 10.
        Not affected if the world's difficulty is peaceful.

        Arguments
        - ticks: the amount of ticks to gain 1 health.
        """
        ...


    def getUnsaturatedRegenRate(self) -> int:
        """
        Get the regeneration rate (1 health per x ticks) of
        the HumanEntity when they have no saturation and
        their food level is >= 18. Default is 80.

        Returns
        - the regeneration rate
        """
        ...


    def setUnsaturatedRegenRate(self, ticks: int) -> None:
        """
        Get the regeneration rate (1 health per x ticks) of
        the HumanEntity when they have no saturation and
        their food level is >= 18. Default is 80.
        Not affected if the world's difficulty is peaceful.

        Arguments
        - ticks: the amount of ticks to gain 1 health.
        """
        ...


    def getStarvationRate(self) -> int:
        """
        Get the starvation rate (1 health per x ticks) of
        the HumanEntity. Default is 80.

        Returns
        - the starvation rate
        """
        ...


    def setStarvationRate(self, ticks: int) -> None:
        """
        Get the starvation rate (1 health per x ticks) of
        the HumanEntity. Default is 80.

        Arguments
        - ticks: the amount of ticks to lose 1 health
        """
        ...


    def getLastDeathLocation(self) -> "Location":
        """
        Gets the player's last death location.

        Returns
        - the last death location if it exists, otherwise null.
        """
        ...


    def setLastDeathLocation(self, location: "Location") -> None:
        """
        Sets the player's last death location.
        
        **Note:** This data is updated in the player's client only when the
        player respawns.

        Arguments
        - location: where to set the last death player location
        """
        ...


    def fireworkBoost(self, fireworkItemStack: "ItemStack") -> "Firework":
        """
        Perform a firework boost.
        
        This method will only work such that .isGliding() is True and
        the entity is actively gliding with an elytra. Additionally, the supplied
        `fireworkItemStack` must be a firework rocket. The power of the boost
        will directly correlate to FireworkMeta.getPower().

        Arguments
        - fireworkItemStack: the firework item stack to use to glide

        Returns
        - the attached Firework, or null if the entity could not
        be boosted

        Raises
        - IllegalArgumentException: if the fireworkItemStack is not a firework
        """
        ...
