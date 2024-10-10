#!/usr/bin/python3
from typing import Callable
"""Defines a function that returns a function that multiplies a float by multiplier."""
def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies a float by multiplier."""
    return lambda x: x * multiplier
