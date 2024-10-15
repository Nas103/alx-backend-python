#!/usr/bin/env python3
import asyncio
from typing import List
from 0-basic_async_syntax import wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    # List of asyncio tasks
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    
    # Gather results as tasks complete (without using sort)
    delays = [await task for task in asyncio.as_completed(tasks)]
    
    return delays