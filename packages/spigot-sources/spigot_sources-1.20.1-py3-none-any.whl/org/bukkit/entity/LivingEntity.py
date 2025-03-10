"""
Python module generated from Java source file org.bukkit.entity.LivingEntity

Java source file obtained from artifact spigot-api version 1.20.1-R0.1-20230921.163938-66

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util import UUID
from org.bukkit import FluidCollisionMode
from org.bukkit import Location
from org.bukkit import Material
from org.bukkit import Sound
from org.bukkit import World
from org.bukkit.attribute import Attributable
from org.bukkit.block import Block
from org.bukkit.entity import *
from org.bukkit.entity.memory import MemoryKey
from org.bukkit.inventory import EntityEquipment
from org.bukkit.inventory import ItemStack
from org.bukkit.potion import PotionEffect
from org.bukkit.potion import PotionEffectType
from org.bukkit.projectiles import ProjectileSource
from org.bukkit.util import RayTraceResult
from org.bukkit.util import Vector
from typing import Any, Callable, Iterable, Tuple


class LivingEntity(Attributable, Damageable, ProjectileSource):
    """
    Represents a living entity, such as a monster or player
    """

    def getEyeHeight(self) -> float:
        """
        Gets the height of the living entity's eyes above its Location.

        Returns
        - height of the living entity's eyes above its location
        """
        ...


    def getEyeHeight(self, ignorePose: bool) -> float:
        """
        Gets the height of the living entity's eyes above its Location.

        Arguments
        - ignorePose: if set to True, the effects of pose changes, eg
            sneaking and gliding will be ignored

        Returns
        - height of the living entity's eyes above its location
        """
        ...


    def getEyeLocation(self) -> "Location":
        """
        Get a Location detailing the current eye position of the living entity.

        Returns
        - a location at the eyes of the living entity
        """
        ...


    def getLineOfSight(self, transparent: set["Material"], maxDistance: int) -> list["Block"]:
        """
        Gets all blocks along the living entity's line of sight.
        
        This list contains all blocks from the living entity's eye position to
        target inclusive. This method considers all blocks as 1x1x1 in size.

        Arguments
        - transparent: Set containing all transparent block Materials (set to
            null for only air)
        - maxDistance: this is the maximum distance to scan (may be limited
            by server by at least 100 blocks, no less)

        Returns
        - list containing all blocks along the living entity's line of
            sight
        """
        ...


    def getTargetBlock(self, transparent: set["Material"], maxDistance: int) -> "Block":
        """
        Gets the block that the living entity has targeted.
        
        This method considers all blocks as 1x1x1 in size. To take exact block
        collision shapes into account, see .getTargetBlockExact(int,
        FluidCollisionMode).

        Arguments
        - transparent: Set containing all transparent block Materials (set to
            null for only air)
        - maxDistance: this is the maximum distance to scan (may be limited
            by server by at least 100 blocks, no less)

        Returns
        - block that the living entity has targeted
        """
        ...


    def getLastTwoTargetBlocks(self, transparent: set["Material"], maxDistance: int) -> list["Block"]:
        """
        Gets the last two blocks along the living entity's line of sight.
        
        The target block will be the last block in the list. This method
        considers all blocks as 1x1x1 in size.

        Arguments
        - transparent: Set containing all transparent block Materials (set to
            null for only air)
        - maxDistance: this is the maximum distance to scan. This may be
            further limited by the server, but never to less than 100 blocks

        Returns
        - list containing the last 2 blocks along the living entity's
            line of sight
        """
        ...


    def getTargetBlockExact(self, maxDistance: int) -> "Block":
        """
        Gets the block that the living entity has targeted.
        
        This takes the blocks' precise collision shapes into account. Fluids are
        ignored.
        
        This may cause loading of chunks! Some implementations may impose
        artificial restrictions on the maximum distance.

        Arguments
        - maxDistance: the maximum distance to scan

        Returns
        - block that the living entity has targeted

        See
        - .getTargetBlockExact(int, org.bukkit.FluidCollisionMode)
        """
        ...


    def getTargetBlockExact(self, maxDistance: int, fluidCollisionMode: "FluidCollisionMode") -> "Block":
        """
        Gets the block that the living entity has targeted.
        
        This takes the blocks' precise collision shapes into account.
        
        This may cause loading of chunks! Some implementations may impose
        artificial restrictions on the maximum distance.

        Arguments
        - maxDistance: the maximum distance to scan
        - fluidCollisionMode: the fluid collision mode

        Returns
        - block that the living entity has targeted

        See
        - .rayTraceBlocks(double, FluidCollisionMode)
        """
        ...


    def rayTraceBlocks(self, maxDistance: float) -> "RayTraceResult":
        """
        Performs a ray trace that provides information on the targeted block.
        
        This takes the blocks' precise collision shapes into account. Fluids are
        ignored.
        
        This may cause loading of chunks! Some implementations may impose
        artificial restrictions on the maximum distance.

        Arguments
        - maxDistance: the maximum distance to scan

        Returns
        - information on the targeted block, or `null` if there
            is no targeted block in range

        See
        - .rayTraceBlocks(double, FluidCollisionMode)
        """
        ...


    def rayTraceBlocks(self, maxDistance: float, fluidCollisionMode: "FluidCollisionMode") -> "RayTraceResult":
        """
        Performs a ray trace that provides information on the targeted block.
        
        This takes the blocks' precise collision shapes into account.
        
        This may cause loading of chunks! Some implementations may impose
        artificial restrictions on the maximum distance.

        Arguments
        - maxDistance: the maximum distance to scan
        - fluidCollisionMode: the fluid collision mode

        Returns
        - information on the targeted block, or `null` if there
            is no targeted block in range

        See
        - World.rayTraceBlocks(Location, Vector, double, FluidCollisionMode)
        """
        ...


    def getRemainingAir(self) -> int:
        """
        Returns the amount of air that the living entity has remaining, in
        ticks.

        Returns
        - amount of air remaining
        """
        ...


    def setRemainingAir(self, ticks: int) -> None:
        """
        Sets the amount of air that the living entity has remaining, in ticks.

        Arguments
        - ticks: amount of air remaining
        """
        ...


    def getMaximumAir(self) -> int:
        """
        Returns the maximum amount of air the living entity can have, in ticks.

        Returns
        - maximum amount of air
        """
        ...


    def setMaximumAir(self, ticks: int) -> None:
        """
        Sets the maximum amount of air the living entity can have, in ticks.

        Arguments
        - ticks: maximum amount of air
        """
        ...


    def getArrowCooldown(self) -> int:
        """
        Gets the time in ticks until the next arrow leaves the entity's body.

        Returns
        - ticks until arrow leaves
        """
        ...


    def setArrowCooldown(self, ticks: int) -> None:
        """
        Sets the time in ticks until the next arrow leaves the entity's body.

        Arguments
        - ticks: time until arrow leaves
        """
        ...


    def getArrowsInBody(self) -> int:
        """
        Gets the amount of arrows in an entity's body.

        Returns
        - amount of arrows in body
        """
        ...


    def setArrowsInBody(self, count: int) -> None:
        """
        Set the amount of arrows in the entity's body.

        Arguments
        - count: amount of arrows in entity's body
        """
        ...


    def getMaximumNoDamageTicks(self) -> int:
        """
        Returns the living entity's current maximum no damage ticks.
        
        This is the maximum duration in which the living entity will not take
        damage.

        Returns
        - maximum no damage ticks
        """
        ...


    def setMaximumNoDamageTicks(self, ticks: int) -> None:
        """
        Sets the living entity's current maximum no damage ticks.

        Arguments
        - ticks: maximum amount of no damage ticks
        """
        ...


    def getLastDamage(self) -> float:
        """
        Returns the living entity's last damage taken in the current no damage
        ticks time.
        
        Only damage higher than this amount will further damage the living
        entity.

        Returns
        - damage taken since the last no damage ticks time period
        """
        ...


    def setLastDamage(self, damage: float) -> None:
        """
        Sets the damage dealt within the current no damage ticks time period.

        Arguments
        - damage: amount of damage
        """
        ...


    def getNoDamageTicks(self) -> int:
        """
        Returns the living entity's current no damage ticks.

        Returns
        - amount of no damage ticks
        """
        ...


    def setNoDamageTicks(self, ticks: int) -> None:
        """
        Sets the living entity's current no damage ticks.

        Arguments
        - ticks: amount of no damage ticks
        """
        ...


    def getNoActionTicks(self) -> int:
        """
        Get the ticks that this entity has performed no action.
        
        The details of what "no action ticks" entails varies from entity to entity
        and cannot be specifically defined. Some examples include squid using this
        value to determine when to swim, raiders for when they are to be expelled
        from raids, or creatures (such as withers) as a requirement to be despawned.

        Returns
        - amount of no action ticks
        """
        ...


    def setNoActionTicks(self, ticks: int) -> None:
        """
        Set the ticks that this entity has performed no action.
        
        The details of what "no action ticks" entails varies from entity to entity
        and cannot be specifically defined. Some examples include squid using this
        value to determine when to swim, raiders for when they are to be expelled
        from raids, or creatures (such as withers) as a requirement to be despawned.

        Arguments
        - ticks: amount of no action ticks
        """
        ...


    def getKiller(self) -> "Player":
        """
        Gets the player identified as the killer of the living entity.
        
        May be null.

        Returns
        - killer player, or null if none found
        """
        ...


    def addPotionEffect(self, effect: "PotionEffect") -> bool:
        """
        Adds the given PotionEffect to the living entity.

        Arguments
        - effect: PotionEffect to be added

        Returns
        - whether the effect could be added
        """
        ...


    def addPotionEffect(self, effect: "PotionEffect", force: bool) -> bool:
        """
        Adds the given PotionEffect to the living entity.
        
        Only one potion effect can be present for a given PotionEffectType.

        Arguments
        - effect: PotionEffect to be added
        - force: whether conflicting effects should be removed

        Returns
        - whether the effect could be added

        Deprecated
        - no need to force since multiple effects of the same type are
        now supported.
        """
        ...


    def addPotionEffects(self, effects: Iterable["PotionEffect"]) -> bool:
        """
        Attempts to add all of the given PotionEffect to the living
        entity.

        Arguments
        - effects: the effects to add

        Returns
        - whether all of the effects could be added
        """
        ...


    def hasPotionEffect(self, type: "PotionEffectType") -> bool:
        """
        Returns whether the living entity already has an existing effect of
        the given PotionEffectType applied to it.

        Arguments
        - type: the potion type to check

        Returns
        - whether the living entity has this potion effect active on them
        """
        ...


    def getPotionEffect(self, type: "PotionEffectType") -> "PotionEffect":
        """
        Returns the active PotionEffect of the specified type.
        
        If the effect is not present on the entity then null will be returned.

        Arguments
        - type: the potion type to check

        Returns
        - the effect active on this entity, or null if not active.
        """
        ...


    def removePotionEffect(self, type: "PotionEffectType") -> None:
        """
        Removes any effects present of the given PotionEffectType.

        Arguments
        - type: the potion type to remove
        """
        ...


    def getActivePotionEffects(self) -> Iterable["PotionEffect"]:
        """
        Returns all currently active PotionEffects on the living
        entity.

        Returns
        - a collection of PotionEffects
        """
        ...


    def hasLineOfSight(self, other: "Entity") -> bool:
        """
        Checks whether the living entity has block line of sight to another.
        
        This uses the same algorithm that hostile mobs use to find the closest
        player.

        Arguments
        - other: the entity to determine line of sight to

        Returns
        - True if there is a line of sight, False if not
        """
        ...


    def getRemoveWhenFarAway(self) -> bool:
        """
        Returns if the living entity despawns when away from players or not.
        
        By default, animals are not removed while other mobs are.

        Returns
        - True if the living entity is removed when away from players
        """
        ...


    def setRemoveWhenFarAway(self, remove: bool) -> None:
        """
        Sets whether or not the living entity despawns when away from players
        or not.

        Arguments
        - remove: the removal status
        """
        ...


    def getEquipment(self) -> "EntityEquipment":
        """
        Gets the inventory with the equipment worn by the living entity.

        Returns
        - the living entity's inventory
        """
        ...


    def setCanPickupItems(self, pickup: bool) -> None:
        """
        Sets whether or not the living entity can pick up items.

        Arguments
        - pickup: whether or not the living entity can pick up items
        """
        ...


    def getCanPickupItems(self) -> bool:
        """
        Gets if the living entity can pick up items.

        Returns
        - whether or not the living entity can pick up items
        """
        ...


    def isLeashed(self) -> bool:
        """
        Returns whether the entity is currently leashed.

        Returns
        - whether the entity is leashed
        """
        ...


    def getLeashHolder(self) -> "Entity":
        """
        Gets the entity that is currently leading this entity.

        Returns
        - the entity holding the leash

        Raises
        - IllegalStateException: if not currently leashed
        """
        ...


    def setLeashHolder(self, holder: "Entity") -> bool:
        """
        Sets the leash on this entity to be held by the supplied entity.
        
        This method has no effect on EnderDragons, Withers, Players, or Bats.
        Non-living entities excluding leashes will not persist as leash
        holders.

        Arguments
        - holder: the entity to leash this entity to, or null to unleash

        Returns
        - whether the operation was successful
        """
        ...


    def isGliding(self) -> bool:
        """
        Checks to see if an entity is gliding, such as using an Elytra.

        Returns
        - True if this entity is gliding.
        """
        ...


    def setGliding(self, gliding: bool) -> None:
        """
        Makes entity start or stop gliding. This will work even if an Elytra
        is not equipped, but will be reverted by the server immediately after
        unless an event-cancelling mechanism is put in place.

        Arguments
        - gliding: True if the entity is gliding.
        """
        ...


    def isSwimming(self) -> bool:
        """
        Checks to see if an entity is swimming.

        Returns
        - True if this entity is swimming.
        """
        ...


    def setSwimming(self, swimming: bool) -> None:
        """
        Makes entity start or stop swimming.
        
        This may have unexpected results if the entity is not in water.

        Arguments
        - swimming: True if the entity is swimming.
        """
        ...


    def isRiptiding(self) -> bool:
        """
        Checks to see if an entity is currently using the Riptide enchantment.

        Returns
        - True if this entity is currently riptiding.
        """
        ...


    def isSleeping(self) -> bool:
        """
        Returns whether this entity is slumbering.

        Returns
        - slumber state
        """
        ...


    def isClimbing(self) -> bool:
        """
        Gets if the entity is climbing.

        Returns
        - if the entity is climbing
        """
        ...


    def setAI(self, ai: bool) -> None:
        """
        Sets whether an entity will have AI.
        
        The entity will be completely unable to move if it has no AI.

        Arguments
        - ai: whether the mob will have AI or not.
        """
        ...


    def hasAI(self) -> bool:
        """
        Checks whether an entity has AI.
        
        The entity will be completely unable to move if it has no AI.

        Returns
        - True if the entity has AI, otherwise False.
        """
        ...


    def attack(self, target: "Entity") -> None:
        """
        Makes this entity attack the given entity with a melee attack.
        
        Attack damage is calculated by the server from the attributes and
        equipment of this mob, and knockback is applied to `target` as
        appropriate.

        Arguments
        - target: entity to attack.
        """
        ...


    def swingMainHand(self) -> None:
        """
        Makes this entity swing their main hand.
        
        This method does nothing if this entity does not have an animation for
        swinging their main hand.
        """
        ...


    def swingOffHand(self) -> None:
        """
        Makes this entity swing their off hand.
        
        This method does nothing if this entity does not have an animation for
        swinging their off hand.
        """
        ...


    def playHurtAnimation(self, yaw: float) -> None:
        """
        Makes this entity flash red as if they were damaged.

        Arguments
        - yaw: The direction the damage is coming from in relation to the
        entity, where 0 is in front of the player, 90 is to the right, 180 is
        behind, and 270 is to the left
        """
        ...


    def setCollidable(self, collidable: bool) -> None:
        """
        Set if this entity will be subject to collisions with other entities.
        
        Exemptions to this rule can be managed with
        .getCollidableExemptions()

        Arguments
        - collidable: collision status
        """
        ...


    def isCollidable(self) -> bool:
        """
        Gets if this entity is subject to collisions with other entities.
        
        Some entities might be exempted from the collidable rule of this entity.
        Use .getCollidableExemptions() to get these.
        
        Please note that this method returns only the custom collidable state,
        not whether the entity is non-collidable for other reasons such as being
        dead.

        Returns
        - collision status
        """
        ...


    def getCollidableExemptions(self) -> set["UUID"]:
        """
        Gets a mutable set of UUIDs of the entities which are exempt from the
        entity's collidable rule and which's collision with this entity will
        behave the opposite of it.
        
        This set can be modified to add or remove exemptions.
        
        For example if collidable is True and an entity is in the exemptions set
        then it will not collide with it. Similarly if collidable is False and an
        entity is in this set then it will still collide with it.
        
        Note these exemptions are not (currently) persistent.

        Returns
        - the collidable exemption set
        """
        ...


    def getMemory(self, memoryKey: "MemoryKey"["T"]) -> "T":
        """
        Returns the value of the memory specified.
        
        Note that the value is null when the specific entity does not have that
        value by default.
        
        Type `<T>`: the type of the return value

        Arguments
        - memoryKey: memory to access

        Returns
        - a instance of the memory section value or null if not present
        """
        ...


    def setMemory(self, memoryKey: "MemoryKey"["T"], memoryValue: "T") -> None:
        """
        Sets the value of the memory specified.
        
        Note that the value will not be persisted when the specific entity does
        not have that value by default.
        
        Type `<T>`: the type of the passed value

        Arguments
        - memoryKey: the memory to access
        - memoryValue: a typed memory value
        """
        ...


    def getHurtSound(self) -> "Sound":
        """
        Get the Sound this entity will make when damaged.

        Returns
        - the hurt sound, or null if the entity does not make any sound
        """
        ...


    def getDeathSound(self) -> "Sound":
        """
        Get the Sound this entity will make on death.

        Returns
        - the death sound, or null if the entity does not make any sound
        """
        ...


    def getFallDamageSound(self, fallHeight: int) -> "Sound":
        """
        Get the Sound this entity will make when falling from the given
        height (in blocks). The sound will often differ between either a small
        or a big fall damage sound if the height exceeds 4 blocks.

        Arguments
        - fallHeight: the fall height in blocks

        Returns
        - the fall damage sound

        See
        - .getFallDamageSoundBig()
        """
        ...


    def getFallDamageSoundSmall(self) -> "Sound":
        """
        Get the Sound this entity will make when falling from a small
        height.

        Returns
        - the fall damage sound
        """
        ...


    def getFallDamageSoundBig(self) -> "Sound":
        """
        Get the Sound this entity will make when falling from a large
        height.

        Returns
        - the fall damage sound
        """
        ...


    def getDrinkingSound(self, itemStack: "ItemStack") -> "Sound":
        """
        Get the Sound this entity will make when drinking the given
        ItemStack.

        Arguments
        - itemStack: the item stack being drank

        Returns
        - the drinking sound
        """
        ...


    def getEatingSound(self, itemStack: "ItemStack") -> "Sound":
        """
        Get the Sound this entity will make when eating the given
        ItemStack.

        Arguments
        - itemStack: the item stack being eaten

        Returns
        - the eating sound
        """
        ...


    def canBreatheUnderwater(self) -> bool:
        """
        Returns True if this entity can breathe underwater and will not take
        suffocation damage when its air supply reaches zero.

        Returns
        - `True` if the entity can breathe underwater
        """
        ...


    def getCategory(self) -> "EntityCategory":
        """
        Get the category to which this entity belongs.
        
        Categories may subject this entity to additional effects, benefits or
        debuffs.

        Returns
        - the entity category
        """
        ...


    def setInvisible(self, invisible: bool) -> None:
        """
        Sets whether the entity is invisible or not.

        Arguments
        - invisible: If the entity is invisible
        """
        ...


    def isInvisible(self) -> bool:
        """
        Gets whether the entity is invisible or not.

        Returns
        - Whether the entity is invisible
        """
        ...
