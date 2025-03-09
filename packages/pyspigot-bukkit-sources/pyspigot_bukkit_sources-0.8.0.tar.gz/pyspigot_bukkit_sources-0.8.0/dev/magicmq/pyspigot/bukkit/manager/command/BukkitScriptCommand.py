"""
Python module generated from Java source file dev.magicmq.pyspigot.bukkit.manager.command.BukkitScriptCommand

Java source file obtained from artifact pyspigot-bukkit version 0.8.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from dev.magicmq.pyspigot.bukkit import PySpigot
from dev.magicmq.pyspigot.bukkit.manager.command import *
from dev.magicmq.pyspigot.bukkit.util import CommandAliasHelpTopic
from dev.magicmq.pyspigot.manager.command import ScriptCommand
from dev.magicmq.pyspigot.manager.script import Script
from dev.magicmq.pyspigot.manager.script import ScriptManager
from java.lang.reflect import Constructor
from java.lang.reflect import Field
from java.lang.reflect import InvocationTargetException
from java.util import Collections
from org.bukkit import Bukkit
from org.bukkit import ChatColor
from org.bukkit.command import Command
from org.bukkit.command import CommandSender
from org.bukkit.command import PluginCommand
from org.bukkit.command import TabExecutor
from org.bukkit.help import GenericCommandHelpTopic
from org.bukkit.help import HelpMap
from org.bukkit.help import HelpTopic
from org.bukkit.help import HelpTopicComparator
from org.bukkit.help import IndexHelpTopic
from org.bukkit.plugin import Plugin
from org.python.core import Py
from org.python.core import PyBoolean
from org.python.core import PyException
from org.python.core import PyFunction
from org.python.core import PyList
from org.python.core import PyObject
from typing import Any, Callable, Iterable, Tuple


class BukkitScriptCommand(TabExecutor, ScriptCommand):
    """
    Represents a registered Bukkit command belonging to a script.

    See
    - org.bukkit.command.defaults.BukkitCommand
    """

    def __init__(self, script: "Script", commandFunction: Callable, tabFunction: Callable, name: str, description: str, usage: str, aliases: list[str], permission: str):
        """
        Arguments
        - script: The script to which this command belongs
        - commandFunction: The command function that should be called when the command is executed
        - tabFunction: The tab function that should be called for tab completion of the command. Can be null
        - name: The name of the command to register
        - description: The description of the command. Use an empty string for no description
        - usage: The usage message for the command
        - aliases: A List of String containing all the aliases for this command. Use an empty list for no aliases
        - permission: The required permission node to use this command. Can be null
        """
        ...


    def onCommand(self, sender: "CommandSender", cmd: "Command", label: str, args: list[str]) -> bool:
        ...


    def onTabComplete(self, sender: "CommandSender", cmd: "Command", alias: str, args: list[str]) -> list[str]:
        ...


    def getScript(self) -> "Script":
        """
        Get the script associated with this command.

        Returns
        - The script associated with this command
        """
        ...


    def getName(self) -> str:
        """
        Get the name of this command.

        Returns
        - The name of this command
        """
        ...


    def getBukkitCommand(self) -> "PluginCommand":
        """
        Get the org.bukkit.command.PluginCommand that underlies this ScriptCommand

        Returns
        - The underlying PluginCommand
        """
        ...


    def toString(self) -> str:
        """
        Prints a representation of this ScriptCommand in string format, including all variables that pertain to the command (such as name, label, description, etc.)

        Returns
        - A string representation of the ScriptCommand
        """
        ...
