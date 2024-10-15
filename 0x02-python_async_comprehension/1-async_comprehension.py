#!/usr/bin/env python3
import asyncio

from .0_async_generator import async_generator  # Import from previous task

async def async_comprehension():
    """
    An asynchronous coroutine that collects 10 random numbers using an
    async comprehension over async_generator and returns them as a list.
    """

    random_numbers = [num async for num in async_generator()]
    return random_numbers
