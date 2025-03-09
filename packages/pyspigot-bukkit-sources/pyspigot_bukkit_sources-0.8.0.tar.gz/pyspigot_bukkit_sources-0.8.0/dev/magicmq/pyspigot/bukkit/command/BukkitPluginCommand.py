"""
Python module generated from Java source file dev.magicmq.pyspigot.bukkit.command.BukkitPluginCommand

Java source file obtained from artifact pyspigot-bukkit version 0.8.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from dev.magicmq.pyspigot.bukkit.command import *
from dev.magicmq.pyspigot.bukkit.util.player import BukkitCommandSender
from dev.magicmq.pyspigot.command import PySpigotCommand
from dev.magicmq.pyspigot.util.player import CommandSenderAdapter
from org.bukkit.command import Command
from org.bukkit.command import CommandSender
from org.bukkit.command import TabExecutor
from typing import Any, Callable, Iterable, Tuple


class BukkitPluginCommand(TabExecutor):
    """
    The executor for the /pyspigot command.
    """

    def __init__(self):
        ...


    def onCommand(self, sender: "CommandSender", command: "Command", label: str, args: list[str]) -> bool:
        ...


    def onTabComplete(self, sender: "CommandSender", command: "Command", alias: str, args: list[str]) -> list[str]:
        ...
