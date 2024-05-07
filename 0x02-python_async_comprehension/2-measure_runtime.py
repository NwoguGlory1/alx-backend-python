#!/usr/bin/env python3
""" A script about prallel comprehension """

import random
import time
from typing import List
from asyncio import gather

async_comprehension = __import__('1-async_comprehension').async_comprehension
"""
imports random, time, List, gather  modules,
async_comprehension function
"""


async def measure_runtime() -> float:
    """
    An coroutine that takes no argument,
    execute async_comprehension four times
     in parallel using asyncio.gather
    """
    start_time = time.time()
    tasks = [async_comprehension() for i in range(4)]
    await gather(*tasks)
    end_time = time.time()
    total_runtime = end_time - start_time
    return total_runtime
