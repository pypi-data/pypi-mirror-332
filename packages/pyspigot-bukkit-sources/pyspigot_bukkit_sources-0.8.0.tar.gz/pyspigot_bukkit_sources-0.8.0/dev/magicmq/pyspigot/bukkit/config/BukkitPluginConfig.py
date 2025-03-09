"""
Python module generated from Java source file dev.magicmq.pyspigot.bukkit.config.BukkitPluginConfig

Java source file obtained from artifact pyspigot-bukkit version 0.8.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from dev.magicmq.pyspigot.bukkit import PySpigot
from dev.magicmq.pyspigot.bukkit.config import *
from dev.magicmq.pyspigot.config import PluginConfig
from java.time.format import DateTimeFormatter
from java.util import Properties
from org.bukkit.configuration.file import FileConfiguration
from typing import Any, Callable, Iterable, Tuple


class BukkitPluginConfig(PluginConfig):
    """
    The Bukkit-specific implementation of the dev.magicmq.pyspigot.config.PluginConfig class, for retreiving values from the plugin config.yml.
    """

    def reload(self) -> None:
        ...


    def getMetricsEnabled(self) -> bool:
        ...


    def getScriptLoadDelay(self) -> int:
        ...


    def getLibraryRelocations(self) -> dict[str, str]:
        ...


    def getLogTimestamp(self) -> "DateTimeFormatter":
        ...


    def doScriptActionLogging(self) -> bool:
        ...


    def doVerboseRedisLogging(self) -> bool:
        ...


    def doScriptUnloadOnPluginDisable(self) -> bool:
        ...


    def scriptOptionEnabled(self) -> bool:
        ...


    def scriptOptionLoadPriority(self) -> int:
        ...


    def scriptOptionPluginDepend(self) -> list[str]:
        ...


    def scriptOptionFileLoggingEnabled(self) -> bool:
        ...


    def scriptOptionMinLoggingLevel(self) -> str:
        ...


    def scriptOptionPermissionDefault(self) -> str:
        ...


    def scriptOptionPermissions(self) -> dict[Any, Any]:
        ...


    def shouldPrintStackTraces(self) -> bool:
        ...


    def shouldShowUpdateMessages(self) -> bool:
        ...


    def loadJythonOnStartup(self) -> bool:
        ...


    def getJythonProperties(self) -> "Properties":
        ...


    def getJythonArgs(self) -> list[str]:
        ...
