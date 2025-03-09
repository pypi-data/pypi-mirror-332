"""
Python module generated from Java source file dev.magicmq.pyspigot.bukkit.manager.listener.BukkitListenerManager

Java source file obtained from artifact pyspigot-bukkit version 0.8.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from dev.magicmq.pyspigot.bukkit import PySpigot
from dev.magicmq.pyspigot.bukkit.manager.listener import *
from dev.magicmq.pyspigot.manager.listener import ListenerManager
from dev.magicmq.pyspigot.manager.script import Script
from dev.magicmq.pyspigot.util import ScriptUtils
from java.lang.reflect import InvocationTargetException
from java.lang.reflect import Method
from org.bukkit import Bukkit
from org.bukkit.event import Event
from org.bukkit.event import EventPriority
from org.bukkit.event import HandlerList
from org.python.core import PyFunction
from typing import Any, Callable, Iterable, Tuple


class BukkitListenerManager(ListenerManager):
    """
    The Bukkit-specific implementation of the listener manager.
    """

    def registerListener(self, function: Callable, eventClass: type["Event"]) -> "BukkitScriptEventListener":
        ...


    def registerListener(self, function: Callable, eventClass: type["Event"], priority: "EventPriority") -> "BukkitScriptEventListener":
        ...


    def registerListener(self, function: Callable, eventClass: type["Event"], ignoreCancelled: bool) -> "BukkitScriptEventListener":
        ...


    def registerListener(self, function: Callable, eventClass: type["Event"], priority: "EventPriority", ignoreCancelled: bool) -> "BukkitScriptEventListener":
        ...


    def unregisterListener(self, listener: "BukkitScriptEventListener") -> None:
        ...


    def unregisterListeners(self, script: "Script") -> None:
        ...


    def getListener(self, script: "Script", eventClass: type["Event"]) -> "BukkitScriptEventListener":
        ...


    @staticmethod
    def get() -> "BukkitListenerManager":
        """
        Get the singleton instance of this BukkitListenerManager.

        Returns
        - The instance
        """
        ...
