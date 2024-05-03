#!/usr/bin/env python3
""" Shebang that tells OS to execute as python script"""
from typing import List, Tuple
""" imports List, Tuple"""


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Zooms an array by a given factor

    Parameters:
    lst (Tuple[int]): A tuple of integers.
    factor (int): The factor by which to zoom the array.

    Returns:
    List[int]: A list containing each element of the input tuple
    repeated by the factor.
    """
    zoomed_in: List = [
        item for item in lst
        for _ in range(factor)
    ]
    return zoomed_in
