"""
 You have a list. Each value from that list can be either a string or an integer. Your task here is to return two values.
 The first one is a concatenation of all strings from the given list. The second one is a sum of all integers from
 the given list.

Input: An array of strings and integers

Output: A list or tuple
"""

from typing import Tuple


def sum_by_types(items: list) -> Tuple[str, int]:
    first = ''
    second = 0
    if len(items) == 0:
        return ("", 0)
    for i in items:
        if type(i) == str:
            first += i
        elif type(i) == int:
            second += i
    return [first, second]


if __name__ == "__main__":
    print("Example:")
    print(sum_by_types([]))

print(sum_by_types([]))
print(sum_by_types(["size", 12, "in", 45, 0]))
print(sum_by_types([1, 2, 3]))