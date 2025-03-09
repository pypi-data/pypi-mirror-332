"""
Python module generated from Java source file dev.magicmq.pyspigot.manager.script.ScriptInfo

Java source file obtained from artifact pyspigot-core version 0.8.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from dev.magicmq.pyspigot import PyCore
from dev.magicmq.pyspigot.manager.command import CommandManager
from dev.magicmq.pyspigot.manager.database import Database
from dev.magicmq.pyspigot.manager.database import DatabaseManager
from dev.magicmq.pyspigot.manager.listener import ListenerManager
from dev.magicmq.pyspigot.manager.redis import RedisManager
from dev.magicmq.pyspigot.manager.redis.client import ScriptRedisClient
from dev.magicmq.pyspigot.manager.script import *
from dev.magicmq.pyspigot.manager.task import Task
from dev.magicmq.pyspigot.manager.task import TaskManager
from dev.magicmq.pyspigot.util import StringUtils
from java.nio.file import Path
from java.time import Duration
from net.md_5.bungee.api import ChatColor
from typing import Any, Callable, Iterable, Tuple


class ScriptInfo:
    """
    A utility class that fetches and returns a script's info.
    """

    def printPlatformManagerInfo(self, script: "Script", appendTo: "StringBuilder") -> None:
        """
        Print platform-specific manager information for a script.

        Arguments
        - script: The script whose information should be printed
        - appendTo: The info StringBuilder that platform-specific manager info should be appended to
        """
        ...


    def printScriptInfo(self, script: "Script") -> str:
        """
        Print a script's info (for the /pyspigot info command).

        Arguments
        - script: The script whose information should be printed

        Returns
        - The info for the script
        """
        ...


    def printOfflineScriptInfo(self, scriptName: str, scriptPath: "Path", options: "ScriptOptions") -> str:
        """
        Print a script's info (for the /pyspigot info command), if the script is not loaded.

        Arguments
        - scriptName: The name of the script whose information should be printed
        - scriptPath: The path of the script
        - options: The options of the script

        Returns
        - The info for the script
        """
        ...
