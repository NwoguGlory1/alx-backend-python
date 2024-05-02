#!/usr/bin/env python3
"""
This script demonstrates the use of typing module
to specify type of collection like list.
"""
from typing import List
""" imports typing module"""


def sum_list(input_list: List[float]) -> float:
    """
    The function uses a built-in sum() function to sum
    up all the floats in the input_list.

    Parameters:
    input_list (List[float]): A list of floats.

    Returns:
    float: The sum of all floats in the input_list.
    """

    return sum(input_list)
