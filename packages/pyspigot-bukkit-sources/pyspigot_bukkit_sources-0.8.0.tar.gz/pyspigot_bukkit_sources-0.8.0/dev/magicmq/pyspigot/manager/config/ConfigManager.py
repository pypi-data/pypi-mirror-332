"""
Python module generated from Java source file dev.magicmq.pyspigot.manager.config.ConfigManager

Java source file obtained from artifact pyspigot-core version 0.8.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from dev.magicmq.pyspigot import PyCore
from dev.magicmq.pyspigot.manager.config import *
from java.io import IOException
from java.nio.file import Files
from java.nio.file import Path
from java.nio.file import Paths
from typing import Any, Callable, Iterable, Tuple


class ConfigManager:
    """
    Manager for scripts to interface with configuration files. Primarily used by scripts to load, write to, and save .yml files.
    """

    def loadConfig(self, filePath: str) -> "ScriptConfig":
        """
        Load a configuration file with the given path/name, relative to the `configs` folder. If the configuration file exists, it will load the existing file. If the configuration file does not exist, a new file will be created with the given path/name.
        
        **Note:** This should be called from scripts only!

        Arguments
        - filePath: The path of the configuration file to load, can be either the file name alone or a path (containing subfolders)

        Returns
        - A ScriptConfig representing the configuration file that was loaded

        Raises
        - IOException: If there was an IOException when attempting to load the configuration
        """
        ...


    def loadConfig(self, filePath: str, defaults: str) -> "ScriptConfig":
        """
        Load a configuration file with the given path/name, relative to the `configs` folder. If the configuration file exists, it will load the existing file. If the configuration file does not exist, a new file will be created with the given path/name.
        
        **Note:** This should be called from scripts only!

        Arguments
        - filePath: The path of the configuration file to load, can be either the file name alone or a path (containing subfolders)
        - defaults: A YAML-formatted string containing the desired default values for the configuration

        Returns
        - A ScriptConfig representing the configuration file that was loaded

        Raises
        - IOException: If there was an IOException when attempting to load the configuration
        """
        ...


    def doesConfigExist(self, filePath: str) -> bool:
        """
        Check if a configuration file exists with the given path/name, relative to the `configs` folder.
        
        **Note:** This should be called from scripts only!

        Arguments
        - filePath: The path of the configuration file to check, can be either the file name alone or a path (containing subfolders)

        Returns
        - True if the file exists, False if it does not
        """
        ...


    def createConfigIfNotExists(self, filePath: str) -> "Path":
        """
        Creates a config file with the given path if it did not previously exist.

        Arguments
        - filePath: The file path for the config file to create

        Returns
        - The Path to the config file

        Raises
        - IOException: If there was an IOException when attempting to create the config file
        """
        ...


    def deleteConfig(self, filePath: str) -> bool:
        """
        Delete a configuration file with the given path/name.
        
        **Note:** This should be called from scripts only!

        Arguments
        - filePath: The path of the configuration file to delete, relative to the `configs` folder. Can be either the file name alone or a path (containing subfolders)

        Returns
        - True if the file was deleted, False if the file could not be deleted because it does not exist

        Raises
        - IOException: If there was an IOException when attempting to delete the file
        """
        ...


    def getConfigFolder(self) -> "Path":
        """
        Get the path of the folder where script configuration files are stored.

        Returns
        - The path of the folder where script configuration files are stored
        """
        ...


    @staticmethod
    def get() -> "ConfigManager":
        """
        Get the singleton instance of this ConfigManager.

        Returns
        - The instance
        """
        ...
