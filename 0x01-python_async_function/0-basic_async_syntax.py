#!/usr/bin/env python3
"""
This module demonstrates asynchronous operations using asyncio.

It includes functions for generating random delays and running
concurrent coroutines.
"""

import asyncio
import random
from typing import List


async def wait_random(max_delay: int = 10) -> float:
    """Waits for a random delay between 0 and max_delay seconds and returns it.

    Args:
        max_delay (int): The maximum delay in seconds. Defaults to 10.

    Returns:
        float: The random delay generated.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawns wait_random n times with the specified max_delay.

    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (int): The maximum delay for each wait_random call.

    Returns:
        List[float]: A list of the delays in ascending order.
    """
    delays = []

    async def append_delay():
        delay = await wait_random(max_delay)
        delays.append(delay)

    await asyncio.gather(*(append_delay() for _ in range(n)))
    return sorted(delays)
