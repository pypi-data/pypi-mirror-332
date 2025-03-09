"""
Python module generated from Java source file dev.magicmq.pyspigot.bukkit.manager.listener.BukkitScriptEventListener

Java source file obtained from artifact pyspigot-bukkit version 0.8.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from dev.magicmq.pyspigot.bukkit.manager.listener import *
from dev.magicmq.pyspigot.manager.script import Script
from org.bukkit.event import Event
from org.bukkit.event import Listener
from org.python.core import PyFunction
from typing import Any, Callable, Iterable, Tuple


class BukkitScriptEventListener(Listener):
    """
    A dummy Bukkit Listener that holds an event a script is currently listening to.

    See
    - org.bukkit.event.Listener
    """

    def __init__(self, script: "Script", listenerFunction: Callable, event: type["Event"]):
        """
        Arguments
        - script: The script listening to events within this listener
        - listenerFunction: The script function that should be called when the event occurs
        - event: The Bukkit event associated with this listener. Should be a Class of the Bukkit event
        """
        ...


    def getScript(self) -> "Script":
        """
        Get the script associated with this listener.

        Returns
        - The script associated with this listener.
        """
        ...


    def getListenerFunction(self) -> Callable:
        """
        Get the script function that should be called when the event occurs.

        Returns
        - The script function that should be called when the event occurs
        """
        ...


    def getEvent(self) -> type["Event"]:
        """
        Get the Bukkit event associated with this listener.
        
        Note: Because of the way scripts register events, this will be a Class of the Bukkit event, which essentially represents its type.

        Returns
        - The Bukkit event associated with this listener.
        """
        ...


    def getEventExecutor(self) -> "BukkitScriptEventExecutor":
        """
        Get the BukkitScriptEventExecutor associated with this script event listener.

        Returns
        - The BukkitScriptEventExecutor associated with this script event listener
        """
        ...


    def toString(self) -> str:
        """
        Prints a representation of this BukkitScriptEventListener in string format, including the event being listened to by the listener

        Returns
        - A string representation of the ScriptEventListener
        """
        ...
