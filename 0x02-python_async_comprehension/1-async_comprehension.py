#!/usr/bin/env python3
"""Module that defines an async comprehension coroutine."""

import asyncio
from typing import List
from .async_generator import async_generator


async def async_comprehension() -> List[float]:
    """Collect 10 random numbers using an async comprehension
    over async_generator and return the numbers.
    """
    return [i async for i in async_generator()]
