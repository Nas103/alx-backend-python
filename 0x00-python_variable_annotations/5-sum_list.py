#!/usr/bin/env python3
"""
Module: 5-sum_list
This module contains a function that sums a list of floats.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Returns the sum of a list of floats.
    Args:
        input_list (List[float]): List of float numbers.
    Returns:
        float: Sum of all elements in input_list.
    """
    return sum(input_list)
