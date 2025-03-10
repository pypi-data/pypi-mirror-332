"""
Python module generated from Java source file org.bukkit.Tag

Java source file obtained from artifact spigot-api version 1.16.5-R0.1-20210611.041013-99

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import *
from typing import Any, Callable, Iterable, Tuple


class Tag(Keyed):
    """
    Represents a tag that may be defined by the server or a resource pack to
    group like things together.
    
    Note that whilst all tags defined within this interface must be present in
    implementations, their existence is not guaranteed across future versions.
    
    Type `<T>`: the type of things grouped by this tag
    """

    REGISTRY_BLOCKS = "blocks"
    """
    Key for the built in block registry.
    """
    WOOL = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("wool"), Material.class)
    """
    Vanilla block tag representing all colors of wool.
    """
    PLANKS = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("planks"), Material.class)
    """
    Vanilla block tag representing all plank variants.
    """
    STONE_BRICKS = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("stone_bricks"), Material.class)
    """
    Vanilla block tag representing all regular/mossy/cracked/chiseled stone
    bricks.
    """
    WOODEN_BUTTONS = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("wooden_buttons"), Material.class)
    """
    Vanilla block tag representing all wooden buttons.
    """
    BUTTONS = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("buttons"), Material.class)
    """
    Vanilla block tag representing all buttons (inherits from
    .WOODEN_BUTTONS.
    """
    CARPETS = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("carpets"), Material.class)
    """
    Vanilla block tag representing all colors of carpet.
    """
    WOODEN_DOORS = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("wooden_doors"), Material.class)
    """
    Vanilla block tag representing all wooden doors.
    """
    WOODEN_STAIRS = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("wooden_stairs"), Material.class)
    """
    Vanilla block tag representing all wooden stairs.
    """
    WOODEN_SLABS = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("wooden_slabs"), Material.class)
    """
    Vanilla block tag representing all wooden slabs.
    """
    WOODEN_FENCES = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("wooden_fences"), Material.class)
    """
    Vanilla block tag representing all wooden fences.
    """
    PRESSURE_PLATES = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("pressure_plates"), Material.class)
    """
    Vanilla block tag representing all pressure plates.
    """
    WOODEN_PRESSURE_PLATES = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("wooden_pressure_plates"), Material.class)
    """
    Vanilla block tag representing all wooden pressure plates.
    """
    STONE_PRESSURE_PLATES = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("stone_pressure_plates"), Material.class)
    """
    Vanilla block tag representing all stone pressure plates.
    """
    WOODEN_TRAPDOORS = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("wooden_trapdoors"), Material.class)
    """
    Vanilla block tag representing all wooden trapdoors.
    """
    DOORS = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("doors"), Material.class)
    """
    Vanilla block tag representing all doors (inherits from
    .WOODEN_DOORS.
    """
    SAPLINGS = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("saplings"), Material.class)
    """
    Vanilla block tag representing all sapling variants.
    """
    LOGS_THAT_BURN = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("logs_that_burn"), Material.class)
    """
    Vanilla block tag representing all log and bark variants that burn.
    """
    LOGS = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("logs"), Material.class)
    """
    Vanilla block tag representing all log and bark variants.
    """
    DARK_OAK_LOGS = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("dark_oak_logs"), Material.class)
    """
    Vanilla block tag representing all dark oak log and bark variants.
    """
    OAK_LOGS = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("oak_logs"), Material.class)
    """
    Vanilla block tag representing all oak log and bark variants.
    """
    BIRCH_LOGS = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("birch_logs"), Material.class)
    """
    Vanilla block tag representing all birch log and bark variants.
    """
    ACACIA_LOGS = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("acacia_logs"), Material.class)
    """
    Vanilla block tag representing all acacia log and bark variants.
    """
    JUNGLE_LOGS = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("jungle_logs"), Material.class)
    """
    Vanilla block tag representing all jungle log and bark variants.
    """
    SPRUCE_LOGS = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("spruce_logs"), Material.class)
    """
    Vanilla block tag representing all spruce log and bark variants.
    """
    CRIMSON_STEMS = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("crimson_stems"), Material.class)
    """
    Vanilla block tag representing all crimson stems.
    """
    WARPED_STEMS = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("warped_stems"), Material.class)
    """
    Vanilla block tag representing all warped stems.
    """
    BANNERS = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("banners"), Material.class)
    """
    Vanilla block tag representing all banner blocks.
    """
    SAND = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("sand"), Material.class)
    """
    Vanilla block tag representing all sand blocks.
    """
    STAIRS = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("stairs"), Material.class)
    """
    Vanilla block tag representing all stairs.
    """
    SLABS = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("slabs"), Material.class)
    """
    Vanilla block tag representing all slabs.
    """
    WALLS = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("walls"), Material.class)
    """
    Vanilla block tag representing all walls.
    """
    ANVIL = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("anvil"), Material.class)
    """
    Vanilla block tag representing all damaged and undamaged anvils.
    """
    RAILS = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("rails"), Material.class)
    """
    Vanilla block tag representing all Minecart rails.
    """
    LEAVES = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("leaves"), Material.class)
    """
    Vanilla block tag representing all leaves fans.
    """
    TRAPDOORS = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("trapdoors"), Material.class)
    """
    Vanilla block tag representing all trapdoors (inherits from
    .WOODEN_TRAPDOORS.
    """
    FLOWER_POTS = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("flower_pots"), Material.class)
    """
    Vanilla block tag representing all empty and filled flower pots.
    """
    SMALL_FLOWERS = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("small_flowers"), Material.class)
    """
    Vanilla block tag representing all small flowers.
    """
    BEDS = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("beds"), Material.class)
    """
    Vanilla block tag representing all beds.
    """
    FENCES = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("fences"), Material.class)
    """
    Vanilla block tag representing all fences.
    """
    TALL_FLOWERS = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("tall_flowers"), Material.class)
    """
    Vanilla block tag representing all tall flowers.
    """
    FLOWERS = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("flowers"), Material.class)
    """
    Vanilla block tag representing all flowers.
    """
    PIGLIN_REPELLENTS = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("piglin_repellents"), Material.class)
    """
    Vanilla block tag representing all piglin repellents.
    """
    GOLD_ORES = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("gold_ores"), Material.class)
    """
    Vanilla block tag representing all gold ores.
    """
    NON_FLAMMABLE_WOOD = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("non_flammable_wood"), Material.class)
    """
    Vanilla block tag representing all non flammable wood.
    """
    ENDERMAN_HOLDABLE = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("enderman_holdable"), Material.class)
    """
    Vanilla block tag denoting blocks that enderman may pick up and hold.
    """
    ICE = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("ice"), Material.class)
    """
    Vanilla block tag denoting ice blocks.
    """
    VALID_SPAWN = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("valid_spawn"), Material.class)
    """
    Vanilla block tag denoting all valid mob spawn positions.
    """
    IMPERMEABLE = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("impermeable"), Material.class)
    """
    Vanilla block tag denoting impermeable blocks which do not drip fluids.
    """
    UNDERWATER_BONEMEALS = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("underwater_bonemeals"), Material.class)
    """
    Vanilla block tag denoting all underwater blocks which may be bonemealed.
    """
    CORAL_BLOCKS = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("coral_blocks"), Material.class)
    """
    Vanilla block tag representing all coral blocks.
    """
    WALL_CORALS = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("wall_corals"), Material.class)
    """
    Vanilla block tag representing all wall corals.
    """
    CORAL_PLANTS = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("coral_plants"), Material.class)
    """
    Vanilla block tag representing all coral plants.
    """
    CORALS = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("corals"), Material.class)
    """
    Vanilla block tag representing all coral.
    """
    BAMBOO_PLANTABLE_ON = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("bamboo_plantable_on"), Material.class)
    """
    Vanilla block tag denoting all blocks bamboo may be planted on.
    """
    STANDING_SIGNS = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("standing_signs"), Material.class)
    """
    Vanilla block tag representing all standing signs.
    """
    WALL_SIGNS = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("wall_signs"), Material.class)
    """
    Vanilla block tag representing all wall signs.
    """
    SIGNS = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("signs"), Material.class)
    """
    Vanilla block tag representing all signs.
    """
    DRAGON_IMMUNE = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("dragon_immune"), Material.class)
    """
    Vanilla block tag representing all blocks immune to dragons.
    """
    WITHER_IMMUNE = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("wither_immune"), Material.class)
    """
    Vanilla block tag representing all blocks immune to withers.
    """
    WITHER_SUMMON_BASE_BLOCKS = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("wither_summon_base_blocks"), Material.class)
    """
    Vanilla block tag representing all base blocks used for wither summoning.
    """
    BEEHIVES = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("beehives"), Material.class)
    """
    Vanilla block tag representing all beehives.
    """
    CROPS = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("crops"), Material.class)
    """
    Vanilla block tag representing all crops.
    """
    BEE_GROWABLES = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("bee_growables"), Material.class)
    """
    Vanilla block tag representing all bee growables.
    """
    PORTALS = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("portals"), Material.class)
    """
    Vanilla block tag representing all portals.
    """
    FIRE = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("fire"), Material.class)
    """
    Vanilla block tag representing all fire blocks.
    """
    NYLIUM = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("nylium"), Material.class)
    """
    Vanilla block tag representing all nylium blocks.
    """
    WART_BLOCKS = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("wart_blocks"), Material.class)
    """
    Vanilla block tag representing all wart blocks.
    """
    BEACON_BASE_BLOCKS = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("beacon_base_blocks"), Material.class)
    """
    Vanilla block tag representing all beacon base blocks.
    """
    SOUL_SPEED_BLOCKS = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("soul_speed_blocks"), Material.class)
    """
    Vanilla block tag representing all blocks affected by the soul speed enchantment.
    """
    WALL_POST_OVERRIDE = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("wall_post_override"), Material.class)
    """
    Vanilla block tag representing all wall post overrides.
    """
    CLIMBABLE = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("climbable"), Material.class)
    """
    Vanilla block tag representing all climbable blocks.
    """
    SHULKER_BOXES = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("shulker_boxes"), Material.class)
    """
    Vanilla block tag representing all shulker boxes.
    """
    HOGLIN_REPELLENTS = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("hoglin_repellents"), Material.class)
    """
    Vanilla block tag representing all hoglin repellents.
    """
    SOUL_FIRE_BASE_BLOCKS = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("soul_fire_base_blocks"), Material.class)
    """
    Vanilla block tag representing all soul fire base blocks.
    """
    STRIDER_WARM_BLOCKS = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("strider_warm_blocks"), Material.class)
    """
    Vanilla block tag representing all warm strider blocks.
    """
    CAMPFIRES = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("campfires"), Material.class)
    """
    Vanilla block tag representing all campfires.
    """
    GUARDED_BY_PIGLINS = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("guarded_by_piglins"), Material.class)
    """
    Vanilla block tag representing all blocks guarded by piglins.
    """
    PREVENT_MOB_SPAWNING_INSIDE = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("prevent_mob_spawning_inside"), Material.class)
    """
    Vanilla block tag representing all blocks that prevent inside mob
    spawning.
    """
    FENCE_GATES = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("fence_gates"), Material.class)
    """
    Vanilla block tag representing all fence gates.
    """
    UNSTABLE_BOTTOM_CENTER = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("unstable_bottom_center"), Material.class)
    """
    Vanilla block tag representing all unstable bottom center blocks.
    """
    INFINIBURN_OVERWORLD = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("infiniburn_overworld"), Material.class)
    """
    Vanilla block tag representing all blocks that burn forever in the
    overworld.
    """
    INFINIBURN_NETHER = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("infiniburn_nether"), Material.class)
    """
    Vanilla block tag representing all blocks that burn forever in the
    nether.
    """
    INFINIBURN_END = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("infiniburn_end"), Material.class)
    """
    Vanilla block tag representing all blocks that burn forever in the end.
    """
    REGISTRY_ITEMS = "items"
    """
    Key for the built in item registry.
    """
    ITEMS_PIGLIN_LOVED = Bukkit.getTag(REGISTRY_ITEMS, NamespacedKey.minecraft("piglin_loved"), Material.class)
    """
    Vanilla item tag representing all items loved by piglins.
    """
    ITEMS_BANNERS = Bukkit.getTag(REGISTRY_ITEMS, NamespacedKey.minecraft("banners"), Material.class)
    """
    Vanilla item tag representing all banner items.
    """
    ITEMS_BOATS = Bukkit.getTag(REGISTRY_ITEMS, NamespacedKey.minecraft("boats"), Material.class)
    """
    Vanilla item tag representing all boat items.
    """
    ITEMS_FISHES = Bukkit.getTag(REGISTRY_ITEMS, NamespacedKey.minecraft("fishes"), Material.class)
    """
    Vanilla item tag representing all fish items.
    """
    ITEMS_MUSIC_DISCS = Bukkit.getTag(REGISTRY_ITEMS, NamespacedKey.minecraft("music_discs"), Material.class)
    """
    Vanilla item tag representing all music disc items.
    """
    ITEMS_CREEPER_DROP_MUSIC_DISCS = Bukkit.getTag(REGISTRY_ITEMS, NamespacedKey.minecraft("creeper_drop_music_discs"), Material.class)
    """
    Vanilla item tag representing all music disc items dropped by creepers.
    """
    ITEMS_COALS = Bukkit.getTag(REGISTRY_ITEMS, NamespacedKey.minecraft("coals"), Material.class)
    """
    Vanilla item tag representing all coal items.
    """
    ITEMS_ARROWS = Bukkit.getTag(REGISTRY_ITEMS, NamespacedKey.minecraft("arrows"), Material.class)
    """
    Vanilla item tag representing all arrow items.
    """
    ITEMS_LECTERN_BOOKS = Bukkit.getTag(REGISTRY_ITEMS, NamespacedKey.minecraft("lectern_books"), Material.class)
    """
    Vanilla item tag representing all books that may be placed on lecterns.
    """
    ITEMS_BEACON_PAYMENT_ITEMS = Bukkit.getTag(REGISTRY_ITEMS, NamespacedKey.minecraft("beacon_payment_items"), Material.class)
    """
    Vanilla item tag representing all items that may be placed in beacons.
    """
    ITEMS_STONE_TOOL_MATERIALS = Bukkit.getTag(REGISTRY_ITEMS, NamespacedKey.minecraft("stone_tool_materials"), Material.class)
    """
    Vanilla item tag representing all stone tool materials.
    """
    ITEMS_FURNACE_MATERIALS = Bukkit.getTag(REGISTRY_ITEMS, NamespacedKey.minecraft("furnace_materials"), Material.class)
    """
    Vanilla item tag representing all furnace materials.
    """
    REGISTRY_FLUIDS = "fluids"
    """
    Key for the built in fluid registry.
    """
    FLUIDS_LAVA = Bukkit.getTag(REGISTRY_FLUIDS, NamespacedKey.minecraft("lava"), Fluid.class)
    """
    Vanilla fluid tag representing lava and flowing lava.
    """
    FLUIDS_WATER = Bukkit.getTag(REGISTRY_FLUIDS, NamespacedKey.minecraft("water"), Fluid.class)
    """
    Vanilla fluid tag representing water and flowing water.
    """


    def isTagged(self, item: "T") -> bool:
        """
        Returns whether or not this tag has an entry for the specified item.

        Arguments
        - item: to check

        Returns
        - if it is tagged
        """
        ...


    def getValues(self) -> set["T"]:
        """
        Gets an immutable set of all tagged items.

        Returns
        - set of tagged items
        """
        ...
