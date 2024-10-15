#!/usr/bin/env python3
"""
Module that contains the wait_n coroutine to execute multiple coroutines
"""

import asyncio
from typing import Generator
from basic_async_syntax import wait_random


async def wait_n(n: int, max_delay: int) -> Generator[float, None, None]:
    """
    Spawns wait_random n times with the specified max_delay.
    Yields the delays (float values) in ascending order as they complete.
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]

    # Yield each delay as the tasks are completed
    for task in asyncio.as_completed(tasks):
        yield await task
