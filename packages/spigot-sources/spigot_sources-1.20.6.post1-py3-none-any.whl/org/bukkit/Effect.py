"""
Python module generated from Java source file org.bukkit.Effect

Java source file obtained from artifact spigot-api version 1.20.6-R0.1-20240613.150924-57

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.collect import Maps
from enum import Enum
from org.bukkit import *
from org.bukkit.block import BlockFace
from typing import Any, Callable, Iterable, Tuple


class Effect(Enum):
    """
    A list of effects that the server is able to send to players.
    """

    CLICK2 = (1000, Type.SOUND)
    """
    An alternate click sound.
    """
    CLICK1 = (1001, Type.SOUND)
    """
    A click sound.
    """
    BOW_FIRE = (1002, Type.SOUND)
    """
    Sound of a bow firing.
    """
    DOOR_TOGGLE = (1006, Type.SOUND)
    """
    Sound of a door opening.

    See
    - Sound.BLOCK_WOODEN_DOOR_OPEN

    Deprecated
    - no longer exists
    """
    IRON_DOOR_TOGGLE = (1005, Type.SOUND)
    """
    Sound of a door opening.

    See
    - Sound.BLOCK_IRON_DOOR_OPEN

    Deprecated
    - no longer exists
    """
    TRAPDOOR_TOGGLE = (1007, Type.SOUND)
    """
    Sound of a trapdoor opening.

    See
    - Sound.BLOCK_WOODEN_TRAPDOOR_OPEN

    Deprecated
    - no longer exists
    """
    IRON_TRAPDOOR_TOGGLE = (1037, Type.SOUND)
    """
    Sound of a door opening.

    See
    - Sound.BLOCK_IRON_TRAPDOOR_OPEN

    Deprecated
    - no longer exists
    """
    FENCE_GATE_TOGGLE = (1008, Type.SOUND)
    """
    Sound of a door opening.

    See
    - Sound.BLOCK_FENCE_GATE_OPEN

    Deprecated
    - no longer exists
    """
    DOOR_CLOSE = (1012, Type.SOUND)
    """
    Sound of a door closing.

    See
    - Sound.BLOCK_WOODEN_DOOR_CLOSE

    Deprecated
    - no longer exists
    """
    IRON_DOOR_CLOSE = (1011, Type.SOUND)
    """
    Sound of a door closing.

    See
    - Sound.BLOCK_IRON_DOOR_CLOSE

    Deprecated
    - no longer exists
    """
    TRAPDOOR_CLOSE = (1013, Type.SOUND)
    """
    Sound of a trapdoor closing.

    See
    - Sound.BLOCK_WOODEN_TRAPDOOR_CLOSE

    Deprecated
    - no longer exists
    """
    IRON_TRAPDOOR_CLOSE = (1036, Type.SOUND)
    """
    Sound of a door closing.

    See
    - Sound.BLOCK_IRON_TRAPDOOR_CLOSE

    Deprecated
    - no longer exists
    """
    FENCE_GATE_CLOSE = (1014, Type.SOUND)
    """
    Sound of a door closing.

    See
    - Sound.BLOCK_FENCE_GATE_CLOSE

    Deprecated
    - no longer exists
    """
    EXTINGUISH = (1009, Type.SOUND)
    """
    Sound of fire being extinguished.
    """
    RECORD_PLAY = (1010, Type.SOUND, Material)
    """
    A song from a record. Needs the record item ID as additional info
    """
    GHAST_SHRIEK = (1015, Type.SOUND)
    """
    Sound of ghast shrieking.
    """
    GHAST_SHOOT = (1016, Type.SOUND)
    """
    Sound of ghast firing.
    """
    BLAZE_SHOOT = (1018, Type.SOUND)
    """
    Sound of blaze firing.
    """
    ZOMBIE_CHEW_WOODEN_DOOR = (1019, Type.SOUND)
    """
    Sound of zombies chewing on wooden doors.
    """
    ZOMBIE_CHEW_IRON_DOOR = (1020, Type.SOUND)
    """
    Sound of zombies chewing on iron doors.
    """
    ZOMBIE_DESTROY_DOOR = (1021, Type.SOUND)
    """
    Sound of zombies destroying a door.
    """
    SMOKE = (2000, Type.VISUAL, BlockFace)
    """
    A visual smoke effect. Needs direction as additional info.
    """
    STEP_SOUND = (2001, Type.SOUND, Material)
    """
    Sound of a block breaking. Needs block ID as additional info.
    """
    POTION_BREAK = (2002, Type.VISUAL, Color)
    """
    Visual effect of a splash potion breaking. Needs potion data value as
    additional info.
    """
    INSTANT_POTION_BREAK = (2007, Type.VISUAL, Color)
    """
    Visual effect of an instant splash potion breaking. Needs color data
    value as additional info.
    """
    ENDER_SIGNAL = (2003, Type.VISUAL)
    """
    An ender eye signal; a visual effect.
    """
    MOBSPAWNER_FLAMES = (2004, Type.VISUAL)
    """
    The flames seen on a mobspawner; a visual effect.
    """
    BREWING_STAND_BREW = (1035, Type.SOUND)
    """
    The sound played by brewing stands when brewing
    """
    CHORUS_FLOWER_GROW = (1033, Type.SOUND)
    """
    The sound played when a chorus flower grows
    """
    CHORUS_FLOWER_DEATH = (1034, Type.SOUND)
    """
    The sound played when a chorus flower dies
    """
    PORTAL_TRAVEL = (1032, Type.SOUND)
    """
    The sound played when traveling through a portal
    """
    ENDEREYE_LAUNCH = (1003, Type.SOUND)
    """
    The sound played when launching an endereye
    """
    FIREWORK_SHOOT = (1004, Type.SOUND)
    """
    The sound played when launching a firework
    """
    VILLAGER_PLANT_GROW = (2005, Type.VISUAL, Integer)
    """
    Particles displayed when a villager grows a plant, data
    is the number of particles
    """
    DRAGON_BREATH = (2006, Type.VISUAL)
    """
    The sound/particles used by the enderdragon's breath
    attack.
    """
    ANVIL_BREAK = (1029, Type.SOUND)
    """
    The sound played when an anvil breaks
    """
    ANVIL_USE = (1030, Type.SOUND)
    """
    The sound played when an anvil is used
    """
    ANVIL_LAND = (1031, Type.SOUND)
    """
    The sound played when an anvil lands after
    falling
    """
    ENDERDRAGON_SHOOT = (1017, Type.SOUND)
    """
    Sound of an enderdragon firing
    """
    WITHER_BREAK_BLOCK = (1022, Type.SOUND)
    """
    The sound played when a wither breaks a block
    """
    WITHER_SHOOT = (1024, Type.SOUND)
    """
    Sound of a wither shooting
    """
    ZOMBIE_INFECT = (1026, Type.SOUND)
    """
    The sound played when a zombie infects a target
    """
    ZOMBIE_CONVERTED_VILLAGER = (1027, Type.SOUND)
    """
    The sound played when a villager is converted by
    a zombie
    """
    BAT_TAKEOFF = (1025, Type.SOUND)
    """
    Sound played by a bat taking off
    """
    END_GATEWAY_SPAWN = (3000, Type.VISUAL)
    """
    The sound/particles caused by a end gateway spawning
    """
    ENDERDRAGON_GROWL = (3001, Type.SOUND)
    """
    The sound of an enderdragon growling
    """
    PHANTOM_BITE = (1039, Type.SOUND)
    """
    The sound played when phantom bites.
    """
    ZOMBIE_CONVERTED_TO_DROWNED = (1040, Type.SOUND)
    """
    The sound played when a zombie converts to a drowned.
    """
    HUSK_CONVERTED_TO_ZOMBIE = (1041, Type.SOUND)
    """
    The sound played when a husk converts to a zombie.
    """
    GRINDSTONE_USE = (1042, Type.SOUND)
    """
    The sound played when a grindstone is being used.
    """
    BOOK_PAGE_TURN = (1043, Type.SOUND)
    """
    The sound played when a book page is being turned.
    """
    SMITHING_TABLE_USE = (1044, Type.SOUND)
    """
    The sound played when a smithing table is being used.
    """
    POINTED_DRIPSTONE_LAND = (1045, Type.SOUND)
    """
    The sound played when a pointed dripstone hits the surface.
    """
    POINTED_DRIPSTONE_DRIP_LAVA_INTO_CAULDRON = (1046, Type.SOUND)
    """
    The sound played when a pointed dripstone drips lava into a cauldron.
    """
    POINTED_DRIPSTONE_DRIP_WATER_INTO_CAULDRON = (1047, Type.SOUND)
    """
    The sound played when a pointed dripstone drips water into a cauldron.
    """
    SKELETON_CONVERTED_TO_STRAY = (1048, Type.SOUND)
    """
    The sound played when a skeleton converts to a stray.
    """
    COMPOSTER_FILL_ATTEMPT = (1500, Type.VISUAL, Boolean)
    """
    The sound played / particles shown when a composter is being attempted to
    fill.
    
    True for a successful attempt False for an unsuccessful attempt.
    """
    LAVA_INTERACT = (1501, Type.VISUAL)
    """
    The sound played / particles shown when lava interacts with the world.
    
    For example by forming stone, obsidian, basalt or destroying blocks such
    as torches.
    """
    REDSTONE_TORCH_BURNOUT = (1502, Type.VISUAL)
    """
    The sound played / particles shown when a redstone torch burns out.
    """
    END_PORTAL_FRAME_FILL = (1503, Type.VISUAL)
    """
    The sound played / particles shown when an eye of ender is placed into an
    ender portal frame.
    """
    DRIPPING_DRIPSTONE = (1504, Type.VISUAL)
    """
    The particles shown when a dripstone drips lava or water.
    
    This effect requires a dripstone at the location as well as lava or water
    at the root of the dripstone.
    """
    BONE_MEAL_USE = (1505, Type.VISUAL, Integer)
    """
    The sound played / particles shown when bone meal is used to grow a
    plant.
    
    Data is the number of particles.
    """
    ENDER_DRAGON_DESTROY_BLOCK = (2008, Type.VISUAL)
    """
    The particles shown when an ender dragon destroys blocks.
    """
    SPONGE_DRY = (2009, Type.VISUAL)
    """
    The particles shown when a sponge dries in an ultra warm world (nether).
    """
    ELECTRIC_SPARK = (3002, Type.VISUAL, Axis)
    """
    The particles shown when a lightning hits a lightning rod or oxidized
    copper.
    
    Data is the axis at which the particle should be shown. If no data is
    provided it will show the particles at the block faces.
    """
    COPPER_WAX_ON = (3003, Type.VISUAL)
    """
    The sound played / particles shown when wax is applied to a copper block.
    """
    COPPER_WAX_OFF = (3004, Type.VISUAL)
    """
    The particles shown when wax is removed from a copper block.
    """
    OXIDISED_COPPER_SCRAPE = (3005, Type.VISUAL)
    """
    The particles shown when oxidation is scraped of an oxidized copper
    block.
    """


    def getId(self) -> int:
        """
        Gets the ID for this effect.

        Returns
        - ID of this effect

        Deprecated
        - Magic value
        """
        ...


    def getType(self) -> "Type":
        """
        Returns
        - The type of the effect.
        """
        ...


    def getData(self) -> type[Any]:
        """
        Returns
        - The class which represents data for this effect, or null if
            none
        """
        ...


    @staticmethod
    def getById(id: int) -> "Effect":
        """
        Gets the Effect associated with the given ID.

        Arguments
        - id: ID of the Effect to return

        Returns
        - Effect with the given ID

        Deprecated
        - Magic value
        """
        ...


    class Type(Enum):
        """
        Represents the type of an effect.
        """

        SOUND = 0
        VISUAL = 1
