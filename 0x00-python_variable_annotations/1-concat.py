#!/usr/bin/env python3
""" Shebang that tells OS to execute as python script"""


def concat(str1: str, str2: str) -> str:
    """
    Concatenates two strings using f-string.

    Parameters:
    str1: The first string.
    str2: The second string.

    Returns:
    A concatenated string: str1str2
    """
    return f"{str1}{str2}"
