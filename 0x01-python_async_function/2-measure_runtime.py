#!/usr/bin/env python3
""" Asynchrous coroutine that executes multiple coroutine """

import asyncio
import random
from typing import List
""" imports asyncio, random module """
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """ Measure the runtime """
    start = time()

    run(wait_n(n, max_delay))

    end = time()

    return (end - start) / n
