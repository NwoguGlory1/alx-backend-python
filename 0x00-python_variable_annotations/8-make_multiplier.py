#!/usr/bin/env python3
"""
This script demonstrates the use of Union, Tuple type hint from
the typing module to sum variables of different types.
"""
from typing import Callable
""" imports Callable """


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Creates a function that multiplies a float by a given multiplier.

    Parameters:
    multiplier (float): The multiplier to be used in the multiplication.

    Returns:
    Callable[[float], float]: A function that takes a float and
    returns the product of the float and the multiplier.

    """
    def inner_function(value: float) -> float:
        return value * multiplier
    return inner_function
