"""
Python module generated from Java source file dev.magicmq.pyspigot.command.subcommands.InfoCommand

Java source file obtained from artifact pyspigot version 0.7.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from dev.magicmq.pyspigot import PySpigot
from dev.magicmq.pyspigot.command import SubCommand
from dev.magicmq.pyspigot.command import SubCommandMeta
from dev.magicmq.pyspigot.command.subcommands import *
from dev.magicmq.pyspigot.manager.command import CommandManager
from dev.magicmq.pyspigot.manager.command import ScriptCommand
from dev.magicmq.pyspigot.manager.database import Database
from dev.magicmq.pyspigot.manager.database import DatabaseManager
from dev.magicmq.pyspigot.manager.listener import ListenerManager
from dev.magicmq.pyspigot.manager.listener import ScriptEventListener
from dev.magicmq.pyspigot.manager.placeholder import PlaceholderManager
from dev.magicmq.pyspigot.manager.placeholder import ScriptPlaceholder
from dev.magicmq.pyspigot.manager.protocol import ProtocolManager
from dev.magicmq.pyspigot.manager.protocol import ScriptPacketListener
from dev.magicmq.pyspigot.manager.redis import RedisManager
from dev.magicmq.pyspigot.manager.redis.client import ScriptRedisClient
from dev.magicmq.pyspigot.manager.script import Script
from dev.magicmq.pyspigot.manager.script import ScriptManager
from dev.magicmq.pyspigot.manager.script import ScriptOptions
from dev.magicmq.pyspigot.manager.task import Task
from dev.magicmq.pyspigot.manager.task import TaskManager
from dev.magicmq.pyspigot.util import StringUtils
from java.nio.file import Path
from java.time import Duration
from org.bukkit import ChatColor
from org.bukkit.command import CommandSender
from typing import Any, Callable, Iterable, Tuple


class InfoCommand(SubCommand):

    def onCommand(self, sender: "CommandSender", args: list[str]) -> bool:
        ...


    def onTabComplete(self, sender: "CommandSender", args: list[str]) -> list[str]:
        ...
