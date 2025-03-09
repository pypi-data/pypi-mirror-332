"""
Python module generated from Java source file dev.magicmq.pyspigot.bukkit.manager.task.BukkitTaskManager

Java source file obtained from artifact pyspigot-bukkit version 0.8.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from dev.magicmq.pyspigot.bukkit import PySpigot
from dev.magicmq.pyspigot.bukkit.manager.task import *
from dev.magicmq.pyspigot.manager.task import RepeatingTask
from dev.magicmq.pyspigot.manager.task import SyncCallbackTask
from dev.magicmq.pyspigot.manager.task import Task
from dev.magicmq.pyspigot.manager.task import TaskManager
from org.bukkit import Bukkit
from typing import Any, Callable, Iterable, Tuple


class BukkitTaskManager(TaskManager):
    """
    The Bukkit-specific implementation of the task manager.
    """

    @staticmethod
    def get() -> "BukkitTaskManager":
        """
        Get the singleton instance of this BukkitTaskManager.

        Returns
        - The instance
        """
        ...
