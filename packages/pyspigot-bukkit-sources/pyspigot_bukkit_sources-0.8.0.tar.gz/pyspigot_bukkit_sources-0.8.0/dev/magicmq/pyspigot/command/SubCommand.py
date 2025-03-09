"""
Python module generated from Java source file dev.magicmq.pyspigot.command.SubCommand

Java source file obtained from artifact pyspigot-core version 0.8.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from dev.magicmq.pyspigot.command import *
from dev.magicmq.pyspigot.util.player import CommandSenderAdapter
from java.util import Collections
from typing import Any, Callable, Iterable, Tuple


class SubCommand:

    def onCommand(self, sender: "CommandSenderAdapter", args: list[str]) -> bool:
        ...


    def onTabComplete(self, sender: "CommandSenderAdapter", args: list[str]) -> list[str]:
        ...
