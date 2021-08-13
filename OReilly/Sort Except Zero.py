"""
 Sort the numbers in an array. But the position of zeros should not be changed.

Input: A List.

Output: An Iterable (tuple, list, iterator ...).
"""

from typing import Iterable

def except_zero(items: list) -> Iterable:
    res = sorted([x for x in items if x != 0])

    for i, v in enumerate(items):
        if v == 0:
            res.insert(i,v)

    return res


if __name__ == '__main__':
    print("Example:")
    print(except_zero([5, 3, 0, 0, 4, 1, 4, 0, 7]))