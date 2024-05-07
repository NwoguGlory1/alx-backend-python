#!/usr/bin/env python3
""" A script about async generator """
import asyncio
import random
""" imports these modules """


async def async_generator():
    """ An async generator that takes no argument """
    for i in range(0, 11):
        await asyncio.sleep(1)
        yield random.randint(0, 10)
