#!/usr/bin/env python3
""" Asynchrous coroutine that takes in an integer arg"""

import asyncio
import random
""" imports asyncio, random module """

async def wait_random(max_delay=10):
    """ defines the async wait_random function """
    delay = random.randint(0, max_delay)
    await asyncio.sleep(delay)
    return delay
