#!/usr/bin/env python3
"""Complex types - functions"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Complex types - functions"""
    def multiplier_func(x: float) -> float:
        return x * multiplier
    return multiplier_func
