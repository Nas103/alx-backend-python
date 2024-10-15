#!/usr/bin/env python3
"""Run multiple tasks concurrently and return sorted delays."""

import asyncio
from typing import List
from 3_tasks import task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn task_wait_random n times and return the list of delays in ascending
    order.
    Args:
        n (int): The number of times to spawn task_wait_random.
        max_delay (int): The maximum delay for each task.
    Returns:
        List[float]: The list of delays in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
