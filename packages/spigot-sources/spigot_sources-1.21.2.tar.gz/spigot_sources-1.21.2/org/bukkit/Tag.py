"""
Python module generated from Java source file org.bukkit.Tag

Java source file obtained from artifact spigot-api version 1.21.2-R0.1-20241023.084343-5

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import *
from org.bukkit.entity import EntityType
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
    STONE_BUTTONS = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("stone_buttons"), Material.class)
    """
    Vanilla block tag representing all stone buttons.
    """
    BUTTONS = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("buttons"), Material.class)
    """
    Vanilla block tag representing all buttons (inherits from
    .WOODEN_BUTTONS.
    """
    WOOL_CARPETS = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("wool_carpets"), Material.class)
    """
    Vanilla block tag representing all colors of carpet.
    """
    CARPETS = WOOL_CARPETS
    """
    Deprecated
    - .WOOL_CARPETS.
    """
    WOODEN_DOORS = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("wooden_doors"), Material.class)
    """
    Vanilla block tag representing all wooden doors.
    """
    MOB_INTERACTABLE_DOORS = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("mob_interactable_doors"), Material.class)
    """
    Vanilla block tag representing all doors which can be opened by mobs.
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
    PALE_OAK_LOGS = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("pale_oak_logs"), Material.class)
    """
    Vanilla block tag representing all pale oak log and bark variants.
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
    CHERRY_LOGS = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("cherry_logs"), Material.class)
    """
    Vanilla block tag representing all cherry log and bark variants.
    """
    JUNGLE_LOGS = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("jungle_logs"), Material.class)
    """
    Vanilla block tag representing all jungle log and bark variants.
    """
    SPRUCE_LOGS = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("spruce_logs"), Material.class)
    """
    Vanilla block tag representing all spruce log and bark variants.
    """
    MANGROVE_LOGS = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("mangrove_logs"), Material.class)
    """
    Vanilla block tag representing all mangrove log and bark variants.
    """
    CRIMSON_STEMS = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("crimson_stems"), Material.class)
    """
    Vanilla block tag representing all crimson stems.
    """
    WARPED_STEMS = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("warped_stems"), Material.class)
    """
    Vanilla block tag representing all warped stems.
    """
    BAMBOO_BLOCKS = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("bamboo_blocks"), Material.class)
    """
    Vanilla block tag representing all bamboo blocks.
    """
    BANNERS = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("banners"), Material.class)
    """
    Vanilla block tag representing all banner blocks.
    """
    SAND = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("sand"), Material.class)
    """
    Vanilla block tag representing all sand blocks.
    """
    SMELTS_TO_GLASS = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("smelts_to_glass"), Material.class)
    """
    Vanilla block tag representing all blocks which smelt to glass in a furnace.
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
    IRON_ORES = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("iron_ores"), Material.class)
    """
    Vanilla block tag representing all iron ores.
    """
    DIAMOND_ORES = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("diamond_ores"), Material.class)
    """
    Vanilla block tag representing all diamond ores.
    """
    REDSTONE_ORES = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("redstone_ores"), Material.class)
    """
    Vanilla block tag representing all redstone ores.
    """
    LAPIS_ORES = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("lapis_ores"), Material.class)
    """
    Vanilla block tag representing all lapis ores.
    """
    COAL_ORES = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("coal_ores"), Material.class)
    """
    Vanilla block tag representing all coal ores.
    """
    EMERALD_ORES = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("emerald_ores"), Material.class)
    """
    Vanilla block tag representing all emerald ores.
    """
    COPPER_ORES = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("copper_ores"), Material.class)
    """
    Vanilla block tag representing all copper ores.
    """
    CANDLES = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("candles"), Material.class)
    """
    Vanilla block tag representing all candles.
    """
    DIRT = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("dirt"), Material.class)
    """
    Vanilla block tag representing all dirt.
    """
    TERRACOTTA = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("terracotta"), Material.class)
    """
    Vanilla block tag representing all terracotta.
    """
    BADLANDS_TERRACOTTA = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("badlands_terracotta"), Material.class)
    """
    Vanilla block tag representing all badlands terracotta.
    """
    CONCRETE_POWDER = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("concrete_powder"), Material.class)
    """
    Vanilla block tag representing all concrete powder.
    """
    COMPLETES_FIND_TREE_TUTORIAL = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("completes_find_tree_tutorial"), Material.class)
    """
    Vanilla block tag representing all blocks which complete the find tree
    tutorial.
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
    Vanilla block tag representing all regular signs.
    """
    CEILING_HANGING_SIGNS = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("ceiling_hanging_signs"), Material.class)
    """
    Vanilla block tag representing all ceiling signs.
    """
    WALL_HANGING_SIGNS = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("wall_hanging_signs"), Material.class)
    """
    Vanilla block tag representing all wall hanging signs.
    """
    ALL_HANGING_SIGNS = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("all_hanging_signs"), Material.class)
    """
    Vanilla block tag representing all hanging signs.
    """
    ALL_SIGNS = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("all_signs"), Material.class)
    """
    Vanilla block tag representing all signs, regardless of type.
    """
    DRAGON_IMMUNE = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("dragon_immune"), Material.class)
    """
    Vanilla block tag representing all blocks immune to dragons.
    """
    DRAGON_TRANSPARENT = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("dragon_transparent"), Material.class)
    """
    Vanilla block tag representing all blocks transparent to the ender
    dragon.
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
    Vanilla block tag representing all blocks affected by the soul speed
    enchantment.
    """
    WALL_POST_OVERRIDE = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("wall_post_override"), Material.class)
    """
    Vanilla block tag representing all wall post overrides.
    """
    CLIMBABLE = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("climbable"), Material.class)
    """
    Vanilla block tag representing all climbable blocks.
    """
    FALL_DAMAGE_RESETTING = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("fall_damage_resetting"), Material.class)
    """
    Vanilla block tag representing all blocks which reset fall damage.
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
    MUSHROOM_GROW_BLOCK = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("mushroom_grow_block"), Material.class)
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
    BASE_STONE_OVERWORLD = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("base_stone_overworld"), Material.class)
    """
    Vanilla block tag representing the overworld base material.
    """
    STONE_ORE_REPLACEABLES = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("stone_ore_replaceables"), Material.class)
    """
    Vanilla block tag representing all blocks that may be replaced by ores.
    """
    DEEPSLATE_ORE_REPLACEABLES = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("deepslate_ore_replaceables"), Material.class)
    """
    Vanilla block tag representing all blocks that may be replaced by
    deepslate ores.
    """
    BASE_STONE_NETHER = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("base_stone_nether"), Material.class)
    """
    Vanilla block tag representing the nether base material.
    """
    OVERWORLD_CARVER_REPLACEABLES = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("overworld_carver_replaceables"), Material.class)
    """
    Vanilla block tag representing all blocks replaceable by the overworld
    carver.
    """
    NETHER_CARVER_REPLACEABLES = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("nether_carver_replaceables"), Material.class)
    """
    Vanilla block tag representing all blocks replaceable by the nether
    carver.
    """
    CANDLE_CAKES = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("candle_cakes"), Material.class)
    """
    Vanilla block tag representing all candle cakes.
    """
    CAULDRONS = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("cauldrons"), Material.class)
    """
    Vanilla block tag representing all cauldrons.
    """
    CRYSTAL_SOUND_BLOCKS = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("crystal_sound_blocks"), Material.class)
    """
    Vanilla block tag representing all blocks that make crystal sounds.
    """
    INSIDE_STEP_SOUND_BLOCKS = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("inside_step_sound_blocks"), Material.class)
    """
    Vanilla block tag representing all blocks that play muffled step sounds.
    """
    COMBINATION_STEP_SOUND_BLOCKS = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("combination_step_sound_blocks"), Material.class)
    """
    Vanilla block tag representing all blocks that play combination step sounds.
    """
    CAMEL_SAND_STEP_SOUND_BLOCKS = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("camel_sand_step_sound_blocks"), Material.class)
    """
    Vanilla block tag representing all blocks that play step sounds with camels on sand.
    """
    OCCLUDES_VIBRATION_SIGNALS = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("occludes_vibration_signals"), Material.class)
    """
    Vanilla block tag representing all blocks that block vibration signals.
    """
    DAMPENS_VIBRATIONS = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("dampens_vibrations"), Material.class)
    """
    Vanilla block tag representing all blocks that dampen the propagation of
    vibration signals.
    """
    DRIPSTONE_REPLACEABLE = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("dripstone_replaceable_blocks"), Material.class)
    """
    Vanilla block tag representing all blocks that are replaceable by
    dripstone.
    """
    CAVE_VINES = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("cave_vines"), Material.class)
    """
    Vanilla block tag representing all cave vines.
    """
    MOSS_REPLACEABLE = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("moss_replaceable"), Material.class)
    """
    Vanilla block tag representing all blocks replaceable by moss.
    """
    LUSH_GROUND_REPLACEABLE = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("lush_ground_replaceable"), Material.class)
    """
    Vanilla block tag representing all blocks replaceable by lush ground.
    """
    AZALEA_ROOT_REPLACEABLE = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("azalea_root_replaceable"), Material.class)
    """
    Vanilla block tag representing all blocks replaceable by azalea root.
    """
    SMALL_DRIPLEAF_PLACEABLE = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("small_dripleaf_placeable"), Material.class)
    """
    Vanilla block tag representing all blocks which small dripleaf can be
    placed on.
    """
    BIG_DRIPLEAF_PLACEABLE = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("big_dripleaf_placeable"), Material.class)
    """
    Vanilla block tag representing all blocks which big dripleaf can be
    placed on.
    """
    SNOW = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("snow"), Material.class)
    """
    Vanilla block tag representing all snow blocks.
    """
    MINEABLE_AXE = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("mineable/axe"), Material.class)
    """
    Vanilla block tag representing all blocks mineable with an axe.
    """
    MINEABLE_HOE = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("mineable/hoe"), Material.class)
    """
    Vanilla block tag representing all blocks mineable with a hoe.
    """
    MINEABLE_PICKAXE = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("mineable/pickaxe"), Material.class)
    """
    Vanilla block tag representing all blocks mineable with a pickaxe.
    """
    MINEABLE_SHOVEL = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("mineable/shovel"), Material.class)
    """
    Vanilla block tag representing all blocks mineable with a shovel.
    """
    SWORD_EFFICIENT = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("sword_efficient"), Material.class)
    """
    Vanilla block tag representing all blocks that can be efficiently mined with a sword.
    """
    NEEDS_DIAMOND_TOOL = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("needs_diamond_tool"), Material.class)
    """
    Vanilla block tag representing all blocks which require a diamond tool.
    """
    NEEDS_IRON_TOOL = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("needs_iron_tool"), Material.class)
    """
    Vanilla block tag representing all blocks which require an iron tool.
    """
    NEEDS_STONE_TOOL = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("needs_stone_tool"), Material.class)
    """
    Vanilla block tag representing all blocks which require a stone tool.
    """
    INCORRECT_FOR_NETHERITE_TOOL = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("incorrect_for_netherite_tool"), Material.class)
    """
    Vanilla block tag representing all blocks which will not drop items with a netherite tool.
    """
    INCORRECT_FOR_DIAMOND_TOOL = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("incorrect_for_diamond_tool"), Material.class)
    """
    Vanilla block tag representing all blocks which will not drop items with a diamond tool.
    """
    INCORRECT_FOR_IRON_TOOL = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("incorrect_for_iron_tool"), Material.class)
    """
    Vanilla block tag representing all blocks which will not drop items with a iron tool.
    """
    INCORRECT_FOR_STONE_TOOL = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("incorrect_for_stone_tool"), Material.class)
    """
    Vanilla block tag representing all blocks which will not drop items with a stone tool.
    """
    INCORRECT_FOR_GOLD_TOOL = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("incorrect_for_gold_tool"), Material.class)
    """
    Vanilla block tag representing all blocks which will not drop items with a gold tool.
    """
    INCORRECT_FOR_WOODEN_TOOL = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("incorrect_for_wooden_tool"), Material.class)
    """
    Vanilla block tag representing all blocks which will not drop items with a wooden tool.
    """
    FEATURES_CANNOT_REPLACE = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("features_cannot_replace"), Material.class)
    """
    Vanilla block tag representing all blocks which will not be replaced by
    world generation features.
    """
    LAVA_POOL_STONE_CANNOT_REPLACE = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("lava_pool_stone_cannot_replace"), Material.class)
    """
    Vanilla block tag representing all blocks which lava pools will not
    replace.
    """
    GEODE_INVALID_BLOCKS = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("geode_invalid_blocks"), Material.class)
    """
    Vanilla block tag representing all blocks which geodes will not spawn in.
    """
    FROG_PREFER_JUMP_TO = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("frog_prefer_jump_to"), Material.class)
    """
    Vanilla block tag representing all blocks which frogs prefer to jump to.
    """
    SCULK_REPLACEABLE = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("sculk_replaceable"), Material.class)
    """
    Vanilla block tag representing all blocks which can be replaced by skulk.
    """
    SCULK_REPLACEABLE_WORLD_GEN = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("sculk_replaceable_world_gen"), Material.class)
    """
    Vanilla block tag representing all blocks which can be replaced by skulk
    during world generation.
    """
    ANCIENT_CITY_REPLACEABLE = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("ancient_city_replaceable"), Material.class)
    """
    Vanilla block tag representing all blocks which can be replaced by
    ancient cities.
    """
    VIBRATION_RESONATORS = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("vibration_resonators"), Material.class)
    """
    Vanilla block tag representing all blocks which resonate vibrations.
    """
    ANIMALS_SPAWNABLE_ON = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("animals_spawnable_on"), Material.class)
    """
    Vanilla block tag representing all blocks which animals will spawn on.
    """
    ARMADILLO_SPAWNABLE_ON = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("armadillo_spawnable_on"), Material.class)
    """
    Vanilla block tag representing all blocks which armadillos will spawn on.
    """
    AXOLOTLS_SPAWNABLE_ON = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("axolotls_spawnable_on"), Material.class)
    """
    Vanilla block tag representing all blocks which axolotls will spawn on.
    """
    GOATS_SPAWNABLE_ON = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("goats_spawnable_on"), Material.class)
    """
    Vanilla block tag representing all blocks which goats will spawn on.
    """
    MOOSHROOMS_SPAWNABLE_ON = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("mooshrooms_spawnable_on"), Material.class)
    """
    Vanilla block tag representing all blocks which mooshrooms will spawn on.
    """
    PARROTS_SPAWNABLE_ON = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("parrots_spawnable_on"), Material.class)
    """
    Vanilla block tag representing all blocks which parrots will spawn on.
    """
    POLAR_BEARS_SPAWNABLE_ON_ALTERNATE = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("polar_bears_spawnable_on_alternate"), Material.class)
    """
    Vanilla block tag representing all blocks which polar bears will spawn
    on.
    """
    RABBITS_SPAWNABLE_ON = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("rabbits_spawnable_on"), Material.class)
    """
    Vanilla block tag representing all blocks which rabbits will spawn on.
    """
    FOXES_SPAWNABLE_ON = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("foxes_spawnable_on"), Material.class)
    """
    Vanilla block tag representing all blocks which foxes will spawn on.
    """
    WOLVES_SPAWNABLE_ON = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("wolves_spawnable_on"), Material.class)
    """
    Vanilla block tag representing all blocks which wolves will spawn on.
    """
    FROGS_SPAWNABLE_ON = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("frogs_spawnable_on"), Material.class)
    """
    Vanilla block tag representing all blocks which frogs will spawn on.
    """
    BATS_SPAWNABLE_ON = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("bats_spawnable_on"), Material.class)
    """
    Vanilla block tag representing all blocks which bats will spawn on.
    """
    AZALEA_GROWS_ON = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("azalea_grows_on"), Material.class)
    """
    Vanilla block tag representing all blocks which azaleas will grow on.
    """
    CONVERTABLE_TO_MUD = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("convertable_to_mud"), Material.class)
    """
    Vanilla block tag representing all blocks which may be converted to mud.
    """
    MANGROVE_LOGS_CAN_GROW_THROUGH = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("mangrove_logs_can_grow_through"), Material.class)
    """
    Vanilla block tag representing all blocks which mangrove logs can grow
    through.
    """
    MANGROVE_ROOTS_CAN_GROW_THROUGH = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("mangrove_roots_can_grow_through"), Material.class)
    """
    Vanilla block tag representing all blocks which mangrove roots can grow
    through.
    """
    DEAD_BUSH_MAY_PLACE_ON = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("dead_bush_may_place_on"), Material.class)
    """
    Vanilla block tag representing all blocks which dead bushes may be placed
    on.
    """
    SNAPS_GOAT_HORN = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("snaps_goat_horn"), Material.class)
    """
    Vanilla block tag representing all blocks which snap dropped goat horns.
    """
    REPLACEABLE_BY_TREES = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("replaceable_by_trees"), Material.class)
    """
    Vanilla block tag representing all blocks replaceable by growing trees.
    """
    SNOW_LAYER_CANNOT_SURVIVE_ON = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("snow_layer_cannot_survive_on"), Material.class)
    """
    Vanilla block tag representing blocks which snow cannot survive on.
    """
    SNOW_LAYER_CAN_SURVIVE_ON = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("snow_layer_can_survive_on"), Material.class)
    """
    Vanilla block tag representing blocks which snow can survive on.
    """
    INVALID_SPAWN_INSIDE = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("invalid_spawn_inside"), Material.class)
    """
    Vanilla block tag representing blocks which cannot be dismounted into.
    """
    SNIFFER_DIGGABLE_BLOCK = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("sniffer_diggable_block"), Material.class)
    """
    Vanilla block tag representing blocks which can be dug by sniffers.
    """
    SNIFFER_EGG_HATCH_BOOST = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("sniffer_egg_hatch_boost"), Material.class)
    """
    Vanilla block tag representing all blocks which booster sniffer egg hatching.
    """
    TRAIL_RUINS_REPLACEABLE = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("trail_ruins_replaceable"), Material.class)
    """
    Vanilla block tag representing all blocks which can be replaced by trail ruins.
    """
    REPLACEABLE = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("replaceable"), Material.class)
    """
    Vanilla block tag representing all blocks which are replaceable.
    """
    ENCHANTMENT_POWER_PROVIDER = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("enchantment_power_provider"), Material.class)
    """
    Vanilla block tag representing all blocks which provide enchantment power.
    """
    ENCHANTMENT_POWER_TRANSMITTER = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("enchantment_power_transmitter"), Material.class)
    """
    Vanilla block tag representing all blocks which transmit enchantment power.
    """
    MAINTAINS_FARMLAND = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("maintains_farmland"), Material.class)
    """
    Vanilla block tag representing all blocks which do not destroy farmland when placed.
    """
    BLOCKS_WIND_CHARGE_EXPLOSIONS = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("blocks_wind_charge_explosions"), Material.class)
    """
    Vanilla block tag representing all blocks which block wind charge explosions.
    """
    DOES_NOT_BLOCK_HOPPERS = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("does_not_block_hoppers"), Material.class)
    """
    Vanilla block tag representing solid blocks which do not block hopper operation.
    """
    AIR = Bukkit.getTag(REGISTRY_BLOCKS, NamespacedKey.minecraft("air"), Material.class)
    """
    Vanilla block tag representing all blocks that resemble air.
    """
    REGISTRY_ITEMS = "items"
    """
    Key for the built in item registry.
    """
    ITEMS_PIGLIN_LOVED = Bukkit.getTag(REGISTRY_ITEMS, NamespacedKey.minecraft("piglin_loved"), Material.class)
    """
    Vanilla item tag representing all items loved by piglins.
    """
    IGNORED_BY_PIGLIN_BABIES = Bukkit.getTag(REGISTRY_ITEMS, NamespacedKey.minecraft("ignored_by_piglin_babies"), Material.class)
    """
    Vanilla item tag representing all items ignored by piglin babies.
    """
    ITEMS_PIGLIN_SAFE_ARMOR = Bukkit.getTag(REGISTRY_ITEMS, NamespacedKey.minecraft("piglin_safe_armor"), Material.class)
    """
    Vanilla item tag representing all items which will prevent piglins from being angered.
    """
    ITEMS_DUPLICATES_ALLAYS = Bukkit.getTag(REGISTRY_ITEMS, NamespacedKey.minecraft("duplicates_allays"), Material.class)
    """
    Vanilla item tag representing all items which can be used to duplicate Allays when they are dancing.
    """
    ITEMS_BREWING_FUEL = Bukkit.getTag(REGISTRY_ITEMS, NamespacedKey.minecraft("brewing_fuel"), Material.class)
    """
    Vanilla item tag representing all brewing stand fuel items.
    """
    ITEMS_MEAT = Bukkit.getTag(REGISTRY_ITEMS, NamespacedKey.minecraft("meat"), Material.class)
    """
    Vanilla item tag representing all meat.
    """
    ITEMS_SNIFFER_FOOD = Bukkit.getTag(REGISTRY_ITEMS, NamespacedKey.minecraft("sniffer_food"), Material.class)
    """
    Vanilla item tag representing all sniffer food.
    """
    ITEMS_PIGLIN_FOOD = Bukkit.getTag(REGISTRY_ITEMS, NamespacedKey.minecraft("piglin_food"), Material.class)
    """
    Vanilla item tag representing all piglin food.
    """
    PIGLIN_FOOD = ITEMS_PIGLIN_FOOD
    """
    Vanilla item tag representing all piglin food.

    Deprecated
    - use .ITEMS_PIGLIN_FOOD
    """
    ITEMS_FOX_FOOD = Bukkit.getTag(REGISTRY_ITEMS, NamespacedKey.minecraft("fox_food"), Material.class)
    """
    Vanilla item tag representing all fox food.
    """
    FOX_FOOD = ITEMS_FOX_FOOD
    """
    Vanilla item tag representing all fox food.

    Deprecated
    - use .ITEMS_FOX_FOOD
    """
    ITEMS_COW_FOOD = Bukkit.getTag(REGISTRY_ITEMS, NamespacedKey.minecraft("cow_food"), Material.class)
    """
    Vanilla item tag representing all cow food.
    """
    ITEMS_GOAT_FOOD = Bukkit.getTag(REGISTRY_ITEMS, NamespacedKey.minecraft("goat_food"), Material.class)
    """
    Vanilla item tag representing all goat food.
    """
    ITEMS_SHEEP_FOOD = Bukkit.getTag(REGISTRY_ITEMS, NamespacedKey.minecraft("sheep_food"), Material.class)
    """
    Vanilla item tag representing all sheep food.
    """
    ITEMS_WOLF_FOOD = Bukkit.getTag(REGISTRY_ITEMS, NamespacedKey.minecraft("wolf_food"), Material.class)
    """
    Vanilla item tag representing all wolf food.
    """
    ITEMS_CAT_FOOD = Bukkit.getTag(REGISTRY_ITEMS, NamespacedKey.minecraft("cat_food"), Material.class)
    """
    Vanilla item tag representing all cat food.
    """
    ITEMS_HORSE_FOOD = Bukkit.getTag(REGISTRY_ITEMS, NamespacedKey.minecraft("horse_food"), Material.class)
    """
    Vanilla item tag representing all horse food.
    """
    ITEMS_HORSE_TEMPT_ITEMS = Bukkit.getTag(REGISTRY_ITEMS, NamespacedKey.minecraft("horse_tempt_items"), Material.class)
    """
    Vanilla item tag representing all horse tempt items.
    """
    ITEMS_CAMEL_FOOD = Bukkit.getTag(REGISTRY_ITEMS, NamespacedKey.minecraft("camel_food"), Material.class)
    """
    Vanilla item tag representing all camel food.
    """
    ITEMS_ARMADILLO_FOOD = Bukkit.getTag(REGISTRY_ITEMS, NamespacedKey.minecraft("armadillo_food"), Material.class)
    """
    Vanilla item tag representing all armadillo food.
    """
    ITEMS_BEE_FOOD = Bukkit.getTag(REGISTRY_ITEMS, NamespacedKey.minecraft("bee_food"), Material.class)
    """
    Vanilla item tag representing all bee food.
    """
    ITEMS_CHICKEN_FOOD = Bukkit.getTag(REGISTRY_ITEMS, NamespacedKey.minecraft("chicken_food"), Material.class)
    """
    Vanilla item tag representing all chicken food.
    """
    ITEMS_FROG_FOOD = Bukkit.getTag(REGISTRY_ITEMS, NamespacedKey.minecraft("frog_food"), Material.class)
    """
    Vanilla item tag representing all frog food.
    """
    ITEMS_HOGLIN_FOOD = Bukkit.getTag(REGISTRY_ITEMS, NamespacedKey.minecraft("hoglin_food"), Material.class)
    """
    Vanilla item tag representing all hoglin food.
    """
    ITEMS_LLAMA_FOOD = Bukkit.getTag(REGISTRY_ITEMS, NamespacedKey.minecraft("llama_food"), Material.class)
    """
    Vanilla item tag representing all llama food.
    """
    ITEMS_LLAMA_TEMPT_ITEMS = Bukkit.getTag(REGISTRY_ITEMS, NamespacedKey.minecraft("llama_tempt_items"), Material.class)
    """
    Vanilla item tag representing all llama tempt items.
    """
    ITEMS_OCELOT_FOOD = Bukkit.getTag(REGISTRY_ITEMS, NamespacedKey.minecraft("ocelot_food"), Material.class)
    """
    Vanilla item tag representing all ocelot food.
    """
    ITEMS_PANDA_FOOD = Bukkit.getTag(REGISTRY_ITEMS, NamespacedKey.minecraft("panda_food"), Material.class)
    """
    Vanilla item tag representing all panda food.
    """
    ITEMS_PANDA_EATS_FROM_GROUND = Bukkit.getTag(REGISTRY_ITEMS, NamespacedKey.minecraft("panda_eats_from_ground"), Material.class)
    """
    Vanilla item tag representing all items that a panda will pick up and eat from the ground.
    """
    ITEMS_PIG_FOOD = Bukkit.getTag(REGISTRY_ITEMS, NamespacedKey.minecraft("pig_food"), Material.class)
    """
    Vanilla item tag representing all pig food.
    """
    ITEMS_RABBIT_FOOD = Bukkit.getTag(REGISTRY_ITEMS, NamespacedKey.minecraft("rabbit_food"), Material.class)
    """
    Vanilla item tag representing all rabbit food.
    """
    ITEMS_STRIDER_FOOD = Bukkit.getTag(REGISTRY_ITEMS, NamespacedKey.minecraft("strider_food"), Material.class)
    """
    Vanilla item tag representing all strider food.
    """
    ITEMS_STRIDER_TEMPT_ITEMS = Bukkit.getTag(REGISTRY_ITEMS, NamespacedKey.minecraft("strider_tempt_items"), Material.class)
    """
    Vanilla item tag representing all strider tempt items.
    """
    ITEMS_TURTLE_FOOD = Bukkit.getTag(REGISTRY_ITEMS, NamespacedKey.minecraft("turtle_food"), Material.class)
    """
    Vanilla item tag representing all turtle food.
    """
    ITEMS_PARROT_FOOD = Bukkit.getTag(REGISTRY_ITEMS, NamespacedKey.minecraft("parrot_food"), Material.class)
    """
    Vanilla item tag representing all parrot food.
    """
    ITEMS_PARROT_POISONOUS_FOOD = Bukkit.getTag(REGISTRY_ITEMS, NamespacedKey.minecraft("parrot_poisonous_food"), Material.class)
    """
    Vanilla item tag representing all parrot poisonous food.
    """
    ITEMS_AXOLOTL_FOOD = Bukkit.getTag(REGISTRY_ITEMS, NamespacedKey.minecraft("axolotl_food"), Material.class)
    """
    Vanilla item tag representing all axolotl food.
    """
    ITEMS_BANNERS = Bukkit.getTag(REGISTRY_ITEMS, NamespacedKey.minecraft("banners"), Material.class)
    """
    Vanilla item tag representing all banner items.
    """
    ITEMS_NON_FLAMMABLE_WOOD = Bukkit.getTag(REGISTRY_ITEMS, NamespacedKey.minecraft("non_flammable_wood"), Material.class)
    """
    Vanilla item tag representing all non flammable wood items.
    """
    ITEMS_BOATS = Bukkit.getTag(REGISTRY_ITEMS, NamespacedKey.minecraft("boats"), Material.class)
    """
    Vanilla item tag representing all boat items.
    """
    ITEMS_CHEST_BOATS = Bukkit.getTag(REGISTRY_ITEMS, NamespacedKey.minecraft("chest_boats"), Material.class)
    """
    Vanilla item tag representing all chest boat items.
    """
    ITEMS_FISHES = Bukkit.getTag(REGISTRY_ITEMS, NamespacedKey.minecraft("fishes"), Material.class)
    """
    Vanilla item tag representing all fish items.
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
    ITEMS_BOOKSHELF_BOOKS = Bukkit.getTag(REGISTRY_ITEMS, NamespacedKey.minecraft("bookshelf_books"), Material.class)
    """
    Vanilla item tag representing all books that may be placed on bookshelves.
    """
    ITEMS_BEACON_PAYMENT_ITEMS = Bukkit.getTag(REGISTRY_ITEMS, NamespacedKey.minecraft("beacon_payment_items"), Material.class)
    """
    Vanilla item tag representing all items that may be placed in beacons.
    """
    ITEMS_WOODEN_TOOL_MATERIALS = Bukkit.getTag(REGISTRY_ITEMS, NamespacedKey.minecraft("wooden_tool_materials"), Material.class)
    """
    Vanilla item tag representing all wooden tool materials.
    """
    ITEMS_STONE_TOOL_MATERIALS = Bukkit.getTag(REGISTRY_ITEMS, NamespacedKey.minecraft("stone_tool_materials"), Material.class)
    """
    Vanilla item tag representing all stone tool materials.
    """
    ITEMS_IRON_TOOL_MATERIALS = Bukkit.getTag(REGISTRY_ITEMS, NamespacedKey.minecraft("iron_tool_materials"), Material.class)
    """
    Vanilla item tag representing all iron tool materials.
    """
    ITEMS_GOLD_TOOL_MATERIALS = Bukkit.getTag(REGISTRY_ITEMS, NamespacedKey.minecraft("gold_tool_materials"), Material.class)
    """
    Vanilla item tag representing all gold tool materials.
    """
    ITEMS_DIAMOND_TOOL_MATERIALS = Bukkit.getTag(REGISTRY_ITEMS, NamespacedKey.minecraft("diamond_tool_materials"), Material.class)
    """
    Vanilla item tag representing all diamond tool materials.
    """
    ITEMS_NETHERITE_TOOL_MATERIALS = Bukkit.getTag(REGISTRY_ITEMS, NamespacedKey.minecraft("netherite_tool_materials"), Material.class)
    """
    Vanilla item tag representing all netherite tool materials.
    """
    ITEMS_REPAIRS_LEATHER_ARMOR = Bukkit.getTag(REGISTRY_ITEMS, NamespacedKey.minecraft("repairs_leather_armor"), Material.class)
    """
    Vanilla item tag representing all items which repair leather armor.
    """
    ITEMS_REPAIRS_CHAIN_ARMOR = Bukkit.getTag(REGISTRY_ITEMS, NamespacedKey.minecraft("repairs_chain_armor"), Material.class)
    """
    Vanilla item tag representing all items which repair chain armor.
    """
    ITEMS_REPAIRS_IRON_ARMOR = Bukkit.getTag(REGISTRY_ITEMS, NamespacedKey.minecraft("repairs_iron_armor"), Material.class)
    """
    Vanilla item tag representing all items which repair iron armor.
    """
    ITEMS_REPAIRS_GOLD_ARMOR = Bukkit.getTag(REGISTRY_ITEMS, NamespacedKey.minecraft("repairs_gold_armor"), Material.class)
    """
    Vanilla item tag representing all items which repair gold armor.
    """
    ITEMS_REPAIRS_DIAMOND_ARMOR = Bukkit.getTag(REGISTRY_ITEMS, NamespacedKey.minecraft("repairs_diamond_armor"), Material.class)
    """
    Vanilla item tag representing all items which repair diamond armor.
    """
    ITEMS_REPAIRS_NETHERITE_ARMOR = Bukkit.getTag(REGISTRY_ITEMS, NamespacedKey.minecraft("repairs_netherite_armor"), Material.class)
    """
    Vanilla item tag representing all items which repair netherite armor.
    """
    ITEMS_REPAIRS_TURTLE_HELMET = Bukkit.getTag(REGISTRY_ITEMS, NamespacedKey.minecraft("repairs_turtle_helmet"), Material.class)
    """
    Vanilla item tag representing all items which repair turtle helmets.
    """
    ITEMS_REPAIRS_WOLF_ARMOR = Bukkit.getTag(REGISTRY_ITEMS, NamespacedKey.minecraft("repairs_wolf_armor"), Material.class)
    """
    Vanilla item tag representing all items which repair wolf armor.
    """
    ITEMS_FURNACE_MATERIALS = Bukkit.getTag(REGISTRY_ITEMS, NamespacedKey.minecraft("furnace_materials"), Material.class)
    """
    Vanilla item tag representing all furnace materials.
    """
    ITEMS_COMPASSES = Bukkit.getTag(REGISTRY_ITEMS, NamespacedKey.minecraft("compasses"), Material.class)
    """
    Vanilla item tag representing all compasses.
    """
    ITEMS_HANGING_SIGNS = Bukkit.getTag(REGISTRY_ITEMS, NamespacedKey.minecraft("hanging_signs"), Material.class)
    """
    Vanilla item tag representing all hanging signs.
    """
    ITEMS_CREEPER_IGNITERS = Bukkit.getTag(REGISTRY_ITEMS, NamespacedKey.minecraft("creeper_igniters"), Material.class)
    """
    Vanilla item tag representing all items which will ignite creepers when
    interacted with.
    """
    ITEMS_NOTE_BLOCK_TOP_INSTRUMENTS = Bukkit.getTag(REGISTRY_ITEMS, NamespacedKey.minecraft("noteblock_top_instruments"), Material.class)
    """
    Vanilla item tag representing all items which modify note block sounds when placed on top.
    """
    ITEMS_FOOT_ARMOR = Bukkit.getTag(REGISTRY_ITEMS, NamespacedKey.minecraft("foot_armor"), Material.class)
    """
    Vanilla item tag representing all foot armor.
    """
    ITEMS_LEG_ARMOR = Bukkit.getTag(REGISTRY_ITEMS, NamespacedKey.minecraft("leg_armor"), Material.class)
    """
    Vanilla item tag representing all leg armor.
    """
    ITEMS_CHEST_ARMOR = Bukkit.getTag(REGISTRY_ITEMS, NamespacedKey.minecraft("chest_armor"), Material.class)
    """
    Vanilla item tag representing all chest armor.
    """
    ITEMS_HEAD_ARMOR = Bukkit.getTag(REGISTRY_ITEMS, NamespacedKey.minecraft("head_armor"), Material.class)
    """
    Vanilla item tag representing all head armor.
    """
    ITEMS_SKULLS = Bukkit.getTag(REGISTRY_ITEMS, NamespacedKey.minecraft("skulls"), Material.class)
    """
    Vanilla item tag representing all skulls.
    """
    ITEMS_TRIMMABLE_ARMOR = Bukkit.getTag(REGISTRY_ITEMS, NamespacedKey.minecraft("trimmable_armor"), Material.class)
    """
    Vanilla item tag representing all trimmable armor items.
    """
    ITEMS_TRIM_MATERIALS = Bukkit.getTag(REGISTRY_ITEMS, NamespacedKey.minecraft("trim_materials"), Material.class)
    """
    Vanilla item tag representing all materials which can be used for trimming armor.
    """
    ITEMS_TRIM_TEMPLATES = Bukkit.getTag(REGISTRY_ITEMS, NamespacedKey.minecraft("trim_templates"), Material.class)
    """
    Vanilla item tag representing all trimming templates.
    """
    ITEMS_DECORATED_POT_SHERDS = Bukkit.getTag(REGISTRY_ITEMS, NamespacedKey.minecraft("decorated_pot_sherds"), Material.class)
    """
    Vanilla item tag representing all decorated pot sherds.
    """
    ITEMS_DECORATED_POT_INGREDIENTS = Bukkit.getTag(REGISTRY_ITEMS, NamespacedKey.minecraft("decorated_pot_ingredients"), Material.class)
    """
    Vanilla item tag representing all decorated pot ingredients.
    """
    ITEMS_SWORDS = Bukkit.getTag(REGISTRY_ITEMS, NamespacedKey.minecraft("swords"), Material.class)
    """
    Vanilla item tag representing all swords.
    """
    ITEMS_AXES = Bukkit.getTag(REGISTRY_ITEMS, NamespacedKey.minecraft("axes"), Material.class)
    """
    Vanilla item tag representing all axes.
    """
    ITEMS_HOES = Bukkit.getTag(REGISTRY_ITEMS, NamespacedKey.minecraft("hoes"), Material.class)
    """
    Vanilla item tag representing all hoes.
    """
    ITEMS_PICKAXES = Bukkit.getTag(REGISTRY_ITEMS, NamespacedKey.minecraft("pickaxes"), Material.class)
    """
    Vanilla item tag representing all pickaxes.
    """
    ITEMS_SHOVELS = Bukkit.getTag(REGISTRY_ITEMS, NamespacedKey.minecraft("shovels"), Material.class)
    """
    Vanilla item tag representing all shovels.
    """
    ITEMS_BREAKS_DECORATED_POTS = Bukkit.getTag(REGISTRY_ITEMS, NamespacedKey.minecraft("breaks_decorated_pots"), Material.class)
    """
    Vanilla item tag representing all items which break decorated pots.
    """
    ITEMS_TOOLS = ITEMS_BREAKS_DECORATED_POTS
    """
    Vanilla item tag representing all tools.

    Deprecated
    - removed in Minecraft 1.20.5. Do not use. Will be removed at a later date. Until then,
    this constant now acts as a reference to .ITEMS_BREAKS_DECORATED_POTS which largely shares
    the same contents of the old "minecraft:tools" tag.
    """
    ITEMS_VILLAGER_PLANTABLE_SEEDS = Bukkit.getTag(REGISTRY_ITEMS, NamespacedKey.minecraft("villager_plantable_seeds"), Material.class)
    """
    Vanilla item tag representing all seeds plantable by villagers.
    """
    ITEMS_VILLAGER_PICKS_UP = Bukkit.getTag(REGISTRY_ITEMS, NamespacedKey.minecraft("villager_picks_up"), Material.class)
    """
    Vanilla item tag representing all items which villagers pick up.
    """
    ITEMS_DYEABLE = Bukkit.getTag(REGISTRY_ITEMS, NamespacedKey.minecraft("dyeable"), Material.class)
    """
    Vanilla item tag representing all dyeable items.
    """
    ITEMS_FURNACE_MINECART_FUEL = Bukkit.getTag(REGISTRY_ITEMS, NamespacedKey.minecraft("furnace_minecart_fuel"), Material.class)
    """
    Vanilla item tag representing all furnace minecart fuel.
    """
    ITEMS_BUNDLES = Bukkit.getTag(REGISTRY_ITEMS, NamespacedKey.minecraft("bundles"), Material.class)
    """
    Vanilla item tag representing all bundle items.
    """
    ITEMS_ENCHANTABLE_FOOT_ARMOR = Bukkit.getTag(REGISTRY_ITEMS, NamespacedKey.minecraft("enchantable/foot_armor"), Material.class)
    """
    Vanilla item tag representing all enchantable foot armor.
    """
    ITEMS_ENCHANTABLE_LEG_ARMOR = Bukkit.getTag(REGISTRY_ITEMS, NamespacedKey.minecraft("enchantable/leg_armor"), Material.class)
    """
    Vanilla item tag representing all enchantable leg armor.
    """
    ITEMS_ENCHANTABLE_CHEST_ARMOR = Bukkit.getTag(REGISTRY_ITEMS, NamespacedKey.minecraft("enchantable/chest_armor"), Material.class)
    """
    Vanilla item tag representing all enchantable chest armor.
    """
    ITEMS_ENCHANTABLE_HEAD_ARMOR = Bukkit.getTag(REGISTRY_ITEMS, NamespacedKey.minecraft("enchantable/head_armor"), Material.class)
    """
    Vanilla item tag representing all enchantable head armor.
    """
    ITEMS_ENCHANTABLE_ARMOR = Bukkit.getTag(REGISTRY_ITEMS, NamespacedKey.minecraft("enchantable/armor"), Material.class)
    """
    Vanilla item tag representing all enchantable armor.
    """
    ITEMS_ENCHANTABLE_SWORD = Bukkit.getTag(REGISTRY_ITEMS, NamespacedKey.minecraft("enchantable/sword"), Material.class)
    """
    Vanilla item tag representing all enchantable swords.
    """
    ITEMS_ENCHANTABLE_FIRE_ASPECT = Bukkit.getTag(REGISTRY_ITEMS, NamespacedKey.minecraft("enchantable/fire_aspect"), Material.class)
    """
    Vanilla item tag representing all items enchantable with the fire aspect enchantment.
    """
    ITEMS_ENCHANTABLE_SHARP_WEAPON = Bukkit.getTag(REGISTRY_ITEMS, NamespacedKey.minecraft("enchantable/sharp_weapon"), Material.class)
    """
    Vanilla item tag representing all items enchantable with the sharpness enchantment.
    """
    ITEMS_ENCHANTABLE_WEAPON = Bukkit.getTag(REGISTRY_ITEMS, NamespacedKey.minecraft("enchantable/weapon"), Material.class)
    """
    Vanilla item tag representing all enchantable weapons.
    """
    ITEMS_ENCHANTABLE_MINING = Bukkit.getTag(REGISTRY_ITEMS, NamespacedKey.minecraft("enchantable/mining"), Material.class)
    """
    Vanilla item tag representing all enchantable mining tools.
    """
    ITEMS_ENCHANTABLE_MINING_LOOT = Bukkit.getTag(REGISTRY_ITEMS, NamespacedKey.minecraft("enchantable/mining_loot"), Material.class)
    """
    Vanilla item tag representing all items enchantable with the mining_loot enchantment.
    """
    ITEMS_ENCHANTABLE_FISHING = Bukkit.getTag(REGISTRY_ITEMS, NamespacedKey.minecraft("enchantable/fishing"), Material.class)
    """
    Vanilla item tag representing all items enchantable with fishing enchantments.
    """
    ITEMS_ENCHANTABLE_TRIDENT = Bukkit.getTag(REGISTRY_ITEMS, NamespacedKey.minecraft("enchantable/trident"), Material.class)
    """
    Vanilla item tag representing all items enchantable with trident enchantments.
    """
    ITEMS_ENCHANTABLE_DURABILITY = Bukkit.getTag(REGISTRY_ITEMS, NamespacedKey.minecraft("enchantable/durability"), Material.class)
    """
    Vanilla item tag representing all items enchantable with durability enchantments.
    """
    ITEMS_ENCHANTABLE_BOW = Bukkit.getTag(REGISTRY_ITEMS, NamespacedKey.minecraft("enchantable/bow"), Material.class)
    """
    Vanilla item tag representing all items enchantable with bow enchantments.
    """
    ITEMS_ENCHANTABLE_EQUIPPABLE = Bukkit.getTag(REGISTRY_ITEMS, NamespacedKey.minecraft("enchantable/equippable"), Material.class)
    """
    Vanilla item tag representing all items enchantable with the binding enchantment.
    """
    ITEMS_ENCHANTABLE_CROSSBOW = Bukkit.getTag(REGISTRY_ITEMS, NamespacedKey.minecraft("enchantable/crossbow"), Material.class)
    """
    Vanilla item tag representing all items enchantable with crossbow enchantments.
    """
    ITEMS_ENCHANTABLE_VANISHING = Bukkit.getTag(REGISTRY_ITEMS, NamespacedKey.minecraft("enchantable/vanishing"), Material.class)
    """
    Vanilla item tag representing all items enchantable with the vanishing enchantment.
    """
    ITEMS_ENCHANTABLE_MACE = Bukkit.getTag(REGISTRY_ITEMS, NamespacedKey.minecraft("enchantable/mace"), Material.class)
    """
    Vanilla item tag representing all items enchantable with mace enchantments.
    """
    ITEMS_MAP_INVISIBILITY_EQUIPMENT = Bukkit.getTag(REGISTRY_ITEMS, NamespacedKey.minecraft("map_invisibility_equipment"), Material.class)
    """
    Vanilla item tag representing all items which when equipped will hide the entity from maps.
    """
    ITEMS_GAZE_DISGUISE_EQUIPMENT = Bukkit.getTag(REGISTRY_ITEMS, NamespacedKey.minecraft("gaze_disguise_equipment"), Material.class)
    """
    Vanilla item tag representing all items which disguise the wearer's gaze from other entities.
    """
    FREEZE_IMMUNE_WEARABLES = Bukkit.getTag(REGISTRY_ITEMS, NamespacedKey.minecraft("freeze_immune_wearables"), Material.class)
    """
    Vanilla item tag representing all items that confer freeze immunity on
    the wearer.
    """
    AXOLOTL_TEMPT_ITEMS = ITEMS_AXOLOTL_FOOD
    """
    Vanilla item tag representing all items which tempt axolotls.

    Deprecated
    - use .ITEMS_AXOLOTL_FOOD
    """
    CLUSTER_MAX_HARVESTABLES = Bukkit.getTag(REGISTRY_ITEMS, NamespacedKey.minecraft("cluster_max_harvestables"), Material.class)
    """
    Vanilla item tag representing all items which are preferred for
    harvesting clusters (unused).
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
    REGISTRY_ENTITY_TYPES = "entity_types"
    """
    Key for the built in entity registry.
    """
    ENTITY_TYPES_SKELETONS = Bukkit.getTag(REGISTRY_ENTITY_TYPES, NamespacedKey.minecraft("skeletons"), EntityType.class)
    """
    Vanilla tag representing skeletons.
    """
    ENTITY_TYPES_RAIDERS = Bukkit.getTag(REGISTRY_ENTITY_TYPES, NamespacedKey.minecraft("raiders"), EntityType.class)
    """
    Vanilla tag representing raiders.
    """
    ENTITY_TYPES_BEEHIVE_INHABITORS = Bukkit.getTag(REGISTRY_ENTITY_TYPES, NamespacedKey.minecraft("beehive_inhabitors"), EntityType.class)
    """
    Vanilla tag representing entities which can live in beehives.
    """
    ENTITY_TYPES_ARROWS = Bukkit.getTag(REGISTRY_ENTITY_TYPES, NamespacedKey.minecraft("arrows"), EntityType.class)
    """
    Vanilla tag representing arrows.
    """
    ENTITY_TYPES_IMPACT_PROJECTILES = Bukkit.getTag(REGISTRY_ENTITY_TYPES, NamespacedKey.minecraft("impact_projectiles"), EntityType.class)
    """
    Vanilla tag representing projectiles.
    """
    ENTITY_TYPES_POWDER_SNOW_WALKABLE_MOBS = Bukkit.getTag(REGISTRY_ENTITY_TYPES, NamespacedKey.minecraft("powder_snow_walkable_mobs"), EntityType.class)
    """
    Vanilla tag representing mobs which can walk on powder snow.
    """
    ENTITY_TYPES_AXOLOTL_ALWAYS_HOSTILES = Bukkit.getTag(REGISTRY_ENTITY_TYPES, NamespacedKey.minecraft("axolotl_always_hostiles"), EntityType.class)
    """
    Vanilla tag representing which entities axolotls are always hostile to.
    """
    ENTITY_TYPES_AXOLOTL_HUNT_TARGETS = Bukkit.getTag(REGISTRY_ENTITY_TYPES, NamespacedKey.minecraft("axolotl_hunt_targets"), EntityType.class)
    """
    Vanilla tag representing axolotl targets.
    """
    ENTITY_TYPES_FREEZE_IMMUNE_ENTITY_TYPES = Bukkit.getTag(REGISTRY_ENTITY_TYPES, NamespacedKey.minecraft("freeze_immune_entity_types"), EntityType.class)
    """
    Vanilla tag representing entities immune from freezing.
    """
    ENTITY_TYPES_FREEZE_HURTS_EXTRA_TYPES = Bukkit.getTag(REGISTRY_ENTITY_TYPES, NamespacedKey.minecraft("freeze_hurts_extra_types"), EntityType.class)
    """
    Vanilla tag representing entities extra susceptible to freezing.
    """
    ENTITY_TYPES_FROG_FOOD = Bukkit.getTag(REGISTRY_ENTITY_TYPES, NamespacedKey.minecraft("frog_food"), EntityType.class)
    """
    Vanilla tag representing entities which can be eaten by frogs.
    """
    ENTITY_TYPES_FALL_DAMAGE_IMMUNE = Bukkit.getTag(REGISTRY_ENTITY_TYPES, NamespacedKey.minecraft("fall_damage_immune"), EntityType.class)
    """
    Vanilla tag representing entities which are immune from fall damage.
    """
    ENTITY_TYPES_DISMOUNTS_UNDERWATER = Bukkit.getTag(REGISTRY_ENTITY_TYPES, NamespacedKey.minecraft("dismounts_underwater"), EntityType.class)
    """
    Vanilla tag representing entities which are dismounted when underwater.
    """
    ENTITY_TYPES_NON_CONTROLLING_RIDER = Bukkit.getTag(REGISTRY_ENTITY_TYPES, NamespacedKey.minecraft("non_controlling_rider"), EntityType.class)
    """
    Vanilla tag representing entities which are not controlled by their mount.
    """
    ENTITY_TYPES_DEFLECTS_PROJECTILES = Bukkit.getTag(REGISTRY_ENTITY_TYPES, NamespacedKey.minecraft("deflects_projectiles"), EntityType.class)
    """
    Vanilla tag representing entities which deflect projectiles.
    """
    ENTITY_TYPES_DEFLECTS_ARROWS = ENTITY_TYPES_DEFLECTS_PROJECTILES
    """
    Vanilla tag representing entities which deflect arrows.

    Deprecated
    - use .ENTITY_TYPES_DEFLECTS_PROJECTILES
    """
    ENTITY_TYPES_CAN_TURN_IN_BOATS = Bukkit.getTag(REGISTRY_ENTITY_TYPES, NamespacedKey.minecraft("can_turn_in_boats"), EntityType.class)
    """
    Vanilla tag representing entities which can turn in boats.
    """
    ENTITY_TYPES_ILLAGER = Bukkit.getTag(REGISTRY_ENTITY_TYPES, NamespacedKey.minecraft("illager"), EntityType.class)
    """
    Vanilla tag representing all entities sensitive to illager enchantments.
    """
    ENTITY_TYPES_AQUATIC = Bukkit.getTag(REGISTRY_ENTITY_TYPES, NamespacedKey.minecraft("aquatic"), EntityType.class)
    """
    Vanilla tag representing all entities sensitive to aquatic enchantments..
    """
    ENTITY_TYPES_ARTHROPOD = Bukkit.getTag(REGISTRY_ENTITY_TYPES, NamespacedKey.minecraft("arthropod"), EntityType.class)
    """
    Vanilla tag representing all entities sensitive to arthropod enchantments..
    """
    ENTITY_TYPES_IGNORES_POISON_AND_REGEN = Bukkit.getTag(REGISTRY_ENTITY_TYPES, NamespacedKey.minecraft("ignores_poison_and_regen"), EntityType.class)
    """
    Vanilla tag representing all entities which ignores poison and regeneration effects.
    """
    ENTITY_TYPES_INVERTED_HEALING_AND_HARM = Bukkit.getTag(REGISTRY_ENTITY_TYPES, NamespacedKey.minecraft("inverted_healing_and_harm"), EntityType.class)
    """
    Vanilla tag representing all entities which are sensitive to inverted healing and harm potion effects.
    """
    ENTITY_TYPES_WITHER_FRIENDS = Bukkit.getTag(REGISTRY_ENTITY_TYPES, NamespacedKey.minecraft("wither_friends"), EntityType.class)
    """
    Vanilla tag representing all entities which are friendly with withers.
    """
    ENTITY_TYPES_ILLAGER_FRIENDS = Bukkit.getTag(REGISTRY_ENTITY_TYPES, NamespacedKey.minecraft("illager_friends"), EntityType.class)
    """
    Vanilla tag representing all entities which are friendly with illagers.
    """
    ENTITY_TYPES_NOT_SCARY_FOR_PUFFERFISH = Bukkit.getTag(REGISTRY_ENTITY_TYPES, NamespacedKey.minecraft("not_scary_for_pufferfish"), EntityType.class)
    """
    Vanilla tag representing all entities which are not scary for pufferfish.
    """
    ENTITY_TYPES_SENSITIVE_TO_IMPALING = Bukkit.getTag(REGISTRY_ENTITY_TYPES, NamespacedKey.minecraft("sensitive_to_impaling"), EntityType.class)
    """
    Vanilla tag representing all entities which are sensitive to impaling.
    """
    ENTITY_TYPES_SENSITIVE_TO_BANE_OF_ARTHROPODS = Bukkit.getTag(REGISTRY_ENTITY_TYPES, NamespacedKey.minecraft("sensitive_to_bane_of_arthropods"), EntityType.class)
    """
    Vanilla tag representing all entities which are sensitive to the bane_of_arthropods enchantment.
    """
    ENTITY_TYPES_SENSITIVE_TO_SMITE = Bukkit.getTag(REGISTRY_ENTITY_TYPES, NamespacedKey.minecraft("sensitive_to_smite"), EntityType.class)
    """
    Vanilla tag representing all entities which are sensitive to the smite enchantment.
    """
    ENTITY_TYPES_NO_ANGER_FROM_WIND_CHARGE = Bukkit.getTag(REGISTRY_ENTITY_TYPES, NamespacedKey.minecraft("no_anger_from_wind_charge"), EntityType.class)
    """
    Vanilla tag representing all entities which do not receive anger from wind charges.
    """
    ENTITY_TYPES_IMMUNE_TO_OOZING = Bukkit.getTag(REGISTRY_ENTITY_TYPES, NamespacedKey.minecraft("immune_to_oozing"), EntityType.class)
    """
    Vanilla tag representing all entities which are immune from the oozing effect.
    """
    ENTITY_TYPES_IMMUNE_TO_INFESTED = Bukkit.getTag(REGISTRY_ENTITY_TYPES, NamespacedKey.minecraft("immune_to_infested"), EntityType.class)
    """
    Vanilla tag representing all entities which are immune from the infested effect.
    """
    ENTITY_TYPES_REDIRECTABLE_PROJECTILE = Bukkit.getTag(REGISTRY_ENTITY_TYPES, NamespacedKey.minecraft("redirectable_projectile"), EntityType.class)
    """
    Vanilla tag representing all projectiles which can be punched back.
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
