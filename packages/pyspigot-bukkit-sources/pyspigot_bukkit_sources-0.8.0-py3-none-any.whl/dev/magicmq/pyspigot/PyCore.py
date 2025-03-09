"""
Python module generated from Java source file dev.magicmq.pyspigot.PyCore

Java source file obtained from artifact pyspigot-core version 0.8.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from dev.magicmq.pyspigot import *
from dev.magicmq.pyspigot.config import PluginConfig
from dev.magicmq.pyspigot.config import ScriptOptionsConfig
from dev.magicmq.pyspigot.manager.database import DatabaseManager
from dev.magicmq.pyspigot.manager.libraries import LibraryManager
from dev.magicmq.pyspigot.manager.redis import RedisManager
from dev.magicmq.pyspigot.manager.script import GlobalVariables
from dev.magicmq.pyspigot.manager.script import ScriptManager
from dev.magicmq.pyspigot.util import StringUtils
from java.io import File
from java.io import FileOutputStream
from java.io import IOException
from java.io import InputStream
from java.io import OutputStream
from java.net import URL
from java.nio.file import Path
from java.util import Scanner
from typing import Any, Callable, Iterable, Tuple


class PyCore:
    """
    Core class of PySpigot for all platform-specific implementations. Platform-specific code is implemented via the PlatformAdapter.

    See
    - PlatformAdapter
    """

    @staticmethod
    def newInstance(adapter: "PlatformAdapter") -> None:
        """
        Initialize the PyCore instance.
        
        Called from the `onEnable` method of the platform-specific plugin class (PySpigot for Bukkit, for example).

        Arguments
        - adapter: The platform-specific adapter.
        """
        ...


    def init(self) -> None:
        """
        Initialize the plugin.
        """
        ...


    def shutdown(self) -> None:
        """
        Shutdown the plugin.
        """
        ...


    def reloadConfigs(self) -> None:
        """
        Reload the plugin config and the script options config.
        """
        ...


    def getLogger(self) -> "Logger":
        """
        Get the logger for PySpigot.

        Returns
        - The logger
        """
        ...


    def getDataFolder(self) -> "File":
        """
        Get the data folder for PySpigot.

        Returns
        - The data folder
        """
        ...


    def getDataFolderPath(self) -> "Path":
        """
        Get the path of the data folder for PySpigot.

        Returns
        - A path representing the data folder
        """
        ...


    def getPluginClassLoader(self) -> "ClassLoader":
        """
        Get the ClassLoader for PySpigot.

        Returns
        - The ClassLoader
        """
        ...


    def getVersion(self) -> str:
        """
        Get the version of the plugin.

        Returns
        - The version
        """
        ...


    def getPluginIdentifier(self) -> str:
        """
        Get the identifier of the plugin.

        Returns
        - The plugin identifier
        """
        ...


    def isPaper(self) -> bool:
        """
        Get if the server is running paper.

        Returns
        - True if the server is running paper, False if otherwise
        """
        ...


    def getConfig(self) -> "PluginConfig":
        """
        Get the plugin configuration for PySpigot.

        Returns
        - The PySpigot plugin config
        """
        ...


    def getSpigotVersion(self) -> str:
        """
        Get the latest available plugin version on Spigot.

        Returns
        - The latest available version on Spigot
        """
        ...


    def fetchSpigotVersion(self) -> None:
        """
        Fetch the latest available plugin version from SpigotMC.
        """
        ...


    def compareVersions(self) -> None:
        """
        Compare the current loaded plugin version with the cached latest SpigotMC plugin version, and log a message to console if the current version is detected as outdated.
        """
        ...


    def saveResource(self, resourcePath: str, replace: bool) -> None:
        """
        Save a resource from the plugin JAR file to the plugin data folder.

        Arguments
        - resourcePath: The path of the resource to save
        - replace: True if the file should be replaced (if it already exists in the data folder), False if it should not
        """
        ...


    @staticmethod
    def get() -> "PyCore":
        ...
