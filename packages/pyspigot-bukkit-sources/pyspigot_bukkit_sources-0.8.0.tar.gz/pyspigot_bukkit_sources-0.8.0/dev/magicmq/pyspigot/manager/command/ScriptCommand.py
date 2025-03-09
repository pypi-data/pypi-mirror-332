"""
Python module generated from Java source file dev.magicmq.pyspigot.manager.command.ScriptCommand

Java source file obtained from artifact pyspigot-core version 0.8.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from dev.magicmq.pyspigot.manager.command import *
from dev.magicmq.pyspigot.manager.script import Script
from typing import Any, Callable, Iterable, Tuple


class ScriptCommand:
    """
    A command registered by a script. Meant to be implemented by platform-specific classes that also implement or extend an API's command executor class/interface.
    """

    def getScript(self) -> "Script":
        """
        Get the script associated with this command.

        Returns
        - The script associated with this command
        """
        ...


    def getName(self) -> str:
        """
        Get the name of this command.

        Returns
        - The name of this command
        """
        ...
