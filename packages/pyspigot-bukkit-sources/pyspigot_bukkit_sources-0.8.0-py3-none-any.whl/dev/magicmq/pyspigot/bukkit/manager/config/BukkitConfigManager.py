"""
Python module generated from Java source file dev.magicmq.pyspigot.bukkit.manager.config.BukkitConfigManager

Java source file obtained from artifact pyspigot-bukkit version 0.8.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from dev.magicmq.pyspigot.bukkit.manager.config import *
from dev.magicmq.pyspigot.manager.config import ConfigManager
from dev.magicmq.pyspigot.manager.config import ScriptConfig
from java.io import IOException
from java.nio.file import Path
from typing import Any, Callable, Iterable, Tuple


class BukkitConfigManager(ConfigManager):
    """
    The Bukkit-specific implementation of the config manager.
    """

    @staticmethod
    def get() -> "BukkitConfigManager":
        """
        Get the singleton instance of this BukkitConfigManager.

        Returns
        - The instance
        """
        ...
