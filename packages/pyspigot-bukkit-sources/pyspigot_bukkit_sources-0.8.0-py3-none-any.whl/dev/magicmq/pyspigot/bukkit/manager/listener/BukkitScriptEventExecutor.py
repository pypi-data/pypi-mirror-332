"""
Python module generated from Java source file dev.magicmq.pyspigot.bukkit.manager.listener.BukkitScriptEventExecutor

Java source file obtained from artifact pyspigot-bukkit version 0.8.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from dev.magicmq.pyspigot.bukkit.event import ScriptExceptionEvent
from dev.magicmq.pyspigot.bukkit.manager.listener import *
from dev.magicmq.pyspigot.manager.script import Script
from dev.magicmq.pyspigot.manager.script import ScriptManager
from org.bukkit.event import Event
from org.bukkit.event import Listener
from org.bukkit.plugin import EventExecutor
from org.python.core import Py
from org.python.core import PyException
from org.python.core import PyObject
from typing import Any, Callable, Iterable, Tuple


class BukkitScriptEventExecutor(EventExecutor):
    """
    Represents a Bukkit event executor for script event listeners.

    See
    - org.bukkit.plugin.EventExecutor
    """

    def __init__(self, scriptEventListener: "BukkitScriptEventListener", eventClass: type["Event"]):
        """
        Arguments
        - scriptEventListener: The BukkitScriptEventListener associated with this ScriptEventExecutor
        - eventClass: The Bukkit event associated with this ScriptEventExecutor. Should be a Class of the Bukkit event
        """
        ...


    def execute(self, listener: "Listener", event: "Event") -> None:
        """
        Called internally when the event occurs.

        Arguments
        - listener: The listener associated with this EventExecutor
        - event: The event that occurred
        """
        ...
