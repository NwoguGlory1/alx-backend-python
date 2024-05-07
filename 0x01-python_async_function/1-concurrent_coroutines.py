#!/usr/bin/env python3
""" Asynchrous coroutine that executes multiple coroutine """

import asyncio
import random
from typing import List
""" imports asyncio, random module """
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    spawn wait_random n times with the specified max_delay.
    """
    queue, array = [], []

    for _ in range(n):
        queue.append(wait_random(max_delay))

    for q in asyncio.as_completed(queue):
        result = await q
        array.append(result)

    return array
