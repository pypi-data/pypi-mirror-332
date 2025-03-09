"""
Python module generated from Java source file dev.magicmq.pyspigot.bukkit.BukkitListener

Java source file obtained from artifact pyspigot-bukkit version 0.8.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from dev.magicmq.pyspigot import PluginListener
from dev.magicmq.pyspigot import PyCore
from dev.magicmq.pyspigot.bukkit import *
from dev.magicmq.pyspigot.bukkit.util.player import BukkitPlayer
from dev.magicmq.pyspigot.manager.script import Script
from dev.magicmq.pyspigot.manager.script import ScriptManager
from dev.magicmq.pyspigot.util.player import PlayerAdapter
from org.bukkit import Bukkit
from org.bukkit.event import EventHandler
from org.bukkit.event import Listener
from org.bukkit.event.player import PlayerJoinEvent
from org.bukkit.event.server import PluginDisableEvent
from typing import Any, Callable, Iterable, Tuple


class BukkitListener(PluginListener, Listener):
    """
    The Bukkit listener.
    """

    def onDisable(self, event: "PluginDisableEvent") -> None:
        ...


    def onJoin(self, event: "PlayerJoinEvent") -> None:
        ...
