#!/usr/bin/env python3
""" Shebang that tells OS to execute as python script """
from typing import Sequence, Any, Optional


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """
    Safely retrieves the first element of a list

    Parameters:
    lst (Sequence[Any]): A sequence of elements, where the type of elements is unknown.

    Return:
    Optional[Any]: The first element of the list, or
    None if the list is empty.
    """
    if lst:
        return lst[0]
    else:
        return None
