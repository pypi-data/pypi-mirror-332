"""
Python module generated from Java source file org.bukkit.plugin.PluginDescriptionFile

Java source file obtained from artifact spigot-api version 1.21.2-R0.1-20241023.084343-5

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.collect import ImmutableList
from com.google.common.collect import ImmutableMap
from com.google.common.collect import ImmutableSet
from java.io import InputStream
from java.io import Reader
from java.io import Writer
from java.util import Locale
from java.util.regex import Pattern
from org.bukkit.command import Command
from org.bukkit.command import CommandExecutor
from org.bukkit.command import CommandSender
from org.bukkit.command import PluginCommand
from org.bukkit.command import TabCompleter
from org.bukkit.permissions import Permissible
from org.bukkit.permissions import Permission
from org.bukkit.permissions import PermissionDefault
from org.bukkit.plugin import *
from org.bukkit.plugin.java import JavaPlugin
from org.yaml.snakeyaml import DumperOptions
from org.yaml.snakeyaml import LoaderOptions
from org.yaml.snakeyaml import Yaml
from org.yaml.snakeyaml.constructor import AbstractConstruct
from org.yaml.snakeyaml.constructor import SafeConstructor
from org.yaml.snakeyaml.nodes import Node
from org.yaml.snakeyaml.nodes import Tag
from org.yaml.snakeyaml.representer import Representer
from typing import Any, Callable, Iterable, Tuple


class PluginDescriptionFile:
    """
    This type is the runtime-container for the information in the plugin.yml.
    All plugins must have a respective plugin.yml. For plugins written in java
    using the standard plugin loader, this file must be in the root of the jar
    file.
    
    When Bukkit loads a plugin, it needs to know some basic information about
    it. It reads this information from a YAML file, 'plugin.yml'. This file
    consists of a set of attributes, each defined on a new line and with no
    indentation.
    
    Every (almost* every) method corresponds with a specific entry in the
    plugin.yml. These are the **required** entries for every plugin.yml:
    
    - .getName() - `name`
    - .getVersion() - `version`
    - .getMain() - `main`
    
    
    Failing to include any of these items will throw an exception and cause the
    server to ignore your plugin.
    
    This is a list of the possible yaml keys, with specific details included in
    the respective method documentations:
    <table border=1>
    <caption>The description of the plugin.yml layout</caption>
    <tr>
        <th>Node</th>
        <th>Method</th>
        <th>Summary</th>
    </tr><tr>
        <td>`name`</td>
        <td>.getName()</td>
        <td>The unique name of plugin</td>
    </tr><tr>
        <td>`provides`</td>
        <td>.getProvides()</td>
        <td>The plugin APIs which this plugin provides</td>
    </tr><tr>
        <td>`version`</td>
        <td>.getVersion()</td>
        <td>A plugin revision identifier</td>
    </tr><tr>
        <td>`main`</td>
        <td>.getMain()</td>
        <td>The plugin's initial class file</td>
    </tr><tr>
        <td>`author``authors`</td>
        <td>.getAuthors()</td>
        <td>The plugin authors</td>
    </tr><tr>
        <td>`contributors`</td>
        <td>.getContributors()</td>
        <td>The plugin contributors</td>
    </tr><tr>
        <td>`description`</td>
        <td>.getDescription()</td>
        <td>Human readable plugin summary</td>
    </tr><tr>
        <td>`website`</td>
        <td>.getWebsite()</td>
        <td>The URL to the plugin's site</td>
    </tr><tr>
        <td>`prefix`</td>
        <td>.getPrefix()</td>
        <td>The token to prefix plugin log entries</td>
    </tr><tr>
        <td>`load`</td>
        <td>.getLoad()</td>
        <td>The phase of server-startup this plugin will load during</td>
    </tr><tr>
        <td>`depend`</td>
        <td>.getDepend()</td>
        <td>Other required plugins</td>
    </tr><tr>
        <td>`softdepend`</td>
        <td>.getSoftDepend()</td>
        <td>Other plugins that add functionality</td>
    </tr><tr>
        <td>`loadbefore`</td>
        <td>.getLoadBefore()</td>
        <td>The inverse softdepend</td>
    </tr><tr>
        <td>`commands`</td>
        <td>.getCommands()</td>
        <td>The commands the plugin will register</td>
    </tr><tr>
        <td>`permissions`</td>
        <td>.getPermissions()</td>
        <td>The permissions the plugin will register</td>
    </tr><tr>
        <td>`default-permission`</td>
        <td>.getPermissionDefault()</td>
        <td>The default Permission.getDefault() default permission
            state for defined .getPermissions() permissions the plugin
            will register</td>
    </tr><tr>
        <td>`awareness`</td>
        <td>.getAwareness()</td>
        <td>The concepts that the plugin acknowledges</td>
    </tr><tr>
        <td>`api-version`</td>
        <td>.getAPIVersion()</td>
        <td>The API version which this plugin was programmed against</td>
    </tr><tr>
        <td>`libraries`</td>
        <td>.getLibraries() ()</td>
        <td>The libraries to be linked with this plugin</td>
    </tr>
    </table>
    
    A plugin.yml example:<blockquote>```
    name: Inferno
    provides: [Hell]
    version: 1.4.1
    description: This plugin is so 31337. You can set yourself on fire.
    # We could place every author in the authors list, but chose not to for illustrative purposes
    # Also, having an author distinguishes that person as the project lead, and ensures their
    # name is displayed first
    author: CaptainInflamo
    authors: [Cogito, verrier, EvilSeph]
    contributors: [Choco, md_5]
    website: http://www.curse.com/server-mods/minecraft/myplugin
    
    main: com.captaininflamo.bukkit.inferno.Inferno
    depend: [NewFire, FlameWire]
    api-version: 1.13
    libraries:
        - com.squareup.okhttp3:okhttp:4.9.0
    
    commands:
     flagrate:
       description: Set yourself on fire.
       aliases: [combust_me, combustMe]
       permission: inferno.flagrate
       usage: Syntax error! Simply type /&lt;command&gt; to ignite yourself.
     burningdeaths:
       description: List how many times you have died by fire.
       aliases: [burning_deaths, burningDeaths]
       permission: inferno.burningdeaths
       usage: |
         /&lt;command&gt; [player]
         Example: /&lt;command&gt; - see how many times you have burned to death
         Example: /&lt;command&gt; CaptainIce - see how many times CaptainIce has burned to death
    
    permissions:
     inferno.*:
       description: Gives access to all Inferno commands
       children:
         inferno.flagrate: True
         inferno.burningdeaths: True
         inferno.burningdeaths.others: True
     inferno.flagrate:
       description: Allows you to ignite yourself
       default: True
     inferno.burningdeaths:
       description: Allows you to see how many times you have burned to death
       default: True
     inferno.burningdeaths.others:
       description: Allows you to see how many times others have burned to death
       default: op
       children:
         inferno.burningdeaths: True
    ```</blockquote>
    """

    def __init__(self, stream: "InputStream"):
        ...


    def __init__(self, reader: "Reader"):
        """
        Loads a PluginDescriptionFile from the specified reader

        Arguments
        - reader: The reader

        Raises
        - InvalidDescriptionException: If the PluginDescriptionFile is
            invalid
        """
        ...


    def __init__(self, pluginName: str, pluginVersion: str, mainClass: str):
        """
        Creates a new PluginDescriptionFile with the given detailed

        Arguments
        - pluginName: Name of this plugin
        - pluginVersion: Version of this plugin
        - mainClass: Full location of the main class of this plugin
        """
        ...


    def getName(self) -> str:
        """
        Gives the name of the plugin. This name is a unique identifier for
        plugins.
        
        - Must consist of all alphanumeric characters, underscores, hyphon,
            and period (a-z,A-Z,0-9, _.-). Any other character will cause the
            plugin.yml to fail loading.
        - Used to determine the name of the plugin's data folder. Data
            folders are placed in the ./plugins/ directory by default, but this
            behavior should not be relied on. Plugin.getDataFolder()
            should be used to reference the data folder.
        - It is good practice to name your jar the same as this, for example
            'MyPlugin.jar'.
        - Case sensitive.
        - The is the token referenced in .getDepend(), .getSoftDepend(), and .getLoadBefore().
        - Using spaces in the plugin's name is deprecated.
        
        
        In the plugin.yml, this entry is named `name`.
        
        Example:<blockquote>```name: MyPlugin```</blockquote>

        Returns
        - the name of the plugin
        """
        ...


    def getProvides(self) -> list[str]:
        """
        Gives the list of other plugin APIs which this plugin provides.
        These are usable for other plugins to depend on.
        
        - Must consist of all alphanumeric characters, underscores, hyphon,
            and period (a-z,A-Z,0-9, _.-). Any other character will cause the
            plugin.yml to fail loading.
        - A different plugin providing the same one or using it as their name
            will not result in the plugin to fail loading.
        - Case sensitive.
        - An entry of this list can be referenced in .getDepend(),
           .getSoftDepend(), and .getLoadBefore().
        - `provides` must be in <a
            href="https://en.wikipedia.org/wiki/YAML#Lists">YAML list
            format</a>.
        
        
        In the plugin.yml, this entry is named `provides`.
        
        Example:
        <blockquote>```provides:
        - OtherPluginName
        - OldPluginName```</blockquote>

        Returns
        - immutable list of the plugin APIs which this plugin provides
        """
        ...


    def getVersion(self) -> str:
        """
        Gives the version of the plugin.
        
        - Version is an arbitrary string, however the most common format is
            MajorRelease.MinorRelease.Build (eg: 1.4.1).
        - Typically you will increment this every time you release a new
            feature or bug fix.
        - Displayed when a user types `/version PluginName`
        
        
        In the plugin.yml, this entry is named `version`.
        
        Example:<blockquote>```version: 1.4.1```</blockquote>

        Returns
        - the version of the plugin
        """
        ...


    def getMain(self) -> str:
        """
        Gives the fully qualified name of the main class for a plugin. The
        format should follow the ClassLoader.loadClass(String) syntax
        to successfully be resolved at runtime. For most plugins, this is the
        class that extends JavaPlugin.
        
        - This must contain the full namespace including the class file
            itself.
        - If your namespace is `org.bukkit.plugin`, and your class
            file is called `MyPlugin` then this must be
            `org.bukkit.plugin.MyPlugin`
        - No plugin can use `org.bukkit.` as a base package for
            **any class**, including the main class.
        
        
        In the plugin.yml, this entry is named `main`.
        
        Example:
        <blockquote>```main: org.bukkit.plugin.MyPlugin```</blockquote>

        Returns
        - the fully qualified main class for the plugin
        """
        ...


    def getDescription(self) -> str:
        """
        Gives a human-friendly description of the functionality the plugin
        provides.
        
        - The description can have multiple lines.
        - Displayed when a user types `/version PluginName`
        
        
        In the plugin.yml, this entry is named `description`.
        
        Example:
        <blockquote>```description: This plugin is so 31337. You can set yourself on fire.```</blockquote>

        Returns
        - description of this plugin, or null if not specified
        """
        ...


    def getLoad(self) -> "PluginLoadOrder":
        """
        Gives the phase of server startup that the plugin should be loaded.
        
        - Possible values are in PluginLoadOrder.
        - Defaults to PluginLoadOrder.POSTWORLD.
        - Certain caveats apply to each phase.
        - When different, .getDepend(), .getSoftDepend(), and
            .getLoadBefore() become relative in order loaded per-phase.
            If a plugin loads at `STARTUP`, but a dependency loads
            at `POSTWORLD`, the dependency will not be loaded before
            the plugin is loaded.
        
        
        In the plugin.yml, this entry is named `load`.
        
        Example:<blockquote>```load: STARTUP```</blockquote>

        Returns
        - the phase when the plugin should be loaded
        """
        ...


    def getAuthors(self) -> list[str]:
        """
        Gives the list of authors for the plugin.
        
        - Gives credit to the developer.
        - Used in some server error messages to provide helpful feedback on
            who to contact when an error occurs.
        - A SpigotMC forum handle or email address is recommended.
        - Is displayed when a user types `/version PluginName`
        - `authors` must be in <a
            href="https://en.wikipedia.org/wiki/YAML#Lists">YAML list
            format</a>.
        
        
        In the plugin.yml, this has two entries, `author` and
        `authors`.
        
        Single author example:
        <blockquote>```author: CaptainInflamo```</blockquote>
        Multiple author example:
        <blockquote>```authors: [Cogito, verrier, EvilSeph]```</blockquote>
        When both are specified, author will be the first entry in the list, so
        this example:
        <blockquote>```author: Grum
        authors:
        - feildmaster
        - amaranth```</blockquote>
        Is equivilant to this example:
        ```authors: [Grum, feildmaster, aramanth]```

        Returns
        - an immutable list of the plugin's authors
        """
        ...


    def getContributors(self) -> list[str]:
        """
        Gives the list of contributors for the plugin.
        
        - Gives credit to those that have contributed to the plugin, though
            not enough so to warrant authorship.
        - Unlike .getAuthors(), contributors will not be mentioned in
        server error messages as a means of contact.
        - A SpigotMC forum handle or email address is recommended.
        - Is displayed when a user types `/version PluginName`
        - `contributors` must be in <a
            href="https://en.wikipedia.org/wiki/YAML#Lists">YAML list
            format</a>.
        
        
        Example:
        <blockquote>```authors: [Choco, md_5]```</blockquote>

        Returns
        - an immutable list of the plugin's contributors
        """
        ...


    def getWebsite(self) -> str:
        """
        Gives the plugin's or plugin's author's website.
        
        - A link to the Curse page that includes documentation and downloads
            is highly recommended.
        - Displayed when a user types `/version PluginName`
        
        
        In the plugin.yml, this entry is named `website`.
        
        Example:
        <blockquote>```website: http://www.curse.com/server-mods/minecraft/myplugin```</blockquote>

        Returns
        - description of this plugin, or null if not specified
        """
        ...


    def getDepend(self) -> list[str]:
        """
        Gives a list of other plugins that the plugin requires.
        
        - Use the value in the .getName() of the target plugin to
            specify the dependency.
        - If any plugin listed here is not found, your plugin will fail to
            load at startup.
        - If multiple plugins list each other in `depend`,
            creating a network with no individual plugin does not list another
            plugin in the <a
            href=https://en.wikipedia.org/wiki/Circular_dependency>network</a>,
            all plugins in that network will fail.
        - `depend` must be in <a
            href="https://en.wikipedia.org/wiki/YAML#Lists">YAML list
            format</a>.
        
        
        In the plugin.yml, this entry is named `depend`.
        
        Example:
        <blockquote>```depend:
        - OnePlugin
        - AnotherPlugin```</blockquote>

        Returns
        - immutable list of the plugin's dependencies
        """
        ...


    def getSoftDepend(self) -> list[str]:
        """
        Gives a list of other plugins that the plugin requires for full
        functionality. The PluginManager will make best effort to treat
        all entries here as if they were a .getDepend() dependency, but
        will never fail because of one of these entries.
        
        - Use the value in the .getName() of the target plugin to
            specify the dependency.
        - When an unresolvable plugin is listed, it will be ignored and does
            not affect load order.
        - When a circular dependency occurs (a network of plugins depending
            or soft-dependending each other), it will arbitrarily choose a
            plugin that can be resolved when ignoring soft-dependencies.
        - `softdepend` must be in <a
            href="https://en.wikipedia.org/wiki/YAML#Lists">YAML list
            format</a>.
        
        
        In the plugin.yml, this entry is named `softdepend`.
        
        Example:
        <blockquote>```softdepend: [OnePlugin, AnotherPlugin]```</blockquote>

        Returns
        - immutable list of the plugin's preferred dependencies
        """
        ...


    def getLoadBefore(self) -> list[str]:
        """
        Gets the list of plugins that should consider this plugin a
        soft-dependency.
        
        - Use the value in the .getName() of the target plugin to
            specify the dependency.
        - The plugin should load before any other plugins listed here.
        - Specifying another plugin here is strictly equivalent to having the
            specified plugin's .getSoftDepend() include .getName() this plugin.
        - `loadbefore` must be in <a
            href="https://en.wikipedia.org/wiki/YAML#Lists">YAML list
            format</a>.
        
        
        In the plugin.yml, this entry is named `loadbefore`.
        
        Example:
        <blockquote>```loadbefore:
        - OnePlugin
        - AnotherPlugin```</blockquote>

        Returns
        - immutable list of plugins that should consider this plugin a
            soft-dependency
        """
        ...


    def getPrefix(self) -> str:
        """
        Gives the token to prefix plugin-specific logging messages with.
        
        - This includes all messages using Plugin.getLogger().
        - If not specified, the server uses the plugin's .getName()
            name.
        - This should clearly indicate what plugin is being logged.
        
        
        In the plugin.yml, this entry is named `prefix`.
        
        Example:<blockquote>```prefix: ex-why-zee```</blockquote>

        Returns
        - the prefixed logging token, or null if not specified
        """
        ...


    def getCommands(self) -> dict[str, dict[str, "Object"]]:
        """
        Gives the map of command-name to command-properties. Each entry in this
        map corresponds to a single command and the respective values are the
        properties of the command. Each property, *with the exception of
        aliases*, can be defined at runtime using methods in PluginCommand and are defined here only as a convenience.
        <table border=1>
        <caption>The command section's description</caption>
        <tr>
            <th>Node</th>
            <th>Method</th>
            <th>Type</th>
            <th>Description</th>
            <th>Example</th>
        </tr><tr>
            <td>`description`</td>
            <td>PluginCommand.setDescription(String)</td>
            <td>String</td>
            <td>A user-friendly description for a command. It is useful for
                documentation purposes as well as in-game help.</td>
            <td><blockquote>```description: Set yourself on fire```</blockquote></td>
        </tr><tr>
            <td>`aliases`</td>
            <td>PluginCommand.setAliases(List)</td>
            <td>String or <a
                href="https://en.wikipedia.org/wiki/YAML#Lists">List</a> of
                strings</td>
            <td>Alternative command names, with special usefulness for commands
                that are already registered. *Aliases are not effective when
                defined at runtime,* so the plugin description file is the
                only way to have them properly defined.
                
                Note: Command aliases may not have a colon in them.</td>
            <td>Single alias format:
                <blockquote>```aliases: combust_me```</blockquote> or
                multiple alias format:
                <blockquote>```aliases: [combust_me, combustMe]```</blockquote></td>
        </tr><tr>
            <td>`permission`</td>
            <td>PluginCommand.setPermission(String)</td>
            <td>String</td>
            <td>The name of the Permission required to use the command.
                A user without the permission will receive the specified
                message (see PluginCommand.setPermissionMessage(String) below), or a
                standard one if no specific message is defined. Without the
                permission node, no PluginCommand.setExecutor(CommandExecutor) CommandExecutor or
                PluginCommand.setTabCompleter(TabCompleter) will be called.</td>
            <td><blockquote>```permission: inferno.flagrate```</blockquote></td>
        </tr><tr>
            <td>`permission-message`</td>
            <td>PluginCommand.setPermissionMessage(String)</td>
            <td>String</td>
            <td>
                - Displayed to a player that attempts to use a command, but
                    does not have the required permission. See PluginCommand.getPermission() above.
                - &lt;permission&gt; is a macro that is replaced with the
                    permission node required to use the command.
                - Using empty quotes is a valid way to indicate nothing
                    should be displayed to a player.
                </td>
            <td><blockquote>```permission-message: You do not have /&lt;permission&gt;```</blockquote></td>
        </tr><tr>
            <td>`usage`</td>
            <td>PluginCommand.setUsage(String)</td>
            <td>String</td>
            <td>This message is displayed to a player when the PluginCommand.setExecutor(CommandExecutor) CommandExecutor.onCommand(CommandSender, Command, String, String[]) returns False.
                &lt;command&gt; is a macro that is replaced the command issued.</td>
            <td><blockquote>```usage: Syntax error! Perhaps you meant /&lt;command&gt; PlayerName?```</blockquote>
                It is worth noting that to use a colon in a yaml, like
                ``usage: Usage: /god [player]'`, you need to
                <a href="http://yaml.org/spec/current.html#id2503232">surround
                the message with double-quote</a>:
                <blockquote>```usage: "Usage: /god [player]"```</blockquote></td>
        </tr>
        </table>
        The commands are structured as a hiearchy of <a
        href="http://yaml.org/spec/current.html#id2502325">nested mappings</a>.
        The primary (top-level, no intendentation) node is
        ``commands`', while each individual command name is
        indented, indicating it maps to some value (in our case, the
        properties of the table above).
        
        Here is an example bringing together the piecemeal examples above, as
        well as few more definitions:<blockquote>```
        commands:
         flagrate:
           description: Set yourself on fire.
           aliases: [combust_me, combustMe]
           permission: inferno.flagrate
           permission-message: You do not have /&lt;permission&gt;
           usage: Syntax error! Perhaps you meant /&lt;command&gt; PlayerName?
         burningdeaths:
           description: List how many times you have died by fire.
           aliases:
           - burning_deaths
           - burningDeaths
           permission: inferno.burningdeaths
           usage: |
             /&lt;command&gt; [player]
             Example: /&lt;command&gt; - see how many times you have burned to death
             Example: /&lt;command&gt; CaptainIce - see how many times CaptainIce has burned to death
         # The next command has no description, aliases, etc. defined, but is still valid
         # Having an empty declaration is useful for defining the description, permission, and messages from a configuration dynamically
         apocalypse:
        ```</blockquote>
        Note: Command names may not have a colon in their name.

        Returns
        - the commands this plugin will register
        """
        ...


    def getPermissions(self) -> list["Permission"]:
        """
        Gives the list of permissions the plugin will register at runtime,
        immediately proceding enabling. The format for defining permissions is
        a map from permission name to properties. To represent a map without
        any specific property, empty <a
        href="http://yaml.org/spec/current.html#id2502702">curly-braces</a> (
        `&#123;&#125;` ) may be used (as a null value is not
        accepted, unlike the .getCommands() commands above).
        
        A list of optional properties for permissions:
        <table border=1>
        <caption>The permission section's description</caption>
        <tr>
            <th>Node</th>
            <th>Description</th>
            <th>Example</th>
        </tr><tr>
            <td>`description`</td>
            <td>Plaintext (user-friendly) description of what the permission
                is for.</td>
            <td><blockquote>```description: Allows you to set yourself on fire```</blockquote></td>
        </tr><tr>
            <td>`default`</td>
            <td>The default state for the permission, as defined by Permission.getDefault(). If not defined, it will be set to
                the value of PluginDescriptionFile.getPermissionDefault().
                
                For reference:
                - `True` - Represents a positive assignment to
                    Permissible permissibles.
                - `False` - Represents no assignment to Permissible permissibles.
                - `op` - Represents a positive assignment to
                    Permissible.isOp() operator permissibles.
                - `notop` - Represents a positive assignment to
                    Permissible.isOp() non-operator permissibiles.
                </td>
            <td><blockquote>```default: True```</blockquote></td>
        </tr><tr>
            <td>`children`</td>
            <td>Allows other permissions to be set as a Permission.getChildren() relation to the parent permission.
                When a parent permissions is assigned, child permissions are
                respectively assigned as well.
                
                - When a parent permission is assigned negatively, child
                    permissions are assigned based on an inversion of their
                    association.
                - When a parent permission is assigned positively, child
                    permissions are assigned based on their association.
                
                
                Child permissions may be defined in a number of ways:
                - Children may be defined as a <a
                    href="https://en.wikipedia.org/wiki/YAML#Lists">list</a> of
                    names. Using a list will treat all children associated
                    positively to their parent.
                - Children may be defined as a map. Each permission name maps
                    to either a boolean (representing the association), or a
                    nested permission definition (just as another permission).
                    Using a nested definition treats the child as a positive
                    association.
                - A nested permission definition must be a map of these same
                    properties. To define a valid nested permission without
                    defining any specific property, empty curly-braces (
                    `&#123;&#125;` ) must be used.
                 - A nested permission may carry it's own nested permissions
                     as children, as they may also have nested permissions, and
                     so forth. There is no direct limit to how deep the
                     permission tree is defined.
                </td>
            <td>As a list:
                <blockquote>```children: [inferno.flagrate, inferno.burningdeaths]```</blockquote>
                Or as a mapping:
                <blockquote>```children:
         inferno.flagrate: True
         inferno.burningdeaths: True```</blockquote>
                An additional example showing basic nested values can be seen
                <a href="doc-files/permissions-example_plugin.yml">here</a>.
                </td>
        </tr>
        </table>
        The permissions are structured as a hiearchy of <a
        href="http://yaml.org/spec/current.html#id2502325">nested mappings</a>.
        The primary (top-level, no intendentation) node is
        ``permissions`', while each individual permission name is
        indented, indicating it maps to some value (in our case, the
        properties of the table above).
        
        Here is an example using some of the properties:<blockquote>```
        permissions:
         inferno.*:
           description: Gives access to all Inferno commands
           children:
             inferno.flagrate: True
             inferno.burningdeaths: True
         inferno.flagate:
           description: Allows you to ignite yourself
           default: True
         inferno.burningdeaths:
           description: Allows you to see how many times you have burned to death
           default: True
        ```</blockquote>
        Another example, with nested definitions, can be found <a
        href="doc-files/permissions-example_plugin.yml">here</a>.

        Returns
        - the permissions this plugin will register
        """
        ...


    def getPermissionDefault(self) -> "PermissionDefault":
        """
        Gives the default Permission.getDefault() default state of
        .getPermissions() permissions registered for the plugin.
        
        - If not specified, it will be PermissionDefault.OP.
        - It is matched using PermissionDefault.getByName(String)
        - It only affects permissions that do not define the
            `default` node.
        - It may be any value in PermissionDefault.
        
        
        In the plugin.yml, this entry is named `default-permission`.
        
        Example:<blockquote>```default-permission: NOT_OP```</blockquote>

        Returns
        - the default value for the plugin's permissions
        """
        ...


    def getAwareness(self) -> set["PluginAwareness"]:
        """
        Gives a set of every PluginAwareness for a plugin. An awareness
        dictates something that a plugin developer acknowledges when the plugin
        is compiled. Some implementions may define extra awarenesses that are
        not included in the API. Any unrecognized
        awareness (one unsupported or in a future version) will cause a dummy
        object to be created instead of failing.
        
        
        - Currently only supports the enumerated values in PluginAwareness.Flags.
        - Each awareness starts the identifier with bang-at
            (`!@`).
        - Unrecognized (future / unimplemented) entries are quietly replaced
            by a generic object that implements PluginAwareness.
        - A type of awareness must be defined by the runtime and acknowledged
            by the API, effectively discluding any derived type from any
            plugin's classpath.
        - `awareness` must be in <a
            href="https://en.wikipedia.org/wiki/YAML#Lists">YAML list
            format</a>.
        
        
        In the plugin.yml, this entry is named `awareness`.
        
        Example:<blockquote>```awareness:
        - !@UTF8```</blockquote>
        
        **Note:** Although unknown versions of some future awareness are
        gracefully substituted, previous versions of Bukkit (ones prior to the
        first implementation of awareness) will fail to load a plugin that
        defines any awareness.

        Returns
        - a set containing every awareness for the plugin
        """
        ...


    def getFullName(self) -> str:
        """
        Returns the name of a plugin, including the version. This method is
        provided for convenience; it uses the .getName() and .getVersion() entries.

        Returns
        - a descriptive name of the plugin and respective version
        """
        ...


    def getAPIVersion(self) -> str:
        """
        Gives the API version which this plugin is designed to support. No
        specific format is guaranteed.
        
        - Refer to release notes for supported API versions.
        
        
        In the plugin.yml, this entry is named `api-version`.
        
        Example:<blockquote>```api-version: 1.13```</blockquote>

        Returns
        - the version of the plugin
        """
        ...


    def getLibraries(self) -> list[str]:
        """
        Gets the libraries this plugin requires. This is a preview feature.
        
        - Libraries must be GAV specifiers and are loaded from Maven Central.
        
        
        Example:<blockquote>```libraries:
            - com.squareup.okhttp3:okhttp:4.9.0```</blockquote>

        Returns
        - required libraries
        """
        ...


    def getClassLoaderOf(self) -> str:
        """
        Returns
        - unused

        Deprecated
        - unused
        """
        ...


    def save(self, writer: "Writer") -> None:
        """
        Saves this PluginDescriptionFile to the given writer

        Arguments
        - writer: Writer to output this file to
        """
        ...


    def getRawName(self) -> str:
        """
        Returns
        - internal use

        Unknown Tags
        - Internal use
        """
        ...
