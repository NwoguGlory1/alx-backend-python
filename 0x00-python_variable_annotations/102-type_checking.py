#!/usr/bin/env python3
""" Shebang that tells OS to execute as python script"""
from typing import List, Tuple
""" imports List, Tuple"""


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    zoomed_in: List = [
        item for item in lst
        for _ in range(factor)
    ]
    return zoomed_in
