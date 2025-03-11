"""
Python module generated from Java source file org.bukkit.Registry

Java source file obtained from artifact spigot-api version 1.21.1-R0.1-20241022.152140-54

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.base import Preconditions
from com.google.common.base import Predicates
from com.google.common.collect import ImmutableMap
from java.util import Iterator
from java.util import Locale
from java.util import Objects
from java.util.function import Predicate
from java.util.stream import Stream
from java.util.stream import StreamSupport
from org.bukkit import *
from org.bukkit.advancement import Advancement
from org.bukkit.attribute import Attribute
from org.bukkit.block import Biome
from org.bukkit.block import BlockType
from org.bukkit.block.banner import PatternType
from org.bukkit.boss import KeyedBossBar
from org.bukkit.damage import DamageType
from org.bukkit.enchantments import Enchantment
from org.bukkit.entity import Cat
from org.bukkit.entity import EntityType
from org.bukkit.entity import Frog
from org.bukkit.entity import Villager
from org.bukkit.entity import Wolf
from org.bukkit.entity.memory import MemoryKey
from org.bukkit.generator.structure import Structure
from org.bukkit.generator.structure import StructureType
from org.bukkit.inventory import ItemType
from org.bukkit.inventory import MenuType
from org.bukkit.inventory.meta.trim import TrimMaterial
from org.bukkit.inventory.meta.trim import TrimPattern
from org.bukkit.loot import LootTables
from org.bukkit.map import MapCursor
from org.bukkit.potion import PotionEffectType
from org.bukkit.potion import PotionType
from typing import Any, Callable, Iterable, Tuple


class Registry(Iterable):
    """
    Represents a registry of Bukkit objects that may be retrieved by
    NamespacedKey.
    
    Type `<T>`: type of item in the registry
    """

    ADVANCEMENT = Registry<Advancement>() {
    
        @Nullable
        @Override
        public Advancement get(@NotNull NamespacedKey key) {
            return Bukkit.getAdvancement(key);
        }
    
        @NotNull
        @Override
        public Advancement getOrThrow(@NotNull NamespacedKey key) {
            Advancement advancement = get(key);
            Preconditions.checkArgument(advancement != null, "No Advancement registry entry found for key %s.", key);
            return advancement;
        }
    
        @NotNull
        @Override
        public Stream<Advancement> stream() {
            return StreamSupport.stream(spliterator(), false);
        }
    
        @NotNull
        @Override
        public Iterator<Advancement> iterator() {
            return Bukkit.advancementIterator();
        }
    }
    """
    Server advancements.

    See
    - Bukkit.advancementIterator()
    """
    ART = SimpleRegistry<>(Art.class)
    """
    Server art.

    See
    - Art
    """
    ATTRIBUTE = SimpleRegistry<>(Attribute.class)
    """
    Attribute.

    See
    - Attribute
    """
    BANNER_PATTERN = Objects.requireNonNull(Bukkit.getRegistry(PatternType.class), "No registry present for Pattern Type. This is a bug.")
    """
    Server banner patterns.

    See
    - PatternType
    """
    BIOME = SimpleRegistry<>(Biome.class)
    """
    Server biomes.

    See
    - Biome
    """
    BLOCK = Objects.requireNonNull(Bukkit.getRegistry(BlockType.class), "No registry present for BlockType. This is a bug.")
    """
    Server block types.

    See
    - BlockType

    Unknown Tags
    - BlockType is not ready for public usage yet
    """
    BOSS_BARS = Registry<KeyedBossBar>() {
    
        @Nullable
        @Override
        public KeyedBossBar get(@NotNull NamespacedKey key) {
            return Bukkit.getBossBar(key);
        }
    
        @NotNull
        @Override
        public KeyedBossBar getOrThrow(@NotNull NamespacedKey key) {
            KeyedBossBar keyedBossBar = get(key);
            Preconditions.checkArgument(keyedBossBar != null, "No KeyedBossBar registry entry found for key %s.", key);
            return keyedBossBar;
        }
    
        @NotNull
        @Override
        public Stream<KeyedBossBar> stream() {
            return StreamSupport.stream(spliterator(), false);
        }
    
        @NotNull
        @Override
        public Iterator<KeyedBossBar> iterator() {
            return Bukkit.getBossBars();
        }
    }
    """
    Custom boss bars.

    See
    - Bukkit.getBossBars()
    """
    CAT_VARIANT = Objects.requireNonNull(Bukkit.getRegistry(Cat.Type.class), "No registry present for Cat Type. This is a bug.")
    """
    Server cat types.

    See
    - Cat.Type
    """
    ENCHANTMENT = Objects.requireNonNull(Bukkit.getRegistry(Enchantment.class), "No registry present for Enchantment. This is a bug.")
    """
    Server enchantments.

    See
    - Enchantment
    """
    ENTITY_TYPE = SimpleRegistry<>(EntityType.class, (entity) -> entity != EntityType.UNKNOWN)
    """
    Server entity types.

    See
    - EntityType
    """
    INSTRUMENT = Objects.requireNonNull(Bukkit.getRegistry(MusicInstrument.class), "No registry present for MusicInstrument. This is a bug.")
    """
    Server instruments.

    See
    - MusicInstrument
    """
    ITEM = Objects.requireNonNull(Bukkit.getRegistry(ItemType.class), "No registry present for ItemType. This is a bug.")
    """
    Server item types.

    See
    - ItemType

    Unknown Tags
    - ItemType is not ready for public usage yet
    """
    LOOT_TABLES = SimpleRegistry<>(LootTables.class)
    """
    Default server loot tables.

    See
    - LootTables
    """
    MATERIAL = SimpleRegistry<>(Material.class, (mat) -> !mat.isLegacy())
    """
    Server materials.

    See
    - Material
    """
    MENU = Objects.requireNonNull(Bukkit.getRegistry(MenuType.class), "No registry present for MenuType. This is a bug.")
    """
    Server menus.

    See
    - MenuType
    """
    EFFECT = Objects.requireNonNull(Bukkit.getRegistry(PotionEffectType.class), "No registry present for PotionEffectType. This is a bug.")
    """
    Server mob effects.

    See
    - PotionEffectType
    """
    PARTICLE_TYPE = SimpleRegistry<>(Particle.class, (par) -> par.register)
    """
    Server particles.

    See
    - Particle
    """
    POTION = SimpleRegistry<>(PotionType.class)
    """
    Server potions.

    See
    - PotionType
    """
    STATISTIC = SimpleRegistry<>(Statistic.class)
    """
    Server statistics.

    See
    - Statistic
    """
    STRUCTURE = Objects.requireNonNull(Bukkit.getRegistry(Structure.class), "No registry present for Structure. This is a bug.")
    """
    Server structures.

    See
    - Structure
    """
    STRUCTURE_TYPE = Objects.requireNonNull(Bukkit.getRegistry(StructureType.class), "No registry present for StructureType. This is a bug.")
    """
    Server structure types.

    See
    - StructureType
    """
    SOUNDS = SimpleRegistry<>(Sound.class)
    """
    Sound keys.

    See
    - Sound
    """
    TRIM_MATERIAL = Objects.requireNonNull(Bukkit.getRegistry(TrimMaterial.class), "No registry present for TrimMaterial. This is a bug.")
    """
    Trim materials.

    See
    - TrimMaterial
    """
    TRIM_PATTERN = Objects.requireNonNull(Bukkit.getRegistry(TrimPattern.class), "No registry present for TrimPattern. This is a bug.")
    """
    Trim patterns.

    See
    - TrimPattern
    """
    DAMAGE_TYPE = Objects.requireNonNull(Bukkit.getRegistry(DamageType.class), "No registry present for DamageType. This is a bug.")
    """
    Damage types.

    See
    - DamageType
    """
    JUKEBOX_SONG = Objects.requireNonNull(Bukkit.getRegistry(JukeboxSong.class), "No registry present for JukeboxSong. This is a bug.")
    """
    Jukebox songs.

    See
    - JukeboxSong
    """
    VILLAGER_PROFESSION = Objects.requireNonNull(Bukkit.getRegistry(Villager.Profession.class), "No registry present for Villager Profession. This is a bug.")
    """
    Villager profession.

    See
    - Villager.Profession
    """
    VILLAGER_TYPE = Objects.requireNonNull(Bukkit.getRegistry(Villager.Type.class), "No registry present for Villager Type. This is a bug.")
    """
    Villager type.

    See
    - Villager.Type
    """
    MEMORY_MODULE_TYPE = Registry<MemoryKey>() {
    
        @NotNull
        @Override
        public Iterator iterator() {
            return MemoryKey.values().iterator();
        }
    
        @Nullable
        @Override
        public MemoryKey get(@NotNull NamespacedKey key) {
            return MemoryKey.getByKey(key);
        }
    
        @NotNull
        @Override
        public MemoryKey getOrThrow(@NotNull NamespacedKey key) {
            MemoryKey memoryKey = get(key);
            Preconditions.checkArgument(memoryKey != null, "No MemoryKey registry entry found for key %s.", key);
            return memoryKey;
        }
    
        @NotNull
        @Override
        public Stream<MemoryKey> stream() {
            return StreamSupport.stream(spliterator(), false);
        }
    }
    """
    Memory Keys.

    See
    - MemoryKey
    """
    FLUID = SimpleRegistry<>(Fluid.class)
    """
    Server fluids.

    See
    - Fluid
    """
    FROG_VARIANT = Objects.requireNonNull(Bukkit.getRegistry(Frog.Variant.class), "No registry present for Frog Variant. This is a bug.")
    """
    Frog variants.

    See
    - Frog.Variant
    """
    WOLF_VARIANT = Objects.requireNonNull(Bukkit.getRegistry(Wolf.Variant.class), "No registry present for Wolf Variant. This is a bug.")
    """
    Wolf variants.

    See
    - Wolf.Variant
    """
    MAP_DECORATION_TYPE = Objects.requireNonNull(Bukkit.getRegistry(MapCursor.Type.class), "No registry present for MapCursor Type. This is a bug.")
    """
    Map cursor types.

    See
    - MapCursor.Type
    """
    GAME_EVENT = Objects.requireNonNull(Bukkit.getRegistry(GameEvent.class), "No registry present for GameEvent. This is a bug.")
    """
    Game events.

    See
    - GameEvent
    """


    def get(self, key: "NamespacedKey") -> "T":
        """
        Get the object by its key.

        Arguments
        - key: non-null key

        Returns
        - item or null if does not exist
        """
        ...


    def getOrThrow(self, key: "NamespacedKey") -> "T":
        """
        Get the object by its key.
        
        If there is no object with the given key, an exception will be thrown.

        Arguments
        - key: to get the object from

        Returns
        - object with the given key

        Raises
        - IllegalArgumentException: if there is no object with the given key
        """
        ...


    def stream(self) -> "Stream"["T"]:
        """
        Returns a new stream, which contains all registry items, which are registered to the registry.

        Returns
        - a stream of all registry items
        """
        ...


    def match(self, input: str) -> "T":
        """
        Attempts to match the registered object with the given key.
        
        This will attempt to find a reasonable match based on the provided input
        and may do so through unspecified means.

        Arguments
        - input: non-null input

        Returns
        - registered object or null if does not exist
        """
        ...
