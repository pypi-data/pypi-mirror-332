"""
Python module generated from Java source file dev.magicmq.pyspigot.manager.task.TaskManager

Java source file obtained from artifact pyspigot-core version 0.8.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from dev.magicmq.pyspigot.manager.script import Script
from dev.magicmq.pyspigot.manager.task import *
from dev.magicmq.pyspigot.util import ScriptUtils
from org.python.core import PyFunction
from typing import Any, Callable, Iterable, Tuple


class TaskManager:
    """
    Manager to interface with a server platform's scheduler. Primarily used by scripts to register and unregister tasks.
    """

    def runTask(self, function: Callable, *functionArgs: Tuple["Object", ...]) -> int:
        """
        Schedule a new synchronous task via a platform-specific implementation.
        
        **Note:** This should be called from scripts only!

        Arguments
        - function: The function that should be called when the synchronous task executes
        - functionArgs: Any arguments that should be passed to the function

        Returns
        - An ID representing the synchronous task that was scheduled
        """
        ...


    def runTaskAsync(self, function: Callable, *functionArgs: Tuple["Object", ...]) -> int:
        """
        Schedule a new asynchronous task via a platform-specific implementation.
        
        **Note:** This should be called from scripts only!

        Arguments
        - function: The function that should be called when the asynchronous task executes
        - functionArgs: Any arguments that should be passed to the function

        Returns
        - An ID representing the asynchronous task that was scheduled
        """
        ...


    def runTaskLater(self, function: Callable, delay: int, *functionArgs: Tuple["Object", ...]) -> int:
        """
        Schedule a new synchronous task to run at a later point in time via a platform-specific implementation.
        
        **Note:** This should be called from scripts only!

        Arguments
        - function: The function that should be called when the synchronous task executes
        - delay: The delay, in ticks, that the scheduler should wait before executing the synchronous task
        - functionArgs: Any arguments that should be passed to the function

        Returns
        - An ID representing the synchronous task that was scheduled
        """
        ...


    def runTaskLaterAsync(self, function: Callable, delay: int, *functionArgs: Tuple["Object", ...]) -> int:
        """
        Schedule a new asynchronous task to run at a later point in time via a platform-specific implementation.
        
        **Note:** This should be called from scripts only!

        Arguments
        - function: The function that should be called when the asynchronous task executes
        - delay: The delay, in ticks, that the scheduler should wait before executing the asynchronous task
        - functionArgs: Any arguments that should be passed to the function

        Returns
        - An ID representing the asynchronous task that was scheduled
        """
        ...


    def scheduleRepeatingTask(self, function: Callable, delay: int, interval: int, *functionArgs: Tuple["Object", ...]) -> int:
        """
        Schedule a new synchronous repeating task via a platform-specific implementation.
        
        **Note:** This should be called from scripts only!

        Arguments
        - function: The function that should be called each time the synchronous task executes
        - delay: The delay, in ticks, to wait before beginning this synchronous repeating task
        - interval: The interval, in ticks, that the synchronous repeating task should be executed
        - functionArgs: Any arguments that should be passed to the function

        Returns
        - An ID representing the synchronous task that was scheduled
        """
        ...


    def scheduleAsyncRepeatingTask(self, function: Callable, delay: int, interval: int, *functionArgs: Tuple["Object", ...]) -> int:
        """
        Schedule a new asynchronous repeating task via a platform-specific implementation.
        
        **Note:** This should be called from scripts only!

        Arguments
        - function: The function that should be called each time the asynchronous task executes
        - delay: The delay, in ticks, to wait before beginning this asynchronous repeating task
        - interval: The interval, in ticks, that the asynchronous repeating task should be executed
        - functionArgs: Any arguments that should be passed to the function

        Returns
        - An ID representing the asynchronous task that was scheduled
        """
        ...


    def runSyncCallbackTask(self, function: Callable, callback: Callable, *functionArgs: Tuple["Object", ...]) -> int:
        """
        Schedule a new asynchronous task with a synchronous callback via a platform-specific implementation. Data returned from the initially called function (asynchronous portion) is automatically passed to the synchronous callback function as a function argument.
        
        **Note:** This should be called from scripts only!

        Arguments
        - function: The function that should be called when the asynchronous task executes
        - callback: The function that should be called for the synchronous callback once the asynchronous portion of the task finishes
        - functionArgs: Any arguments that should be passed to the function

        Returns
        - An ID representing the asynchronous task that was scheduled
        """
        ...


    def runSyncCallbackTaskLater(self, function: Callable, callback: Callable, delay: int, *functionArgs: Tuple["Object", ...]) -> int:
        """
        Schedule a new asynchronous task with a synchronous callback to run at a later point in time via a platform-specific implementation. Data returned from the initially called function (asynchronous portion) is automatically passed to the synchronous callback function as a function argument.
        
        **Note:** This should be called from scripts only!

        Arguments
        - function: The function that should be called when the asynchronous task executes
        - callback: The function that should be called for the synchronous callback once the asynchronous portion of the task finishes
        - delay: The delay, in ticks, that the scheduler should wait before executing the asynchronous task
        - functionArgs: Any arguments that should be passed to the function

        Returns
        - An ID representing the asynchronous task that was scheduled
        """
        ...


    def stopTask(self, taskId: int) -> None:
        """
        Terminate a task with the given task ID via a platform-specific implementation.

        Arguments
        - taskId: The ID of the task to terminate
        """
        ...


    def stopTasks(self, script: "Script") -> None:
        """
        Terminate all scheduled tasks belonging to a script via a platform-specific implementation.

        Arguments
        - script: The script whose scheduled tasks should be terminated
        """
        ...


    def getTask(self, taskId: int) -> "Task":
        """
        Get a scheduled task from its ID.

        Arguments
        - taskId: The task ID

        Returns
        - The scheduled task associated with the task ID, null if no task was found with the given ID
        """
        ...


    def getTasks(self, script: "Script") -> list["Task"]:
        """
        Get all scheduled tasks associated with a script.

        Arguments
        - script: The script whose scheduled tasks should be gotten

        Returns
        - An immutable list containing all scheduled tasks associated with the script. Returns null if the script has no scheduled tasks
        """
        ...


    @staticmethod
    def get() -> "TaskManager":
        ...
