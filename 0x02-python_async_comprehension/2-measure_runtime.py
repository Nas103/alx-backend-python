#!/usr/bin/env python3
import asyncio

from .1_async_comprehension import async_comprehension  # Import from previous task

async def measure_runtime():
    """
    Measures the total runtime of executing async_comprehension four times
    in parallel using asyncio.gather.

    Explanation:

    - While the individual async_generator coroutines might each take roughly
      one second to complete due to the one-second sleep, the total runtime
      when running them in parallel is not necessarily four seconds. This is
      because Python's Global Interpreter Lock (GIL) prevents true parallel
      execution of CPU-bound tasks like the random number generation.
      - asyncio can manage I/O-bound tasks efficiently with concurrency, but
        CPU-bound tasks are serialized by the GIL.
      - Therefore, the total runtime often reflects the time it takes to
        complete the slowest of the four parallel async_comprehension calls,
        which can be close to, but not exactly, four seconds in practice.
    """

    start_time = asyncio.get_running_loop().time()
    await asyncio.gather(*[async_comprehension() for _ in range(4)])
    end_time = asyncio.get_running_loop().time()

    return end_time - start_time