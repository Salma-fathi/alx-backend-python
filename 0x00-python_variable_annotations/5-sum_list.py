#!/usr/bin/python3

"""Type-annotated function sum_list which takes a list input """
from typing import List

def sum_list(input_list: List[float]) -> float:
    """Return the sum of a list of floats."""
    return sum(input_list)
