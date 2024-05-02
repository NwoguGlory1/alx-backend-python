#!/usr/bin/env python3
""" Shebang that tells OS to execute as python script"""
from typing import TypeVar, Mapping, Any, Union
""" imports these modules"""

T = TypeVar('T')


def safely_get_value(dct: Mapping[Any, T], key: Any, default: Union[T, None] = None) ->
    Union[T, None]:
    """
    Safely retrieves a value from a dictionary by key, returning a default value if the key is not found.

    Parameters:
    dct (Mapping[Any, T]): A dictionary where keys are of any type
    and values are of type T.
    key (Any): The key to retrieve from the dictionary.
    default (Union[T, None], optional): The default value to return
    if the key is not found. Defaults to None.

    Returns:
    Union[T, None]: The value associated with the key if it exists in the dictionary, or the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
