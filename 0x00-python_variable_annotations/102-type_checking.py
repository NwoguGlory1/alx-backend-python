#!/usr/bin/env python3
""" Shebang that tells OS to execute as python script"""
from typing import List, Tuple
""" imports List, Tuple"""


def zoom_array(lst: List[int], factor: int = 2) -> List[int]:
    zoomed_in: List[int] = [
        item for item in lst
        for _ in range(factor)
    ]
    return zoomed_in
