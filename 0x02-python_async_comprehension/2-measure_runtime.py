#!/usr/bin/env python3
"""Module to measure the runtime of parallel async comprehensions."""

import asyncio
import time
from .async_comprehension import async_comprehension


async def measure_runtime() -> float:
    """Execute async_comprehension 4 times in parallel and measure
    the total runtime.
    """
    start = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    total_time = time.perf_counter() - start
    return total_time
