"""
In this mission you should check if all elements in the given list are equal.
"""

from typing import List, Any

def all_the_same(elements: List[Any]) -> bool:
    # your code here
    if len(set(elements)) < 2:
        return True
    return False


if __name__ == '__main__':
    print("Example:")
    print(all_the_same([1, 1, 1]))
    print(all_the_same([1, 2, 1]))
    print(all_the_same([1]))
    print(all_the_same([]))