#!/usr/bin/env python3
""" A script about async generator """

import asyncio
import random
from typing import AsyncGenerator, Generator
""" imports asyncio module """
""" imports random module """


async def async_generator() -> Generator[float, None, None]:
    """
    An async generator that takes no argument,
    yields random numbers between 0 and 10
    after an asynchronous wait of 1 second
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
