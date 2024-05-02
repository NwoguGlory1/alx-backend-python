#!/usr/bin/env python3
"""
This script demonstrates the use of Union, Tuple type hint from
the typing module to sum variables of different types.
"""
from typing import Union, Tuple
""" imports Union, Tuple """


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Converts a string and a value (either int or float) into a tuple.

    Parameters:
    k (str): The string to be included in the tuple.
    v (Union[int, float]): The value to be squared and included in the tuple.

    Returns:
    Tuple[str, float]: A tuple containing the string and the square of the value.
    """
    return k, v**2
