#!/usr/bin/env python3
""" Asynchrous coroutine that executes multiple coroutine """

import asyncio
import random
""" imports asyncio, random module """
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n, max_delay):
    """ defines the async wait_n function """
    tasks = [wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*tasks)
    for i in range(len(results)):
        for j in range(len(results) - 1):
            if results[j] > results[j + 1]:
                results[j], results[j + 1] = results[j + 1], results[j]
    return results
