#!/usr/bin/env python3
""" Shebang that tells OS to execute as python script"""
from typing import List, Tuple, Sequence, Iterable
""" imports these"""


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Calculates the length of each element in a list, returns a list of tuples,
    where each tuple contains the element and its length.

    Parameters:
    lst (Iterable[Sequence]): A list of sequences (strings, lists, etc.).

    Returns:
    List[Tuple[Sequence, int]]: A list of tuples, where each tuple contains
    a sequence from the input list and its length.
    """
    return [(i, len(i)) for i in lst]
