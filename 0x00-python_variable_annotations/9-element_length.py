#!/usr/bin/env python3
"""annotating a function"""
from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """annotating a function"""
    return [(i, len(i)) for i in lst]
