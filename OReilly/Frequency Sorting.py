"""
Your mission is to sort the list by the frequency of numbers
included in it. If a few numbers have an equal frequency -
they should be sorted according to their natural order.
For example: [5, 2, 4, 1, 1, 1, 3] ==> [1, 1, 1, 2, 3, 4, 5]
"""
import collections
from typing import List


def frequency_sorting(numbers: List[int]) -> List[int]:
    return sorted(sorted(numbers), key=lambda x: numbers.count(x), reverse=True)



if __name__ == "__main__":
    print("Example:")
    print(frequency_sorting([1, 2, 3, 4, 5]))
    print(frequency_sorting([99, 99, 55, 55, 10, 55, 21, 21, 10, 10]))
    print(frequency_sorting([3, 4, 11, 13, 11, 4, 4, 7, 3]))