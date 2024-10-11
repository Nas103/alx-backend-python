#!/usr/bin/env python3
from typing import TypeVar, Mapping, Any, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping[Any, T], key: Any,
                     default: Union[T, None] = None) -> Union[T, None]:
    """
    Safely retrieves a value from a dictionary. If the key is not present,
    returns the default value.

    Args:
        dct: Dictionary from which to retrieve a value.
        key: Key to look for in the dictionary.
        default: Value to return if key is not found (defaults to None).

    Returns:
        The value from the dictionary or the default value.
    """
    if key in dct:
        return dct[key]
    return default
