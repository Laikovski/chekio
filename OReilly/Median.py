"""
 A median is a numerical value separating the upper half of a sorted array of numbers from the lower half.
 In a list where there are an odd number of entities, the median is the number found in the middle of the array.
 If the array contains an even number of entities, then there is no single middle value, instead the median becomes
 the average of the two numbers found in the middle. For this mission, you are given a non-empty array of natural numbers (X).
 With it, you must separate the upper half of the numbers from the lower half and find the median.

Input: An array as a list of integers.

Output: The median as a float or an integer.


"""
import math
from typing import List

def checkio(data: List[int]) -> [int, float]:

    #replace this for solution
    l = len(data)
    data.sort()

    if l % 2 != 0:
        return data[math.floor(l / 2)]
    else:
        return (data[l // 2 - 1] + data[l // 2]) / 2

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print("Example:")
    print(checkio([1, 2, 3, 4, 5]))
    print(checkio([3, 1, 2, 5, 3]))
    print(checkio([3, 6, 20, 99, 10, 15]))