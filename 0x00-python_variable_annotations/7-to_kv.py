#!/usr/bin/env python3
"""
Module: 7-to_kv
This module contains a function that returns a tuple with a string
and the square of a number.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple with a string and the square of an integer/float.
    Args:
    k (str): Input string.
    v (Union[int, float]): Input integer or float.
    Returns:
    Tuple[str, float]: Tuple with string and square of v as a float.
    """
    return (k, float(v ** 2))
