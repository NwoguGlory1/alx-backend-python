#!/usr/bin/env python3
"""
This script demonstrates the use of Union type hint from
the typing module to sum variables of different types.
"""
from typing import List, Union
""" imports List """


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    The function uses sum built-in function to add
    all the integers and floats in the input list.
    There is no need to iterate over the list manually

    Parameters:
    mxd_lst (List[Union[int, float]]): A list of integers and/or floats.

    Returns:
    float: The sum of all integers and floats in the input list.
    """
    return sum(mxd_lst)
