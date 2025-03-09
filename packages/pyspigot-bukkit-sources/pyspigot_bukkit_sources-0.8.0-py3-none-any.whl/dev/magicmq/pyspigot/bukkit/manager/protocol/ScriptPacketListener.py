"""
Python module generated from Java source file dev.magicmq.pyspigot.bukkit.manager.protocol.ScriptPacketListener

Java source file obtained from artifact pyspigot-bukkit version 0.8.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.comphenix.protocol import PacketType
from com.comphenix.protocol.events import ListenerPriority
from com.comphenix.protocol.events import PacketAdapter
from com.comphenix.protocol.events import PacketEvent
from dev.magicmq.pyspigot.bukkit import PySpigot
from dev.magicmq.pyspigot.bukkit.manager.protocol import *
from dev.magicmq.pyspigot.manager.script import Script
from dev.magicmq.pyspigot.manager.script import ScriptManager
from org.python.core import Py
from org.python.core import PyException
from org.python.core import PyFunction
from org.python.core import PyObject
from typing import Any, Callable, Iterable, Tuple


class ScriptPacketListener(PacketAdapter):
    """
    An abstract class designed to represent a basic script packet listener.

    See
    - com.comphenix.protocol.events.PacketAdapter
    """

    def __init__(self, script: "Script", function: Callable, packetType: "PacketType", listenerPriority: "ListenerPriority", listenerType: "ListenerType"):
        """
        Arguments
        - script: The script associated with this packet listener
        - function: The function to be called when the packet event occurs
        - packetType: The packet type to listen for
        - listenerPriority: The com.comphenix.protocol.events.ListenerPriority of this listener
        - listenerType: The ListenerType of this listener
        """
        ...


    def getScript(self) -> "Script":
        """
        Get the script associated with this listener.

        Returns
        - The script associated with this listener
        """
        ...


    def getFunction(self) -> Callable:
        """
        Get the function that should be called when the packet event occurs.

        Returns
        - The function that should be called
        """
        ...


    def getPacketType(self) -> "PacketType":
        """
        Get the packet type being listener for.

        Returns
        - The packet type beign listened for
        """
        ...


    def getListenerType(self) -> "ListenerType":
        """
        The listener type of this listener.

        Returns
        - The ListenerType of this listener
        """
        ...


    def callToScript(self, event: "PacketEvent") -> None:
        """
        A helper method to call a script's packet listener function when the packet event occurs.

        Arguments
        - event: The event that occurred, will be passed to the script's function
        """
        ...


    def toString(self) -> str:
        """
        Prints a representation of this ScriptPacketListener in string format, including the packet type listened to by the listener

        Returns
        - A string representation of the ScriptPacketListener
        """
        ...
