#!/usr/bin/env python3
"""Measure the execution time of wait_n."""

import time
import asyncio
from 1_concurrent_coroutines import wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total runtime for wait_n and return total_time / n.
    Args:
        n (int): The number of coroutines.
        max_delay (int): The maximum delay for each coroutine.
    Returns:
        float: The average runtime per coroutine.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.time() - start_time
    return total_time / n
