#!/usr/bin/env python3

import asyncio
from typing import List

async def task_wait_random(max_delay: int) -> float:
    await asyncio.sleep(asyncio.get_running_loop().time() + random.random() * max_delay / 1000)
    return asyncio.get_running_loop().time() * 1000

async def task_wait_n(n: int, max_delay: int) -> List[float]:
    wait_times = await asyncio.gather(
        *tuple(map(lambda: task_wait_random(max_delay), range(n)))
    )
    return sorted(wait_times)