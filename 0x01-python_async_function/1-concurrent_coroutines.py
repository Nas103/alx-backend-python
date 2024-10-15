#!/usr/bin/env python3
"""
Module that contains the wait_n coroutine
"""

"""
    Spawns wait_random n times with the specified max_delay
    and returns the list of all the delays (float values)
    in ascending order.
    """

import asyncio
from typing import List
from 0-basic_async_syntax import wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:

    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delays = [await task for task in asyncio.as_completed(tasks)]
    return delays