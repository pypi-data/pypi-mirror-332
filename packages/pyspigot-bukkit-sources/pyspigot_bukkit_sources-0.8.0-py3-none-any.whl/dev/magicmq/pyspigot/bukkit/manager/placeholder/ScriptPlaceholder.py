"""
Python module generated from Java source file dev.magicmq.pyspigot.bukkit.manager.placeholder.ScriptPlaceholder

Java source file obtained from artifact pyspigot-bukkit version 0.8.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from dev.magicmq.pyspigot.bukkit.manager.placeholder import *
from dev.magicmq.pyspigot.manager.script import Script
from dev.magicmq.pyspigot.manager.script import ScriptManager
from me.clip.placeholderapi.expansion import PlaceholderExpansion
from me.clip.placeholderapi.expansion import Relational
from org.bukkit import OfflinePlayer
from org.bukkit.entity import Player
from org.python.core import Py
from org.python.core import PyException
from org.python.core import PyFunction
from org.python.core import PyObject
from org.python.core import PyString
from typing import Any, Callable, Iterable, Tuple


class ScriptPlaceholder(PlaceholderExpansion, Relational):
    """
    A class that represents a script placeholder expansion.
    
    A ScriptPlaceholder can have multiple individual placeholders. For example, a script with the name "test.py" could have "%script:test_placeholder1%" and "%script:test_placeholder2%". It will be up to the script to handle each individual placeholder.

    See
    - me.clip.placeholderapi.expansion.PlaceholderExpansion
    """

    def __init__(self, script: "Script", function: Callable, relFunction: Callable, author: str, version: str):
        """
        Arguments
        - script: The script associated with this ScriptPlaceholder
        - function: The function to call when the placeholder is used
        - relFunction: The function to call when the relational placeholder is used
        - author: The author of this ScriptPlaceholder
        - version: The version of this ScriptPlaceholder
        """
        ...


    def getScript(self) -> "Script":
        """
        Get the script associated with this ScriptPlaceholder.

        Returns
        - The script associated with this ScriptPlaceholder
        """
        ...


    def getAuthor(self) -> str:
        """
        Get the author of this ScriptPlaceholder.

        Returns
        - The author of this ScriptPlaceholder
        """
        ...


    def getVersion(self) -> str:
        """
        Get the version of this ScriptPlaceholder.

        Returns
        - The version of this ScriptPlaceholder
        """
        ...


    def getIdentifier(self) -> str:
        """
        Get the identifier of this ScriptPlaceholder.
        
        This is used to identify the script's placeholder. It will be in the format "script:name", where "name" is the name of the script (without the file extension, .py). For example, for a script named "test.py", the placeholder identifier will be "script:test".

        Returns
        - The identifier of this ScriptPlaceholder
        """
        ...


    def persist(self) -> bool:
        """
        Indicates that the ScriptPlaceholder should persist when PlaceholderAPI is reloaded.

        Returns
        - True
        """
        ...


    def onRequest(self, player: "OfflinePlayer", params: str) -> str:
        """
        Called internally when the ScriptPlaceholder is used.

        Arguments
        - player: The org.bukkit.OfflinePlayer associated with the placeholder, or null if there is none
        - params: The specific placeholder that was used (the ScriptPlaceholder expansion can have multiple individual placeholders. Scripts will handle each specific placeholder on their own)

        Returns
        - The replaced text
        """
        ...


    def onPlaceholderRequest(self, playerOne: "Player", playerTwo: "Player", identifier: str) -> str:
        """
        Called internally when the ScriptPlaceholder is used in a relational fashion.

        Arguments
        - playerOne: The first org.bukkit.entity.Player used for the placeholder.
        - playerTwo: The second org.bukkit.entity.Player used for the placeholder.
        - identifier: The specific placeholder that was used, right after the relational aspect.

        Returns
        - The replaced text
        """
        ...
