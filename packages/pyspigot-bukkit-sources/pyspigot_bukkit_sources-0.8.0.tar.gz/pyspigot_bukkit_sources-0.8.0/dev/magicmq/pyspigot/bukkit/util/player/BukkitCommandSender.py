"""
Python module generated from Java source file dev.magicmq.pyspigot.bukkit.util.player.BukkitCommandSender

Java source file obtained from artifact pyspigot-bukkit version 0.8.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from dev.magicmq.pyspigot.bukkit.util.player import *
from dev.magicmq.pyspigot.util.player import CommandSenderAdapter
from net.md_5.bungee.api.chat import BaseComponent
from org.bukkit.command import CommandSender
from org.bukkit.entity import Player
from typing import Any, Callable, Iterable, Tuple


class BukkitCommandSender(CommandSenderAdapter):
    """
    A wrapper for the Bukkit org.bukkit.command.CommandSender class.
    """

    def __init__(self, sender: "CommandSender"):
        """
        Arguments
        - sender: The Bukkit CommandSender
        """
        ...


    def hasPermission(self, permission: str) -> bool:
        ...


    def sendMessage(self, message: str) -> None:
        ...


    def sendMessage(self, message: list["BaseComponent"]) -> None:
        ...


    def isPlayer(self) -> bool:
        ...
