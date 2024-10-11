#!/usr/bin/env python3
"""
# The code snippet you provided is defining a Python function called `to_kv` that takes a string `k` and an integer or float `v` as input arguments. The function is annotated with type hints using the `typing` module to specify the types of the input arguments and the return value.
Complex types - string and int/float to tuple
Write typed-annotated function to_kv that takes str k and an int OR float v
Returns a tuple
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Typed-annotated function
    to_kv
    """
    return (k, v * v)
