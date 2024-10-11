#!/usr/bin/env python3
from typing import Tuple, List


def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> List[int]:
    """
    Zooms into an array by repeating each element based on a factor.

    Args:
        lst: Tuple containing elements to be repeated.
        factor: The number of times each element is repeated (default is 2).

    Returns:
        A list containing the zoomed elements.
    """
    zoomed_in: List[int] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
