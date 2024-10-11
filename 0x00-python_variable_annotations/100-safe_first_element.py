#!/usr/bin/env python3
"""
Module: 100-safe_first_element
This module contains a function that returns the first element of a sequence.
"""

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Returns the first element of a sequence, or None if it's empty.
    Args:
        lst (Sequence[Any]): Input sequence.
    Returns:
        Union[Any, None]: First element of lst, or None if lst is empty.
    """
    if lst:
        return lst[0]
    return None
