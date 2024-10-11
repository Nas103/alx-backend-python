#!/usr/bin/env python3
"""
Module: 6-sum_mixed_list
This module contains a function that sums a mixed list of ints and floats.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Returns the sum of a mixed list of integers and floats.
    Args:
    mxd_lst (List[Union[int, float]]): List of integers and floats.
    Returns:
    float: Sum of all elements in mxd_lst.
    """
    return sum(mxd_lst)
