"""
Python module generated from Java source file dev.magicmq.pyspigot.bukkit.manager.command.BukkitCommandManager

Java source file obtained from artifact pyspigot-bukkit version 0.8.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from dev.magicmq.pyspigot import PyCore
from dev.magicmq.pyspigot.bukkit.manager.command import *
from dev.magicmq.pyspigot.bukkit.util import ReflectionUtils
from dev.magicmq.pyspigot.manager.command import CommandManager
from dev.magicmq.pyspigot.manager.command import ScriptCommand
from dev.magicmq.pyspigot.manager.script import Script
from java.lang.reflect import Field
from java.lang.reflect import InvocationTargetException
from java.lang.reflect import Method
from org.bukkit import Bukkit
from org.bukkit.command import Command
from org.bukkit.command import SimpleCommandMap
from org.python.core import PyFunction
from typing import Any, Callable, Iterable, Tuple


class BukkitCommandManager(CommandManager):
    """
    The Bukkit-specific implementation of the command manager.
    """

    @staticmethod
    def get() -> "BukkitCommandManager":
        """
        Get the singleton instance of this BukkitCommandManager.

        Returns
        - The instance
        """
        ...
