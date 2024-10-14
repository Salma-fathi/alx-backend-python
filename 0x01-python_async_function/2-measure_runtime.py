#!/usr/bin/env python3

"""This module demonstrates asynchronous operations using asyncio."""
import asyncio
import random
from typing import List


async def wait_random(max_delay: int = 10) -> float:
    """Asynchronous coroutine that waits for a random delay."""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


async def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total execution time for wait_n(n, max_delay) and return it.
    """
    start = asyncio.get_event_loop().time()
    await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))
    return asyncio.get_event_loop().time() - start
