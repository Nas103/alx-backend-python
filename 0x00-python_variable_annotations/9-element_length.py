#!/usr/bin/env python3
"""
Module: 9-element_length
This module contains a function that returns a list of tuples with elements
and their lengths.
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples with elements and their lengths.
    Args:
    lst (Iterable[Sequence]): Iterable of seque
    Returns:
        List[Tuple[Sequence, int]]: List of tuples with sequences and lengths.
    """
    return [(i, len(i)) for i in lst]
