"""
Python module generated from Java source file dev.magicmq.pyspigot.manager.script.RunResult

Java source file obtained from artifact pyspigot version 0.5.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from dev.magicmq.pyspigot.manager.script import *
from enum import Enum
from typing import Any, Callable, Iterable, Tuple


class RunResult(Enum):

    SUCCESS = 0
    """
    Returned if the script loaded successfully.
    """
    FAIL_DISABLED = 1
    """
    Returned if the script was not loaded because it was disabled as per its script options in script_options.yml
    """
    FAIL_DEPENDENCY = 2
    """
    Returned if the script was not loaded because it has missing dependencies.
    """
    FAIL_ERROR = 3
    """
    Returned if the script was loaded but failed during runtime due to an error.
    """
    FAIL_DUPLICATE = 4
    """
    Returned if a script is already loaded with the same name.
    """
