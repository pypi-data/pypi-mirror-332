"""
Python module generated from Java source file dev.magicmq.pyspigot.PluginListener

Java source file obtained from artifact pyspigot-core version 0.8.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from dev.magicmq.pyspigot import *
from dev.magicmq.pyspigot.util import StringUtils
from dev.magicmq.pyspigot.util.player import PlayerAdapter
from net.md_5.bungee.api import ChatColor
from net.md_5.bungee.api.chat import BaseComponent
from net.md_5.bungee.api.chat import ClickEvent
from net.md_5.bungee.api.chat import ComponentBuilder
from net.md_5.bungee.api.chat import HoverEvent
from net.md_5.bungee.api.chat import TextComponent
from typing import Any, Callable, Iterable, Tuple


class PluginListener:
    """
    The primary listener for PySpigot. Methods called in this class are called via platform-specific listeners.
    """


