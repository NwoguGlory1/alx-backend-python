#!/usr/bin/env python3
""" A script about async comprehension """

import asyncio
import random
from typing import AsyncGenerator, Generator
async_generator = __import__('0-async_generator').async_generator
"""
imports asyncio, random  modules,
generator, async_generator function
"""


async def async_comprehension() -> List[float]:
    """
    An async comprehension coroutine that takes no argument,
    collects random numbers from imported async_generator
    function, then returns the random numbers
    """
    random_nums = [random_num async for random_num in async_generator()]
    return random_nums
