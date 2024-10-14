#!/usr/bin/env python3
"""Run multiple coroutines concurrently and return sorted delays."""

import asyncio
from typing import List
from 0_basic_async_syntax import wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn wait_random n times with the specified max_delay and return
    the list of delays in ascending order.
    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (int): The maximum delay for each call.
    Returns:
        List[float]: The list of delays in ascending order.
    """
    delays = await asyncio.gather(
        *(wait_random(max_delay) for _ in range(n))
    )
    return sorted(delays)
