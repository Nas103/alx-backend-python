#!/usr/bin/env python3
"""
Module: 8-make_multiplier
This module contains a function that returns a multiplier function.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by the given multiplier.
    Args:
        multiplier (float): The multiplier value.
    Returns:
        Callable[[float], float]: Function that multiplies by multiplier.
    """
    return lambda x: x * multiplier
