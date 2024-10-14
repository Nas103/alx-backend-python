#!/usr/bin/env python3
"""Create a task for wait_random."""

import asyncio
from 0_basic_async_syntax import wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Return an asyncio.Task that waits for a random delay.
    Args:
        max_delay (int): The maximum delay.
    Returns:
        asyncio.Task: A task waiting for a random delay.
    """
    return asyncio.create_task(wait_random(max_delay))
