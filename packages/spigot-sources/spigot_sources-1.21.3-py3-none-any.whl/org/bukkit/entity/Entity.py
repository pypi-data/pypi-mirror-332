"""
Python module generated from Java source file org.bukkit.entity.Entity

Java source file obtained from artifact spigot-api version 1.21.3-R0.1-20241203.162251-46

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util import UUID
from org.bukkit import EntityEffect
from org.bukkit import Location
from org.bukkit import Nameable
from org.bukkit import Server
from org.bukkit import Sound
from org.bukkit import World
from org.bukkit.block import BlockFace
from org.bukkit.block import PistonMoveReaction
from org.bukkit.command import CommandSender
from org.bukkit.entity import *
from org.bukkit.event.entity import EntityDamageEvent
from org.bukkit.event.player.PlayerTeleportEvent import TeleportCause
from org.bukkit.material import Directional
from org.bukkit.metadata import Metadatable
from org.bukkit.persistence import PersistentDataHolder
from org.bukkit.util import BoundingBox
from org.bukkit.util import Vector
from typing import Any, Callable, Iterable, Tuple


class Entity(Metadatable, CommandSender, Nameable, PersistentDataHolder):
    """
    Represents a base entity in the world
    
    Not all methods are guaranteed to work/may have side effects when
    .isInWorld() is False.
    """

    def getLocation(self) -> "Location":
        """
        Gets the entity's current position

        Returns
        - a new copy of Location containing the position of this entity
        """
        ...


    def getLocation(self, loc: "Location") -> "Location":
        """
        Stores the entity's current position in the provided Location object.
        
        If the provided Location is null this method does nothing and returns
        null.

        Arguments
        - loc: the location to copy into

        Returns
        - The Location object provided or null
        """
        ...


    def setVelocity(self, velocity: "Vector") -> None:
        """
        Sets this entity's velocity in meters per tick

        Arguments
        - velocity: New velocity to travel with
        """
        ...


    def getVelocity(self) -> "Vector":
        """
        Gets this entity's current velocity

        Returns
        - Current traveling velocity of this entity
        """
        ...


    def getHeight(self) -> float:
        """
        Gets the entity's height

        Returns
        - height of entity
        """
        ...


    def getWidth(self) -> float:
        """
        Gets the entity's width

        Returns
        - width of entity
        """
        ...


    def getBoundingBox(self) -> "BoundingBox":
        """
        Gets the entity's current bounding box.
        
        The returned bounding box reflects the entity's current location and
        size.

        Returns
        - the entity's current bounding box
        """
        ...


    def isOnGround(self) -> bool:
        """
        Returns True if the entity is supported by a block. This value is a
        state updated by the server and is not recalculated unless the entity
        moves.

        Returns
        - True if entity is on ground.

        See
        - Player.isOnGround()
        """
        ...


    def isInWater(self) -> bool:
        """
        Returns True if the entity is in water.

        Returns
        - `True` if the entity is in water.
        """
        ...


    def getWorld(self) -> "World":
        """
        Gets the current world this entity resides in

        Returns
        - World
        """
        ...


    def setRotation(self, yaw: float, pitch: float) -> None:
        """
        Sets the entity's rotation.
        
        Note that if the entity is affected by AI, it may override this rotation.

        Arguments
        - yaw: the yaw
        - pitch: the pitch

        Raises
        - UnsupportedOperationException: if used for players
        """
        ...


    def teleport(self, location: "Location") -> bool:
        """
        Teleports this entity to the given location. If this entity is riding a
        vehicle, it will be dismounted prior to teleportation.

        Arguments
        - location: New location to teleport this entity to

        Returns
        - `True` if the teleport was successful
        """
        ...


    def teleport(self, location: "Location", cause: "TeleportCause") -> bool:
        """
        Teleports this entity to the given location. If this entity is riding a
        vehicle, it will be dismounted prior to teleportation.

        Arguments
        - location: New location to teleport this entity to
        - cause: The cause of this teleportation

        Returns
        - `True` if the teleport was successful
        """
        ...


    def teleport(self, destination: "Entity") -> bool:
        """
        Teleports this entity to the target Entity. If this entity is riding a
        vehicle, it will be dismounted prior to teleportation.

        Arguments
        - destination: Entity to teleport this entity to

        Returns
        - `True` if the teleport was successful
        """
        ...


    def teleport(self, destination: "Entity", cause: "TeleportCause") -> bool:
        """
        Teleports this entity to the target Entity. If this entity is riding a
        vehicle, it will be dismounted prior to teleportation.

        Arguments
        - destination: Entity to teleport this entity to
        - cause: The cause of this teleportation

        Returns
        - `True` if the teleport was successful
        """
        ...


    def getNearbyEntities(self, x: float, y: float, z: float) -> list["org.bukkit.entity.Entity"]:
        """
        Returns a list of entities within a bounding box centered around this
        entity

        Arguments
        - x: 1/2 the size of the box along x axis
        - y: 1/2 the size of the box along y axis
        - z: 1/2 the size of the box along z axis

        Returns
        - `List<Entity>` List of entities nearby
        """
        ...


    def getEntityId(self) -> int:
        """
        Returns a unique id for this entity

        Returns
        - Entity id
        """
        ...


    def getFireTicks(self) -> int:
        """
        Returns the entity's current fire ticks (ticks before the entity stops
        being on fire).

        Returns
        - int fireTicks
        """
        ...


    def getMaxFireTicks(self) -> int:
        """
        Returns the entity's maximum fire ticks.

        Returns
        - int maxFireTicks
        """
        ...


    def setFireTicks(self, ticks: int) -> None:
        """
        Sets the entity's current fire ticks (ticks before the entity stops
        being on fire).

        Arguments
        - ticks: Current ticks remaining
        """
        ...


    def setVisualFire(self, fire: bool) -> None:
        """
        Sets if the entity has visual fire (it will always appear to be on fire).

        Arguments
        - fire: whether visual fire is enabled
        """
        ...


    def isVisualFire(self) -> bool:
        """
        Gets if the entity has visual fire (it will always appear to be on fire).

        Returns
        - whether visual fire is enabled
        """
        ...


    def getFreezeTicks(self) -> int:
        """
        Returns the entity's current freeze ticks (amount of ticks the entity has
        been in powdered snow).

        Returns
        - int freeze ticks
        """
        ...


    def getMaxFreezeTicks(self) -> int:
        """
        Returns the entity's maximum freeze ticks (amount of ticks before it will
        be fully frozen)

        Returns
        - int max freeze ticks
        """
        ...


    def setFreezeTicks(self, ticks: int) -> None:
        """
        Sets the entity's current freeze ticks (amount of ticks the entity has
        been in powdered snow).

        Arguments
        - ticks: Current ticks
        """
        ...


    def isFrozen(self) -> bool:
        """
        Gets if the entity is fully frozen (it has been in powdered snow for max
        freeze ticks).

        Returns
        - freeze status
        """
        ...


    def remove(self) -> None:
        """
        Mark the entity's removal.

        Raises
        - UnsupportedOperationException: if you try to remove a Player use Player.kickPlayer(String) in this case instead
        """
        ...


    def isDead(self) -> bool:
        """
        Returns True if this entity has been marked for removal.

        Returns
        - True if it is dead.
        """
        ...


    def isValid(self) -> bool:
        """
        Returns False if the entity has died, been despawned for some other
        reason, or has not been added to the world.

        Returns
        - True if valid.
        """
        ...


    def getServer(self) -> "Server":
        """
        Gets the Server that contains this Entity

        Returns
        - Server instance running this Entity
        """
        ...


    def isPersistent(self) -> bool:
        """
        Returns True if the entity gets persisted.
        
        By default all entities are persistent. An entity will also not get
        persisted, if it is riding an entity that is not persistent.
        
        The persistent flag on players controls whether or not to save their
        playerdata file when they quit. If a player is directly or indirectly
        riding a non-persistent entity, the vehicle at the root and all its
        passengers won't get persisted.
        
        **This should not be confused with
        LivingEntity.setRemoveWhenFarAway(boolean) which controls
        despawning of living entities. **

        Returns
        - True if this entity is persistent
        """
        ...


    def setPersistent(self, persistent: bool) -> None:
        """
        Sets whether or not the entity gets persisted.

        Arguments
        - persistent: the persistence status

        See
        - .isPersistent()
        """
        ...


    def getPassenger(self) -> "Entity":
        """
        Gets the primary passenger of a vehicle. For vehicles that could have
        multiple passengers, this will only return the primary passenger.

        Returns
        - an entity

        Deprecated
        - entities may have multiple passengers, use
        .getPassengers()
        """
        ...


    def setPassenger(self, passenger: "Entity") -> bool:
        """
        Set the passenger of a vehicle.

        Arguments
        - passenger: The new passenger.

        Returns
        - False if it could not be done for whatever reason

        Deprecated
        - entities may have multiple passengers, use
        .addPassenger(org.bukkit.entity.Entity)
        """
        ...


    def getPassengers(self) -> list["Entity"]:
        """
        Gets a list of passengers of this vehicle.
        
        The returned list will not be directly linked to the entity's current
        passengers, and no guarantees are made as to its mutability.

        Returns
        - list of entities corresponding to current passengers.
        """
        ...


    def addPassenger(self, passenger: "Entity") -> bool:
        """
        Add a passenger to the vehicle.

        Arguments
        - passenger: The passenger to add

        Returns
        - False if it could not be done for whatever reason
        """
        ...


    def removePassenger(self, passenger: "Entity") -> bool:
        """
        Remove a passenger from the vehicle.

        Arguments
        - passenger: The passenger to remove

        Returns
        - False if it could not be done for whatever reason
        """
        ...


    def isEmpty(self) -> bool:
        """
        Check if a vehicle has passengers.

        Returns
        - True if the vehicle has no passengers.
        """
        ...


    def eject(self) -> bool:
        """
        Eject any passenger.

        Returns
        - True if there was a passenger.
        """
        ...


    def getFallDistance(self) -> float:
        """
        Returns the distance this entity has fallen

        Returns
        - The distance.
        """
        ...


    def setFallDistance(self, distance: float) -> None:
        """
        Sets the fall distance for this entity

        Arguments
        - distance: The new distance.
        """
        ...


    def setLastDamageCause(self, event: "EntityDamageEvent") -> None:
        """
        Record the last EntityDamageEvent inflicted on this entity

        Arguments
        - event: a EntityDamageEvent

        Deprecated
        - method is for internal use only and will be removed
        """
        ...


    def getLastDamageCause(self) -> "EntityDamageEvent":
        """
        Retrieve the last EntityDamageEvent inflicted on this entity.
        This event may have been cancelled.

        Returns
        - the last known EntityDamageEvent or null if hitherto
            unharmed
        """
        ...


    def getUniqueId(self) -> "UUID":
        """
        Returns a unique and persistent id for this entity

        Returns
        - unique id
        """
        ...


    def getTicksLived(self) -> int:
        """
        Gets the amount of ticks this entity has lived for.
        
        This is the equivalent to "age" in entities.

        Returns
        - Age of entity
        """
        ...


    def setTicksLived(self, value: int) -> None:
        """
        Sets the amount of ticks this entity has lived for.
        
        This is the equivalent to "age" in entities. May not be less than one
        tick.

        Arguments
        - value: Age of entity
        """
        ...


    def playEffect(self, type: "EntityEffect") -> None:
        """
        Performs the specified EntityEffect for this entity.
        
        This will be viewable to all players near the entity.
        
        If the effect is not applicable to this class of entity, it will not play.

        Arguments
        - type: Effect to play.
        """
        ...


    def getType(self) -> "EntityType":
        """
        Get the type of the entity.

        Returns
        - The entity type.
        """
        ...


    def getSwimSound(self) -> "Sound":
        """
        Get the Sound this entity makes while swimming.

        Returns
        - the swimming sound
        """
        ...


    def getSwimSplashSound(self) -> "Sound":
        """
        Get the Sound this entity makes when splashing in water. For most
        entities, this is just Sound.ENTITY_GENERIC_SPLASH.

        Returns
        - the splash sound
        """
        ...


    def getSwimHighSpeedSplashSound(self) -> "Sound":
        """
        Get the Sound this entity makes when splashing in water at high
        speeds. For most entities, this is just Sound.ENTITY_GENERIC_SPLASH.

        Returns
        - the splash sound
        """
        ...


    def isInsideVehicle(self) -> bool:
        """
        Returns whether this entity is inside a vehicle.

        Returns
        - True if the entity is in a vehicle.
        """
        ...


    def leaveVehicle(self) -> bool:
        """
        Leave the current vehicle. If the entity is currently in a vehicle (and
        is removed from it), True will be returned, otherwise False will be
        returned.

        Returns
        - True if the entity was in a vehicle.
        """
        ...


    def getVehicle(self) -> "Entity":
        """
        Get the vehicle that this entity is inside. If there is no vehicle,
        null will be returned.

        Returns
        - The current vehicle.
        """
        ...


    def setCustomNameVisible(self, flag: bool) -> None:
        """
        Sets whether or not to display the mob's custom name client side. The
        name will be displayed above the mob similarly to a player.
        
        This value has no effect on players, they will always display their
        name.

        Arguments
        - flag: custom name or not
        """
        ...


    def isCustomNameVisible(self) -> bool:
        """
        Gets whether or not the mob's custom name is displayed client side.
        
        This value has no effect on players, they will always display their
        name.

        Returns
        - if the custom name is displayed
        """
        ...


    def setVisibleByDefault(self, visible: bool) -> None:
        """
        Sets whether or not this entity is visible by default.
        
        If this entity is not visible by default, then
        Player.showEntity(org.bukkit.plugin.Plugin, org.bukkit.entity.Entity)
        will need to be called before the entity is visible to a given player.

        Arguments
        - visible: default visibility status
        """
        ...


    def isVisibleByDefault(self) -> bool:
        """
        Gets whether or not this entity is visible by default.
        
        If this entity is not visible by default, then
        Player.showEntity(org.bukkit.plugin.Plugin, org.bukkit.entity.Entity)
        will need to be called before the entity is visible to a given player.

        Returns
        - default visibility status
        """
        ...


    def getTrackedBy(self) -> set["Player"]:
        """
        Get all players that are currently tracking this entity.
        
        'Tracking' means that this entity has been sent to the player and that
        they are receiving updates on its state. Note that the client's `'Entity Distance'` setting does not affect the range at which entities
        are tracked.

        Returns
        - the players tracking this entity, or an empty set if none
        """
        ...


    def setGlowing(self, flag: bool) -> None:
        """
        Sets whether the entity has a team colored (default: white) glow.
        
        **nb: this refers to the 'Glowing' entity property, not whether a
        glowing potion effect is applied**

        Arguments
        - flag: if the entity is glowing
        """
        ...


    def isGlowing(self) -> bool:
        """
        Gets whether the entity is glowing or not.
        
        **nb: this refers to the 'Glowing' entity property, not whether a
        glowing potion effect is applied**

        Returns
        - whether the entity is glowing
        """
        ...


    def setInvulnerable(self, flag: bool) -> None:
        """
        Sets whether the entity is invulnerable or not.
        
        When an entity is invulnerable it can only be damaged by players in
        creative mode.

        Arguments
        - flag: if the entity is invulnerable
        """
        ...


    def isInvulnerable(self) -> bool:
        """
        Gets whether the entity is invulnerable or not.

        Returns
        - whether the entity is
        """
        ...


    def isSilent(self) -> bool:
        """
        Gets whether the entity is silent or not.

        Returns
        - whether the entity is silent.
        """
        ...


    def setSilent(self, flag: bool) -> None:
        """
        Sets whether the entity is silent or not.
        
        When an entity is silent it will not produce any sound.

        Arguments
        - flag: if the entity is silent
        """
        ...


    def hasGravity(self) -> bool:
        """
        Returns whether gravity applies to this entity.

        Returns
        - whether gravity applies
        """
        ...


    def setGravity(self, gravity: bool) -> None:
        """
        Sets whether gravity applies to this entity.

        Arguments
        - gravity: whether gravity should apply
        """
        ...


    def getPortalCooldown(self) -> int:
        """
        Gets the period of time (in ticks) before this entity can use a portal.

        Returns
        - portal cooldown ticks
        """
        ...


    def setPortalCooldown(self, cooldown: int) -> None:
        """
        Sets the period of time (in ticks) before this entity can use a portal.

        Arguments
        - cooldown: portal cooldown ticks
        """
        ...


    def getScoreboardTags(self) -> set[str]:
        """
        Returns a set of tags for this entity.
        
        Entities can have no more than 1024 tags.

        Returns
        - a set of tags for this entity
        """
        ...


    def addScoreboardTag(self, tag: str) -> bool:
        """
        Add a tag to this entity.
        
        Entities can have no more than 1024 tags.

        Arguments
        - tag: the tag to add

        Returns
        - True if the tag was successfully added
        """
        ...


    def removeScoreboardTag(self, tag: str) -> bool:
        """
        Removes a given tag from this entity.

        Arguments
        - tag: the tag to remove

        Returns
        - True if the tag was successfully removed
        """
        ...


    def getPistonMoveReaction(self) -> "PistonMoveReaction":
        """
        Returns the reaction of the entity when moved by a piston.

        Returns
        - reaction
        """
        ...


    def getFacing(self) -> "BlockFace":
        """
        Get the closest cardinal BlockFace direction an entity is
        currently facing.
        
        This will not return any non-cardinal directions such as
        BlockFace.UP or BlockFace.DOWN.
        
        Hanging entities will override this call and thus their behavior
        may be different.

        Returns
        - the entity's current cardinal facing.

        See
        - Directional.getFacing()
        """
        ...


    def getPose(self) -> "Pose":
        """
        Gets the entity's current pose.
        
        **Note that the pose is only updated at the end of a tick, so may be
        inconsistent with other methods. eg Player.isSneaking() being
        True does not imply the current pose will be Pose.SNEAKING**

        Returns
        - current pose
        """
        ...


    def getSpawnCategory(self) -> "SpawnCategory":
        """
        Get the category of spawn to which this entity belongs.

        Returns
        - the entity´s category spawn
        """
        ...


    def isInWorld(self) -> bool:
        """
        Checks if this entity has been spawned in a world. 
        Entities not spawned in a world will not tick, be sent to players, or be
        saved to the server files.

        Returns
        - whether the entity has been spawned in a world
        """
        ...


    def getAsString(self) -> str:
        """
        Get this entity as an NBT string.
        
        This string should not be relied upon as a serializable value.

        Returns
        - the NBT string or null if one cannot be made
        """
        ...


    def createSnapshot(self) -> "EntitySnapshot":
        """
        Crates an EntitySnapshot representing the current state of this entity.

        Returns
        - a snapshot representing this entity or null if one cannot be made
        """
        ...


    def copy(self) -> "Entity":
        """
        Creates a copy of this entity and all its data. Does not spawn the copy in
        the world. 
        **Note:** Players cannot be copied.

        Returns
        - a copy of this entity.
        """
        ...


    def copy(self, to: "Location") -> "Entity":
        """
        Creates a copy of this entity and all its data. Spawns the copy at the given location. 
        **Note:** Players cannot be copied.

        Arguments
        - to: the location to copy to

        Returns
        - a copy of this entity.
        """
        ...


    def spigot(self) -> "Spigot":
        ...


    class Spigot(Spigot):


